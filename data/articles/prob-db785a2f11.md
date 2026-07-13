---
title: "为什么用 Inflow 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用 是一回事？"
subtitle: "Inflow 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
description: "Inflow 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
date: "2025-03-22"
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
slug: "为什么用-inflow-治-adhd-的任务启动困难和给-agent-套-function-calling-工具调用-是一回事"
topicId: "prob-db785a2f11"
angle: "反直觉同构"
rank: 187
score: 7.69
sourceCount: 2
toolsCited:
  - "Goblin Tools"
  - "Saner.AI"
  - "Lex"
  - "Mem"
problem: "为什么用 Inflow 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用 是一回事？"
spine: "工具使用与认知卸载"
spineKind: ""
isEvolved: true
---
# 为什么用 Inflow 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用 是一回事？

> Inflow 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。

先说一个事实：MBT appears to be more effective than TAU at reducing self-harm (RR 0.62, 95% CI 0.49 to 0.80; 3 trials, 252 participants), suicidality (RR 0.10, 95% CI 0.04, 0.30, 3 trials, 218 participants) and depression (SMD -0.58, 95% CI -1.22 to 0.05, 4 trials, 333 participants)。

如果你是 ADHD 人群，你大概率经历过——在一堆效率工具之间反复横跳，却没有一个能真正坚持用下去。这不是你不够努力，而是 ADHD 大脑的运作方式本就不同。而 AI 的出现，第一次让我们有机会用「外接」的方式补上这块短板。这篇文章不讲空话，只讲有据可查的工具、研究和可落地的方法。

## 为什么这件事对 ADHD 格外重要

ADHD 并不是「注意力不足」这么简单，它的核心是执行功能（executive function）的差异。具体来说，ADHD 大脑往往时间感知偏差（time blindness），难以估算时长。但与此同时，ADHD 也有自己的天赋：发散思维和联想能力强，擅长看到别人忽略的连接。

关键不在于「治好」ADHD，而在于用合适的外部系统补上短板、放大长处。AI 恰好擅长承接那些 ADHD 最吃力的部分——记住、组织、提醒、拆解、追踪。

## 最新研究怎么说

在动手之前，先看看证据。近年来 AI×ADHD 领域的研究进展很快：

- - 核心发现：将ChatGPT-4 Turbo和Claude-3 Opus集成到机器人助手中用于ADHD治疗，ChatGPT在性能响应上更优，Claude在伦理考虑上更强。[^1205^]（来源：adhd_ai_cross_literature）。
- - 核心发现：Sincrolab Adults AI认知刺激项目RCT，104名成人ADHD，12周干预，使用MOXO CPT、ASRS、AAQoL评估。[^1209^]（来源：adhd_ai_cross_literature）。
- - 核心发现：153名ADHD幼儿随机分组，AI聊天机器人引导的共享阅读（SBR-AI）在表达性词汇、识字和句法上显著优于对照组。[^1218^]（来源：adhd_ai_cross_literature）。

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

1. - Example prompt: "I want to establish a daily routine to help manage my ADHD.
2. Chatbot prompts, such as those offered by OpenAI's ChatGPT, can provide invaluable support and guidance in areas like prioritization, time management, overcoming procrastination, and more.
3. By utilizing these prompts, those with ADHD can better navigate their daily tasks and ultimately improve their overall well-being.
4. Message schemas between agents are typically concise JSON packets containing task IDs, tool descriptions, input payloads, and result metadata.
5. Decomposition considers tool registry inspection, input/output contract formation, format constraints, and, in some systems, explicit verification predicates and behavioral checks for each node in the decomposition graph (Xu et al., 24 May 2026).

建议只挑其中**一条**今天就开始，ADHD 大脑最怕「全部一起改」。

## 一个容易被忽略的提醒

AI 很强，但它不是替你做决定的人。对 ADHD 来说，最大的风险是「工具囤积」——不停地试新工具，却从没真正用起来任何一个。这本身就是一种拖延。

另外要理解一个概念：time blindness（时间盲（难以感知时间流逝和估算时长））。真正可持续的改变，是让 AI 嵌入你已有的习惯回路，而不是再造一套全新的系统。从最小、最痛的那个点开始，让 AI 帮你赢得第一个小胜利，多巴胺会带着你继续走下去。

## 写在最后

ADHD 不是你的缺陷，而是一套不同的操作系统。AI 也不是万能解药，它是一个强大的外接模块——当你学会正确地接上它，那些曾经让你精疲力竭的事，会变得轻一点。

记住：**开始不需要完美，只需要开始。** 选择这篇文章里最打动你的那一个方法，今天就试试看。

## 参考来源

- [Psychological therapies for people with borderline personality disorder](https://doi.org/10.1002/14651858.cd005652.pub2) — 证据等级：低（GRADE）
- [Subcortical brain volume differences in participants with attention deficit hyperactivity disorder in children and adults: a cross-sectional mega-analysis](https://doi.org/10.1016/s2215-0366(17)30049-4) — 证据等级：低（GRADE）

---

*本文是「ADHD × AI」系列的第 67 篇，内容基于全网最新情报与研究自动整合生成，并持续迭代更新。*
