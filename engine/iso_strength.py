"""
同构强度分级（类比 GRADE 之于证据等级）

给每篇文章的「ADHD↔LLM 同构」论证标注强度，回应怀疑论者视角、防止过度类比：

  A 直接文献支撑 —— 引用了直接研究 ADHD↔LLM 认知同构的专题论文
  B 机制类比（双域证据）—— ADHD 侧与 LLM/agent 侧各有真实文献，机制上可映射
  C 仅修辞类比 —— 只有单侧证据或无文献，类比停留在修辞层面
"""

import json
import os

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")
ISO_PAPERS_PATH = os.path.join(DATA_DIR, "isomorphism_papers.json")

_ADHD_MARKERS = [
    "adhd", "attention-deficit", "attention deficit", "hyperactivity",
    "executive function", "working memory", "多动", "注意缺陷",
]
_HARNESS_MARKERS = [
    "llm", "language model", "agent", "transformer", "gpt", "reinforcement",
    "reward", "prompt", "context", "retrieval", "hallucination", "attention head",
    "self-attention", "credit assignment",
]

_iso_titles: set | None = None


def _load_iso_titles() -> set:
    global _iso_titles
    if _iso_titles is None:
        _iso_titles = set()
        try:
            with open(ISO_PAPERS_PATH, "r", encoding="utf-8") as f:
                for p in json.load(f):
                    t = (p.get("title") or "").strip().lower()
                    if t:
                        _iso_titles.add(t)
        except (OSError, json.JSONDecodeError):
            pass
    return _iso_titles


def _hits(text: str, markers: list[str]) -> bool:
    return any(m in text for m in markers)


def grade_iso_strength(sources: list[dict]) -> tuple[str, str]:
    """输入参考来源列表（{title, url}），返回 (等级字母, 标签)。"""
    iso_titles = _load_iso_titles()
    titles = [(s.get("title") or "").lower() for s in sources]

    if any(t in iso_titles for t in titles):
        return "A", "直接文献支撑（引用 ADHD↔LLM 同构专题研究）"

    has_adhd = any(_hits(t, _ADHD_MARKERS) for t in titles)
    has_harness = any(_hits(t, _HARNESS_MARKERS) for t in titles)
    if has_adhd and has_harness:
        return "B", "机制类比（ADHD 侧与 LLM/agent 侧均有真实文献，机制可映射）"

    return "C", "仅修辞类比（缺双域文献支撑，类比停留在修辞层面）"
