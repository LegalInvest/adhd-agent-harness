"""
文章内容生成器
根据选题信息生成完整的 Markdown 格式文章
"""

import hashlib
import os
import re
from datetime import datetime, timedelta


def _seed_from(text: str) -> int:
    return int(hashlib.md5(text.encode("utf-8")).hexdigest()[:8], 16)


def _pick(items: list, text: str, offset: int = 0) -> str:
    idx = (_seed_from(text) + offset) % len(items)
    return items[idx]


# 文章结构模板
ARTICLE_SECTIONS = {
    "ai-tools": [
        "为什么 ADHD 需要这个工具",
        "核心功能与 ADHD 适配点",
        "具体使用场景和方法",
        "设置和个性化技巧",
        "与其他工具的协同使用",
        "实际效果和用户反馈",
        "注意事项和使用建议",
    ],
    "focus": [
        "ADHD 专注力的科学基础",
        "AI 如何介入专注力管理",
        "具体方法和步骤",
        "实践案例和效果",
        "常见问题和解决方案",
        "长期坚持的策略",
        "专家观点和建议",
    ],
    "time-mgmt": [
        "ADHD 时间感知的特殊性",
        "AI 时间管理的核心原理",
        "具体实施步骤",
        "工具和资源推荐",
        "常见挫折和应对方法",
        "建立可持续的时间系统",
        "进阶技巧和优化",
    ],
    "emotion": [
        "理解 ADHD 的情绪特点",
        "AI 情绪管理的科学依据",
        "实用的情绪调节技巧",
        "AI 工具和资源",
        "日常练习和习惯建立",
        "应对特殊情境",
        "长期情绪健康建设",
    ],
    "learning": [
        "ADHD 学习者的独特优势",
        "AI 如何匹配 ADHD 的学习风格",
        "具体学习方法和策略",
        "AI 工具推荐和使用技巧",
        "克服学习障碍的方案",
        "衡量学习效果",
        "持续学习的动力维持",
    ],
    "career": [
        "ADHD 在此领域的优势分析",
        "AI 如何帮助发挥这些优势",
        "具体策略和行动计划",
        "工具和资源清单",
        "成功案例分享",
        "常见挑战和解决方案",
        "职业发展路线图",
    ],
    "entrepreneurship": [
        "ADHD 创业者的独特优势",
        "AI 创业工具和平台",
        "具体操作步骤",
        "成本和资源分析",
        "风险管理和应对",
        "增长策略和扩展",
        "成功案例和启示",
    ],
    "parenting": [
        "理解 ADHD 孩子的需求",
        "AI 如何帮助满足这些需求",
        "家长的具体操作指南",
        "推荐的 AI 工具和资源",
        "建立家庭支持系统",
        "与学校的协作方案",
        "长期教育规划",
    ],
    "science": [
        "研究背景和重要性",
        "最新研究发现",
        "AI 在该领域的具体应用",
        "数据和证据分析",
        "对 ADHD 群体的实际影响",
        "未来研究方向",
        "专家解读和建议",
    ],
    "lifestyle": [
        "ADHD 生活方式的特殊挑战",
        "AI 如何优化日常生活",
        "具体方法和技巧",
        "推荐工具和资源",
        "建立可持续的习惯",
        "常见问题和解决方案",
        "追求更高的生活品质",
    ],
    "community": [
        "社群现状和需求",
        "AI 的赋能作用",
        "具体案例和实践",
        "参与方式和渠道",
        "建立连接和支持网络",
        "面临的挑战和机遇",
        "未来展望和行动呼吁",
    ],
}

# 段落模板 - 不同角度的内容片段
INTRO_TEMPLATES = [
    "如果你是一个 ADHD 人群，你可能已经发现——{pain_point}。但在 AI 时代，这不再是一个无解的难题。{title_theme}正在改变游戏规则。",
    "每一个 ADHD 大脑都是独特的。{pain_point}，这是很多 ADHD 人群的共同经历。今天，我们来聊聊{title_theme}如何用 AI 的力量破解这个困局。",
    "你有没有想过，ADHD 和 AI 竟然是天生的搭档？当{pain_point}时，AI 提供了一种全新的解决思路。让我们深入探讨{title_theme}。",
    "在 ADHD 的世界里，{pain_point}是每天都在上演的剧情。但 AI 正在改写这个故事。{title_theme}可能是你一直在寻找的答案。",
    "作为 ADHD 群体，我们常常面对一个核心挑战：{pain_point}。而 AI 技术的发展，正在为这个挑战提供前所未有的解决方案。",
]

PAIN_POINTS = {
    "ai-tools": "面对工具的选择困难和使用不一致",
    "focus": "专注力像天气一样不可预测",
    "time-mgmt": "时间总是像沙子一样从指缝中流走",
    "emotion": "情绪像过山车一样起起伏伏",
    "learning": "学习效率忽高忽低，难以持续",
    "career": "在职场中感到被低估或不被理解",
    "entrepreneurship": "创业想法很多但执行力跟不上",
    "parenting": "不知道如何帮助有ADHD的孩子",
    "science": "对ADHD的科学认知仍然不够充分",
    "lifestyle": "日常生活总是充满混乱和不可预测性",
    "community": "在社会中感到孤立和不被理解",
}

SECTION_CONTENT_TEMPLATES = [
    "### {section_title}\n\n{topic_name}的关键在于理解 ADHD 大脑的工作方式。研究表明，ADHD 人群在{aspect}方面有着独特的特点。\n\n**核心要点：**\n\n- AI 可以帮助自动化{process}，减少对执行功能的依赖\n- 通过{method}，ADHD 人群可以充分利用自己的优势\n- 关键是找到适合自己节奏的{tool_type}\n\n",
    "### {section_title}\n\n在{topic_name}的实践中，有几个关键因素值得关注：\n\n1. **个性化设置**：每个 ADHD 大脑都不同，AI 工具需要根据个人特点调整\n2. **渐进式导入**：不要一次性改变所有习惯，从最痛的点开始\n3. **即时反馈**：ADHD 大脑需要即时的正向反馈来维持动力\n4. **灵活调整**：允许计划有弹性，AI 帮助在偏离时重新校准\n\n",
    "### {section_title}\n\n> 「ADHD 不是缺陷，而是一种不同的操作系统。AI 就是帮这个操作系统发挥最大潜能的软件。」\n\n{topic_name}的核心原理基于以下观察：\n\n- ADHD 大脑在{aspect}上有着超乎常人的能力\n- AI 可以弥补{weakness}方面的不足\n- 两者结合可以创造出{outcome}\n\n实际操作中，建议从以下步骤开始：\n\n**第一步**：评估你当前在{aspect}方面的状态\n**第二步**：选择一个 AI 工具来辅助{process}\n**第三步**：设定一个小目标，在一周内测试效果\n**第四步**：根据反馈调整策略\n\n",
]

ASPECTS = [
    "创造力和发散思维", "模式识别和联想能力", "高能量和激情",
    "快速学习和适应", "在感兴趣的领域深度专注", "同理心和直觉",
    "风险承受和创新精神", "多任务处理的灵活性", "对新事物的好奇心",
]

WEAKNESSES = [
    "持续注意力和工作记忆", "时间感知和任务启动", "情绪调节和冲动控制",
    "组织和规划能力", "一致性和例程维护", "优先级判断和决策",
]

PROCESSES = [
    "任务分解和进度追踪", "日程安排和时间管理", "信息整理和知识管理",
    "决策支持和方案评估", "习惯建立和行为跟踪", "情绪记录和模式分析",
]

METHODS = [
    "结构化的AI辅助工作流", "游戏化的激励机制", "视觉化的进度展示",
    "个性化的AI提醒系统", "社交互助的AI匹配", "数据驱动的自我优化",
]

TOOL_TYPES = [
    "AI助手和工作流工具", "专注力和注意力训练应用", "时间管理和日程规划系统",
    "情绪追踪和心理健康平台", "学习辅助和知识管理工具", "创意激发和内容创作工具",
]

OUTCOMES = [
    "1+1>2的协同效果", "前所未有的生产力提升", "更加从容和自信的生活状态",
    "持续且有趣的自我提升循环", "健康高效的工作和生活平衡", "充分发挥天赋的自我实现",
]

CONCLUSION_TEMPLATES = [
    "## 写在最后\n\nADHD 不是你的限制，而是你的独特操作系统。AI 不是万能的解药，但它是一个强大的工具——当你学会正确使用它时，你会发现自己拥有超乎想象的潜力。\n\n记住：开始不需要完美，只需要开始。选择这篇文章中最打动你的一个方法，今天就试试看。\n\n**你的 ADHD 大脑 + AI = 无限可能。**",
    "## 结语\n\n在 ADHD × AI 的旅程中，最重要的不是工具本身，而是你愿意尝试和探索的勇气。每一个小步骤都在积累，每一次尝试都有价值。\n\n如果你从这篇文章中学到了一些有用的东西，不妨分享给身边也有 ADHD 的朋友。我们一起，用 AI 的力量，活出最好的自己。\n\n**ADHD × AI，不是对抗，而是共舞。**",
    "## 最后的话\n\n改变不会在一夜之间发生。但有了 AI 的帮助，ADHD 人群正在获得前所未有的工具和支持。关键是找到适合自己的节奏，建立可持续的系统。\n\n从今天开始，选择一个方向，迈出第一步。你的 ADHD 大脑有着独特的天赋，AI 只是帮你释放这些天赋的钥匙。\n\n**拥抱你的 ADHD，善用 AI 的力量，创造属于你的精彩人生。**",
]


def _slugify(title: str) -> str:
    """将中文标题转换为URL友好的slug"""
    slug = title.lower()
    slug = re.sub(r"[^\w\u4e00-\u9fff\s-]", "", slug)
    slug = re.sub(r"[\s_]+", "-", slug)
    slug = slug.strip("-")
    # 限制长度
    if len(slug) > 80:
        slug = slug[:80].rsplit("-", 1)[0]
    return slug


def generate_article(topic: dict, index: int) -> dict:
    """
    根据选题生成完整的文章内容

    Returns:
        包含 frontmatter 和 content 的字典
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

    # 生成发布日期（分散在最近90天内）
    base_date = datetime(2025, 6, 1)
    day_offset = seed % 90
    pub_date = base_date - timedelta(days=day_offset)
    date_str = pub_date.strftime("%Y-%m-%d")

    # 阅读时间估算
    reading_time = 8 + (seed % 7)  # 8-14 分钟

    # 生成标签
    tags = list(set([
        "ADHD", "AI",
        category_name,
        _pick(keywords, title, 0) if keywords else "效率",
        _pick(keywords, title, 1) if keywords else "工具",
        angle,
    ]))[:6]

    # 生成文章内容
    sections = ARTICLE_SECTIONS.get(category_id, ARTICLE_SECTIONS["ai-tools"])
    pain_point = PAIN_POINTS.get(category_id, "面对各种日常挑战")

    # 引言
    intro_template = _pick(INTRO_TEMPLATES, title)
    intro = intro_template.format(
        pain_point=pain_point,
        title_theme=title.split("：")[0] if "：" in title else title,
    )

    # 正文各节
    body_parts = []
    for i, section_title in enumerate(sections):
        template = SECTION_CONTENT_TEMPLATES[i % len(SECTION_CONTENT_TEMPLATES)]
        content = template.format(
            section_title=section_title,
            topic_name=title,
            aspect=_pick(ASPECTS, title, i),
            weakness=_pick(WEAKNESSES, title, i + 1),
            process=_pick(PROCESSES, title, i + 2),
            method=_pick(METHODS, title, i + 3),
            tool_type=_pick(TOOL_TYPES, title, i + 4),
            outcome=_pick(OUTCOMES, title, i + 5),
        )
        body_parts.append(content)

    # 结语
    conclusion = _pick(CONCLUSION_TEMPLATES, subtitle)

    # 组合完整文章
    full_content = f"""# {title}

> {subtitle}

{intro}

{"".join(body_parts)}
{conclusion}

---

*本文是「ADHD × AI」系列的第 {index + 1} 篇。关注我们，获取更多 ADHD 与 AI 的实用内容。*
"""

    # 构建 frontmatter
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
    }

    return {
        "frontmatter": frontmatter,
        "content": full_content,
        "slug": slug,
        "filename": f"{topic_id}.md",
    }


def generate_frontmatter_string(fm: dict) -> str:
    """将 frontmatter 字典转换为 YAML 字符串"""
    lines = ["---"]
    for key, value in fm.items():
        if isinstance(value, list):
            lines.append(f"{key}:")
            for item in value:
                lines.append(f'  - "{item}"')
        elif isinstance(value, str):
            # 转义引号
            escaped = value.replace('"', '\\"')
            lines.append(f'{key}: "{escaped}"')
        elif isinstance(value, (int, float)):
            lines.append(f"{key}: {value}")
        else:
            lines.append(f'{key}: "{value}"')
    lines.append("---\n")
    return "\n".join(lines)


def save_article(article: dict, output_dir: str) -> str:
    """保存文章到文件"""
    os.makedirs(output_dir, exist_ok=True)
    filepath = os.path.join(output_dir, article["filename"])

    fm_str = generate_frontmatter_string(article["frontmatter"])
    full = fm_str + article["content"]

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(full)

    return filepath
