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
from engine.knowledge import KnowledgeRetriever, KNOWN_TOOLS


@dataclass
class EvolutionConfig:
    pool_size: int = 400            # 目标选题池大小
    elimination_rate: float = 0.08  # 每轮淘汰比例
    generations: int = 5            # 迭代代数
    elite_ratio: float = 0.15       # 精英保护比例


# 基于真实工具/研究角度的新选题模板（用于进化时生成候选）
# 这些模板会和知识库中发现的真实工具组合，产生全新选题
CANDIDATE_TEMPLATES = {
    "ai-tools": [
        ("用 {tool} 解决 ADHD 的{pain}", "实测 {tool} 如何弥补 ADHD 的执行功能缺口", "工具实测"),
        ("{tool} 深度评测：ADHD 用户值得用吗", "从 ADHD 视角全面测评 {tool} 的真实体验", "工具评测"),
        ("ADHD 工作流：把 {tool} 接入你的第二大脑", "用 {tool} 搭建不会遗漏的任务系统", "工作流"),
    ],
    "focus": [
        ("用 {tool} 进入 ADHD 的专注状态", "{tool} 如何帮 ADHD 大脑维持注意力", "专注工具"),
        ("身体在场效应 + {tool}：ADHD 的抗分心组合", "用 {tool} 实践 body doubling 对抗拖延", "方法实践"),
    ],
    "time-mgmt": [
        ("用 {tool} 治好 ADHD 的时间盲", "{tool} 如何让 ADHD「看见」并掌控时间", "时间工具"),
        ("ADHD 自动排程：让 {tool} 替你规划每一天", "{tool} 的 AI 排程如何解决过度承诺", "自动排程"),
    ],
    "emotion": [
        ("用 {tool} 管理 ADHD 的情绪过山车", "{tool} 如何辅助 ADHD 的情绪调节", "情绪工具"),
        ("ADHD 的拒绝敏感性：{tool} 的认知重构辅助", "用 {tool} 练习 CBT 应对 RSD", "心理辅助"),
    ],
    "learning": [
        ("用 {tool} 重塑 ADHD 的学习方式", "{tool} 如何匹配 ADHD 的学习节奏", "学习工具"),
        ("ADHD 的听觉学习法：用 {tool} 把读变成听", "{tool} 如何利用 ADHD 的感官偏好", "学习方法"),
    ],
    "science": [
        ("AI 如何用 EEG 客观诊断 ADHD：最新研究解读", "深度学习模型在 ADHD 诊断上的真实进展", "研究解读"),
        ("AI 眼底/影像识别 ADHD：突破还是炒作", "拆解 ADHD AI 诊断研究的方法学真相", "研究批判"),
        ("从 342 篇论文看 AI×ADHD 研究全景", "全球 AI×ADHD 研究热点、趋势与临床应用", "研究综述"),
    ],
    "career": [
        ("用 {tool} 放大 ADHD 在职场的优势", "{tool} 如何让 ADHD 的特质成为职场资产", "职场工具"),
    ],
    "entrepreneurship": [
        ("ADHD 创业者用 {tool} 补齐执行短板", "{tool} 如何成为 ADHD 创业者的运营外挂", "创业工具"),
    ],
    "parenting": [
        ("用 {tool} 支持 ADHD 孩子的学习", "家长如何用 {tool} 为 ADHD 孩子搭建支持系统", "育儿工具"),
    ],
    "lifestyle": [
        ("用 {tool} 建立 ADHD 友好的日常例程", "{tool} 如何把混乱的日常变成可执行系统", "生活工具"),
    ],
    "community": [
        ("用 {tool} 连接 ADHD 互助社区", "{tool} 如何帮 ADHD 找到同伴支持", "社区工具"),
    ],
}

PAIN_BY_CATEGORY = {
    "ai-tools": "任务启动困难",
    "focus": "注意力涣散",
    "time-mgmt": "时间盲",
    "emotion": "情绪失调",
    "learning": "学习半途而废",
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
        从知识库中发现的真实工具 + 研究角度生成新选题候选
        这是"涌入新发现"的核心：候选完全来自全网最新情报
        """
        candidates = []
        # 按分类用真实工具填充模板
        tools_by_cat: dict[str, list[str]] = {}
        for name, info in KNOWN_TOOLS.items():
            tools_by_cat.setdefault(info["category"], []).append(name)

        for cat_id, templates in CANDIDATE_TEMPLATES.items():
            tools = tools_by_cat.get(cat_id, list(KNOWN_TOOLS.keys())[:3])
            for tmpl_title, tmpl_sub, angle in templates:
                for tool in tools:
                    if "{tool}" in tmpl_title:
                        title = tmpl_title.format(tool=tool, pain=PAIN_BY_CATEGORY.get(cat_id, "日常挑战"))
                        subtitle = tmpl_sub.format(tool=tool)
                    else:
                        title = tmpl_title
                        subtitle = tmpl_sub
                    if title in existing_titles:
                        continue
                    existing_titles.add(title)
                    candidates.append({
                        "id": f"evolved-{cat_id}-{len(candidates):03d}",
                        "title": title,
                        "subtitle": subtitle,
                        "angle": angle,
                        "category_id": cat_id,
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
