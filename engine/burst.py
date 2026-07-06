"""
突发检测（Kleinberg burst detection 的轻量实现）。

对双域学术语料按年份统计术语频率，检测近两年相对历史基线
显著加速的「正在爆发的概念」，作为滚动选题池的前沿雷达——
让 400 篇的滚动竞争对新兴概念（如 context engineering、
computer-use agents）保持敏感，而不是只靠既有关键词。
"""

from __future__ import annotations

import json
import os
import re
from collections import defaultdict

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")
CORPUS_PATH = os.path.join(DATA_DIR, "academic_corpus.json")
OUT_PATH = os.path.join(DATA_DIR, "burst_terms.json")

# 监控术语（英文匹配词 → 中文名），双域覆盖
WATCH_TERMS = {
    "context engineering": "上下文工程",
    "agentic": "agentic 智能体",
    "tool use": "工具使用",
    "function calling": "函数调用",
    "computer use": "计算机操作智能体",
    "multi-agent": "多智能体",
    "agent memory": "智能体记忆",
    "long-horizon": "长程任务",
    "self-reflection": "自我反思",
    "chain-of-thought": "思维链",
    "reasoning model": "推理模型",
    "hallucination": "幻觉",
    "guardrail": "护栏",
    "scaffold": "脚手架",
    "human-in-the-loop": "人在回路",
    "orchestration": "编排",
    "digital therapeutic": "数字疗法",
    "digital phenotyping": "数字表型",
    "wearable": "可穿戴监测",
    "large language model": "大语言模型",
    "executive function": "执行功能",
    "body doubling": "身体在场",
    "cognitive offloading": "认知卸载",
    "time blindness": "时间盲",
    "hyperfocus": "超聚焦",
    "emotion dysregulation": "情绪失调",
    "medication adherence": "服药依从",
    "telehealth": "远程医疗",
}

BASE_YEARS = (2015, 2023)   # 历史基线窗口
BURST_YEARS = (2024, 2027)  # 突发窗口


def detect(corpus: list[dict] | None = None, min_burst_count: int = 8) -> list[dict]:
    if corpus is None:
        if not os.path.exists(CORPUS_PATH):
            return []
        with open(CORPUS_PATH, "r", encoding="utf-8") as f:
            corpus = json.load(f)

    year_totals: dict[int, int] = defaultdict(int)
    counts: dict[str, dict[int, int]] = {t: defaultdict(int) for t in WATCH_TERMS}
    for rec in corpus:
        y = rec.get("year")
        if not isinstance(y, int) or y < BASE_YEARS[0]:
            continue
        year_totals[y] += 1
        text = f"{rec.get('title', '')} {rec.get('abstract', '')}".lower()
        for term in WATCH_TERMS:
            if term in text:
                counts[term][y] += 1

    base_total = sum(v for y, v in year_totals.items() if BASE_YEARS[0] <= y <= BASE_YEARS[1]) or 1
    burst_total = sum(v for y, v in year_totals.items() if BURST_YEARS[0] <= y <= BURST_YEARS[1]) or 1

    out = []
    for term, zh in WATCH_TERMS.items():
        base = sum(v for y, v in counts[term].items() if BASE_YEARS[0] <= y <= BASE_YEARS[1])
        burst = sum(v for y, v in counts[term].items() if BURST_YEARS[0] <= y <= BURST_YEARS[1])
        if burst < min_burst_count:
            continue
        base_rate = base / base_total
        burst_rate = burst / burst_total
        ratio = burst_rate / base_rate if base_rate > 0 else float("inf")
        out.append({
            "term": term,
            "term_zh": zh,
            "base_count": base,
            "burst_count": burst,
            "burst_ratio": round(ratio, 2) if ratio != float("inf") else 999.0,
            "is_bursting": ratio >= 2.0,
        })
    out.sort(key=lambda x: x["burst_ratio"], reverse=True)
    return out


def save(bursts: list[dict]) -> None:
    with open(OUT_PATH, "w", encoding="utf-8") as f:
        json.dump(bursts, f, ensure_ascii=False, indent=1)


def load() -> list[dict]:
    if not os.path.exists(OUT_PATH):
        return []
    with open(OUT_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def topic_candidates(bursts: list[dict] | None = None, limit: int = 12) -> list[dict]:
    """把正在爆发的概念转成前沿选题候选。"""
    bursts = bursts if bursts is not None else load()
    out = []
    for b in bursts:
        if not b.get("is_bursting"):
            continue
        surge = "从零爆发" if b["burst_ratio"] >= 900 else f"频率 {b['burst_ratio']}×"
        out.append({
            "title": f"「{b['term_zh']}」正在学术界爆发（近两年{surge}）——它对 ADHD 意味着什么？",
            "subtitle": f"突发检测：{b['term']} 近两年 {b['burst_count']} 篇 vs 基线 {b['base_count']} 篇。用双域证据解读这个新兴概念的同构意义。",
            "term": b["term_zh"],
        })
        if len(out) >= limit:
            break
    return out


if __name__ == "__main__":
    bursts = detect()
    save(bursts)
    print(f"监控 {len(WATCH_TERMS)} 个术语，检出 {sum(1 for b in bursts if b['is_bursting'])} 个爆发中")
    for b in bursts[:10]:
        flag = "🔥" if b["is_bursting"] else "  "
        print(f" {flag} {b['term_zh']}({b['term']}): {b['burst_ratio']}× ({b['base_count']}→{b['burst_count']})")
