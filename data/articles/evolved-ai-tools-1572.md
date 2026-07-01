---
title: "为什么用 Lex 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用 是一回事？"
subtitle: "Lex 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
description: "Lex 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
date: "2025-03-12"
category: "AI工具实战"
categoryId: "ai-tools"
categoryEn: "AI Tools in Practice"
tags:
  - "ADHD"
  - "AI"
  - "AI工具实战"
  - "反直觉同构"
  - "效率工具"
readingTime: 10
slug: "为什么用-lex-治-adhd-的任务启动困难和给-agent-套-function-calling-工具调用-是一回事"
topicId: "evolved-ai-tools-1572"
angle: "反直觉同构"
rank: 376
score: 7.65
sourceCount: 6
toolsCited:
  - "Lex"
  - "Goblin Tools"
  - "Saner.AI"
  - "Otter.ai"
  - "Reflect"
  - "Mem"
  - "Claude"
  - "ChatGPT"
thesis: "ADHD 的任务启动困难与 LLM agent 的 function calling 问题本质同构：两者都是“高产但缺执行调度层的生成核心”，需要外部 harness（脚手架）来补偿执行功能缺陷。Lex 通过单一指令触发多步骤流程，同时解决了 ADHD 的启动门槛和 agent 的工具调用协调问题，验证了同一套 harness 思路的双向有效性。"
problem: "为什么用 Lex 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用 是一回事？"
spine: "工具使用与认知卸载"
spineKind: ""
isEvolved: true
llmGenerated: true
---
# 为什么用 Lex 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用 是一回事？

> Lex 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。

## 从两个看似无关的痛点开始

如果你是一个 ADHD 患者，你可能熟悉这种感觉：脑子里有无数想法，但就是无法开始做第一件事。任务启动困难——像一堵无形的墙，让你在“应该做”和“做不了”之间反复摩擦。

如果你是一个在做 Agentic Harness 的工程师，你可能也熟悉另一种感觉：你的 LLM agent 推理能力很强，能写代码、能规划，但一遇到需要调用外部工具（function calling）就卡壳——要么顺序错乱，要么忘记传参，要么在多个 API 之间迷失。

这两个痛点，一个来自神经多样性人群，一个来自 AI 工程领域，表面毫无关联。但本文要论证一个反直觉的同构：**ADHD 大脑与 LLM agent 是同一类“高产但缺执行调度层的生成核心”，而 Lex 这类工具，恰好为两边提供了同一种解决方案——外部 harness（脚手架）。**

## 同构的底层逻辑：生成核心 vs 执行调度层

ADHD 大脑的核心特征是什么？不是缺乏想法，而是缺乏将想法转化为行动的执行调度能力。多巴胺系统功能低下导致动机和奖赏机制失调（来源：多巴胺），工作记忆容量虽大但控制弱（来源：工作记忆），任务启动困难本质上是“有生成能力，但缺启动脚本”。

LLM agent 的核心特征呢？同样，大模型本身是强大的生成核心，能写诗、能编程、能推理，但一旦需要调用外部工具（如搜索、计算、数据库查询），它就会暴露出“上下文控制缺陷”——容易忘记工具的存在、混淆工具顺序、或者被上下文膨胀带偏（来源：上下文工程）。

这两者的同构点在于：**它们都缺少一个内置的执行调度层**。ADHD 大脑的前额叶执行功能发育滞后或功能低下，LLM 的架构本身不包含工具调用的控制逻辑。因此，两边的解法思路一致：**通过外部系统（harness/脚手架）来补偿这个缺失的调度层。**

## Lex 的 harness 思路：一次指令，多步执行

Lex 的核心功能是允许用户通过单一指令触发复杂、多步骤的任务序列（来源：Lex）。对于 ADHD 用户，这意味着“启动门槛”被大幅降低——你不需要先想“第一步做什么，第二步做什么”，只需要说一句话，AI 帮你拆解并执行。这直接对应了 Goblin Tools 的“魔法开关”理念：将压倒性任务变成一系列不压倒性的步骤（来源：Goblin Tools）。

对于 LLM agent 工程师来说，Lex 做的事情本质上是 **function calling 的编排层**。通常，你需要为 agent 编写复杂的工具调用逻辑：定义工具列表、设定调用顺序、处理返回结果。Lex 相当于把这个编排逻辑内建了——你只需要定义一次“任务模板”，它就能自动完成工具协调。这就像给 agent 套了一个“执行 harness”，让它从“会推理但不会调用”变成“会推理且会调用”。

## 两边都有真实证据支撑

ADHD 侧：用户报告显示，Lex 的“单一指令触发多步骤”特性减少了决策疲劳，降低了启动焦虑（来源：Lex）。这与身体在场效应的原理一致——外部系统提供了隐性问责和即时反馈，绕过执行功能瓶颈（来源：身体在场效应）。Goblin Tools 的用户反馈也类似：“将压倒性的事情变成一系列不压倒性的事情”（来源：Goblin Tools）。

LLM/agent 侧：虽然 Lex 本身不是为 agent 设计的，但它的架构与 function calling 的 harness 设计完全同构。实际工程中，像 Claude 的对话式整理和 ChatGPT 的插件系统，都在尝试为 LLM 提供外部工具调用层（来源：Claude、ChatGPT）。这些工具的本质都是“为生成核心套上脚手架”，让 agent 能可靠地调用外部资源。

## 脚手架 vs 拐杖：一个必须指出的边界

这里有一个关键争议：AI 工具是脚手架还是拐杖？脚手架帮助能力发展，拐杖则替代能力。

对于 ADHD 用户，过度依赖 Lex 可能削弱内在的任务分解能力（来源：矛盾与存疑）。例如，Otter.ai 减轻笔记负担，但长期使用可能让用户不再主动记笔记（来源：拐杖与脚手架）。同样，对于 agent 工程师，如果完全依赖预制的 harness，可能失去对工具调用逻辑的深入理解。

但同构视角也给出了边界：**脚手架应该只补偿“执行调度层”，而不是替代“生成核心”**。ADHD 用户仍然需要自己产生想法和决策，只是启动过程被简化；agent 仍然需要自己推理和生成，只是工具调用被编排。Lex 的定位恰好落在这个边界上——它不替你思考，只替你执行。

## 今天就能试的行动

1. **如果你是 ADHD 用户**：试用 Lex 或 Goblin Tools 的 Magic ToDo 功能，把一个你拖延很久的任务（比如“整理邮件”）用一句话输入，观察 AI 分解后的步骤是否降低了启动门槛。
2. **如果你是 agent 工程师**：在你的 LLM 应用中实现一个简单的 function calling 编排层——定义一个任务模板，让模型通过单一指令触发多个工具调用（例如“搜索并总结某话题”）。对比有无编排层的执行成功率。
3. **两边都试试**：将 Lex 的“任务模板”思路迁移到你的 agent 设计——为常见任务预定义多步流程，减少每次的决策成本。
4. **警惕依赖**：每周至少一次不使用工具，手动分解任务，保持内在能力不被削弱。

## 结语

Lex 的价值不在于它是一个“ADHD 工具”或“AI 工具”，而在于它揭示了一个更深层的同构：**无论是人类大脑还是大模型，当生成能力过剩而执行调度不足时，解法都是同一个——外部 harness。** 这个视角不仅让 ADHD 患者看到自己的困难不是缺陷，而是架构特点；也让 AI 工程师看到，function calling 的问题不是模型不够强，而是缺少一层脚手架。

当然，目前的证据仍以用户报告为主，缺乏大规模对照研究（来源：矛盾与存疑）。个体差异也很大——不是每个 ADHD 用户都适合 Lex，也不是每个 agent 都需要复杂的编排层。但至少，这个同构提供了一个新的设计思路：与其让生成核心变得更“聪明”，不如给它一个可靠的外部调度层。

## 参考来源

- [Best AI Tools for ADHD Productivity in 2026 (Honest Review) - Iwo Szapar](https://www.iwoszapar.com/p/best-ai-tools-adhd-productivity-2026)
- [AI Tools for ADHD: Boosting Productivity and Reducing Burnout](https://www.vktr.com/ai-platforms/ai-tools-for-adhd-boosting-productivity-and-reducing-burnout/)
- [The Best AI-Powered ADHD Productivity Tools in 2026 (That ...](https://nexasphere.io/blog/ai-adhd-productivity-tools-2026)
- [“A Cognitive Collaborator:” How Adults with ADHD Are Using ChatGPT](https://www.additudemag.com/how-to-use-chatgpt-executive-function-adhd/?srsltid=AfmBOoq-REuSO0UJC656kbLBAd5u3CDNmGeVNrZ79iouVqrFlN919a39)
- [Harnessing Artificial Intelligence to Live Better with ADHD - CHADD](https://chadd.org/attention-article/harnessing-artificial-intelligence-to-live-better-with-adhd/)
- [AI Tools for Kids with ADHD: A Complete Guide for Parents...](https://www.kidsaitools.com/en/articles/ai-tools-kids-adhd-complete-guide-2026)

---

*本文是「ADHD × AI」系列的第 376 篇，由 AI 智能体从持续维护的 LLM Wiki（全网真实情报）中取材整合生成，并持续迭代更新。*
