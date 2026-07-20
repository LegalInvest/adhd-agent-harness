"""
文章内容生成器（研究驱动版）
不再用空洞模板填充，而是把知识库中的真实工具、研究发现、
统计数据和实用策略编织进每一篇文章，并附上真实来源引用。
每篇文章都是事实驱动、可溯源、彼此不同的。
"""

import hashlib
import os
import re
from datetime import datetime, timedelta

from engine.knowledge import KnowledgeRetriever, CORE_CONCEPTS
from engine.grade import label as grade_label
from engine.iso_strength import grade_iso_strength


def _seed_from(text: str) -> int:
    return int(hashlib.md5(text.encode("utf-8")).hexdigest()[:8], 16)


def _pick(items: list, text: str, offset: int = 0):
    if not items:
        return None
    return items[(_seed_from(text) + offset) % len(items)]


def _slugify(title: str) -> str:
    slug = title.lower()
    slug = re.sub(r"[^\w\u4e00-\u9fff\s-]", "", slug)
    slug = re.sub(r"[\s_]+", "-", slug)
    slug = slug.strip("-")
    if len(slug) > 80:
        slug = slug[:80].rsplit("-", 1)[0]
    return slug


# 分类对应的核心痛点（用于真实的开场）
PAIN_POINTS = {
    "ai-tools": "在一堆效率工具之间反复横跳，却没有一个能真正坚持用下去",
    "focus": "注意力像没装锚的船，明明想专注却总是漂走",
    "time-mgmt": "时间像握不住的沙，常常低估任务耗时、错过截止日期",
    "emotion": "情绪来得又快又猛，一句批评能让一整天崩盘",
    "learning": "学习热情来得快去得也快，买的课总是看不完",
    "career": "在职场上明明有能力，却被组织、跟进这些事拖了后腿",
    "entrepreneurship": "点子多到爆炸，但把想法落地执行却异常艰难",
    "parenting": "想帮 ADHD 孩子，却不知道哪些方法真的有用",
    "science": "网上关于 ADHD 的说法五花八门，到底哪些有科学依据",
    "lifestyle": "日常生活总在混乱边缘，习惯怎么都建立不起来",
    "community": "觉得没人真正理解 ADHD 的处境，常常感到孤立",
}

# ADHD 大脑特质（真实，来自研究共识）
ADHD_TRAITS = [
    "在感兴趣的领域可以进入「超聚焦」（hyperfocus）状态",
    "发散思维和联想能力强，擅长看到别人忽略的连接",
    "对新鲜刺激敏感，学习新事物上手快",
    "在高压和紧迫感下反而能爆发出惊人的执行力",
    "共情能力和直觉往往优于常人",
]

# 执行功能短板（真实）
EXEC_WEAKNESSES = [
    "工作记忆（working memory）容量有限，容易边做边忘",
    "任务启动（task initiation）困难，明知该做却开不了头",
    "时间感知偏差（time blindness），难以估算时长",
    "情绪调节（emotional regulation）需要更多外部支持",
    "组织和优先级排序需要额外的结构支撑",
]


def _format_finding(f: dict) -> str:
    """把研究发现格式化为带来源的引用句"""
    text = f["text"].strip().rstrip(".。")
    src = f.get("source_title", "").strip()
    return f"{text}。" if not src else f"{text}（来源：{src}）。"


def _build_keywords(topic: dict) -> list[str]:
    kws = list(topic.get("keywords", []))
    cat_kw = {
        "ai-tools": ["tool", "app", "AI", "productivity", "ChatGPT"],
        "focus": ["focus", "attention", "concentration", "hyperfocus"],
        "time-mgmt": ["time", "schedule", "task", "planning", "procrastination"],
        "emotion": ["emotion", "anxiety", "regulation", "mood", "CBT"],
        "learning": ["learning", "study", "education", "memory"],
        "career": ["work", "career", "workplace", "job", "executive function"],
        "entrepreneurship": ["business", "entrepreneur", "startup"],
        "parenting": ["children", "kids", "parent", "education"],
        "science": ["research", "diagnosis", "brain", "EEG", "MRI", "machine learning"],
        "lifestyle": ["habit", "sleep", "daily", "routine"],
        "community": ["community", "support", "social"],
    }
    kws.extend(cat_kw.get(topic.get("category_id", ""), []))
    kws.append("ADHD")
    return kws


def generate_article(topic: dict, index: int, retriever: KnowledgeRetriever) -> dict:
    """
    根据选题 + 知识库生成一篇事实驱动的文章
    """
    title = topic["title"]
    subtitle = topic.get("subtitle", "")
    category_id = topic.get("category_id", "")
    category_name = topic.get("category_name", "")
    category_name_en = topic.get("category_name_en", "")
    angle = topic.get("angle", "")
    keywords = topic.get("keywords", [])
    topic_id = topic.get("id", f"article-{index:03d}")

    seed = _seed_from(title)
    slug = _slugify(title)

    base_date = datetime(2025, 6, 1)
    pub_date = base_date - timedelta(days=seed % 90)
    date_str = pub_date.strftime("%Y-%m-%d")

    query_kws = _build_keywords(topic)

    # 从知识库检索真实素材（用 index 做 offset 保证不同文章取到不同素材）
    tools = retriever.tools_for_category(category_id, limit=4)
    findings = retriever.findings_for(query_kws, limit=3, offset=index)
    stats = retriever.statistics_for(query_kws, limit=2, offset=index)
    strategies = retriever.strategies_for(query_kws, limit=5, offset=index * 2)

    reading_time = 7 + (seed % 8)

    tags = list(dict.fromkeys([
        "ADHD", "AI", category_name, angle,
        (keywords[seed % len(keywords)] if keywords else "效率"),
    ]))[:6]

    pain = PAIN_POINTS.get(category_id, "面对各种日常挑战")
    trait = _pick(ADHD_TRAITS, title, 0)
    weakness = _pick(EXEC_WEAKNESSES, title, 1)

    # ===== 构建正文 =====
    parts = []

    # 引言：用真实统计数据开场（如果有）
    if stats:
        stat_text = stats[0]["text"].strip().rstrip(".。")
        intro = (
            f"> {subtitle}\n\n"
            f"先说一个事实：{stat_text}。\n\n"
            f"如果你是 ADHD 人群，你大概率经历过——{pain}。这不是你不够努力，"
            f"而是 ADHD 大脑的运作方式本就不同。而 AI 的出现，第一次让我们有机会"
            f"用「外接」的方式补上这块短板。这篇文章不讲空话，只讲有据可查的工具、研究和可落地的方法。"
        )
    else:
        intro = (
            f"> {subtitle}\n\n"
            f"如果你是 ADHD 人群，你大概率经历过——{pain}。这不是你不够努力，"
            f"而是 ADHD 大脑的运作方式本就不同。好消息是，AI 正在成为 ADHD 最称职的「外接大脑」。"
            f"这篇文章基于最新的研究和真实工具，带你看清{angle}到底怎么落地。"
        )
    parts.append(intro)

    # 第一节：为什么 ADHD 需要这个 —— 结合真实大脑机制
    parts.append(
        f"## 为什么这件事对 ADHD 格外重要\n\n"
        f"ADHD 并不是「注意力不足」这么简单，它的核心是执行功能（executive function）的差异。"
        f"具体来说，ADHD 大脑往往{weakness}。但与此同时，ADHD 也有自己的天赋：{trait}。\n\n"
        f"关键不在于「治好」ADHD，而在于用合适的外部系统补上短板、放大长处。"
        f"AI 恰好擅长承接那些 ADHD 最吃力的部分——记住、组织、提醒、拆解、追踪。"
    )

    # 第二节：最新研究怎么说 —— 注入真实 findings
    if findings:
        research_lines = "\n".join(f"- {_format_finding(f)}" for f in findings)
        parts.append(
            f"## 最新研究怎么说\n\n"
            f"在动手之前，先看看证据。近年来 AI×ADHD 领域的研究进展很快：\n\n"
            f"{research_lines}\n\n"
            f"这些研究的共同信号是：AI 在 ADHD 的评估、辅助和日常管理上正在从「概念」走向「可用」，"
            f"但也要警惕被夸大的宣传——真正可靠的方案，往往是把 AI 当工具而非神药。"
        )

    # 第三节：真实可用的工具 —— 注入真实 tools
    if tools:
        tool_lines = "\n".join(
            f"### {t['keywords'][0]}\n\n{t['text']}"
            for t in tools
        )
        parts.append(
            f"## 真实可用的 AI 工具\n\n"
            f"下面这些工具都是 ADHD 社区和评测中被反复推荐的，按它们最擅长的场景挑一两个上手即可，"
            f"千万别一次性全装——那只会变成新的分心来源。\n\n"
            f"{tool_lines}"
        )

    # 第四节：可落地的策略 —— 注入真实 strategies
    if strategies:
        strat_lines = "\n".join(
            f"{i+1}. {s['text'].strip()}"
            for i, s in enumerate(strategies)
        )
        parts.append(
            f"## 可以今天就试的策略\n\n"
            f"工具只是载体，方法才是关键。结合社区实践，这里有几条可操作的策略：\n\n"
            f"{strat_lines}\n\n"
            f"建议只挑其中**一条**今天就开始，ADHD 大脑最怕「全部一起改」。"
        )

    # 第五节：批判性提醒 —— 体现"形成新观点"
    concept_key = _pick(list(CORE_CONCEPTS.keys()), title, 3)
    concept_desc = CORE_CONCEPTS.get(concept_key, "")
    parts.append(
        f"## 一个容易被忽略的提醒\n\n"
        f"AI 很强，但它不是替你做决定的人。对 ADHD 来说，最大的风险是「工具囤积」——"
        f"不停地试新工具，却从没真正用起来任何一个。这本身就是一种拖延。\n\n"
        f"另外要理解一个概念：{concept_key}（{concept_desc}）。"
        f"真正可持续的改变，是让 AI 嵌入你已有的习惯回路，而不是再造一套全新的系统。"
        f"从最小、最痛的那个点开始，让 AI 帮你赢得第一个小胜利，多巴胺会带着你继续走下去。"
    )

    # 结语
    parts.append(
        f"## 写在最后\n\n"
        f"ADHD 不是你的缺陷，而是一套不同的操作系统。AI 也不是万能解药，"
        f"它是一个强大的外接模块——当你学会正确地接上它，那些曾经让你精疲力竭的事，会变得轻一点。\n\n"
        f"记住：**开始不需要完美，只需要开始。** 选择这篇文章里最打动你的那一个方法，今天就试试看。"
    )

    # 参考来源（真实 URL）
    refs = []
    seen_urls = set()
    for item in findings + stats:
        url = item.get("source_url", "")
        title_src = item.get("source_title", "")
        if url and url not in seen_urls:
            seen_urls.add(url)
            refs.append(f"- [{title_src}]({url}) — {grade_label(title_src, url)}")
    if refs:
        parts.append("## 参考来源\n\n" + "\n".join(refs[:6]))

    full_content = f"# {title}\n\n" + "\n\n".join(parts) + (
        f"\n\n---\n\n*本文是「ADHD × AI」系列的第 {index + 1} 篇，"
        f"内容基于全网最新情报与研究自动整合生成，并持续迭代更新。*\n"
    )

    frontmatter = {
        "title": title,
        "subtitle": subtitle,
        "description": subtitle,
        "date": date_str,
        "category": category_name,
        "categoryId": category_id,
        "categoryEn": category_name_en,
        "tags": tags,
        "readingTime": reading_time,
        "slug": slug,
        "topicId": topic_id,
        "angle": angle,
        "rank": topic.get("rank", index + 1),
        "score": topic.get("weighted_score", 0),
        "sourceCount": len(refs),
        "toolsCited": [t["keywords"][0] for t in tools],
        "problem": topic.get("problem", title),
        "spine": topic.get("spine", ""),
        "spineKind": topic.get("spine_kind", ""),
        "isEvolved": topic.get("is_evolved", False),
    }

    return {
        "frontmatter": frontmatter,
        "content": full_content,
        "slug": slug,
        "filename": f"{topic_id}.md",
    }


ARTICLE_SYS = (
    "你是一名资深的「ADHD × AI」中文内容作者，写作循证、克制、有观点。"
    "你只能依据给定的 wiki 资料写作，不得编造资料中不存在的工具、数据或来源。"
    "你的文章要在整合事实的同时**形成自己的判断与新观点**，并诚实指出争议与局限。"
    "项目北极星：深入研究 ADHD、找到「人生 Harness 系统」的方法论，助力 ADHD 者获得幸福、成长与人生价值——"
    "文章的成功标准不是『读完觉得有道理』，而是读者能把一个具体组件（协议/仪式/参数/清单）装进自己的人生系统。"
    "遵守内容方法论（docs/METHODOLOGY.md）：机制证据≠产品证据；类比停在计算层；"
    "医疗相关话题（药物/共病/睡眠/严重情绪）必须提示寻求专业评估；不诊断读者、不承诺治愈。"
)


def _wiki_context_block(ctx: dict) -> str:
    """把 wiki 上下文压缩成提示词"""
    blocks = []
    if ctx.get("topic"):
        t = ctx["topic"]
        blocks.append(f"【主题综述：{t['name']}】\n{t['body'][:1400]}")
    for c in ctx.get("concepts", []):
        blocks.append(f"【概念页：{c['name']}】\n{c['body'][:1100]}")
    for t in ctx.get("tools", []):
        blocks.append(f"【工具页：{t['name']}】\n{t['body'][:1100]}")
    if ctx.get("contradictions"):
        blocks.append(f"【全局矛盾与存疑】\n{ctx['contradictions'][:1000]}")
    return "\n\n".join(blocks)


def _collect_wiki_sources(ctx: dict) -> list[dict]:
    sources, seen = [], set()
    pages = list(ctx.get("tools", [])) + list(ctx.get("concepts", []))
    if ctx.get("topic"):
        pages.append(ctx["topic"])
    for p in pages:
        for s in p.get("sources", []):
            url = s.get("url", "")
            if url and url not in seen:
                seen.add(url)
                sources.append({"title": s.get("title", ""), "url": url})
    return sources


def _case_block(topic: dict, index: int, case_retriever, cases=None) -> str:
    if cases is None:
        if case_retriever is None or not case_retriever.available:
            return ""
        cases = case_retriever.cases_for_topic(topic, offset=index)
    if not cases:
        return ""
    lines = "\n".join(f"- [{c['kind']}] {c['text']}" for c in cases)
    stat = case_retriever.stat_for_topic(topic)
    stat_line = f"\n\u76f8\u5173\u6027\u7edf\u8ba1\uff08\u771f\u5b9e\u6765\u6e90\uff09\uff1a{stat}" if stat else ""
    return (
        "\n=== \u4eba\u7269\u6848\u4f8b\uff08\u771f\u5b9e\u4eba\u7269\u7684 harness \u81ea\u6211\u7ba1\u7406\u7cfb\u7edf\uff0c\u53ef\u4f5c\u4e3a\u672c\u6587\u6848\u4f8b\u7d20\u6750\uff09===\n"
        f"{lines}{stat_line}\n"
        "\u4f7f\u7528\u8981\u6c42\uff1a\u4ece\u4e2d\u9009 1-2 \u4f4d\u4e0e\u672c\u6587\u95ee\u9898\u6700\u5951\u5408\u7684\u4eba\u7269\uff0c\u5728\u6b63\u6587\u91cc\u7528\u4e00\u5c0f\u6bb5\u8bb2\u6e05\u4ed6/\u5979\u7684 ADHD \u7279\u8d28\u4e0e harness \u7cfb\u7edf\uff0c"
        "\u5e76\u70b9\u660e\u5b83\u4e0e LLM/agent harness \u7684\u540c\u6784\u5bf9\u5e94\uff08\u5982\u300c\u65e5\u8bfe\u2194\u5b9a\u65f6 re-grounding\u300d\u300c\u79d8\u4e66\u2194\u5916\u90e8\u8c03\u5ea6\u5668\u300d\uff09\u3002"
        "\u4e0d\u8981\u7f57\u5217\u5168\u90e8\u6848\u4f8b\uff0c\u4e0d\u5f97\u7f16\u9020\u6848\u4f8b\u4e2d\u6ca1\u6709\u7684\u7ec6\u8282\u3002\n=== \u6848\u4f8b\u7ed3\u675f ===\n"
    )


def generate_article_llm(topic: dict, index: int, wiki_retriever, llm, case_retriever=None) -> dict:
    """
    研究驱动 + LLM Wiki 版文章生成：
    从 LLM 维护的互链 wiki 中取材，由大模型整合成有观点、可溯源的文章。
    """
    title = topic["title"]
    subtitle = topic.get("subtitle", "")
    category_id = topic.get("category_id", "")
    category_name = topic.get("category_name", "")
    category_name_en = topic.get("category_name_en", "")
    angle = topic.get("angle", "")
    keywords = topic.get("keywords", [])
    topic_id = topic.get("id", f"article-{index:03d}")
    problem = topic.get("problem", title)
    spine = topic.get("spine", "")
    spine_kind = topic.get("spine_kind", "")
    spine_mirror = topic.get("spine_mirror", "")
    adhd_pain = topic.get("adhd_pain", "")
    harness_parallel = topic.get("harness_parallel", "")

    seed = _seed_from(title)
    slug = _slugify(title)
    pub_date = (datetime(2025, 6, 1) - timedelta(days=seed % 90)).strftime("%Y-%m-%d")

    ctx = wiki_retriever.context_for_topic(topic, offset=index)
    context_block = _wiki_context_block(ctx)
    wiki_sources = _collect_wiki_sources(ctx)
    cases = (
        case_retriever.cases_for_topic(topic, offset=index)
        if (case_retriever is not None and case_retriever.available) else []
    )
    case_block = _case_block(topic, index, case_retriever, cases)

    spine_block = ""
    if spine:
        spine_block = (
            f"\n=== 同构脊柱（本文的思想主线，必须贯穿全文）===\n"
            f"核心概念：{spine}\n"
            + (f"ADHD 侧痛点：{adhd_pain}\n" if adhd_pain else "")
            + (f"LLM/Agent 侧对应：{harness_parallel or spine_mirror}\n" if (harness_parallel or spine_mirror) else "")
            + "论证要求：ADHD 大脑与 LLM/agent 是同一类「高产但缺执行调度层的生成核心」，"
              "两边的解法（harness/脚手架）结构同构。必须**同时给出 ADHD 侧与 LLM/agent 侧的真实证据**，"
              "不要做空洞类比；并点明『脚手架 vs 拐杖』的边界。\n=== 脊柱结束 ===\n"
        )

    user = (
        f"请基于以下 wiki 资料，写一篇**问题驱动**、面向中文读者的文章。\n"
        f"它要同时打动两类人：被 {adhd_pain or 'ADHD 困扰'} 折磨的 ADHD 人群，"
        f"以及在做 Agentic Harness 工程（{harness_parallel or 'agent/LLM 编排'}）的工程师。\n\n"
        f"要回答的核心问题：{problem}\n"
        f"标题：{title}\n副标题：{subtitle}\n分类：{category_name}\n切入角度：{angle}\n"
        f"{spine_block}{case_block}\n"
        f"=== wiki 资料（你唯一可用的事实来源）===\n{context_block}\n=== 资料结束 ===\n\n"
        "写作要求：\n"
        "- 1800-2500 字，markdown，用 ## 小节组织；**开头必须是一个具体的冲突/失败现场**（具体的人在具体场景里的具体失败），再用同构脊柱给出答案；\n"
        "- 必须整合 wiki 资料里的真实工具、概念与研究，关键论断后用「（来源：标题）」标注；\n"
        + ("- 必须织入「人物案例」中 1-2 位真实人物的 harness 系统作为论据，并点明其与 LLM harness 的同构对应；\n" if case_block else "")
        + "- 必须**同时**给出 ADHD 侧与 LLM/agent 侧的真实证据，让两类读者都觉得「这说的就是我」；\n"
        "- 必须提出一个**鲜明的核心观点/判断**（不要只罗列工具），并结合『矛盾与存疑』诚实指出局限；\n"
        "- 用一节「## 今天就能试的 3 件事」给出 3 条当天可做的低摩擦行动；\n"
        "- 涉及具体产品时：写明产品未被证实为 ADHD 治疗手段，并把建议打包成可自测的 N-of-1 协议（指标+对照+两三周轮换）；\n"
        "- 结尾点明本文服务于人生 Harness 金字塔的哪一层（状态/执行/关系/叙事/价值），并回答『这让读者的生活好在哪』；\n"
        "- 涉及药物、共病、睡眠、严重情绪症状时，必须包含「请寻求专业评估/支持」的明确提示；\n"
        "- 不要写 H1 大标题（标题会另行添加），从引言直接开始；\n"
        "- 不得编造 wiki 资料中不存在的工具、数据或来源。\n\n"
        "严格输出 JSON：\n"
        '{\n'
        '  "thesis": "一句话概括本文的核心观点（点明 ADHD↔LLM 同构）",\n'
        '  "tools_cited": ["文中真实引用到的工具名", ...],\n'
        '  "body": "markdown 正文（不含 H1 标题）"\n'
        "}"
    )
    data = llm.chat_json(
        [
            {"role": "system", "content": ARTICLE_SYS},
            {"role": "user", "content": user},
        ],
        temperature=0.65,
        max_tokens=6000,
    )
    if not isinstance(data, dict) or "body" not in data:
        raise ValueError(f"文章 {title} 返回结构异常")

    body = data["body"].strip()
    thesis = data.get("thesis", "")
    tools_cited = [t for t in data.get("tools_cited", []) if isinstance(t, str)][:8]

    reading_time = 7 + (seed % 8)
    tags = list(dict.fromkeys([
        "ADHD", "AI", category_name, angle,
        (keywords[seed % len(keywords)] if keywords else "效率"),
    ]))[:6]

    refs = [
        f"- [{s['title']}]({s['url']}) — {grade_label(s['title'], s['url'])}"
        for s in wiki_sources[:6]
    ]
    iso_grade, iso_label = grade_iso_strength(wiki_sources[:6])
    refs_block = (
        f"\n\n## 参考来源\n\n**同构强度：{iso_grade} 级** —— {iso_label}\n\n" + "\n".join(refs)
    ) if refs else ""

    full_content = (
        f"# {title}\n\n"
        + (f"> {subtitle}\n\n" if subtitle else "")
        + body
        + refs_block
        + (
            f"\n\n---\n\n*本文是「ADHD × AI」系列的第 {index + 1} 篇，"
            f"由 AI 智能体从持续维护的 LLM Wiki（全网真实情报）中取材整合生成，并持续迭代更新。*\n"
        )
    )

    frontmatter = {
        "title": title,
        "subtitle": subtitle,
        "description": subtitle,
        "date": pub_date,
        "category": category_name,
        "categoryId": category_id,
        "categoryEn": category_name_en,
        "tags": tags,
        "readingTime": reading_time,
        "slug": slug,
        "topicId": topic_id,
        "angle": angle,
        "rank": topic.get("rank", index + 1),
        "score": topic.get("weighted_score", 0),
        "sourceCount": len(refs),
        "toolsCited": tools_cited,
        "thesis": thesis,
        "problem": problem,
        "spine": spine,
        "spineKind": spine_kind,
        "isEvolved": topic.get("is_evolved", False),
        "llmGenerated": True,
        "isoStrength": iso_grade,
        "caseStudies": [c["name"] for c in cases],
    }
    return {
        "frontmatter": frontmatter,
        "content": full_content,
        "slug": slug,
        "filename": f"{topic_id}.md",
    }


def generate_frontmatter_string(fm: dict) -> str:
    lines = ["---"]
    for key, value in fm.items():
        if isinstance(value, list):
            if not value:
                lines.append(f"{key}: []")
            else:
                lines.append(f"{key}:")
                for item in value:
                    escaped = str(item).replace('"', '\\"')
                    lines.append(f'  - "{escaped}"')
        elif isinstance(value, bool):
            lines.append(f"{key}: {str(value).lower()}")
        elif isinstance(value, str):
            escaped = value.replace('"', '\\"')
            lines.append(f'{key}: "{escaped}"')
        elif isinstance(value, (int, float)):
            lines.append(f"{key}: {value}")
        else:
            lines.append(f'{key}: "{value}"')
    lines.append("---\n")
    return "\n".join(lines)


def save_article(article: dict, output_dir: str) -> str:
    os.makedirs(output_dir, exist_ok=True)
    filepath = os.path.join(output_dir, article["filename"])
    fm_str = generate_frontmatter_string(article["frontmatter"])
    full = fm_str + article["content"]
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(full)
    return filepath
