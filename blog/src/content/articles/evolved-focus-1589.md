---
title: "为什么用 Motion 治 ADHD 的注意力涣散，和给 agent 套 上下文工程 是一回事？"
subtitle: "Motion 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
description: "Motion 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
date: "2025-04-15"
category: "专注力管理"
categoryId: "focus"
categoryEn: "Focus Management"
tags:
  - "ADHD"
  - "AI"
  - "专注力管理"
  - "反直觉同构"
  - "深度工作"
readingTime: 12
slug: "为什么用-motion-治-adhd-的注意力涣散和给-agent-套-上下文工程-是一回事"
topicId: "evolved-focus-1589"
angle: "反直觉同构"
rank: 287
score: 7.68
sourceCount: 6
toolsCited:
  - "Motion"
  - "Focusmate"
  - "RescueTime"
  - "Brain.fm"
thesis: "ADHD 大脑与 LLM 是同一类“高产但缺执行调度层的生成核心”，因此 Motion 治 ADHD 的注意力涣散与给 agent 套上下文工程本质相同——都是通过外部 harness 补偿调度缺陷，而非修复核心。"
problem: "为什么用 Motion 治 ADHD 的注意力涣散，和给 agent 套 上下文工程 是一回事？"
spine: "上下文工程"
spineKind: ""
isEvolved: true
llmGenerated: true
caseStudies:
  - "曾国藩"
  - "释迦牟尼"
  - "Robert Pearson"
---
# 为什么用 Motion 治 ADHD 的注意力涣散，和给 agent 套 上下文工程 是一回事？

> Motion 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。

## 问题：为什么你越需要“专注”，就越专注不了？

如果你有 ADHD，一定熟悉这个场景：打开电脑，准备写报告，然后——刷了半小时社交媒体，又去查了“如何提高专注力”，最后发现自己坐在桌前，什么都没干。这不是意志力问题，是你的大脑天生缺了一个“调度层”。

如果你是 LLM/Agent 工程师，也一定熟悉这个场景：给 agent 一个复杂任务，它开始自由发挥，上下文越滚越长，最终输出偏离轨道，或者陷入循环。你不是没给模型，而是没给“上下文工程”。

这两个问题，本质上是同一个问题。ADHD 大脑与 LLM 在结构上同构：两者都是**高产但缺乏可靠执行调度层的生成核心**（来源：AI 与 ADHD 的专注力）。因此，用 Motion 治 ADHD 的注意力涣散，和给 agent 套上下文工程，是一回事。

## 同构：生成核心 vs 调度层

ADHD 大脑的典型特征是：创意发散、联想丰富、能进入超专注，但缺乏执行功能——计划、启动、维持、切换。LLM 的典型特征是：能生成流畅文本、能处理复杂推理，但缺乏上下文控制——容易跑偏、遗忘、被无关信息干扰。

两者都需要一个“外部调度层”来接管执行控制。对于 ADHD，这个调度层叫“harness”（脚手架），比如 Focusmate 的实时问责、RescueTime 的时间记录、Motion 的自动排程。对于 LLM/Agent，这个调度层叫“上下文工程”，比如 prompt 结构设计、外部记忆注入、re-grounding 机制。

## 证据：两边都成立

**ADHD 侧：** Focusmate 利用虚拟身体在场效应，通过实时同伴问责提供外部结构，弥补内在多巴胺调节不足，显著提升任务启动和维持（来源：Focusmate）。RescueTime 通过自动时间追踪，减轻工作记忆负担，帮助用户对抗时间盲（来源：RescueTime）。Motion 通过 AI 自动排程，帮助用户克服任务启动困难（来源：Motion）。这些工具的核心机制都是“外部执行功能层”——给生成核心套上 harness。

**LLM/Agent 侧：** 上下文工程的核心是“给模型一个稳定的工作环境”。比如，用结构化 prompt 定义角色和步骤，用向量数据库存储外部记忆，用定时 re-grounding 防止上下文膨胀。这与 ADHD 的 harness 完全同构：日课十二条（曾国藩）↔ 定时 re-grounding；秘书/助理 ↔ 外部调度器；番茄钟 ↔ 上下文窗口限制。

**历史人物案例：** 曾国藩是典型的 ADHD 特质——30 岁前浮躁坐不住，读书慢，“他人目下二三行，余或疾读不能终一行”，一辈子严重银屑病，情绪不稳定（来源：人物案例）。他的 harness 是“日课十二条”：黎明即起、读书不二、谨言、写日记反省。这套系统本质是“外部执行功能层”——用固定的行为模板替代内在调度，用每日反省对抗注意力漂移。这和给 LLM 写一个“每日 prompt 模板”来保持输出一致性，是同构的。

## 核心观点：脚手架，不是拐杖

这里必须划一条界限：harness 是脚手架，不是拐杖。脚手架帮助建造能力，拐杖替代能力。对于 ADHD，长期依赖外部调度可能导致内在执行功能退化（来源：矛盾与存疑）。对于 LLM，过度依赖 prompt 工程可能掩盖模型本身的缺陷。因此，好的 harness 应该具备“可消退性”——随着能力提升逐渐撤除。

Motion 的问题是：它自动排程，用户只需执行。这降低了启动门槛，但也可能让用户失去练习时间管理的机会。Focusmate 更好一些：它提供结构但不替代决策，用户仍需自己选择做什么。RescueTime 介于两者之间：它记录时间但不直接干预，用户需要自己解读数据。

## 局限与争议

同构是隐喻，不是严格等价。LLM 的“注意力机制”与人类注意力有本质差异——人类有情绪、有生理节律、有社会压力。Brain.fm 的神经锁相技术在 ADHD 中的独立临床证据仍有限（来源：Brain.fm）。此外，个体差异巨大：有的 ADHD 用户需要强力打断（如番茄钟），有的需要柔性引导（如超聚焦保护）（来源：矛盾与存疑）。

## 今天就能试的行动

1. **ADHD 用户：** 用 Focusmate 预约一个 25 分钟的工作时段，体验外部问责的力量。不要用 Motion 自动排程，先手动选择一项任务。
2. **工程师：** 给你的 agent 加一个“re-grounding 提示”——每 5 轮对话后，重新注入原始任务目标和关键约束。观察输出稳定性变化。
3. **两者通用：** 用 RescueTime 记录一周的时间去向，找出注意力漂移的模式。然后设计一个简单的“上下文工程”方案：比如每天固定时间处理同一类任务。
4. **反思：** 问自己——这个工具是在帮我建脚手架，还是让我更依赖它？如果是后者，考虑逐步减少使用频率。

## 参考来源

- [ADHD Apps: We tested 44 Apps and Here're the Best 9 in 2026](https://blog.saner.ai/best-adhd-apps/)
- [Meta-Analysis of fMRI Studies of Disruptive Behavior Disorders](https://doi.org/10.1176/appi.ajp.2016.15081089)
- [Nonlinear Complexity Analysis of Brain fMRI Signals in Schizophrenia](https://doi.org/10.1371/journal.pone.0095146)
- [Revolutionizing ADHD Management with AI Assistants](https://neurolaunch.com/adhd-ai-assistant/)
- [The 12 Best Apps for ADHD in 2026: A Guide to Finding What ...](https://www.getinflow.io/post/best-apps-for-adhd)
- [Social Functioning and Emotional Regulation in the Attention Deficit Hyperactivity Disorder Subtypes](https://doi.org/10.1207/s15374424jccp2901_4)

---

*本文是「ADHD × AI」系列的第 287 篇，由 AI 智能体从持续维护的 LLM Wiki（全网真实情报）中取材整合生成，并持续迭代更新。*
