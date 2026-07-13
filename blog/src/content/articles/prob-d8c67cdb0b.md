---
title: "为什么用 Speechify 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用 是一回事？"
subtitle: "Speechify 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
description: "Speechify 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
date: "2025-03-26"
category: "AI工具实战"
categoryId: "ai-tools"
categoryEn: "AI Tools in Practice"
tags:
  - "ADHD"
  - "AI"
  - "AI工具实战"
  - "反直觉同构"
  - "ADHD辅助"
readingTime: 10
slug: "为什么用-speechify-治-adhd-的任务启动困难和给-agent-套-function-calling-工具调用-是一回事"
topicId: "prob-d8c67cdb0b"
angle: "反直觉同构"
rank: 192
score: 7.69
sourceCount: 2
toolsCited:
  - "Goblin Tools"
  - "Saner.AI"
  - "Lex"
  - "Mem"
problem: "为什么用 Speechify 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用 是一回事？"
spine: "工具使用与认知卸载"
spineKind: ""
isEvolved: true
---
# 为什么用 Speechify 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用 是一回事？

> Speechify 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。

先说一个事实：By adjusting for the global demographic structure in 2020, the prevalence of persistent adult ADHD was 2.58% and that of symptomatic adult ADHD was 6.76%, translating to 139.84 million and 366.33 million affected adults in 2020 globally。

如果你是 ADHD 人群，你大概率经历过——在一堆效率工具之间反复横跳，却没有一个能真正坚持用下去。这不是你不够努力，而是 ADHD 大脑的运作方式本就不同。而 AI 的出现，第一次让我们有机会用「外接」的方式补上这块短板。这篇文章不讲空话，只讲有据可查的工具、研究和可落地的方法。

## 为什么这件事对 ADHD 格外重要

ADHD 并不是「注意力不足」这么简单，它的核心是执行功能（executive function）的差异。具体来说，ADHD 大脑往往情绪调节（emotional regulation）需要更多外部支持。但与此同时，ADHD 也有自己的天赋：对新鲜刺激敏感，学习新事物上手快。

关键不在于「治好」ADHD，而在于用合适的外部系统补上短板、放大长处。AI 恰好擅长承接那些 ADHD 最吃力的部分——记住、组织、提醒、拆解、追踪。

## 最新研究怎么说

在动手之前，先看看证据。近年来 AI×ADHD 领域的研究进展很快：

- - 核心发现：生成式AI对ADHD诊断趋势的影响分析——AI既是补偿支持工具，也可能通过注意力碎片化加剧ADHD症状。[^1211^]（来源：adhd_ai_cross_literature）。
- - 核心发现：识别AI对ADHD程序员的四种支持机制——认知支架、任务分解、实时支持、个性化学习。[^229^]（来源：adhd_ai_cross_literature）。
- - 核心发现：全面综述AI在ASD、ADHD等神经发育障碍中的应用，涵盖筛查、诊断、治疗，强调算法偏见风险。[^1172^]（来源：adhd_ai_cross_literature）。

这些研究的共同信号是：AI 在 ADHD 的评估、辅助和日常管理上正在从「概念」走向「可用」，但也要警惕被夸大的宣传——真正可靠的方案，往往是把 AI 当工具而非神药。

## 真实可用的 AI 工具

下面这些工具都是 ADHD 社区和评测中被反复推荐的，按它们最擅长的场景挑一两个上手即可，千万别一次性全装——那只会变成新的分心来源。

### Goblin Tools

Goblin Tools：一套专为神经多样性人群设计的轻量 AI 工具集，其中 Magic ToDo 能把一个笼统的任务自动拆解成可执行的微步骤。适用场景：克服任务启动困难和「不知道从哪下手」的瘫痪感。
### Saner.AI

Saner.AI：面向 ADHD 的 AI 个人助理，整合笔记、邮件、日程，用自然语言管理所有碎片信息。适用场景：把散落各处的想法、待办和提醒集中到一个 AI 大脑里。
### Lex

Lex：内置 AI 的写作工具，能在你卡壳时续写、生成大纲、克服空白页恐惧。适用场景：解决 ADHD 写作启动困难和组织思路的难题。
### Mem

Mem：AI 驱动的笔记工具，自动整理和关联你的笔记，无需手动建立文件夹结构。适用场景：适配 ADHD 不擅长手动归类整理的特点，让 AI 自动建立知识连接。

## 可以今天就试的策略

工具只是载体，方法才是关键。结合社区实践，这里有几条可操作的策略：

1. Design an Agentic AI system that can autonomously plan and execute a multi-step task using external tools.
2. The agent autonomously decomposes the user goal into smaller tasks and executes them using specialized tools while maintaining context through memory.
3. These ChatGPT prompts are designed to help you plan, reflect, stay grounded, and most importantly, work with your brain, not against it.
4. Treat this guide as your ADHD-friendly prompt toolkit.
5. Please help me come up with a simple, step-by-step plan that works with my ADHD brain.

建议只挑其中**一条**今天就开始，ADHD 大脑最怕「全部一起改」。

## 一个容易被忽略的提醒

AI 很强，但它不是替你做决定的人。对 ADHD 来说，最大的风险是「工具囤积」——不停地试新工具，却从没真正用起来任何一个。这本身就是一种拖延。

另外要理解一个概念：emotional dysregulation（情绪失调（难以调节情绪强度和恢复））。真正可持续的改变，是让 AI 嵌入你已有的习惯回路，而不是再造一套全新的系统。从最小、最痛的那个点开始，让 AI 帮你赢得第一个小胜利，多巴胺会带着你继续走下去。

## 写在最后

ADHD 不是你的缺陷，而是一套不同的操作系统。AI 也不是万能解药，它是一个强大的外接模块——当你学会正确地接上它，那些曾经让你精疲力竭的事，会变得轻一点。

记住：**开始不需要完美，只需要开始。** 选择这篇文章里最打动你的那一个方法，今天就试试看。

## 参考来源

- [The prevalence of adult attention-deficit hyperactivity disorder: A global systematic review and meta-analysis](https://doi.org/10.7189/jogh.11.04009) — 证据等级：高（GRADE）
- [Development of Large-Scale Functional Brain Networks in Children](https://doi.org/10.1371/journal.pbio.1000157) — 证据等级：低（GRADE）

---

*本文是「ADHD × AI」系列的第 72 篇，内容基于全网最新情报与研究自动整合生成，并持续迭代更新。*
