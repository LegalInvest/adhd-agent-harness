"""
Reddit 社区收集器 - 抓取 r/ADHD 等热门讨论
"""
import requests
from datetime import datetime
from typing import List
from collectors.base import BaseCollector, RawItem

class RedditCollector(BaseCollector):
    """Reddit ADHD 社区收集器"""

    BASE_URL = "https://www.reddit.com"

    @property
    def source_name(self) -> str:
        return "Reddit"

    def collect(self) -> List[RawItem]:
        if not self.enabled:
            return []

        items = []
        subreddits = self.config.get('subreddits', ['ADHD'])
        sort = self.config.get('sort', 'hot')
        limit = self.config.get('limit', 10)
        min_score = self.config.get('min_score', 50)

        headers = {
            "User-Agent": "ADHD-AI-Intel-Bot/1.0 (Research Purpose)"
        }

        for sub in subreddits:
            try:
                url = f"{self.BASE_URL}/r/{sub}/{sort}.json?limit={limit}"
                resp = requests.get(url, headers=headers, timeout=15)

                if resp.status_code != 200:
                    continue

                data = resp.json()
                posts = data.get('data', {}).get('children', [])

                for post in posts:
                    p = post.get('data', {})
                    score = p.get('score', 0)

                    # 过滤低质量帖
                    if score < min_score:
                        continue

                    title = p.get('title', '')
                    selftext = p.get('selftext', '')[:1500]
                    permalink = f"https://reddit.com{p.get('permalink', '')}"
                    author = p.get('author')
                    created_utc = p.get('created_utc')
                    num_comments = p.get('num_comments', 0)

                    # 简单AI相关性过滤
                    content_lower = (title + " " + selftext).lower()
                    ai_keywords = ['ai', 'artificial intelligence', 'chatgpt', 'claude', 'app', 
                                   'tool', 'software', 'digital', 'technology', 'machine learning',
                                   'automation', 'productivity', 'focus', 'medication', 'therapy']

                    relevance = sum(1 for k in ai_keywords if k in content_lower)

                    items.append(RawItem(
                        source="reddit",
                        source_name=f"r/{sub}",
                        title=title,
                        content=selftext or title,
                        url=permalink,
                        author=author,
                        published_at=datetime.fromtimestamp(created_utc) if created_utc else None,
                        raw_data={
                            "score": score,
                            "comments": num_comments,
                            "subreddit": sub,
                            "relevance_signals": relevance
                        },
                        score=score
                    ))

            except Exception as e:
                print(f"[Reddit r/{sub}] 收集失败: {e}")

        # 按热度排序
        items.sort(key=lambda x: x.score, reverse=True)
        print(f"[Reddit] 收集到 {len(items)} 条热门帖")
        return items[:limit * len(subreddits)]
