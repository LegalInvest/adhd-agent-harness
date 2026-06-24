"""
进化晋升机制
通过多轮迭代，淘汰低分选题，用新生成的候选替换，持续优化选题池
"""

import json
import os
from dataclasses import dataclass

from engine.scorer import rank_topics, score_topic, compute_weighted_score


@dataclass
class EvolutionConfig:
    pool_size: int = 400           # 目标选题池大小
    elimination_rate: float = 0.1  # 每轮淘汰比例
    mutation_rate: float = 0.05    # 变异率（标题微调）
    generations: int = 5           # 迭代代数
    elite_ratio: float = 0.1      # 精英保护比例


class TopicEvolution:
    """选题进化引擎"""

    def __init__(self, config: EvolutionConfig | None = None):
        self.config = config or EvolutionConfig()
        self.history: list[dict] = []

    def evolve(
        self,
        topics: list[dict],
        candidate_pool: list[dict] | None = None,
    ) -> list[dict]:
        """
        执行进化过程

        Args:
            topics: 初始选题池
            candidate_pool: 候选替换选题（用于替换被淘汰的选题）

        Returns:
            进化后的最优选题列表
        """
        current = list(topics)
        candidates = list(candidate_pool) if candidate_pool else []

        for gen in range(self.config.generations):
            # 评分并排序
            ranked = rank_topics(current)

            # 记录本代统计
            scores = [t["weighted_score"] for t in ranked]
            gen_stats = {
                "generation": gen + 1,
                "pool_size": len(ranked),
                "avg_score": round(sum(scores) / len(scores), 2),
                "max_score": round(max(scores), 2),
                "min_score": round(min(scores), 2),
                "median_score": round(sorted(scores)[len(scores) // 2], 2),
            }
            self.history.append(gen_stats)

            # 精英保护：top N% 直接晋级
            elite_count = max(1, int(len(ranked) * self.config.elite_ratio))
            elite = ranked[:elite_count]

            # 淘汰底部选题
            eliminate_count = int(len(ranked) * self.config.elimination_rate)

            if candidates and eliminate_count > 0:
                # 有候选池时才真正淘汰
                survivors = ranked[:len(ranked) - eliminate_count]
                scored_candidates = rank_topics(candidates)
                replacements = scored_candidates[:eliminate_count]
                survivors.extend(replacements)
                used_ids = {r.get("id") for r in replacements}
                candidates = [c for c in candidates if c.get("id") not in used_ids]
            else:
                # 没有候选池时，不淘汰，只做排序和变异优化
                survivors = ranked

            # 变异：对部分选题进行标题微调（底部选题变异概率更高）
            mutated = self._mutate(survivors)
            current = mutated

        # 最终排序，取目标数量
        final = rank_topics(current)
        return final[: self.config.pool_size]

    def _mutate(self, topics: list[dict]) -> list[dict]:
        """
        对选题进行轻微变异（标题增强）

        通过添加增强标签来测试不同标题策略的效果
        """
        import hashlib

        enhancers = [
            "（深度指南）", "（实战攻略）", "（完整方案）",
            "（2025最新）", "（亲测有效）", "（收藏必看）",
        ]

        mutated = []
        for topic in topics:
            # 使用确定性方式决定是否变异
            h = hashlib.md5(topic.get("title", "").encode()).hexdigest()
            mutation_chance = int(h[:4], 16) / 0xFFFF

            if mutation_chance < self.config.mutation_rate:
                # 选择增强标签
                idx = int(h[4:6], 16) % len(enhancers)
                enhanced = dict(topic)
                # 只在subtitle后添加增强标签
                enhanced["subtitle"] = topic.get("subtitle", "") + " " + enhancers[idx]
                mutated.append(enhanced)
            else:
                mutated.append(topic)

        return mutated

    def get_evolution_report(self) -> str:
        """生成进化过程报告"""
        lines = ["# 选题进化报告\n"]
        for stats in self.history:
            lines.append(
                f"## 第 {stats['generation']} 代\n"
                f"- 选题池大小: {stats['pool_size']}\n"
                f"- 平均分: {stats['avg_score']}\n"
                f"- 最高分: {stats['max_score']}\n"
                f"- 最低分: {stats['min_score']}\n"
                f"- 中位数: {stats['median_score']}\n"
            )
        return "\n".join(lines)

    def save_history(self, filepath: str) -> None:
        """保存进化历史到JSON文件"""
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(self.history, f, ensure_ascii=False, indent=2)
