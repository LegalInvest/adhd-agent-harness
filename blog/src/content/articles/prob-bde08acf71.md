---
title: "ADHD 家长视角：为什么「治好 ADHD 的工作记忆容量小、边做边忘」和「让 LLM 不跑飞」其实是同一道工程题？"
subtitle: "LLM 无跨会话状态，靠外部记忆/向量库续命——同一套 harness 思路，两边都成立。"
description: "LLM 无跨会话状态，靠外部记忆/向量库续命——同一套 harness 思路，两边都成立。"
date: "2025-05-09"
category: "AI工具实战"
categoryId: "ai-tools"
categoryEn: "AI Tools in Practice"
tags:
  - "ADHD"
  - "AI"
  - "AI工具实战"
  - "人群×同构"
  - "智能助手"
readingTime: 14
slug: "adhd-家长视角为什么治好-adhd-的工作记忆容量小边做边忘和让-llm-不跑飞其实是同一道工程题"
topicId: "prob-bde08acf71"
angle: "人群×同构"
rank: 100
score: 7.77
sourceCount: 6
toolsCited:
  - "Goblin Tools"
  - "Lex"
  - "Saner.AI"
  - "Motion"
  - "Reclaim.ai"
thesis: "ADHD 大脑与 LLM 都是「高产生成核心 + 不可靠执行调度层」：补偿工作记忆不足和防止 LLM 跑飞，本质上是同一套外部 harness——外部记忆、任务分解与重锚定系统——的安装工程。"
problem: "ADHD 家长视角：为什么「治好 ADHD 的工作记忆容量小、边做边忘」和「让 LLM 不跑飞」其实是同一道工程题？"
spine: "无状态与外部记忆"
spineKind: "llm"
isEvolved: false
llmGenerated: true
isoStrength: "B"
caseStudies:
  - "孔子"
  - "曾国藩"
  - "蒋燕"
---
# ADHD 家长视角：为什么「治好 ADHD 的工作记忆容量小、边做边忘」和「让 LLM 不跑飞」其实是同一道工程题？

> LLM 无跨会话状态，靠外部记忆/向量库续命——同一套 harness 思路，两边都成立。

## 引言：两个“掉链子”的瞬间

作为家长，我太熟悉这个场景：让 ADHD 孩子去收拾房间，他答应得好好的，五分钟后却蹲在地板上研究一只死蚊子。不是他故意，是他的工作记忆在任务切换中“掉线”了——目标、步骤、截止条件，像没保存的文档一样丢失。而坐在电脑前做 Agentic Harness 的工程师，大概也熟悉另一个场景：LLM 前几句还围绕着你的目标，聊到第三四轮就突然提出要加一个根本不存在的 API，把之前的约束忘得一干二净。一个是孩子“边做边忘”，一个是模型“无跨会话状态”，两者看起来风马牛不相及，但解法却惊人地一致：给生成核心装一个外部执行调度层。

## 同一类系统：高产生成核心 + 缺执行调度层

ADHD 大脑的痛处不是“没想法”，而是执行功能不稳定。前额叶调度层受损，导致工作记忆容量有限、目标容易漂移、计划难以持续（来源：ADHD 的 AI 工具全景）。LLM 的痛处也不是“没知识”，而是它本质上是一个无跨会话状态、靠上下文窗口续命的生成核心，缺乏原生规划、目标维持与注意力约束，容易在对话中偏离目标或产生幻觉（来源：ADHD 大脑与 LLM 的同构；生成核心与调度层）。因此，两者可以看作同一种结构：一个高产生成核心，加上一个不可靠的执行调度层。想让它们稳定输出，不能指望核心自愈，只能在外部加 harness（来源：外部执行功能层）。

## 外部记忆与规划：同一套 harness

两边需要的外部结构是同构的：把不稳定的工作记忆外化为可检索、可复用的结构，并通过上下文工程主动限定“此刻该关注什么”（来源：上下文工程；ADHD 的 AI 工具全景）。在 ADHD 侧，Goblin Tools 的 Magic ToDo 能把“清理厨房”这种模糊任务拆成可执行的子任务，用“辣度”调节粒度，降低启动门槛（来源：Gob

## 参考来源

**同构强度：B 级** —— 机制类比（ADHD 侧与 LLM/agent 侧均有真实文献，机制可映射）

- [ADHD Apps: We tested 44 Apps and Here're the Best 9 in 2026](https://blog.saner.ai/best-adhd-apps/) — 证据等级：低（GRADE）
- [12 AI Personal Assistants Built for ADHD Brains (2026 Rankings)](https://www.usecarly.com/blog/best-ai-personal-assistant-adhd/) — 证据等级：低（GRADE）
- [LBD同构对：任务分解与规划 — Attention-deficit/hyperactivity disorder is characterized by ↔ Language-conditioned world model improves policy generalizat](https://doi.org/10.1073/pnas.0707741104) — 证据等级：低（GRADE）
- [LBD同构对：任务分解与规划 — Safety and recommendations for TMS use in healthy subjects a ↔ AgentGen: Enhancing Planning Abilities for Large Language Mo](https://doi.org/10.1016/j.clinph.2020.10.003) — 证据等级：低（GRADE）
- [LBD同构对：任务分解与规划 — How specific are executive functioning deficits in attention ↔ AMAP Agentic Planning Technical Report](https://doi.org/10.1111/j.1469-7610.2004.00276.x) — 证据等级：低（GRADE）
- [The AI Powered SuperApp for Work | Motion](https://www.usemotion.com/) — 证据等级：低（GRADE）

---

*本文是「ADHD × AI」系列的第 21 篇，由 AI 智能体从持续维护的 LLM Wiki（全网真实情报）中取材整合生成，并持续迭代更新。*
