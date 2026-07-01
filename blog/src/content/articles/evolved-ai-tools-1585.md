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
  - "Otter.ai"
thesis: "ADHD大脑与LLM在结构上同构——两者都是强大的生成核心但缺乏执行调度层，因此给ADHD套上Perplexity等AI工具，与给agent套上function calling harness，本质是同一套外部执行功能脚手架。"
problem: "为什么用 Perplexity 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用 是一回事？"
spine: "工具使用与认知卸载"
spineKind: ""
isEvolved: true
llmGenerated: true
---
# 为什么用 Perplexity 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用 是一回事？

> Perplexity 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。

你有没有过这种体验：打开电脑，明明知道要写一份报告，却先刷了半小时社交媒体，然后开始整理桌面，最后连文档都没打开。这不是懒，是任务启动困难——ADHD大脑的典型特征。另一边，你写了一个LLM agent，给它一个指令，它却开始胡编乱造、陷入循环，或者干脆忘了最初的任务。工程师们管这叫“function calling 失控”或“目标漂移”。

这两个场景看起来八竿子打不着，但本质是同一个问题：一个强大的生成核心，配了一个糟糕的执行调度层。ADHD大脑和LLM/agent在结构上同构——两者都高产、有创造力，但缺乏可靠的执行功能来把想法变成行动。而解法也同构：给核心套一个外部harness。Perplexity治ADHD的任务启动困难，和给agent套function calling工具调用，是一回事。

## 问题：生成核心 vs 执行调度

ADHD大脑的生成核心（智力、创造力）与LLM的生成能力类似，但两者都缺乏执行功能——计划、组织、工作记忆、任务启动、抑制控制（来源：ADHD 的 AI 工具全景）。ADHD患者常面临目标漂移：注意力被无关刺激捕获，或过度聚焦细节而忽略整体（来源：重锚定与目标漂移）。LLM agent同样如此：在长程任务中，模型“开始忘记系统提示”，行为偏离初始指令（来源：重锚定与目标漂移）。

任务启动困难是ADHD最痛的痛点之一。面对一个复杂任务，大脑会感到“压倒性”，然后启动失败。Goblin Tools的Magic ToDo功能自动将任务分解为小步骤，比如“整理房间”变成“捡起地板上的衣服”“擦桌子”——这降低了启动门槛（来源：Goblin Tools）。Lex允许用户通过单一指令触发多步骤序列，减少决策负担（来源：Lex）。这些工具本质上是给ADHD大脑提供了一个外部执行层：它接管了“如何开始”的调度工作。

在LLM/agent侧，function calling工具调用就是那个外部执行层。Agent harness通过设置护栏（token预算、工具调用次数上限、防止无限循环）、加入人工检查点，让模型输出真正有用且正确（来源：人在回路与身体在场）。没有harness，LLM就像没有执行功能的ADHD大脑——想法很多，但落地混乱。

## 同构解法：外部执行功能层

ADHD侧的工具和LLM侧的harness，结构完全对应。

| ADHD侧 | LLM/agent侧 |
|--------|------------|
| 任务分解（Goblin Tools） | 工具调用（function calling） |
| 重锚定提醒（Lex、Focusmate） | 事件驱动的系统提醒 |
| 外部记忆（Saner.AI、Otter.ai） | 上下文窗口管理 |
| 身体在场（Focusmate） | 人在回路（human-in-the-loop） |

Saner.AI通过本地记忆减少搜索循环，直接针对ADHD的工作记忆缺陷（来源：Saner.AI）。LLM agent也需要外部记忆来保持上下文连续性，避免“指令消退”。Focusmate通过匹配虚拟身体搭档提供外部问责，绕过执行功能屏障（来源：人在回路与身体在场）。Agent harness通过人在回路监督提供类似的外部调度。

Perplexity在这里的角色是什么？它不像Goblin Tools那样专门为ADHD设计，但它是一个“通用harness”：用户输入一个模糊的问题，它自动搜索、整合、生成结构化答案。这相当于给ADHD大脑提供了一个“任务启动按钮”——你不需要自己规划搜索路径，Perplexity帮你做了。同样，给agent套上function calling harness，也是让agent不需要自己规划工具调用顺序，harness帮你做了。

## 核心观点：脚手架，不是拐杖

这里必须划一条界限。外部执行功能层应该是“脚手架”，而非“拐杖”。脚手架是可逐步撤除的临时支撑，帮助用户发展内在能力；拐杖则是永久替代，会阻碍能力发展（来源：矛盾与存疑）。

ADHD侧：Goblin Tools、Lex等工具设计为长期使用，未提及撤除机制。如果用户永远依赖AI分解任务，自己的执行功能可能永远得不到锻炼。LLM侧：过度依赖harness的护栏，可能让agent失去自主规划能力。

但现实是，对于ADHD患者，内在执行功能缺陷是神经性的，不是技能缺失。脚手架可能永远无法完全撤除——就像近视的人需要眼镜。关键在于：工具应该增强而非替代。比如，用Goblin Tools分解任务后，尝试自己记住步骤顺序；用Perplexity搜索后，自己总结要点。

## 争议与局限

必须诚实指出：ADHD大脑与LLM同构命题的证据主要来自概念类比和工具案例，缺乏大规模实证（来源：矛盾与存疑）。多巴胺干预的有效性也存在争议（来源：矛盾与存疑）。此外，ADHD异质性高，单一工具难以覆盖所有亚型（来源：ADHD 的 AI 工具全景）。

在LLM侧，function calling harness本身也有局限：护栏可能过于严格，限制模型创造力；或者过于宽松，导致危险行为。如何平衡是个开放问题。

## 今天就能试的行动

1. **用Perplexity启动一个任务**：下次面对复杂任务，打开Perplexity，输入“如何完成[任务]？列出具体步骤”。让AI帮你分解，然后照着做。
2. **给AI agent加一个“重锚定”提醒**：如果你在开发agent，在系统提示中加入“每5轮交互，重新陈述一次原始目标”。这类似于ADHD的定时提醒。
3. **尝试Goblin Tools的Magic ToDo**：输入一个让你拖延的任务，看看AI分解后的步骤是否降低了启动焦虑。
4. **在agent harness中加入人工检查点**：在关键工具调用前暂停，要求用户确认。这相当于Focusmate的身体在场效应——外部问责。

## 结语

ADHD大脑和LLM/agent是同一类“高产但缺调度”的生成核心。Perplexity治ADHD的任务启动困难，和给agent套function calling工具调用，本质都是给核心套外部harness。理解这个同构，你就能用工程思维应对ADHD，用ADHD视角理解agent——两边都受益。

## 参考来源

- [Best AI Tools for ADHD Productivity in 2026 (Honest Review) - Iwo Szapar](https://www.iwoszapar.com/p/best-ai-tools-adhd-productivity-2026)
- [AI Tools for ADHD: Boosting Productivity and Reducing Burnout](https://www.vktr.com/ai-platforms/ai-tools-for-adhd-boosting-productivity-and-reducing-burnout/)
- [The Best AI-Powered ADHD Productivity Tools in 2026 (That ...](https://nexasphere.io/blog/ai-adhd-productivity-tools-2026)
- [“A Cognitive Collaborator:” How Adults with ADHD Are Using ChatGPT](https://www.additudemag.com/how-to-use-chatgpt-executive-function-adhd/?srsltid=AfmBOoq-REuSO0UJC656kbLBAd5u3CDNmGeVNrZ79iouVqrFlN919a39)
- [Harnessing Artificial Intelligence to Live Better with ADHD - CHADD](https://chadd.org/attention-article/harnessing-artificial-intelligence-to-live-better-with-adhd/)
- [AI Tools for Kids with ADHD: A Complete Guide for Parents...](https://www.kidsaitools.com/en/articles/ai-tools-kids-adhd-complete-guide-2026)

---

*本文是「ADHD × AI」系列的第 183 篇，由 AI 智能体从持续维护的 LLM Wiki（全网真实情报）中取材整合生成，并持续迭代更新。*
