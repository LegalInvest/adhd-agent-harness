---
title: "两个互不引用的领域都在研究「注意调度」——ADHD 文献和 LLM harness 文献为什么得出了同一个结论？"
subtitle: "Swanson 文献发现：622 篇 ADHD 论文 ↔ 35 篇 harness 论文共享机制「attention allocation」，双域代表作对照解读。"
description: "Swanson 文献发现：622 篇 ADHD 论文 ↔ 35 篇 harness 论文共享机制「attention allocation」，双域代表作对照解读。"
date: "2025-05-18"
category: "专注力管理"
categoryId: "focus"
categoryEn: "Focus Management"
tags:
  - "ADHD"
  - "AI"
  - "专注力管理"
  - "LBD同构发现"
  - "分心管理"
readingTime: 11
slug: "两个互不引用的领域都在研究注意调度adhd-文献和-llm-harness-文献为什么得出了同一个结论"
topicId: "prob-55ca9bac1b"
angle: "LBD同构发现"
rank: 263
score: 7.65
sourceCount: 6
toolsCited:
  - "RescueTime"
  - "Focusmate"
  - "Brain.fm"
  - "Forest"
  - "Endel"
thesis: "ADHD 大脑与 LLM 都是‘高产但缺乏可靠执行调度层’的生成核心，因此都必须靠外部 harness/脚手架进行上下文工程，才能主动分配注意力、把潜能转化为目标导向行为。"
problem: "两个互不引用的领域都在研究「注意调度」——ADHD 文献和 LLM harness 文献为什么得出了同一个结论？"
spine: "上下文工程"
spineKind: "llm"
isEvolved: false
llmGenerated: true
isoStrength: "A"
caseStudies:
  - "曾国藩"
  - "曹植"
  - "王秀英"
---
# 两个互不引用的领域都在研究「注意调度」——ADHD 文献和 LLM harness 文献为什么得出了同一个结论？

> Swanson 文献发现：622 篇 ADHD 论文 ↔ 35 篇 harness 论文共享机制「attention allocation」，双域代表作对照解读。

为什么你刚坐下写报告，手机一亮、窗外一响、念头一闪就跑了？为什么 LLM 的上下文窗口一膨胀，回答就开始跑题、重复、甚至“幻觉”？这看起来是两个世界的问题，但两边在解决的根本难题是同一个：**注意力到底该分配到哪**。

## 一、同一个结论：注意力必须被“工程化”调度

ADHD 文献和 LLM/agent 文献很少互相引用，却殊途同归地指向一个机制：attention allocation（注意分配）。ADHD 侧的核心困境是，大脑拥有极高的发散、联想与创意产出，但**执行功能**这个“驾驶座”常常无人驾驶——计划、组织、工作记忆、冲动控制都不可靠（来源：AI Tools for ADHD: Boosting Productivity and Reducing Burnout）。LLM/agent 侧的核心困境是，模型本身是强大的生成核心，却没有可靠的内置执行调度层，直接输出可能偏离目标、循环或失控（来源：Building an AI Agent Harness from Scratch: The Architecture Between LLM and Agent - DEV Community）。

因此，两边得出的结论都是：**必须从外部设计“此刻该注意什么”的机制**。对 ADHD 这叫环境设计与执行功能支架；对 LLM 这叫上下文工程（context engineering）与 agent harness。

## 二、ADHD 侧的证据：生成核心缺调度层

ADHD 的执行功能缺陷不是“不想专注”，而是“无法可靠地调度注意”。工作记忆被公认为关键瓶颈：信息在脑中保不住，操作难以连续完成（来源：6 ways AI can help you manage ADHD symptoms - Understood.org）。于是注意力被环境线索“带偏”——一个新通知、一个更有趣的念头、一个身体烦躁，都能重新分配掉本已有限的认知资源。

ADHD 群体最常用的外部解法之一，是**身体在场（body doubling）**：有他人在场时，启动困难与维持困难被显著绕过（来源：Using an AI Assistant to Manage ADHD: A Practical Guide）。Focusmate 用算法匹配虚拟伙伴，实现“AI-Matched Body Doubling”，让社会问责和外部可见性替代内部多巴胺调节（来源：The Best AI-Powered ADHD Productivity Tools in 2026 (That ...)）。RescueTime 则自动记录时间、分类活动、阻断分心网站，直接补偿 ADHD 的“时间盲”与工作记忆负担（来源：Revolutionizing ADHD Management with AI Assistants）。Brain.fm 和 Endel 用 AI 生成声音环境，Forest 用游戏化番茄钟，这些工具共同构成一个外部执行功能层——不是让大脑“更努力”，而是给大脑一个更窄、更稳的上下文（来源：AI 与 ADHD 的专注力）。

## 三、LLM/agent 侧的证据：上下文窗口就是它的“注意环境”

LLM 的“注意力”同样不是意志问题，而是机制问题。最新研究发现，在经典 Stroop 冲突任务中，Transformer 的注意力会随着序列变长，在冲突试次上骤降到随机水平——这正是“无法抑制优势反应、无法解决认知冲突”的表现，与 ADHD 执行功能缺陷的标志一一对应（来源：Deficient Executive Control in Transformer Attention）。另一项研究更直接地刻画出 LLM 的“强记忆、弱控制”剖面：工作记忆容量甚至超过常人，但认知灵活性与注意控制存在核心缺陷，无法灵活切换任务集、无法抑制自动化反应（来源：Strong Memory, Weak Control: An Empirical Study of Executive Functioning in LLMs）。还有研究显示，Transformer 在工作记忆任务中自发发展出输入—输出门控机制，这模仿的正是人类前额叶—纹状体回路——而这套回路正是 ADHD 核心受损的系统（来源：TRANSFORMER MEC...）。

工程上，LLM 的 harness 做的就是 ADHD 工具在做的事：从外部约束注意分配。通过设置 token 预算、工具调用次数上限、防止无限循环、加入人工检查点（pause-and-ask），harness 把“生成核心”套进一个可监督的执行层（来源：Building an AI Agent Harness from Scratch: The Architecture Between LLM and Agent - DEV Community）。这和人用 Focusmate、RescueTime 给自己加“外部驾驶座”是同一种结构。

## 四、案例：曾国藩的“日课十二条”就是一套 19 世纪的 harness

晚清曾国藩常被评“半个圣人”，但年轻时的他与 ADHD 的注意力不集中型高度吻合：坐不住，天天串门、喝酒、看热闹；读书极慢，“他人目下二三行，余或疾读不能终一行”；情绪不稳，打败仗就跳水；终身严重银屑病。他的解法不是“让自己变得更自律”，而是**给自己设计一套外部调度系统**：日课十二条——黎明即起、读书不二、谨言、写日记反省；打仗“结硬寨、打呆仗”，用最笨最稳的方法抵消冲动；一辈子写日记骂自己，以外部文本持续重新定位当下的注意目标。

这正对应 LLM harness 的三种组件：
- **“黎明即起、读书不二”** ↔ 定时 re-grounding / 系统提示词的周期性重新注入，让模型回到初始任务目标；
- **“结硬寨、打呆仗”** ↔ 硬性约束（token 上限、工具调用次数上限），用慢而稳的策略避免冲动式跳跃；
- **“写日记反省”** ↔ 外部日志与遥测，把状态外化，让“驾驶座”能基于记录而非当下的情绪做调度。

曾国藩的“生成核心”并不低——他创办了洋务运动、平定太平天国、家书传世。但如果没有这套 harness，他的高产能只会继续被冲动和分心消耗。这正是 ADHD 与 LLM 共同的结构：高产不是目的，**可靠的目标导向行为才是**。

## 五、脚手架 vs. 拐杖：边界在哪里？

关键区分不在“用不用外部工具”，而在**工具是否帮助内部能力逐步内化**。脚手架是临时的、可撤除的、能帮人学会自己搭结构；拐杖是永久的、让人依赖的、撤掉后能力反而更差。AI 工具对 ADHD 用户可能既是脚手架，也可能变成拐杖，目前长期追踪研究几乎空白（来源：AI 与 ADHD 的专注力）。对 LLM 来说，如果 harness 只是无限增加护栏而不让模型学会更稳定的策略，那它也只是把风险后移，并没有解决调度层缺陷。

诚实的边界是：
- 同构是**功能类比**，不是已被验证的神经机制同一性（来源：矛盾与存疑）；
- Brain.fm、Endel 等工具在 ADHD 人群中的独立临床证据有限，效果多来自间接推论或小样本（来源：AI 与 ADHD 的专注力）；
- Focusmate 的虚拟身体在场能否替代真实人际互动，仍有争议（来源：矛盾与存疑）；
- ADHD 本身有高度异质性，同一工具对注意缺陷型和多动冲动型可能效果迥异。

## 六、今天就能试的四条行动

1. **给任务加一个“上下文锚点”**：用 Forest 或一个简单的可见计时器，把“现在只做这一件”变成环境线索；给 LLM 写一段固定系统提示词，明确角色、目标、输出格式与禁区。
2. **让注意力的去向“可被审计”**：用 RescueTime 或手写 15 分钟时间日志，看看真正吃掉注意力的不是“大问题”，而是哪些小触发；对应到 LLM，就是在 harness 里加遥测，记录模型在哪里偏离了任务链。
3. **加入一个“人在回路”检查点**：ADHD 侧可找一个伙伴用 Focusmate 或定期报告进度；LLM 侧在关键工具调用前设置“暂停并询问”节点，而不是让模型自动链式执行（来源：Building an AI Agent Harness from Scratch: The Architecture Between LLM and Agent - DEV Community）。
4. **先搭脚手架，再判断是否该撤除**：选定一个支持系统，两周后回头问：我是因为这个工具更能完成任务，还是因为离开它我就更糟？前者是脚手架，后者正在变成拐杖。

ADHD 与 LLM 不会互相解释彼此，但它们在“注意调度”这个问题上分享了同一个工程直觉：**一个高产的生成核心，需要被设计过的上下文托住，才能把散乱的可能性收敛成可靠的结果**。

## 参考来源

**同构强度：A 级** —— 直接文献支撑（引用 ADHD↔LLM 同构专题研究）

- [ADHD Apps: We tested 44 Apps and Here're the Best 9 in 2026](https://blog.saner.ai/best-adhd-apps/) — 证据等级：低（GRADE）
- [Meta-Analysis of fMRI Studies of Disruptive Behavior Disorders](https://doi.org/10.1176/appi.ajp.2016.15081089) — 证据等级：高（GRADE）
- [Nonlinear Complexity Analysis of Brain fMRI Signals in Schizophrenia](https://doi.org/10.1371/journal.pone.0095146) — 证据等级：低（GRADE）
- [Revolutionizing ADHD Management with AI Assistants](https://neurolaunch.com/adhd-ai-assistant/) — 证据等级：低（GRADE）
- [Toward Neurodivergent-Aware Productivity: A Systems and AI-Based Human-in-the-Loop Framework for ADHD-Affected Professionals](https://arxiv.org/pdf/2507.06864) — 证据等级：低（GRADE）
- [Using an AI Assistant to Manage ADHD: A Practical Guide](https://www.lobsterfarm.ai/guides/ai-for-adhd/) — 证据等级：低（GRADE）

---

*本文是「ADHD × AI」系列的第 115 篇，由 AI 智能体从持续维护的 LLM Wiki（全网真实情报）中取材整合生成，并持续迭代更新。*
