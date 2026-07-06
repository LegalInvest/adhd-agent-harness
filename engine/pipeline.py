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
from engine.problems import generate_problem_pool
from engine import academic
from engine import isomorphism
from engine import harness_figures
from engine.case_studies import CaseStudyRetriever
from engine import intelligence_assets
from engine import lbd as lbd_mod
from engine import burst as burst_mod
from engine import storm as storm_mod
from engine import graphrag
from engine.knowledge import (
    build_knowledge_base,
    save_knowledge_base,
    load_knowledge_base,
    KnowledgeRetriever,
)
from engine.evolution import EvolutionConfig, TopicEvolution
from engine.generator import generate_article, generate_article_llm, save_article
from engine.scorer import rank_topics
from engine.wiki import build_wiki, WikiRetriever
from engine.llm import is_llm_available, get_client


DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")
ARTICLES_DIR = os.path.join(DATA_DIR, "articles")
BLOG_CONTENT_DIR = os.path.join(
    os.path.dirname(os.path.dirname(__file__)), "blog", "src", "content", "articles"
)


def run_pipeline(
    refresh_research: bool = False,
    target_count: int = 400,
    use_llm: bool = True,
    limit: int | None = None,
    academic_kb_per_domain: int = 1200,
    academic_wiki_per_domain: int = 4000,
) -> None:
    """执行完整的研究驱动 + LLM Wiki 内容引擎流程"""
    print("=" * 60)
    print("ADHD × AI 内容引擎（研究驱动 + LLM Wiki 版）")
    print("=" * 60)

    llm = None
    if use_llm and is_llm_available():
        llm = get_client()
        print(f"   LLM: 已启用（{llm.active_model}）")
    elif use_llm:
        print("   LLM: 未配置凭证，降级为确定性模板生成")

    # 1. 全网检索情报（网页深抓 + 大规模学术语料）
    print("\n🌐 步骤 1/7: 全网检索最新情报...")
    research_articles = run_research(use_cache=True, force_refresh=refresh_research)
    print(f"   网页情报库: {len(research_articles)} 篇真实深抓文章")

    academic_all = academic.load_academic()
    academic_stats = academic.stats(academic_all)
    print(f"   学术语料库: {academic_stats['total']} 篇论文摘要 "
          f"(ADHD {academic_stats['by_domain'].get('adhd', 0)} / "
          f"harness {academic_stats['by_domain'].get('harness', 0)})")
    # 给知识萃取（评分燃料）用有上限的高影响力子集，控制检索性能
    academic_kb_articles = (
        academic.as_articles(academic_all, domain="adhd", limit=academic_kb_per_domain)
        + academic.as_articles(academic_all, domain="harness", limit=academic_kb_per_domain)
    )
    # 给 wiki 取材用更大的子集，提升萃取深度
    academic_wiki_articles = (
        academic.as_articles(academic_all, domain="adhd", limit=academic_wiki_per_domain)
        + academic.as_articles(academic_all, domain="harness", limit=academic_wiki_per_domain)
    )
    # 同构脊柱证据（直接论证 ADHD↔LLM 同构的真实论文）——最高优先级，置于语料最前
    iso_articles = isomorphism.as_articles()
    print(f"   同构脊柱证据: {len(iso_articles)} 篇直接论证 ADHD↔LLM 同构的真实论文")
    # 名人 harness 案例（人类侧「外挂执行功能层」的活教材）——次高优先级
    figure_articles = harness_figures.as_articles()
    print(f"   名人 harness 案例: {len(figure_articles)} 位 ADHD 特质人物的自我管理系统")
    case_retriever = CaseStudyRetriever()
    print(f"   人物案例钩子: 名人 {len(case_retriever.figures)} / 创业者·投资人 {len(case_retriever.entrepreneurs)} / 相关性统计 {len(case_retriever.correlation_stats)}")
    intel_articles = intelligence_assets.as_articles()
    print(f"   情报资产: {len(intel_articles)} 篇一手研究资产（创作者情报库/深度研究/策略报告）")
    # 文献计量层：LBD 同构对 / 突发检测 / 概念图谱 / STORM 视角轮（均带磁盘缓存）
    lbd_pairs = lbd_mod.load_pairs()
    if not lbd_pairs:
        lbd_pairs = lbd_mod.mine_pairs()
        lbd_mod.save_pairs(lbd_pairs)
    lbd_articles = lbd_mod.as_articles(lbd_pairs)
    bursts = burst_mod.load()
    if not bursts:
        bursts = burst_mod.detect()
        burst_mod.save(bursts)
    if not os.path.exists(graphrag.OUT_PATH):
        graphrag.save(graphrag.build_graph())
    if llm is not None:
        from engine.problems import SPINE_PROBLEM_SPECS
        storm_mod.generate(llm, SPINE_PROBLEM_SPECS)
    print(f"   文献计量层: LBD 同构对 {len(lbd_pairs)} 组 / 突发概念 {sum(1 for b in bursts if b.get('is_bursting'))} 个 / STORM 问题 {sum(len(v) for v in storm_mod.load().values())} 条")
    kb_corpus = iso_articles + lbd_articles + figure_articles + intel_articles + research_articles + academic_kb_articles
    wiki_corpus = iso_articles + lbd_articles + figure_articles + intel_articles + research_articles + academic_wiki_articles

    # 2. 知识萃取（双域：网页深抓 + 学术摘要）
    print("\n🧠 步骤 2/7: 知识萃取（双域语料）...")
    kb = build_knowledge_base(kb_corpus)
    save_knowledge_base(kb)
    print(f"   萃取结果: {kb['meta']['tools']} 个工具 / "
          f"{kb['meta']['findings']} 条研究发现 / "
          f"{kb['meta']['statistics']} 条统计 / "
          f"{kb['meta']['strategies']} 条策略")
    retriever = KnowledgeRetriever(kb)

    # 2.5 LLM Wiki：增量构建/维护持久互链知识 wiki
    wiki_retriever = None
    if llm is not None:
        print("\n📚 步骤 3/7: LLM Wiki 增量构建（持久互链 + 矛盾标记）...")
        wiki_store = build_wiki(wiki_corpus, llm, verbose=True)
        wiki_retriever = WikiRetriever(wiki_store)
        wm = wiki_store.index["meta"]
        print(f"   wiki: {wm.get('concept_pages',0)} 概念页 / "
              f"{wm.get('tool_pages',0)} 工具页 / {wm.get('topic_pages',0)} 主题页")
    else:
        print("\n📚 步骤 3/7: 跳过 LLM Wiki（未启用 LLM）")

    # 3. 证据驱动评分（问题驱动 + 双受众张力）
    print("\n📊 步骤 4/7: 证据驱动评分（问题驱动选题池）...")
    problem_pool = generate_problem_pool()
    print(f"   问题驱动候选池: {len(problem_pool)} 条（双受众 + 同构脊柱标注）")
    ranked = rank_topics(problem_pool, retriever=retriever)
    # 取分数最高的 target_count 作为进化起始池，其余作为挑战者参与滚动替换
    seed = ranked[:target_count]
    print(f"   起始 Top {len(seed)} 选题:")
    for t in ranked[:5]:
        print(f"   #{t['rank']} [{t['weighted_score']}] {t['title']}")

    # 4. 研究驱动进化
    print("\n🧬 步骤 5/7: 研究驱动进化 (用最新情报替换低分选题)...")
    config = EvolutionConfig(
        pool_size=target_count,
        elimination_rate=0.08,
        generations=5,
        elite_ratio=0.15,
    )
    evolution = TopicEvolution(config, retriever=retriever)
    optimized = evolution.evolve(seed, categories=CATEGORIES)
    print(f"   最终选题池: {len(optimized)} 篇")
    total_replaced = len(evolution.replacement_log)
    print(f"   累计用最新情报替换: {total_replaced} 个低分选题")
    for stats in evolution.history:
        print(f"   第{stats['generation']}代: 平均{stats['avg_score']} / "
              f"最高{stats['max_score']} / 最低{stats['min_score']} / "
              f"替换{stats['replaced']}")

    # 5. 保存数据
    print("\n💾 步骤 6/7: 保存选题与排名数据...")
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

    # 6. 生成文章（优先 LLM 从 wiki 取材，失败回退确定性模板）
    targets = optimized if limit is None else optimized[:limit]
    mode = "LLM Wiki 取材" if (llm and wiki_retriever and wiki_retriever.available) else "确定性模板"
    print(f"\n✍️  步骤 7/7: 生成 {len(targets)} 篇文章（{mode}）...")
    os.makedirs(ARTICLES_DIR, exist_ok=True)
    os.makedirs(BLOG_CONTENT_DIR, exist_ok=True)

    # 清空旧文章，避免新旧混杂
    for d in (ARTICLES_DIR, BLOG_CONTENT_DIR):
        for fn in os.listdir(d):
            if fn.endswith(".md"):
                os.remove(os.path.join(d, fn))

    use_llm = bool(llm and wiki_retriever and wiki_retriever.available)
    workers = max(1, int(os.environ.get("GEN_WORKERS", "6"))) if use_llm else 1

    def _gen_llm(i_topic):
        """仅做 LLM 生成（I/O 密集，可并发）；失败返回 None 交主线程回退。"""
        i, topic = i_topic
        try:
            return i, generate_article_llm(topic, i, wiki_retriever, llm, case_retriever)
        except Exception as e:  # noqa: BLE001 - 单篇失败不应中断整批
            return i, e

    llm_ok, fallback = 0, 0

    def _finalize(i: int, res) -> None:
        """拿到单篇结果后立即落盘（崩溃不丢成果）。"""
        nonlocal llm_ok, fallback
        topic = targets[i]
        if isinstance(res, dict):
            article = res
            llm_ok += 1
        else:
            if use_llm:
                print(f"   ⚠️ 第{i+1}篇 LLM 生成失败，回退模板: {res}")
            article = generate_article(topic, i, retriever)
            fallback += 1
        save_article(article, ARTICLES_DIR)
        save_article(article, BLOG_CONTENT_DIR)

    if workers > 1:
        import concurrent.futures
        with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as ex:
            for done, (i, res) in enumerate(
                ex.map(_gen_llm, list(enumerate(targets))), 1
            ):
                _finalize(i, res)
                if done % 25 == 0:
                    print(f"   已生成 {done}/{len(targets)} 篇（LLM {llm_ok} / 回退 {fallback}）...")
    else:
        for i, topic in enumerate(targets):
            res = _gen_llm((i, topic))[1] if use_llm else None
            _finalize(i, res)
            if (i + 1) % 25 == 0:
                print(f"   已生成 {i + 1}/{len(targets)} 篇（LLM {llm_ok} / 回退 {fallback}）...")

    print(f"   ✅ 全部 {len(targets)} 篇文章生成完成! (LLM {llm_ok} / 回退 {fallback}, 并发 {workers})")

    print("\n" + "=" * 60)
    print("🎉 研究驱动内容引擎运行完成!")
    print(f"   📁 选题数据: {DATA_DIR}")
    print(f"   📝 文章文件: {ARTICLES_DIR}")
    print(f"   🌐 博客内容: {BLOG_CONTENT_DIR}")
    print("=" * 60)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="ADHD × AI 研究驱动 + LLM Wiki 内容引擎")
    parser.add_argument("--refresh", action="store_true", help="强制全网重新检索情报")
    parser.add_argument("--no-llm", action="store_true", help="关闭 LLM，使用确定性模板")
    parser.add_argument("--limit", type=int, default=None, help="只生成前 N 篇（用于测试）")
    args = parser.parse_args()

    run_pipeline(
        refresh_research=args.refresh,
        use_llm=not args.no_llm,
        limit=args.limit,
    )
