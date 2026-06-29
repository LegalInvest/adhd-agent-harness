"""
多维度选题评分系统（研究驱动版）
评分不再依赖随机数，而是基于真实信号：
- 知识库证据覆盖（有多少真实研究/工具/策略支撑这个选题）
- SEO 关键词强度（基于真实高搜索量词表）
- 跨平台传播特征（标题结构、列表型、情感词）
- 内容深度潜力（可写的真实素材丰富度）
"""

import re
from dataclasses import dataclass

from engine.knowledge import KnowledgeRetriever


@dataclass
class ScoreDimensions:
    seo_potential: float        # SEO潜力 (1-10)
    cross_platform: float       # 跨平台吸引力 (1-10)
    evidence_strength: float    # 证据强度：有多少真实研究/数据支撑 (1-10)
    practical_value: float      # 实用价值 (1-10)
    emotional_resonance: float  # 情感共鸣 (1-10)
    share_potential: float      # 分享潜力 (1-10)

    def to_dict(self) -> dict:
        return {
            "seo_potential": round(self.seo_potential, 2),
            "cross_platform": round(self.cross_platform, 2),
            "evidence_strength": round(self.evidence_strength, 2),
            "practical_value": round(self.practical_value, 2),
            "emotional_resonance": round(self.emotional_resonance, 2),
            "share_potential": round(self.share_potential, 2),
        }


# 评分权重：证据强度被赋予最高权重，体现"事实驱动"理念
DEFAULT_WEIGHTS = {
    "seo_potential": 0.18,
    "cross_platform": 0.17,
    "evidence_strength": 0.25,
    "practical_value": 0.18,
    "emotional_resonance": 0.10,
    "share_potential": 0.12,
}

# 高搜索量关键词（基于真实搜索热度）
HIGH_SEO_KEYWORDS = {
    "ChatGPT": 1.5, "AI工具": 1.4, "效率": 1.3, "学习方法": 1.3,
    "专注力": 1.4, "拖延": 1.4, "时间管理": 1.5, "焦虑": 1.3,
    "创业": 1.3, "副业": 1.4, "远程工作": 1.3, "自律": 1.4,
    "冥想": 1.2, "心流": 1.3, "孩子": 1.3, "育儿": 1.3,
    "记忆力": 1.3, "考试": 1.3, "简历": 1.3, "面试": 1.3,
    "赚钱": 1.4, "被动收入": 1.4, "职场": 1.3, "晋升": 1.2,
    "编程": 1.3, "Python": 1.2, "习惯": 1.4, "Notion": 1.2,
    "Copilot": 1.3, "Claude": 1.2, "Midjourney": 1.2, "情绪": 1.3,
    "睡眠": 1.3, "运动": 1.2, "饮食": 1.2, "减压": 1.3,
    "诊断": 1.3, "多巴胺": 1.3, "神经科学": 1.2, "执行功能": 1.3,
    "番茄钟": 1.2, "Perplexity": 1.1, "Motion": 1.1, "Goblin": 1.1,
}

EMOTIONAL_KEYWORDS = {
    "焦虑": 1.5, "痛苦": 1.4, "克服": 1.4, "拯救": 1.4,
    "超能力": 1.5, "改变": 1.3, "自信": 1.4, "挣扎": 1.4,
    "希望": 1.4, "孤独": 1.3, "理解": 1.3, "接纳": 1.4,
    "过山车": 1.3, "崩溃": 1.4, "恢复": 1.3, "内疚": 1.3,
    "完美主义": 1.3, "最好的自己": 1.4, "亲子": 1.4, "家庭": 1.3,
}

SHARE_TRIGGERS = {
    "指南": 1.3, "攻略": 1.4, "秘密": 1.3, "技巧": 1.3,
    "方法": 1.2, "策略": 1.2, "清单": 1.3, "方案": 1.2,
    "系统": 1.2, "必备": 1.4, "终极": 1.3, "路线图": 1.3,
    "从0到1": 1.4, "完整": 1.3, "评测": 1.3, "对比": 1.3,
}

LIST_TITLE_BONUS = 1.3
PRACTICAL_CATEGORIES = {"ai-tools", "time-mgmt", "focus", "learning"}


def _keyword_boost(text: str, keyword_map: dict) -> float:
    boost = 1.0
    for kw, factor in keyword_map.items():
        if kw in text:
            boost *= factor
    return boost


def _has_number_list(title: str) -> bool:
    return bool(re.search(r"\d+\s*[个种步条款招大类项]", title))


def _build_query_keywords(topic: dict) -> list[str]:
    """从选题构建检索关键词（用于知识库匹配）"""
    kws = []
    kws.extend(topic.get("keywords", []))
    title = topic.get("title", "")
    # 加入工具名和概念词
    for tool in ["ChatGPT", "Claude", "Motion", "Goblin", "Notion", "Tiimo",
                 "Brain.fm", "Focusmate", "Perplexity"]:
        if tool.lower() in title.lower():
            kws.append(tool)
    # 加入分类英文关键词
    cat_kw = {
        "ai-tools": ["tool", "app", "AI", "productivity"],
        "focus": ["focus", "attention", "concentration"],
        "time-mgmt": ["time", "schedule", "task", "planning"],
        "emotion": ["emotion", "anxiety", "regulation", "mood"],
        "learning": ["learning", "study", "education", "memory"],
        "career": ["work", "career", "workplace", "job"],
        "entrepreneurship": ["business", "entrepreneur", "startup"],
        "parenting": ["children", "kids", "parent", "education"],
        "science": ["research", "diagnosis", "brain", "study", "EEG", "MRI"],
        "lifestyle": ["habit", "sleep", "daily", "routine"],
        "community": ["community", "support", "social"],
    }
    kws.extend(cat_kw.get(topic.get("category_id", ""), []))
    kws.append("ADHD")
    return kws


def score_topic(topic: dict, retriever: KnowledgeRetriever | None = None) -> ScoreDimensions:
    """
    对单个选题进行多维度评分

    与旧版最大区别：evidence_strength 维度真实统计知识库中
    能支撑该选题的研究发现、统计数据、工具和策略数量
    """
    title = topic.get("title", "")
    subtitle = topic.get("subtitle", "")
    angle = topic.get("angle", "")
    category_id = topic.get("category_id", "")
    full_text = f"{title} {subtitle} {angle}"

    # 1. SEO潜力：真实关键词覆盖
    seo_score = 5.0
    seo_boost = _keyword_boost(full_text, HIGH_SEO_KEYWORDS)
    seo_score = min(10.0, seo_score * min(seo_boost, 2.0))
    if _has_number_list(title):
        seo_score = min(10.0, seo_score * 1.15)

    # 2. 跨平台吸引力
    cross_base = 5.8
    if category_id in PRACTICAL_CATEGORIES:
        cross_base += 0.8
    if _has_number_list(title):
        cross_base *= LIST_TITLE_BONUS
    if "：" in title or "?" in title or "？" in title:
        cross_base += 0.3
    cross_score = min(10.0, cross_base)

    # 3. 证据强度：知识库真实支撑度（核心创新）
    evidence_score = 4.0
    if retriever is not None:
        keywords = _build_query_keywords(topic)
        findings = retriever.findings_for(keywords, limit=5)
        stats = retriever.statistics_for(keywords, limit=3)
        strategies = retriever.strategies_for(keywords, limit=6)
        tools = retriever.tools_for_category(category_id, limit=4)
        # 计算相关度命中
        rel_findings = sum(1 for f in findings if retriever._relevance(f["text"], keywords) > 0)
        rel_strategies = sum(1 for s in strategies if retriever._relevance(s["text"], keywords) > 0)
        evidence_score = min(10.0,
            4.0
            + rel_findings * 0.5
            + len(stats) * 0.4
            + rel_strategies * 0.3
            + len(tools) * 0.3
        )

    # 4. 实用价值
    practical_base = 5.5
    practical_markers = ["方法", "策略", "技巧", "指南", "方案", "系统",
                         "工具", "清单", "步骤", "流程", "攻略", "教程"]
    for marker in practical_markers:
        if marker in full_text:
            practical_base += 0.35
    if category_id in PRACTICAL_CATEGORIES:
        practical_base += 0.5
    practical_score = min(10.0, practical_base)

    # 5. 情感共鸣
    emotion_base = 5.2
    emotion_boost = _keyword_boost(full_text, EMOTIONAL_KEYWORDS)
    emotion_score = min(10.0, emotion_base * min(emotion_boost, 1.8))

    # 6. 分享潜力
    share_base = 5.2
    share_boost = _keyword_boost(full_text, SHARE_TRIGGERS)
    if _has_number_list(title):
        share_boost *= 1.2
    share_score = min(10.0, share_base * min(share_boost, 2.0))

    return ScoreDimensions(
        seo_potential=round(seo_score, 2),
        cross_platform=round(cross_score, 2),
        evidence_strength=round(evidence_score, 2),
        practical_value=round(practical_score, 2),
        emotional_resonance=round(emotion_score, 2),
        share_potential=round(share_score, 2),
    )


def compute_weighted_score(dimensions: ScoreDimensions, weights: dict | None = None) -> float:
    w = weights or DEFAULT_WEIGHTS
    total = (
        dimensions.seo_potential * w["seo_potential"]
        + dimensions.cross_platform * w["cross_platform"]
        + dimensions.evidence_strength * w["evidence_strength"]
        + dimensions.practical_value * w["practical_value"]
        + dimensions.emotional_resonance * w["emotional_resonance"]
        + dimensions.share_potential * w["share_potential"]
    )
    return round(total, 2)


def rank_topics(
    topics: list[dict],
    weights: dict | None = None,
    retriever: KnowledgeRetriever | None = None,
) -> list[dict]:
    """对选题列表评分并按综合得分降序排序"""
    scored = []
    for topic in topics:
        dimensions = score_topic(topic, retriever)
        weighted = compute_weighted_score(dimensions, weights)
        scored.append({
            **topic,
            "scores": dimensions.to_dict(),
            "weighted_score": weighted,
        })
    scored.sort(key=lambda x: x["weighted_score"], reverse=True)
    for i, item in enumerate(scored):
        item["rank"] = i + 1
    return scored
