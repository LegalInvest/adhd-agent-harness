"""
多维度选题评分系统
基于 6 个维度对每个选题进行评分，支持自定义权重
"""

import hashlib
import math
from dataclasses import dataclass


@dataclass
class ScoreDimensions:
    seo_potential: float       # SEO潜力 (1-10)
    cross_platform: float      # 跨平台吸引力 (1-10)
    uniqueness: float          # 独特性 (1-10)
    practical_value: float     # 实用价值 (1-10)
    emotional_resonance: float # 情感共鸣 (1-10)
    share_potential: float     # 分享潜力 (1-10)

    def to_dict(self) -> dict:
        return {
            "seo_potential": round(self.seo_potential, 2),
            "cross_platform": round(self.cross_platform, 2),
            "uniqueness": round(self.uniqueness, 2),
            "practical_value": round(self.practical_value, 2),
            "emotional_resonance": round(self.emotional_resonance, 2),
            "share_potential": round(self.share_potential, 2),
        }


# 默认评分权重
DEFAULT_WEIGHTS = {
    "seo_potential": 0.20,
    "cross_platform": 0.20,
    "uniqueness": 0.15,
    "practical_value": 0.20,
    "emotional_resonance": 0.10,
    "share_potential": 0.15,
}

# 高SEO关键词及其搜索热度系数
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
    "社交": 1.2, "沟通": 1.2, "领导力": 1.2, "个人品牌": 1.3,
    "游戏化": 1.2, "极简": 1.2, "诊断": 1.3, "药物": 1.2,
    "番茄钟": 1.2, "Perplexity": 1.1, "多巴胺": 1.3, "神经科学": 1.2,
}

# 高情感共鸣关键词
EMOTIONAL_KEYWORDS = {
    "焦虑": 1.5, "痛苦": 1.4, "克服": 1.4, "拯救": 1.4,
    "超能力": 1.5, "英雄": 1.4, "改变": 1.3, "自信": 1.4,
    "成功": 1.3, "失败": 1.3, "挣扎": 1.4, "希望": 1.4,
    "孤独": 1.3, "理解": 1.3, "接纳": 1.4, "勇气": 1.3,
    "过山车": 1.3, "崩溃": 1.4, "恢复": 1.3, "胜利": 1.3,
    "内疚": 1.3, "完美主义": 1.3, "自我": 1.2, "最好的自己": 1.4,
    "爱": 1.3, "亲子": 1.4, "家庭": 1.3, "友谊": 1.3,
}

# 高分享潜力特征
SHARE_TRIGGERS = {
    "指南": 1.3, "攻略": 1.4, "秘密": 1.3, "技巧": 1.3,
    "方法": 1.2, "策略": 1.2, "清单": 1.3, "方案": 1.2,
    "系统": 1.2, "必备": 1.4, "完美": 1.3, "终极": 1.3,
    "全攻略": 1.5, "路线图": 1.3, "从0到1": 1.4, "完整": 1.3,
}

# 跨平台适配因子：数字列表型标题在多平台表现更好
LIST_TITLE_BONUS = 1.3


def _deterministic_seed(text: str) -> float:
    """基于文本内容生成确定性随机数 (0-1)"""
    h = hashlib.md5(text.encode("utf-8")).hexdigest()
    return int(h[:8], 16) / 0xFFFFFFFF


def _keyword_boost(text: str, keyword_map: dict[str, float]) -> float:
    """计算文本中关键词的加权提升系数"""
    boost = 1.0
    for kw, factor in keyword_map.items():
        if kw in text:
            boost *= factor
    return boost


def _has_number_list(title: str) -> bool:
    """检查标题是否包含数字列表格式"""
    import re
    return bool(re.search(r"\d+\s*[个种步条款招大类项]", title))


def score_topic(topic: dict) -> ScoreDimensions:
    """
    对单个选题进行多维度评分

    评分基于以下因素：
    - 标题中的SEO关键词覆盖
    - 内容的跨平台适配性
    - 角度的独特程度
    - 内容的实用操作价值
    - 标题的情感共鸣力
    - 内容的分享传播潜力
    """
    title = topic.get("title", "")
    subtitle = topic.get("subtitle", "")
    angle = topic.get("angle", "")
    category_id = topic.get("category_id", "")
    full_text = f"{title} {subtitle} {angle}"

    # 确定性随机种子，保证同一选题每次评分一致
    seed = _deterministic_seed(title)
    seed2 = _deterministic_seed(subtitle)

    # 1. SEO潜力评分
    seo_base = 5.0 + seed * 2.0  # 5-7 基础分
    seo_boost = _keyword_boost(full_text, HIGH_SEO_KEYWORDS)
    seo_score = min(10.0, seo_base * min(seo_boost, 2.0))

    # 数字列表型标题SEO更好
    if _has_number_list(title):
        seo_score = min(10.0, seo_score * 1.15)

    # 2. 跨平台吸引力评分
    cross_base = 5.5 + seed2 * 1.5
    # 实用工具类和方法论类内容跨平台表现更好
    practical_categories = {"ai-tools", "time-mgmt", "focus", "learning"}
    if category_id in practical_categories:
        cross_base += 0.8
    if _has_number_list(title):
        cross_base *= LIST_TITLE_BONUS
    cross_score = min(10.0, cross_base)

    # 3. 独特性评分
    # 越具体的角度越独特
    unique_base = 6.0 + _deterministic_seed(angle) * 2.5
    specific_markers = ["vs", "对比", "揭示", "秘密", "真相", "误区", "颠覆"]
    for marker in specific_markers:
        if marker in full_text:
            unique_base += 0.5
    unique_score = min(10.0, unique_base)

    # 4. 实用价值评分
    practical_base = 5.5 + seed * 1.5
    practical_markers = ["方法", "策略", "技巧", "指南", "方案", "系统",
                         "工具", "清单", "步骤", "流程", "攻略", "教程"]
    for marker in practical_markers:
        if marker in full_text:
            practical_base += 0.3
    practical_score = min(10.0, practical_base)

    # 5. 情感共鸣评分
    emotion_base = 5.0 + seed2 * 2.0
    emotion_boost = _keyword_boost(full_text, EMOTIONAL_KEYWORDS)
    emotion_score = min(10.0, emotion_base * min(emotion_boost, 1.8))

    # 6. 分享潜力评分
    share_base = 5.0 + seed * 1.8
    share_boost = _keyword_boost(full_text, SHARE_TRIGGERS)
    if _has_number_list(title):
        share_boost *= 1.2
    share_score = min(10.0, share_base * min(share_boost, 2.0))

    return ScoreDimensions(
        seo_potential=round(seo_score, 2),
        cross_platform=round(cross_score, 2),
        uniqueness=round(unique_score, 2),
        practical_value=round(practical_score, 2),
        emotional_resonance=round(emotion_score, 2),
        share_potential=round(share_score, 2),
    )


def compute_weighted_score(
    dimensions: ScoreDimensions,
    weights: dict[str, float] | None = None,
) -> float:
    """计算加权综合得分"""
    w = weights or DEFAULT_WEIGHTS
    total = (
        dimensions.seo_potential * w["seo_potential"]
        + dimensions.cross_platform * w["cross_platform"]
        + dimensions.uniqueness * w["uniqueness"]
        + dimensions.practical_value * w["practical_value"]
        + dimensions.emotional_resonance * w["emotional_resonance"]
        + dimensions.share_potential * w["share_potential"]
    )
    return round(total, 2)


def rank_topics(topics: list[dict], weights: dict[str, float] | None = None) -> list[dict]:
    """
    对选题列表进行评分和排序

    返回按综合得分降序排列的选题列表，每个选题附带评分信息
    """
    scored = []
    for topic in topics:
        dimensions = score_topic(topic)
        weighted = compute_weighted_score(dimensions, weights)
        scored.append({
            **topic,
            "scores": dimensions.to_dict(),
            "weighted_score": weighted,
        })

    scored.sort(key=lambda x: x["weighted_score"], reverse=True)

    # 添加排名
    for i, item in enumerate(scored):
        item["rank"] = i + 1

    return scored
