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
from engine.attention import score_attention


@dataclass
class ScoreDimensions:
    seo_potential: float          # SEO潜力 (1-10)
    cross_platform: float         # 跨平台吸引力 (1-10)
    evidence_strength: float      # 证据强度：有多少真实研究/数据支撑 (1-10)
    isomorphism_alignment: float  # 同构脊柱契合度：是否engage ADHD↔LLM同构 + 双域证据 (1-10)
    practical_value: float        # 实用价值 (1-10)
    emotional_resonance: float    # 情感共鸣 (1-10)
    share_potential: float        # 分享潜力 (1-10)
    attention: float              # 注意力分（Upworthy 22,680 组 A/B 测试校准）(1-10)

    def to_dict(self) -> dict:
        return {
            "seo_potential": round(self.seo_potential, 2),
            "cross_platform": round(self.cross_platform, 2),
            "evidence_strength": round(self.evidence_strength, 2),
            "isomorphism_alignment": round(self.isomorphism_alignment, 2),
            "practical_value": round(self.practical_value, 2),
            "emotional_resonance": round(self.emotional_resonance, 2),
            "share_potential": round(self.share_potential, 2),
            "attention": round(self.attention, 2),
        }


# 评分权重：证据强度 + 同构脊柱契合度并列为最高权重，
# 体现"事实驱动 + 以 ADHD↔LLM 同构为脊柱"的双重理念。
DEFAULT_WEIGHTS = {
    "seo_potential": 0.12,
    "cross_platform": 0.11,
    "evidence_strength": 0.22,
    "isomorphism_alignment": 0.20,
    "practical_value": 0.11,
    "emotional_resonance": 0.07,
    "share_potential": 0.07,
    "attention": 0.10,
}

# 同构脊柱信号词：标题/副标题命中越多，说明越贴合「ADHD↔LLM 同构」脊柱
ISOMORPHISM_SIGNALS = [
    "同构", "harness", "脚手架", "拐杖", "外部记忆", "第二大脑", "执行功能",
    "调度", "生成核心", "agent", "llm", "大语言模型", "上下文", "幻觉",
    "验证", "采样", "temperature", "目标漂移", "重锚定", "任务分解",
    "human-in-the-loop", "body doubling", "认知卸载", "外化", "外接",
]
# 双受众张力：最有张力的选题必须**同时**命中两端——
# ADHD 人群一端（痛点/身份）+ Agentic Harness 工程师一端（LLM/agent 工程）。
ADHD_AUDIENCE_SIGNALS = [
    "adhd", "拖延", "分心", "走神", "专注", "注意力", "时间盲", "多巴胺",
    "工作记忆", "执行功能", "情绪", "超聚焦", "第二大脑", "拐杖", "习惯",
]
ENGINEER_AUDIENCE_SIGNALS = [
    "llm", "agent", "harness", "大语言模型", "gpt", "orchestration", "调度",
    "上下文", "context", "幻觉", "hallucination", "采样", "temperature",
    "function calling", "rag", "向量", "prompt", "human-in-the-loop", "生成核心",
]
# 社媒病毒性框架信号（好奇缺口 / 反直觉 / 身份认同 / 数字清单 / 行动召唤）
VIRAL_HOOK_SIGNALS = [
    "为什么", "其实", "真的", "竟然", "停止", "别再", "原来", "一文",
    "30 天", "我把", "3 个", "5 个", "7 个", "10 个", "同一", "正在偷偷",
    "重写", "彻底", "？", "??",
]
# harness 工程域关键词（用于统计"双域证据"是否两端都有支撑）
HARNESS_QUERY_KEYWORDS = [
    "agent", "llm", "memory", "context", "hallucination", "verification",
    "planning", "tool", "retrieval", "rag", "temperature", "prompt",
    "stateless", "scaffold", "orchestration", "human in the loop",
]

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
    spine = topic.get("spine", "")
    spine_mirror = topic.get("spine_mirror", "")
    full_text = f"{title} {subtitle} {angle}"
    iso_text = f"{title} {subtitle} {angle} {spine} {spine_mirror}".lower()

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

    # 3.5 同构脊柱契合度（含双受众张力 + 社媒病毒性 + 双域证据）
    # 核心约束：最有张力的 400 篇必须**同时**勾住 ADHD 人群与 Harness 工程师两端。
    iso_score = 2.0
    sig_hits = sum(1 for s in ISOMORPHISM_SIGNALS if s.lower() in iso_text)
    iso_score += min(sig_hits, 6) * 0.4

    has_adhd = any(s in iso_text for s in ADHD_AUDIENCE_SIGNALS)
    has_eng = any(s in iso_text for s in ENGINEER_AUDIENCE_SIGNALS)
    if has_adhd and has_eng:
        iso_score += 2.5  # 双受众都被勾住——这才是「最有张力」的选题
    elif has_adhd or has_eng:
        iso_score += 0.3  # 只勾住一端，张力不足
    else:
        iso_score -= 1.0  # 两端都没勾住，几乎没有同构张力

    viral_hits = sum(1 for s in VIRAL_HOOK_SIGNALS if s.lower() in iso_text)
    iso_score += min(viral_hits, 4) * 0.35  # 社媒病毒性框架加成

    if spine:
        iso_score += 1.0  # 显式锚定到某条脊柱
    if topic.get("is_problem_driven"):
        iso_score += 0.4  # 问题驱动

    if retriever is not None:
        adhd_find = retriever.findings_for(_build_query_keywords(topic), limit=4)
        harness_find = retriever.findings_for(HARNESS_QUERY_KEYWORDS, limit=4)
        rel_harness = sum(
            1 for f in harness_find if retriever._relevance(f["text"], HARNESS_QUERY_KEYWORDS) > 0
        )
        if adhd_find and rel_harness:
            iso_score += 1.2  # 两端都有真实证据（真正的双域）
        elif rel_harness:
            iso_score += 0.4
    iso_score = max(0.0, min(10.0, iso_score))

    # 4. 实用价值
    practical_base = 5.5
    practical_markers = ["方法", "策略", "技巧", "指南", "方案", "系统",
                         "工具", "清单", "步骤", "流程", "攻略", "教程"]
    for marker in practical_markers:
        if marker in full_text:
            practical_base += 0.35
    if category_id in PRACTICAL_CATEGORIES:
        practical_base += 0.5
    # 人生 Harness 金字塔上层（叙事/关系/价值层）加成：
    # 项目北极星是助力 ADHD 者获得幸福与人生价值，而非仅提升效率，
    # 自我和解、关系、职业与人生方向类选题在实用价值维度获得加权。
    growth_markers = ["幸福", "成长", "自我和解", "羞耻", "自责", "自我接纳",
                      "人生", "价值感", "意义", "职业", "亲密关系", "伴侣",
                      "家人", "身份", "叙事", "和解", "优势", "长处"]
    growth_hits = sum(1 for m in growth_markers if m in full_text)
    practical_base += min(1.2, growth_hits * 0.4)
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
        isomorphism_alignment=round(iso_score, 2),
        practical_value=round(practical_score, 2),
        emotional_resonance=round(emotion_score, 2),
        share_potential=round(share_score, 2),
        attention=round(score_attention(title, subtitle), 2),
    )


def compute_weighted_score(dimensions: ScoreDimensions, weights: dict | None = None) -> float:
    w = weights or DEFAULT_WEIGHTS
    total = (
        dimensions.seo_potential * w["seo_potential"]
        + dimensions.cross_platform * w["cross_platform"]
        + dimensions.evidence_strength * w["evidence_strength"]
        + dimensions.isomorphism_alignment * w["isomorphism_alignment"]
        + dimensions.practical_value * w["practical_value"]
        + dimensions.emotional_resonance * w["emotional_resonance"]
        + dimensions.share_potential * w["share_potential"]
        + dimensions.attention * w["attention"]
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
