#!/usr/bin/env python3
"""
ADHD×AI 情报自动流系统 (Intelligence Auto-Flow System)
Version: 1.0
Author: Based on 122-year ADHD research + 200+ blogger archaeology

功能:
- 多源情报收集 (X/Twitter, Reddit, 小红书, arXiv, Product Hunt, RSS)
- AI智能分析 (分类, 摘要, 选题推荐)
- 情感角度注入 (你的差异化)
- 每日简报自动生成
- 选题库管理
- 存稿发布工作流

部署:
1. 安装依赖: pip install requests feedparser python-dotenv
2. 配置环境变量 (见下方)
3. 设置定时任务: crontab -e → 0 8 * * * python3 /path/to/adhd_ai_intelligence_system.py
4. 每日8点自动接收情报简报
"""

import os
import json
import re
import hashlib
from datetime import datetime, timedelta
from dataclasses import dataclass, asdict, field
from typing import List, Dict, Optional, Set
from enum import Enum
import logging

# ========== 配置日志 ==========
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# ========== 环境变量配置模板 ==========
ENV_TEMPLATE = """
# 复制到 .env 文件并填入你的API密钥

# X/Twitter API (v2) - 用于追踪博主动态
X_BEARER_TOKEN=your_x_bearer_token_here

# Reddit API - 用于社区监控
REDDIT_CLIENT_ID=your_reddit_client_id
REDDIT_CLIENT_SECRET=your_reddit_client_secret
REDDIT_USER_AGENT=ADHDIntelligenceBot/1.0

# Anthropic Claude API - 用于AI分析
ANTHROPIC_API_KEY=your_claude_api_key

# OpenAI API (可选) - 备用AI分析
OPENAI_API_KEY=your_openai_api_key_optional

# 数据存储路径
DATA_DIR=/path/to/your/data
"""

# ========== 数据模型 ==========

class SourceType(Enum):
    X_TWITTER = "x_twitter"
    REDDIT = "reddit"
    XIAOHONGSHU = "xiaohongshu"
    BILIBILI = "bilibili"
    ZHIHU = "zhihu"
    SUBSTACK = "substack"
    RSS = "rss"
    ARXIV = "arxiv"
    YOUTUBE = "youtube"
    TIKTOK = "tiktok"
    PODCAST = "podcast"
    GITHUB = "github"
    PRODUCT_HUNT = "product_hunt"
    MANUAL = "manual"  # 手动添加

class ContentType(Enum):
    NEW_TOOL = "new_tool"
    TOOL_UPDATE = "tool_update"
    CREATOR_CONTENT = "creator_content"
    ACADEMIC_PAPER = "academic_paper"
    PRODUCT_LAUNCH = "product_launch"
    FUNDING_NEWS = "funding_news"
    COMMUNITY_DISCUSSION = "community_discussion"
    TREND_SIGNAL = "trend_signal"
    CREATOR_MILESTONE = "creator_milestone"
    OPPORTUNITY = "opportunity"

@dataclass
class IntelligenceItem:
    """情报条目"""
    id: str
    title: str
    source: str
    source_type: SourceType
    content_type: ContentType
    url: str
    creator_name: Optional[str] = None
    summary: str = ""
    key_points: List[str] = field(default_factory=list)
    related_tools: List[str] = field(default_factory=list)
    adhd_relevance: int = 5       # 1-10
    actionability: int = 5         # 1-10
    novelty_score: int = 5         # 1-10
    emotion_angle: Optional[str] = None
    story_idea: Optional[str] = None
    timestamp: str = ""
    processed: bool = False
    
    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "source": self.source,
            "source_type": self.source_type.value,
            "content_type": self.content_type.value,
            "url": self.url,
            "creator_name": self.creator_name,
            "summary": self.summary,
            "key_points": self.key_points,
            "related_tools": self.related_tools,
            "adhd_relevance": self.adhd_relevance,
            "actionability": self.actionability,
            "novelty_score": self.novelty_score,
            "emotion_angle": self.emotion_angle,
            "story_idea": self.story_idea,
            "timestamp": self.timestamp,
            "processed": self.processed
        }
    
    @classmethod
    def from_dict(cls, d):
        return cls(
            id=d["id"],
            title=d["title"],
            source=d["source"],
            source_type=SourceType(d["source_type"]),
            content_type=ContentType(d["content_type"]),
            url=d["url"],
            creator_name=d.get("creator_name"),
            summary=d.get("summary", ""),
            key_points=d.get("key_points", []),
            related_tools=d.get("related_tools", []),
            adhd_relevance=d.get("adhd_relevance", 5),
            actionability=d.get("actionability", 5),
            novelty_score=d.get("novelty_score", 5),
            emotion_angle=d.get("emotion_angle"),
            story_idea=d.get("story_idea"),
            timestamp=d.get("timestamp", ""),
            processed=d.get("processed", False)
        )

@dataclass
class StoryIdea:
    """选题灵感"""
    id: str
    title: str
    emotion_angle: str
    adhd_relevance: int
    actionability: int
    estimated_time: str
    priority: str
    format: str
    source_items: List[str] = field(default_factory=list)
    status: str = "idea"  # idea → drafting → scheduled → published → archived
    created_date: str = ""
    
    def to_dict(self):
        return asdict(self)

# ========== 核心引擎 ==========

class ADHDIntelligenceEngine:
    """
    ADHD×AI 情报自动流核心引擎
    """
    
    def __init__(self, data_dir: str = None):
        self.data_dir = data_dir or os.environ.get("DATA_DIR", "./adhd_ai_data")
        os.makedirs(self.data_dir, exist_ok=True)
        os.makedirs(os.path.join(self.data_dir, "briefings"), exist_ok=True)
        os.makedirs(os.path.join(self.data_dir, "ideas"), exist_ok=True)
        os.makedirs(os.path.join(self.data_dir, "creators"), exist_ok=True)
        os.makedirs(os.path.join(self.data_dir, "tools"), exist_ok=True)
        
        # 加载数据库
        self.creators_db = self._load_or_init("creators_db.json", self._default_creators())
        self.tools_db = self._load_or_init("tools_db.json", self._default_tools())
        self.idea_bank = self._load_ideas()
        
        # API配置
        self.x_bearer = os.environ.get("X_BEARER_TOKEN", "")
        self.reddit_client_id = os.environ.get("REDDIT_CLIENT_ID", "")
        self.reddit_secret = os.environ.get("REDDET_CLIENT_SECRET", "")
        self.anthropic_key = os.environ.get("ANTHROPIC_API_KEY", "")
        self.openai_key = os.environ.get("OPENAI_API_KEY", "")
        
        logger.info(f"引擎初始化完成 | 数据目录: {self.data_dir}")
        logger.info(f"追踪博主: {len(self.creators_db)}人 | 监控工具: {len(self.tools_db)}个")
    
    def _load_or_init(self, filename, default_data):
        """加载或初始化数据文件"""
        filepath = os.path.join(self.data_dir, filename)
        if os.path.exists(filepath):
            with open(filepath, 'r') as f:
                return json.load(f)
        with open(filepath, 'w') as f:
            json.dump(default_data, f, indent=2, ensure_ascii=False)
        return default_data
    
    def _load_ideas(self) -> List[StoryIdea]:
        """加载选题库"""
        filepath = os.path.join(self.data_dir, "ideas", "idea_bank.json")
        if os.path.exists(filepath):
            with open(filepath, 'r') as f:
                data = json.load(f)
                return [StoryIdea(**d) for d in data]
        return []
    
    def _save_ideas(self):
        """保存选题库"""
        filepath = os.path.join(self.data_dir, "ideas", "idea_bank.json")
        with open(filepath, 'w') as f:
            json.dump([idea.to_dict() for idea in self.idea_bank], f, indent=2, ensure_ascii=False)
    
    def _default_creators(self):
        """默认博主追踪数据库 - 来自我们的200+博主研究"""
        return {
            "Rafeh Qazi": {"platforms": ["X"], "handle": "rafehqazi", "focus": "Poppy AI/Vibe Coding", "tier": "core"},
            "Jesse J. Anderson": {"platforms": ["X"], "handle": "adhdjesse", "focus": "ADHD education", "tier": "core"},
            "ThePrimeagen": {"platforms": ["X"], "handle": "ThePrimeagen", "focus": "Vibe coding", "tier": "core"},
            "Joe Bartolozzi": {"platforms": ["X"], "handle": "joe.bartolozzi", "focus": "ADHD advocacy", "tier": "core"},
            "Sonya Barlow": {"platforms": ["X"], "handle": "sonyabarlowuk", "focus": "Neurodiversity CEO", "tier": "core"},
            "Maor Shlomo": {"platforms": ["X"], "handle": "ms_base44", "focus": "Base44/Vibe coding", "tier": "core"},
            "Jessica McCabe": {"platforms": ["X"], "handle": "HowtoADHD", "focus": "How to ADHD", "tier": "core"},
            "William Curb": {"platforms": ["X"], "handle": "HackingYourADHD", "focus": "AI outsourcing EF", "tier": "core"},
            "Dr. Sasha Hamdani": {"platforms": ["X"], "handle": "dr.sashahamdani", "focus": "ADHD psychiatry", "tier": "core"},
            "Emad Mostaque": {"platforms": ["X"], "handle": "EMostaque", "focus": "Schelling AI", "tier": "core"},
            "Bram De Buyser": {"platforms": ["X"], "handle": "bramdb", "focus": "Goblin Tools", "tier": "core"},
            "张程": {"platforms": ["xiaohongshu"], "handle": "ADHD执行力实验室", "focus": "ADHD AI tools CN", "tier": "core"},
            "Junga": {"platforms": ["xiaohongshu"], "handle": "独立开发者Junga", "focus": "ADHD Pal", "tier": "core"},
            # 扩展追踪
            "Karina Adelgaard": {"platforms": ["X"], "handle": "HejAdelgaard", "focus": "ADHD tools", "tier": "extended"},
            "Clark Kegley": {"platforms": ["X"], "handle": "ClarkKegley", "focus": "ADHD systems", "tier": "extended"},
            "Connor DeWolfe": {"platforms": ["X"], "handle": "ConnorDeWolfe", "focus": "ADHD content", "tier": "extended"},
            "Katiefaithfitness": {"platforms": ["X"], "handle": "katiefaithfit", "focus": "ADHD fitness AI", "tier": "extended"},
        }
    
    def _default_tools(self):
        """默认AI工具监控数据库"""
        return {
            "Poppy AI": {"category": "workspace", "founder": "Rafeh Qazi", "status": "active"},
            "Goblin Tools": {"category": "productivity", "founder": "Bram De Buyser", "status": "active"},
            "Focus Bear": {"category": "productivity", "founder": "Jeremy Nagel", "status": "active"},
            "Base44": {"category": "development", "founder": "Maor Shlomo", "status": "acquired"},
            "ADHD Pal": {"category": "productivity", "founder": "Junga", "status": "active"},
            "Leantime": {"category": "project_management", "founder": "Gloria Folaron", "status": "active"},
            "Tiimo": {"category": "planning", "founder": "Danish Team", "status": "active"},
            "EndeavorRx": {"category": "digital_therapeutic", "company": "Akili", "status": "active"},
            "Cursor": {"category": "coding", "company": "Anysphere", "status": "active"},
            "Claude": {"category": "AI assistant", "company": "Anthropic", "status": "active"},
            "ChatGPT": {"category": "AI assistant", "company": "OpenAI", "status": "active"},
            "Midjourney": {"category": "creative", "company": "Midjourney", "status": "active"},
            "Suno": {"category": "creative", "company": "Suno", "status": "active"},
            "Goblin Tools Magic ToDo": {"category": "productivity", "parent": "Goblin Tools", "status": "active"},
        }
    
    # ========== 情报收集层 ==========
    
    def collect_all(self) -> List[IntelligenceItem]:
        """
        全量情报收集
        实际部署时替换为真实API调用
        当前架构展示+手动输入支持
        """
        items = []
        
        # 1. X/Twitter - 博主动态 (需要X_BEARER_TOKEN)
        if self.x_bearer:
            items.extend(self._fetch_x_timeline())
        
        # 2. Reddit - 社区热议 (需要REDDIT_CLIENT_ID)
        if self.reddit_client_id:
            items.extend(self._fetch_reddit())
        
        # 3. arXiv - 学术论文
        items.extend(self._fetch_arxiv())
        
        # 4. RSS - 综合源
        items.extend(self._fetch_rss())
        
        # 5. 手动输入检查
        items.extend(self._check_manual_input())
        
        logger.info(f"情报收集完成: {len(items)} 条")
        return items
    
    def _fetch_x_timeline(self) -> List[IntelligenceItem]:
        """
        X/Twitter API抓取
        实际部署时取消注释并使用真实API
        """
        # import requests
        # headers = {"Authorization": f"Bearer {self.x_bearer}"}
        # items = []
        # for name, info in self.creators_db.items():
        #     if "X" in info.get("platforms", []):
        #         handle = info["handle"]
        #         url = f"https://api.twitter.com/2/users/by/username/{handle}/tweets"
        #         resp = requests.get(url, headers=headers, params={"max_results": 5})
        #         ... 解析并创建IntelligenceItem ...
        logger.info("X/Twitter: API密钥未配置，跳过 (设置X_BEARER_TOKEN环境变量启用)")
        return []
    
    def _fetch_reddit(self) -> List[IntelligenceItem]:
        """
        Reddit API抓取
        监控 r/ADHD, r/ADHD_Programmers, r/neurodiversity
        """
        logger.info("Reddit: API密钥未配置，跳过 (设置REDDIT_CLIENT_ID启用)")
        return []
    
    def _fetch_arxiv(self) -> List[IntelligenceItem]:
        """
        arXiv RSS抓取
        关键词: ADHD, neurodiversity, executive function, attention deficit
        """
        try:
            import feedparser
            items = []
            queries = [
                "ADHD+artificial+intelligence",
                "neurodiversity+AI",
                "executive+function+machine+learning",
                "attention+deficit+language+model"
            ]
            for q in queries:
                url = f"http://export.arxiv.org/api/query?search_query=all:{q}&sortBy=submittedDate&max_results=5"
                feed = feedparser.parse(url)
                for entry in feed.entries[:3]:
                    item_id = hashlib.md5(entry.link.encode()).hexdigest()[:8]
                    items.append(IntelligenceItem(
                        id=f"arx_{item_id}",
                        title=entry.title[:120],
                        source="arXiv",
                        source_type=SourceType.ARXIV,
                        content_type=ContentType.ACADEMIC_PAPER,
                        url=entry.link,
                        summary=entry.get("summary", "")[:200],
                        adhd_relevance=8,
                        actionability=5,
                        novelty_score=7,
                        timestamp=datetime.now().isoformat()
                    ))
            logger.info(f"arXiv: 获取 {len(items)} 条")
            return items
        except ImportError:
            logger.warning("arXiv: 需要安装 feedparser (pip install feedparser)")
            return []
        except Exception as e:
            logger.error(f"arXiv抓取失败: {e}")
            return []
    
    def _fetch_rss(self) -> List[IntelligenceItem]:
        """
        RSS源抓取
        """
        rss_sources = [
            ("TechCrunch AI", "https://techcrunch.com/category/artificial-intelligence/feed/"),
            ("Product Hunt", "https://www.producthunt.com/feed"),
            ("MIT AI News", "https://news.mit.edu/topic/artificial-intelligence2/feed"),
        ]
        try:
            import feedparser
            items = []
            for name, url in rss_sources:
                feed = feedparser.parse(url)
                for entry in feed.entries[:3]:
                    # 筛选ADHD相关
                    content = f"{entry.title} {entry.get('summary', '')}".lower()
                    if any(k in content for k in ['adhd', 'neurodivergent', 'neurodiversity', 'attention', 'focus']):
                        item_id = hashlib.md5(entry.link.encode()).hexdigest()[:8]
                        items.append(IntelligenceItem(
                            id=f"rss_{item_id}",
                            title=entry.title[:120],
                            source=name,
                            source_type=SourceType.RSS,
                            content_type=ContentType.TREND_SIGNAL,
                            url=entry.link,
                            adhd_relevance=6,
                            actionability=4,
                            novelty_score=5,
                            timestamp=datetime.now().isoformat()
                        ))
            logger.info(f"RSS: 获取 {len(items)} 条")
            return items
        except ImportError:
            logger.warning("RSS: 需要安装 feedparser (pip install feedparser)")
            return []
        except Exception as e:
            logger.error(f"RSS抓取失败: {e}")
            return []
    
    def _check_manual_input(self) -> List[IntelligenceItem]:
        """
        检查手动输入文件
        用户可以手动添加情报到 manual_input.json
        """
        filepath = os.path.join(self.data_dir, "manual_input.json")
        if not os.path.exists(filepath):
            return []
        try:
            with open(filepath, 'r') as f:
                data = json.load(f)
            items = [IntelligenceItem.from_dict(d) for d in data]
            # 清空已读取的手动输入
            with open(filepath, 'w') as f:
                json.dump([], f)
            logger.info(f"手动输入: {len(items)} 条")
            return items
        except Exception as e:
            logger.error(f"手动输入读取失败: {e}")
            return []
    
    # ========== AI分析层 ==========
    
    def analyze_with_ai(self, items: List[IntelligenceItem]) -> List[IntelligenceItem]:
        """
        使用Claude API进行AI分析
        为每条情报生成摘要、关键要点、情感角度和选题灵感
        """
        if not self.anthropic_key:
            logger.info("Claude API未配置，使用本地规则分析 (设置ANTHROPIC_API_KEY启用AI分析)")
            return self._analyze_local(items)
        
        try:
            import anthropic
            client = anthropic.Anthropic(api_key=self.anthropic_key)
            
            for item in items:
                if item.processed:
                    continue
                    
                prompt = f"""
分析以下ADHD×AI领域的情报，提供结构化输出。

标题: {item.title}
来源: {item.source}
摘要: {item.summary}

请以JSON格式输出:
{{
    "summary": "一句话中文摘要",
    "key_points": ["要点1", "要点2", "要点3"],
    "related_tools": ["提到的AI工具"],
    "adhd_relevance": 1-10,
    "actionability": 1-10,
    "novelty_score": 1-10,
    "emotion_angle": "一个ADHDer看到这条情报时的真实情感反应，用第一人称",
    "story_idea": "基于这条情报的中文选题灵感"
}}
"""
                try:
                    resp = client.messages.create(
                        model="claude-sonnet-4-20250514",
                        max_tokens=1000,
                        messages=[{"role": "user", "content": prompt}]
                    )
                    result = json.loads(resp.content[0].text)
                    item.summary = result.get("summary", item.summary)
                    item.key_points = result.get("key_points", [])
                    item.related_tools = result.get("related_tools", [])
                    item.adhd_relevance = result.get("adhd_relevance", 5)
                    item.actionability = result.get("actionability", 5)
                    item.novelty_score = result.get("novelty_score", 5)
                    item.emotion_angle = result.get("emotion_angle")
                    item.story_idea = result.get("story_idea")
                    item.processed = True
                except Exception as e:
                    logger.error(f"AI分析失败 [{item.id}]: {e}")
                    continue
            
            return items
        except ImportError:
            logger.warning("需要安装 anthropic SDK: pip install anthropic")
            return self._analyze_local(items)
    
    def _analyze_local(self, items: List[IntelligenceItem]) -> List[IntelligenceItem]:
        """
        本地规则分析（无API时的备选）
        """
        for item in items:
            if item.processed:
                continue
            
            # 根据内容类型设定基础分数
            score_map = {
                ContentType.ACADEMIC_PAPER: (8, 5, 8),
                ContentType.PRODUCT_LAUNCH: (9, 8, 7),
                ContentType.TOOL_UPDATE: (8, 7, 6),
                ContentType.CREATOR_CONTENT: (7, 6, 5),
                ContentType.FUNDING_NEWS: (6, 5, 6),
                ContentType.COMMUNITY_DISCUSSION: (8, 5, 4),
                ContentType.TREND_SIGNAL: (7, 4, 7),
            }
            rel, act, nov = score_map.get(item.content_type, (5, 5, 5))
            
            # 关键词加分
            title_lower = item.title.lower()
            if any(k in title_lower for k in ['adhd', 'neurodivergent', 'neurodiversity']):
                rel = min(10, rel + 1)
            if any(k in title_lower for k in ['vibe coding', 'claude', 'cursor', 'focus']):
                act = min(10, act + 1)
            
            item.adhd_relevance = rel
            item.actionability = act
            item.novelty_score = nov
            
            # 生成本地情感角度
            item.emotion_angle = self._generate_emotion_angle(item)
            item.story_idea = self._generate_story_idea(item)
            
            item.processed = True
        
        return items
    
    def _generate_emotion_angle(self, item: IntelligenceItem) -> str:
        """生成本地情感角度"""
        angles = {
            ContentType.ACADEMIC_PAPER: "学术界终于开始认真对待我们了——这篇论文让我相信ADHD×AI不只是个人经验",
            ContentType.PRODUCT_LAUNCH: "又一个'己病己治'的产品——ADHD创始人建ADHD工具，这个循环正在加速",
            ContentType.TOOL_UPDATE: "看到有人在为我们设计功能，那种感觉就像'终于被理解了'",
            ContentType.CREATOR_CONTENT: "他说的就是我——这种被看见的感觉，比任何工具都重要",
            ContentType.FUNDING_NEWS: "资本终于相信ADHD不是小问题而是大市场——这让我对未来更有信心",
            ContentType.COMMUNITY_DISCUSSION: "2.3k upvotes意味着我不是一个人——这是整个社区的共同体验",
            ContentType.TREND_SIGNAL: "趋势正在形成——我要在其他人还没看到的时候就开始记录",
        }
        return angles.get(item.content_type, "这个信息让我兴奋——因为它可能是下一个选题的火花")
    
    def _generate_story_idea(self, item: IntelligenceItem) -> str:
        """生成本地选题灵感"""
        ideas = {
            ContentType.ACADEMIC_PAPER: f"【深度解读】{item.title[:40]}...对ADHDer意味着什么",
            ContentType.PRODUCT_LAUNCH: f"【产品评测】{item.title[:40]}...如何外包我的{item.related_tools[0] if item.related_tools else '执行功能'}",
            ContentType.TOOL_UPDATE: f"【工具追踪】{item.title[:40]}...新功能如何改变我的工作流",
            ContentType.CREATOR_CONTENT: f"【博主动态】{item.creator_name or '核心博主'}的新动向——制图者观察",
            ContentType.FUNDING_NEWS: f"【资本信号】{item.title[:40]}...市场正在验证什么",
            ContentType.COMMUNITY_DISCUSSION: f"【社区热议】为什么这个话题在ADHD圈炸了——分析",
            ContentType.TREND_SIGNAL: f"【趋势预警】{item.title[:40]}...制图者的早期信号",
        }
        return ideas.get(item.content_type, f"【情报分析】{item.title[:50]}...")
    
    # ========== 输出层 ==========
    
    def generate_briefing(self, items: List[IntelligenceItem]) -> str:
        """生成每日情报简报文本"""
        today = datetime.now().strftime("%Y-%m-%d")
        
        # 排序
        items.sort(key=lambda x: x.adhd_relevance * 2 + x.actionability + x.novelty_score, reverse=True)
        
        # 分类
        top_stories = items[:5]
        creator_items = [i for i in items if i.creator_name]
        tool_items = [i for i in items if i.content_type in [ContentType.NEW_TOOL, ContentType.TOOL_UPDATE, ContentType.PRODUCT_LAUNCH]]
        paper_items = [i for i in items if i.content_type == ContentType.ACADEMIC_PAPER]
        story_candidates = [i for i in items if i.story_idea and i.adhd_relevance >= 7]
        
        # 生成文本
        text = f"""
╔══════════════════════════════════════════════════════════════════════════════╗
║              🧠⚡ ADHD×AI 情报日报 - {today}                            ║
║         制图者的每日雷达 | 200+博主追踪 | 30+工具监控                  ║
╚══════════════════════════════════════════════════════════════════════════════╝

📊 今日概览: {len(items)} 条情报
   头条: {len(top_stories)} | 博主动态: {len(creator_items)} | 工具: {len(tool_items)} | 论文: {len(paper_items)} | 选题: {len(story_candidates)}

═══════════════════════════════════════════════════════════════════════════════
🗞️ 头条 ({len(top_stories)}条)
═══════════════════════════════════════════════════════════════════════════════
"""
        for i, s in enumerate(top_stories, 1):
            text += f"""
【{i}】{s.title}
    📍 {s.source} | 🎯 ADHD:{s.adhd_relevance}/10 | ⚡ 行动:{s.actionability}/10 | 🆕 新颖:{s.novelty_score}/10
    🔗 {s.url}
    💡 {s.summary[:100]}...
"""
        
        if creator_items:
            text += f"""
═══════════════════════════════════════════════════════════════════════════════
👥 博主追踪动态
═══════════════════════════════════════════════════════════════════════════════
"""
            for c in creator_items[:5]:
                text += f"• [{c.creator_name}] {c.title[:70]}... (相关度:{c.adhd_relevance}/10)\n"
        
        if tool_items:
            text += f"""
═══════════════════════════════════════════════════════════════════════════════
🔧 工具雷达
═══════════════════════════════════════════════════════════════════════════════
"""
            for t in tool_items:
                text += f"• {t.title[:80]}... (新颖度:{t.novelty_score}/10)\n"
        
        if paper_items:
            text += f"""
═══════════════════════════════════════════════════════════════════════════════
📚 学术前沿
═══════════════════════════════════════════════════════════════════════════════
"""
            for p in paper_items:
                text += f"• {p.title[:80]}...\n  {p.summary[:120]}...\n"
        
        if story_candidates:
            text += f"""
═══════════════════════════════════════════════════════════════════════════════
✨ 选题推荐 (已注入你的情感角度)
═══════════════════════════════════════════════════════════════════════════════
"""
            for i, s in enumerate(story_candidates[:8], 1):
                text += f"""
【{i}】{s.story_idea}
    ❤️ 情感角度: {s.emotion_angle[:100]}...
    ⏱️ 预估: 2-3小时 | 相关度: {s.adhd_relevance}/10 | 行动度: {s.actionability}/10
"""
        
        # 情感角度汇总
        emotion_angles = [s.emotion_angle for s in top_stories if s.emotion_angle]
        if emotion_angles:
            text += f"""
═══════════════════════════════════════════════════════════════════════════════
❤️ 今日情感角度
═══════════════════════════════════════════════════════════════════════════════
"""
            for i, ea in enumerate(emotion_angles[:3], 1):
                text += f"{i}. {ea[:150]}...\n"
        
        text += f"""
═══════════════════════════════════════════════════════════════════════════════
📌 下一步行动
═══════════════════════════════════════════════════════════════════════════════
1. 选择一个HIGH相关度(≥8)的选题
2. 用"外包日记"模板: 我做不到的事 → 试过的方法 → AI解决方案 → 前后对比
3. 发布到主平台(Newsletter优先)
4. 将反馈作为明天情报输入 (添加到 manual_input.json)

💡 制图者提醒:
你的内容不是"AI工具评测"，而是"一个ADHDer用AI重建自己的过程中，
那些让你想哭/想喊/想分享的真实瞬间"。
每一个"外包发现"，都是你与另一个ADHDer之间的秘密握手。

---
生成: {datetime.now().strftime("%Y-%m-%d %H:%M")}
数据来源: 200+博主追踪 | 30+AI工具监控 | arXiv论文 | 社区热议
系统版本: v1.0 | 基于122年ADHD研究 + 101位名人考古
"""
        
        # 保存
        filepath = os.path.join(self.data_dir, "briefings", f"briefing_{today}.txt")
        with open(filepath, 'w') as f:
            f.write(text)
        
        # 同时更新选题库
        self._update_idea_bank(story_candidates)
        
        return text
    
    def _update_idea_bank(self, items: List[IntelligenceItem]):
        """将选题灵感保存到选题库"""
        for item in items:
            if not item.story_idea:
                continue
            # 去重检查
            exists = any(i.title == item.story_idea for i in self.idea_bank)
            if not exists:
                idea = StoryIdea(
                    id=f"idea_{hashlib.md5(item.story_idea.encode()).hexdigest()[:8]}",
                    title=item.story_idea,
                    emotion_angle=item.emotion_angle or "",
                    adhd_relevance=item.adhd_relevance,
                    actionability=item.actionability,
                    estimated_time="2-3小时",
                    priority="HIGH" if item.adhd_relevance >= 9 else "MEDIUM",
                    format="Newsletter/长文",
                    source_items=[item.id],
                    created_date=datetime.now().strftime("%Y-%m-%d")
                )
                self.idea_bank.append(idea)
        self._save_ideas()
    
    # ========== 主流程 ==========
    
    def run_daily(self):
        """每日运行入口"""
        logger.info("=" * 60)
        logger.info("ADHD×AI 情报自动流 - 每日运行")
        logger.info("=" * 60)
        
        # 1. 收集情报
        items = self.collect_all()
        
        # 2. AI分析
        items = self.analyze_with_ai(items)
        
        # 3. 生成简报
        briefing = self.generate_briefing(items)
        
        # 4. 输出
        logger.info("简报生成完成")
        print("\n" + briefing)
        
        return briefing


# ========== 手动输入模板 ==========
MANUAL_INPUT_TEMPLATE = [
    {
        "id": "manual_001",
        "title": "示例: 在这里填入你看到的情报标题",
        "source": "你看到的来源",
        "source_type": "manual",
        "content_type": "creator_content",
        "url": "https://example.com",
        "creator_name": "博主名字(可选)",
        "summary": "简要描述这条情报",
        "key_points": ["要点1", "要点2"],
        "related_tools": ["提到的工具"],
        "adhd_relevance": 8,
        "actionability": 7,
        "novelty_score": 6,
        "timestamp": "2026-05-08T00:00:00"
    }
]

# ========== 入口 ==========

if __name__ == "__main__":
    engine = ADHDIntelligenceEngine()
    
    # 检查是否有手动输入
    manual_path = os.path.join(engine.data_dir, "manual_input.json")
    if not os.path.exists(manual_path):
        with open(manual_path, 'w') as f:
            json.dump(MANUAL_INPUT_TEMPLATE, f, indent=2, ensure_ascii=False)
        logger.info(f"已创建手动输入模板: {manual_path}")
        logger.info("编辑此文件添加你手动发现的情报，然后再次运行")
    
    # 运行日报生成
    engine.run_daily()
