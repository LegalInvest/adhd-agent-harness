"""
ADHD×AI 情报自动流 - 智能处理器
负责: 分类、分析、重要性评分、思考生成
"""
import yaml
import json
from datetime import datetime
from typing import List, Dict, Optional
from dataclasses import dataclass, field
from collectors.base import RawItem

@dataclass
class ProcessedItem:
    """处理后的情报项"""
    raw: RawItem                      # 原始数据
    category: str                     # 分类
    importance: float                 # 重要性 1-10
    summary_zh: str                   # 中文摘要
    key_insight: str                  # 关键洞察
    connections: List[str] = field(default_factory=list)  # 与已有知识的连接
    social_post: str = ""            # 社交媒体动态稿
    is_deep_draft_trigger: bool = False  # 是否触发深度选题

class IntelligenceProcessor:
    """情报处理器 - 使用LLM进行分析"""

    def __init__(self, config_path: str = "config/config.yaml"):
        with open(config_path, 'r') as f:
            self.config = yaml.safe_load(f)
        self.categories = self.config['processing']['categories']
        self.importance_threshold = self.config['processing']['importance_threshold']
        self.deep_threshold = self.config['output']['formats']['deep_draft']['trigger_threshold']

    def process(self, items: List[RawItem]) -> List[ProcessedItem]:
        """处理一批原始数据"""
        processed = []
        for item in items:
            p = self._analyze(item)
            if p.importance >= self.importance_threshold:
                processed.append(p)
        # 按重要性排序
        processed.sort(key=lambda x: x.importance, reverse=True)
        return processed

    def _analyze(self, item: RawItem) -> ProcessedItem:
        """分析单个项目"""
        # 分类 (基于关键词规则)
        category = self._classify(item)

        # 重要性评分 (多因子)
        importance = self._score_importance(item, category)

        # 生成中文摘要 (使用模板/规则)
        summary_zh = self._generate_summary(item)

        # 生成关键洞察
        key_insight = self._generate_insight(item, category)

        # 与已有知识连接
        connections = self._find_connections(item)

        # 生成社交媒体动态
        social_post = self._generate_social_post(item, summary_zh, key_insight)

        # 判断是否触发深度选题
        is_deep = importance >= self.deep_threshold

        return ProcessedItem(
            raw=item,
            category=category,
            importance=importance,
            summary_zh=summary_zh,
            key_insight=key_insight,
            connections=connections,
            social_post=social_post,
            is_deep_draft_trigger=is_deep
        )

    def _classify(self, item: RawItem) -> str:
        """基于内容关键词分类"""
        text = (item.title + " " + item.content).lower()

        rules = {
            "研究突破": ["study", "trial", "RCT", "meta-analysis", "neuroimaging", "fMRI", 
                        "dopamine", "neurobiological", "genome", "biomarker"],
            "产品工具": ["app", "tool", "software", "platform", " wearable", "game", 
                        "endeavorrx", "digital therapeutic", "chatgpt", "claude"],
            "政策监管": ["FDA", "approval", "guideline", "WHO", "diagnostic", "DSM", 
                        "ICD", "prescription", "medication shortage"],
            "AI×ADHD": ["machine learning", "AI ", "artificial intelligence", "algorithm",
                        "digital phenotyping", "predict", "automation", "LLM"],
            "争议批评": ["overdiagnosis", "misdiagnosis", "stimulant", "abuse", "controversy",
                        "critique", "pharmaceutical", "big pharma"],
            "个人故事": ["diagnosed", "my experience", "I have ADHD", "sharing", "story",
                        "life with", "struggle with"],
            "社区热议": ["tip", "hack", "advice", "help", "recommendation", "what works",
                        "does anyone", "how do you"]
        }

        scores = {}
        for cat, keywords in rules.items():
            scores[cat] = sum(1 for k in keywords if k in text)

        best = max(scores, key=scores.get)
        return best if scores[best] > 0 else "其他"

    def _score_importance(self, item: RawItem, category: str) -> float:
        """多因子重要性评分"""
        score = 5.0  # 基础分
        text = (item.title + " " + item.content).lower()

        # 来源权重
        source_weights = {"arxiv": 1.5, "pubmed": 1.5, "reddit": 0.8, "news": 1.0}
        score *= source_weights.get(item.source, 1.0)

        # AI×ADHD 交叉加权
        ai_signals = ["artificial intelligence", "machine learning", "digital phenotyping",
                      "neurofeedback", "brain computer", " EndeavorRx"]
        if any(s in text for s in ai_signals):
            score += 2.0

        # 时效性 (越新越重要)
        if item.published_at:
            days_old = (datetime.now() - item.published_at).days
            if days_old <= 1:
                score += 1.5
            elif days_old <= 3:
                score += 0.8

        # 热度加权
        if item.score > 1000:
            score += 1.5
        elif item.score > 500:
            score += 1.0
        elif item.score > 100:
            score += 0.5

        # 类别权重
        cat_weights = {"研究突破": 1.3, "AI×ADHD": 1.5, "政策监管": 1.2}
        score *= cat_weights.get(category, 1.0)

        return min(score, 10.0)  # 封顶10分

    def _generate_summary(self, item: RawItem) -> str:
        """生成中文摘要 (规则驱动，后续可接入LLM)"""
        title = item.title[:120]
        content = item.content[:500] if item.content else ""

        # 如果是论文，提取关键信息
        if item.source == "arxiv":
            return f"【论文】{title}\n摘要: {content[:300]}..."
        elif item.source == "reddit":
            return f"【社区热议】{title}\n{content[:200]}..."
        else:
            return f"{title}\n{content[:300]}..."

    def _generate_insight(self, item: RawItem, category: str) -> str:
        """生成关键洞察 (基于规则和模板)"""
        insights_map = {
            "研究突破": "新研究可能改变我们对ADHD的理解，值得关注后续进展。",
            "产品工具": "新工具可能为ADHD群体提供新的自我管理选项。",
            "政策监管": "政策变化可能影响ADHD的诊断和治疗格局。",
            "AI×ADHD": "AI技术在ADHD领域的应用正在加速，交叉点值得关注。",
            "争议批评": "争议声音提醒我们保持批判性思维，审视ADHD叙事的完整性。",
            "个人故事": "真实经历为ADHD研究提供了宝贵的定性数据。",
            "社区热议": "社区共识可能反映未被研究记录的实际需求和有效策略。"
        }
        return insights_map.get(category, "值得关注的发展。")

    def _find_connections(self, item: RawItem) -> List[str]:
        """与已有知识库建立连接"""
        # 简化的关键词匹配
        text = (item.title + " " + item.content).lower()
        connections = []

        knowledge_nodes = {
            "多巴胺": "与多巴胺机制研究相关——我们的深度研究第8章详细分析了DA系统在ADHD中的作用",
            "超聚焦": "与超聚焦(Hyperfocus)机制相关——详见第一轮惊喜发现Dim02",
            "执行功能": "与执行功能障碍理论相关——Barkley模型在第5章详细阐述",
            "超能力": "与ADHD优势/超能力叙事相关——详见超能力激活框架",
            "注意力": "与注意力调控机制相关——DMN/TPN网络研究",
            "数字疗法": "与FDA批准数字疗法(EndeavorRx)相关——治疗范式变迁第2章",
            "睡眠": "与ADHD睡眠问题相关——昼夜节律研究详见惊喜发现",
            "拖延": "与ADHD拖延机制相关——任务启动困难分析",
            "正念": "与正念干预效果相关——CBT/正念局限性分析",
            "药物": "与ADHD药物治疗相关——长期效果争议(MTA研究)",
        }

        for keyword, connection in knowledge_nodes.items():
            if keyword in text:
                connections.append(connection)

        return connections[:3]  # 最多返回3个连接

    def _generate_social_post(self, item: RawItem, summary: str, insight: str) -> str:
        """生成社交媒体动态稿"""
        # 针对不同平台生成不同格式
        title = item.title[:80]

        # Twitter/X 格式 (280字)
        twitter_post = f"📊 ADHD×AI情报\n\n{title}\n\n{insight[:60]}\n\n🔗 {item.url[:60]}\n#ADHD #AI"

        # 中文平台格式
        zh_post = f"【ADHD×AI情报流】\n\n{title}\n\n💡 {insight}\n\n来源: {item.source_name}\n{item.url}"

        return zh_post
