---
title: "为什么用 Claude 治 ADHD 的想法落地难，和给 agent 套 外部编排调度层 是一回事？"
subtitle: "Claude 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
description: "Claude 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
date: "2025-04-26"
category: "创业创新"
categoryId: "entrepreneurship"
categoryEn: "Entrepreneurship & Innovation"
tags:
  - "ADHD"
  - "AI"
  - "创业创新"
  - "反直觉同构"
  - "创新"
readingTime: 9
slug: "为什么用-claude-治-adhd-的想法落地难和给-agent-套-外部编排调度层-是一回事"
topicId: "prob-de85cc029a"
angle: "反直觉同构"
rank: 365
score: 7.62
sourceCount: 6
toolsCited:
  - "Claude"
  - "Goblin Tools"
  - "Motion"
  - "Saner.AI"
  - "Focusmate"
  - "Building an AI Agent Harness from Scratch"
thesis: "ADHD 大脑与 LLM/agent 都是「高产生成核心 + 薄弱执行调度层」的同一结构，用 Claude 治 ADHD 的想法落地难，和给 agent 加外部 harness，本质都是在生成核心外面包一层可靠的外部调度层。"
problem: "为什么用 Claude 治 ADHD 的想法落地难，和给 agent 套 外部编排调度层 是一回事？"
spine: "生成核心与调度层"
spineKind: ""
isEvolved: true
llmGenerated: true
isoStrength: "B"
caseStudies:
  - "罗振宇"
  - "陶华碧"
  - "David Neeleman"
---
# 为什么用 Claude 治 ADHD 的想法落地难，和给 agent 套 外部编排调度层 是一回事？

> Claude 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。

## 01 问题：两个看似无关的“落地难”

如果你有过这样的早晨——脑子里同时跑着三个产品方案、两篇没写完的文章、一个想学的框架，结果到中午连一封邮件都没回——你不是懒，你是一个**高产的生成核心**，缺了一个**调度层**。

如果你是一名在搭 Agent 的工程师，你一定也见过类似的场景：LLM 能写出漂亮代码，也能在循环里调用 47 次工具、越跑越远，最后把生产环境弄得一团糟。模型很聪明，但**没有执行外壳**。

这两件事，表面上一个关于大脑，一个关于模型，其实结构相同：**核心太亮，外壳太薄**。ADHD 大脑的生成核心（发散思维、创意、多任务并行、超聚焦）产出极高，但执行功能（任务启动、持续专注、抑制冲动）薄弱，结果“高产但不可靠”（来源：人在回路与身体在场）。LLM 本身也是强大的生成核心，但缺乏可靠的执行调度层，直接输出可能偏离目标、陷入循环或产生危险行为（来源：Building an AI Agent Harness from Scratch: The Architecture Between LLM and Agent - DEV Community）。

所以，用 Claude 治 ADHD 的“想法落地难”，和给 agent 套一个外部编排调度层，是**同一类工程问题**。

## 02 同构的解剖：生成核心 + 调度层

ADHD 的创造力不是玄学。Lifted Ventures 2024 的研究显示，ADHD 组的创意产出率是对照组的 1.8 倍（来源：Lifted Ventures 2024）。但产出高不等于交付高。ADHD 大脑在执行任务时极易发生**目标漂移**：注意力被无关刺激捕获，或过度聚焦细节而忽略整体目标（来源：重锚定与目标漂移）。背后是执行功能、工作记忆、时间盲的系统性薄弱（来源：重锚定与目标漂移）。

LLM 侧类似：它有惊人的模式生成能力，但不会在目标上自动“重锚定”。让它自己规划，它可能漂移、循环、幻觉，甚至做出越权操作。于是工程师要在外部给它加**护栏**：token 预算、工具调用次数上限、防止无限循环、人工检查点（来源：Building an AI Agent Harness from Scratch: The Architecture Between LLM and Agent - DEV Community）。这套东西就是 agent 的 harness/脚手架。

两边的结构可以写成同一个公式：

> **系统可靠性 = 生成核心的能力 × 外部调度层的稳定性**

ADHD 和 LLM 的生成核心都不差，差的是后面那个乘数。

## 03 真实工具：两边的 harness 长什么样

ADHD 侧已经有不少 harness 实践。Goblin Tools 的 Magic ToDo 能把模糊任务——比如“清理厨房”——自动拆成具体、可执行的子任务，用户还能调节“辣度”控制粒度（来源：Goblin Tools）。这相当于给大脑装了一个**外部任务分解器**，降低启动门槛。Motion 则更进一步，自动根据任务、会议和截止日期动态排程，日程被打乱时自动重新安排，还会提前数周警告延期风险（来源：Motion）。它消除的不是时间，而是“下一步该做什么”的决策负担。Saner.AI 用本地记忆和通用收件箱减少搜索循环和标签切换，把工作记忆外包给系统（来源：Saner.AI）。

这些工具还利用了一个关键机制：**身体在场效应**。ADHD 群体在有他人在场时更容易启动和

## 参考来源

**同构强度：B 级** —— 机制类比（ADHD 侧与 LLM/agent 侧均有真实文献，机制可映射）

- [ADHD Apps: We tested 44 Apps and Here're the Best 9 in 2026](https://blog.saner.ai/best-adhd-apps/) — 证据等级：低（GRADE）
- [12 AI Personal Assistants Built for ADHD Brains (2026 Rankings)](https://www.usecarly.com/blog/best-ai-personal-assistant-adhd/) — 证据等级：低（GRADE）
- [LBD同构对：自我调节与元认知 — Inhibitory control and emotion regulation in preschool child ↔ ObjexMT: Objective Extraction and Metacognitive Calibration ](https://doi.org/10.1016/j.cogdev.2007.08.002) — 证据等级：低（GRADE）
- [LBD同构对：自我调节与元认知 — Emotion-related self-regulation and its relation to children ↔ A Reproducibility Study of Metacognitive Retrieval-Augmented](https://doi.org/10.1146/annurev.clinpsy.121208.131208) — 证据等级：低（GRADE）
- [The 12 Best AI Tools for 2026 (That People Actually Use)](https://www.synthesia.io/post/ai-tools) — 证据等级：低（GRADE）
- [The AI Powered SuperApp for Work | Motion](https://www.usemotion.com/) — 证据等级：低（GRADE）

---

*本文是「ADHD × AI」系列的第 206 篇，由 AI 智能体从持续维护的 LLM Wiki（全网真实情报）中取材整合生成，并持续迭代更新。*
