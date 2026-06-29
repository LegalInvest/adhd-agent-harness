"""
LLM 客户端（provider-agnostic）

为「LLM Wiki」机制提供统一的大模型调用层：
- 主用 Kimi K2（coding plan，OpenAI 兼容接口），失败自动降级到 DeepSeek
- 内置指数退避重试、JSON 模式辅助、磁盘缓存（同样的请求不重复付费、可复现）

环境变量：
  LLM_API_KEY       主 provider 的 key（必填）
  LLM_BASE_URL      主 provider base_url（默认 https://api.kimi.com/coding/v1）
  LLM_MODEL         主 provider 模型（默认 kimi-latest）
  DEEPSEEK_API_KEY  降级 provider 的 key（可选）
  DEEPSEEK_BASE_URL 降级 base_url（默认 https://api.deepseek.com）
  DEEPSEEK_MODEL    降级模型（默认 deepseek-chat）
  LLM_DISABLE_CACHE 设为 1 时关闭磁盘缓存
"""

from __future__ import annotations

import hashlib
import json
import os
import time
from dataclasses import dataclass

try:
    from openai import OpenAI
except ImportError:  # pragma: no cover
    OpenAI = None

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")
CACHE_DIR = os.path.join(DATA_DIR, "llm_cache")


@dataclass
class Provider:
    name: str
    api_key: str
    base_url: str
    model: str

    @property
    def usable(self) -> bool:
        return bool(self.api_key)


def _providers() -> list[Provider]:
    primary = Provider(
        name="primary",
        api_key=os.environ.get("LLM_API_KEY", ""),
        base_url=os.environ.get("LLM_BASE_URL", "https://api.kimi.com/coding/v1"),
        model=os.environ.get("LLM_MODEL", "kimi-latest"),
    )
    fallback = Provider(
        name="deepseek",
        api_key=os.environ.get("DEEPSEEK_API_KEY", ""),
        base_url=os.environ.get("DEEPSEEK_BASE_URL", "https://api.deepseek.com"),
        model=os.environ.get("DEEPSEEK_MODEL", "deepseek-chat"),
    )
    return [p for p in (primary, fallback) if p.usable]


class LLMError(RuntimeError):
    pass


class LLMClient:
    """带重试、降级和磁盘缓存的轻量 LLM 客户端"""

    def __init__(self, max_retries: int = 4, use_cache: bool = True):
        if OpenAI is None:
            raise LLMError("缺少 openai 库，请先 pip install openai>=1.40.0")
        self.providers = _providers()
        if not self.providers:
            raise LLMError(
                "未配置 LLM 凭证：请设置 LLM_API_KEY（以及可选的 DEEPSEEK_API_KEY）"
            )
        self.max_retries = max_retries
        self.use_cache = use_cache and os.environ.get("LLM_DISABLE_CACHE") != "1"
        self._clients: dict[str, object] = {}
        if self.use_cache:
            os.makedirs(CACHE_DIR, exist_ok=True)

    @property
    def active_model(self) -> str:
        return self.providers[0].model

    def _client_for(self, p: Provider):
        if p.name not in self._clients:
            self._clients[p.name] = OpenAI(api_key=p.api_key, base_url=p.base_url, timeout=120.0)
        return self._clients[p.name]

    @staticmethod
    def _cache_key(model: str, messages: list[dict], temperature: float, json_mode: bool) -> str:
        payload = json.dumps(
            {"m": model, "msgs": messages, "t": temperature, "j": json_mode},
            ensure_ascii=False,
            sort_keys=True,
        )
        return hashlib.sha256(payload.encode("utf-8")).hexdigest()

    def _cache_get(self, key: str) -> str | None:
        if not self.use_cache:
            return None
        path = os.path.join(CACHE_DIR, key + ".json")
        if os.path.exists(path):
            with open(path, "r", encoding="utf-8") as f:
                return json.load(f).get("content")
        return None

    def _cache_put(self, key: str, content: str, model: str) -> None:
        if not self.use_cache:
            return
        path = os.path.join(CACHE_DIR, key + ".json")
        with open(path, "w", encoding="utf-8") as f:
            json.dump({"content": content, "model": model}, f, ensure_ascii=False)

    def chat(
        self,
        messages: list[dict],
        temperature: float = 0.6,
        max_tokens: int = 2400,
        json_mode: bool = False,
    ) -> str:
        """调用 chat completion，返回文本内容。带缓存、重试、跨 provider 降级。"""
        # 缓存键基于"主模型"，保证可复现；降级命中时仍按主模型缓存语义存储
        cache_key = self._cache_key(self.providers[0].model, messages, temperature, json_mode)
        cached = self._cache_get(cache_key)
        if cached is not None:
            return cached

        last_err: Exception | None = None
        for p in self.providers:
            client = self._client_for(p)
            kwargs: dict = {
                "model": p.model,
                "messages": messages,
                "temperature": temperature,
                "max_tokens": max_tokens,
            }
            if json_mode:
                kwargs["response_format"] = {"type": "json_object"}
            for attempt in range(self.max_retries):
                try:
                    resp = client.chat.completions.create(**kwargs)
                    content = (resp.choices[0].message.content or "").strip()
                    if not content:
                        raise LLMError("空响应")
                    self._cache_put(cache_key, content, p.model)
                    return content
                except Exception as e:  # noqa: BLE001 - 需要捕获所有 provider 错误以便降级/重试
                    last_err = e
                    wait = min(2 ** attempt, 20)
                    time.sleep(wait)
            # 当前 provider 多次失败 → 尝试下一个 provider
        raise LLMError(f"所有 provider 调用失败: {last_err}")

    def chat_json(
        self,
        messages: list[dict],
        temperature: float = 0.4,
        max_tokens: int = 2400,
    ) -> dict | list:
        """调用并解析 JSON。容忍模型在 JSON 外包裹 ```json 代码块。"""
        raw = self.chat(messages, temperature=temperature, max_tokens=max_tokens, json_mode=True)
        return _parse_json(raw)


def _parse_json(raw: str):
    raw = raw.strip()
    if raw.startswith("```"):
        raw = raw.split("```", 2)[1] if raw.count("```") >= 2 else raw.strip("`")
        if raw.lstrip().startswith("json"):
            raw = raw.lstrip()[4:]
    raw = raw.strip()
    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        # 尝试截取首个 { ... } 或 [ ... ]
        for opener, closer in (("{", "}"), ("[", "]")):
            start = raw.find(opener)
            end = raw.rfind(closer)
            if start != -1 and end != -1 and end > start:
                try:
                    return json.loads(raw[start : end + 1])
                except json.JSONDecodeError:
                    continue
        raise


def is_llm_available() -> bool:
    return bool(_providers()) and OpenAI is not None


def get_client(**kwargs) -> LLMClient:
    return LLMClient(**kwargs)
