---
title: "为什么用 Focusmate 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用 是一回事？"
subtitle: "Focusmate 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
description: "Focusmate 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
date: "2025-04-07"
category: "AI工具实战"
categoryId: "ai-tools"
categoryEn: "AI Tools in Practice"
tags:
  - "ADHD"
  - "AI"
  - "AI工具实战"
  - "反直觉同构"
  - "AI工具"
readingTime: 10
slug: "为什么用-focusmate-治-adhd-的任务启动困难和给-agent-套-function-calling-工具调用-是一回事"
topicId: "evolved-ai-tools-1570"
angle: "反直觉同构"
rank: 374
score: 7.65
sourceCount: 6
toolsCited:
  - "Focusmate"
  - "Goblin Tools"
  - "Saner.AI"
  - "Lex"
  - "ChatGPT"
  - "Claude"
thesis: "ADHD 大脑与 LLM 是同一类‘高产但缺执行调度层的生成核心’，Focusmate 与 function calling 工具调用都是通过外部 harness 补偿调度缺陷，两者结构同构。"
problem: "为什么用 Focusmate 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用 是一回事？"
spine: "工具使用与认知卸载"
spineKind: ""
isEvolved: true
llmGenerated: true
---
# 为什么用 Focusmate 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用 是一回事？

> Focusmate 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。

## 问题：为什么启动一件事这么难？

如果你是 ADHD 患者，你一定熟悉这个场景：任务摆在眼前，大脑却像死机一样，光标在空白文档上闪烁，你盯着屏幕，内心焦躁却无法行动。这种“任务启动困难”不是懒，而是执行功能的核心缺陷——大脑的“驾驶座”无人驾驶（来源：执行功能）。

如果你是做 Agentic Harness 的工程师，你一定也熟悉另一个场景：你给 LLM 一个复杂的任务，比如“帮我订机票并安排行程”，它要么直接拒绝，要么在第一步就卡住，无法自主调用工具完成多步流程。你不得不手动编写 function calling 的 schema，把任务拆成一个个原子步骤，再组装成链。

这两个场景看似风马牛不相及，但本质是同一个问题：**一个高产但缺执行调度层的生成核心，需要一个外部 harness 来启动和执行**。

## 同构：ADHD 大脑与 LLM 共享同一套缺陷剖面

最新研究揭示了一个反直觉的事实：ADHD 大脑与 LLM 在认知架构上惊人相似。明尼苏达大学的系统测试发现，LLM 呈现“强记忆、弱控制”剖面——工作记忆容量甚至超过常人，但认知灵活性与注意控制存在核心缺陷，无法灵活切换任务集、无法抑制自动化反应，这正是 ADHD 的经典神经心理模式（来源：Strong Memory, Weak Control: An Empirical Study of Executive Functioning in LLMs）。

耶鲁大学进一步发现，自注意力机制本身导致工作记忆容量限制：随任务复杂度增加，注意力分数熵增、注意力弥散、表现下降，与人类注意分散机制同源——“注意力资源的弥散分配”正是 ADHD 注意缺陷的计算本质（来源：Self-Attention Limits Working Memory Capacity of Transformer-Based Models）。

换句话说，ADHD 大脑和 LLM 都是**生成能力极强但调度层薄弱**的系统。ADHD 患者脑中充满创意和想法，但无法有效启动和排序；LLM 拥有海量知识，但无法自主规划多步行动。两者都需要一个“外部执行功能层”来补偿。

## 解法：Focusmate 与 function calling 是同一个 harness

Focusmate 是一个简单的服务：你预约一个 50 分钟的线上 session，和另一个陌生人同时开摄像头，各自做自己的事。它的原理是**身体在场效应**——知道有人在看着你，会迫使你的大脑进入“执行模式”。这不是心理暗示，而是对执行功能缺陷的直接补偿：外部监督代替了内部调度。

而 Function calling 工具调用呢？工程师为 LLM 定义一组工具（如“搜索航班”“查询日历”“发送邮件”），并编写一个 harness 来管理调用顺序和状态。LLM 不再需要自己规划全部步骤，只需在每一步选择正确的工具，由 harness 负责执行和上下文传递。

两者共享同一个结构：
- **ADHD 侧**：Focusmate 提供外部启动信号 + 持续监督，相当于一个“执行调度层”。
- **LLM 侧**：Function calling harness 提供预定义的步骤链 + 上下文管理，相当于一个“执行调度层”。

这就是同构脊柱的核心：**工具使用与认知卸载**。ADHD 大脑与 LLM 都是“生成核心”，而 Focusmate 和 function calling 都是“脚手架”——它们不是替代核心能力，而是补偿调度缺陷。

## 证据：真实工具如何体现这一思路

**Goblin Tools** 的 Magic ToDo 功能自动将“整理房间”分解为“捡起衣服”“擦桌子”等步骤，直接降低启动门槛（来源：Goblin Tools）。这相当于为 ADHD 大脑预写好 function calling 的 schema。用户反馈称“将压倒性的事情变成一系列不压倒性的事情”（来源：Goblin Tools）。

**Lex** 允许用户通过单一指令触发复杂多步骤任务，类似于为 LLM 定义了一个高级 API——你只需说“帮我写一篇周报”，它自动完成数据收集、模板填充、格式调整（来源：Lex）。这种“一次触发”的设计减少了决策疲劳，与 Focusmate 的“一键预约”异曲同工。

**Saner.AI** 通过增强知识回忆减少标签切换，相当于为 LLM 提供持久化上下文（来源：Saner.AI）。ADHD 用户常因工作记忆不足而丢失上下文，Saner.AI 的外部记忆相当于 LLM 的 RAG 系统。

## 脚手架 vs 拐杖：边界在哪里？

这里有一个必须指出的争议：过度依赖外部工具可能削弱内在能力。有警告指出，过度依赖 AI 工具可能削弱内在时间感知能力（来源：矛盾与存疑）。同样，如果 LLM 永远依赖预定义的 function calling 链，它永远不会学会自主规划。

关键在于区分“脚手架”与“拐杖”：脚手架是暂时性的，最终目标是让用户或模型内化技能；拐杖则是永久替代。Focusmate 的理想效果是用户逐渐学会在没有监督时也能启动；Function calling 的理想效果是 LLM 最终能自己生成工具调用链。但目前缺乏严格证据表明这些工具能促进能力迁移——大多数证据来自用户报告，缺乏大规模对照实验（来源：矛盾与存疑）。

## 今天就能试的行动

1. **ADHD 侧**：注册 Focusmate，预约一个 25 分钟 session（免费版可用），选择一件你拖延了一周的任务。体验“外部监督”如何降低启动门槛。
2. **LLM 侧**：如果你用 ChatGPT，尝试用“GPT Actions”或“Plugins”功能，定义一个简单的 function calling schema（比如“搜索+总结”）。观察 LLM 如何依赖外部工具完成多步任务。
3. **通用**：用 Goblin Tools 的 Magic ToDo 分解你当前最头疼的任务，把每一步写下来。对比你平时直接面对大任务时的启动焦虑差异。
4. **反思**：一周后，问自己：这些工具是帮助我学会了新技能，还是只是让我更依赖它们？如果是后者，尝试减少使用频率，刻意练习内部调度。

## 参考来源

- [Best AI Tools for ADHD Productivity in 2026 (Honest Review) - Iwo Szapar](https://www.iwoszapar.com/p/best-ai-tools-adhd-productivity-2026)
- [AI Tools for ADHD: Boosting Productivity and Reducing Burnout](https://www.vktr.com/ai-platforms/ai-tools-for-adhd-boosting-productivity-and-reducing-burnout/)
- [The Best AI-Powered ADHD Productivity Tools in 2026 (That ...](https://nexasphere.io/blog/ai-adhd-productivity-tools-2026)
- [“A Cognitive Collaborator:” How Adults with ADHD Are Using ChatGPT](https://www.additudemag.com/how-to-use-chatgpt-executive-function-adhd/?srsltid=AfmBOoq-REuSO0UJC656kbLBAd5u3CDNmGeVNrZ79iouVqrFlN919a39)
- [Harnessing Artificial Intelligence to Live Better with ADHD - CHADD](https://chadd.org/attention-article/harnessing-artificial-intelligence-to-live-better-with-adhd/)
- [AI Tools for Kids with ADHD: A Complete Guide for Parents...](https://www.kidsaitools.com/en/articles/ai-tools-kids-adhd-complete-guide-2026)

---

*本文是「ADHD × AI」系列的第 374 篇，由 AI 智能体从持续维护的 LLM Wiki（全网真实情报）中取材整合生成，并持续迭代更新。*
