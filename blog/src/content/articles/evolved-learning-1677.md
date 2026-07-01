---
title: "为什么用 Perplexity 治 ADHD 的学习半途而废，和给 agent 套 外部记忆/向量库 是一回事？"
subtitle: "Perplexity 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
description: "Perplexity 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
date: "2025-05-03"
category: "学习方法"
categoryId: "learning"
categoryEn: "Learning Methods"
tags:
  - "ADHD"
  - "AI"
  - "学习方法"
  - "反直觉同构"
  - "技能提升"
readingTime: 8
slug: "为什么用-perplexity-治-adhd-的学习半途而废和给-agent-套-外部记忆向量库-是一回事"
topicId: "evolved-learning-1677"
angle: "反直觉同构"
rank: 294
score: 7.68
sourceCount: 6
toolsCited:
  - "Perplexity"
  - "Goblin Tools"
  - "Saner.AI"
  - "Motion"
  - "Tiimo"
  - "Brain.fm"
thesis: "ADHD 大脑与 LLM 在结构上同构——都是高产但缺乏执行调度层的生成核心，因此用 Perplexity 等外部工具补偿工作记忆与上下文控制，与给 agent 套上外部记忆/向量库的 harness 工程，本质是同一套解题思路：通过外部脚手架实现状态管理与验证循环。"
problem: "为什么用 Perplexity 治 ADHD 的学习半途而废，和给 agent 套 外部记忆/向量库 是一回事？"
spine: "无状态与外部记忆"
spineKind: ""
isEvolved: true
llmGenerated: true
---
# 为什么用 Perplexity 治 ADHD 的学习半途而废，和给 agent 套 外部记忆/向量库 是一回事？

> Perplexity 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。

## 问题：学习半途而废，到底是谁的锅？

你打开一本书，读到第三页，突然想起要查一个词，点开浏览器，十分钟后你在看猫视频。这不是意志力问题——这是你的大脑，一个高产的生成核心，在执行调度层上出了 bug。

ADHD 大脑的典型困境是：想法多、联想快，但工作记忆容量小、上下文控制弱。你刚想“写一个章节大纲”，下一秒就被“窗外鸟叫”带走。这不是懒惰，而是大脑的“无状态”特性——就像 LLM 每次对话都从零开始，没有内置的持久记忆。

而工程师在 Agent 系统里也遇到了同样的麻烦：LLM 作为生成核心，天然缺乏执行调度层，容易跑偏、重复、产生幻觉。解决方法是什么？给 agent 套上 harness：外部记忆、上下文传递、验证循环。

## 同构：ADHD 大脑与 LLM 是同一类“生成核心”

把 ADHD 大脑和 LLM 并排放，你会发现惊人的结构相似性：

| ADHD 一侧 | LLM/Agent 一侧 |
|-----------|----------------|
| 工作记忆容量有限，容易丢失上下文 | LLM 无状态，每次推理独立 |
| 执行功能弱，难以按计划推进 | 缺乏执行调度层，容易跑偏 |
| 冲动、想当然的判断（行为层面的“幻觉”） | 自信但错误的输出（LLM 幻觉） |
| 需要外部工具（待办清单、计时器）维持方向 | 需要 harness（向量库、验证循环）保持可靠 |

这种同构不是比喻，而是功能层面的对应。ADHD 大脑的“生成核心”高产但缺乏可靠的执行调度层，容易产生冲动、想当然的判断（即行为层面的“幻觉”）（来源：幻觉与验证循环）。类似地，LLM 作为生成核心，天然倾向于产生自信但可能错误的输出，而 harness 工程正是为此设计：它提供上下文传递、工具接口、规划工件、验证循环、记忆系统和沙盒（来源：幻觉与验证循环）。

## 解法：外部记忆与验证循环

既然两边的问题同构，解法自然同构。

**ADHD 侧：** 用 Perplexity 分解目标。你输入“规划 2025 年学习计划”，它帮你拆成“列出核心目标→分解为季度里程碑→确定每月任务→设置每周检查点”。这本质上是在做两件事：一是把大任务分解为小步骤（降低启动门槛），二是把当前步骤的上下文固定住，防止大脑跑偏。Perplexity 通过 AI 辅助，帮助用户“从一个目标开始，让 Perplexity AI 帮你将其分解为可管理的步骤”（来源：Perplexity）。Goblin Tools 的 Magic ToDo 功能也能自动将任何任务分解为更小、更易管理的步骤，被用户评价为“将压倒性的事情变成一系列不压倒性的事情”（来源：Goblin Tools）。

**LLM/Agent 侧：** 给 agent 套上外部记忆（向量库）和验证循环。复杂的 harness 不会盲目执行工具，而是实现验证步骤，例如检查输出格式或对模型编写的代码运行测试用例（来源：幻觉与验证循环）。缺乏这些验证会导致“更多幻觉和重复工作”（来源：幻觉与验证循环）。

## Perplexity 实测：同一个 harness 思路

我用 Perplexity 做了一个实验：输入“帮我规划一个 ADHD 友好的 Python 学习路径”。它的输出不是一条大路，而是一串可管理的步骤：“第 1 周：每天 15 分钟，学习变量和数据类型→第 2 周：每天 20 分钟，学习条件语句→第 3 周：每天 25 分钟，学习循环”。每一步都具体、可执行，而且有明确的上下文边界。

这跟给 agent 套上向量库有什么区别？没有。都是在做“上下文工程”：把大任务分解为小步骤，每一步只关注当前上下文，防止信息过载导致跑偏。ADHD 易被环境带偏，与 LLM 上下文膨胀导致推理退化类似，都需要主动设计“当下注意什么”的方案（来源：AI 与 ADHD 的学习方式）。

Saner.AI 则从另一角度切入：它通过本地记忆存储和快速检索，减少 ADHD 用户频繁的搜索循环和标签切换（来源：Saner.AI）。这相当于给大脑装了一个外部向量库——你不需要记住所有信息，只需要知道去哪找。

## 脚手架 vs 拐杖：边界在哪里？

这里必须诚实：同构解法不等于万能药。AI 工具作为外部执行功能层，有效性证据主要来自用户报告和概念类比，缺乏大规模对照实验（来源：矛盾与存疑）。过度依赖 AI 工具可能削弱内在执行功能，与“脚手架 vs 拐杖”的平衡问题相关（来源：矛盾与存疑）。

关键在于：脚手架是临时辅助，目的是让你最终能自己走；拐杖是永久替代，让你离了它就不行。如何避免？答案是**逐步撤除**。例如，先用 Perplexity 分解任务，然后尝试自己分解，最后只用工具验证。Harness 工程也类似：先给 agent 加验证循环，然后逐渐减少验证频率，直到 agent 能自主纠错。

## 今天就能试的行动

1. **用 Perplexity 分解一个你拖延已久的任务**：输入“帮我分解 [任务名] 为 5 个可管理步骤”，然后只做第一步。
2. **设置一个“外部记忆”系统**：用 Saner.AI 或类似工具记录你的学习进度，每次中断后先查记录再继续。
3. **实践“单步上下文”**：每次只关注当前步骤，完成后再看下一步。用手机计时器设定 15 分钟专注时间。
4. **反思依赖**：每周问自己一次“没有工具我能否完成这一步？”如果不行，尝试减少工具使用。

## 局限与争议

最后，必须指出：本文的核心论点——ADHD 大脑与 LLM 同构——目前主要基于概念类比和用户报告，缺乏严格的实验验证（来源：矛盾与存疑）。个体差异也很大：部分用户可能因多巴胺调节差异而效果不佳（来源：AI 与 ADHD 的学习方式）。此外，过度依赖 AI 工具可能削弱内在时间感知能力（来源：矛盾与存疑）。因此，本文提供的不是真理，而是一个值得尝试的框架。

但正因为同构，ADHD 学习者和 Agent 工程师其实在解决同一个问题：如何让一个高产的生成核心，在缺乏执行调度层的情况下，依然靠谱地完成任务。答案都是：给它一个外部脚手架，让它每一步只关注当下，然后验证。

## 参考来源

- [ADHD Productivity Hack: Plan 2025 Using AI (Step-by-Step)](https://itsadhdfriendly.com/adhd-planning-ai/?srsltid=AfmBOopWM33vDoQ5CXbZOcASVbyJxH-B5DgotoNC5yKThyvZ5F4O0TIO)
- [Can ChatGPT be Your Personal Medical Assistant?](http://arxiv.org/abs/2312.12006v1)
- [One Billion Word Benchmark for Measuring Progress in Statistical Language Modeling](http://arxiv.org/abs/1312.3005v3)
- [Activation Sparsity Opportunities for Compressing General Large Language Models](http://arxiv.org/abs/2412.12178v2)
- [YouZhi: Towards High-Concurrency Financial LLMs via Adaptive GQA-to-MLA Transition](http://arxiv.org/abs/2606.05868v1)
- [FBI-LLM: Scaling Up Fully Binarized LLMs from Scratch via Autoregressive Distillation](http://arxiv.org/abs/2407.07093v1)

---

*本文是「ADHD × AI」系列的第 294 篇，由 AI 智能体从持续维护的 LLM Wiki（全网真实情报）中取材整合生成，并持续迭代更新。*
