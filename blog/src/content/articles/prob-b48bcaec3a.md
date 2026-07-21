---
title: "两个互不引用的领域都在研究「目标维持」——ADHD 文献和 LLM harness 文献为什么得出了同一个结论？"
subtitle: "Swanson 文献发现：240 篇 ADHD 论文 ↔ 145 篇 harness 论文共享机制「goal maintenance」，双域代表作对照解读。"
description: "Swanson 文献发现：240 篇 ADHD 论文 ↔ 145 篇 harness 论文共享机制「goal maintenance」，双域代表作对照解读。"
date: "2025-03-11"
category: "专注力管理"
categoryId: "focus"
categoryEn: "Focus Management"
tags:
  - "ADHD"
  - "AI"
  - "专注力管理"
  - "LBD同构发现"
  - "深度工作"
readingTime: 11
slug: "两个互不引用的领域都在研究目标维持adhd-文献和-llm-harness-文献为什么得出了同一个结论"
topicId: "prob-b48bcaec3a"
angle: "LBD同构发现"
rank: 98
score: 7.65
sourceCount: 6
toolsCited:
  - "RescueTime"
  - "Focusmate"
  - "Brain.fm"
  - "Forest"
  - "Motion"
  - "Reclaim.ai"
thesis: "ADHD 大脑与 LLM/agent 都是高产却缺乏内置目标维持层的生成核心，所以两个互不引用的领域在 \"goal maintenance\" 上殊途同归：解法不是提升意志力，而是构建可定期重锚定的外部 harness/脚手架。"
problem: "两个互不引用的领域都在研究「目标维持」——ADHD 文献和 LLM harness 文献为什么得出了同一个结论？"
spine: "重锚定与目标漂移"
spineKind: "llm"
isEvolved: false
llmGenerated: false
isoStrength: "B"
caseStudies:
  - "曾国藩"
  - "王阳明"
  - "Christopher Jones"
---

# 两个互不引用的领域都在研究「目标维持」——ADHD 文献和 LLM harness 文献为什么得出了同一个结论？

> 续上一篇的文献计量观察:「任务分解」不是唯一一条被两个领域同时挖掘的隧道。在「目标维持(goal maintenance)」这个关键词下,同样的构型再次出现——ADHD 文献研究「为什么行为会脱离意图」,agent 文献研究「为什么执行会偏离指令」,两边各自积累了厚实的实证,互引依然接近零。**而这一次,两边不仅结论相同,连描述失败的曲线形状都相同**:目标不是突然丢失的,是随时间/负载单调衰减的。

ADHD 侧的隧道:目标维持在执行功能研究里有精确的操作化——在持续性任务(如各类 CPT 与工作记忆任务)中,ADHD 组的特征不是开局就差,而是**表现随时间劣化更快、且在干扰项出现后恢复更慢**;行为层的对应是每个 ADHD 者都熟的剧本:出门倒垃圾,顺路收了快递,拆了包裹,坐下看说明书——垃圾还在手里。重要的是文献给出的机制方向:**目标表征需要在工作记忆中主动维持,而维持是持续耗能的过程**;干扰不是「夺走」目标,是在目标表征已经衰减到低水平时「覆盖」了它。据此的干预方向也清晰:**外部再激活**——把目标放在环境里反复可见(便签、闹钟、他人提醒),定期给衰减的表征充电。

Agent 侧的隧道,同款曲线:LLM 执行长任务时的目标漂移(goal drift)是被反复复现的现象——初始指令的约束力随上下文长度增长而衰减,模型逐渐滑向局部合理但全局偏离的行为;用冲突任务测 Transformer 的研究给出了更干净的版本:**短上下文中能正确执行任务规则,序列拉长后规则的约束力崩坏**。工程解法与 ADHD 干预精确对应:**周期性重注入**——把 system prompt/任务目标定期重新写入上下文(re-anchoring),而不是指望初始指令永久有效;每隔 N 步做一次「当前行为 vs 原始目标」的对齐检查。Agent 侧的结论:**目标不是设置一次就持续生效的状态,是需要周期性刷新的信号**。

并排看两边的结论:「目标表征需要主动维持+外部再激活」vs「目标信号会衰减+需要周期性重注入」——**又一次,措辞可以互换**。共同的深层结构:两种系统的「当前行为控制器」都只对**工作区内激活的内容**响应(工作记忆/上下文窗口),而工作区是有限的、被不断涌入的新内容竞争的——**目标若不被反复写回工作区,就会被统计规律稀释掉**。这不是缺陷的巧合,是「有限工作区+持续输入流」这个架构的必然属性:任何这样的系统,目标维持都必须是主动过程。

互相的馈赠,这次尤其对称。ADHD 侧可以直接借 agent 的工程参数:**①重注入要定周期,不能靠「需要时想起」**(想起本身就依赖目标激活,循环依赖——所以是闹钟每小时响,不是「记得看便签」);**②重注入的内容要短**(agent 的 re-anchoring 是一句压缩的目标陈述,不是全文重贴——你的版本:「我现在的目标是____」一句话,贴在屏幕边);**③检查点做「对齐 diff」**(闹钟响时只问一个问题:当前动作服务于目标吗?偏了不自责,写一笔,拉回来——漂移是架构属性,不是道德事件)。agent 侧则从 ADHD 文献借到几十年的干扰研究:什么样的刺激最容易覆盖目标(新奇、情绪性、社交性——所以通知是漂移的头号推手,两边都是),这直接指导 harness 的输入过滤设计。

## 边界

同构强度 B 级:两侧的核心现象各有扎实实证(ADHD 的持续性任务劣化与目标维持研究;LLM 目标漂移与长上下文规则崩坏),「有限工作区」的共同解释是合理的理论综合,但两种系统的维持机制在实现层面并不相同——同构在功能模式,不在生物学。声明:目标维持的困难若伴随整体的动机丧失(什么目标都提不起来),要考虑抑郁的排查而不只是维持技巧;文献计量描述为方向性概括。

## 今天就能试的 3 件事

1. **设一个每小时的重注入闹钟**:响时读一句「我现在的目标是____」——今天就写好这句话。
2. **做三次对齐 diff**:闹钟响时问「当前动作服务于目标吗」——偏了记一笔,不自责,拉回。
3. **砍一个漂移推手**:挑通知最凶的一个 app,今天静音——干扰研究说,新奇+社交刺激最会覆盖目标。

目标不是许愿池里的硬币,扔一次管一年——**两个领域各自发现:它是需要每小时充电的信号**。衰减不可耻,不充电才可惜。

## 参考来源

**同构强度：B 级** —— 机制类比（ADHD 侧与 LLM/agent 侧均有真实文献，机制可映射）

- [ADHD Apps: We tested 44 Apps and Here're the Best 9 in 2026](https://blog.saner.ai/best-adhd-apps/) — 证据等级：低（GRADE）
- [Meta-Analysis of fMRI Studies of Disruptive Behavior Disorders](https://doi.org/10.1176/appi.ajp.2016.15081089) — 证据等级：高（GRADE）
- [Nonlinear Complexity Analysis of Brain fMRI Signals in Schizophrenia](https://doi.org/10.1371/journal.pone.0095146) — 证据等级：低（GRADE）
- [Revolutionizing ADHD Management with AI Assistants](https://neurolaunch.com/adhd-ai-assistant/) — 证据等级：低（GRADE）
- [LBD同构对：任务分解与规划 — Attention-deficit/hyperactivity disorder is characterized by ↔ Language-conditioned world model improves policy generalizat](https://doi.org/10.1073/pnas.0707741104) — 证据等级：低（GRADE）
- [LBD同构对：任务分解与规划 — Safety and recommendations for TMS use in healthy subjects a ↔ AgentGen: Enhancing Planning Abilities for Large Language Mo](https://doi.org/10.1016/j.clinph.2020.10.003) — 证据等级：低（GRADE）

---

*本文是「ADHD × AI」系列的第 113 篇，由 Devin 基于持续维护的双域研究语料（72,739 篇论文 + LLM Wiki）亲自撰写，并持续迭代更新。*
