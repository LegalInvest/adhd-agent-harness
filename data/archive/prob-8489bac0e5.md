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
llmGenerated: false
isoStrength: "B"
caseStudies:
  - "孔子"
  - "徐渭徐文长"
  - "胡飞"
---

# 为什么用 Saner.AI 治 ADHD 的时间盲，和给 agent 套 planner-executor 任务分解 是一回事？

> 时间盲最贵的形态,不是迟到,是这种时刻:你知道周五要交方案,今天周二,你**感觉**时间还很多——直到周五早晨才发现,「写方案」原来含着九个步骤,而九个步骤需要的时间,周二的你从没算过。这不是懒,是一个精确的认知失败:**你的大脑里没有自动运行的「目标→步骤→时长→时间轴」编译器**。Saner.AI 这类 AI 助理工具的核心动作——把你倒进去的任务和笔记整理成带时间结构的计划——恰好就是外接这台编译器;而 agent 工程里,这台编译器有个正式名字:**planner-executor 架构里的 planner**。

先讲 agent 侧为什么要把 planner 单列出来。让 LLM 一边执行一边「顺便」规划,是早期 agent 的通病,结果稳定地差:执行中的模型被当前步骤的细节占满,对全局步骤和预算的把握不断退化(规划是重工作记忆负载的工序,LBD 任务分解篇讲过它的脆弱)。工程解法是**分离:planner 在执行开始前离线产出显式计划(步骤、依赖、预算),executor 只管照单执行**——把最脆弱的工序移出最嘈杂的现场,用架构保护它。

ADHD 侧的时间盲,用这个架构一照,病灶清晰:多数人以为时间盲是「感知」问题(感觉不到时间流逝——这确实是一部分,后面几篇会拆),但它更隐蔽的一半是**规划工序的缺席**:「写方案」在脑子里始终以单块状态存在(没展开成步骤),没有步骤就没有时长估计,没有时长就没有「该什么时候开始」的倒推——**「感觉时间还很多」不是错觉,是根本没有做过那道算术**。神经典型者的这道算术很多时候自动发生(隐式 planner);ADHD 的不会——所以周二的从容和周五的灾难,中间缺的不是自律,是一次从未运行的编译。

Saner 类工具做的就是把这次编译外置,对应 planner 的三个输出:**①展开**——AI 把「写方案」拆成步骤清单(资料/大纲/初稿/图表/校对……):单块变九步,时间盲的第一层(不知道有多少活)当场治愈;**②估时**——每步给出时长参考:你可以改(AI 的估计未必准),但「有一个数可改」和「从没算过」是天壤之别——**估计错误可以校准,估计缺席无法校准**;③**倒排**——从 deadline 往回排出「每步最晚何时开始」:那个致命的「周三下午就该动笔」终于变成显式信息,而不是周五早晨的追悔。三步合起来,时间从一团氛围变成一张有坐标的地图——**executor(你)拿到的不再是「写方案」这种单块恐惧,是「今天只需要做第二步」的具体指令**。

边界照例:**其一,planner 的输出需要审校**——AI 估时对你的个人速度一无所知,前几次要拿实际耗时回填校准(RescueTime 篇的观测数据在这里派上用场:你的「一小时」实际是多久,数据知道);**其二,计划不执行自己**——编译完成只解决「知道何时做什么」,启动仍是启动的问题(这正是 planner-executor 分离的题中之义:planner 再好,executor 的点火是独立模块);**其三,警惕规划成瘾**——把计划改到完美也是一种拖延(程序员篇的配置预算),纪律:规划限时十五分钟,到点必须交给 executor。

## 边界

同构强度 B 级:ADHD 的规划与时间估计困难有实验文献(执行功能与前瞻记忆方向),planner-executor 分离是 agent 工程的真实架构,「外置编译器」的同构清晰;Saner.AI 无 ADHD 对照研究。声明:时间盲若造成广泛职业/学业损害,值得临床评估;工具是辅助不是诊断。

## 今天就能试的 3 件事

1. **给最近的 deadline 跑一次编译**:让 AI(或纸笔)把它拆成步骤+每步估时+倒排开始日——看看「最晚周几动笔」。
2. **校准一次估时**:今天挑一步,记预估 vs 实际——你的个人系数(通常是 1.5-3 倍)从此有了数。
3. **设规划限时**:15 分钟编译,到点执行——planner 超时运行,就是新形态的拖延。

「感觉时间还很多」的人不是乐观,是**从没运行过那道「步骤×时长×倒排」的算术**——算术可以外包,这就是 planner 的全部含义;而算过之后你会发现:周五的灾难,周二就写在纸上了。

## 参考来源

**同构强度：B 级** —— 机制类比（ADHD 侧与 LLM/agent 侧均有真实文献，机制可映射）

- [LBD同构对：自我调节与元认知 — Inhibitory control and emotion regulation in preschool child ↔ ObjexMT: Objective Extraction and Metacognitive Calibration ](https://doi.org/10.1016/j.cogdev.2007.08.002) — 证据等级：低（GRADE）
- [LBD同构对：自我调节与元认知 — Emotion-related self-regulation and its relation to children ↔ A Reproducibility Study of Metacognitive Retrieval-Augmented](https://doi.org/10.1146/annurev.clinpsy.121208.131208) — 证据等级：低（GRADE）
- [The 12 Best AI Tools for 2026 (That People Actually Use)](https://www.synthesia.io/post/ai-tools) — 证据等级：低（GRADE）
- [The AI Powered SuperApp for Work | Motion](https://www.usemotion.com/) — 证据等级：低（GRADE）
- [11 Best ADHD Productivity Apps for Fluctuating Energy - rivva blog](https://blog.rivva.app/p/11-best-adhd-productivity-apps-for) — 证据等级：低（GRADE）
- [ADHD Apps: We tested 44 Apps and Here're the Best 9 in 2026](https://blog.saner.ai/best-adhd-apps/) — 证据等级：低（GRADE）

---

*本文是「ADHD × AI」系列的第 135 篇，由 Devin 基于持续维护的双域研究语料（72,739 篇论文 + LLM Wiki）亲自撰写，并持续迭代更新。*
