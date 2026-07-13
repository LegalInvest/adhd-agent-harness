"""
LBD 同构对挖掘器（Swanson ABC 文献发现）。

Swanson (1986) 范式：两个互不引用的文献群 A（ADHD）与 C（agentic harness），
通过共享的中间机制概念 B（执行功能/工作记忆/注意调度…）隐性连接，
构成「未被发现的公共知识」。本模块在双域学术语料上系统性挖掘
A↔B↔C 同构对候选，每一对都是潜在的脊柱证据与选题素材。
"""

from __future__ import annotations

import json
import os
import re

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")
CORPUS_PATH = os.path.join(DATA_DIR, "academic_corpus.json")
OUT_PATH = os.path.join(DATA_DIR, "lbd_pairs.json")

# 中间机制概念 B：每条含英文匹配词 + 中文名 + 对应脊柱概念
BRIDGE_TERMS = [
    {"b": "executive function", "alts": ["executive control", "executive dysfunction"],
     "zh": "执行功能", "spine": "外部执行功能层"},
    {"b": "working memory", "alts": ["memory capacity", "memory interference"],
     "zh": "工作记忆", "spine": "无状态与外部记忆"},
    {"b": "attention allocation", "alts": ["attention control", "selective attention", "sustained attention"],
     "zh": "注意调度", "spine": "上下文工程"},
    {"b": "inhibition", "alts": ["inhibitory control", "response inhibition", "impulsivity"],
     "zh": "抑制控制", "spine": "幻觉与验证循环"},
    {"b": "task decomposition", "alts": ["task switching", "task planning", "planning"],
     "zh": "任务分解与规划", "spine": "规划循环与任务分解"},
    {"b": "goal maintenance", "alts": ["goal-directed", "goal neglect", "goal drift"],
     "zh": "目标维持", "spine": "重锚定与目标漂移"},
    {"b": "reward", "alts": ["dopamine", "reinforcement", "motivation"],
     "zh": "奖赏与动机", "spine": "采样温度与表现波动"},
    {"b": "time perception", "alts": ["temporal processing", "time estimation", "time blindness"],
     "zh": "时间感知", "spine": "外部执行功能层"},
    {"b": "error monitoring", "alts": ["error detection", "self-monitoring", "verification"],
     "zh": "错误监控与验证", "spine": "幻觉与验证循环"},
    {"b": "cognitive load", "alts": ["cognitive offloading", "mental effort"],
     "zh": "认知负荷与卸载", "spine": "工具使用与认知卸载"},
    {"b": "distraction", "alts": ["mind wandering", "distractibility", "off-task"],
     "zh": "分心与走神", "spine": "上下文工程"},
    {"b": "self-regulation", "alts": ["self-control", "self-monitoring", "metacognition"],
     "zh": "自我调节与元认知", "spine": "人在回路与身体在场"},
]


def _matches(text: str, spec: dict) -> bool:
    t = text.lower()
    if spec["b"] in t:
        return True
    return any(a in t for a in spec["alts"])


def mine_pairs(corpus: list[dict] | None = None, top_per_bridge: int = 5) -> list[dict]:
    """对每个 B 概念，取两域引用数最高的论文配成 A↔B↔C 同构对候选。"""
    if corpus is None:
        if not os.path.exists(CORPUS_PATH):
            return []
        with open(CORPUS_PATH, "r", encoding="utf-8") as f:
            corpus = json.load(f)

    pairs = []
    used: set[str] = set()  # 跨 bridge 去重，保证代表作多样性
    for spec in BRIDGE_TERMS:
        by_domain: dict[str, list[dict]] = {"adhd": [], "harness": []}
        for rec in corpus:
            dom = rec.get("domain")
            if dom not in by_domain:
                continue
            text = f"{rec.get('title', '')} {rec.get('abstract', '')}"
            if _matches(text, spec):
                by_domain[dom].append(rec)
        for dom in by_domain:
            by_domain[dom].sort(key=lambda r: r.get("cited_by") or 0, reverse=True)
            by_domain[dom] = [r for r in by_domain[dom] if r.get("id") not in used]
        n = min(top_per_bridge, len(by_domain["adhd"]), len(by_domain["harness"]))
        for i in range(n):
            a, c = by_domain["adhd"][i], by_domain["harness"][i]
            used.add(a.get("id"))
            used.add(c.get("id"))
            pairs.append({
                "bridge": spec["b"],
                "bridge_zh": spec["zh"],
                "spine": spec["spine"],
                "adhd_support": len(by_domain["adhd"]),
                "harness_support": len(by_domain["harness"]),
                "adhd_paper": {k: a.get(k) for k in ("title", "year", "venue", "url", "cited_by")},
                "harness_paper": {k: c.get(k) for k in ("title", "year", "venue", "url", "cited_by")},
                "score": (a.get("cited_by") or 0) + (c.get("cited_by") or 0),
            })
    pairs.sort(key=lambda p: p["score"], reverse=True)
    return pairs


def save_pairs(pairs: list[dict]) -> None:
    with open(OUT_PATH, "w", encoding="utf-8") as f:
        json.dump(pairs, f, ensure_ascii=False, indent=1)


def load_pairs() -> list[dict]:
    if not os.path.exists(OUT_PATH):
        return []
    with open(OUT_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def as_articles(pairs: list[dict] | None = None, limit: int = 40) -> list[dict]:
    """把同构对转成语料条目，供知识萃取与 wiki 取材。"""
    pairs = pairs if pairs is not None else load_pairs()
    out = []
    for p in pairs[:limit]:
        a, c = p["adhd_paper"], p["harness_paper"]
        content = (
            f"Swanson 文献发现（LBD）同构对：中间机制概念「{p['bridge_zh']}（{p['bridge']}）」"
            f"同时被 ADHD 文献群（{p['adhd_support']} 篇命中）与 agentic harness 文献群"
            f"（{p['harness_support']} 篇命中）研究，但两群几乎零互引——构成未被发现的公共知识。\n"
            f"ADHD 侧代表作：{a['title']}（{a.get('venue') or '—'}, {a.get('year')}, 被引 {a.get('cited_by')}，{a.get('url')}）\n"
            f"harness 侧代表作：{c['title']}（{c.get('venue') or '—'}, {c.get('year')}, 被引 {c.get('cited_by')}，{c.get('url')}）\n"
            f"对应脊柱概念：{p['spine']}。"
        )
        out.append({
            "title": f"LBD同构对：{p['bridge_zh']} — {a['title'][:60]} ↔ {c['title'][:60]}",
            "content": content,
            "content_length": len(content),
            "url": a.get("url") or "",
            "source_title": "Swanson LBD 同构对挖掘",
            "domain": "bridge",
            "is_academic": True,
            "is_lbd_pair": True,
        })
    return out


def topic_candidates(pairs: list[dict] | None = None, limit: int = 24) -> list[dict]:
    """把最强同构对转成问题驱动选题候选。"""
    pairs = pairs if pairs is not None else load_pairs()
    seen, out = set(), []
    for p in pairs:
        if p["bridge_zh"] in seen:
            continue
        seen.add(p["bridge_zh"])
        out.append({
            "title": f"两个互不引用的领域都在研究「{p['bridge_zh']}」——ADHD 文献和 LLM harness 文献为什么得出了同一个结论？",
            "subtitle": f"Swanson 文献发现：{p['adhd_support']} 篇 ADHD 论文 ↔ {p['harness_support']} 篇 harness 论文共享机制「{p['bridge']}」，双域代表作对照解读。",
            "spine": p["spine"],
            "bridge": p["bridge_zh"],
        })
        if len(out) >= limit:
            break
    return out


if __name__ == "__main__":
    pairs = mine_pairs()
    save_pairs(pairs)
    print(f"挖出同构对 {len(pairs)} 组")
    for p in pairs[:6]:
        print(f"  [{p['score']}] {p['bridge_zh']}: {p['adhd_paper']['title'][:50]} ↔ {p['harness_paper']['title'][:50]}")
