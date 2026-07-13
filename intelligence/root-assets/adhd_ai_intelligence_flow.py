
"""
================================================================================
ADHD×AI 情报自动流系统 (ADHD-AI Intelligence Flow System)
================================================================================
版本: v1.0
作者: ADHD内容创业者专用
功能: 自动追踪ADHD相关AI博主动态 → 智能分析 → 生成洞察 → 准备发布

核心设计理念:
- ADHD友好: 短时爆发(15分钟)、即时反馈、多巴胺驱动
- 信息节食: 只关注30位核心目标，避免信息过载
- 自动化: 机器做收集和初筛，人做最终判断和创作
- 一鱼多吃: 一次采集，多平台变形输出
================================================================================
"""

import json
import hashlib
import re
from datetime import datetime, timedelta
from typing import List, Dict, Optional
from dataclasses import dataclass, asdict
from collections import defaultdict

# =============================================================================
# 1. 数据模型层 (Data Models)
# =============================================================================

@dataclass
class RawItem:
    """原始采集数据项"""
    id: str
    source: str           # twitter/wechat/bilibili/youtube/rss
    author: str           # 博主名称
    author_handle: str    # 账号handle
    content: str          # 原始内容
    url: str              # 原始链接
    published_at: str     # 发布时间 ISO格式
    media_urls: List[str] # 配图/视频URL
    raw_metadata: Dict    # 原始元数据

    def __post_init__(self):
        if not self.id:
            self.id = hashlib.md5(f"{self.source}:{self.author}:{self.content[:100]}".encode()).hexdigest()[:16]

@dataclass
class AnalysisResult:
    """分析结果"""
    item_id: str
    adhd_relevance_score: float  # 0-1, ADHD相关度
    ai_topic_score: float        # 0-1, AI主题相关度
    sentiment: str               # positive/negative/neutral/excited/controversial
    key_concepts: List[str]      # 提取的关键概念
    summary: str                 # 自动摘要
    importance_score: float      # 0-1, 综合重要性
    recommended_action: str      # 建议操作: share/analyze/ignore/urgent
    platform_adaptations: Dict   # 各平台适配建议

@dataclass
class DailyDigest:
    """每日情报摘要"""
    date: str
    total_items: int
    high_priority_items: List[AnalysisResult]
    adhd_blogger_activities: Dict[str, int]  # 博主名: 活跃数
    trending_concepts: List[str]
    recommended_topics: List[str]  # 推荐你写的选题
    raw_digest_text: str

# =============================================================================
# 2. 配置层 (Configuration)
# =============================================================================

class ADHDConfig:
    """系统配置 - 专为ADHD大脑设计的信息节食方案"""

    # ADHD关键词词典 - 用于检测ADHD相关内容
    ADHD_KEYWORDS = [
        "adhd", "attention", "hyperfocus", "dopamine", "procrastination",
        "impulsivity", "creativity", "neurodiversity", "neurodivergent",
        "founder", "startup", "burnout", "productivity", "workflow",
        "energy", "burst", "focus", "distraction", "time management",
        "karpathy", "elon", "musk", "sam altman", "LeCun",
    ]

    # AI关键词词典
    AI_KEYWORDS = [
        "ai", "artificial intelligence", "llm", "gpt", "chatgpt", "claude",
        "agent", "agi", "openai", "deepmind", "anthropic", "nvidia",
        "transformer", "prompt", "fine-tuning", "reasoning",
        "deepseek", "sora", "midjourney", "stable diffusion", "aigc",
        "vibe coding", "english is the hottest",
    ]

    # 情绪/爆款信号词
    SIGNAL_WORDS = {
        "urgent": ["breaking", "leaked", "exposed", "exclusive", "突发", "震惊"],
        "controversial": ["wrong", "vs", "debate", "fud", "骂战", "反驳"],
        "excited": ["amazing", "incredible", "炸裂", "wow", "what a time"],
        "trending": ["trending", "viral", "热门", "热搜", "爆火"],
    }

    # ADHD友好阈值设置
    MAX_DAILY_ITEMS = 50
    MIN_ADHD_SCORE = 0.15
    MIN_AI_SCORE = 0.20
    MIN_IMPORTANCE = 0.40

    # 博主监控列表
    WATCHLIST = {
        "twitter": [
            {"handle": "karpathy", "name": "Andrej Karpathy", "priority": "S", "adhd_type": "Burst型"},
            {"handle": "ylecun", "name": "Yann LeCun", "priority": "S", "adhd_type": "高频对线型"},
            {"handle": "rowancheung", "name": "Rowan Cheung", "priority": "A", "adhd_type": "信息猎手型"},
            {"handle": "emollick", "name": "Ethan Mollick", "priority": "A", "adhd_type": "实验驱动型"},
            {"handle": "sama", "name": "Sam Altman", "priority": "A", "adhd_type": "多线程型"},
            {"handle": "drjimfan", "name": "Jim Fan", "priority": "A", "adhd_type": "跳跃型"},
            {"handle": "lexfridman", "name": "Lex Fridman", "priority": "B", "adhd_type": "规律型"},
            {"handle": "geoffreyhinton", "name": "Geoffrey Hinton", "priority": "B", "adhd_type": "审慎型"},
        ],
        "rss": [
            {"name": "The Rundown AI", "url": "https://www.therundown.ai/rss", "priority": "A"},
            {"name": "One Useful Thing", "url": "https://oneusefulthing.substack.com/feed", "priority": "A"},
            {"name": "Import AI", "url": "https://importai.substack.com/feed", "priority": "B"},
            {"name": "The Batch", "url": "https://www.deeplearning.ai/the-batch/rss", "priority": "B"},
        ],
    }

# =============================================================================
# 3. 采集层 (Collection Engine)
# =============================================================================

class CollectionEngine:
    """数据采集引擎 - ADHD友好的信息节食采集器"""

    def __init__(self, config: ADHDConfig):
        self.config = config
        self.collected_count = 0

    def collect_twitter(self, handle: str, mock_mode: bool = True) -> List[RawItem]:
        """采集Twitter博主最新动态"""
        items = []

        if mock_mode:
            mock_tweets = self._generate_mock_tweets(handle)
            for tweet in mock_tweets:
                items.append(RawItem(
                    id="",
                    source="twitter",
                    author=tweet["author"],
                    author_handle=f"@{handle}",
                    content=tweet["text"],
                    url=f"https://twitter.com/{handle}/status/mock",
                    published_at=tweet["time"],
                    media_urls=[],
                    raw_metadata={"likes": tweet.get("likes", 0), "retweets": tweet.get("retweets", 0)}
                ))
        else:
            # 真实API调用需要 tweepy 库
            pass

        self.collected_count += len(items)
        return items

    def collect_rss(self, feed_url: str, mock_mode: bool = True) -> List[RawItem]:
        """采集RSS订阅源"""
        items = []

        if mock_mode:
            mock_articles = self._generate_mock_rss(feed_url)
            for article in mock_articles:
                items.append(RawItem(
                    id="",
                    source="rss",
                    author=article["author"],
                    author_handle="",
                    content=article["title"] + "\n" + article["summary"],
                    url=article["url"],
                    published_at=article["time"],
                    media_urls=[],
                    raw_metadata={"feed": feed_url}
                ))
        else:
            # 真实RSS解析需要 feedparser 库
            pass

        self.collected_count += len(items)
        return items

    def _generate_mock_tweets(self, handle: str) -> List[Dict]:
        """基于真实博主风格生成模拟推文"""
        now = datetime.now().isoformat()

        templates = {
            "karpathy": [
                {"author": "Andrej Karpathy", "text": "vibe coding is real. spent 3 hours in hyperfocus mode building a neural net visualizer. forgot to eat. the code basically wrote itself through pure intuition.", "time": now, "likes": 5200, "retweets": 890},
                {"author": "Andrej Karpathy", "text": "thinking about digital hygiene again. ADHD brain + infinite scroll = dopamine casino. built a chrome extension that blocks Twitter after 3 consecutive likes on my own tweets.", "time": now, "likes": 3400, "retweets": 560},
            ],
            "ylecun": [
                {"author": "Yann LeCun", "text": "People who claim LLMs are thinking fundamentally misunderstand what reasoning is. My cat reasons better than GPT-4 about physics. Heres why... [thread]", "time": now, "likes": 8900, "retweets": 2100},
                {"author": "Yann LeCun", "text": "ADHD is not a disorder, its a different operating system. The problem is society is built for batch processing brains, not event-driven ones.", "time": now, "likes": 12000, "retweets": 3400},
            ],
            "rowancheung": [
                {"author": "Rowan Cheung", "text": "BREAKING: OpenAI just dropped something huge at 3am. 5 things you need to know before your morning coffee...", "time": now, "likes": 2100, "retweets": 890},
                {"author": "Rowan Cheung", "text": "Daily AI Digest (Apr 28): - Meta releases Llama 4 - DeepSeek V4 rumored - New ADHD productivity app using AI agents - Elon vs LeCun round 47", "time": now, "likes": 1500, "retweets": 600},
            ],
            "emollick": [
                {"author": "Ethan Mollick", "text": "Just ran an experiment: gave 50 ADHD students access to Claude 4 for a week. Result: 73% reported better focus because the AI handled their idea overflow. Paper coming soon.", "time": now, "likes": 6700, "retweets": 1800},
                {"author": "Ethan Mollick", "text": "The most underrated AI use case for neurodivergent folks: using LLMs as a cognitive prosthetic. Not replacement, but scaffolding. Thread on how I use it daily...", "time": now, "likes": 5400, "retweets": 1200},
            ],
        }
        return templates.get(handle, [{"author": handle, "text": f"Mock tweet from @{handle} about AI and ADHD", "time": now, "likes": 100}])

    def _generate_mock_rss(self, feed_url: str) -> List[Dict]:
        """生成模拟RSS文章"""
        now = datetime.now().isoformat()
        return [
            {"title": "ADHD Entrepreneurs Are Building the Next Wave of AI Startups", "summary": "New research shows ADHD founders are 6x more likely to build AI companies. Why neurodiversity is the secret weapon of the AI era.", "url": "https://example.com/1", "author": "The Rundown AI", "time": now},
            {"title": "How Andrej Karpathy Uses AI to Manage His ADHD", "summary": "Inside the tools and workflows that help the legendary AI researcher stay focused in a world of infinite distractions.", "url": "https://example.com/2", "author": "The Rundown AI", "time": now},
        ]

# =============================================================================
# 4. 分析引擎 (Analysis Engine)
# =============================================================================

class AnalysisEngine:
    """内容分析引擎 - ADHD×AI相关性评分系统"""

    def __init__(self, config: ADHDConfig):
        self.config = config

    def analyze(self, item: RawItem) -> AnalysisResult:
        """分析单个内容项"""
        content_lower = item.content.lower()

        adhd_score = self._calculate_keyword_score(content_lower, self.config.ADHD_KEYWORDS)
        ai_score = self._calculate_keyword_score(content_lower, self.config.AI_KEYWORDS)
        sentiment = self._detect_sentiment(content_lower)
        concepts = self._extract_concepts(item.content)
        summary = self._generate_summary(item.content)
        importance = self._calculate_importance(adhd_score, ai_score, sentiment, item)
        action = self._recommend_action(adhd_score, ai_score, importance, sentiment)
        adaptations = self._generate_platform_adaptations(item, summary, concepts)

        return AnalysisResult(
            item_id=item.id,
            adhd_relevance_score=round(adhd_score, 2),
            ai_topic_score=round(ai_score, 2),
            sentiment=sentiment,
            key_concepts=concepts,
            summary=summary,
            importance_score=round(importance, 2),
            recommended_action=action,
            platform_adaptations=adaptations
        )

    def _calculate_keyword_score(self, content: str, keywords: List[str]) -> float:
        """基于关键词匹配计算相关度分数"""
        if not content:
            return 0.0
        matched = sum(1 for kw in keywords if kw.lower() in content)
        return min(1.0, (matched / 3) ** 0.7)

    def _detect_sentiment(self, content: str) -> str:
        """检测情绪信号"""
        for sentiment_type, words in self.config.SIGNAL_WORDS.items():
            for word in words:
                if word.lower() in content:
                    return sentiment_type
        return "neutral"

    def _extract_concepts(self, content: str) -> List[str]:
        """提取关键概念"""
        concepts = []
        ai_products = ["GPT-4", "Claude", "Llama", "Sora", "Midjourney", "ChatGPT", "DeepSeek"]
        for product in ai_products:
            if product.lower() in content.lower():
                concepts.append(product)
        adhd_concepts = ["hyperfocus", "dopamine", "neurodiversity", "ADHD", "creativity", "burnout"]
        for concept in adhd_concepts:
            if concept.lower() in content.lower():
                concepts.append(concept)
        return list(set(concepts))[:5]

    def _generate_summary(self, content: str, max_length: int = 200) -> str:
        """生成自动摘要"""
        if len(content) <= max_length:
            return content
        sentences = re.split(r'[.!?。！？]', content)
        for sent in sentences:
            if len(sent) > 20 and any(kw in sent.lower() for kw in ["ai", "adhd", "new", "announced"]):
                return sent.strip()[:max_length]
        return content[:max_length] + "..."

    def _calculate_importance(self, adhd_score: float, ai_score: float, sentiment: str, item: RawItem) -> float:
        """计算综合重要性分数"""
        base = adhd_score * 0.4 + ai_score * 0.4
        sentiment_bonus = {"urgent": 0.25, "controversial": 0.20, "excited": 0.15, "trending": 0.15, "neutral": 0.05}.get(sentiment, 0)

        priority_bonus = 0
        for platform, bloggers in self.config.WATCHLIST.items():
            for b in bloggers:
                if b["name"] == item.author or b.get("handle", "") == item.author_handle.replace("@", ""):
                    priority_bonus = {"S": 0.20, "A": 0.10, "B": 0.05}.get(b.get("priority", "C"), 0)

        engagement = 0
        raw = item.raw_metadata
        if "likes" in raw and raw["likes"] > 1000:
            engagement = min(0.10, raw["likes"] / 100000)

        return min(1.0, base + sentiment_bonus + priority_bonus + engagement)

    def _recommend_action(self, adhd_score: float, ai_score: float, importance: float, sentiment: str) -> str:
        """推荐操作"""
        if importance > 0.85:
            return "urgent"
        elif importance > 0.65:
            return "analyze"
        elif importance > 0.45:
            return "share"
        return "ignore"

    def _generate_platform_adaptations(self, item: RawItem, summary: str, concepts: List[str]) -> Dict:
        """生成各平台适配建议"""
        return {
            "twitter": {
                "format": "短推/thread",
                "suggested_text": f"🔥 {item.author}刚发了关于{'/'.join(concepts[:2]) if concepts else 'AI'}的内容:\n\n{summary[:100]}...\n\n你的ADHD视角解读: ___",
                "length_limit": 280,
                "best_time": "22:00-24:00"
            },
            "wechat": {
                "format": "公众号文章",
                "suggested_title": f"{item.author}最新观点：{'/'.join(concepts[:2]) if concepts else 'AI新动态'}——ADHD视角解读",
                "suggested_structure": "开头钩子→核心观点→ADHD视角分析→行动建议",
                "length_range": "1500-3000字",
                "best_time": "6:00-8:00 或 22:00-24:00"
            },
            "xiaohongshu": {
                "format": "图文笔记",
                "suggested_title": f"🔥 {item.author}又输出了！ADHD人看{'/'.join(concepts[:1]) if concepts else 'AI'}",
                "suggested_hook": "3句话讲清 + 1张关键截图",
                "length_limit": "1000字",
                "best_time": "12:00-13:00 或 19:00-20:00"
            },
            "bilibili": {
                "format": "短视频/动态",
                "suggested_script": f"3秒钩子→15秒核心→5秒ADHD视角→5秒互动提问",
                "length_range": "30-60秒",
                "best_time": "18:00-22:00"
            }
        }

# =============================================================================
# 5. 每日摘要生成器
# =============================================================================

class DailyDigestGenerator:
    """每日情报摘要生成器"""

    def __init__(self, config: ADHDConfig):
        self.config = config

    def generate(self, results: List[AnalysisResult], date: str = None) -> DailyDigest:
        """生成每日情报摘要"""
        if date is None:
            date = datetime.now().strftime("%Y-%m-%d")

        high_priority = [r for r in results if r.importance_score >= self.config.MIN_IMPORTANCE]
        high_priority.sort(key=lambda x: x.importance_score, reverse=True)

        blogger_activity = defaultdict(int)
        all_concepts = []
        for r in results:
            all_concepts.extend(r.key_concepts)
        concept_counts = defaultdict(int)
        for c in all_concepts:
            concept_counts[c] += 1
        trending = [c for c, count in sorted(concept_counts.items(), key=lambda x: x[1], reverse=True)[:5]]

        recommended = self._generate_topic_ideas(high_priority, trending)
        digest_text = self._format_digest_text(date, high_priority, trending, recommended)

        return DailyDigest(
            date=date,
            total_items=len(results),
            high_priority_items=high_priority[:10],
            adhd_blogger_activities=dict(blogger_activity),
            trending_concepts=trending,
            recommended_topics=recommended,
            raw_digest_text=digest_text
        )

    def _generate_topic_ideas(self, high_priority: List[AnalysisResult], trending: List[str]) -> List[str]:
        """生成推荐选题"""
        ideas = []
        for concept in trending[:3]:
            ideas.append(f"{concept}对ADHD大脑的影响：效率翻倍还是分心陷阱？")
        for result in high_priority[:3]:
            ideas.append(f"从ADHD视角解读：{result.summary[:30]}...")
        ideas.extend([
            "今日AI圈ADHD含量最高的3个动态",
            "ADHD创始人如何用AI工具管理信息过载",
        ])
        return list(set(ideas))[:5]

    def _format_digest_text(self, date: str, high_priority: List[AnalysisResult], 
                           trending: List[str], recommended: List[str]) -> str:
        """格式化摘要文本"""
        lines = [
            f"# ADHD×AI 情报摘要 [{date}]",
            "",
            f"📊 今日采集: {len(high_priority)}条高价值动态",
            f"🔥 趋势概念: {', '.join(trending) if trending else '暂无'}",
            "",
            "## 高优先级动态",
            ""
        ]
        for i, r in enumerate(high_priority[:5], 1):
            lines.extend([
                f"{i}. **{r.sentiment.upper()}** | ADHD:{r.adhd_relevance_score} | AI:{r.ai_topic_score} | 重要性:{r.importance_score}",
                f"   > {r.summary[:120]}...",
                f"   💡 建议操作: {r.recommended_action}",
                ""
            ])
        lines.extend(["## 💡 今日推荐选题", ""])
        for i, topic in enumerate(recommended[:3], 1):
            lines.append(f"{i}. {topic}")
        return "\n".join(lines)

# =============================================================================
# 6. 主控制器
# =============================================================================

class ADHDIntelligenceFlow:
    """ADHD×AI情报自动流主控制器"""

    def __init__(self):
        self.config = ADHDConfig()
        self.collector = CollectionEngine(self.config)
        self.analyzer = AnalysisEngine(self.config)
        self.digest_gen = DailyDigestGenerator(self.config)
        self.history = []

    def run_daily_flow(self, mock_mode: bool = True) -> DailyDigest:
        """执行每日情报采集-分析-摘要完整流程"""
        print("=" * 60)
        print("🧠 ADHD×AI 情报自动流启动")
        print("=" * 60)

        all_items = []
        all_results = []

        print("\n📡 [1/4] 采集Twitter ADHD博主动态...")
        for blogger in self.config.WATCHLIST["twitter"]:
            items = self.collector.collect_twitter(blogger["handle"], mock_mode=mock_mode)
            all_items.extend(items)
            print(f"   ✅ @{blogger['handle']} ({blogger['name']}) - {len(items)}条")

        print("\n📡 [2/4] 采集RSS订阅源...")
        for feed in self.config.WATCHLIST["rss"]:
            items = self.collector.collect_rss(feed["url"], mock_mode=mock_mode)
            all_items.extend(items)
            print(f"   ✅ {feed['name']} - {len(items)}条")

        print(f"\n🔬 [3/4] 分析 {len(all_items)} 条内容...")
        for item in all_items:
            result = self.analyzer.analyze(item)
            all_results.append(result)
            if result.importance_score >= self.config.MIN_IMPORTANCE:
                print(f"   🔥 [{result.recommended_action.upper()}] ADHD:{result.adhd_relevance_score} | "
                      f"AI:{result.ai_topic_score} | 重要性:{result.importance_score} | {item.author}")

        print("\n📋 [4/4] 生成每日情报摘要...")
        digest = self.digest_gen.generate(all_results)
        self.history.append({"date": digest.date, "digest": asdict(digest), "results": [asdict(r) for r in all_results]})

        print("\n" + "=" * 60)
        print(digest.raw_digest_text)
        print("=" * 60)

        return digest

    def generate_content(self, digest: DailyDigest, platform: str = "wechat") -> str:
        """生成指定平台的发布内容"""
        if not digest.high_priority_items:
            return "暂无足够内容。"

        top_item = digest.high_priority_items[0]
        adaptations = top_item.platform_adaptations

        if platform in adaptations:
            return adaptations[platform].get("suggested_text", 
                   adaptations[platform].get("suggested_title", "内容生成失败"))

        return f"""
【ADHD×AI情报速递】{digest.date}
今日发现 {digest.total_items} 条相关动态，{len(digest.high_priority_items)}条高价值。
🔥 最热趋势: {', '.join(digest.trending_concepts[:3]) if digest.trending_concepts else '暂无'}
💡 推荐选题:
{chr(10).join(f"{i+1}. {t}" for i, t in enumerate(digest.recommended_topics[:3]))}
#ADHD #AI #神经多样性
"""

    def export_data(self, filepath: str = "adhd_ai_flow_data.json"):
        """导出所有历史数据"""
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(self.history, f, ensure_ascii=False, indent=2)
        print(f"\n💾 数据已导出: {filepath} ({len(self.history)} 天历史)")


# =============================================================================
# 7. 运行演示
# =============================================================================

if __name__ == "__main__":
    flow = ADHDIntelligenceFlow()
    digest = flow.run_daily_flow(mock_mode=True)

    print("\n" + "=" * 60)
    print("📱 各平台发布内容生成")
    print("=" * 60)

    for platform in ["twitter", "wechat", "xiaohongshu"]:
        content = flow.generate_content(digest, platform=platform)
        print(f"\n--- {platform.upper()} ---")
        print(content[:300] + "..." if len(content) > 300 else content)

    flow.export_data("adhd_ai_flow_data.json")
    print("\n✅ ADHD×AI情报自动流演示完成！")
    print("\n💡 下一步: 配置真实API key，设置定时任务(cron)，开始自动运行！")
