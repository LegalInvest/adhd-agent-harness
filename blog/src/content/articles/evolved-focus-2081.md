---
title: "为什么用 Claude 治 ADHD 的注意力涣散，和给 agent 套 上下文工程 是一回事？"
subtitle: "Claude 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
description: "Claude 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
date: "2025-05-15"
category: "专注力管理"
categoryId: "focus"
categoryEn: "Focus Management"
tags:
  - "ADHD"
  - "AI"
  - "专注力管理"
  - "反直觉同构"
  - "深度工作"
readingTime: 10
slug: "为什么用-claude-治-adhd-的注意力涣散和给-agent-套-上下文工程-是一回事"
topicId: "evolved-focus-2081"
angle: "反直觉同构"
rank: 179
score: 7.75
sourceCount: 6
toolsCited:
  - "Brain.fm"
  - "Focusmate"
  - "RescueTime"
thesis: "ADHD 大脑与 LLM 是同一类「高产但缺执行调度层的生成核心」，两者都需要上下文工程作为外部脚手架来补偿调度缺陷，而非依赖拐杖。"
problem: "为什么用 Claude 治 ADHD 的注意力涣散，和给 agent 套 上下文工程 是一回事？"
spine: "上下文工程"
spineKind: ""
isEvolved: true
llmGenerated: true
caseStudies:
  - "曾国藩"
  - "李白"
  - "Samantha Jones"
---
# 为什么用 Claude 治 ADHD 的注意力涣散，和给 agent 套 上下文工程 是一回事？

> Claude 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。

如果你是一名 ADHD 患者，你一定熟悉这种体验：脑子里同时跑着十几个想法，每个都精彩绝伦，但就是无法落地。如果你是一名在做 Agentic Harness 的工程师，你同样熟悉这种体验：LLM 能写出惊艳的代码片段，但一放到复杂任务中就幻觉频出、跑偏失焦。

这两个群体看似毫无交集，却共享同一个底层困境：**我们拥有一个强大的生成核心，却缺少一个可靠的内置执行调度层。** ADHD 大脑和 LLM 在结构上同构——两者都是高产出、低控制的“引擎”，需要外部脚手架来弥补调度缺陷。这就是为什么用 Claude 治 ADHD 的注意力涣散，和给 agent 套上下文工程，本质上是同一件事。

## 从“无状态”到“上下文工程”

ADHD 的工作记忆缺陷，与 LLM 的“无跨会话状态”是同一个问题：两者都无法可靠地记住“刚才发生了什么”。ADHD 患者常因忘记任务上下文而中断工作（来源：AI 与 ADHD 的专注力）；LLM 则会在长对话中因上下文膨胀而推理退化（来源：同上）。

解法也同构：**主动设计“当下注意什么”的工程化方案。** 对 ADHD 来说，这可能是用 RescueTime 自动追踪时间，让“时间到底去了哪里”变得可见（来源：RescueTime）；对 LLM 来说，这是通过上下文传递、规划工件和记忆系统来约束注意力范围（来源：幻觉与验证循环）。

**我的核心判断是：** 无论是人还是模型，注意力都不是意志力问题，而是工程问题。上下文工程不是锦上添花，而是生成核心能运行的先决条件。

## 真实人物的 Harness 系统

曾国藩是 ADHD 自我管理的经典案例。他 30 岁前“浮躁坐不住”，日记里天天骂自己“无恒”“浮躁”，读书“不能终一行”。他的解法是“日课十二条”：黎明即起、读书不二、谨言、写日记反省……用最笨最稳的方法抵消冲动（来源：人物案例）。这本质上是一套**外部调度系统**——用固定的时间块、行为模板和每日复盘，补偿内生的执行功能缺陷。

与 LLM 的 harness 工程对照：曾国藩的“日课”相当于 agent 的**定时 re-grounding 机制**，每天重新校准方向；他的“写日记反省”相当于 agent 的**验证循环**，将内部状态与外部现实核对（来源：幻觉与验证循环）。两者都是主动设计的上下文工程，而非依赖意志力。

## 工具生态：外部执行功能层

现有工具正在构建这个“外部执行功能层”。Brain.fm 通过神经锁相技术生成专注音乐，帮助 ADHD 用户进入状态（来源：Brain.fm）；Focusmate 通过虚拟身体在场提供实时问责，弥补启动困难（来源：Focusmate）。这些工具的共同逻辑是：**用外部结构补偿内部缺陷。** 对于 LLM agent，同样的逻辑体现为确定性工作流、工具契约和状态机，用以稳定输出（来源：采样温度与表现波动）。

但必须诚实指出：这些工具的证据大多来自用户报告或小样本研究，缺乏大规模随机对照试验（来源：AI 与 ADHD 的专注力）。同构性本身也只是功能类比，并非神经科学上的实证（来源：矛盾与存疑）。

## 脚手架，不是拐杖

最关键的争议在于：外部脚手架会不会变成永久拐杖？曾国藩的“日课”伴随了他一生，你很难说他最终“内化”了执行功能——他只是把脚手架焊在了生活里。同样，LLM agent 如果永远依赖外部验证循环，是否意味着它从未真正“学会”自我纠错？

我的观点是：**脚手架和拐杖的边界在于是否可拆卸。** 如果移除工具后系统崩溃，那就是拐杖；如果工具只是加速了本就可能的路径，那就是脚手架。对 ADHD 来说，这意味着逐步减少对工具的依赖；对 agent 来说，这意味着在训练中融入自我校验能力。但目前两者都缺乏长期追踪研究（来源：AI 与 ADHD 的专注力）。

## 今天就能试的 3 件事

1. **ADHD 侧：** 打开 RescueTime 或类似工具，先追踪 3 天，不做任何改变，只是观察“时间到底去了哪里”。这是最基础的上下文工程。
2. **LLM 侧：** 下次用 Claude 写复杂文档时，主动给它一个“验证步骤”，比如“请先列出大纲，然后逐段检查是否有事实错误”。这就是 agent 的验证循环。
3. **通用：** 尝试 Focusmate 一次，找一个虚拟伙伴一起工作 25 分钟。你可能会发现，外部在场本身就是最强大的调度器。

ADHD 和 LLM 的困境不是缺陷，而是设计特征。当我们停止责怪自己“不够专注”，开始像工程师一样设计上下文，两个世界的问题就变成了同一个答案。

## 参考来源

- [ADHD Apps: We tested 44 Apps and Here're the Best 9 in 2026](https://blog.saner.ai/best-adhd-apps/) — 证据等级：低（GRADE）
- [Meta-Analysis of fMRI Studies of Disruptive Behavior Disorders](https://doi.org/10.1176/appi.ajp.2016.15081089) — 证据等级：高（GRADE）
- [Nonlinear Complexity Analysis of Brain fMRI Signals in Schizophrenia](https://doi.org/10.1371/journal.pone.0095146) — 证据等级：低（GRADE）
- [Revolutionizing ADHD Management with AI Assistants](https://neurolaunch.com/adhd-ai-assistant/) — 证据等级：低（GRADE）
- [Confabulation: The Surprising Value of Large Language Model Hallucinations](https://preview.aclanthology.org/navbar-space/2024.acl-long.770.pdf) — 证据等级：低（GRADE）
- [LBD同构对：分心与走神 — Therapeutic Doses of Oral Methylphenidate Significantly Incr ↔ AutoHallusion: Automatic Generation of Hallucination Benchma](https://doi.org/10.1523/jneurosci.21-02-j0001.2001) — 证据等级：低（GRADE）

---

*本文是「ADHD × AI」系列的第 179 篇，由 AI 智能体从持续维护的 LLM Wiki（全网真实情报）中取材整合生成，并持续迭代更新。*
