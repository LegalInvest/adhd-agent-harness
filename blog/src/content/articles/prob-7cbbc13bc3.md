---
title: "为什么用 Inflow 治 ADHD 的时间盲，和给 agent 套 planner-executor 任务分解 是一回事？"
subtitle: "Inflow 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
description: "Inflow 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
date: "2025-05-09"
category: "时间管理"
categoryId: "time-mgmt"
categoryEn: "Time Management"
tags:
  - "ADHD"
  - "AI"
  - "时间管理"
  - "反直觉同构"
  - "拖延"
readingTime: 10
slug: "为什么用-inflow-治-adhd-的时间盲和给-agent-套-planner-executor-任务分解-是一回事"
topicId: "prob-7cbbc13bc3"
angle: "反直觉同构"
rank: 296
score: 7.65
sourceCount: 6
toolsCited:
  - "Inflow"
  - "Motion"
  - "Reclaim.ai"
  - "Tiimo"
  - "Structured"
  - "Todoist"
  - "Saner.AI"
  - "Goblin Tools"
thesis: "ADHD 大脑与 LLM 都是高产生成核心，两者缺的不是聪明，而是一个可持久、可调用、可撤销的外部执行调度层；用 Inflow 这类工具治时间盲，与给 agent 套 planner-executor 任务分解，本质上是同一套 harness 工程。"
problem: "为什么用 Inflow 治 ADHD 的时间盲，和给 agent 套 planner-executor 任务分解 是一回事？"
spine: "规划循环与任务分解"
spineKind: ""
isEvolved: true
llmGenerated: false
isoStrength: "B"
caseStudies:
  - "孔子"
  - "张居正"
  - "罗想"
---

# 为什么用 Inflow 治 ADHD 的时间盲，和给 agent 套 planner-executor 任务分解 是一回事？

> 时间盲栈修到这里,全是硬件:编译器、调度器、仪表、cron。但有一层软件问题,任何硬件都修不掉:**你对「计划」这件事本身的信念已经坏了**。多年的循环——雄心勃勃地排计划→崩→自责→更雄心地排→更大地崩——在很多 ADHD 者心里沉淀出两个极端之一:「计划无用,我是例外」(规划虚无主义),或「这次要排一个完美的计划」(规划完美主义,崩得更疼)。Inflow 这类 CBT 框架的 ADHD 自助工具,在时间盲战场上的角色,就是修这层软件:**修改 planner 的元参数——你带着什么信念去规划,决定了你排出什么样的计划**。

先讲 agent 侧的对应,它藏在 planner 的配置里。同一个 planner,超参数不同,输出天壤之别:**过度乐观的 planner**(步骤预算全按理想路径估)排出的计划一遇现实就雪崩;**过度悲观的 planner**(处处冗余)则永远启动不了任务。工程上的校准之道,不是把 planner 换掉,是**调它的先验**:用历史轨迹回填真实的耗时分布、给估计乘上校准系数、为已知的失败模式预留缓冲。**planner 的质量,一半在算法,一半在先验**——而先验,就是系统对「事情通常会怎么样」的信念。

ADHD 者的规划先验,通常坏在两个方向,CBT 的语言恰好能命名它们:**①「这次不一样」偏差**——每次做计划时的状态(通常是动机高涨的时刻)被当作执行时的默认状态:排计划的周日晚上,你以为周三的自己也这么有劲——**用峰值状态给全周定价,是 ADHD 计划必崩的第一原因**(状态波动篇:你是全人群里波动最大的,却在用最平稳的假设做规划);**②灾难化与全或无**——一个块崩了=「全天毁了」=弃盘(认知扭曲的经典款「全或无思维」):计划的脆性一半来自结构(串行),一半来自这个解释——**同样的偏差,神经典型者损失一小时,「全或无」者损失一整天**。

Inflow 类工具的 CBT 模块,对这两个先验的修法,精确对应 planner 校准:**①心理教育=注入正确的系统模型**——「你的能量按日波动是特质不是堕落」:接受了这个模型,规划范式自动改变——从「按最好的自己排」变为「按波动的自己排」(低电量日预案、缓冲块、每日只定一个必达项——全是波动先验下的自然推论);**②思维记录=捕获灾难化的瞬间**——计划崩掉的那一刻,抓住脑内那句「全毁了」,替换为准确版:「一个块崩了,重排剩余的」——**这句替换直接改变行为分叉:弃盘 vs 重排,一天的产出差在这一句**;**③行为实验=用数据修先验**——CBT 的招牌技术:把「我做计划从来没用」当假设去检验(排一个极简计划,记录实际完成率)——多数人发现真实完成率远高于信念里的「从来没用」——**先验被数据校准,和 agent 用轨迹回填估计,是同一个动作**。

老边界重申+一条新的:CBT 对成人 ADHD 有 RCT/荟萃证据,app 自助形态证据弱(涣散篇讲过);新的一条:**别把信念工作当成硬件的替代**——「我调整了心态」不能替代 cron 和日历(反过来硬件也替代不了信念:工具齐全但「全或无」还在,第一次崩仍然弃盘)。软硬两层是并联的,本系列十几篇硬件+这一篇软件,合起来才是完整的栈。

## 边界

同构强度 B 级(按正式分级):CBT 对成人 ADHD 的证据较扎实,planner 先验校准是工程实践,「规划信念=元参数」的同构为机制类比;自助 app 的独立疗效证据有限。声明:自助工具不替代治疗;若规划失败伴随持续的自我否定与情绪低落,专业评估优先。

## 今天就能试的 3 件事

1. **给下周排一个「波动先验」计划**:按最差状态排必达项(每天一个),好状态当盈余——试一周,和峰值计划比完成率。
2. **准备好那句替换**:写下「一个块崩了≠一天毁了,重排剩余的」——贴在计划工具旁,崩的时刻照着念。
3. **跑一个行为实验**:把「计划对我没用」当假设,极简计划跑五天记完成率——让数据投票,别让创伤投票。

计划年年崩,不总是排程的错——**有时是 planner 的先验坏了:用峰值给波动定价,用灾难解释局部失败**。调先验不需要新 app,需要抓住脑内那一句话,换掉它。

## 参考来源

**同构强度：B 级** —— 机制类比（ADHD 侧与 LLM/agent 侧均有真实文献，机制可映射）

- [LBD同构对：自我调节与元认知 — Inhibitory control and emotion regulation in preschool child ↔ ObjexMT: Objective Extraction and Metacognitive Calibration ](https://doi.org/10.1016/j.cogdev.2007.08.002) — 证据等级：低（GRADE）
- [LBD同构对：自我调节与元认知 — Emotion-related self-regulation and its relation to children ↔ A Reproducibility Study of Metacognitive Retrieval-Augmented](https://doi.org/10.1146/annurev.clinpsy.121208.131208) — 证据等级：低（GRADE）
- [The 12 Best AI Tools for 2026 (That People Actually Use)](https://www.synthesia.io/post/ai-tools) — 证据等级：低（GRADE）
- [The AI Powered SuperApp for Work | Motion](https://www.usemotion.com/) — 证据等级：低（GRADE）
- [11 Best ADHD Productivity Apps for Fluctuating Energy - rivva blog](https://blog.rivva.app/p/11-best-adhd-productivity-apps-for) — 证据等级：低（GRADE）
- [ADHD Apps: We tested 44 Apps and Here're the Best 9 in 2026](https://blog.saner.ai/best-adhd-apps/) — 证据等级：低（GRADE）

---

*本文是「ADHD × AI」系列的第 147 篇，由 Devin 基于持续维护的双域研究语料（72,739 篇论文 + LLM Wiki）亲自撰写，并持续迭代更新。*
