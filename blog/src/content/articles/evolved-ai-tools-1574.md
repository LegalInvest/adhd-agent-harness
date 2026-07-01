---
title: "为什么用 ChatGPT 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用 是一回事？"
subtitle: "ChatGPT 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
description: "ChatGPT 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
date: "2025-05-11"
category: "AI工具实战"
categoryId: "ai-tools"
categoryEn: "AI Tools in Practice"
tags:
  - "ADHD"
  - "AI"
  - "AI工具实战"
  - "反直觉同构"
  - "效率工具"
readingTime: 14
slug: "为什么用-chatgpt-治-adhd-的任务启动困难和给-agent-套-function-calling-工具调用-是一回事"
topicId: "evolved-ai-tools-1574"
angle: "反直觉同构"
rank: 24
score: 8.0
sourceCount: 6
toolsCited:
  - "ChatGPT"
  - "Goblin Tools"
  - "Saner.AI"
  - "Lex"
  - "Mem"
  - "Claude"
  - "Otter.ai"
  - "Reflect"
thesis: "ADHD的任务启动困难与LLM agent的function calling冷启动是同一类问题——两者都是「高产但缺执行调度层的生成核心」，解决方案也同构：通过外部harness（脚手架）提供启动脚本与工具调用接口，而非永久拐杖。"
problem: "为什么用 ChatGPT 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用 是一回事？"
spine: "工具使用与认知卸载"
spineKind: ""
isEvolved: true
llmGenerated: true
---
# 为什么用 ChatGPT 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用 是一回事？

> ChatGPT 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。

## 问题：两个世界，同一个卡住

如果你是一个ADHD成年人，你大概率经历过这样的时刻：明明知道该写报告了，但手指就是敲不下键盘，大脑像卡壳的发动机，越催越不动。你打开ChatGPT，输入“帮我拆解写报告的第一步”，然后……顺利启动了。

如果你是一个在做Agentic Harness工程的开发者，你大概率也经历过这样的场景：你给大模型套上了function calling框架，定义了十几个工具，但模型在第一个任务上就犹豫不决，输出了一堆无关的思考，迟迟不调用`call_tool`。你给它一个明确的“启动脚本”，它才流畅地执行下去。

这两个场景，看似分属心理学和工程学，但底层是同一个问题：**一个高产能的生成核心，缺少一个外部执行调度层。** ADHD大脑和LLM agent，都是“高产但缺执行调度层的生成核心”（来源：ADHD 的 AI 工具全景）。本文要论证的是：用ChatGPT治ADHD的任务启动困难，和给agent套function calling工具调用，本质上是同一套harness思路。

## 同构：任务启动困难 vs. 冷启动问题

ADHD侧的任务启动困难，根源于多巴胺系统失衡导致行动动机不足，以及工作记忆容量有限使任务步骤难以清晰呈现（来源：任务启动）。LLM侧的对应物是“冷启动”问题：模型在零样本或少样本下，面对一个模糊的复杂任务，缺乏明确的执行路径，容易陷入循环或发散（来源：ADHD 的 AI 工具全景）。两者都需要一个“启动脚本”——一个将模糊意图转化为具体可执行步骤的外部指令。

**真实证据（ADHD侧）：** 用户报告显示，Goblin Tools的“魔法待办”功能可将“整理房间”自动分解为“捡起地板上的衣服”“擦桌子”等步骤，降低启动门槛（来源：Goblin Tools）。另一项研究指出，ADHD成年人自发使用ChatGPT作为执行功能外挂，通过对话生成步骤、提供即时反馈来弥补启动困难（来源：任务启动）。这些工具本质上是外部执行功能层，为生成核心提供启动脚本。

**真实证据（LLM/Agent侧）：** 在function calling框架中，开发者通过定义工具列表和调用规范，让LLM从“自由生成”切换到“工具调用”模式。例如，Lex允许用户通过单一指令触发复杂、多步骤的任务序列（来源：Lex），这与agent的“单指令多工具调用”完全同构。Saner.AI通过增强知识回忆减少搜索循环和标签切换（来源：Saner.AI），对应LLM侧的外部记忆系统（如Mem的“AI第二大脑”），为agent提供持久化上下文。

## 核心观点：脚手架，而非拐杖

本文的核心判断是：**AI工具作为外部harness，应设计为脚手架促进能力发展，而非永久拐杖。** 这一观点在wiki资料中反复出现：Goblin Tools等工具被描述为“将压倒性的事情变成一系列不压倒性的事情”，但过度依赖可能削弱内在能力（来源：矛盾与存疑）。同样，在agent工程中，function calling框架应逐步减少硬编码规则，让模型学会自主调度——否则agent永远无法脱离人工编排。

**脚手架 vs. 拐杖的边界：** 脚手架提供临时支撑，帮助用户/模型构建内在能力；拐杖则永久替代。例如，Tiimo通过视觉化时间表帮助ADHD用户感知时间流逝（来源：时间盲），但若用户从不主动估算时间，工具就成了拐杖。在agent侧，如果每次任务都需要人类手动定义工具调用顺序，框架就成了拐杖。好的harness应像Lex那样“实时适应大脑的工作方式”（来源：Lex），同时留出成长空间。

## 矛盾与局限

必须诚实指出，当前证据存在局限。**第一，有效性证据不足：** 大多数AI工具的效果基于用户报告，缺乏大规模随机对照试验（来源：矛盾与存疑）。**第二，个体差异大：** 任务启动困难的程度和成因因人而异，一刀切的工具可能无效（来源：矛盾与存疑）。**第三，依赖风险真实存在：** 过度使用Goblin Tools可能削弱主动分解任务的能力，正如过度依赖Otter.ai可能削弱主动记笔记的能力（来源：ADHD 的 AI 工具全景）。在agent工程中，过度依赖function calling模板也可能降低模型的泛化能力。

## 今天就能试的行动

1. **ADHD侧：** 下次启动困难时，打开ChatGPT或Goblin Tools，输入“帮我将[具体任务]分解为3-5个可执行的步骤”，并立即执行第一步。这相当于给大脑一个启动脚本。
2. **Agent侧：** 在开发function calling框架时，为agent设计一个“初始化提示”，明确指定第一个工具调用的触发条件。例如，在系统提示中加入“当收到任务后，先调用`analyze_task`工具，再决定后续步骤”。
3. **通用行动：** 每周反思一次：我是否过度依赖某个工具？尝试在没有工具的情况下手动完成一次任务分解或工具调用，评估内在能力是否退化。
4. **双向借鉴：** 如果你是ADHD用户，可以学习agent的“工具调用”思维——把每个任务视为一系列工具调用（如“打开文档”=调用`open_doc`，“写第一段”=调用`write_para`），降低认知负荷。如果你是工程师，可以借鉴ADHD工具的设计原则——减少决策点，提供即时反馈。

## 结语

ADHD大脑和LLM agent，本质上都是“天才生成器，傻瓜调度器”。理解这一同构，不仅能帮助ADHD用户更聪明地使用AI，也能帮助工程师设计更人性化的agent框架。下一次当你卡在启动时，记住：你需要的不是更多意志力，而是一个更好的harness。

## 参考来源

- [Best AI Tools for ADHD Productivity in 2026 (Honest Review) - Iwo Szapar](https://www.iwoszapar.com/p/best-ai-tools-adhd-productivity-2026)
- [AI Tools for ADHD: Boosting Productivity and Reducing Burnout](https://www.vktr.com/ai-platforms/ai-tools-for-adhd-boosting-productivity-and-reducing-burnout/)
- [The Best AI-Powered ADHD Productivity Tools in 2026 (That ...](https://nexasphere.io/blog/ai-adhd-productivity-tools-2026)
- [“A Cognitive Collaborator:” How Adults with ADHD Are Using ChatGPT](https://www.additudemag.com/how-to-use-chatgpt-executive-function-adhd/?srsltid=AfmBOoq-REuSO0UJC656kbLBAd5u3CDNmGeVNrZ79iouVqrFlN919a39)
- [Harnessing Artificial Intelligence to Live Better with ADHD - CHADD](https://chadd.org/attention-article/harnessing-artificial-intelligence-to-live-better-with-adhd/)
- [AI Tools for Kids with ADHD: A Complete Guide for Parents...](https://www.kidsaitools.com/en/articles/ai-tools-kids-adhd-complete-guide-2026)

---

*本文是「ADHD × AI」系列的第 24 篇，由 AI 智能体从持续维护的 LLM Wiki（全网真实情报）中取材整合生成，并持续迭代更新。*
