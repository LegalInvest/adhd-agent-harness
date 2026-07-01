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
  - "Goblin Tools"
  - "Saner.AI"
  - "Lex"
  - "ChatGPT"
  - "Motion"
  - "Reclaim.ai"
  - "Tiimo"
thesis: "ADHD大脑与LLM在结构上同构——都是强大的生成核心但缺乏执行调度层，因此用ChatGPT治任务启动困难与给agent套function calling是同一套harness思路：通过外部工具提供执行功能、记忆管理和上下文控制，弥补内在调度缺陷。"
problem: "为什么用 ChatGPT 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用 是一回事？"
spine: "工具使用与认知卸载"
spineKind: ""
isEvolved: true
llmGenerated: true
---
# 为什么用 ChatGPT 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用 是一回事？

> ChatGPT 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。

## 问题：两个看似不相关的困境

你是一个ADHD患者，坐在书桌前，任务清单上写着“整理房间”或“写周报”。你知道该做什么，大脑里甚至已经闪过几个步骤，但身体就是不动。你盯着屏幕，刷了半小时手机，然后陷入自责。这是**任务启动困难**——ADHD的核心执行功能缺陷之一（来源：任务启动）。

你是一个AI工程师，在构建一个LLM agent。你发现模型本身能生成流畅的文本、理解复杂指令，但一旦需要它调用外部API、执行多步骤任务，它就频频出错：要么忘记传递参数，要么在中间步骤卡住，要么输出一堆废话而不实际执行。你需要给这个“聪明但混乱”的模型套上**function calling**框架，定义好工具、约束输出格式、管理上下文。

表面看，这是两个完全不同的世界。但本文要论证一个反直觉的同构：**ADHD大脑与LLM是同一类“高产但缺执行调度层的生成核心”，两边的解法（harness/脚手架）结构同构。** 用ChatGPT治ADHD的任务启动困难，和给agent套function calling工具调用，本质上是同一回事。

## 同构：生成核心 vs 执行调度层

ADHD大脑的生成核心（智力、创造力）与LLM的生成能力类似，但两者都缺乏执行功能——计划、组织、工作记忆的稳定调度（来源：ADHD 的 AI 工具全景）。ADHD患者的工作记忆常常成为瓶颈（来源：工作记忆），导致任务步骤无法在脑中清晰呈现，就像LLM的上下文窗口有限，容易丢失中间状态。

在LLM agent中，function calling是一种外部执行功能层：它定义工具（如搜索、计算器）、约束输出格式（JSON）、管理调用历史（上下文）。这恰好对应ADHD领域AI工具的设计逻辑：**通过外部工具提供执行功能、记忆管理和上下文控制**（来源：ADHD 的 AI 工具全景）。

## 证据：两边都成立的harness思路

### ADHD侧：工具即脚手架

- **Goblin Tools**的Magic ToDo功能将复杂任务分解为小步骤，降低启动焦虑。用户输入“整理房间”，AI输出“捡起地板上的衣服”“擦桌子”等步骤（来源：Goblin Tools）。这相当于给ADHD大脑一个预定义的function calling序列，每个步骤是一个明确的工具调用。
- **Lex**允许用户通过单一指令触发复杂、多步骤的任务序列（来源：Lex）。这类似于LLM agent的“一次触发，多步执行”模式，减少了决策负担。
- **Saner.AI**通过知识回忆功能减少搜索循环（来源：Saner.AI），相当于给ADHD大脑一个外部记忆库，避免在工作记忆中同时维持太多信息。

### LLM/Agent侧：同样的脚手架

在agent工程中，function calling的核心是：
1. **分解任务**：将复杂指令拆分为可调用的工具步骤（类似Goblin Tools的分解）。
2. **管理上下文**：维护调用历史，避免模型遗忘（类似Saner.AI的外部记忆）。
3. **约束输出**：强制模型输出结构化JSON，而非自由文本（类似Lex的单一指令触发）。

一项针对ADHD儿童的研究指出，AI工具特别适合“任务启动和规划困难”（来源：任务启动），而这正是function calling要解决的agent痛点。

## 核心判断：脚手架 vs 拐杖

本文的核心观点是：**AI工具作为外部执行功能层，有效补偿ADHD的核心缺陷，但需警惕过度依赖成为“拐杖”而非“脚手架”。** 脚手架是可逐步撤除的临时支撑，而拐杖是永久替代。

当前多数工具（如Goblin Tools、Saner.AI）设计为长期使用，未明确提供撤除机制（来源：矛盾与存疑）。同样，在agent工程中，过度依赖function calling框架可能导致模型本身不学习规划能力——但这对agent不是问题，因为它的目标是完成任务。而对ADHD患者，目标是最终减少对工具的依赖。

## 争议与局限

必须诚实指出：
- **同构命题的证据**主要来自概念类比和工具案例，缺乏大规模实证（来源：矛盾与存疑）。
- **长期效果未知**：缺乏随机对照试验验证AI工具对ADHD核心症状的长期改善（来源：ADHD 的 AI 工具全景）。
- **个性化适配不足**：ADHD异质性高，单一工具难以覆盖所有亚型（来源：ADHD 的 AI 工具全景）。

## 今天就能试的行动

1. **用ChatGPT模拟Goblin Tools**：输入“把‘整理房间’分解成10个小步骤，每个步骤用一句话描述”，观察它如何降低启动门槛。
2. **给自己设计“function calling”**：在便签上写下当前任务所需的“工具”（如“打开文档”“搜索资料”“写第一段”），每完成一个划掉。
3. **尝试Lex或类似工具**：如果可用，用一个指令触发一个多步骤流程（如“准备会议：创建议程、发送邀请、准备幻灯片”）。
4. **反思依赖**：记录使用AI工具后，你是否能逐渐减少使用频率？如果完全依赖，考虑设置“撤除计划”。

## 参考来源

- [Best AI Tools for ADHD Productivity in 2026 (Honest Review) - Iwo Szapar](https://www.iwoszapar.com/p/best-ai-tools-adhd-productivity-2026)
- [AI Tools for ADHD: Boosting Productivity and Reducing Burnout](https://www.vktr.com/ai-platforms/ai-tools-for-adhd-boosting-productivity-and-reducing-burnout/)
- [The Best AI-Powered ADHD Productivity Tools in 2026 (That ...](https://nexasphere.io/blog/ai-adhd-productivity-tools-2026)
- [“A Cognitive Collaborator:” How Adults with ADHD Are Using ChatGPT](https://www.additudemag.com/how-to-use-chatgpt-executive-function-adhd/?srsltid=AfmBOoq-REuSO0UJC656kbLBAd5u3CDNmGeVNrZ79iouVqrFlN919a39)
- [Harnessing Artificial Intelligence to Live Better with ADHD - CHADD](https://chadd.org/attention-article/harnessing-artificial-intelligence-to-live-better-with-adhd/)
- [AI Tools for Kids with ADHD: A Complete Guide for Parents...](https://www.kidsaitools.com/en/articles/ai-tools-kids-adhd-complete-guide-2026)

---

*本文是「ADHD × AI」系列的第 24 篇，由 AI 智能体从持续维护的 LLM Wiki（全网真实情报）中取材整合生成，并持续迭代更新。*
