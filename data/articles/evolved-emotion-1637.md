---
title: "为什么用 Tiimo 治 ADHD 的情绪失调，和给 agent 套 会褪去的脚手架 是一回事？"
subtitle: "Tiimo 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
description: "Tiimo 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
date: "2025-04-18"
category: "情绪调节"
categoryId: "emotion"
categoryEn: "Emotional Regulation"
tags:
  - "ADHD"
  - "AI"
  - "情绪调节"
  - "反直觉同构"
  - "压力管理"
readingTime: 11
slug: "为什么用-tiimo-治-adhd-的情绪失调和给-agent-套-会褪去的脚手架-是一回事"
topicId: "evolved-emotion-1637"
angle: "反直觉同构"
rank: 390
score: 7.65
sourceCount: 6
toolsCited:
  - "Tiimo"
  - "Inflow"
  - "Goblin Tools"
  - "Saner.AI"
  - "Focusmate"
thesis: "ADHD 情绪失调与 LLM agent 目标漂移共享同一结构缺陷：强大的生成核心缺乏可靠的执行调度层；Tiimo 和会褪去的脚手架都是通过外部重锚定系统补偿这一缺陷，且必须设计为可撤除的临时支撑，否则沦为拐杖。"
problem: "为什么用 Tiimo 治 ADHD 的情绪失调，和给 agent 套 会褪去的脚手架 是一回事？"
spine: "拐杖与脚手架"
spineKind: ""
isEvolved: true
llmGenerated: true
---
# 为什么用 Tiimo 治 ADHD 的情绪失调，和给 agent 套 会褪去的脚手架 是一回事？

> Tiimo 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。

## 问题：情绪不是失控，是调度层掉了

你是否有过这样的体验：明明计划好要写一份报告，打开电脑后却刷了半小时手机，然后陷入自责和焦虑，最终什么也没做。对 ADHD 人群来说，这并非意志力薄弱，而是大脑的执行调度层——负责任务启动、工作记忆和时间感知的系统——在关键时刻失灵了。情绪失调往往不是情绪本身的问题，而是调度层崩溃后的连锁反应：任务启动失败 → 自责 → 焦虑 → 更无法启动，形成恶性循环。

与此同时，在 AI 工程领域，LLM agent 也面临类似的困境。一个强大的语言模型可以写出优美的代码，但在长程任务中，它可能逐渐忘记初始指令，陷入无限循环，或者输出与目标无关的内容。工程师们发现，问题不在于模型的能力，而在于它缺乏一个可靠的执行调度层来保持方向。

这两个看似无关的问题，实际上共享同一个核心结构：**高产但缺乏执行调度层的生成核心**。ADHD 大脑和 LLM 都是强大的生成器，但都容易在任务执行中发生目标漂移——注意力被无关刺激捕获，或者过度聚焦细节而忽略整体。情绪失调，正是这种目标漂移在情感层面的表现。

## 同构答案：外部重锚定系统

解决这一问题的思路在两边惊人地一致：**提供一个外部重锚定系统，定期将注意力拉回原任务**。

### ADHD 侧：Tiimo 和它的同类

Tiimo 是一款专门为 ADHD 人群设计的视觉计时器和日程管理工具。它通过可视化时间块和倒计时，帮助用户感知时间流逝，对抗时间盲（来源：Tiimo 官方描述）。但更关键的是，它充当了一个重锚定系统：当用户开始走神或陷入情绪漩涡时，Tiimo 的提醒和视觉反馈将注意力拉回当前任务。

类似的工具还有 Inflow，它通过训练工作记忆和认知控制来改善执行功能（来源：Inflow 页面）。Goblin Tools 的 Magic ToDo 功能将复杂任务分解为小步骤，降低启动门槛（来源：Goblin Tools 页面）。Saner.AI 则通过知识回忆减少搜索循环和标签切换（来源：Saner.AI 页面）。这些工具的共同点是：它们都在提供一个外部执行功能层，补偿 ADHD 大脑缺失的调度能力。

### LLM/agent 侧：会褪去的脚手架

在 LLM agent 工程中，工程师们构建了所谓的“harness”或“脚手架”——一个围绕模型的架构，包含护栏、事件驱动的系统提醒、人在回路监督等。例如，当 agent 在长程任务中开始忘记系统提示时，harness 会通过定期注入上下文或触发检查点来重锚定模型的行为（来源：重锚定与目标漂移页面）。这种脚手架的设计原则是：它必须足够强大以引导模型，但又不能永久依赖——最终目标是让模型学会自我维持方向。

这正是“会褪去的脚手架”的含义：一个临时的外部支撑，随着内在能力的提升逐步撤除。

## 核心判断：脚手架 vs 拐杖的边界

这里必须做出一个关键区分：**脚手架和拐杖不是一回事**。

脚手架是临时支撑，设计目标是在使用者能力增强后撤除；拐杖则是永久替代，长期使用会导致依赖和内在能力萎缩。当前多数 ADHD 工具（如 Goblin Tools、Saner.AI）被设计为长期使用，未提及撤除机制（来源：矛盾与存疑页面）。这引发了一个争议：它们究竟是脚手架还是拐杖？

我的判断是：**Tiimo 这类工具如果只作为外部提醒，它可能是拐杖；但如果结合训练和工作记忆改善（如 Inflow 的神经可塑性训练），它就有潜力成为脚手架**。关键在于工具的设计是否包含“逐步撤除”的机制。目前，几乎没有 ADHD 工具明确提供撤除路径，这是一个重要的局限（来源：矛盾与存疑页面）。

同样，LLM agent 的 harness 也需要考虑褪去。如果 harness 永远不撤，agent 就无法在无监督环境下自主运行。一些前沿实践已经开始尝试动态降低护栏强度，但这仍是开放问题。

## 证据与局限

### 证据

- **工作记忆**：Inflow 基于背外侧前额叶皮层作为因果流入中枢的研究，其功能连接性与工作记忆表现正相关（来源：Inflow 页面）。
- **任务启动**：Goblin Tools 被评价为“将压倒性的事情变成一系列不压倒性的事情”（来源：Goblin Tools 页面）。
- **时间盲**：Tiimo 的视觉计时器提供实时时间反馈。
- **身体在场**：Focusmate 通过虚拟身体搭档提供外部问责，绕过执行功能屏障（来源：人在回路与身体在场页面）。
- **LLM 侧**：Harness 通过事件驱动的系统提醒对抗指令消退（来源：重锚定与目标漂移页面）。

### 局限

1. **证据强度不足**：多数 ADHD 工具缺乏独立随机对照试验，证据主要来自用户评价和概念对齐（来源：矛盾与存疑页面）。
2. **多巴胺干预争议**：基于多巴胺的 AI 干预（如奖励系统）可能强化依赖而非内在动机（来源：矛盾与存疑页面）。
3. **长期效果未知**：AI 对情绪调节的长期神经可塑性影响未明（来源：AI 与 ADHD 情绪调节页面）。
4. **个性化不足**：现有工具多基于通用认知模型，对共病焦虑等个体差异覆盖有限（来源：同上）。

## 今天就能试的行动

1. **设置定时重锚定**：用 Tiimo 或手机闹钟，每 25 分钟提醒自己“当前目标是什么”，对抗目标漂移。
2. **分解一个压倒性任务**：用 Goblin Tools 的 Magic ToDo 将一个让你焦虑的任务分解为 5 个小步骤，每完成一个就划掉。
3. **引入虚拟身体搭档**：尝试 Focusmate 或找一个朋友视频连线，各自做自己的事，利用身体在场效应启动任务。
4. **为你的 AI agent 加一个检查点**：如果你在写代码或使用 LLM，每 10 轮交互后让模型总结当前进度和下一步目标，模拟 harness 的重锚定。

## 参考来源

- [Dynamic causal brain circuits during working memory and their functional controllability](https://doi.org/10.1038/s41467-021-23509-x)
- [Best AI Tools for ADHD Productivity in 2026 (Honest Review) - Iwo Szapar](https://www.iwoszapar.com/p/best-ai-tools-adhd-productivity-2026)
- [AI Tools for ADHD: Boosting Productivity and Reducing Burnout](https://www.vktr.com/ai-platforms/ai-tools-for-adhd-boosting-productivity-and-reducing-burnout/)
- [The Best AI-Powered ADHD Productivity Tools in 2026 (That ...](https://nexasphere.io/blog/ai-adhd-productivity-tools-2026)
- [“A Cognitive Collaborator:” How Adults with ADHD Are Using ChatGPT](https://www.additudemag.com/how-to-use-chatgpt-executive-function-adhd/?srsltid=AfmBOoq-REuSO0UJC656kbLBAd5u3CDNmGeVNrZ79iouVqrFlN919a39)
- [Harnessing Artificial Intelligence to Live Better with ADHD - CHADD](https://chadd.org/attention-article/harnessing-artificial-intelligence-to-live-better-with-adhd/)

---

*本文是「ADHD × AI」系列的第 390 篇，由 AI 智能体从持续维护的 LLM Wiki（全网真实情报）中取材整合生成，并持续迭代更新。*
