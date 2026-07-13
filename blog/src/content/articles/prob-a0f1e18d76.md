---
title: "为什么用 Tiimo 治 ADHD 的想理解自己的大脑，和给 agent 套 生成核心 + 缺失的执行层 是一回事？"
subtitle: "Tiimo 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
description: "Tiimo 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
date: "2025-05-15"
category: "科学研究"
categoryId: "science"
categoryEn: "Scientific Research"
tags:
  - "ADHD"
  - "AI"
  - "科学研究"
  - "反直觉同构"
  - "诊断"
readingTime: 12
slug: "为什么用-tiimo-治-adhd-的想理解自己的大脑和给-agent-套-生成核心-缺失的执行层-是一回事"
topicId: "prob-a0f1e18d76"
angle: "反直觉同构"
rank: 394
score: 7.61
sourceCount: 6
toolsCited:
  - "Tiimo"
  - "Motion"
  - "Goblin Tools"
  - "Saner.AI"
  - "ReAct"
  - "Chain-of-Thought"
thesis: "ADHD 大脑与 LLM/agent 都是‘生成核心强、执行调度层弱’的同一类系统，Tiimo 与 ReAct/CoT/外部记忆一样，都是给这个核心套上一层外挂的 harness，让灵感能被时间、任务与上下文组织起来，而不是在无序中耗散。"
problem: "为什么用 Tiimo 治 ADHD 的想理解自己的大脑，和给 agent 套 生成核心 + 缺失的执行层 是一回事？"
spine: "ADHD 大脑与 LLM 的同构"
spineKind: ""
isEvolved: true
llmGenerated: true
isoStrength: "B"
caseStudies:
  - "毛泽东"
  - "杨振宁"
  - "Carolyn Daniel"
---
# 为什么用 Tiimo 治 ADHD 的想理解自己的大脑，和给 agent 套 生成核心 + 缺失的执行层 是一回事？

> Tiimo 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。

## 引言：理解自己的大脑，为何那么难？

很多 ADHD 人并不是不聪明，而是被自己“想理解自己的大脑”反复折磨：昨天刚冒出的灵感，今天就忘了上下文；早上列好的计划，会议一乱就全盘崩溃；知道该做什么，却像隔着毛玻璃一样启动不了。Tiimo 这类自适应规划器常被 ADHD 社区推荐，因为它把抽象的时间表变成看得见、能在日程被打乱时自动重新安排的视觉线（来源：AI Tools for ADHD: Boosting Productivity and Reducing Burnout）。但工具本身不是答案。真正的问题是：Tiimo 在做的，和给大模型 agent 补一个“执行层”——ReAct、Chain-of-Thought、外部记忆、human-in-the-loop——其实是同一件事：给一个没有内置调度器的高产生成核心，外挂一个 harness。

## 同构：ADHD 大脑与 LLM 是同一类系统

从 ADHD 侧看，痛苦的核心不是“笨”，而是**生成强、执行弱**。ADHD 大脑往往具备极佳的直觉、创造力、超聚焦与好奇心，但工作记忆不稳定、任务启动困难、时间盲、注意力容易在认知负荷下崩溃（来源：ADHD, Executive Functions, and AI: A New Era in Treatment | Psychology Today；来源：6 ways AI can help you manage ADHD symptoms - Understood.org）。认知心理学家把 ADHD 描述为“执行功能障碍”，其中工作记忆是最关键的瓶颈——它负责在处理信息时短暂保持当前上下文，一旦超载，计划、决策与优先级排序就会瘫痪（来源：Outsourcing Executive Function with AI — Hacking Your ADHD）。

LLM 侧的研究给出了惊人相似的画像。明尼苏达大学系统测试 LLM 执行功能，发现其剖面是“强记忆、弱控制”：工作记忆容量甚至超过常人，但认知灵活性与注意控制存在核心缺陷，无法灵活切换任务集，也无法抑制自动化反应（来源：Strong Memory, Weak Control: An Empirical Study of Executive Functioning in LLMs）。耶鲁研究进一步发现，自注意力机制本身就会限制工作记忆容量：随着上下文变长，注意力分数熵增、注意力弥散、表现下降，与人类注意缺陷的计算本质同源（来源：Self-Attention Limits Working Memory Capacity of Transformer-Based Models）。在 Stroop 冲突任务中，Transformer 在短上下文里表现正常，但序列一长就骤降到随机水平——无法抑制优势反应、无法解决认知冲突（来源：Deficient Executive Control in Transformer Attention）。

简言之：ADHD 大脑和 LLM 都是**高产但缺执行调度层的生成核心**。

## Harness：不是修理核心，而是外挂调度层

 harness 的思路不是“修好坏掉的大脑”或“重写模型”，而是在核心外面搭一层可替换、可升级的脚手架。

对人的 harness：Tiimo、Motion 这样的自适应规划器把“下一步做什么、何时做、被打乱后怎么重排”外包给外部系统，直接降低决策带来的认知负荷（来源：The AI Powered SuperApp for Work | Motion；来源：11 Best ADHD Productivity Apps for Fluctuating Energy - rivva blog）。Goblin Tools 的 Magic ToDo 把“清理厨房”这种模糊任务自动分解为可执行的子任务，用户还能调节“辣度”控制粒度，这正是把任务启动的摩擦力外化（来源：12 AI Personal Assistants Built for ADHD Brains (2026 Rankings)）。Saner.AI 则通过本地记忆和知识回忆，减少搜索循环与标签切换，相当于给人加一个外部记忆缓冲区（来源：Best AI Tools for ADHD Productivity in 2026 (Honest Review) - Iwo Szapar）。

对 agent 的 harness：ReAct 让模型“先想后做、再观察”，CoT 把内部推理外化，外部记忆库维持跨会话上下文，工具调用把计算交给确定性模块，planner 负责任务分解与重排，human-in-the-loop 则作为最终检查点。两者解决的问题完全一致：工作记忆不稳定、上下文膨胀、任务启动困难、时间盲、冲动输出。

## 人物案例：天才也需要 harness

杨振宁的 ADHD 式特质极为明显：思维极度跳跃，物理直觉极强，能一眼看到问题本质，90 多岁仍在工作。他的 harness 系统很有工程感：每天固定时间看书想问题，主动“不做没用的事”，用长期稳定的朋友关系作为外部锚点。对应到 LLM harness：固定日课就是**定时 re-grounding**，剔除无用事务就是**上下文剪枝与注意力聚焦**，而一辈子的友谊网络就是**稳定的外部长期记忆检索锚点**。

毛泽东的 harness 更偏向组织层：他小时候是好动、冲动的问题儿童，后来用“调查研究”收集真实上下文，用“批评与自我批评”引入外部反馈，用“民主集中制”约束个人冲动，用“党指挥枪”把军队和国家纳入

## 参考来源

**同构强度：B 级** —— 机制类比（ADHD 侧与 LLM/agent 侧均有真实文献，机制可映射）

- [ADHD Apps: We tested 44 Apps and Here're the Best 9 in 2026](https://blog.saner.ai/best-adhd-apps/) — 证据等级：低（GRADE）
- [12 AI Personal Assistants Built for ADHD Brains (2026 Rankings)](https://www.usecarly.com/blog/best-ai-personal-assistant-adhd/) — 证据等级：低（GRADE）
- [LBD同构对：自我调节与元认知 — Inhibitory control and emotion regulation in preschool child ↔ ObjexMT: Objective Extraction and Metacognitive Calibration ](https://doi.org/10.1016/j.cogdev.2007.08.002) — 证据等级：低（GRADE）
- [LBD同构对：自我调节与元认知 — Emotion-related self-regulation and its relation to children ↔ A Reproducibility Study of Metacognitive Retrieval-Augmented](https://doi.org/10.1146/annurev.clinpsy.121208.131208) — 证据等级：低（GRADE）
- [The 12 Best AI Tools for 2026 (That People Actually Use)](https://www.synthesia.io/post/ai-tools) — 证据等级：低（GRADE）
- [The AI Powered SuperApp for Work | Motion](https://www.usemotion.com/) — 证据等级：低（GRADE）

---

*本文是「ADHD × AI」系列的第 232 篇，由 AI 智能体从持续维护的 LLM Wiki（全网真实情报）中取材整合生成，并持续迭代更新。*
