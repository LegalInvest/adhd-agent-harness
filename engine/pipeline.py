"""
主流程编排
协调选题生成、评分、进化和文章生成的完整流程
"""

import json
import os
import sys

from engine.categories import CATEGORIES, get_all_topics
from engine.evolution import EvolutionConfig, TopicEvolution
from engine.generator import generate_article, save_article
from engine.scorer import rank_topics


DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")
ARTICLES_DIR = os.path.join(DATA_DIR, "articles")
BLOG_CONTENT_DIR = os.path.join(
    os.path.dirname(os.path.dirname(__file__)), "blog", "src", "content", "articles"
)


def run_pipeline() -> None:
    """执行完整的内容引擎流程"""
    print("=" * 60)
    print("ADHD × AI 内容引擎")
    print("=" * 60)

    # 1. 获取全部选题
    print("\n📋 步骤 1/5: 获取选题库...")
    all_topics = get_all_topics()
    print(f"   共 {len(all_topics)} 个选题，来自 {len(CATEGORIES)} 个分类")
    for cat in CATEGORIES:
        print(f"   - {cat.icon} {cat.name}: {len(cat.topics)} 个选题")

    # 2. 多维度评分
    print("\n📊 步骤 2/5: 多维度评分...")
    ranked = rank_topics(all_topics)
    top5 = ranked[:5]
    print("   Top 5 选题:")
    for t in top5:
        print(f"   #{t['rank']} [{t['weighted_score']}] {t['title']}")

    # 3. 进化优化
    print("\n🧬 步骤 3/5: 进化优化 (5代)...")
    config = EvolutionConfig(
        pool_size=400,
        elimination_rate=0.05,
        mutation_rate=0.03,
        generations=5,
        elite_ratio=0.15,
    )
    evolution = TopicEvolution(config)
    optimized = evolution.evolve(ranked)
    print(f"   最终选题池: {len(optimized)} 篇")
    print(f"   进化报告:")
    for stats in evolution.history:
        print(
            f"   第{stats['generation']}代: "
            f"平均{stats['avg_score']} / "
            f"最高{stats['max_score']} / "
            f"最低{stats['min_score']}"
        )

    # 4. 保存选题数据
    print("\n💾 步骤 4/5: 保存选题数据...")
    os.makedirs(DATA_DIR, exist_ok=True)

    topics_path = os.path.join(DATA_DIR, "topics.json")
    with open(topics_path, "w", encoding="utf-8") as f:
        json.dump(optimized, f, ensure_ascii=False, indent=2)
    print(f"   选题数据已保存到 {topics_path}")

    rankings_path = os.path.join(DATA_DIR, "rankings.json")
    rankings_data = {
        "total": len(optimized),
        "categories": {},
        "evolution_history": evolution.history,
        "top_20": [
            {"rank": t["rank"], "title": t["title"], "score": t["weighted_score"]}
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
    with open(rankings_path, "w", encoding="utf-8") as f:
        json.dump(rankings_data, f, ensure_ascii=False, indent=2)
    print(f"   排名数据已保存到 {rankings_path}")

    evolution.save_history(os.path.join(DATA_DIR, "evolution_history.json"))

    # 5. 生成文章
    print("\n✍️  步骤 5/5: 生成 400 篇文章...")
    os.makedirs(ARTICLES_DIR, exist_ok=True)
    os.makedirs(BLOG_CONTENT_DIR, exist_ok=True)

    for i, topic in enumerate(optimized):
        article = generate_article(topic, i)
        # 保存到 data/articles/
        save_article(article, ARTICLES_DIR)
        # 同时保存到 blog/src/content/articles/
        save_article(article, BLOG_CONTENT_DIR)

        if (i + 1) % 50 == 0:
            print(f"   已生成 {i + 1}/{len(optimized)} 篇...")

    print(f"   ✅ 全部 {len(optimized)} 篇文章生成完成!")

    # 汇总
    print("\n" + "=" * 60)
    print("🎉 内容引擎运行完成!")
    print(f"   📁 选题数据: {DATA_DIR}")
    print(f"   📝 文章文件: {ARTICLES_DIR}")
    print(f"   🌐 博客内容: {BLOG_CONTENT_DIR}")
    print("=" * 60)


if __name__ == "__main__":
    run_pipeline()
