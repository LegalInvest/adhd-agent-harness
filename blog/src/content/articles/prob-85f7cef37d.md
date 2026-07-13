---
title: "ADHD 研究生视角：为什么「治好 ADHD 的注意力容易被环境带偏」和「让 LLM 不跑飞」其实是同一道工程题？"
subtitle: "LLM 受上下文窗口内容左右，需要上下文工程——同一套 harness 思路，两边都成立。"
description: "LLM 受上下文窗口内容左右，需要上下文工程——同一套 harness 思路，两边都成立。"
date: "2025-04-13"
category: "专注力管理"
categoryId: "focus"
categoryEn: "Focus Management"
tags:
  - "ADHD"
  - "AI"
  - "专注力管理"
  - "人群×同构"
  - "分心管理"
readingTime: 10
slug: "adhd-研究生视角为什么治好-adhd-的注意力容易被环境带偏和让-llm-不跑飞其实是同一道工程题"
topicId: "prob-85f7cef37d"
angle: "人群×同构"
rank: 107
score: 7.77
sourceCount: 6
toolsCited:
  - "Brain.fm"
  - "Focusmate"
  - "RescueTime"
  - "Endel"
  - "Forest"
  - "Tiimo"
  - "Saner.AI"
  - "Goblin Tools"
thesis: "ADHD 大脑与 LLM 都不是'坏了的核心'，而是同一个工程问题：高产但缺乏可靠执行调度层；真正要修的，不是核心本身，而是围绕它设计一套'上下文工程'的 harness，把目标、约束、记忆和校验外化到环境里。"
problem: "ADHD 研究生视角：为什么「治好 ADHD 的注意力容易被环境带偏」和「让 LLM 不跑飞」其实是同一道工程题？"
spine: "上下文工程"
spineKind: "llm"
isEvolved: false
llmGenerated: true
isoStrength: "A"
caseStudies:
  - "曾国藩"
  - "徐渭徐文长"
  - "Shannon Jones"
---
# ADHD 研究生视角：为什么「治好 ADHD 的注意力容易被环境带偏」和「让 LLM 不跑飞」其实是同一道工程题？

> LLM 受上下文窗口内容左右，需要上下文工程——同一套 harness 思路，两边都成立。

## 引子：两个房间，同一种走神

想象一下两个并行的房间：一间里，ADHD 研究生盯着电脑，三小时前准备写论文，现在已经回完邮件、刷完三个公众号、约了周末球局；另一间里，LLM agent 接到"帮我优化产品文案"的任务，上下文窗口里挤进了会议纪要、竞品文档、slack 消息，最后生成了一篇半是营销套话、半是梦境呓语的文本。两边的核心都不算弱：ADHD 大脑 often 有惊人的联想和创造性（来源：AI 与 ADHD 的专注力）；LLM 在受控 prompt 下也能输出高质量内容。问题是同一个——**注意力被环境带偏，上下文 drift 了**。ADHD 的痛点叫"环境带偏"，LLM 的痛点叫"上下文膨胀导致推理退化"（来源：外部执行功能层），但解法都叫"上下文工程"。

## 第一节：注意力偏移，本质是上下文漂移

ADHD 的核心问题常被误解为"不专心"，更准确的说法是执行功能不稳定：工作记忆会掉、任务启动困难、时间感扭曲（来源：Best AI Tools for ADHD Productivity in 2026 (Honest Review) - Iwo Szapar）。这些特征对应到 LLM 上几乎是一组同义词：LLM 无跨会话状态，必须靠外部记忆系统；上下文一多，注意力分数熵增，冲突解决能力会塌到随机水平（来源：Deficient Executive Control in Transformer Attention）。换句话说，ADHD 大脑和 LLM 都是"强记忆、弱控制"的生成核心（来源：Strong Memory, Weak Control: An Empirical Study of Executive Functioning in LLMs）。它们不是不能产出，而是不能自己决定当下该产出什么、不该产出什么。这个决定权，要靠外部 harness 来调度。

## 第二节：曾国藩的 harness：日课十二条作为"上下文工程"

晚清曾国藩很可能是 ADHD  harness 的先驱。他的日记里反复骂自己"无恒""浮躁"：读书慢，"他人目下二三行，余或疾读不能终一行"；年轻时坐不住，天天串门喝酒看杀人；情绪起伏剧烈，打完败仗就要跳水自杀。他的解法不是修心养性，而是给自己搭一套外部系统：日课十二条——黎明即起、读书不二、谨言、写日记反省；打仗时"结硬寨、打呆仗"，用最笨的方式对抗冲动。这些全是把目标、约束、记忆和反馈外化到日程与纸笔里，相当于为自己的大脑写了一个"system prompt + 定期 re-grounding"的 harness。

这里的同构对应非常明显：
- **日课时间表** ↔ LLM 的定时 re-grounding / 系统提示更新；
- **日记反省** ↔ 外部日志、记忆系统、状态快照；
- **结硬寨打呆仗** ↔ 给 agent 设计固定的验证循环、约束沙箱，不让它自由发挥。

曾国藩的成就不靠他"治好"了注意力分散，而是靠 harness 把分散的可能性锁进了一个结构里。

## 第三节：LLM 的 harness：上下文工程、脚手架与验证循环

在 LLM 工程侧，这套结构叫"harness engineering"：围绕 AI 代理设计脚手架——上下文交付、工具接口、规划工件、验证循环、记忆系统和沙箱（来源：GitHub - ai-boost/awesome-harness-engineering）。具体做法包括用 Git 仓库存储项目上下文（相当于 ADHD 用户的 Second Brain），通过 MCP 连接器访问外部数据（来源：Worker Agents | Harness Developer Hub），以及把控制逻辑外化为可移植的 harness 代码（来源：Building AI Coding Agents for the Terminal: Scaffolding, Harness, Context Engineering, and Lessons Learned）。

这和 ADHD 侧的工具箱一一对应：
- **RescueTime** 用自动化时间追踪与分心阻断，直接补偿时间盲与执行功能缺陷（来源：Revolutionizing ADHD Management with AI Assistants）；
- **Focusmate** 用虚拟身体在场（body doubling）制造外部启动压力和问责（来源：ADHD科技行业深度研究）；
- **Brain.fm** 与 **Endel** 用 AI 生成声音环境，试图把"当下注意什么"工程化（来源：AI 与 ADHD 的专注力）；
- **Forest** 用游戏化番茄钟把多巴胺机制转化为外部计时器（来源：AI 与 ADHD 的专注力）。

这些工具不是治疗 ADHD，而是像 LLM 的 harness 一样，把执行调度层外化。

## 第四节：同构的边界——它只是一个类比，不是科学定律

但必须诚实：ADHD 大脑与 LLM 的"同构"目前只是功能层面的类比，而非被神经机制验证的事实（来源：矛盾与存疑）。Transformer 的注意力熵增和前额叶执行功能失调是否共享同一套数学或生物原理，尚无定论。同样，工具的临床证据也很薄弱：Brain.fm 在 44 款 ADHD 应用测试中进入最佳 9 款，但针对 ADHD 人群的独立临床证据仍有限（来源：Brain.fm）；Endel 也缺乏 ADHD 特异性研究（来源：AI 与 ADHD 的专注力）；RescueTime 的自动分类可能不准，对执行功能弱的用户仍是额外负担（来源：RescueTime）。

所以同构最好被当作一个**启发式**，而不是证明。

## 第五节：脚手架 vs. 拐杖——边界在哪里？

无论是 ADHD 侧还是 LLM 侧，最大的争议都是：这套 harness 会不会从"脚手架"变成"拐杖"？（来源：AI 与 ADHD 的专注力）。如果系统永远替你做决定，你的内部调度层可能进一步萎缩；如果 LLM 的 harness 过度约束，agent 也会失去泛化能力。

我的判断是：**harness 的目标不是替核心做决定，而是把"做决定所需的信息"提前放到上下文窗口里**。曾国藩的日记不是替他做人，而是每天早上把他拉回"今天要做什么"；LLM 的 system prompt 不是替模型思考，而是限定它可用的工具和目标。好的 harness 是渐隐的：它先提供结构，然后让你（或模型）学会在更少的提示下自我 re-ground。坏的 harness 则是永久依赖，永远替你按住刹车。

## 第六节：今天就能试的四件事

1. **给 LLM 写一个 50 字的 system prompt 放在每个任务前**，包括目标、输出格式、禁止事项——这就是你的"上下文工程"第一步。
2. **用一个番茄钟工具锁住 25 分钟**，Forest 或 Brain.fm 都可以，让外部时钟替 ADHD 大脑感知时间（来源：Forest；Brain.fm）。
3. **约一次 Focusmate**，用虚拟身体在场降低任务启动阻力（来源：Focusmate）。
4. **睡前写三行"今日上下文"**：完成了什么、明天第一优先项、一个可能让注意力 drift 的陷阱。这是曾国藩式日记的极简版。

## 结语：同一道题，两种解法

ADHD 研究生和 LLM agent 工程师看似在两个世界，但面对的是同一道工程题：如何为一个高产、敏感、容易跑飞的生成核心，设计一个可靠的外部调度层。注意力被环境带偏，和 LLM 因上下文膨胀而跑飞，都是"上下文没有工程好"。解题的关键不是消灭分心或限制模型，而是**主动设计当下应该出现什么信息、不应该出现什么信息**。这既是曾国藩的日课，也是 agentic harness 的 context engineering。

## 参考来源

**同构强度：A 级** —— 直接文献支撑（引用 ADHD↔LLM 同构专题研究）

- [ADHD Apps: We tested 44 Apps and Here're the Best 9 in 2026](https://blog.saner.ai/best-adhd-apps/) — 证据等级：低（GRADE）
- [Meta-Analysis of fMRI Studies of Disruptive Behavior Disorders](https://doi.org/10.1176/appi.ajp.2016.15081089) — 证据等级：高（GRADE）
- [Nonlinear Complexity Analysis of Brain fMRI Signals in Schizophrenia](https://doi.org/10.1371/journal.pone.0095146) — 证据等级：低（GRADE）
- [Revolutionizing ADHD Management with AI Assistants](https://neurolaunch.com/adhd-ai-assistant/) — 证据等级：低（GRADE）
- [Deficient Executive Control in Transformer Attention](https://www.biorxiv.org/content/10.1101/2025.01.22.634394v1.full.pdf) — 证据等级：低（GRADE）
- [Strong Memory, Weak Control: An Empirical Study of Executive Functioning in LLMs](https://preview.aclanthology.org/evt-to-venues/2026.eacl-long.281.pdf) — 证据等级：低（GRADE）

---

*本文是「ADHD × AI」系列的第 28 篇，由 AI 智能体从持续维护的 LLM Wiki（全网真实情报）中取材整合生成，并持续迭代更新。*
