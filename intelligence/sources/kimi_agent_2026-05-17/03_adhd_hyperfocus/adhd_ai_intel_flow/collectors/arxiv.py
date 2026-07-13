"""
arXiv 论文收集器 - 抓取 ADHD×AI 交叉领域最新论文
"""
import requests
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta
from typing import List
from collectors.base import BaseCollector, RawItem

class ArxivCollector(BaseCollector):
    """arXiv ADHD×AI 论文收集器"""

    API_URL = "http://export.arxiv.org/api/query"

    @property
    def source_name(self) -> str:
        return "arXiv"

    def collect(self) -> List[RawItem]:
        if not self.enabled:
            return []

        items = []
        keywords = self.config.get('keywords', ['ADHD'])
        categories = self.config.get('categories', [])
        max_results = self.config.get('max_results', 20)
        days_back = self.config.get('days_back', 7)

        # 构建搜索查询
        kw_query = " OR ".join([f'"{k}"' for k in keywords])
        cat_filter = " OR ".join([f"cat:{c}" for c in categories]) if categories else ""
        query = f"({kw_query})"
        if cat_filter:
            query = f"({kw_query}) AND ({cat_filter})"

        # 日期范围
        start_date = (datetime.now() - timedelta(days=days_back)).strftime("%Y%m%d")

        params = {
            "search_query": query,
            "start": 0,
            "max_results": max_results,
            "sortBy": "submittedDate",
            "sortOrder": "descending"
        }

        try:
            resp = requests.get(self.API_URL, params=params, timeout=30)
            resp.raise_for_status()

            root = ET.fromstring(resp.content)
            ns = {'atom': 'http://www.w3.org/2005/Atom'}

            for entry in root.findall('atom:entry', ns):
                title = entry.find('atom:title', ns)
                summary = entry.find('atom:summary', ns)
                link = entry.find('atom:link[@rel="alternate"]', ns)
                published = entry.find('atom:published', ns)
                authors = entry.findall('atom:author/atom:name', ns)

                if title is None:
                    continue

                title_text = title.text.replace('\n', ' ').strip() if title.text else ""
                summary_text = summary.text[:2000] if summary is not None and summary.text else ""
                url = link.get('href') if link is not None else ""

                # 提取作者
                author_names = [a.text for a in authors if a.text][:3]
                author_str = ", ".join(author_names) if author_names else None

                # 解析日期
                pub_date = None
                if published is not None and published.text:
                    try:
                        pub_date = datetime.fromisoformat(published.text.replace('Z', '+00:00'))
                    except:
                        pass

                items.append(RawItem(
                    source="arxiv",
                    source_name="arXiv",
                    title=title_text,
                    content=summary_text,
                    url=url,
                    author=author_str,
                    published_at=pub_date,
                    raw_data={"categories": categories}
                ))

        except Exception as e:
            print(f"[arXiv] 收集失败: {e}")

        print(f"[arXiv] 收集到 {len(items)} 篇论文")
        return items
