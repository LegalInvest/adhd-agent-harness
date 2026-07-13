"""
STORM 式多视角提问（Stanford STORM 的视角轮）。

STORM 生成 wiki 文章的核心不是检索，而是先模拟多个视角的
专家互相追问再作答。本模块对每个脊柱概念让 LLM 分别扮演
ADHD 患者 / 认知神经科学家 / agent 工程师 / 怀疑论者互相提问，
产出的问题天然带双受众张力，并入问题池参与滚动竞争。
带磁盘缓存：同一脊柱概念不重复调用。
"""

from __future__ import annotations

import json
import os

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")
OUT_PATH = os.path.join(DATA_DIR, "storm_questions.json")

PERSPECTIVES = [
    "确诊多年的成人 ADHD 患者（关心真实生活困境）",
    "认知神经科学家（关心机制与证据边界）",
    "agentic harness 工程师（关心 LLM 编排与可迁移方法）",
    "怀疑论者（专挑同构类比被夸大的地方）",
]

_PROMPT = """你在为「ADHD 大脑 ↔ LLM 同构」内容项目做 STORM 式多视角选题风暴。

脊柱概念：{spine}
ADHD 侧痛点：{pain}
LLM/harness 侧平行机制：{parallel}

请模拟以下 4 个视角的专家围绕这个概念互相追问：
{perspectives}

要求：
- 每个视角提出 2 个问题，共 8 个；
- 问题必须同时勾住 ADHD 人群和 agentic harness 工程师（双受众张力）；
- 问题要具体、锋利、可用双域证据作答，不要空泛；
- 怀疑论者的问题要真实挑战同构类比的边界。

只返回 JSON：{{"questions": [{{"perspective": "视角", "question": "问题", "subtitle": "一句话切入角度"}}]}}"""


def generate(llm, spines: list[dict], force: bool = False) -> list[dict]:
    """对每个脊柱概念生成多视角问题，带磁盘缓存。"""
    cache: dict = {}
    if os.path.exists(OUT_PATH) and not force:
        with open(OUT_PATH, "r", encoding="utf-8") as f:
            cache = json.load(f)

    for spec in spines:
        key = spec["spine"]
        if key in cache:
            continue
        prompt = _PROMPT.format(
            spine=key, pain=spec["pain"], parallel=spec["parallel"],
            perspectives="\n".join(f"- {p}" for p in PERSPECTIVES),
        )
        try:
            data = llm.chat_json([{"role": "user", "content": prompt}], temperature=0.8)
            qs = data.get("questions", []) if isinstance(data, dict) else []
            cache[key] = [
                {"perspective": q.get("perspective", ""), "question": q.get("question", ""),
                 "subtitle": q.get("subtitle", "")}
                for q in qs if q.get("question")
            ]
        except Exception:  # noqa: BLE001 - 单概念失败不阻断
            cache[key] = []
        with open(OUT_PATH, "w", encoding="utf-8") as f:
            json.dump(cache, f, ensure_ascii=False, indent=1)
    return cache


def load() -> dict:
    if not os.path.exists(OUT_PATH):
        return {}
    with open(OUT_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def topic_candidates(spine_meta: dict[str, dict] | None = None) -> list[dict]:
    """把 STORM 问题转成问题池候选。"""
    out = []
    for spine, qs in load().items():
        for q in qs:
            if not q.get("question"):
                continue
            out.append({
                "title": q["question"],
                "subtitle": q.get("subtitle") or f"STORM 视角轮（{q.get('perspective', '')}）提出的双受众问题。",
                "spine": spine,
            })
    return out


if __name__ == "__main__":
    from engine.llm import get_client, is_llm_available
    from engine.problems import SPINE_PROBLEM_SPECS

    if not is_llm_available():
        print("LLM 未配置")
    else:
        cache = generate(get_client(), SPINE_PROBLEM_SPECS)
        total = sum(len(v) for v in cache.values())
        print(f"{len(cache)} 个脊柱概念，共 {total} 个多视角问题")
        for spine, qs in list(cache.items())[:2]:
            print(f"  [{spine}]")
            for q in qs[:3]:
                print(f"    - ({q['perspective'][:10]}) {q['question'][:60]}")
