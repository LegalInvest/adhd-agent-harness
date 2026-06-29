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
            refs.append(f"- [{title_src}]({url})")
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
        "isEvolved": topic.get("is_evolved", False),
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
