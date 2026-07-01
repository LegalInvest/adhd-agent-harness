"""
LLM Wiki 模块 —— 借鉴 Andrej Karpathy 的「LLM Wiki」模式

核心思想（与 RAG 的区别）：
  不是每次都从原始素材里临时检索拼凑，而是让 LLM **增量地构建并维护一个
  持久、互相链接的 wiki**。新素材进来时，LLM 读它、抽取要点、更新已有的
  概念页/工具页、标记与旧结论的矛盾、强化或挑战正在演化的综述。
  知识被「编译」一次后持续保鲜、复利式积累，而不是每次重算。

三层架构：
  1. Raw sources  —— data/scraped_knowledge.json（只读，真理之源）
  2. The Wiki     —— data/wiki/ 下 LLM 维护的互链 markdown 页面（概念/工具/主题 + 综述 + 矛盾）
  3. The Schema   —— data/wiki/WIKI_SCHEMA.md，告诉 LLM 如何维护 wiki

每个页面记录已摄入的素材指纹（ingested_source_hashes），重跑时只对有「新素材」
的页面调用 LLM 修订，从而实现真正的增量、复利累积，而非每次重建。
"""

from __future__ import annotations

import hashlib
import json
import os
import re
from datetime import datetime, timezone

from engine.knowledge import (
    KNOWN_TOOLS,
    CORE_CONCEPTS,
    SPINE_CONCEPTS,
    _split_sentences,
)
from engine.llm import LLMClient

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")
WIKI_DIR = os.path.join(DATA_DIR, "wiki")
INDEX_PATH = os.path.join(WIKI_DIR, "_index.json")

# 主题（按博客分类）综述页：把分散在工具/概念页里的事实编织成「演化中的论点」
TOPIC_PAGES = {
    "ai-tools": "ADHD 的 AI 工具全景",
    "focus": "AI 与 ADHD 的专注力",
    "time-mgmt": "AI 与 ADHD 的时间管理",
    "emotion": "AI 与 ADHD 的情绪调节",
    "learning": "AI 与 ADHD 的学习方式",
    "career": "AI 与 ADHD 的职业发展",
    "science": "ADHD × AI 的科学与研究前沿",
    "lifestyle": "AI 与 ADHD 的日常生活",
}


def _now() -> str:
    return datetime.now(timezone.utc).isoformat()


def _slugify(text: str) -> str:
    s = text.lower()
    s = re.sub(r"[^\w\u4e00-\u9fff\s-]", "", s)
    s = re.sub(r"[\s_]+", "-", s).strip("-")
    return s[:60] or hashlib.md5(text.encode()).hexdigest()[:8]


def _source_hash(text: str) -> str:
    return hashlib.md5(text.encode("utf-8")).hexdigest()[:12]


def gather_excerpts(
    articles: list[dict], terms: list[str], max_excerpts: int = 14, max_len: int = 300
) -> list[dict]:
    """从原始素材中收集提及 terms 的句子（带来源），作为 LLM 合成页面的原料"""
    terms = [t.lower() for t in terms if t]
    excerpts: list[dict] = []
    seen: set[str] = set()
    for a in articles:
        content = a.get("content", "")
        title = a.get("title", "")
        url = a.get("url", "")
        for sent in _split_sentences(content):
            low = sent.lower()
            if 30 < len(sent) < max_len and any(t in low for t in terms):
                key = sent[:48].lower()
                if key in seen:
                    continue
                seen.add(key)
                excerpts.append({
                    "source_title": title,
                    "source_url": url,
                    "text": sent,
                    "domain": a.get("domain", "adhd"),
                })
                if len(excerpts) >= max_excerpts:
                    return excerpts
    return excerpts


def gather_excerpts_balanced(
    articles: list[dict], terms: list[str], per_domain: int = 8
) -> list[dict]:
    """跨域收集摘录：ADHD 域与 harness 域各取若干，供同构脊柱页双端对照。"""
    adhd = [a for a in articles if a.get("domain", "adhd") != "harness"]
    harness = [a for a in articles if a.get("domain") == "harness"]
    ex_a = gather_excerpts(adhd, terms, max_excerpts=per_domain)
    ex_h = gather_excerpts(harness, terms, max_excerpts=per_domain)
    return ex_a + ex_h


# ───────────────────────── Wiki Store ─────────────────────────


class WikiStore:
    """管理 data/wiki/ 目录下的页面与索引（持久化）"""

    def __init__(self):
        self.index: dict = self._load_index()

    def _load_index(self) -> dict:
        if os.path.exists(INDEX_PATH):
            with open(INDEX_PATH, "r", encoding="utf-8") as f:
                return json.load(f)
        return {"pages": {}, "meta": {}}

    def save_index(self) -> None:
        os.makedirs(WIKI_DIR, exist_ok=True)
        with open(INDEX_PATH, "w", encoding="utf-8") as f:
            json.dump(self.index, f, ensure_ascii=False, indent=2)

    @staticmethod
    def _page_path(page_type: str, slug: str) -> str:
        return os.path.join(WIKI_DIR, page_type + "s", slug + ".md")

    def page_key(self, page_type: str, name: str) -> str:
        return f"{page_type}:{name}"

    def get_page(self, page_type: str, name: str) -> dict | None:
        return self.index["pages"].get(self.page_key(page_type, name))

    def read_body(self, entry: dict) -> str:
        path = os.path.join(WIKI_DIR, entry["path"])
        if os.path.exists(path):
            with open(path, "r", encoding="utf-8") as f:
                return f.read()
        return ""

    def write_page(
        self,
        page_type: str,
        name: str,
        body: str,
        summary: str,
        cross_links: list[str],
        ingested_hashes: list[str],
        sources: list[dict],
    ) -> None:
        slug = _slugify(name)
        rel_path = os.path.join(page_type + "s", slug + ".md")
        abs_path = os.path.join(WIKI_DIR, rel_path)
        os.makedirs(os.path.dirname(abs_path), exist_ok=True)
        with open(abs_path, "w", encoding="utf-8") as f:
            f.write(f"# {name}\n\n{body.strip()}\n")
        self.index["pages"][self.page_key(page_type, name)] = {
            "name": name,
            "type": page_type,
            "slug": slug,
            "path": rel_path,
            "summary": summary,
            "cross_links": cross_links,
            "sources": sources,
            "ingested_source_hashes": ingested_hashes,
            "updated_at": _now(),
        }

    def pages_of_type(self, page_type: str) -> list[dict]:
        return [p for p in self.index["pages"].values() if p["type"] == page_type]


# ───────────────────────── Wiki Builder (LLM) ─────────────────────────

SCHEMA_DOC = """# Wiki Schema —— LLM 维护规范

本 wiki 由 LLM 智能体增量维护，遵循 Andrej Karpathy 的「LLM Wiki」模式。

## 三层架构
- **Raw sources**：`data/scraped_knowledge.json` 全网抓取的真实文章（只读，真理之源）。
- **The Wiki**：本目录下的 markdown 页面，全部由 LLM 生成/维护，人类只读。
- **The Schema**：本文件，定义页面结构与维护工作流。

## 页面类型
- `concepts/*.md` —— 核心概念页（执行功能、时间盲、多巴胺…）。
- `tools/*.md` —— 工具页（Lex、Motion、Mem…），含定位、ADHD 适配点、证据、局限。
- `topics/*.md` —— 主题综述页（按分类），编织出「演化中的论点」。
- `_overview.md` —— 全局综述与当前核心论点。
- `_contradictions.md` —— 跨来源的矛盾与存疑点。

## 维护工作流
1. **摄入**：读取新素材摘录，整合进相关页面，而非另起炉灶。
2. **互链**：用 `[[页面名]]` 交叉引用相关概念/工具页。
3. **溯源**：每个关键论断后标注 `（来源：标题）`，页面末尾列出来源链接。
4. **矛盾标记**：当新素材与既有结论冲突时，用 `> ⚠️ 矛盾：…` 显式标注，不要抹平。
5. **复利**：知识只增不重置；每次新素材进来只做增量修订。
"""

CONCEPT_SYS = (
    "你是一个严谨的知识库维护者，正在为「ADHD × AI」主题维护一个互相链接的中文 wiki。"
    "你只能基于给定的真实素材摘录写作，不得编造事实或来源。"
    "语言精炼、专业、可读，面向中文 ADHD 读者。"
)


def _excerpts_block(excerpts: list[dict]) -> str:
    lines = []
    for i, e in enumerate(excerpts, 1):
        lines.append(f"[{i}] （来源：{e['source_title']}）{e['text']}")
    return "\n".join(lines)


SPINE_SYS = (
    "你是一个跨学科的知识库维护者，正在论证一个核心命题："
    "ADHD 大脑与大语言模型（LLM）在结构上是同构的——都是「高产但缺乏可靠执行调度层的生成核心」，"
    "因此给 LLM 套 harness（脚手架）和给 ADHD 搭执行功能支架，是同一类工程。"
    "你只能基于给定的真实摘录写作，区分 [ADHD] 与 [harness] 两端，把对应关系讲清楚，"
    "既要点明结构相似，也要诚实标注'类比在哪里会失效'。语言精炼、专业、面向中文读者。"
)


def _spine_excerpts_block(excerpts: list[dict]) -> str:
    lines = []
    for i, e in enumerate(excerpts, 1):
        tag = "harness" if e.get("domain") == "harness" else "ADHD"
        lines.append(f"[{i}][{tag}]（来源：{e['source_title']}）{e['text']}")
    return "\n".join(lines)


def _spine_json_instructions(
    name: str, kind: str, mirror: str, related: list[str]
) -> str:
    related_str = "、".join(related) if related else "（暂无）"
    return (
        f"请为同构脊柱概念「{name}」撰写/维护 wiki 页面。\n"
        f"对应关系提示：{mirror}\n"
        f"可交叉引用的其它页面（用 [[页面名]] 链接）：{related_str}。\n\n"
        "严格输出 JSON 对象：\n"
        '{\n'
        '  "summary": "1-2 句话点明这个同构对应关系",\n'
        '  "cross_links": ["正文引用到的其它页面名", ...],\n'
        '  "body": "markdown 正文"\n'
        "}\n\n"
        "正文 body 要求：\n"
        "- 用 ## 小节组织，必须包含：『ADHD 一侧』『LLM/harness 一侧』『同构对应』"
        "『工程启示（可迁移的做法）』『类比的边界与反例』；\n"
        "- 关键论断后用「（来源：标题）」标注，只能引用给定摘录里的来源，"
        "并尽量让 ADHD 侧引 [ADHD] 摘录、harness 侧引 [harness] 摘录；\n"
        "- 用 [[页面名]] 交叉引用相关 ADHD 概念页、工具页或其它脊柱页；\n"
        "- 摘录冲突或类比过度时，用 `> ⚠️ 矛盾：…` 显式标注，不要抹平；\n"
        "- 末尾加 `## 来源` 小节列出用到的来源标题；\n"
        "- 不得编造摘录中不存在的数据或来源。"
    )


def _json_instructions(page_kind: str, name: str, related: list[str]) -> str:
    related_str = "、".join(related) if related else "（暂无）"
    return (
        f"请为「{name}」这个{page_kind}撰写/维护 wiki 页面。"
        f"可交叉引用的其它页面（用 [[页面名]] 语法链接）：{related_str}。\n\n"
        "严格输出 JSON 对象，字段如下：\n"
        '{\n'
        '  "summary": "1-2 句话的页面摘要",\n'
        '  "cross_links": ["被你正文引用的其它页面名", ...],\n'
        '  "body": "markdown 正文字符串"\n'
        "}\n\n"
        "正文 body 要求：\n"
        "- 用 ## 小节组织（如：是什么 / 与 ADHD 的关系 / AI 如何介入 / 证据 / 局限与争议）；\n"
        "- 关键论断后用「（来源：标题）」标注，只能引用给定摘录里的来源；\n"
        "- 用 [[页面名]] 交叉引用相关概念或工具；\n"
        "- 若摘录之间存在冲突，用 `> ⚠️ 矛盾：…` 显式标注；\n"
        "- 末尾加 `## 来源` 小节，列出用到的来源标题。\n"
        "- 不要编造摘录中不存在的数据或来源。"
    )


class WikiBuilder:
    def __init__(self, llm: LLMClient, store: WikiStore | None = None):
        self.llm = llm
        self.store = store or WikiStore()

    def _synthesize_page(
        self,
        page_type: str,
        name: str,
        page_kind_label: str,
        excerpts: list[dict],
        related: list[str],
        existing_body: str | None,
    ) -> dict:
        if existing_body:
            user = (
                f"这是「{name}」页面的**现有内容**：\n\n{existing_body}\n\n"
                f"以下是**新摄入的素材摘录**，请把其中的新信息整合进页面，"
                f"保留仍然成立的旧内容，发现矛盾时显式标注：\n\n{_excerpts_block(excerpts)}\n\n"
                + _json_instructions(page_kind_label, name, related)
            )
        else:
            user = (
                f"以下是关于「{name}」的真实素材摘录：\n\n{_excerpts_block(excerpts)}\n\n"
                + _json_instructions(page_kind_label, name, related)
            )
        data = self.llm.chat_json(
            [
                {"role": "system", "content": CONCEPT_SYS},
                {"role": "user", "content": user},
            ],
            temperature=0.4,
            max_tokens=2600,
        )
        if not isinstance(data, dict) or "body" not in data:
            raise ValueError(f"页面 {name} 返回结构异常: {type(data)}")
        return data

    def build_entity_page(
        self,
        page_type: str,
        name: str,
        page_kind_label: str,
        terms: list[str],
        articles: list[dict],
        related: list[str],
    ) -> bool:
        """构建/增量更新一个概念或工具页。返回是否实际调用了 LLM。"""
        excerpts = gather_excerpts(articles, terms)
        if not excerpts:
            return False
        hashes = [_source_hash(e["text"]) for e in excerpts]
        existing = self.store.get_page(page_type, name)
        if existing:
            already = set(existing.get("ingested_source_hashes", []))
            new_hashes = [h for h in hashes if h not in already]
            if not new_hashes:
                return False  # 没有新素材，跳过（复利累积，不重算）
            new_excerpts = [e for e, h in zip(excerpts, hashes) if h not in already]
            existing_body = self.store.read_body(existing)
            data = self._synthesize_page(
                page_type, name, page_kind_label, new_excerpts, related, existing_body
            )
            merged_hashes = sorted(already | set(hashes))
        else:
            data = self._synthesize_page(
                page_type, name, page_kind_label, excerpts, related, None
            )
            merged_hashes = hashes

        sources = []
        seen_urls = set()
        for e in excerpts:
            if e["source_url"] and e["source_url"] not in seen_urls:
                seen_urls.add(e["source_url"])
                sources.append({"title": e["source_title"], "url": e["source_url"]})
        self.store.write_page(
            page_type=page_type,
            name=name,
            body=data["body"],
            summary=data.get("summary", ""),
            cross_links=data.get("cross_links", []),
            ingested_hashes=merged_hashes,
            sources=sources,
        )
        return True

    def build_spine_page(
        self,
        concept: dict,
        articles: list[dict],
        related: list[str],
    ) -> bool:
        """构建/增量更新一个同构脊柱概念页（跨域双端对照）。返回是否调用了 LLM。"""
        name = concept["name"]
        excerpts = gather_excerpts_balanced(articles, concept["terms"])
        if not excerpts:
            return False
        hashes = [_source_hash(e["text"]) for e in excerpts]
        existing = self.store.get_page("concept", name)
        if existing:
            already = set(existing.get("ingested_source_hashes", []))
            if not [h for h in hashes if h not in already]:
                return False  # 无新素材，复利跳过
            new_excerpts = [e for e, h in zip(excerpts, hashes) if h not in already]
            existing_body = self.store.read_body(existing)
            data = self._synthesize_spine_page(
                concept, new_excerpts, related, existing_body
            )
            merged_hashes = sorted(already | set(hashes))
        else:
            data = self._synthesize_spine_page(concept, excerpts, related, None)
            merged_hashes = hashes

        sources, seen_urls = [], set()
        for e in excerpts:
            if e["source_url"] and e["source_url"] not in seen_urls:
                seen_urls.add(e["source_url"])
                sources.append({"title": e["source_title"], "url": e["source_url"]})
        self.store.write_page(
            page_type="concept",
            name=name,
            body=data["body"],
            summary=data.get("summary", ""),
            cross_links=data.get("cross_links", []),
            ingested_hashes=merged_hashes,
            sources=sources,
        )
        return True

    def _synthesize_spine_page(
        self,
        concept: dict,
        excerpts: list[dict],
        related: list[str],
        existing_body: str | None,
    ) -> dict:
        kind = concept.get("kind", "bridge")
        mirror = concept.get("mirror", "")
        prior = (
            f"这是「{concept['name']}」页面的**现有内容**，请把新摘录的信息整合进去、"
            f"保留仍成立的旧内容、发现冲突时显式标注：\n\n{existing_body}\n\n"
            if existing_body else ""
        )
        instruction = _spine_json_instructions(concept["name"], kind, mirror, related)
        user = (
            f"{prior}以下是来自**两个领域**的真实素材摘录——`[ADHD]` 来自 ADHD/神经科学，"
            f"`[harness]` 来自 LLM/agent 工程。请基于它们维护同构脊柱页「{concept['name']}」，"
            f"用结构类比把两端对应起来：\n\n{_spine_excerpts_block(excerpts)}\n\n"
            + instruction
        )
        data = self.llm.chat_json(
            [
                {"role": "system", "content": SPINE_SYS},
                {"role": "user", "content": user},
            ],
            temperature=0.45,
            max_tokens=2800,
        )
        if not isinstance(data, dict) or "body" not in data:
            raise ValueError(f"脊柱页 {concept['name']} 返回结构异常: {type(data)}")
        return data

    def build_topic_page(
        self, category_id: str, name: str, articles: list[dict]
    ) -> bool:
        """构建分类主题综述页：把相关概念页/工具页的摘要编织成演化论点"""
        tool_summaries = [
            f"- [[{p['name']}]]：{p['summary']}"
            for p in self.store.pages_of_type("tool")
            if KNOWN_TOOLS.get(p["name"], {}).get("category") == category_id
        ]
        spine_set = {c["name"] for c in SPINE_CONCEPTS}
        concept_pages = self.store.pages_of_type("concept")
        # 优先放入同构脊柱页，让每个主题综述都从「ADHD↔LLM 同构」脊柱长出来
        spine_pages = [p for p in concept_pages if p["name"] in spine_set]
        other_concepts = [p for p in concept_pages if p["name"] not in spine_set]
        chosen = spine_pages[:6] + other_concepts[:6]
        concept_summaries = [f"- [[{p['name']}]]：{p['summary']}" for p in chosen]
        if not tool_summaries and not concept_summaries:
            return False
        user = (
            f"请撰写主题综述页「{name}」。下面是本 wiki 已有的相关页面摘要，"
            f"请把它们编织成一个有观点、有逻辑的综述。\n"
            f"贯穿全篇的脊柱命题：ADHD 大脑与 LLM 同构——都是「高产但缺执行调度层的生成核心」，"
            f"所以本主题下'AI 帮 ADHD'本质上是'给生成核心套 harness'。请围绕这条脊柱提出"
            f"「当前最站得住脚的核心论点」，并指出仍存争议或证据不足之处。\n\n"
            f"相关工具页：\n{chr(10).join(tool_summaries) or '（无）'}\n\n"
            f"相关概念页（含同构脊柱页）：\n{chr(10).join(concept_summaries) or '（无）'}\n\n"
            "严格输出 JSON：{\"summary\": \"...\", \"cross_links\": [...], \"body\": \"markdown\"}。\n"
            "body 用 ## 小节组织，包含「核心论点」「同构视角」「证据脉络」「仍存争议」四部分，"
            "用 [[页面名]] 交叉引用上面的页面（包括同构脊柱页），不得编造事实。"
        )
        data = self.llm.chat_json(
            [
                {"role": "system", "content": CONCEPT_SYS},
                {"role": "user", "content": user},
            ],
            temperature=0.5,
            max_tokens=2400,
        )
        if not isinstance(data, dict) or "body" not in data:
            return False
        self.store.write_page(
            page_type="topic",
            name=name,
            body=data["body"],
            summary=data.get("summary", ""),
            cross_links=data.get("cross_links", []),
            ingested_hashes=[],
            sources=[],
        )
        return True

    def build_overview_and_contradictions(self) -> None:
        """生成全局综述与矛盾页"""
        page_summaries = [
            f"- [[{p['name']}]]（{p['type']}）：{p['summary']}"
            for p in self.store.index["pages"].values()
            if p["type"] in ("concept", "tool", "topic")
        ]
        block = "\n".join(page_summaries)
        # overview
        ov = self.llm.chat_json(
            [
                {"role": "system", "content": CONCEPT_SYS},
                {
                    "role": "user",
                    "content": (
                        "这是 ADHD × AI wiki 的全部页面摘要：\n\n" + block + "\n\n"
                        "请写一个全局综述页 _overview，提出整个知识库当前的「核心论点」。"
                        "请把『ADHD 大脑与 LLM 同构——都是高产但缺执行调度层的生成核心，"
                        "所以「AI 帮 ADHD」本质是「给生成核心套 harness」』作为统领全局的脊柱命题，"
                        "并给出阅读地图（用 [[页面名]] 链接关键页面，尤其是同构脊柱页）。\n"
                        '严格输出 JSON：{"summary":"...","cross_links":[...],"body":"markdown"}'
                    ),
                },
            ],
            temperature=0.5,
            max_tokens=2200,
        )
        if isinstance(ov, dict) and "body" in ov:
            os.makedirs(WIKI_DIR, exist_ok=True)
            with open(os.path.join(WIKI_DIR, "_overview.md"), "w", encoding="utf-8") as f:
                f.write(f"# 总览：ADHD × AI 知识库\n\n{ov['body'].strip()}\n")
            self.store.index["meta"]["overview_summary"] = ov.get("summary", "")
        # contradictions
        ct = self.llm.chat_json(
            [
                {"role": "system", "content": CONCEPT_SYS},
                {
                    "role": "user",
                    "content": (
                        "基于以下页面摘要，找出 ADHD × AI 领域中**互相矛盾或被夸大/存疑**的说法，"
                        "整理成一个 _contradictions 页面，逐条用 `> ⚠️` 标注，并说明分歧所在。"
                        "如果信息不足以判断，也要诚实说明。\n\n" + block + "\n\n"
                        '严格输出 JSON：{"summary":"...","cross_links":[...],"body":"markdown"}'
                    ),
                },
            ],
            temperature=0.4,
            max_tokens=2000,
        )
        if isinstance(ct, dict) and "body" in ct:
            with open(os.path.join(WIKI_DIR, "_contradictions.md"), "w", encoding="utf-8") as f:
                f.write(f"# 矛盾与存疑\n\n{ct['body'].strip()}\n")
            self.store.index["meta"]["contradictions_summary"] = ct.get("summary", "")


def write_schema_doc() -> None:
    os.makedirs(WIKI_DIR, exist_ok=True)
    with open(os.path.join(WIKI_DIR, "WIKI_SCHEMA.md"), "w", encoding="utf-8") as f:
        f.write(SCHEMA_DOC)


def build_wiki(articles: list[dict], llm: LLMClient, verbose: bool = True) -> WikiStore:
    """
    构建/增量维护整个 LLM Wiki。可重复调用：只对有新素材的页面调用 LLM。
    """
    write_schema_doc()
    store = WikiStore()
    builder = WikiBuilder(llm, store)

    concept_names = list(CORE_CONCEPTS.keys())
    all_tool_names = list(KNOWN_TOOLS.keys())
    core_zh_names = [CORE_CONCEPTS[c].split("（")[0] for c in concept_names]
    spine_names = [c["name"] for c in SPINE_CONCEPTS]

    def _safe(label: str, fn):
        """单页 LLM 合成失败时跳过该页（保留旧版本），不让整次构建崩溃。"""
        try:
            return fn()
        except Exception as e:  # noqa: BLE001 - 单页失败应被隔离
            if verbose:
                print(f"   [skip] {label} 合成失败，保留旧页：{e}")
            return False

    # 1. ADHD 核心概念页（交叉引用里加入脊柱页，让同构脊柱与基础概念双向互链）
    calls = 0
    for cn_en in concept_names:
        zh = CORE_CONCEPTS[cn_en]
        name = zh.split("（")[0]
        terms = [cn_en, name]
        related = [c for c in core_zh_names if c != name][:5]
        related += spine_names[:3]
        related += all_tool_names[:4]
        if _safe(f"concept/{name}",
                 lambda: builder.build_entity_page("concept", name, "ADHD 核心概念", terms, articles, related)):
            calls += 1
            if verbose:
                print(f"   [concept] {name} ✓")
        store.save_index()

    # 1b. 同构脊柱概念页（ADHD ↔ LLM/harness 跨域对照）
    for concept in SPINE_CONCEPTS:
        related = [n for n in spine_names if n != concept["name"]][:5]
        related += core_zh_names[:6]
        related += all_tool_names[:4]
        if _safe(f"spine/{concept['name']}",
                 lambda: builder.build_spine_page(concept, articles, related)):
            calls += 1
            if verbose:
                print(f"   [spine/{concept['kind']}] {concept['name']} ✓")
        store.save_index()

    # 2. 工具页
    for tool_name, info in KNOWN_TOOLS.items():
        terms = [tool_name] + info.get("aliases", [])
        related = [t for t in all_tool_names if t != tool_name][:5]
        related += [CORE_CONCEPTS[c].split("（")[0] for c in concept_names][:5]
        if _safe(f"tool/{tool_name}",
                 lambda: builder.build_entity_page("tool", tool_name, "AI 工具", terms, articles, related)):
            calls += 1
            if verbose:
                print(f"   [tool] {tool_name} ✓")
        store.save_index()

    # 3. 主题综述页
    for cat_id, name in TOPIC_PAGES.items():
        if _safe(f"topic/{name}",
                 lambda: builder.build_topic_page(cat_id, name, articles)):
            calls += 1
            if verbose:
                print(f"   [topic] {name} ✓")
        store.save_index()

    # 4. 全局综述 + 矛盾页
    _safe("overview+contradictions", builder.build_overview_and_contradictions)
    store.save_index()

    spine_set = {c["name"] for c in SPINE_CONCEPTS}
    n_harness = sum(1 for a in articles if a.get("domain") == "harness")
    store.index["meta"].update(
        {
            "source_articles": len(articles),
            "source_adhd": len(articles) - n_harness,
            "source_harness": n_harness,
            "concept_pages": len(store.pages_of_type("concept")),
            "spine_pages": sum(
                1 for p in store.pages_of_type("concept") if p["name"] in spine_set
            ),
            "tool_pages": len(store.pages_of_type("tool")),
            "topic_pages": len(store.pages_of_type("topic")),
            "llm_model": llm.active_model,
            "built_at": _now(),
        }
    )
    store.save_index()
    if verbose:
        print(f"   wiki 构建完成：本次 {calls} 次 LLM 调用，"
              f"共 {len(store.index['pages'])} 个页面")
    return store


# ───────────────────────── Wiki Retriever ─────────────────────────


class WikiRetriever:
    """从已构建的 wiki 中，为某个选题挑选相关页面，喂给文章生成器"""

    def __init__(self, store: WikiStore | None = None):
        self.store = store or WikiStore()

    def _read(self, entry: dict) -> str:
        return self.store.read_body(entry)

    def tool_pages_for_category(self, category_id: str, limit: int = 3) -> list[dict]:
        matched = [
            p for p in self.store.pages_of_type("tool")
            if KNOWN_TOOLS.get(p["name"], {}).get("category") == category_id
        ]
        others = [
            p for p in self.store.pages_of_type("tool")
            if KNOWN_TOOLS.get(p["name"], {}).get("category") != category_id
        ]
        return (matched + others)[:limit]

    def concept_pages_for(self, keywords: list[str], limit: int = 2, offset: int = 0) -> list[dict]:
        kws = [k.lower() for k in keywords]
        pages = self.store.pages_of_type("concept")
        scored = sorted(
            pages,
            key=lambda p: sum(
                1 for k in kws if k in (p["name"] + p["summary"]).lower()
            ),
            reverse=True,
        )
        pool = scored or pages
        if not pool:
            return []
        start = offset % len(pool)
        rotated = pool[start:] + pool[:start]
        return rotated[:limit]

    def topic_page_for(self, category_id: str) -> dict | None:
        name = TOPIC_PAGES.get(category_id)
        if not name:
            return None
        return self.store.get_page("topic", name)

    def context_for_topic(self, topic: dict, offset: int = 0) -> dict:
        """汇总一个选题可用的 wiki 上下文（页面正文 + 摘要 + 来源 + 矛盾）"""
        cat = topic.get("category_id", "")
        kws = topic.get("keywords", []) + [topic.get("angle", "")]
        tool_pages = self.tool_pages_for_category(cat, limit=3)
        concept_pages = self.concept_pages_for(kws, limit=2, offset=offset)
        topic_page = self.topic_page_for(cat)

        def pack(entry):
            return {
                "name": entry["name"],
                "type": entry["type"],
                "summary": entry.get("summary", ""),
                "body": self._read(entry),
                "sources": entry.get("sources", []),
            }

        contradictions_path = os.path.join(WIKI_DIR, "_contradictions.md")
        contradictions = ""
        if os.path.exists(contradictions_path):
            with open(contradictions_path, "r", encoding="utf-8") as f:
                contradictions = f.read()

        return {
            "tools": [pack(p) for p in tool_pages],
            "concepts": [pack(p) for p in concept_pages],
            "topic": pack(topic_page) if topic_page else None,
            "contradictions": contradictions,
        }

    @property
    def available(self) -> bool:
        return len(self.store.index.get("pages", {})) > 0
