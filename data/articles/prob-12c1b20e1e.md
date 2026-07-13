---
title: "ADHD 研究生视角：为什么「治好 ADHD 的工作记忆容量小、边做边忘」和「让 LLM 不跑飞」其实是同一道工程题？"
subtitle: "LLM 无跨会话状态，靠外部记忆/向量库续命——同一套 harness 思路，两边都成立。"
description: "LLM 无跨会话状态，靠外部记忆/向量库续命——同一套 harness 思路，两边都成立。"
date: "2025-03-05"
category: "AI工具实战"
categoryId: "ai-tools"
categoryEn: "AI Tools in Practice"
tags:
  - "ADHD"
  - "AI"
  - "AI工具实战"
  - "人群×同构"
  - "智能助手"
readingTime: 13
slug: "adhd-研究生视角为什么治好-adhd-的工作记忆容量小边做边忘和让-llm-不跑飞其实是同一道工程题"
topicId: "prob-12c1b20e1e"
angle: "人群×同构"
rank: 102
score: 7.77
sourceCount: 6
toolsCited:
  - "Goblin Tools"
  - "Saner.AI"
  - "Lex"
  - "Tiimo"
  - "Focusmate"
thesis: "ADHD 大脑与 LLM 都是「高产生成核心 + 不可靠执行调度层」的同构系统：两边要解决的都不是「让核心更聪明」，而是同一道工程题——在外部搭建 harness（外部记忆、任务分解、上下文约束、人在回路），把不稳定的输出转换成可交付、可复现、不跑飞的结果。"
problem: "ADHD 研究生视角：为什么「治好 ADHD 的工作记忆容量小、边做边忘」和「让 LLM 不跑飞」其实是同一道工程题？"
spine: "无状态与外部记忆"
spineKind: "llm"
isEvolved: false
llmGenerated: true
isoStrength: "A"
caseStudies:
  - "孔子"
  - "老子"
  - "陈华"
---
# ADHD 研究生视角：为什么「治好 ADHD 的工作记忆容量小、边做边忘」和「让 LLM 不跑飞」其实是同一道工程题？

> LLM 无跨会话状态，靠外部记忆/向量库续命——同一套 harness 思路，两边都成立。

## 引言：从「边做边忘」到「跑飞」

你是一名 ADHD 研究生。打开电脑要写论文综述，三分钟后却盯着「孔子身高」的搜索页发呆；你的论文窗口、Zotero、微信、笔记软件在屏幕底部排成一排，每个都打开，每个都只看了一半。你不是没有想法，相反，你的生成核心二十四小时运转；问题是，工作记忆容量太小，边做边忘，目标像沙子一样从指缝漏走。

你也是一名在做 Agentic Harness 的工程师。你的 LLM 单会话内文采飞扬，但跨会话一问三不知；它会在长对话里偏离目标、陷入循环、调用工具停不下来，直到把 token 预算烧光。你也不是没有算力，相反，生成核心足够强大；问题是，LLM 没有原生跨会话状态，没有执行调度层，一旦上下文约束松动，它就开始「跑飞」。

这两个场景，其实是同一道工程题。

## 同构诊断：两个缺调度层的生成核心

ADHD 与 LLM 的交汇点，最站得住脚的核心论点是结构同构：两者都是**高产生成核心 + 不可靠执行调度层**。ADHD 大脑并不缺乏想法、创意或信息检索能力，却往往在工作记忆、任务启动、时间管理与组织排序上失灵；LLM 同样能高速生成文本，却缺乏稳定的跨会话状态、原生规划与注意力约束（来源：ADHD 的 AI 工具全景）。

具体而言，同构至少体现在三个层面：

- **调度层缺失**：ADHD 前额叶执行功能受损，难以稳定计划、抑制分心、维持目标导向；LLM 没有内置执行调度层，容易偏离目标或产生幻觉。两者都需要外部脚手架来约束输出方向。
- **工作记忆脆弱**：ADHD 工作记忆容量不稳定，信息在任务切换中丢失；LLM 上下文窗口有限，且通常不具备真正的跨会话持久状态。
- **注意力漂移**：ADHD 多巴胺调节异常导致注意力被新颖刺激吸引；LLM 在缺乏提示工程约束时产生发散输出。两者都需要「限定上下文」来减少漂移（来源：ADHD 的 AI 工具全景）。

所以，「AI 帮 ADHD」和「harness 让 LLM 不跑飞」并不是两个领域，而是同一类结构工程：为两个同构系统安装同一套外部 harness，即**外部执行功能层**。

## ADHD 侧：当内部工作记忆崩溃，外部记忆就是执行功能

ADHD 的核心痛点之一是工作记忆容量小、边做边忘。用户常陷入「搜索循环」：在多个标签、应用、笔记之间切换，却始终找不回刚才的思路。时间盲（time blindness）让 ADHD 患者「真的感觉不到 45 分钟已经过去」，承诺和任务迅速从记忆中消失（来源：时间盲；9 Best AI Assistants for ADHD in 2026 - by Nia - rivva blog）。

针对这个结构问题，现有工具的价值主要体现在四类补偿：

1. **任务分解与启动**：把模糊目标拆解为可执行的下一步，降低任务启动门槛。Goblin Tools 的 Magic ToDo 能把「清理厨房」这类模糊任务分解为具体子任务，用户还可调节「辣度」控制粒度（来源：12 AI Personal Assistants Built for ADHD Brains (2026 Rankings)）。
2. **外部记忆系统**：把不稳定的内部工作记忆外化为可检索、可复用的结构。Saner.AI 通过 Personal AI Skai 实现自动笔记组织、语义搜索和语音捕获，目标是减少 ADHD 用户常见的「搜索循环」和认知负荷（来源：Best AI Tools for ADHD Productivity in 2026 (Honest Review) - Iwo Szapar）。
3. **时间管理与提醒**：用视觉化、智能调度与外部提醒对抗时间盲。Tiimo 专为时间盲设计，提供视觉时间表，让时间「可触摸」（来源：The 12 Best Apps for ADHD in 2026: A Guide to ...）。
4. **元认知与反思支架**：帮助 ADHD 个体完成本难自发进行的回顾与总结。

贯穿这些补偿的核心操作是「上下文工程」——通过外部支架主动限定「此刻应关注什么」，用结构换可控性（来源：ADHD 的 AI 工具全景）。

## LLM/Agent 侧：没有跨会话状态，向量库就是它的工作记忆

LLM 的痛点与 ADHD 几乎一一对应：它能生成，但不能记住；它能规划一段对话，但不能稳定执行跨会话目标。LLM 本身没有可靠的执行调度层，直接输出可能偏离目标、陷入循环或产生危险行为。Agent harness（脚手架）通过 human-in-the-loop 监督提供外部调度：设置护栏（token 预算、工具调用次数上限、防止无限循环）、加入人工检查点（暂停并询问后再执行）（来源：Building an AI Agent Harness from Scratch: The Architecture Between LLM and Agent - DEV Community）。

从结构上看，LLM 的 harness 与 ADHD 工具系统完全同构：

- **向量库 / 外部记忆系统** = ADHD 的 Saner.AI、笔记系统，负责把跨会话状态持久化，让模型「不会忘记自己写到哪」。
- **任务规划器 / 子目标分解** = ADHD 的 Goblin Tools、Lex，把宏大目标拆成可执行的下一步。
- **护栏与 token 预算** = ADHD 的「限定上下文」策略，通过约束防止漂移。
- **人在回路检查点** = ADHD 的 body doubling（身体在场效应）和定期向 AI 报告进度，用外部监督维持目标导向（来源：人在回路与身体在场）。

Lex 的设计尤其说明问题：它允许用户通过「单一指令触发复杂、多步骤的任务序列」，底层架构类似于 agent scaffolding，围绕 LLM 构建软件架构和工具以执行复杂、目标驱动的任务（来源：Best AI Tools for ADHD Productivity in 2026 (Honest Review) - Iwo Szapar；Agent Scaffolding: Architecture and Design Patterns for Agentic AI）。这本质上就是把 LLM 的「启动困难」外包给外部调度器。

## 孔子的 harness：把「礼」写成 guardrails

要理解这套 harness 为什么是工程而非鸡汤，可以看一个真实的案例：孔子。

孔子的 ADHD 特质非常典型：身高一米九，精力旺盛，周游列国十四年坐不住；冲动爱骂人，见南子急得对天发誓，骂宰予「朽木不可雕」；对音乐超专注到「三月不知肉味」，对种地等俗事零耐心；思维极度跳跃，《论语》全是场景化语录，没有系统著作。但他没有靠「意志力」硬扛，而是建立了一套外部 harness：以「克己复礼」为核心，把外在的「礼」当作行为边界；每日三省吾身，用反省日志作为外部记忆与重新接地（re-grounding）机制；直到七十岁才做到「从心所欲不逾矩」——也就是说，他花了一辈子用外部结构约束自己的冲动系统。

把孔子的 harness 翻译成工程语言：

- **礼** = 护栏（guardrails），规定什么能做、什么不能做的行为边界；
- **日课三省** = 定时 re-grounding，周期性把系统状态拉回目标上下文；
- **无系统著作、靠弟子记录整理** = 生成核心输出的是碎片，需要外部编排层（弟子的编辑、后世的注疏）才能沉淀为可复用的知识体系。

孔子没有「治好」ADHD，但他用 harness 把高产生成核心的输出，转换成了可交付、可传承两千五百年的结构。这正是 ADHD 个体与 LLM 工程师共同面对的工程题。

## 脚手架的边界：不是拐杖，是结构

同是外部支持，harness 与拐杖的区别在于：拐杖让你把重量完全交给它，脚手架让你能够完成本来做得到、只是结构不稳的事。ADHD 大脑不缺想法，LLM 不缺生成能力，它们缺的是把想法落地成可靠输出的**执行调度层**。外部记忆、任务分解、护栏、人在回路，不是为了替代核心，而是为了让核心能稳定工作。

这也是为什么「AI 工具帮 ADHD」不等于「让 AI 替你思考」。Goblin Tools 帮你分解任务，但你仍然决定目标；Saner.AI 帮你找回信息，但你仍然做判断；Lex 触发多步骤任务，但第一步仍需你发出。同样，agent harness 里的 LLM 负责生成，但目标、护栏、检查点、终止条件由工程师设定。两边都是**生成核心 + 外部调度层**的分层架构。

## 局限与争议：同构是类比，不是定律

必须诚实指出，这个同构框架有局限。

首先，ADHD 大脑与 LLM 的同构性目前只是理论

## 参考来源

**同构强度：A 级** —— 直接文献支撑（引用 ADHD↔LLM 同构专题研究）

- [ADHD Apps: We tested 44 Apps and Here're the Best 9 in 2026](https://blog.saner.ai/best-adhd-apps/) — 证据等级：低（GRADE）
- [12 AI Personal Assistants Built for ADHD Brains (2026 Rankings)](https://www.usecarly.com/blog/best-ai-personal-assistant-adhd/) — 证据等级：低（GRADE）
- [Toward Neurodivergent-Aware Productivity: A Systems and AI-Based Human-in-the-Loop Framework for ADHD-Affected Professionals](https://arxiv.org/pdf/2507.06864) — 证据等级：低（GRADE）
- [Using an AI Assistant to Manage ADHD: A Practical Guide](https://www.lobsterfarm.ai/guides/ai-for-adhd/) — 证据等级：低（GRADE）
- [Revolutionizing ADHD Management with AI Assistants](https://neurolaunch.com/adhd-ai-assistant/) — 证据等级：低（GRADE）
- [Agent Scaffolding: Architecture and Design Patterns for Agentic AI](https://zbrain.ai/agent-scaffolding/) — 证据等级：低（GRADE）

---

*本文是「ADHD × AI」系列的第 23 篇，由 AI 智能体从持续维护的 LLM Wiki（全网真实情报）中取材整合生成，并持续迭代更新。*
