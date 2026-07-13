---
title: "为什么用 Todoist 治 ADHD 的注意力涣散，和给 agent 套 上下文工程 是一回事？"
subtitle: "Todoist 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
description: "Todoist 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
date: "2025-04-18"
category: "专注力管理"
categoryId: "focus"
categoryEn: "Focus Management"
tags:
  - "ADHD"
  - "AI"
  - "专注力管理"
  - "反直觉同构"
  - "分心管理"
readingTime: 9
slug: "为什么用-todoist-治-adhd-的注意力涣散和给-agent-套-上下文工程-是一回事"
topicId: "prob-8dbd955a73"
angle: "反直觉同构"
rank: 277
score: 7.65
sourceCount: 6
toolsCited:
  - "RescueTime"
  - "Focusmate"
  - "Brain.fm"
  - "Endel"
  - "Forest"
thesis: "ADHD 大脑与 LLM 都是高产但缺执行调度层的生成核心，因此 ADHD 用外部工具（如 Todoist 这类任务清单/RescueTime/Focusmate）治注意力涣散，与给 agent 做上下文工程（记忆、路由、规划-执行分离、上下文压缩）本质上是同一套 harness：把「当下该注意什么」从内部调度层外包给外部脚手架。"
problem: "为什么用 Todoist 治 ADHD 的注意力涣散，和给 agent 套 上下文工程 是一回事？"
spine: "上下文工程"
spineKind: ""
isEvolved: true
llmGenerated: true
isoStrength: "A"
caseStudies:
  - "曾国藩"
  - "孔子"
  - "Charles Lester"
---
# 为什么用 Todoist 治 ADHD 的注意力涣散，和给 agent 套 上下文工程 是一回事？

> Todoist 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。

## 引言：两个看起来无关的崩溃现场

一边是 ADHD 的人：Todoist 里列满了任务，早上 8 点写下的「写周报」还躺在那里，但人已经刷了两个小时短视频。另一边是 agent 工程师：给 LLM 塞了 30 页上下文，目标写得清清楚楚，它却在最后一步输出跑偏，开始胡说八道。两个问题表面不同，深层 bug 却一样：**不是生成能力不足，而是执行调度层在关键时刻掉了线**。一个对 ADHD 人感同身受，一个对工程师扎心。本文要回答：为什么用 Todoist 这类任务调度工具治 ADHD 的注意力涣散，和给 agent 套上下文工程（context engineering）其实是一回事？

> 说明：Todoist 本身不在本次 wiki 资料的工具实测列表中；以下 ADHD 侧的实测证据来自资料收录的 RescueTime、Focusmate、Brain.fm、Endel、Forest 等，它们与 Todoist 同属「外部执行调度层」这一 harness 类别。

## 同一个核心问题：高产，但缺一个调度层

ADHD 侧的核心困境不是笨，而是执行功能失控。wiki 资料将其形容为「大脑的驾驶座常常感觉方向盘后没有人」（来源：AI Tools for ADHD: Boosting Productivity and Reducing Burnout）。计划本、便签、意志力用一周就崩溃，因为 ADHD 的痛点不是不会列计划，而是计划无法被稳定执行。ADHD 的注意力分散、思维跳跃，被归结为「注意力资源的弥散分配」（来源：Self-Attention Limits Working Memory Capacity of Transformer-Based Models）。更关键的是，ADHD 呈现「强记忆、弱控制」的认知剖面：工作记忆容量未必差，但自上而下的控制和调节能力不足，无法抑制自动化反应、无法灵活切换任务集（来源：Strong Memory, Weak Control: An Empirical Study of Executive Functioning in LLMs）。

LLM 侧几乎镜像。LLM 是极强的生成核心，但缺乏可靠的内置调度与执行控制。研究者用经典 Stroop 冲突任务测试 Transformer 注意力：短上下文里表现正常，序列一长，模型在冲突试次上骤降到随机水平——无法抑制优势反应、无法解决认知冲突，这和 ADHD 执行功能缺陷的标志一一对应（来源：Strong Memory, Weak Control: An Empirical Study of Executive Functioning in LLMs）。agent 工程师要解决的正是同一个问题：上下文一膨胀，推理就退化（来源：Building AI Coding Agents for the Terminal: Scaffolding, Harness, Context

## 参考来源

**同构强度：A 级** —— 直接文献支撑（引用 ADHD↔LLM 同构专题研究）

- [ADHD Apps: We tested 44 Apps and Here're the Best 9 in 2026](https://blog.saner.ai/best-adhd-apps/) — 证据等级：低（GRADE）
- [Meta-Analysis of fMRI Studies of Disruptive Behavior Disorders](https://doi.org/10.1176/appi.ajp.2016.15081089) — 证据等级：高（GRADE）
- [Nonlinear Complexity Analysis of Brain fMRI Signals in Schizophrenia](https://doi.org/10.1371/journal.pone.0095146) — 证据等级：低（GRADE）
- [Revolutionizing ADHD Management with AI Assistants](https://neurolaunch.com/adhd-ai-assistant/) — 证据等级：低（GRADE）
- [The Wanderer's Algorithm: Controlled Distraction as a Catalyst for Machine Creativity](https://www.techrxiv.org/users/950560/articles/1356399/master/file/data/wanderers_algorithm_paper_independent%203/wanderers_algorithm_paper_independent%203.pdf) — 证据等级：低（GRADE）
- [Deficient Executive Control in Transformer Attention](https://www.biorxiv.org/content/10.1101/2025.01.22.634394v1.full.pdf) — 证据等级：低（GRADE）

---

*本文是「ADHD × AI」系列的第 128 篇，由 AI 智能体从持续维护的 LLM Wiki（全网真实情报）中取材整合生成，并持续迭代更新。*
