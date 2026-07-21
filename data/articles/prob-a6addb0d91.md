---
title: "Tiimo 之于 ADHD，就像 planner-executor 任务分解 之于 LLM——但有人用错了"
subtitle: "从同构视角实测 Tiimo：它到底补上了哪一层执行功能？"
description: "从同构视角实测 Tiimo：它到底补上了哪一层执行功能？"
date: "2025-04-01"
category: "时间管理"
categoryId: "time-mgmt"
categoryEn: "Time Management"
tags:
  - "ADHD"
  - "AI"
  - "时间管理"
  - "工具×同构"
  - "任务规划"
readingTime: 12
slug: "tiimo-之于-adhd就像-planner-executor-任务分解-之于-llm但有人用错了"
topicId: "prob-a6addb0d91"
angle: "工具×同构"
rank: 396
score: 7.15
sourceCount: 2
toolsCited:
  - "Motion"
  - "Tiimo"
  - "Structured"
  - "Todoist"
problem: "Tiimo 之于 ADHD，就像 planner-executor 任务分解 之于 LLM——但有人用错了"
spine: "规划循环与任务分解"
spineKind: "llm"
isEvolved: true
---
# Tiimo 之于 ADHD，就像 planner-executor 任务分解 之于 LLM——但有人用错了

> 从同构视角实测 Tiimo：它到底补上了哪一层执行功能？

先说一个事实：Clinical and psychoeducational data were analyzed for 119 children ages 8 to 16 years who were evaluated in a child diagnostic clinic。

如果你是 ADHD 人群，你大概率经历过——时间像握不住的沙，常常低估任务耗时、错过截止日期。这不是你不够努力，而是 ADHD 大脑的运作方式本就不同。而 AI 的出现，第一次让我们有机会用「外接」的方式补上这块短板。这篇文章不讲空话，只讲有据可查的工具、研究和可落地的方法。

## 为什么这件事对 ADHD 格外重要

ADHD 并不是「注意力不足」这么简单，它的核心是执行功能（executive function）的差异。具体来说，ADHD 大脑往往时间感知偏差（time blindness），难以估算时长。但与此同时，ADHD 也有自己的天赋：发散思维和联想能力强，擅长看到别人忽略的连接。

关键不在于「治好」ADHD，而在于用合适的外部系统补上短板、放大长处。AI 恰好擅长承接那些 ADHD 最吃力的部分——记住、组织、提醒、拆解、追踪。

## 最新研究怎么说

在动手之前，先看看证据。近年来 AI×ADHD 领域的研究进展很快：

- - **500%更可能**：有研究估计ADHD患者成为创业者的可能性高出500%（来源：ADHD科技行业深度研究）。
- 2023年12月发表的一篇学术论文《Challenges, Strengths, and Strategies of Software Engineers with ADHD: A Case Study》是首批专门针对ADHD软件工程师的质性研究。该研究通过对19名ADHD软件工程师的深度访谈，提取了15个挑战、8个优势和12个应对策略（来源：ADHD科技行业深度研究）。
- - **投资ADHD工具**：他的基金还投资了**Shelpful**——一个使用人类和AI帮助人们保持专注的创业公司，该产品被发现特别适合ADHD用户（来源：ADHD科技行业深度研究）。

这些研究的共同信号是：AI 在 ADHD 的评估、辅助和日常管理上正在从「概念」走向「可用」，但也要警惕被夸大的宣传——真正可靠的方案，往往是把 AI 当工具而非神药。

## 真实可用的 AI 工具

下面这些工具都是 ADHD 社区和评测中被反复推荐的，按它们最擅长的场景挑一两个上手即可，千万别一次性全装——那只会变成新的分心来源。

### Motion

Motion：AI 日历和任务管理工具，能根据优先级和截止日期自动排布你的一天，任务延误时自动重新规划。适用场景：解决 ADHD 的时间盲和过度承诺，让 AI 替你做日程决策。
### Tiimo

Tiimo：视觉化的日程与计划 App，专为神经多样性设计，用图标、颜色和倒计时让时间「看得见」。适用场景：对抗时间盲，把抽象的时间转化为视觉信号。
### Structured

Structured：可视化的每日时间线规划 App，把一天排成清晰的视觉时间轴。适用场景：让 ADHD 用户对一天的节奏有直观掌控感。
### Todoist

Todoist：任务管理 App，带自然语言输入和 AI 辅助功能。适用场景：快速捕捉待办，减少遗忘。

## 可以今天就试的策略

工具只是载体，方法才是关键。结合社区实践，这里有几条可操作的策略：

1. Executors in this architecture are instantiated per subtask, with stateless, single-use semantics beyond their input payload.
2. - Message Schemas: All inter-agent messages use compact, well-typed JSON schemas containing task IDs, subtask descriptions, input arguments, tool endpoints, and system prompts.
3. - Working-Memory Models: The planner maintains a persistent working-memory tree (or file), capturing the root goal, the decomposition hierarchy, individual subtask states, and back-pointers for stateful dependency management (Wang et al., 18 Sep 2025).
4. - Feedback-Driven Flow: Results produced by executors immediately update the planner's state, triggering progression to downstream subtasks.
5. So, we’re doing a deep dive into Chat GPT and how to use it to make your ADHD life easier.

建议只挑其中**一条**今天就开始，ADHD 大脑最怕「全部一起改」。

## 一个容易被忽略的提醒

AI 很强，但它不是替你做决定的人。对 ADHD 来说，最大的风险是「工具囤积」——不停地试新工具，却从没真正用起来任何一个。这本身就是一种拖延。

另外要理解一个概念：dopamine（多巴胺（与动机和奖励相关的神经递质，ADHD 大脑相对缺乏））。真正可持续的改变，是让 AI 嵌入你已有的习惯回路，而不是再造一套全新的系统。从最小、最痛的那个点开始，让 AI 帮你赢得第一个小胜利，多巴胺会带着你继续走下去。

## 写在最后

ADHD 不是你的缺陷，而是一套不同的操作系统。AI 也不是万能解药，它是一个强大的外接模块——当你学会正确地接上它，那些曾经让你精疲力竭的事，会变得轻一点。

记住：**开始不需要完美，只需要开始。** 选择这篇文章里最打动你的那一个方法，今天就试试看。

## 参考来源

- [Learning Disabilities and ADHD](https://doi.org/10.1177/002221940003300502) — 证据等级：低（GRADE）
- [NEUROPSYCHOLOGICAL MEASURES OF EXECUTIVE FUNCTION AND ANTISOCIAL BEHAVIOR: A META-ANALYSIS*](https://doi.org/10.1111/j.1745-9125.2011.00252.x) — 证据等级：高（GRADE）

---

*本文是「ADHD × AI」系列的第 228 篇，内容基于全网最新情报与研究自动整合生成，并持续迭代更新。*
