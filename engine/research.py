"""
全网情报检索模块
使用 DuckDuckGo 搜索 + trafilatura 抓取，获取最新 ADHD × AI 情报
每次运行自动搜索最新内容，融入知识库
"""

import json
import os
import time
import hashlib
from dataclasses import dataclass, field, asdict
from datetime import datetime

try:
    from ddgs import DDGS
except ImportError:
    from duckduckgo_search import DDGS

try:
    import trafilatura
except ImportError:
    trafilatura = None


DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")


@dataclass
class SearchResult:
    url: str
    title: str
    snippet: str
    query: str
    content: str = ""
    content_length: int = 0
    scraped_at: str = ""
    content_hash: str = ""


# 多维度搜索查询矩阵：英文 + 中文，覆盖所有核心角度
SEARCH_QUERIES_EN = [
    # AI 工具实战
    "ADHD AI tools 2025 2026 best productivity apps",
    "ADHD AI assistant executive function support",
    "ChatGPT ADHD strategies prompts productivity",
    "AI powered ADHD task management apps review",
    "ADHD AI automation workflow tools",
    # 诊断与科学
    "ADHD AI diagnosis machine learning EEG 2024 2025",
    "ADHD neuroscience artificial intelligence research breakthroughs",
    "ADHD brain imaging AI deep learning study",
    "ADHD biomarkers AI detection screening",
    "ADHD comorbidity AI assessment tool",
    # 专注力与时间
    "ADHD focus AI neurofeedback wearable devices",
    "ADHD time blindness AI timer apps solutions",
    "ADHD procrastination AI intervention strategies",
    "ADHD pomodoro AI adaptive focus timer",
    # 情绪与心理
    "ADHD emotional dysregulation AI therapy tools",
    "ADHD anxiety AI CBT chatbot support",
    "ADHD rejection sensitivity AI coping strategies",
    "ADHD mindfulness AI meditation apps",
    # 学习与教育
    "ADHD students AI learning tools personalized education",
    "ADHD children AI educational technology 2025",
    "ADHD AI tutoring adaptive learning platforms",
    "ADHD study skills AI note-taking apps",
    # 职场与创业
    "ADHD workplace AI accommodations productivity",
    "ADHD entrepreneurs AI business tools advantages",
    "ADHD remote work AI tools strategies",
    "ADHD career coaching AI platforms",
    # 生活方式
    "ADHD AI habit tracking behavior change gamification",
    "ADHD sleep AI monitoring improvement apps",
    "ADHD medication management AI reminders tracking",
    "ADHD AI coaching virtual support community",
]

SEARCH_QUERIES_CN = [
    "ADHD AI工具 2025 效率 最新推荐",
    "多动症 人工智能 诊断 最新研究 2024",
    "ADHD 成人 AI 辅助 生活管理",
    "注意力缺陷 AI 专注力训练 工具",
    "ADHD 创业者 AI 优势 成功案例",
    "ADHD 情绪管理 AI 应用 技术",
    "ADHD 时间管理 AI 工具 方法",
    "ADHD 儿童 教育 AI 辅助 2025",
    "ADHD 脑科学 神经影像 AI 研究",
    "多动症 药物 AI 管理 追踪",
    "ADHD 冥想 正念 AI 引导 应用",
    "ADHD 社区 互助 在线平台 AI",
    "ADHD 职场 效率 AI 工具 远程工作",
    "ADHD ChatGPT 使用技巧 提示词",
    "ADHD 可穿戴设备 神经反馈 AI",
]

# Agent / LLM harness 工程域：为「ADHD 大脑 ↔ LLM 同构」论证提供真实的另一端来源。
# 这些素材描述"如何给一个强但不可靠的生成核心套上脚手架"，与 ADHD 的执行功能脚手架
# 形成结构对照。抓取后会被标记 domain="harness"，与 ADHD 域语料并列入库。
SEARCH_QUERIES_HARNESS = [
    # Agent 脚手架 / 编排
    "LLM agent harness scaffolding architecture orchestration",
    "AI agent framework memory tools planning loop",
    "agentic workflow task decomposition planner executor",
    "LLM agent reliability guardrails verification self-critique",
    # 记忆与上下文（对应工作记忆/外部记忆）
    "LLM agent memory long-term persistent vector store",
    "context engineering LLM context window management",
    "retrieval augmented generation external memory agents",
    "LLM statelessness session memory scratchpad",
    # 幻觉/验证（对应冲动/想当然）
    "LLM hallucination mitigation verification grounding",
    "chain of thought self-consistency critique loop LLM",
    "human in the loop LLM agent oversight",
    # 采样/不稳定（对应表现波动）
    "LLM temperature sampling output variance determinism",
    # 工具使用 / 重锚定
    "LLM function calling tool use offloading reasoning",
    "agent re-grounding system prompt goal drift long horizon",
    # 直接讨论同构 / ADHD 与 AI 认知类比
    "ADHD brain large language model analogy executive function",
    "AI as external executive function cognitive prosthesis",
    "second brain externalized cognition tools knowledge management",
]


def search_web(
    queries: list[str] | None = None,
    max_results_per_query: int = 8,
    delay: float = 1.0,
) -> list[dict]:
    """
    执行全网搜索，返回结构化搜索结果

    Args:
        queries: 搜索查询列表，默认使用内置查询矩阵
        max_results_per_query: 每个查询的最大结果数
        delay: 请求间隔（秒）

    Returns:
        去重后的搜索结果列表
    """
    if queries is None:
        queries = SEARCH_QUERIES_EN + SEARCH_QUERIES_CN + SEARCH_QUERIES_HARNESS

    harness_queries = set(SEARCH_QUERIES_HARNESS)

    ddgs = DDGS()
    all_results = {}
    seen_urls = set()

    for i, query in enumerate(queries):
        domain = "harness" if query in harness_queries else "adhd"
        try:
            results = ddgs.text(query, max_results=max_results_per_query)
            for r in results:
                url = r.get("href", "")
                if url and url not in seen_urls:
                    seen_urls.add(url)
                    all_results[url] = {
                        "url": url,
                        "title": r.get("title", ""),
                        "snippet": r.get("body", ""),
                        "query": query,
                        "domain": domain,
                    }
            print(f"  [{i+1}/{len(queries)}] {query[:50]}... → {len(results)} results")
            if delay > 0:
                time.sleep(delay)
        except Exception as e:
            print(f"  [{i+1}/{len(queries)}] ✗ {query[:50]}... → {e}")

    print(f"\n  Total unique URLs: {len(all_results)}")
    return list(all_results.values())


def scrape_content(
    results: list[dict],
    max_pages: int = 80,
    max_chars_per_page: int = 8000,
    delay: float = 0.5,
) -> list[dict]:
    """
    深度抓取搜索结果页面内容

    Args:
        results: search_web() 返回的搜索结果
        max_pages: 最大抓取页面数
        max_chars_per_page: 每页最大保留字符数
        delay: 请求间隔（秒）

    Returns:
        附带完整内容的结果列表
    """
    if trafilatura is None:
        print("  ⚠ trafilatura not installed, skipping content scraping")
        return results

    scraped = []
    failed = 0
    now = datetime.now().isoformat()

    for i, item in enumerate(results[:max_pages]):
        url = item["url"]
        try:
            downloaded = trafilatura.fetch_url(url)
            if downloaded:
                text = trafilatura.extract(
                    downloaded,
                    include_comments=False,
                    include_tables=True,
                )
                if text and len(text) > 200:
                    content = text[:max_chars_per_page]
                    content_hash = hashlib.md5(content.encode()).hexdigest()
                    scraped.append({
                        **item,
                        "content": content,
                        "content_length": len(text),
                        "scraped_at": now,
                        "content_hash": content_hash,
                    })
                    print(f"  ✓ [{i+1}/{max_pages}] {item['title'][:55]}... ({len(text):,} chars)")
                else:
                    failed += 1
            else:
                failed += 1
            if delay > 0:
                time.sleep(delay)
        except Exception as e:
            failed += 1

    print(f"\n  Scraped: {len(scraped)}, Failed: {failed}")
    return scraped


def save_research(data: list[dict], filename: str = "scraped_knowledge.json") -> str:
    """保存研究数据到 JSON 文件"""
    os.makedirs(DATA_DIR, exist_ok=True)
    filepath = os.path.join(DATA_DIR, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    return filepath


def load_research(filename: str = "scraped_knowledge.json") -> list[dict]:
    """加载已有的研究数据。历史数据无 domain 字段时默认归为 adhd 域。"""
    filepath = os.path.join(DATA_DIR, filename)
    if os.path.exists(filepath):
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)
        for item in data:
            item.setdefault("domain", "adhd")
        return data
    return []


def _interleave_by_domain(results: list[dict]) -> list[dict]:
    """按 domain 交错排序，保证后续截断抓取时两域都被覆盖到。"""
    adhd = [r for r in results if r.get("domain") != "harness"]
    harness = [r for r in results if r.get("domain") == "harness"]
    out: list[dict] = []
    for a, h in zip(adhd, harness):
        out.append(a)
        out.append(h)
    out.extend(adhd[len(harness):])
    out.extend(harness[len(adhd):])
    return out


def merge_research(existing: list[dict], new: list[dict]) -> list[dict]:
    """
    合并新旧研究数据，去重，保留最新版本

    基于 URL 去重，新数据优先
    """
    by_url = {}
    for item in existing:
        by_url[item["url"]] = item
    for item in new:
        by_url[item["url"]] = item  # 新数据覆盖旧数据
    return list(by_url.values())


def run_research(
    use_cache: bool = True,
    force_refresh: bool = False,
    queries: list[str] | None = None,
    max_pages: int = 150,
) -> list[dict]:
    """
    执行完整的研究流程

    Args:
        use_cache: 是否使用已有缓存数据
        force_refresh: 是否强制重新搜索和抓取
        queries: 自定义查询；None 时使用 ADHD + harness 全量矩阵
        max_pages: 单次抓取的最大页面数（两域交错后截断）

    Returns:
        完整的研究数据列表
    """
    existing = []
    if use_cache and not force_refresh:
        existing = load_research()
        if existing:
            n_h = sum(1 for x in existing if x.get("domain") == "harness")
            print(f"  📚 已有缓存: {len(existing)} 篇（adhd {len(existing)-n_h} / harness {n_h}）")

    if force_refresh or not existing:
        print("\n🔍 Phase 1: 全网搜索...")
        search_results = search_web(queries=queries)
        search_results = _interleave_by_domain(search_results)

        print("\n📄 Phase 2: 深度抓取...")
        scraped = scrape_content(search_results, max_pages=max_pages)

        if existing:
            merged = merge_research(existing, scraped)
            print(f"\n  合并后: {len(merged)} 篇（原 {len(existing)} + 新 {len(scraped)} - 重复）")
        else:
            merged = scraped

        save_research(merged)
        n_h = sum(1 for x in merged if x.get("domain") == "harness")
        print(f"  域分布: adhd {len(merged)-n_h} / harness {n_h}")
        return merged

    return existing


def run_harness_research(max_pages: int = 80) -> list[dict]:
    """只补抓 harness 域素材并并入现有语料（不重抓 ADHD 域，省时省请求）。"""
    existing = load_research()
    print(f"  📚 现有语料: {len(existing)} 篇，开始补抓 harness 域...")
    print("\n🔍 搜索 harness 域...")
    results = search_web(queries=SEARCH_QUERIES_HARNESS)
    print("\n📄 抓取 harness 域...")
    scraped = scrape_content(results, max_pages=max_pages)
    merged = merge_research(existing, scraped)
    save_research(merged)
    n_h = sum(1 for x in merged if x.get("domain") == "harness")
    print(f"\n  合并后: {len(merged)} 篇（新增 harness 抓取 {len(scraped)}；harness 域共 {n_h}）")
    return merged
