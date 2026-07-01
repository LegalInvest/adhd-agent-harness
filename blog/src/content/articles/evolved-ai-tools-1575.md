---
title: "为什么用 Claude 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用 是一回事？"
subtitle: "Claude 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
description: "Claude 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
date: "2025-05-03"
category: "AI工具实战"
categoryId: "ai-tools"
categoryEn: "AI Tools in Practice"
tags:
  - "ADHD"
  - "AI"
  - "AI工具实战"
  - "反直觉同构"
  - "自动化"
readingTime: 14
slug: "为什么用-claude-治-adhd-的任务启动困难和给-agent-套-function-calling-工具调用-是一回事"
topicId: "evolved-ai-tools-1575"
angle: "反直觉同构"
rank: 137
score: 7.79
sourceCount: 6
toolsCited:
  - "Goblin Tools"
  - "Saner.AI"
  - "Lex"
  - "Claude"
  - "ChatGPT"
  - "Focusmate"
thesis: "ADHD大脑与LLM/agent在结构上同构——都是高产但缺执行调度层的生成核心——因此用Claude治ADHD的任务启动困难，和给agent套function calling工具调用，本质上是同一套harness（脚手架）思路：通过外部执行功能层补偿内在的调度缺陷，实现认知卸载与重锚定。"
problem: "为什么用 Claude 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用 是一回事？"
spine: "工具使用与认知卸载"
spineKind: ""
isEvolved: true
llmGenerated: true
---
# 为什么用 Claude 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用 是一回事？

> Claude 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。

你有没有过这样的经历：打开Claude，想写一封邮件，结果打了几个字就卡住，然后刷了半小时手机？或者，你给一个AI agent写好了详细的系统提示，它执行到第三步就开始跑偏，最后输出了一堆废话？

这两件事，表面看一个属于ADHD的“任务启动困难”，一个属于LLM agent的“指令消退”，但背后的结构问题一模一样。

## 问题：两个“高产但缺调度”的生成核心

ADHD大脑的核心矛盾是：发散思维、创意、多任务并行能力极高，但执行功能（任务启动、持续专注、抑制冲动）薄弱，导致“高产但不可靠”（来源：人在回路与身体在场）。正如wiki资料指出的，ADHD的执行功能缺陷与LLM的上下文控制缺陷一一对应：工作记忆容量保留但控制弱，任务启动困难对应LLM的“冷启动”问题，时间盲对应时序推理弱点（来源：ADHD的AI工具全景）。

LLM/agent侧同样如此。模型本身是强大的生成核心，但缺乏可靠的执行调度层，直接输出可能偏离目标、陷入循环或产生危险行为（来源：人在回路与身体在场）。在长程任务中，模型会“开始忘记系统提示”，导致行为偏离初始指令——这正是ADHD式的“目标漂移”（来源：重锚定与目标漂移）。

两边都是：核心很强，但缺一个执行调度层。

## 答案：同一套harness思路

解决方案也同构：为生成核心套上一个外部harness（脚手架），通过工具调用（function calling）和人在回路监督，提供任务分解、上下文管理和重锚定。

**ADHD侧的证据：**
- **Goblin Tools**的Magic ToDo功能，自动将复杂任务分解为小步骤，用户反馈“将压倒性的事情变成一系列不压倒性的事情”（来源：Goblin Tools）。这直接针对任务启动困难，相当于为大脑提供“启动脚本”。
- **Lex**允许通过单一指令触发多步骤任务序列，降低了决策疲劳（来源：Lex）。这对应LLM侧的“一次指令，多次工具调用”。
- **Saner.AI**通过本地记忆减少搜索循环和标签切换，补偿工作记忆不足（来源：Saner.AI）。这对应LLM侧的持久化上下文。
- **Focusmate**等虚拟身体搭档提供外部问责，绕过执行功能屏障（来源：人在回路与身体在场）。这对应LLM侧的human-in-the-loop监督。

**LLM/agent侧的证据：**
- Agent harness通过事件驱动的系统提醒对抗“指令消退”，类似于ADHD工具的重锚定系统（来源：重锚定与目标漂移）。
- Harness加入人工检查点（暂停并询问后再执行），设置护栏（token预算、工具调用次数上限），确保模型输出可靠（来源：人在回路与身体在场）。
- “模型本身强大，可靠性来自架构+护栏”（来源：人在回路与身体在场）。这正是ADHD工具的设计哲学：不改变核心，而是改造环境。

## 核心观点：脚手架，不是拐杖

但这里有一个关键边界：脚手架 vs 拐杖。Wiki资料明确警告：“过度依赖AI工具可能削弱内在能力”（来源：矛盾与存疑）。Goblin Tools的任务分解如果永远不让你自己学会拆任务，就成了拐杖；Saner.AI的自动回忆如果让你不再练习记忆，也成了拐杖。同样，agent harness如果过度依赖人在回路，模型永远学不会自我纠偏。

好的harness应该是“可渐撤的脚手架”：一开始提供强支持，随着能力提升逐步移除。例如，Claude的对话式整理可以帮你理清思路，但最终你应该内化这种结构化思考方式。

## 局限与争议

必须诚实承认：现有证据主要来自用户报告和概念类比，缺乏大规模对照实验（来源：矛盾与存疑）。AI工具的实际效果尚未得到严格验证，存在夸大宣传的可能。个体差异也很大——对某些ADHD用户有效的工具，对另一些人可能无效甚至适得其反。

## 今天就能试的行动

1. **用Claude做任务分解**：输入一个让你焦虑的大任务（如“整理房间”），要求它拆成5-10个可执行的小步骤。完成后，尝试不看清单自己复述步骤——这是“渐撤”的第一步。
2. **给自己设一个“重锚定”提醒**：用手机或Claude的定时功能，每20分钟问自己一次“我现在在做什么？应该做什么？”对抗目标漂移。
3. **尝试一次“单指令多步骤”**：在Claude里写一个复合指令，比如“帮我写一封邮件，主题是会议确认，然后把它添加到我的待办清单里”。观察它是否一次完成——这正是agent function calling的雏形。
4. **记录一次“指令消退”**：下次你用任何AI工具时，注意它是否在几轮对话后开始偏离原始意图。记录下来，这就是你的harness需要加强的地方。

## 结语

ADHD大脑和LLM/agent是同一种“天才但失控”的架构。Claude治ADHD和agent套function calling，本质上都是在说同一件事：别指望核心自己变好，给它一个外部调度层。这个认识，既能让ADHD用户少一些自责，也能让agent工程师少一些对模型的幻想。

## 参考来源

- [Best AI Tools for ADHD Productivity in 2026 (Honest Review) - Iwo Szapar](https://www.iwoszapar.com/p/best-ai-tools-adhd-productivity-2026)
- [AI Tools for ADHD: Boosting Productivity and Reducing Burnout](https://www.vktr.com/ai-platforms/ai-tools-for-adhd-boosting-productivity-and-reducing-burnout/)
- [The Best AI-Powered ADHD Productivity Tools in 2026 (That ...](https://nexasphere.io/blog/ai-adhd-productivity-tools-2026)
- [“A Cognitive Collaborator:” How Adults with ADHD Are Using ChatGPT](https://www.additudemag.com/how-to-use-chatgpt-executive-function-adhd/?srsltid=AfmBOoq-REuSO0UJC656kbLBAd5u3CDNmGeVNrZ79iouVqrFlN919a39)
- [Harnessing Artificial Intelligence to Live Better with ADHD - CHADD](https://chadd.org/attention-article/harnessing-artificial-intelligence-to-live-better-with-adhd/)
- [AI Tools for Kids with ADHD: A Complete Guide for Parents...](https://www.kidsaitools.com/en/articles/ai-tools-kids-adhd-complete-guide-2026)

---

*本文是「ADHD × AI」系列的第 137 篇，由 AI 智能体从持续维护的 LLM Wiki（全网真实情报）中取材整合生成，并持续迭代更新。*
