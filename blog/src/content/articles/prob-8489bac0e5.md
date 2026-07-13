---
title: "为什么用 Saner.AI 治 ADHD 的时间盲，和给 agent 套 planner-executor 任务分解 是一回事？"
subtitle: "Saner.AI 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
description: "Saner.AI 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
date: "2025-05-30"
category: "时间管理"
categoryId: "time-mgmt"
categoryEn: "Time Management"
tags:
  - "ADHD"
  - "AI"
  - "时间管理"
  - "反直觉同构"
  - "日程安排"
readingTime: 7
slug: "为什么用-sanerai-治-adhd-的时间盲和给-agent-套-planner-executor-任务分解-是一回事"
topicId: "prob-8489bac0e5"
angle: "反直觉同构"
rank: 284
score: 7.65
sourceCount: 6
toolsCited:
  - "Saner.AI"
  - "Tiimo"
  - "Motion"
  - "Reclaim.ai"
  - "Goblin Tools"
  - "Todoist"
thesis: "ADHD 大脑与 LLM 都是高产能的生成核心，却因为缺少可靠的内部执行调度层而同样受困于时间盲与计划脱轨；给它们外部化的 planner-executor harness（如 Saner.AI 与 agentic scaffolding）并非让它们变‘正常’，而是把调度功能从内部搬到外部，让生成核心能在被限定的上下文里稳定运行。"
problem: "为什么用 Saner.AI 治 ADHD 的时间盲，和给 agent 套 planner-executor 任务分解 是一回事？"
spine: "规划循环与任务分解"
spineKind: ""
isEvolved: true
llmGenerated: true
isoStrength: "B"
caseStudies:
  - "孔子"
  - "徐渭徐文长"
  - "胡飞"
---
# 为什么用 Saner.AI 治 ADHD 的时间盲，和给 agent 套 planner-executor 任务分解 是一回事？

> Saner.AI 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。

如果你早上睁眼，明明事情堆成山，却像“时间是一片雾”一样不知道先抓哪一件；而当你写 Agent 时，发现 LLM 能写代码、写报告，却隔三句就忘记最初要干嘛——这两种崩溃，其实是同一个bug的不同界面。

本文要回答：为什么用 Saner.AI 帮助 ADHD 应对时间盲，和给大模型套上 planner-executor 任务分解，是同一件事？答案不在“AI 有多聪明”，而在“生成核心缺了一个外部调度层”。

## 01 同构：高产但缺执行调度层

ADHD 的大脑并不缺想法。研究表明，ADHD 的核心困难在于执行功能——尤其是计划、组织与任务分解，而非单纯的注意力不足（来源：How specific are executive functioning deficits in attention ↔ AMAP Agentic Planning Technical Report）。Swanson 的文献映射也发现，ADHD 文献群与 agentic harness 文献群都把“任务分解与规划”作为核心机制概念，ADHD 一侧命中 681 篇，agent 一侧命中 2914 篇（来源：LBD同构对：任务分解与规划 — Attention-deficit/hyperactivity disorder is characterized by ↔ Language-conditioned world model improves policy generalization）。

LLM 也一样。它能生成高质量文本，却没有跨会话的持久状态、可靠的目标维持与多步调度能力。Agent scaffolding 文献的共识是：单个 LLM 不足以可靠完成多步骤任务、与业务工具交互或适应领域特定逻辑（来源：Agent Scaffolding: Architecture and Design Patterns for Agentic AI）。

所以两者同构在结构，而非症状：ADHD 大脑和 LLM 都是高产生成核心，都缺一个能持续问“此刻该做什么、做到哪了、下一步怎么调整”的外部执行调度层。这就像一个强力引擎没有方向盘和仪表盘，harness 不是替换引擎，而是把驾驶座装上去。

## 02 ADHD 侧的真实证据：时间盲、启动难与外部化

ADHD 的“时间盲”不是没看表，而是内部时间感知无法把抽象未来变成可操作的现在。应对它的工程思路，是把时间、任务和优先级从大脑里搬出来，变成可见、可触、可自动维护的外部结构。

- **Tiimo** 用视觉日程、颜色块和动态时间流把抽象时间“实体化”，让时间从雾变成图形（来源：The 12 Best Apps for ADHD in 2026: A Guide to Finding What ...）。
- **Motion** 自动根据任务优先级、截止日期和可用时间重建每日计划，并在任务可能逾期前提前数天警告，直接卸载“下一步该做什么”的决策负担（来源：The AI Powered SuperApp for Work | Motion）。
- **Reclaim.ai** 不强调“填满日程”，而是主动保护深度工作与习惯时间块，减少会议入侵导致的

## 参考来源

**同构强度：B 级** —— 机制类比（ADHD 侧与 LLM/agent 侧均有真实文献，机制可映射）

- [LBD同构对：自我调节与元认知 — Inhibitory control and emotion regulation in preschool child ↔ ObjexMT: Objective Extraction and Metacognitive Calibration ](https://doi.org/10.1016/j.cogdev.2007.08.002) — 证据等级：低（GRADE）
- [LBD同构对：自我调节与元认知 — Emotion-related self-regulation and its relation to children ↔ A Reproducibility Study of Metacognitive Retrieval-Augmented](https://doi.org/10.1146/annurev.clinpsy.121208.131208) — 证据等级：低（GRADE）
- [The 12 Best AI Tools for 2026 (That People Actually Use)](https://www.synthesia.io/post/ai-tools) — 证据等级：低（GRADE）
- [The AI Powered SuperApp for Work | Motion](https://www.usemotion.com/) — 证据等级：低（GRADE）
- [11 Best ADHD Productivity Apps for Fluctuating Energy - rivva blog](https://blog.rivva.app/p/11-best-adhd-productivity-apps-for) — 证据等级：低（GRADE）
- [ADHD Apps: We tested 44 Apps and Here're the Best 9 in 2026](https://blog.saner.ai/best-adhd-apps/) — 证据等级：低（GRADE）

---

*本文是「ADHD × AI」系列的第 135 篇，由 AI 智能体从持续维护的 LLM Wiki（全网真实情报）中取材整合生成，并持续迭代更新。*
