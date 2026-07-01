"""
问题驱动的选题池（同构脊柱版）

每个选题不再是名词标题，而是一个**真实问题**——既是 ADHD 用户在问的，
也是 LLM/agent 工程师在问的。文章用「ADHD 大脑 ↔ LLM 同构」脊柱 + 双域证据来回答。

选题池远大于 400，交给 scorer/evolution 滚动晋升：
契合同构脊柱、双域证据强的问题留下，弱问题被新发现替换。
"""

from __future__ import annotations

from engine.categories import CATEGORIES
from engine.knowledge import KNOWN_TOOLS, SPINE_CONCEPTS


# 每条同构脊柱 → 一组「问题驱动」选题规格
# pain：ADHD 一侧的真实困扰；parallel：LLM/harness 一侧的对应工程问题
SPINE_PROBLEM_SPECS = [
    {
        "spine": "无状态与外部记忆",
        "category_id": "ai-tools",
        "pain": "工作记忆容量小、边做边忘",
        "parallel": "LLM 无跨会话状态，靠外部记忆/向量库续命",
        "mirror": "外部记忆/向量库",
        "questions": [
            "ADHD 的工作记忆总在「边做边忘」，能不能像给 agent 接外部记忆那样，给大脑装一个「第二大脑」？",
            "为什么 ADHD 记不住事，和 LLM 的「无状态」是同一个问题？外部记忆是两边共同的解法吗？",
            "把待办、灵感、上下文都丢给 AI 记，会不会让 ADHD 的工作记忆更退化（拐杖化）？",
        ],
    },
    {
        "spine": "上下文工程",
        "category_id": "focus",
        "pain": "注意力容易被环境带偏",
        "parallel": "LLM 受上下文窗口内容左右，需要上下文工程",
        "mirror": "上下文工程",
        "questions": [
            "ADHD 一被打断就「跑题」，和 LLM 被无关上下文带偏是同一回事吗？「上下文工程」能套用到注意力管理上吗？",
            "如何像管理 LLM 的上下文窗口一样，主动管理 ADHD 大脑「此刻该注意什么」？",
            "环境设计 vs 屏蔽干扰：ADHD 的注意力到底该「清空上下文」还是「重写上下文」？",
        ],
    },
    {
        "spine": "幻觉与验证循环",
        "category_id": "science",
        "pain": "冲动下结论、想当然",
        "parallel": "LLM 自信地编造（幻觉），靠验证与自我批判兜底",
        "mirror": "self-critique 验证循环",
        "questions": [
            "ADHD 的「冲动下结论」和 LLM 的「自信幻觉」结构上是一回事吗？验证循环能同时治两者吗？",
            "给 ADHD 加一道「核对清单/验证步骤」，和给 agent 加 self-critique 循环，是同一种工程吗？",
            "为什么「让 AI 帮我检查」对 ADHD 有效，却也可能制造新的幻觉？",
        ],
    },
    {
        "spine": "采样温度与表现波动",
        "category_id": "lifestyle",
        "pain": "状态日内大幅波动、不稳定",
        "parallel": "LLM 采样温度带来输出随机性，靠结构约束稳定",
        "mirror": "调低采样温度",
        "questions": [
            "ADHD 的「今天神明天废」和 LLM 的采样随机性像吗？「降低温度」式的结构约束能稳定 ADHD 的输出吗？",
            "例程、模板、脚手架之于 ADHD，是不是就像「降 temperature + 结构化输出」之于 LLM？",
            "想要稳定，又怕失去 ADHD 的创造性爆发——表现波动到底该压制还是该利用？",
        ],
    },
    {
        "spine": "工具使用与认知卸载",
        "category_id": "ai-tools",
        "pain": "不擅长精确、重复、状态维护类任务",
        "parallel": "agent 通过 function calling 把精确计算外包给工具",
        "mirror": "function calling 工具调用",
        "questions": [
            "ADHD 该把哪些事「外包」给 AI？这和 agent 用 function calling 卸载精确计算是同一个判断标准吗？",
            "认知卸载到什么程度算「聪明地用工具」，到什么程度算「能力退化」？",
            "为什么把记账、计算、排程交给 AI，对 ADHD 的收益可能比对普通人大得多？",
        ],
    },
    {
        "spine": "规划循环与任务分解",
        "category_id": "time-mgmt",
        "pain": "任务启动困难、不会拆解",
        "parallel": "agent 用 planner-executor 循环分解长任务",
        "mirror": "planner-executor 任务分解",
        "questions": [
            "「打扫房间」对 ADHD 为何难如登天？把它当成 agent 的任务分解（planner-executor）来处理会怎样？",
            "AI 自动把大任务拆成原子步骤，和 agent 的 planning loop 是同一套机制吗？对 ADHD 真有用吗？",
            "任务启动困难的本质，是缺一个「执行器」还是缺一个「规划器」？",
        ],
    },
    {
        "spine": "重锚定与目标漂移",
        "category_id": "focus",
        "pain": "分心走神或超聚焦跑偏，丢失目标",
        "parallel": "长程任务里 agent 会目标漂移，需要重锚定 system prompt",
        "mirror": "重锚定 system prompt",
        "questions": [
            "ADHD 的「走神」和 agent 跑长任务时的「目标漂移」是同一种失败吗？「重锚定」该怎么做？",
            "如何给 ADHD 设计一个像 system prompt 那样、能随时把人拉回目标的「锚」？",
            "超聚焦到忘记吃饭，算不算一种「停不下来的目标漂移」？怎么用 AI 打断它？",
        ],
    },
    {
        "spine": "人在回路与身体在场",
        "category_id": "community",
        "pain": "独自做事缺乏问责、容易放弃",
        "parallel": "高风险 agent 需要 human-in-the-loop 监督",
        "mirror": "human-in-the-loop 监督",
        "questions": [
            "Body doubling（身体在场）为什么对 ADHD 有效？它和给 AI agent 加 human-in-the-loop 是同构的吗？",
            "AI 能不能替代「有人陪着一起做」的问责感，还是说人类回路不可替代？",
            "把「监督者」这个角色交给 AI，对 ADHD 是减负还是制造新的依赖？",
        ],
    },
    {
        "spine": "外部执行功能层",
        "category_id": "science",
        "pain": "执行功能（计划/组织/启动）先天偏弱",
        "parallel": "agent 的编排/记忆/工具层就是「外部执行功能」",
        "mirror": "agent 的编排层",
        "questions": [
            "如果执行功能可以「外置」，那 agent 的编排层是不是一份现成的 ADHD 执行功能蓝图？",
            "AI 究竟是补上了 ADHD 缺失的执行功能层，还是只是又一个待管理的工具？",
            "「认知义肢」这个说法对 ADHD 成立吗？外部执行功能层的边界在哪里？",
        ],
    },
    {
        "spine": "生成核心与调度层",
        "category_id": "career",
        "pain": "有想法有能力，却卡在执行与落地",
        "parallel": "LLM 智力强但需要外部编排才能完成长任务",
        "mirror": "外部编排调度层",
        "questions": [
            "ADHD 的瓶颈从来不是「不够聪明」，而是缺调度层——这点和 LLM 一模一样吗？",
            "把「智力/创意」和「执行/编排」解耦后，ADHD 该把精力投在哪一层？",
            "职场上如何让 ADHD 当「生成核心」、让 AI 当「调度层」，组成一个完整系统？",
        ],
    },
    {
        "spine": "拐杖与脚手架",
        "category_id": "emotion",
        "pain": "怕过度依赖工具、又怕没有支撑就崩",
        "parallel": "harness 应是会褪去的脚手架，而非永久拐杖",
        "mirror": "会褪去的脚手架",
        "questions": [
            "AI 对 ADHD 到底是「会褪去的脚手架」还是「永久拐杖」？怎么判断自己越过了那条线？",
            "给 LLM 太多自主会跑飞，ADHD 完全外包给工具会「拐杖化」——两种失败如何同时避免？",
            "理想状态下，AI 用久了之后 ADHD 的内在能力应该变强还是变弱？",
        ],
    },
    {
        "spine": "ADHD 大脑与 LLM 的同构",
        "category_id": "science",
        "pain": "想理解自己的大脑到底是怎么回事",
        "parallel": "LLM 是「高产但缺执行调度层的生成核心」",
        "mirror": "生成核心 + 缺失的执行层",
        "questions": [
            "ADHD 大脑和大语言模型，真的是「同一类心智」——高产生成核心 + 缺失的执行层吗？",
            "如果 ADHD 和 LLM 同构，那三年来 agent 工程的所有招数，是不是都能迁移成 ADHD 适配方案？",
            "这个同构在哪里会失效？把人脑类比成 LLM 的风险和边界是什么？",
        ],
    },
]


# 跨脊柱 × 工具的问题模板（用于把池子扩到 400+，并支持滚动替换）
TOOL_PROBLEM_TEMPLATES = [
    ("用 {tool} 给 ADHD 补上{layer}，真的能像 agent 那样工作吗？",
     "把 {tool} 当作 ADHD 的外部执行层来实测：它补的是哪一块短板？"),
    ("{tool} 之于 ADHD，是脚手架还是拐杖？",
     "从「同构」视角评测 {tool}：用久了会让 ADHD 更强还是更依赖？"),
    ("ADHD 想把{pain}外包给 {tool}，该怎么设计这套「人 + AI」的回路？",
     "把 {tool} 接进 ADHD 工作流：哪些该交给它，哪些必须自己留着？"),
    ("如果把 ADHD 大脑当成生成核心，{tool} 能不能当它的{layer}？",
     "用 agent 工程的思路重新理解 {tool} 对 ADHD 的真正价值。"),
    ("{tool} 解决了 ADHD 的{pain}，代价是什么？",
     "{tool} 的收益与「能力退化」风险：一份诚实的同构权衡。"),
]

# 受众框架：把同一条脊柱问题落到不同人群的真实场景里（扩池 + 提升检索覆盖）
AUDIENCE_FRAMES = [
    ("ADHD 学生", "考试与作业"),
    ("ADHD 职场人", "项目推进与汇报"),
    ("ADHD 家长", "陪伴 ADHD 孩子"),
    ("ADHD 创业者", "把想法落地执行"),
    ("ADHD 自由职业者", "无人监督下的自我管理"),
    ("ADHD 研究生", "长周期科研与论文"),
    ("ADHD 程序员", "在 IDE 与 agent 之间切换"),
]


# ── 病毒级双受众钩子 ──
# 每条标题都必须同时勾住「ADHD 人群」和「Agentic Harness 工程师」两端，
# 用好奇缺口 / 反直觉 / 身份认同 / 数字清单等社媒高传播框架包装同构脊柱。
# 占位符：{pain}=ADHD痛点  {parallel}=harness侧对应  {spine}=脊柱名
SPINE_VIRAL_HOOKS = [
    ("为什么「治好 ADHD 的{pain}」和「让 LLM 不跑飞」其实是同一道工程题？",
     "{parallel}——同一套 harness 思路，两边都成立。", "反直觉同构"),
    ("你的 ADHD 大脑，其实就是一个没装 harness 的大语言模型",
     "{spine}：{pain} ↔ {parallel}。", "身份认同"),
    ("Agent 工程师每天在解决的问题，ADHD 大脑已经面对了一辈子",
     "把「{parallel}」翻译成 ADHD 的{pain}解法。", "跨界顿悟"),
    ("如果把 ADHD 当成一个需要调试的 agent，会发生什么？",
     "用 {spine} 这条脊柱，把{pain}当成可工程化的问题。", "思想实验"),
    ("ADHD 不是缺陷，是缺了一层 orchestration——和 GPT 一样",
     "{spine}：生成核心没问题，缺的是调度层（{parallel}）。", "去污名化"),
    ("3 个 LLM 工程概念，彻底重写了我对 ADHD {pain}的理解",
     "{parallel} 如何反向照亮 ADHD 的{pain}。", "数字清单"),
    ("ADHD 圈和 AI agent 圈，正在偷偷解决同一个问题",
     "{spine} 把两群人连到了一起：{pain} ↔ {parallel}。", "社群桥接"),
    ("停止「管理」你的 ADHD，开始给它「套 harness」",
     "{parallel} 给{pain}的一份可迁移蓝图。", "行动召唤"),
]

# 工具级双受众钩子（带 {tool}）
TOOL_VIRAL_HOOKS = [
    ("{tool} 之于 ADHD，就像 {mirror} 之于 LLM——但有人用错了",
     "从同构视角实测 {tool}：它到底补上了哪一层执行功能？", "工具×同构"),
    ("我把 {tool} 当作 ADHD 大脑的「外部 harness」用了 30 天",
     "{tool} 解决{pain}的真实收益与「拐杖化」代价。", "亲历实测"),
    ("用 {tool} 给 ADHD 补上{spine}，是脚手架还是拐杖？",
     "{tool} 接进 ADHD 工作流：哪些交给它、哪些必须自己留着。", "权衡评测"),
]


def _category_meta() -> dict[str, dict]:
    return {
        c.id: {
            "category_name": c.name,
            "category_name_en": c.name_en,
            "category_icon": c.icon,
            "category_color": c.color,
            "keywords": c.keywords,
        }
        for c in CATEGORIES
    }


def _spine_meta() -> dict[str, dict]:
    return {c["name"]: c for c in SPINE_CONCEPTS}


def generate_problem_pool() -> list[dict]:
    """生成问题驱动的选题池（每条都带 spine 同构脊柱标注 + 双域提示）"""
    cat_meta = _category_meta()
    spine_meta = _spine_meta()
    pool: list[dict] = []
    seen: set[str] = set()

    def add(title, subtitle, angle, category_id, spine, pain, parallel):
        if title in seen:
            return
        seen.add(title)
        meta = cat_meta.get(category_id, {})
        sm = spine_meta.get(spine, {})
        pool.append({
            "id": f"prob-{len(pool):04d}",
            "category_id": category_id,
            "category_name": meta.get("category_name", ""),
            "category_name_en": meta.get("category_name_en", ""),
            "category_icon": meta.get("category_icon", ""),
            "category_color": meta.get("category_color", ""),
            "keywords": meta.get("keywords", []),
            "title": title,
            "subtitle": subtitle,
            "angle": angle,
            "problem": title,
            "spine": spine,
            "spine_kind": sm.get("kind", "bridge"),
            "spine_mirror": sm.get("mirror", parallel),
            "adhd_pain": pain,
            "harness_parallel": parallel,
            "is_problem_driven": True,
        })

    # 1. 脊柱锚定的核心问题（高质量、人工策划）
    for spec in SPINE_PROBLEM_SPECS:
        for q in spec["questions"]:
            add(
                title=q,
                subtitle=f"ADHD 侧：{spec['pain']}；LLM/harness 侧：{spec['parallel']}。用双域证据作答。",
                angle="同构问答",
                category_id=spec["category_id"],
                spine=spec["spine"],
                pain=spec["pain"],
                parallel=spec["parallel"],
            )

    def fill(tmpl, spec, tool=""):
        return tmpl.format(
            pain=spec["pain"], parallel=spec["parallel"],
            mirror=spec.get("mirror", spec["parallel"]),
            spine=spec["spine"], layer=spec["spine"], tool=tool,
        )

    # 2. 病毒级双受众脊柱钩子（社媒高传播框架包装同构）
    for spec in SPINE_PROBLEM_SPECS:
        for t, s, ang in SPINE_VIRAL_HOOKS:
            add(fill(t, spec), fill(s, spec), ang,
                spec["category_id"], spec["spine"], spec["pain"], spec["parallel"])

    # 3. 工具 × 脊柱扩展（遍历全部工具 × 多套钩子/模板，扩到数千条）
    all_tool_names = list(KNOWN_TOOLS.keys())
    for spec in SPINE_PROBLEM_SPECS:
        cat = spec["category_id"]
        for tool in all_tool_names:
            for t, s, ang in TOOL_VIRAL_HOOKS:
                add(fill(t, spec, tool), fill(s, spec, tool), ang,
                    cat, spec["spine"], spec["pain"], spec["parallel"])
            for tmpl_title, tmpl_sub in TOOL_PROBLEM_TEMPLATES:
                title = tmpl_title.format(tool=tool, layer=spec["spine"], pain=spec["pain"])
                subtitle = tmpl_sub.format(tool=tool)
                add(title, subtitle, "工具×同构",
                    cat, spec["spine"], spec["pain"], spec["parallel"])

    # 4. 受众 × 脊柱：把同一同构问题落到不同人群的真实场景
    for spec in SPINE_PROBLEM_SPECS:
        for audience, scene in AUDIENCE_FRAMES:
            add(
                f"{audience}如何用「给生成核心套 harness」的思路应对{scene}里的{spec['pain']}？",
                f"把 LLM 工程里的「{spec['parallel']}」迁移到{audience}的{scene}场景，双域证据作答。",
                "人群×同构", spec["category_id"], spec["spine"],
                spec["pain"], spec["parallel"],
            )
            # 受众 × 病毒钩子（带受众前缀，进一步扩池且保持独特）
            for t, s, ang in SPINE_VIRAL_HOOKS[:5]:
                add(f"{audience}视角：" + fill(t, spec), fill(s, spec),
                    "人群×同构", spec["category_id"], spec["spine"],
                    spec["pain"], spec["parallel"])

    return pool


if __name__ == "__main__":
    p = generate_problem_pool()
    print(f"问题驱动选题池：{len(p)} 条")
    from collections import Counter
    print("按脊柱：", Counter(x["spine"] for x in p))
    print("按分类：", Counter(x["category_id"] for x in p))
    for x in p[:5]:
        print("-", x["title"])
