---
title: "为什么用 Todoist 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用 是一回事？"
subtitle: "Todoist 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
description: "Todoist 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
date: "2025-04-20"
category: "AI工具实战"
categoryId: "ai-tools"
categoryEn: "AI Tools in Practice"
tags:
  - "ADHD"
  - "AI"
  - "AI工具实战"
  - "反直觉同构"
  - "ADHD辅助"
readingTime: 7
slug: "为什么用-todoist-治-adhd-的任务启动困难和给-agent-套-function-calling-工具调用-是一回事"
topicId: "evolved-ai-tools-1579"
angle: "反直觉同构"
rank: 381
score: 7.65
sourceCount: 6
toolsCited:
  - "Todoist"
  - "Goblin Tools"
  - "Saner.AI"
  - "Lex"
  - "Claude"
  - "Otter.ai"
thesis: "ADHD 的任务启动困难与 LLM 的冷启动问题本质相同，都是生成核心缺乏执行调度层；Todoist 和 function calling 工具调用作为外部 harness，通过分解任务、管理上下文、提供即时反馈，解决了同一类问题。"
problem: "为什么用 Todoist 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用 是一回事？"
spine: "工具使用与认知卸载"
spineKind: ""
isEvolved: true
llmGenerated: true
---
# 为什么用 Todoist 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用 是一回事？

> Todoist 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。

## 问题：为什么计划本和便签治不了“启动困难”？

如果你有 ADHD，你一定经历过这种时刻：大脑里有一堆想做的事，但身体就是动不了。你打开 Todoist，看着“写周报”这个任务，光标闪了十分钟，最后关掉窗口去刷手机。这不是懒，是执行功能（executive function）的失效——就像大脑的驾驶座上没有人（来源：AI Tools for ADHD: Boosting Productivity and Reducing Burnout）。

同样，如果你在做 Agentic Harness 工程，你一定见过这种场景：你给 LLM 一个复杂的任务，比如“帮我整理代码并提交 PR”，结果它要么开始长篇大论地解释步骤，要么跑题去写诗。这不是模型笨，是它缺乏一个可靠的执行调度层——LLM 本身是无状态、仅生成文本的核心（来源：Building AI Coding Agents for the Terminal: Scaffolding, Harness, Context Engineering, and Lessons Learned）。

两件事看起来毫不相关，但本质是同一个问题：**一个高产但缺调度层的生成核心，需要外部脚手架才能启动和执行。**

## 同构：ADHD 大脑 ≈ LLM，Todoist ≈ function calling

最新研究揭示了一个反直觉的发现：ADHD 患者的工作记忆容量可能正常甚至超常，但认知灵活性和注意控制存在核心缺陷，呈现“强记忆、弱控制”的认知剖面（来源：Strong Memory, Weak Control: An Empirical Study of Executive Functioning in LLMs）。这与 LLM 惊人相似——Transformer 自注意力机制在长上下文下冲突解决能力崩溃至随机水平（来源：Deficient Executive Control in Transformer Attention）。

换句话说，ADHD 大脑和 LLM 都是“生成核心”：它们能产出大量想法或文本，但缺乏内置的调度层来按顺序、按优先级执行。ADHD 的任务启动困难，对应 LLM 的“冷启动”问题；ADHD 的时间盲，对应 LLM 的时序推理弱点；ADHD 易被环境带偏，对应 LLM 的上下文膨胀（来源：ADHD 大脑与 LLM 的同构）。

那么，解决方案是什么？对 ADHD 来说，是外部执行功能层——比如 Todoist 配上 AI 的分解功能。对 LLM 来说，是 harness 工程——比如 function calling 工具调用。

**Todoist 的 AI 任务分解，本质上就是给 ADHD 大脑套了一个 function calling 的 harness。** 你输入“整理房间”，它自动拆成“捡衣服、擦桌子、叠被子”等小步骤。这就像给 LLM 定义了一个 `decompose_task()` 函数，把模糊意图转化为可执行的原子操作。Goblin Tools 的 Magic ToDo 功能做了同样的事：将压倒性的事情变成一系列不压倒性的事情（来源：The Best AI-Powered ADHD Productivity Tools in 2026 (That ...)）。用户报告称，这种分解能降低启动焦虑（来源：Goblin Tools）。

在 LLM 侧，现代 AI 代理通过“复合 AI 系统架构”来弥补调度缺陷，包括“工作负载专用模型路由、分离规划与执行的双代理架构、惰性工具发现、自适应上下文压缩”（来源：Building AI Coding Agents for the Terminal: Scaffolding, Harness, Context Engineering, and Lessons Learned）。这些技术本质上是在 LLM 外部搭建调度层，防止“上下文膨胀和推理退化”。

## 证据：两边都真实有效

### ADHD 侧的证据

- **Goblin Tools** 被用户评价为“简单有用”，能将复杂任务分解为小步骤（来源：Best AI Tools for ADHD Productivity in 2026 (Honest Review) - Iwo Szapar）。
- **Lex** 允许用户通过单一指令触发多步骤任务序列，减少决策疲劳（来源：Best AI Tools for ADHD Productivity in 2026 (Honest Review) - Iwo Szapar）。
- **Saner.AI** 通过本地记忆存储和快速检索，减少搜索循环和标签切换（来源：Best AI Tools for ADHD Productivity in 2026 (Honest Review) - Iwo Szapar）。
- **Claude** 和 **Otter.ai** 作为外部对话记忆，提供即时反馈，类似于“身体在场效应”的虚拟版本（来源：ADHD 的 AI 工具全景）。

### LLM/Agent 侧的证据

- Harness 工程被定义为“设计围绕 AI 代理的脚手架——上下文交付、工具接口、规划工件、验证循环、记忆系统和沙箱”（来源：GitHub - ai-boost/awesome-harness-engineering）。
- 具体实现包括用 Git 仓库存储项目上下文（类似 ADHD 侧的 Second Brain），通过 MCP 连接器访问外部数据（来源：Worker Agents | Harness Developer）。
- 实验证明，没有 harness 的 LLM 在长上下文下冲突解决能力崩溃（来源：Deficient Executive Control in Transformer Attention），而有了 harness 后，代理能可靠执行多步骤任务。

## 脚手架 vs 拐杖：边界在哪里？

这里有一个关键争议：AI 工具是促进能力发展的脚手架，还是削弱内在能力的拐杖？

资料中明确警告：过度依赖 AI 工具可能削弱内在时间感知能力（来源：时间盲），存在依赖风险（来源：任务启动）。Otter.ai 减轻笔记负担，但过度依赖可能削弱主动记笔记的能力（来源：ADHD 的 AI 工具全景）。同样，给 LLM 套上过度的 harness，也可能让模型失去自主推理的能力。

我的判断是：**脚手架与拐杖的区别在于，工具是否帮助用户/模型理解过程，而不仅仅是跳过过程。** Goblin Tools 的分解步骤是脚手架，因为它让用户看到任务的结构；而一个自动完成所有工作的“一键搞定”工具就是拐杖。对 LLM 来说，function calling 是脚手架，因为它让模型学会调用外部工具；而一个完全替代推理的硬编码流程就是拐杖。

## 局限与诚实

必须承认，目前证据主要来自用户报告和概念类比，缺乏大规模随机对照试验（来源：矛盾与存疑）。个体差异很大——有人觉得 Goblin Tools 好用，有人觉得它分得太细反而干扰（来源：任务启动）。此外，Brain.fm 的 ADHD 效果缺乏独立临床研究（来源：Brain.fm），Structured 的 AI 功能细节不明确（来源：Structured）。所以，别指望任何工具是灵丹妙药。

## 今天就能试的行动

1. **用 Todoist 或 Goblin Tools 分解一个你拖延已久的任务**：输入“整理书桌”，看 AI 拆出的步骤。如果它拆得太细，手动合并；如果太粗，手动拆分。记录启动时间的变化。
2. **给你的 LLM 项目加一个 function calling 接口**：哪怕只是一个 `search_web()` 函数，也能显著减少模型的冷启动问题。观察它在多步任务中的表现。
3. **对比两种工具的效果**：用 Lex 的单一指令触发多步骤，对比手动一步步执行。记录哪个更容易让你/模型完成。
4. **注意依赖风险**：每周至少一次，不用任何 AI 工具手动分解任务，保持内在能力。如果发现离开了工具完全无法启动，说明已经过度依赖。

最后，记住这个同构：**你需要的不是更强的意志力，而是更好的 harness。** 对 ADHD 大脑和对 LLM 都一样。

## 参考来源

- [Best AI Tools for ADHD Productivity in 2026 (Honest Review) - Iwo Szapar](https://www.iwoszapar.com/p/best-ai-tools-adhd-productivity-2026)
- [AI Tools for ADHD: Boosting Productivity and Reducing Burnout](https://www.vktr.com/ai-platforms/ai-tools-for-adhd-boosting-productivity-and-reducing-burnout/)
- [The Best AI-Powered ADHD Productivity Tools in 2026 (That ...](https://nexasphere.io/blog/ai-adhd-productivity-tools-2026)
- [“A Cognitive Collaborator:” How Adults with ADHD Are Using ChatGPT](https://www.additudemag.com/how-to-use-chatgpt-executive-function-adhd/?srsltid=AfmBOoq-REuSO0UJC656kbLBAd5u3CDNmGeVNrZ79iouVqrFlN919a39)
- [Harnessing Artificial Intelligence to Live Better with ADHD - CHADD](https://chadd.org/attention-article/harnessing-artificial-intelligence-to-live-better-with-adhd/)
- [AI Tools for Kids with ADHD: A Complete Guide for Parents...](https://www.kidsaitools.com/en/articles/ai-tools-kids-adhd-complete-guide-2026)

---

*本文是「ADHD × AI」系列的第 381 篇，由 AI 智能体从持续维护的 LLM Wiki（全网真实情报）中取材整合生成，并持续迭代更新。*
