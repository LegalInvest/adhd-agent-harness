---
title: "为什么用 Perplexity 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用 是一回事？"
subtitle: "Perplexity 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
description: "Perplexity 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
date: "2025-05-14"
category: "AI工具实战"
categoryId: "ai-tools"
categoryEn: "AI Tools in Practice"
tags:
  - "ADHD"
  - "AI"
  - "AI工具实战"
  - "反直觉同构"
  - "智能助手"
readingTime: 13
slug: "为什么用-perplexity-治-adhd-的任务启动困难和给-agent-套-function-calling-工具调用-是一回事"
topicId: "evolved-ai-tools-1585"
angle: "反直觉同构"
rank: 183
score: 7.72
sourceCount: 6
toolsCited:
  - "Perplexity"
  - "Goblin Tools"
  - "Saner.AI"
  - "Lex"
  - "Focusmate"
thesis: "ADHD大脑与LLM/agent共享‘高产但缺执行调度层’的同构缺陷，因此为ADHD设计的工具（如Perplexity）与为agent设计的function calling harness本质上是同一套外部执行功能层——通过脚手架补偿内在调度缺陷，而非替代核心生成能力。"
problem: "为什么用 Perplexity 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用 是一回事？"
spine: "工具使用与认知卸载"
spineKind: ""
isEvolved: true
llmGenerated: true
---
# 为什么用 Perplexity 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用 是一回事？

> Perplexity 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。

## 同一个问题，两个世界

你有没有过这样的时刻：明明知道该做什么，但就是“启动不了”？任务拆解到最小步骤了，大脑却像卡壳的引擎，怎么都点不着火。与此同时，在AI工程领域，另一群人也在为同样的困境头疼：他们精心训练的LLM agent，在长程任务中会“忘记”系统提示，偏离初始目标，甚至陷入死循环。

这两群人——ADHD患者与Agentic Harness工程师——看似毫无关联，实则面对的是同一个核心问题：**一个高产但缺乏可靠执行调度层的生成核心**。ADHD大脑与LLM在结构上惊人同构：两者都能产生丰富的想法和输出，但都欠缺一个稳定的“执行层”来启动、跟踪和完成目标（来源：ADHD的AI工具全景）。

## 同构的痛点：任务启动困难 vs 冷启动问题

ADHD侧的任务启动困难，本质是执行功能缺陷——大脑的“调度器”无法将意图转化为行动。LLM侧对应的则是“冷启动”问题：模型在初始状态缺乏足够的上下文和指令来可靠地执行复杂任务。

Perplexity这类AI工具之所以能帮助ADHD用户，不是因为它有多“聪明”，而是因为它充当了外部执行功能层：将模糊的“研究一下X”分解为搜索、摘要、对比等具体步骤，并提供即时反馈。这与给LLM agent套上function calling harness是同一种思路——harness通过定义工具集、设置护栏、加入人工检查点，将模型的生成能力约束在可控范围内（来源：人在回路与身体在场）。

## 证据：两边都成立

### ADHD侧的真实证据

- **Goblin Tools**的Magic ToDo功能自动将“整理房间”拆解为“捡起衣服、擦桌子”等小步骤，用户报告称启动焦虑显著降低（来源：Goblin Tools）。
- **Lex**通过单一指令触发多步骤执行，减少决策疲劳，直接针对任务启动困难（来源：Lex）。
- **Saner.AI**通过增强知识回忆，减少搜索循环和标签切换，补偿工作记忆不足（来源：Saner.AI）。
- **Focusmate**等虚拟身体搭档提供外部问责，绕过执行功能屏障（来源：人在回路与身体在场）。

### LLM/agent侧的真实证据

- Agent harness通过**事件驱动的系统提醒**对抗“指令消退”，即模型在长程任务中忘记系统提示的问题（来源：重锚定与目标漂移）。
- Harness集成MCP工具、遥测、代码仓库等，并引入human-in-the-loop监督，设置token预算、工具调用次数上限等护栏（来源：人在回路与身体在场）。
- 核心原则是“形式化规划与护栏，使代理输出真正有用且正确”（来源：人在回路与身体在场）。

## 脚手架 vs 拐杖：关键的边界

同构视角揭示了一个重要辩证关系：AI工具应作为**脚手架**促进能力发展，而非永久**拐杖**。ADHD侧，过度依赖Goblin Tools可能削弱内在的任务分解能力；LLM侧，过度依赖harness的护栏可能让模型失去自主调整的灵活性（来源：矛盾与存疑）。

真正的脚手架，是让用户在使用过程中逐步内化那些外部结构。例如，Goblin Tools的分解步骤可以成为用户大脑中的“默认思维模式”，而harness的检查点可以训练模型在无监督时也主动验证输出。关键在于：工具的设计意图是“补偿”还是“替代”？补偿是暂时的，替代是永久的。

## 局限与诚实警告

必须承认，目前所有证据主要来自用户报告和概念类比，缺乏大规模随机对照试验（来源：矛盾与存疑）。个体差异极大——对某些ADHD用户有效的工具，对另一些人可能毫无作用。同样，harness工程中，不同的模型和任务需要不同的护栏配置，没有万能方案。

此外，存在过度依赖的风险：用户可能逐渐丧失主动记忆和规划的能力，模型可能因过度约束而失去创造性（来源：矛盾与存疑）。工具设计者声称是“脚手架”，但实际使用中可能沦为“拐杖”。

## 今天就能试的行动

1. **用Perplexity启动一个“可怕”的任务**：比如写一份报告。输入“帮我分解写报告的任务，列出前5步”，然后只做第一步。
2. **给自己设计一个“harness”**：在开始任何项目前，写下不超过3个关键规则（例如“每25分钟检查一次目标”“完成后才能切换任务”），像agent的护栏一样约束自己。
3. **尝试Goblin Tools的Magic ToDo**：输入一个让你拖延的任务，观察AI如何分解它，然后执行第一步。
4. **对于工程师**：在agent代码中显式加入“重锚定”逻辑——每N步将原始系统提示重新注入上下文，就像ADHD用户设置定时提醒一样。

## 结语

Perplexity治ADHD的任务启动困难，和给agent套function calling harness，本质上是同一件事：为强大的生成核心提供一个可靠的外部执行调度层。理解这一点，你就能从两类人的经验中互相借鉴——ADHD用户可以从harness工程中学到“护栏”的重要性，工程师则可以从ADHD策略中学到“分解与反馈”的精细度。

这不是类比，而是同构。

## 参考来源

- [Best AI Tools for ADHD Productivity in 2026 (Honest Review) - Iwo Szapar](https://www.iwoszapar.com/p/best-ai-tools-adhd-productivity-2026)
- [AI Tools for ADHD: Boosting Productivity and Reducing Burnout](https://www.vktr.com/ai-platforms/ai-tools-for-adhd-boosting-productivity-and-reducing-burnout/)
- [The Best AI-Powered ADHD Productivity Tools in 2026 (That ...](https://nexasphere.io/blog/ai-adhd-productivity-tools-2026)
- [“A Cognitive Collaborator:” How Adults with ADHD Are Using ChatGPT](https://www.additudemag.com/how-to-use-chatgpt-executive-function-adhd/?srsltid=AfmBOoq-REuSO0UJC656kbLBAd5u3CDNmGeVNrZ79iouVqrFlN919a39)
- [Harnessing Artificial Intelligence to Live Better with ADHD - CHADD](https://chadd.org/attention-article/harnessing-artificial-intelligence-to-live-better-with-adhd/)
- [AI Tools for Kids with ADHD: A Complete Guide for Parents...](https://www.kidsaitools.com/en/articles/ai-tools-kids-adhd-complete-guide-2026)

---

*本文是「ADHD × AI」系列的第 183 篇，由 AI 智能体从持续维护的 LLM Wiki（全网真实情报）中取材整合生成，并持续迭代更新。*
