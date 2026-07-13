"""
进化晋升机制（研究驱动版）
核心理念：每一代进化都从最新情报中挖掘"新选题候选"，
用真实工具、真实研究角度生成新选题，去替换得分最低的旧选题。
这才是真正的"更好的留下，差的被替换"——而且替换品来自全网最新发现。
"""

import json
import os
from dataclasses import dataclass

from engine.scorer import rank_topics
from engine.knowledge import KnowledgeRetriever, KNOWN_TOOLS, SPINE_CONCEPTS


@dataclass
class EvolutionConfig:
    pool_size: int = 400            # 目标选题池大小
    elimination_rate: float = 0.08  # 每轮淘汰比例
    generations: int = 5            # 迭代代数
    elite_ratio: float = 0.15       # 精英保护比例


# 进化挑战者（challenger）模板：问题驱动 + 双受众张力。
# 每个挑战者都把一个（可能新发现的）工具，包进一条「ADHD↔LLM 同构」的病毒钩子里，
# 让它能和种子问题池公平竞争——只有真正同时勾住两端的，才挤得进 Top 400。
CHALLENGER_TEMPLATES = [
    ("{tool} 之于 ADHD，就像 {parallel} 之于 LLM——但有人用错了",
     "从同构视角实测 {tool}：它到底补上了哪一层执行功能？", "工具×同构"),
    ("我把 {tool} 当作 ADHD 大脑的「外部 harness」用了 30 天",
     "{tool} 解决{pain}的真实收益与「拐杖化」代价。", "亲历实测"),
    ("为什么用 {tool} 治 ADHD 的{pain}，和给 agent 套 {parallel} 是一回事？",
     "{tool} 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。", "反直觉同构"),
]

# 分类 → 默认脊柱 + ADHD 痛点 + harness 对应（给挑战者打 spine 标签）
CATEGORY_SPINE = {
    "ai-tools": ("工具使用与认知卸载", "任务启动困难", "function calling 工具调用"),
    "focus": ("上下文工程", "注意力涣散", "上下文工程"),
    "time-mgmt": ("规划循环与任务分解", "时间盲", "planner-executor 任务分解"),
    "emotion": ("拐杖与脚手架", "情绪失调", "会褪去的脚手架"),
    "learning": ("无状态与外部记忆", "学习半途而废", "外部记忆/向量库"),
    "science": ("ADHD 大脑与 LLM 的同构", "想理解自己的大脑", "生成核心 + 缺失的执行层"),
    "career": ("生成核心与调度层", "卡在执行与落地", "外部编排调度层"),
    "entrepreneurship": ("生成核心与调度层", "想法落地难", "外部编排调度层"),
    "parenting": ("人在回路与身体在场", "不知哪些方法有用", "human-in-the-loop 监督"),
    "lifestyle": ("采样温度与表现波动", "日常混乱不稳定", "调低采样温度"),
    "community": ("人在回路与身体在场", "感到孤立缺问责", "human-in-the-loop 监督"),
}


class TopicEvolution:
    """选题进化引擎：每代从最新情报生成候选并替换低分选题"""

    def __init__(self, config: EvolutionConfig | None = None, retriever: KnowledgeRetriever | None = None):
        self.config = config or EvolutionConfig()
        self.retriever = retriever
        self.history: list[dict] = []
        self.replacement_log: list[dict] = []

    def _generate_candidates(self, existing_titles: set[str]) -> list[dict]:
        """
        生成问题驱动 + 双受众张力的挑战者候选池。

        两个来源：
        1. 问题池（problems.generate_problem_pool）——成千上万条「同时勾住 ADHD 人群
           和 Agentic Harness 工程师」的问题驱动选题，每条带 spine 同构脊柱标注。
        2. 工具 × 同构钩子（CHALLENGER_TEMPLATES）——把（可能新发现的）真实工具包进
           「ADHD↔LLM 同构」病毒钩子，让新工具也能公平竞争 Top 400。

        只有真正同时勾住两端、且有双域证据支撑的，才在评分中挤得进 Top 400。
        """
        from engine.problems import generate_problem_pool

        candidates: list[dict] = []

        # 1. 问题驱动的大候选池（数千条）
        for p in generate_problem_pool():
            if p["title"] in existing_titles:
                continue
            existing_titles.add(p["title"])
            c = dict(p)
            c["is_evolved"] = True
            candidates.append(c)

        # 2. 工具 × 同构钩子挑战者（让真实工具进入竞争）
        tools = list(KNOWN_TOOLS.keys())
        for cat_id, (spine, pain, parallel) in CATEGORY_SPINE.items():
            for tool in tools:
                for tmpl_title, tmpl_sub, angle in CHALLENGER_TEMPLATES:
                    title = tmpl_title.format(tool=tool, pain=pain, parallel=parallel)
                    if title in existing_titles:
                        continue
                    existing_titles.add(title)
                    candidates.append({
                        "id": f"evolved-{cat_id}-{len(candidates):04d}",
                        "title": title,
                        "subtitle": tmpl_sub.format(tool=tool, pain=pain, parallel=parallel),
                        "angle": angle,
                        "category_id": cat_id,
                        "problem": title,
                        "spine": spine,
                        "adhd_pain": pain,
                        "harness_parallel": parallel,
                        "is_problem_driven": True,
                        "is_evolved": True,
                    })
        return candidates

    def evolve(self, topics: list[dict], categories=None) -> list[dict]:
        """
        执行进化过程

        每一代：
        1. 用研究驱动的评分器对当前池排序
        2. 保护精英选题
        3. 淘汰底部低分选题
        4. 从最新情报生成的候选中挑选高分选题替换
        """
        # 补全候选选题的分类元数据
        cat_map = {}
        if categories:
            cat_map = {c.id: c for c in categories}

        def enrich(t: dict) -> dict:
            cat = cat_map.get(t.get("category_id"))
            if cat:
                t.setdefault("category_name", cat.name)
                t.setdefault("category_name_en", cat.name_en)
                t.setdefault("keywords", cat.keywords)
            return t

        current = [enrich(dict(t)) for t in topics]
        existing_titles = {t["title"] for t in current}
        candidate_pool = [enrich(c) for c in self._generate_candidates(existing_titles)]

        for gen in range(self.config.generations):
            ranked = rank_topics(current, retriever=self.retriever)
            scores = [t["weighted_score"] for t in ranked]
            gen_stats = {
                "generation": gen + 1,
                "pool_size": len(ranked),
                "avg_score": round(sum(scores) / len(scores), 2),
                "max_score": round(max(scores), 2),
                "min_score": round(min(scores), 2),
                "median_score": round(sorted(scores)[len(scores) // 2], 2),
                "candidates_available": len(candidate_pool),
                "replaced": 0,
            }

            elite_count = max(1, int(len(ranked) * self.config.elite_ratio))
            eliminate_count = int(len(ranked) * self.config.elimination_rate)

            if candidate_pool and eliminate_count > 0:
                survivors = ranked[: len(ranked) - eliminate_count]
                eliminated = ranked[len(ranked) - eliminate_count:]
                # 候选评分排序
                scored_candidates = rank_topics(candidate_pool, retriever=self.retriever)
                # 只用比被淘汰者更优的候选替换
                replacements = scored_candidates[:eliminate_count]
                actual_replacements = []
                for repl, elim in zip(replacements, eliminated):
                    if repl["weighted_score"] >= elim["weighted_score"]:
                        actual_replacements.append(repl)
                        self.replacement_log.append({
                            "generation": gen + 1,
                            "out": {"title": elim["title"], "score": elim["weighted_score"]},
                            "in": {"title": repl["title"], "score": repl["weighted_score"]},
                        })
                    else:
                        # 候选不够好，保留原选题
                        actual_replacements.append(elim)
                survivors.extend(actual_replacements)
                gen_stats["replaced"] = len([r for r in self.replacement_log if r["generation"] == gen + 1])
                used_ids = {r.get("id") for r in actual_replacements}
                candidate_pool = [c for c in candidate_pool if c.get("id") not in used_ids]
                current = survivors
            else:
                current = ranked

            self.history.append(gen_stats)

        final = rank_topics(current, retriever=self.retriever)
        return final[: self.config.pool_size]

    def get_evolution_report(self) -> str:
        lines = ["# 选题进化报告\n"]
        for stats in self.history:
            lines.append(
                f"## 第 {stats['generation']} 代\n"
                f"- 选题池大小: {stats['pool_size']}\n"
                f"- 平均分: {stats['avg_score']}\n"
                f"- 最高分: {stats['max_score']}\n"
                f"- 最低分: {stats['min_score']}\n"
                f"- 本代替换: {stats['replaced']} 个低分选题\n"
            )
        return "\n".join(lines)

    def save_history(self, filepath: str) -> None:
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        data = {"generations": self.history, "replacements": self.replacement_log}
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
