"""
主流程编排（研究驱动版）
完整情报闭环：
  全网检索(research) → 知识萃取(knowledge) → 证据评分(scorer)
  → 研究驱动进化(evolution) → 事实文章生成(generator)

体现核心机制：用大模型智能体全网检索获得最新情报，
萃取真实事实，形成新选题与新观点，好的留下、差的被最新发现替换。
"""

import json
import os

from engine.categories import CATEGORIES, get_all_topics
from engine.research import run_research
from engine.knowledge import (
    build_knowledge_base,
    save_knowledge_base,
    load_knowledge_base,
    KnowledgeRetriever,
)
from engine.evolution import EvolutionConfig, TopicEvolution
from engine.generator import generate_article, save_article
from engine.scorer import rank_topics


DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")
ARTICLES_DIR = os.path.join(DATA_DIR, "articles")
BLOG_CONTENT_DIR = os.path.join(
    os.path.dirname(os.path.dirname(__file__)), "blog", "src", "content", "articles"
)


def run_pipeline(refresh_research: bool = False, target_count: int = 400) -> None:
    """执行完整的研究驱动内容引擎流程"""
    print("=" * 60)
    print("ADHD × AI 内容引擎（研究驱动版）")
    print("=" * 60)

    # 1. 全网检索情报
    print("\n🌐 步骤 1/6: 全网检索最新情报...")
    research_articles = run_research(use_cache=True, force_refresh=refresh_research)
    print(f"   情报库: {len(research_articles)} 篇真实文章")

    # 2. 知识萃取
    print("\n🧠 步骤 2/6: 知识萃取...")
    kb = build_knowledge_base(research_articles)
    save_knowledge_base(kb)
    print(f"   萃取结果: {kb['meta']['tools']} 个工具 / "
          f"{kb['meta']['findings']} 条研究发现 / "
          f"{kb['meta']['statistics']} 条统计 / "
          f"{kb['meta']['strategies']} 条策略")
    retriever = KnowledgeRetriever(kb)

    # 3. 证据驱动评分
    print("\n📊 步骤 3/6: 证据驱动评分...")
    all_topics = get_all_topics()
    ranked = rank_topics(all_topics, retriever=retriever)
    print(f"   候选选题: {len(ranked)} 个")
    print("   Top 5 选题:")
    for t in ranked[:5]:
        print(f"   #{t['rank']} [{t['weighted_score']}] {t['title']}")

    # 4. 研究驱动进化
    print("\n🧬 步骤 4/6: 研究驱动进化 (用最新情报替换低分选题)...")
    config = EvolutionConfig(
        pool_size=target_count,
        elimination_rate=0.08,
        generations=5,
        elite_ratio=0.15,
    )
    evolution = TopicEvolution(config, retriever=retriever)
    optimized = evolution.evolve(ranked, categories=CATEGORIES)
    print(f"   最终选题池: {len(optimized)} 篇")
    total_replaced = len(evolution.replacement_log)
    print(f"   累计用最新情报替换: {total_replaced} 个低分选题")
    for stats in evolution.history:
        print(f"   第{stats['generation']}代: 平均{stats['avg_score']} / "
              f"最高{stats['max_score']} / 最低{stats['min_score']} / "
              f"替换{stats['replaced']}")

    # 5. 保存数据
    print("\n💾 步骤 5/6: 保存选题与排名数据...")
    os.makedirs(DATA_DIR, exist_ok=True)

    topics_path = os.path.join(DATA_DIR, "topics.json")
    with open(topics_path, "w", encoding="utf-8") as f:
        json.dump(optimized, f, ensure_ascii=False, indent=2)

    rankings_data = {
        "total": len(optimized),
        "evidence_driven": True,
        "research_sources": kb["meta"]["source_articles"],
        "knowledge_meta": kb["meta"],
        "categories": {},
        "evolution_history": evolution.history,
        "replacements": evolution.replacement_log[:50],
        "top_20": [
            {"rank": t["rank"], "title": t["title"], "score": t["weighted_score"],
             "evidence": t["scores"]["evidence_strength"]}
            for t in optimized[:20]
        ],
    }
    for cat in CATEGORIES:
        cat_topics = [t for t in optimized if t["category_id"] == cat.id]
        rankings_data["categories"][cat.id] = {
            "name": cat.name,
            "count": len(cat_topics),
            "avg_score": round(
                sum(t["weighted_score"] for t in cat_topics) / max(len(cat_topics), 1), 2
            ),
        }
    with open(os.path.join(DATA_DIR, "rankings.json"), "w", encoding="utf-8") as f:
        json.dump(rankings_data, f, ensure_ascii=False, indent=2)
    evolution.save_history(os.path.join(DATA_DIR, "evolution_history.json"))

    # 6. 生成事实驱动文章
    print(f"\n✍️  步骤 6/6: 生成 {len(optimized)} 篇事实驱动文章...")
    os.makedirs(ARTICLES_DIR, exist_ok=True)
    os.makedirs(BLOG_CONTENT_DIR, exist_ok=True)

    # 清空旧文章，避免新旧混杂
    for d in (ARTICLES_DIR, BLOG_CONTENT_DIR):
        for fn in os.listdir(d):
            if fn.endswith(".md"):
                os.remove(os.path.join(d, fn))

    for i, topic in enumerate(optimized):
        article = generate_article(topic, i, retriever)
        save_article(article, ARTICLES_DIR)
        save_article(article, BLOG_CONTENT_DIR)
        if (i + 1) % 50 == 0:
            print(f"   已生成 {i + 1}/{len(optimized)} 篇...")

    print(f"   ✅ 全部 {len(optimized)} 篇文章生成完成!")

    print("\n" + "=" * 60)
    print("🎉 研究驱动内容引擎运行完成!")
    print(f"   📁 选题数据: {DATA_DIR}")
    print(f"   📝 文章文件: {ARTICLES_DIR}")
    print(f"   🌐 博客内容: {BLOG_CONTENT_DIR}")
    print("=" * 60)


if __name__ == "__main__":
    import sys
    refresh = "--refresh" in sys.argv
    run_pipeline(refresh_research=refresh)
