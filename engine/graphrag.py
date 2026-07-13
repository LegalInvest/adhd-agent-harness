"""
GraphRAG 式概念图谱 + 社区检测（Microsoft GraphRAG 思路的轻量实现）。

从双域学术语料抽概念共现图（节点=监控概念，边=同摘要共现），
用标签传播做社区检测，自动发现「还没写进脊柱的同构簇」——
比人工定 12 个脊柱概念更能发现盲区。社区可由 LLM 生成摘要，
输出 data/concept_graph.json 供 wiki 与选题参考。
"""

from __future__ import annotations

import json
import os
import random
from collections import defaultdict
from itertools import combinations

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")
CORPUS_PATH = os.path.join(DATA_DIR, "academic_corpus.json")
OUT_PATH = os.path.join(DATA_DIR, "concept_graph.json")

# 概念词典：英文匹配词 → (中文名, 所属域倾向)
CONCEPTS = {
    "executive function": "执行功能", "working memory": "工作记忆",
    "inhibition": "抑制控制", "impulsivity": "冲动性",
    "time perception": "时间感知", "reward": "奖赏系统",
    "dopamine": "多巴胺", "emotion regulation": "情绪调节",
    "mind wandering": "走神", "hyperfocus": "超聚焦",
    "medication": "药物治疗", "digital therapeutic": "数字疗法",
    "wearable": "可穿戴", "comorbidity": "共病",
    "sleep": "睡眠", "procrastination": "拖延",
    "planning": "规划", "task decomposition": "任务分解",
    "memory augmentation": "记忆增强", "retrieval": "检索增强",
    "hallucination": "幻觉", "tool use": "工具使用",
    "multi-agent": "多智能体", "self-reflection": "自我反思",
    "chain-of-thought": "思维链", "context window": "上下文窗口",
    "reinforcement learning": "强化学习", "attention mechanism": "注意力机制",
    "guardrail": "护栏", "human-in-the-loop": "人在回路",
    "orchestration": "编排", "cognitive load": "认知负荷",
    "self-regulation": "自我调节", "feedback": "反馈回路",
    "error correction": "错误纠正", "goal": "目标管理",
}


def build_graph(corpus: list[dict] | None = None, min_edge: int = 5) -> dict:
    if corpus is None:
        if not os.path.exists(CORPUS_PATH):
            return {"nodes": [], "edges": [], "communities": {}}
        with open(CORPUS_PATH, "r", encoding="utf-8") as f:
            corpus = json.load(f)

    node_count: dict[str, int] = defaultdict(int)
    node_domains: dict[str, dict] = defaultdict(lambda: defaultdict(int))
    edge_count: dict[tuple, int] = defaultdict(int)

    for rec in corpus:
        text = f"{rec.get('title', '')} {rec.get('abstract', '')}".lower()
        hits = [c for c in CONCEPTS if c in text]
        dom = rec.get("domain", "")
        for c in hits:
            node_count[c] += 1
            node_domains[c][dom] += 1
        for a, b in combinations(sorted(hits), 2):
            edge_count[(a, b)] += 1

    edges = [
        {"source": a, "target": b, "weight": w}
        for (a, b), w in edge_count.items() if w >= min_edge
    ]

    # 标签传播社区检测
    neighbors: dict[str, list[tuple]] = defaultdict(list)
    for e in edges:
        neighbors[e["source"]].append((e["target"], e["weight"]))
        neighbors[e["target"]].append((e["source"], e["weight"]))
    labels = {n: n for n in neighbors}
    rng = random.Random(42)
    for _ in range(20):
        nodes = list(neighbors)
        rng.shuffle(nodes)
        changed = False
        for n in nodes:
            tally: dict[str, int] = defaultdict(int)
            for nb, w in neighbors[n]:
                tally[labels[nb]] += w
            if tally:
                best = max(tally, key=lambda k: tally[k])
                if labels[n] != best:
                    labels[n] = best
                    changed = True
        if not changed:
            break

    communities: dict[str, list[dict]] = defaultdict(list)
    for n, lab in labels.items():
        doms = node_domains[n]
        communities[lab].append({
            "concept": n, "zh": CONCEPTS[n], "count": node_count[n],
            "adhd": doms.get("adhd", 0), "harness": doms.get("harness", 0),
            "is_bridge": doms.get("adhd", 0) >= 10 and doms.get("harness", 0) >= 10,
        })

    return {
        "nodes": [
            {"concept": c, "zh": CONCEPTS[c], "count": node_count[c],
             "adhd": node_domains[c].get("adhd", 0),
             "harness": node_domains[c].get("harness", 0)}
            for c in sorted(node_count, key=node_count.get, reverse=True)
        ],
        "edges": sorted(edges, key=lambda e: e["weight"], reverse=True),
        "communities": {k: sorted(v, key=lambda x: x["count"], reverse=True)
                        for k, v in communities.items()},
    }


def save(graph: dict) -> None:
    with open(OUT_PATH, "w", encoding="utf-8") as f:
        json.dump(graph, f, ensure_ascii=False, indent=1)


def load() -> dict:
    if not os.path.exists(OUT_PATH):
        return {"nodes": [], "edges": [], "communities": {}}
    with open(OUT_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def bridge_concepts(graph: dict | None = None, min_each: int = 10) -> list[dict]:
    """双域都有充分文献支撑的桥概念（潜在新脊柱候选）。"""
    graph = graph or load()
    return [
        n for n in graph.get("nodes", [])
        if n.get("adhd", 0) >= min_each and n.get("harness", 0) >= min_each
    ]


if __name__ == "__main__":
    g = build_graph()
    save(g)
    print(f"节点 {len(g['nodes'])} / 边 {len(g['edges'])} / 社区 {len(g['communities'])}")
    print("双域桥概念（新脊柱候选）：")
    for n in bridge_concepts(g)[:12]:
        print(f"  {n['zh']}({n['concept']}): ADHD {n['adhd']} / harness {n['harness']}")
    print("最强共现边：")
    for e in g["edges"][:6]:
        print(f"  {CONCEPTS[e['source']]} — {CONCEPTS[e['target']]} ({e['weight']})")
