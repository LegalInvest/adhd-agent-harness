"""
知识萃取与管理模块
从抓取的网页内容中萃取结构化知识：真实工具、研究发现、统计数据、实用策略、专家观点
并提供按主题检索知识的接口，作为文章生成的"事实燃料"
"""

import json
import os
import re
from collections import Counter
from dataclasses import dataclass, field, asdict

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")


# 已知的真实 AI×ADHD 工具库（名称 → 简介、适配点）
# 这些工具均在抓取的真实文章中被反复提及
KNOWN_TOOLS = {
    "Goblin Tools": {
        "aliases": ["goblin.tools", "goblin tools", "magic todo", "magictodo"],
        "category": "ai-tools",
        "desc": "一套专为神经多样性人群设计的轻量 AI 工具集，其中 Magic ToDo 能把一个笼统的任务自动拆解成可执行的微步骤",
        "use_case": "克服任务启动困难和「不知道从哪下手」的瘫痪感",
    },
    "Saner.AI": {
        "aliases": ["saner.ai", "saner ai"],
        "category": "ai-tools",
        "desc": "面向 ADHD 的 AI 个人助理，整合笔记、邮件、日程，用自然语言管理所有碎片信息",
        "use_case": "把散落各处的想法、待办和提醒集中到一个 AI 大脑里",
    },
    "Motion": {
        "aliases": ["usemotion", "motion app"],
        "category": "time-mgmt",
        "desc": "AI 日历和任务管理工具，能根据优先级和截止日期自动排布你的一天，任务延误时自动重新规划",
        "use_case": "解决 ADHD 的时间盲和过度承诺，让 AI 替你做日程决策",
    },
    "Reclaim.ai": {
        "aliases": ["reclaim.ai", "reclaim ai"],
        "category": "time-mgmt",
        "desc": "AI 日程防御工具，自动为习惯、任务和休息时间在日历上预留并保护时间块",
        "use_case": "防止日程被会议填满，为深度工作和恢复留出空间",
    },
    "Tiimo": {
        "aliases": ["tiimo"],
        "category": "time-mgmt",
        "desc": "视觉化的日程与计划 App，专为神经多样性设计，用图标、颜色和倒计时让时间「看得见」",
        "use_case": "对抗时间盲，把抽象的时间转化为视觉信号",
    },
    "Brain.fm": {
        "aliases": ["brain.fm", "brainfm", "brain fm"],
        "category": "focus",
        "desc": "基于神经科学的 AI 功能性音乐平台，用特定节奏的声音诱导专注、放松或睡眠状态",
        "use_case": "用声音环境帮助 ADHD 大脑更快进入并维持专注状态",
    },
    "Focusmate": {
        "aliases": ["focusmate"],
        "category": "focus",
        "desc": "虚拟共同工作（body doubling）平台，把你和另一个真人配对进行计时专注 session",
        "use_case": "利用「身体在场效应」对抗拖延和孤独工作时的分心",
    },
    "Structured": {
        "aliases": ["structured app"],
        "category": "time-mgmt",
        "desc": "可视化的每日时间线规划 App，把一天排成清晰的视觉时间轴",
        "use_case": "让 ADHD 用户对一天的节奏有直观掌控感",
    },
    "Lex": {
        "aliases": ["lex.page", "lex ai"],
        "category": "ai-tools",
        "desc": "内置 AI 的写作工具，能在你卡壳时续写、生成大纲、克服空白页恐惧",
        "use_case": "解决 ADHD 写作启动困难和组织思路的难题",
    },
    "Mem": {
        "aliases": ["mem.ai", "mem ai"],
        "category": "ai-tools",
        "desc": "AI 驱动的笔记工具，自动整理和关联你的笔记，无需手动建立文件夹结构",
        "use_case": "适配 ADHD 不擅长手动归类整理的特点，让 AI 自动建立知识连接",
    },
    "ChatGPT": {
        "aliases": ["chatgpt", "gpt-4", "gpt4", "openai"],
        "category": "ai-tools",
        "desc": "通用对话式 AI，可充当 ADHD 的「认知协作者」：拆解任务、起草文本、整理思绪、模拟教练",
        "use_case": "作为随叫随到的执行功能外挂，弥补工作记忆和组织能力的不足",
    },
    "Claude": {
        "aliases": ["claude", "anthropic"],
        "category": "ai-tools",
        "desc": "Anthropic 的对话式 AI，以长文理解和更自然的对话著称，适合深度梳理复杂任务",
        "use_case": "处理长文档、深度对话式思考整理",
    },
    "Otter.ai": {
        "aliases": ["otter.ai", "otter ai"],
        "category": "ai-tools",
        "desc": "AI 会议转录工具，自动记录、转写并总结会议要点和行动项",
        "use_case": "弥补 ADHD 在会议中走神、记不住要点的问题",
    },
    "Reflect": {
        "aliases": ["reflect.app", "reflect notes"],
        "category": "ai-tools",
        "desc": "AI 笔记工具，强调网状链接和 AI 辅助回顾",
        "use_case": "帮助 ADHD 把碎片想法连成网络",
    },
    "Routinery": {
        "aliases": ["routinery"],
        "category": "lifestyle",
        "desc": "习惯例程 App，把晨间/晚间例程拆成带计时的步骤序列",
        "use_case": "用结构化例程对抗 ADHD 的日常混乱",
    },
    "Todoist": {
        "aliases": ["todoist"],
        "category": "time-mgmt",
        "desc": "任务管理 App，带自然语言输入和 AI 辅助功能",
        "use_case": "快速捕捉待办，减少遗忘",
    },
    "Inflow": {
        "aliases": ["inflow app"],
        "category": "emotion",
        "desc": "基于 CBT（认知行为疗法）的 ADHD 自助管理 App，提供结构化课程和工具",
        "use_case": "用循证心理方法管理 ADHD 症状和情绪",
    },
    "Endel": {
        "aliases": ["endel"],
        "category": "focus",
        "desc": "AI 生成的自适应声景 App，根据时间、天气、心率实时生成专注或放松音景",
        "use_case": "个性化的声音环境帮助专注和放松",
    },
    "Forest": {
        "aliases": ["forest app"],
        "category": "focus",
        "desc": "游戏化专注 App，专注时种一棵虚拟树，离开则树枯死",
        "use_case": "用游戏化机制和损失厌恶对抗手机分心",
    },
    "RescueTime": {
        "aliases": ["rescuetime"],
        "category": "focus",
        "desc": "自动时间追踪工具，记录你在各应用和网站上花的时间并生成报告",
        "use_case": "帮 ADHD 看清「时间都去哪了」",
    },
    "Habitica": {
        "aliases": ["habitica"],
        "category": "lifestyle",
        "desc": "把习惯养成变成 RPG 游戏的 App，完成任务获得经验和装备",
        "use_case": "用游戏化奖励驱动 ADHD 大脑的多巴胺需求",
    },
    "Perplexity": {
        "aliases": ["perplexity"],
        "category": "learning",
        "desc": "AI 搜索引擎，直接给出带引用来源的答案而非一堆链接",
        "use_case": "满足 ADHD 的好奇心，让探索式学习更高效不易跑偏",
    },
    "Speechify": {
        "aliases": ["speechify"],
        "category": "learning",
        "desc": "AI 文本转语音工具，把文章、邮件、PDF 转成自然语音",
        "use_case": "适配 ADHD 的听觉学习偏好，把阅读变成听",
    },
}


# 核心概念词典：ADHD × AI 领域的关键概念，用于内容深度
CORE_CONCEPTS = {
    "executive function": "执行功能（计划、组织、启动、工作记忆等大脑管理能力）",
    "working memory": "工作记忆（短期保持和操作信息的能力）",
    "time blindness": "时间盲（难以感知时间流逝和估算时长）",
    "body doubling": "身体在场效应（有人陪伴时更容易专注完成任务）",
    "dopamine": "多巴胺（与动机和奖励相关的神经递质，ADHD 大脑相对缺乏）",
    "task initiation": "任务启动（开始一项任务的能力，ADHD 常见困难）",
    "rejection sensitive dysphoria": "拒绝敏感性焦虑（RSD，对批评和拒绝的强烈情绪反应）",
    "hyperfocus": "超聚焦（ADHD 在感兴趣领域的高强度专注状态）",
    "cognitive load": "认知负荷（大脑同时处理信息的负担）",
    "neuroplasticity": "神经可塑性（大脑通过训练改变结构的能力）",
    "emotional dysregulation": "情绪失调（难以调节情绪强度和恢复）",
    "executive dysfunction": "执行功能障碍",
}


# ────────────────────────────────────────────────────────────────────
# 同构脊柱（Spine）：「ADHD 大脑 ↔ LLM」同构论的核心概念页。
# 分两类：
#   - bridge：跨域综合概念，terms 同时命中 ADHD 域与 harness 域素材，
#             由 LLM 从两端真实摘录里合成「同构」论点。
#   - llm   ：LLM/agent harness 侧概念，与某个 ADHD 执行功能缺陷结构对应。
# 这些概念页会与 CORE_CONCEPTS、工具页交叉互链，构成 400 篇选题的脊柱。
# ────────────────────────────────────────────────────────────────────
SPINE_CONCEPTS = [
    {
        "name": "ADHD 大脑与 LLM 的同构",
        "kind": "bridge",
        "terms": [
            "analogy", "large language model", "llm", "adhd", "brain",
            "executive function", "cognitive", "同构", "执行功能",
        ],
        "mirror": "总纲：高产生成核心 + 缺失的执行调度层",
    },
    {
        "name": "外部执行功能层",
        "kind": "bridge",
        "terms": [
            "executive function", "external", "externalize", "外化", "外部",
            "执行功能", "cognitive prosthesis", "second brain", "scaffold",
            "working memory", "工作记忆", "agent memory",
        ],
        "mirror": "执行功能 / 工作记忆 ↔ agent 的外部记忆与编排层",
    },
    {
        "name": "生成核心与调度层",
        "kind": "bridge",
        "terms": [
            "generative", "orchestration", "agent", "executive", "调度",
            "core model", "reasoning", "planner", "执行功能",
        ],
        "mirror": "把'智力/算力'与'编排/执行'解耦——两边瓶颈都在后者",
    },
    {
        "name": "拐杖与脚手架",
        "kind": "bridge",
        "terms": [
            "scaffold", "scaffolding", "training wheels", "dependence",
            "dependency", "over-reliance", "拐杖", "依赖", "脚手架",
        ],
        "mirror": "过度依赖风险：harness/工具应是会褪去的脚手架而非永久拐杖",
    },
    {
        "name": "无状态与外部记忆",
        "kind": "llm",
        "terms": [
            "stateless", "statelessness", "session memory", "scratchpad",
            "agent memory", "persistent memory", "vector store",
            "external memory", "second brain", "retrieval",
        ],
        "mirror": "工作记忆缺陷 ↔ LLM 无跨会话状态：都靠外部记忆补偿",
    },
    {
        "name": "上下文工程",
        "kind": "llm",
        "terms": [
            "context engineering", "context window", "context management",
            "retrieval augmented", "rag", "prompt", "summarization",
        ],
        "mirror": "易被环境带偏 ↔ 上下文窗口管理：都需主动管理'当下注意什么'",
    },
    {
        "name": "幻觉与验证循环",
        "kind": "llm",
        "terms": [
            "hallucination", "grounding", "verification", "self-critique",
            "self-consistency", "fact check", "critique loop",
        ],
        "mirror": "冲动/想当然 ↔ LLM 自信幻觉：都靠核对与验证循环兜底",
    },
    {
        "name": "采样温度与表现波动",
        "kind": "llm",
        "terms": [
            "temperature", "sampling", "variance", "deterministic",
            "determinism", "output variability",
        ],
        "mirror": "ADHD 表现日内波动 ↔ LLM 采样随机性：都靠结构约束稳定输出",
    },
    {
        "name": "工具使用与认知卸载",
        "kind": "llm",
        "terms": [
            "function calling", "tool use", "tools", "offload", "offloading",
            "external tool", "calculator", "code execution",
        ],
        "mirror": "把不擅长的精确状态外包 ↔ agent function calling",
    },
    {
        "name": "规划循环与任务分解",
        "kind": "llm",
        "terms": [
            "planning", "planner", "task decomposition", "decompose",
            "agentic workflow", "executor", "react", "subtask", "step by step",
        ],
        "mirror": "任务启动/拆解困难 ↔ agent planner-executor 循环",
    },
    {
        "name": "重锚定与目标漂移",
        "kind": "llm",
        "terms": [
            "re-grounding", "goal drift", "system prompt", "long horizon",
            "drift", "stay on task", "reminder",
        ],
        "mirror": "分心/超聚焦跑偏 ↔ agent 长程目标漂移：都靠重锚定目标",
    },
    {
        "name": "人在回路与身体在场",
        "kind": "llm",
        "terms": [
            "human in the loop", "human-in-the-loop", "oversight",
            "guardrails", "supervision", "body doubling", "accountability",
        ],
        "mirror": "身体在场效应(body doubling) ↔ human-in-the-loop 监督",
    },
]


def spine_concept_names() -> list[str]:
    return [c["name"] for c in SPINE_CONCEPTS]


@dataclass
class KnowledgeItem:
    kind: str           # tool | finding | statistic | strategy | concept
    text: str
    source_title: str = ""
    source_url: str = ""
    category: str = ""
    keywords: list[str] = field(default_factory=list)


def _split_sentences(text: str) -> list[str]:
    """中英文混合分句"""
    parts = re.split(r"(?<=[.!?。！？])\s+|\n+", text)
    return [p.strip() for p in parts if p and len(p.strip()) > 20]


def extract_statistics(articles: list[dict]) -> list[KnowledgeItem]:
    """萃取含统计数据的事实句"""
    items = []
    seen = set()
    # 匹配百分比、样本量、患病率等
    stat_re = re.compile(
        r"\b\d[\d,\.]*\s*(?:%|percent|million|billion|参与者|名|人|项研究|studies|study|"
        r"participants|adults|children|patients|articles|countries)\b",
        re.IGNORECASE,
    )
    for a in articles:
        for sent in _split_sentences(a.get("content", "")):
            if 30 < len(sent) < 280 and stat_re.search(sent):
                key = sent[:60].lower()
                if key not in seen:
                    seen.add(key)
                    items.append(KnowledgeItem(
                        kind="statistic",
                        text=sent,
                        source_title=a.get("title", ""),
                        source_url=a.get("url", ""),
                    ))
    return items


def extract_findings(articles: list[dict]) -> list[KnowledgeItem]:
    """萃取研究发现类句子（含研究信号词）"""
    items = []
    seen = set()
    signal_words = [
        "study found", "research shows", "researchers", "study", "trial",
        "accuracy", "deep learning", "machine learning", "EEG", "MRI",
        "diagnosis", "algorithm", "model", "data", "evidence", "review",
        "研究", "发现", "诊断", "准确率", "算法", "模型", "证据",
    ]
    for a in articles:
        for sent in _split_sentences(a.get("content", "")):
            low = sent.lower()
            if 40 < len(sent) < 300 and any(w in low for w in signal_words):
                key = sent[:60].lower()
                if key not in seen:
                    seen.add(key)
                    items.append(KnowledgeItem(
                        kind="finding",
                        text=sent,
                        source_title=a.get("title", ""),
                        source_url=a.get("url", ""),
                    ))
    return items


def extract_strategies(articles: list[dict]) -> list[KnowledgeItem]:
    """萃取可操作的策略/技巧/提示词类句子"""
    items = []
    seen = set()
    action_words = [
        "try", "use", "ask", "prompt", "break down", "set", "create",
        "start", "schedule", "tip", "strategy", "step", "how to",
        "尝试", "使用", "可以", "建议", "提示", "技巧", "策略", "步骤", "方法",
    ]
    for a in articles:
        for sent in _split_sentences(a.get("content", "")):
            low = sent.lower()
            if 40 < len(sent) < 260 and any(w in low for w in action_words):
                key = sent[:60].lower()
                if key not in seen:
                    seen.add(key)
                    items.append(KnowledgeItem(
                        kind="strategy",
                        text=sent,
                        source_title=a.get("title", ""),
                        source_url=a.get("url", ""),
                    ))
    return items


def extract_tools(articles: list[dict]) -> list[KnowledgeItem]:
    """识别文章中真实出现的工具，返回工具知识项"""
    full_text = " ".join(a.get("content", "") + " " + a.get("title", "") for a in articles).lower()
    items = []
    for name, info in KNOWN_TOOLS.items():
        mentioned = name.lower() in full_text or any(
            alias in full_text for alias in info["aliases"]
        )
        if mentioned:
            items.append(KnowledgeItem(
                kind="tool",
                text=f"{name}：{info['desc']}。适用场景：{info['use_case']}。",
                category=info["category"],
                keywords=[name],
            ))
    return items


def build_knowledge_base(articles: list[dict]) -> dict:
    """
    从抓取的文章构建完整知识库

    Returns:
        结构化知识库字典
    """
    tools = extract_tools(articles)
    findings = extract_findings(articles)
    statistics = extract_statistics(articles)
    strategies = extract_strategies(articles)

    kb = {
        "meta": {
            "source_articles": len(articles),
            "total_source_chars": sum(a.get("content_length", 0) for a in articles),
            "tools": len(tools),
            "findings": len(findings),
            "statistics": len(statistics),
            "strategies": len(strategies),
        },
        "tools": [asdict(t) for t in tools],
        "findings": [asdict(f) for f in findings],
        "statistics": [asdict(s) for s in statistics],
        "strategies": [asdict(s) for s in strategies],
        "concepts": CORE_CONCEPTS,
        "sources": [
            {"title": a.get("title", ""), "url": a.get("url", "")}
            for a in articles
        ],
    }
    return kb


def save_knowledge_base(kb: dict, filename: str = "knowledge_base.json") -> str:
    os.makedirs(DATA_DIR, exist_ok=True)
    filepath = os.path.join(DATA_DIR, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(kb, f, indent=2, ensure_ascii=False)
    return filepath


def load_knowledge_base(filename: str = "knowledge_base.json") -> dict:
    filepath = os.path.join(DATA_DIR, filename)
    if os.path.exists(filepath):
        with open(filepath, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}


class KnowledgeRetriever:
    """
    知识检索器：给定主题/分类/关键词，返回最相关的知识项
    用于在文章生成时注入真实事实
    """

    def __init__(self, kb: dict):
        self.kb = kb
        self.tools = kb.get("tools", [])
        self.findings = kb.get("findings", [])
        self.statistics = kb.get("statistics", [])
        self.strategies = kb.get("strategies", [])
        self.concepts = kb.get("concepts", {})
        self.sources = kb.get("sources", [])
        # 预计算小写文本，避免每次检索都重复 .lower()（大规模学术语料下是性能关键）
        for coll in (self.findings, self.statistics, self.strategies):
            for item in coll:
                if "_low" not in item:
                    item["_low"] = item.get("text", "").lower()
        self._query_cache: dict = {}

    @staticmethod
    def _relevance(text: str, keywords: list[str]) -> int:
        low = text.lower()
        return sum(1 for kw in keywords if kw.lower() in low)

    @staticmethod
    def _rel_low(low: str, kw_low: list[str]) -> int:
        return sum(1 for kw in kw_low if kw in low)

    def _ranked(self, coll_name: str, keywords: list[str], limit: int,
                offset: int, require_relevant: bool) -> list[dict]:
        """带缓存的相关性排序检索（关键词常在同类选题间复用，缓存命中率高）。"""
        kw_low = tuple(sorted(k.lower() for k in keywords))
        key = (coll_name, kw_low, limit, offset, require_relevant)
        cached = self._query_cache.get(key)
        if cached is not None:
            return cached
        coll = getattr(self, coll_name)
        kw_list = list(kw_low)
        scored = sorted(
            coll, key=lambda it: self._rel_low(it["_low"], kw_list), reverse=True
        )
        if require_relevant:
            relevant = [it for it in scored if self._rel_low(it["_low"], kw_list) > 0]
            pool = relevant if relevant else scored
        else:
            pool = scored
        if not pool:
            self._query_cache[key] = []
            return []
        start = offset % max(len(pool), 1)
        result = (pool[start:] + pool[:start])[:limit]
        self._query_cache[key] = result
        return result

    def tools_for_category(self, category_id: str, limit: int = 4) -> list[dict]:
        matched = [t for t in self.tools if t.get("category") == category_id]
        others = [t for t in self.tools if t.get("category") != category_id]
        return (matched + others)[:limit]

    def findings_for(self, keywords: list[str], limit: int = 3, offset: int = 0) -> list[dict]:
        return self._ranked("findings", keywords, limit, offset, require_relevant=True)

    def statistics_for(self, keywords: list[str], limit: int = 2, offset: int = 0) -> list[dict]:
        return self._ranked("statistics", keywords, limit, offset, require_relevant=False)

    def strategies_for(self, keywords: list[str], limit: int = 4, offset: int = 0) -> list[dict]:
        return self._ranked("strategies", keywords, limit, offset, require_relevant=True)
