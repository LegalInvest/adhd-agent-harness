---
title: "为什么用 Saner.AI 治 ADHD 的注意力涣散，和给 agent 套 上下文工程 是一回事？"
subtitle: "Saner.AI 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
description: "Saner.AI 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
date: "2025-05-17"
category: "专注力管理"
categoryId: "focus"
categoryEn: "Focus Management"
tags:
  - "ADHD"
  - "AI"
  - "专注力管理"
  - "反直觉同构"
  - "专注力"
readingTime: 10
slug: "为什么用-sanerai-治-adhd-的注意力涣散和给-agent-套-上下文工程-是一回事"
topicId: "prob-2627c6ebc3"
angle: "反直觉同构"
rank: 266
score: 7.65
sourceCount: 6
toolsCited:
  - "Saner.AI"
  - "Brain.fm"
  - "Focusmate"
  - "RescueTime"
  - "Forest"
  - "Endel"
thesis: "ADHD 大脑与 LLM/agent 都是「高产但缺执行调度层的生成核心」，因此都需要用上下文工程（context engineering）在外部搭建一个 harness/脚手架，把工作记忆不稳定、注意力弥散和任务启动困难转化为可控的目标导向行为。"
problem: "为什么用 Saner.AI 治 ADHD 的注意力涣散，和给 agent 套 上下文工程 是一回事？"
spine: "上下文工程"
spineKind: ""
isEvolved: true
llmGenerated: true
isoStrength: "A"
caseStudies:
  - "曾国藩"
  - "文天祥"
  - "Brian Gregory"
---
# 为什么用 Saner.AI 治 ADHD 的注意力涣散，和给 agent 套 上下文工程 是一回事？

> Saner.AI 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。

## 你熟悉的两个场景

早上九点，你坐在桌前准备写一份方案。二十分钟后，你在回消息；四十分钟后，你在查一个完全无关的知识点；一小时后，你盯着屏幕，完全忘了最初要干什么。你不缺想法，也不缺能力，缺的是把念头稳住的能力。

如果你做 Agent 或 LLM 工程，这个画面应该似曾相识。模型上下文一长，关键指令被后面的话淹没，输出就开始「自说自话」——推理还在进行，但目标已经漂移。你调 prompt、做 RAG、压缩上下文，本质上是在做同一件事：防止核心被噪声带偏。

为什么 ADHD 大脑与 LLM 会掉同一个坑？答案藏在同一个结构里：它们都是**高产但缺执行调度层的生成核心**。

## 一、核心同构：强记忆、弱控制、注意力弥散

ADHD 常被描述为执行功能障碍，而工作记忆是最关键的瓶颈。患者大脑能生成大量想法，却很难把「现在该注意什么」稳定地保持在意识中（来源：Outsourcing Executive Function with AI — Hacking Your ADHD）。

大语言模型也出现了几乎相同的剖面。明尼苏达大学的研究者测试 LLM 的执行功能，发现它们呈现**「强记忆、弱控制」**：工作记忆容量甚至超过常人，但认知灵活性与注意控制存在核心缺陷，无法灵活切换任务集，也无法抑制自动化反应——这正是 ADHD 的经典神经心理模式（来源：Strong Memory, Weak Control: An Empirical Study of Executive Functioning in LLMs）。

耶鲁大学更进一步指出，自注意力机制本身就会导致工作记忆容量限制：随着任务中需要保持的项目增加，注意力分数熵增、注意力弥散、表现下降，与人类 ADHD 的注意力分散机制同源（来源：Self-Attention Limits Working Memory Capacity of Transformer-Based Models）。

换句话说，**两边的瓶颈都不在「算力」或「创造力」，而在调度层（orchestration）**：谁来决定此刻注意什么、记住什么、先做什么。

## 二、上下文工程：给注意力做一套 harness

Agent 侧的上下文工程，通俗说就是：通过 system prompt、上下文窗口管理、外部记忆、检索和反馈机制，让模型在正确的时间看到正确的信息，避免被无关 token 淹没。

ADHD 侧也需要同样的工程。它不再依赖「靠意志力硬撑」，而是把环境、工具和社会结构变成外部执行功能层：

- **外部记忆**：RescueTime 自动记录时间流向，减少工作记忆负担；Forest 用游戏化记录把专注可视化，帮你对抗「时间盲」（来源：Revolutionizing ADHD Management with AI Assistants；ADHD Apps: We tested 44 Apps and Here're the Best 9 in 2026）。
- **注意力过滤**：Brain.fm 用 AI 生成经神经锁相设计的音乐，改变大脑信息处理方式；Endel 用 AI 生成个性化声音环境，帮助人在特定状态里停留（来源：11 Best ADHD Productivity Apps for Fluctuating Energy；AI 与 ADHD 的专注力）。
- **身体在场与问责**：Focusmate 通过虚拟身体在场（Body Doubling）提供外部启动压力，弥补多巴胺调节不足和执行功能缺陷（来源：ADHD科技行业深度研究；11 Best ADHD Productivity Apps for Fluctuating Energy）。
- **低摩擦脚手架**：与强调阻断的工具相比，Saner.AI 被定位为更温和、低摩擦的提醒系统，进入 2026 年 ADHD 应用最佳 9 款榜单（来源：ADHD Apps: We tested 44 Apps and Here're the Best 9 in 2026；RescueTime）。

这套设计的核心不是「让人更努力」，而是**把「该注意什么」这件事从大脑内部搬到外部系统里去管理**。这正是上下文工程的定义：主动设计当下注意什么。

## 三、曾国藩的「日课十二条」：古人的 system prompt

晚清名臣曾国藩年轻时极像典型 ADHD 注意力涣散型：坐不住，爱串门、喝酒、看热闹，读书「他人目下二三行，余或疾读不能终一行」，情绪大起大落，还常因银屑病和挫败感崩溃。他后半生的

## 参考来源

**同构强度：A 级** —— 直接文献支撑（引用 ADHD↔LLM 同构专题研究）

- [ADHD Apps: We tested 44 Apps and Here're the Best 9 in 2026](https://blog.saner.ai/best-adhd-apps/) — 证据等级：低（GRADE）
- [Meta-Analysis of fMRI Studies of Disruptive Behavior Disorders](https://doi.org/10.1176/appi.ajp.2016.15081089) — 证据等级：高（GRADE）
- [Nonlinear Complexity Analysis of Brain fMRI Signals in Schizophrenia](https://doi.org/10.1371/journal.pone.0095146) — 证据等级：低（GRADE）
- [Revolutionizing ADHD Management with AI Assistants](https://neurolaunch.com/adhd-ai-assistant/) — 证据等级：低（GRADE）
- [Strong Memory, Weak Control: An Empirical Study of Executive Functioning in LLMs](https://preview.aclanthology.org/evt-to-venues/2026.eacl-long.281.pdf) — 证据等级：低（GRADE）
- [Self-Attention Limits Working Memory Capacity of Transformer-Based Models](https://arxiv.org/pdf/2409.10715) — 证据等级：低（GRADE）

---

*本文是「ADHD × AI」系列的第 117 篇，由 AI 智能体从持续维护的 LLM Wiki（全网真实情报）中取材整合生成，并持续迭代更新。*
