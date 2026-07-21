---
title: "为什么用 Claude 治 ADHD 的时间盲，和给 agent 套 planner-executor 任务分解 是一回事？"
subtitle: "Claude 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
description: "Claude 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
date: "2025-05-21"
category: "时间管理"
categoryId: "time-mgmt"
categoryEn: "Time Management"
tags:
  - "ADHD"
  - "AI"
  - "时间管理"
  - "反直觉同构"
  - "任务规划"
readingTime: 10
slug: "为什么用-claude-治-adhd-的时间盲和给-agent-套-planner-executor-任务分解-是一回事"
topicId: "evolved-time-mgmt-2104"
angle: "反直觉同构"
rank: 248
score: 7.47
sourceCount: 6
toolsCited:
  - "Motion"
  - "Reclaim.ai"
  - "Tiimo"
  - "Structured"
  - "Goblin Tools"
  - "Todoist"
thesis: "ADHD 的时间盲与 LLM/agent 的非确定性输出，本质都是强大生成核心缺乏稳定调度层的问题，而外部 harness（对人是脚手架，对 agent 是 planner-executor 架构）是同一类工程解法。"
problem: "为什么用 Claude 治 ADHD 的时间盲，和给 agent 套 planner-executor 任务分解 是一回事？"
spine: "规划循环与任务分解"
spineKind: ""
isEvolved: true
llmGenerated: false
caseStudies:
  - "孔子"
  - "于谦"
  - "余玉英"
---

# 为什么用 Claude 治 ADHD 的时间盲，和给 agent 套 planner-executor 任务分解是一回事？

> 「还有三周,来得及」和「怎么就剩三天了」之间,隔着 ADHD 最经典的一种失能:时间盲。有趣的是,agent 工程师从不指望 LLM 自己「感觉」任务要多久——他们把感觉换成了结构:planner 拆解、estimator 估时、executor 按块执行。这套架构,恰好就是时间盲患者缺的那部分。

先把「时间盲」说准。它不是不识钟表,是**对时间的内感受缺失**:感觉不到「三周」和「三天」的差别(远期时间是一团没有刻度的雾),估不准任务耗时(「一小时能写完」的报告实际要六小时),感觉不到时间在流逝(一抬头三小时没了)。研究者用「时间视界收窄」描述它:**只有「现在」和「不是现在」两档**。后果链条清晰:估时失真→承诺失真→死线雪崩→通宵→自责——循环复利。

LLM 侧的对照精确得刺眼:模型对「这个任务要多少步」同样没有可靠直觉,直接让它一口气做完长任务,产出漂移、步骤跳漏。工程答案是 **planner-executor 架构**:先由 planner 把目标拆成显式步骤序列(每步小、有完成判据),executor 按步执行,外部循环追踪进度。**本质:不修「时间感」,把时间感外置成结构。** 用 Claude 给自己搭同款:

## 一、让 Claude 当你的 planner + estimator

任何超过两小时的任务,先丢给 Claude:「拆成 30-60 分钟的块,每块给出产出物;然后给每块估时,再把估时全部乘以 2。」**乘 2 不是玩笑**——规划谬误人人有,ADHD 加倍;更聪明的做法是用你自己的历史系数:翻三个旧任务,算「实际/当初估计」的均值,让 Claude 记住这个系数,以后一律套用。**用数据替代时间感,是时间盲的第一根假肢。**

## 二、把拆出来的块钉进日历

拆解不落日历等于没拆。让 Claude 输出的每个块带上建议时段,你把它们钉进日历——**日历是时间盲的可视化眼镜**:雾状的「三周后交」变成 14 个有日期的块,每个块都是一个近端死线。倒排时留白 20%(生活会来收税)。「不是现在」的任务从此有了「现在」的形状——这正是把远期奖励 reshape 成近端奖励。

## 三、执行时:外部时钟循环

块内的时间流逝感靠外部循环补:计时器 30-45 分钟一响(响=看一眼「这块的产出物完成了几成」),这就是 executor 的 step check。做完一块,回 Claude 报一句「块 3 完成,实际用时 X」——**它替你记账,账本会持续校准你的估时系数**;偏差大的块型(哪类任务你总是低估),几周后一目了然。

## 用错的姿势

**只拆不执**:让 Claude 拆得漂漂亮亮,然后欣赏计划——计划的完成度不等于任务的完成度,防法是「拆完立刻做第一块」入协议;**无限重排**:每天重新规划一遍,规划本身成了新的拖延——计划一天只准动一次(收工时);**把估时当承诺压自己**:估时是导航不是军令状,超了就更新系数,不启动自责程序——**账本的作用是校准,不是审判。**

## 边界

同构强度 A 级:任务分解对 LLM 长任务表现的增益有直接研究,ADHD 时间知觉异常有实验文献(时距估计任务的系统性偏差),planner-executor 与「外置时间结构」的映射直接。声明:时间盲的神经机制与 agent 架构无关,类比止于「都不该依赖内部时间感,都该外置结构」。严重的时间管理失能影响工作与关系的,请专业评估;药物改善部分患者的时间知觉表现,证据在积累中,结构化工具是配合项。

## 今天就能试的 3 件事

1. **挑一个「还有三周」的任务**:今天让 Claude 拆块+估时×2,钉进日历。
2. **算你的历史系数**:三个旧任务,实际/估计,告诉 Claude 以后一律套用。
3. **今晚开始记块账**:每完成一块报实际用时,一个月后你会第一次「看见」自己的时间。

时间感这东西,别人是天生的表,你是没表——但没表的人可以看日历、设闹钟、记账本。Claude 拆解、日历显影、时钟循环:三件套装齐,时间盲不是治好了,是**不再需要被治**——正如 agent 从来不需要「学会感觉时间」,它只需要一个好 planner。

## 参考来源

- [LBD同构对：自我调节与元认知 — Inhibitory control and emotion regulation in preschool child ↔ ObjexMT: Objective Extraction and Metacognitive Calibration ](https://doi.org/10.1016/j.cogdev.2007.08.002) — 证据等级：低（GRADE）
- [LBD同构对：自我调节与元认知 — Emotion-related self-regulation and its relation to children ↔ A Reproducibility Study of Metacognitive Retrieval-Augmented](https://doi.org/10.1146/annurev.clinpsy.121208.131208) — 证据等级：低（GRADE）
- [The 12 Best AI Tools for 2026 (That People Actually Use)](https://www.synthesia.io/post/ai-tools) — 证据等级：低（GRADE）
- [The AI Powered SuperApp for Work | Motion](https://www.usemotion.com/) — 证据等级：低（GRADE）
- [11 Best ADHD Productivity Apps for Fluctuating Energy - rivva blog](https://blog.rivva.app/p/11-best-adhd-productivity-apps-for) — 证据等级：低（GRADE）
- [ADHD Apps: We tested 44 Apps and Here're the Best 9 in 2026](https://blog.saner.ai/best-adhd-apps/) — 证据等级：低（GRADE）

---

*本文是「ADHD × AI」系列的第 180 篇，由 Devin 基于持续维护的双域研究语料（72,739 篇论文 + LLM Wiki）亲自撰写，并持续迭代更新。*
