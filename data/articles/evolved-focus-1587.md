---
title: "为什么用 Goblin Tools 治 ADHD 的注意力涣散，和给 agent 套 上下文工程 是一回事？"
subtitle: "Goblin Tools 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
description: "Goblin Tools 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
date: "2025-04-06"
category: "专注力管理"
categoryId: "focus"
categoryEn: "Focus Management"
tags:
  - "ADHD"
  - "AI"
  - "专注力管理"
  - "反直觉同构"
  - "注意力"
readingTime: 11
slug: "为什么用-goblin-tools-治-adhd-的注意力涣散和给-agent-套-上下文工程-是一回事"
topicId: "evolved-focus-1587"
angle: "反直觉同构"
rank: 286
score: 7.68
sourceCount: 6
toolsCited:
  - "Goblin Tools"
  - "Brain.fm"
  - "Focusmate"
  - "RescueTime"
  - "Forest"
thesis: "ADHD 大脑与 LLM 在结构上同构——都是高产但缺执行调度层的生成核心——因此 Goblin Tools 等 AI 工具通过上下文工程提供外部脚手架，同时解决了注意力涣散和 agent 不可靠问题。"
problem: "为什么用 Goblin Tools 治 ADHD 的注意力涣散，和给 agent 套 上下文工程 是一回事？"
spine: "上下文工程"
spineKind: ""
isEvolved: true
llmGenerated: true
---
# 为什么用 Goblin Tools 治 ADHD 的注意力涣散，和给 agent 套 上下文工程 是一回事？

> Goblin Tools 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。

你打开一个空白文档，脑子里的想法像爆米花一样炸开，但手指就是敲不下去。另一边，你调试的 LLM agent 每次输出都跑偏，明明指令写得很清楚，它却像没听见一样。这两个场景，一个属于 ADHD 患者，一个属于 AI 工程师，但它们的病根是同一个：**一个高产但缺调度层的生成核心，碰上了没有上下文的执行环境**。

这个反直觉的同构，就是本文要拆解的核心。

## 问题：注意力涣散与 agent 不可靠，是同一类故障

ADHD 的注意力涣散，本质是执行功能障碍（Executive Dysfunction）。不是不想专注，而是大脑的「调度层」——负责计划、启动、抑制控制、时间管理的系统——效率低下（来源：执行功能障碍）。你有一个强大的生成核心（思维、创意、联想），但缺乏可靠的执行调度，所以任务启动困难、容易漂移、时间盲。

LLM/agent 的不可靠，本质是上下文溢出和调度失败。模型本身是强大的生成核心，但如果不给它清晰的上下文框架（角色、目标、约束、记忆），它就会自由联想、跑题、遗忘指令。工程师做上下文工程，就是在给这个生成核心套 harness——定义边界、注入记忆、编排步骤。

**所以，ADHD 的注意力涣散，和 agent 的不可靠，是同一类故障：生成核心缺少执行调度层。**

## 答案：上下文工程就是那个 harness

Goblin Tools 是 ADHD 社区里口碑很好的 AI 工具。它把一个大任务（比如「写一篇周报」）自动分解成可执行的小步骤，并估算每个步骤的时间。这本质上就是**上下文工程**：把模糊的目标转化成结构化的上下文，让生成核心（你的大脑）知道该做什么、按什么顺序、花多少时间。

同样的思路，工程师在做 agent 编排时，会把用户 query 拆成子任务、注入历史记忆、设置输出格式约束——这就是在给 LLM 套 harness。

证据在哪？看几个工具：

- **Brain.fm** 用 AI 生成神经锁相音乐，主动维持大脑的注意力连贯性（来源：Brain.fm）。这相当于给大脑注入一个「专注上下文」，防止环境干扰导致上下文溢出。
- **Focusmate** 通过 AI 匹配虚拟同伴，提供实时问责（来源：Focusmate）。这相当于给 agent 加了一个「监督者角色」，在每一步检查进度，防止漂移。
- **RescueTime** 自动记录时间使用，充当外部记忆（来源：RescueTime）。这解决了 ADHD 的「时间盲」和 LLM 的「无状态性」——两者都需要外部记忆来补偿。
- **Forest** 用游戏化奖励维持专注，本质是给大脑一个「多巴胺上下文」，激励它留在任务轨道上。

这些工具的共同点：**它们不是替代你的大脑或模型，而是为生成核心提供外部脚手架（scaffolding），补偿缺失的调度层。**

## 核心观点：脚手架 vs 拐杖，边界在哪？

我的判断是：**上下文工程的本质不是让生成核心变强，而是让执行环境变清晰。** 好的脚手架应该像训练轮——帮助你在骑行中建立平衡感，最终可以撤除。但当前多数工具（包括 Goblin Tools）设计为长期使用，没有撤除机制（来源：矛盾与存疑）。这就有变成「拐杖」的风险：过度依赖外部结构，可能阻碍内在执行功能的发展。

神经可塑性的研究告诉我们，大脑可以通过训练重塑（来源：神经可塑性）。但问题是：这些工具是否真的在训练执行功能，还是仅仅在补偿？目前没有长期研究证明脚手架可以逐步撤除（来源：矛盾与存疑）。

所以，我的观点是：**工具应该设计为「可渐撤的脚手架」，而不是永久拐杖。** 比如 Goblin Tools 可以增加一个「逐步减少分解粒度」的模式，让用户逐渐自己承担调度任务。

## 争议与局限

必须诚实指出：

1. **证据缺口**：多数工具缺乏针对 ADHD 的独立临床研究（来源：矛盾与存疑）。Brain.fm 的神经锁相技术理论上有效，但无 RCT 支持。Focusmate 的效果归因于身体在场，而非 AI 本身。
2. **个体差异**：ADHD 亚型对工具反应不同（来源：矛盾与存疑）。注意力缺陷型可能更需要外部记忆，多动冲动型可能更需要抑制控制工具。
3. **多巴胺争议**：游戏化奖励是否真正改善专注，证据矛盾（来源：矛盾与存疑）。

## 今天就能试的行动

1. **用 Goblin Tools 分解一个你拖延的任务**：把「整理房间」拆成「收拾桌面→叠衣服→扫地→倒垃圾」，每个步骤估时。你会在执行中感到阻力骤减。
2. **给你的 agent 写一个「角色+约束+步骤」的 system prompt**：明确告诉它「你是客服，回复不超过 100 字，先确认问题再回答」。你会发现输出质量提升。
3. **尝试一次 Focusmate 时段**：预约 25 分钟，和陌生人对坐工作。你会体验到「外部调度层」的力量。
4. **反思你的工具依赖**：问自己——如果明天所有工具消失，我能独立完成这个任务吗？如果不能，试着降低一个层级的辅助。

ADHD 大脑和 LLM 不是需要修复的残次品。它们是高产的生成核心，只是缺一个 harness。上下文工程，就是那个 harness。

## 参考来源

- [11 Best ADHD Productivity Apps for Fluctuating Energy - rivva blog](https://blog.rivva.app/p/11-best-adhd-productivity-apps-for)
- [Meta-Analysis of fMRI Studies of Disruptive Behavior Disorders](https://doi.org/10.1176/appi.ajp.2016.15081089)
- [Nonlinear Complexity Analysis of Brain fMRI Signals in Schizophrenia](https://doi.org/10.1371/journal.pone.0095146)
- [The Best AI-Powered ADHD Productivity Tools in 2026 (That ...](https://nexasphere.io/blog/ai-adhd-productivity-tools-2026)
- [AI Tools for Kids with ADHD: A Complete Guide for Parents...](https://www.kidsaitools.com/en/articles/ai-tools-kids-adhd-complete-guide-2026)
- [AI Tools for ADHD: Boosting Productivity and Reducing Burnout](https://www.vktr.com/ai-platforms/ai-tools-for-adhd-boosting-productivity-and-reducing-burnout/)

---

*本文是「ADHD × AI」系列的第 286 篇，由 AI 智能体从持续维护的 LLM Wiki（全网真实情报）中取材整合生成，并持续迭代更新。*
