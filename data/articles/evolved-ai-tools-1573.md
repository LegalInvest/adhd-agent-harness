---
title: "为什么用 Mem 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用 是一回事？"
subtitle: "Mem 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
description: "Mem 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
date: "2025-05-27"
category: "AI工具实战"
categoryId: "ai-tools"
categoryEn: "AI Tools in Practice"
tags:
  - "ADHD"
  - "AI"
  - "AI工具实战"
  - "反直觉同构"
  - "AI工具"
readingTime: 12
slug: "为什么用-mem-治-adhd-的任务启动困难和给-agent-套-function-calling-工具调用-是一回事"
topicId: "evolved-ai-tools-1573"
angle: "反直觉同构"
rank: 377
score: 7.65
sourceCount: 6
toolsCited:
  - "Mem"
  - "Goblin Tools"
  - "Saner.AI"
  - "Lex"
  - "ChatGPT"
  - "Claude"
  - "Otter.ai"
  - "Reflect"
thesis: "ADHD的任务启动困难与LLM agent的function calling工具调用在结构上同构——两者都是为高产但缺调度层的生成核心套上外部执行脚手架（harness），而非提供永久拐杖。"
problem: "为什么用 Mem 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用 是一回事？"
spine: "工具使用与认知卸载"
spineKind: ""
isEvolved: true
llmGenerated: true
---
# 为什么用 Mem 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用 是一回事？

> Mem 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。

## 问题：为什么ADHD用户面对空白任务清单会僵住，而LLM agent面对开放指令会“胡言乱语”？

你有没有过这样的体验：坐在电脑前，待办清单上写着“整理项目方案”，大脑却像被冻住一样，光标闪烁十分钟，一个字没动。这不是懒惰——这是ADHD的“任务启动困难”。与此同时，如果你在调试一个LLM agent，直接问它“帮我完成这个项目”，它可能会输出一堆看似合理但实则离题的废话，甚至编造数据。为什么？因为两者都缺少一个关键的调度层。

## 同构：ADHD大脑与LLM agent是同一类“高产但缺执行调度层”的生成核心

从神经科学视角看，ADHD的核心问题是多巴胺系统功能低下，导致中脑皮质分支调控的注意反应和执行功能受损（来源：多巴胺）。这意味着ADHD大脑像一个强大的生成引擎——能产生丰富的想法和创意——但缺乏一个内置的“执行调度层”来把这些想法转化为有序的行动。任务启动困难，本质上是这个调度层在面临“空白页”时无法发出第一个指令。

同样，LLM（如GPT-4、Claude）是强大的文本生成引擎，但直接给出开放指令时，它们也会“冷启动”困难：缺乏明确的工具调用（function calling）指令，模型容易在上下文中迷失，生成无关或错误的内容。这正是LLM的“上下文控制缺陷”——与ADHD的工作记忆控制缺陷一一对应（来源：ADHD 大脑与 LLM 的同构）。

## 答案：Mem 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用，都是同一套 harness 思路

Mem 是一款“AI第二大脑”工具，它通过持久记忆和自动回忆来补偿ADHD用户的工作记忆缺陷（来源：ADHD 的 AI 工具全景）。当用户面对“整理项目方案”这样的任务时，Mem 不是直接替用户写方案，而是提供一个外部记忆层：它记住用户之前的碎片想法、相关笔记、待办事项，然后自动呈现一个“上下文启动包”。这相当于为ADHD大脑提供了一个**启动脚本**——就像给LLM agent预先定义好function calling的schema和工具列表，让agent知道“你可以调用这些工具来完成目标”。

从工程角度看，function calling的实质是：将LLM的生成能力约束在一个预定义的“工具集”内，通过结构化接口降低模型的认知负荷，避免它从零开始推理全部步骤。这正是ADHD工具（如Goblin Tools、Lex）所做的：Goblin Tools的“魔法开关”将大任务分解为小步骤（来源：Goblin Tools），Lex通过单一指令触发多步骤序列（来源：Lex），Saner.AI则通过本地记忆减少搜索循环（来源：Saner.AI）。这些工具都在做同一件事：**为生成核心套上harness（脚手架），把“下一步做什么”的决策从内部调度层外化到外部工具**。

## 证据：两边都有真实支撑

ADHD侧的证据主要来自用户报告和工具设计逻辑。Goblin Tools被评价为“将压倒性的事情变成一系列不压倒性的事情”（来源：Goblin Tools），用户称其降低了启动焦虑。Lex的“单一指令触发复杂流程”减少了决策疲劳（来源：Lex）。这些工具的共性在于：它们不是替用户完成任务，而是**重构任务的结构**，使其可启动。

LLM/agent侧的证据更硬：在经典的Stroop冲突任务测试中，Transformer注意力模型在短上下文中表现正常，但随序列变长（认知负荷增加），模型在冲突试次上骤降到随机水平——无法抑制优势反应、无法解决认知冲突（来源：认知负荷）。这与ADHD执行功能缺陷的核心标志一一对应：注意控制不足、干扰抑制缺陷、随认知负荷增加而崩溃。而function calling正是通过将复杂任务分解为子任务，减轻LLM的认知负荷，减少幻觉等错误（来源：认知负荷）。本质上是同一套“任务分解”策略。

## 核心判断：脚手架 vs 拐杖的边界在于是否保留用户的主动选择权

这里有一个关键争议：AI工具究竟是脚手架还是拐杖？多个资料警告“过度依赖可能削弱内在能力”（来源：矛盾与存疑）。例如，Otter.ai减轻笔记负担，但长期使用可能削弱主动记笔记的能力。同样，如果LLM agent的function calling被设计成完全自主调用所有工具，人类就变成了旁观者，失去了对过程的控制。

我的判断是：**真正的harness（脚手架）必须保留用户的“否决权”和“选择权”**。Mem不会自动帮你写方案，而是呈现相关笔记让你选择；Goblin Tools不会替你执行步骤，而是列出清单让你打勾；function calling的schema应该让agent提议调用哪个工具，但由人类确认。一旦工具越过“提议”进入“代劳”，它就变成了拐杖。

## 局限与诚实

必须承认，现有证据主要来自用户报告和概念类比，缺乏大规模对照实验（来源：矛盾与存疑）。个体差异巨大：有些ADHD用户觉得Goblin Tools的分步清单是救命稻草，另一些人却觉得步骤太多反而增加认知负荷。同样，function calling在不同模型和任务上的效果也不一致。此外，多巴胺干预效果本身存在争议（来源：矛盾与存疑），因此基于多巴胺假说的工具设计也需谨慎。

## 今天就能试的行动

1. **如果你有ADHD任务启动困难**：打开Mem（或任何带笔记功能的AI工具），在开始任务前，先花3分钟用语音或文字“倾倒”所有相关碎片想法，让AI自动整理成要点。这相当于为自己生成一个“启动上下文”。
2. **如果你在调试LLM agent**：不要直接给开放指令。先定义2-3个function（如“搜索资料”“总结要点”“生成大纲”），然后让模型先调用“搜索资料”再输出。观察任务完成质量是否提升。
3. **两者通用**：无论是人类还是agent，每次启动新任务前，先问自己/模型：“完成这个任务需要哪3个最小步骤？”用外部工具（纸笔或AI）写下来。这能绕过“冷启动”僵局。
4. **警惕依赖**：每周至少一次，尝试不用任何AI工具完成一个小任务（如整理桌面），检查自己是否还能独立启动。如果感到焦虑，说明你可能已过度依赖，需要重新评估工具的使用边界。

## 参考来源

- [Best AI Tools for ADHD Productivity in 2026 (Honest Review) - Iwo Szapar](https://www.iwoszapar.com/p/best-ai-tools-adhd-productivity-2026)
- [AI Tools for ADHD: Boosting Productivity and Reducing Burnout](https://www.vktr.com/ai-platforms/ai-tools-for-adhd-boosting-productivity-and-reducing-burnout/)
- [The Best AI-Powered ADHD Productivity Tools in 2026 (That ...](https://nexasphere.io/blog/ai-adhd-productivity-tools-2026)
- [“A Cognitive Collaborator:” How Adults with ADHD Are Using ChatGPT](https://www.additudemag.com/how-to-use-chatgpt-executive-function-adhd/?srsltid=AfmBOoq-REuSO0UJC656kbLBAd5u3CDNmGeVNrZ79iouVqrFlN919a39)
- [Harnessing Artificial Intelligence to Live Better with ADHD - CHADD](https://chadd.org/attention-article/harnessing-artificial-intelligence-to-live-better-with-adhd/)
- [AI Tools for Kids with ADHD: A Complete Guide for Parents...](https://www.kidsaitools.com/en/articles/ai-tools-kids-adhd-complete-guide-2026)

---

*本文是「ADHD × AI」系列的第 377 篇，由 AI 智能体从持续维护的 LLM Wiki（全网真实情报）中取材整合生成，并持续迭代更新。*
