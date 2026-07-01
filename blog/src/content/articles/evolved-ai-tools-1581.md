---
title: "为什么用 Endel 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用 是一回事？"
subtitle: "Endel 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
description: "Endel 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
date: "2025-03-16"
category: "AI工具实战"
categoryId: "ai-tools"
categoryEn: "AI Tools in Practice"
tags:
  - "ADHD"
  - "AI"
  - "AI工具实战"
  - "反直觉同构"
  - "ADHD辅助"
readingTime: 8
slug: "为什么用-endel-治-adhd-的任务启动困难和给-agent-套-function-calling-工具调用-是一回事"
topicId: "evolved-ai-tools-1581"
angle: "反直觉同构"
rank: 383
score: 7.65
sourceCount: 6
toolsCited:
  - "Endel"
  - "Goblin Tools"
  - "Saner.AI"
  - "Lex"
  - "Mem"
  - "Otter.ai"
  - "ChatGPT"
  - "Claude"
thesis: "ADHD大脑与LLM都是强大的生成核心但缺乏执行调度层，两者共享同一套'工具调用'解法——通过外部harness提供function calling式的认知卸载，这正是Endel等工具能同时帮助ADHD患者和agent工程师的根本原因。"
problem: "为什么用 Endel 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用 是一回事？"
spine: "工具使用与认知卸载"
spineKind: ""
isEvolved: true
llmGenerated: true
---
# 为什么用 Endel 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用 是一回事？

> Endel 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。

## 问题：为什么你明明有想法，却就是动不了？

如果你是ADHD患者，你一定熟悉这个场景：大脑里装着无数创意、计划和待办事项，但坐在电脑前，光标闪烁，你却什么也做不了。不是不想做，而是**启动任务**——那个从“想”到“做”的瞬间——像一堵无形的墙。

如果你是做Agentic Harness的工程师，你同样熟悉另一个场景：你精心训练的LLM模型，在基准测试中表现优异，但一旦扔进真实任务，它要么卡在第一步，要么输出一堆格式错误、上下文断裂的垃圾。不是模型不够聪明，而是它**缺乏调用外部工具的能力**——它不知道何时、如何、以什么顺序调用function。

这两个问题，看似风马牛不相及，但当你把ADHD大脑和LLM并排放置时，会发现惊人的同构：**两者都是高产但缺执行调度层的生成核心**。ADHD大脑的智力与创造力，和LLM的生成能力一样，都需要一个外部的“执行调度层”——也就是harness——来把意图转化为行动。而Endel这类工具，本质上就是在做这件事：为ADHD大脑提供function calling式的认知卸载。

## 同构：ADHD大脑与LLM的“执行功能缺失”

ADHD大脑的核心缺陷在于**执行功能**——包括工作记忆、任务启动、时间感知和计划组织（来源：AI Tools for ADHD: Boosting Productivity and Reducing Burnout）。这就像一个超级GPU，算力爆表，但缺少CPU来调度指令。ADHD患者常常“知道该做什么，但就是做不了”，因为大脑的“执行调度层”宕机了。

LLM/Agent同样如此。一个没有harness的LLM只是一个无状态的API调用（来源：Building an AI Agent Harness from Scratch: The Architecture Between LLM and Agent - DEV Community）。它可以在一次对话中生成精彩内容，但无法跨会话保持上下文，无法自主调用工具，无法分解复杂任务。它需要外部系统提供上下文传递、工具接口、规划工件和记忆系统——这正是harness工程要解决的问题（来源：GitHub - ai-boost/awesome-harness-engineering）。

两边缺失的是同一个东西：**一个可靠的、可调用的外部执行层**。

## 解法同构：Endel与function calling

Endel是一款通过自适应音频帮助用户进入专注状态的工具。它根据你的心率、环境、时间等因素，实时生成声音场景，降低认知负荷，帮助启动任务。但Endel的真正价值不在于“音乐”，而在于它**充当了一个外部调度器**：它接管了大脑中“我需要进入状态”这个元认知任务，把它变成了一个自动化的、低决策成本的触发信号。

这恰好就是function calling在agent中的角色。当agent需要执行一个任务时，它不再自己硬算所有步骤，而是调用外部工具（如搜索、计算器、数据库）来分担认知负载。function calling的本质是**认知卸载**：把“如何做”的细节交给外部系统，让生成核心专注于“做什么”。

ADHD大脑同样需要这种卸载。Goblin Tools的Magic ToDo功能自动将“整理房间”分解为“捡起地板上的衣服”“擦桌子”等小步骤（来源：Harnessing Artificial Intelligence to Live Better with ADHD - CHADD），这相当于给ADHD大脑注册了一个“任务分解”function。Saner.AI提供知识回忆，减少搜索循环（来源：Best AI Tools for ADHD Productivity in 2026 (Honest Review) - Iwo Szapar），相当于一个“记忆检索”function。Lex允许单一指令触发多步骤任务（来源：Best AI Tools for ADHD Productivity in 2026 (Honest Review) - Iwo Szapar），相当于一个“复合任务”function。

## 脚手架 vs 拐杖：边界在哪里？

既然解法同构，那么ADHD工具和agent harness面临同一个挑战：**如何避免成为永久拐杖，而是可撤除的脚手架？**

在agent工程中，一个好的harness应该允许agent逐步内化能力。比如，初始阶段agent依赖外部搜索工具，但通过微调，模型可以将搜索模式内化为自身知识。同样，ADHD工具也应该设计为：用户先依赖工具完成启动，然后逐步减少依赖，最终内化执行功能。

但现实是，多数ADHD工具（如Goblin Tools、Saner.AI）被设计为长期使用，未提及撤除机制（来源：拐杖与脚手架概念页）。专家警告，过度依赖可能阻碍内在执行功能发展（来源：AI Tools for ADHD: Boosting Productivity and Reducing Burnout）。同样，agent工程中，如果harness过于厚重，agent会失去自主性，变成“提线木偶”。

## 证据与争议

目前，ADHD工具的效果证据主要来自用户评价和综述，缺乏大规模随机对照试验（来源：ADHD的AI工具全景）。Endel的神经锁相技术声称有效，但缺乏独立临床研究支持（来源：矛盾与存疑）。同构命题本身更多是概念类比，缺乏实证（来源：ADHD大脑与LLM的同构概念页）。

但这并不妨碍我们利用这个框架。因为即使同构不是科学事实，它也是一个极其有效的**设计原则**：当你为ADHD大脑设计工具时，假装它是一个LLM，问自己“这个LLM需要什么harness才能可靠工作？”答案往往是：上下文管理、工具接口、记忆系统、任务分解——而这些，正是Goblin Tools、Saner.AI、Lex在做的事。

## 今天就能试的行动

1. **用Goblin Tools分解一个你拖延已久的任务**：输入“写周报”，看它输出哪些步骤。感受一下“启动门槛”被降低的感觉。
2. **用Endel或类似工具作为“启动触发器”**：在开始工作前播放5分钟，把它当作一个function call，告诉大脑“现在调用执行模式”。
3. **给ChatGPT/Claude写一个“ADHD助手”提示**：明确要求它扮演执行功能教练，帮你分解任务、提醒时间、记录上下文。这相当于你手动搭建了一个轻量级harness。
4. **反思你的工具依赖**：问自己“如果明天这些工具消失了，我还能独立完成这个任务吗？”如果是，说明工具是脚手架；如果否，说明已经成了拐杖。

同构不是巧合，而是设计智慧的体现。ADHD大脑和LLM都需要一个外部的执行调度层——而Endel、Goblin Tools、function calling，都是这个层上的不同实现。理解这一点，你就能同时成为更好的ADHD自我管理者，和更好的agent工程师。

## 参考来源

- [Best AI Tools for ADHD Productivity in 2026 (Honest Review) - Iwo Szapar](https://www.iwoszapar.com/p/best-ai-tools-adhd-productivity-2026)
- [AI Tools for ADHD: Boosting Productivity and Reducing Burnout](https://www.vktr.com/ai-platforms/ai-tools-for-adhd-boosting-productivity-and-reducing-burnout/)
- [The Best AI-Powered ADHD Productivity Tools in 2026 (That ...](https://nexasphere.io/blog/ai-adhd-productivity-tools-2026)
- [“A Cognitive Collaborator:” How Adults with ADHD Are Using ChatGPT](https://www.additudemag.com/how-to-use-chatgpt-executive-function-adhd/?srsltid=AfmBOoq-REuSO0UJC656kbLBAd5u3CDNmGeVNrZ79iouVqrFlN919a39)
- [Harnessing Artificial Intelligence to Live Better with ADHD - CHADD](https://chadd.org/attention-article/harnessing-artificial-intelligence-to-live-better-with-adhd/)
- [AI Tools for Kids with ADHD: A Complete Guide for Parents...](https://www.kidsaitools.com/en/articles/ai-tools-kids-adhd-complete-guide-2026)

---

*本文是「ADHD × AI」系列的第 383 篇，由 AI 智能体从持续维护的 LLM Wiki（全网真实情报）中取材整合生成，并持续迭代更新。*
