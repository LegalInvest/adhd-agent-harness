"""
情报资产语料：把从 adhd-ai-creator-intelligence 仓库迁入的知识资产
（创作者情报库 / 深度研究报告 / 考古与策略报告等 markdown）
作为语料注入知识萃取与 wiki 取材，让引擎复用作者已有的一手研究成果。
"""

from __future__ import annotations

import os

ROOT = os.path.join(os.path.dirname(os.path.dirname(__file__)), "intelligence")

# 高价值资产（相对 intelligence/ 的路径），按优先级排列
KEY_ASSETS = [
    "research/2026-06-24_ADHD×AI_深度研究报告.md",
    "research/ADHDxAI创作者情报库_v4_2026-07-03.md",
    "research/adhd_ai_cross_literature.md",
    "research/adhd_ai_creator_map_v2_2026-07-03.md",
    "root-assets/ADHDxAI创作者情报库_v4_2026-07-03.md",
    "root-assets/ADHD科技行业深度研究.md",
    "root-assets/ADHD每日10篇爆火策略.md",
    "root-assets/隐藏模式与反直觉洞察.md",
    "root-assets/Twitter内容考古报告.md",
    "root-assets/公众号内容解剖报告.md",
    "root-assets/跨平台变形策略报告.md",
    "root-assets/视频内容策略分析报告.md",
]

MAX_CHARS = 60_000


def as_articles() -> list[dict]:
    out, seen = [], set()
    for rel in KEY_ASSETS:
        path = os.path.join(ROOT, rel)
        if not os.path.exists(path):
            continue
        name = os.path.splitext(os.path.basename(path))[0]
        if name in seen:
            continue
        seen.add(name)
        try:
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()[:MAX_CHARS]
        except Exception:  # noqa: BLE001
            continue
        if len(content) < 200:
            continue
        out.append({
            "title": name,
            "content": content,
            "content_length": len(content),
            "url": "",
            "source_title": "ADHD×AI 创作者情报库（一手研究资产）",
            "domain": "adhd",
            "is_academic": False,
            "is_intelligence_asset": True,
        })
    return out


if __name__ == "__main__":
    arts = as_articles()
    print(f"情报资产 {len(arts)} 篇，共 {sum(a['content_length'] for a in arts)} 字")
    for a in arts:
        print(f"  - {a['title']} ({a['content_length']}字)")
