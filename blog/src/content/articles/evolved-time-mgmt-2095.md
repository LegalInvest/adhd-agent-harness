---
title: "为什么用 Motion 治 ADHD 的时间盲，和给 agent 套 planner-executor 任务分解 是一回事？"
subtitle: "Motion 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
description: "Motion 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
date: "2025-04-05"
category: "时间管理"
categoryId: "time-mgmt"
categoryEn: "Time Management"
tags:
  - "ADHD"
  - "AI"
  - "时间管理"
  - "反直觉同构"
  - "日程安排"
readingTime: 12
slug: "为什么用-motion-治-adhd-的时间盲和给-agent-套-planner-executor-任务分解-是一回事"
topicId: "evolved-time-mgmt-2095"
angle: "反直觉同构"
rank: 163
score: 7.71
sourceCount: 6
toolsCited:
  - "Motion"
  - "Tiimo"
  - "Reclaim.ai"
thesis: "ADHD 大脑与 LLM 都是高产生成核心，但缺少可靠的内置调度层；Motion 与 agent 的 planner-executor 任务分解是同一套外部 harness，通过把‘下一步做什么’的决策外包给时间/任务调度器，来弥补执行功能（orchestration）层的缺陷。"
problem: "为什么用 Motion 治 ADHD 的时间盲，和给 agent 套 planner-executor 任务分解 是一回事？"
spine: "规划循环与任务分解"
spineKind: ""
isEvolved: true
llmGenerated: false
caseStudies:
  - "孔子"
  - "老子"
  - "Dr. Randall Duthler"
---

# 为什么用 Motion 治 ADHD 的时间盲，和给 agent 套 planner-executor 任务分解 是一回事？

> 时间盲有两个层级。第一层是「估不准一个任务多久」——上一篇的辖区,拆解+系数能治。第二层更隐蔽也更致命:「感受不到一天正在流逝」。上午还觉得「今天时间很多」,一抬头四点半了,惊恐、赶工、自责——每天重演。第一层是测量问题,第二层是显示问题:你缺的不是钟表,是把「剩余时间 vs 剩余任务」实时对齐的仪表盘。这恰好是 planner-executor 架构里,planner 的另一半职责。

先看架构侧。planner 的工作不只是把任务拆成步骤——**它还要把步骤映射到资源预算上**:这个 agent 的上下文窗口还剩多少?API 配额还剩多少?每一步的消耗是否在预算内?没有这层映射,executor 会在第三步烧光资源,剩下七步搁浅——**这是 agent 长任务失败的经典模式:不是不会做,是对资源的流逝没有感知。** 成熟的编排系统因此都带资源监控:每步执行后更新剩余预算,超支预警,自动调整后续计划。

「一天」就是你的资源预算,时间盲的第二层就是没装监控:任务在消耗时间,而你的主观仪表盘不更新——**ADHD 的时间感知研究里,「当下时间的流逝感」和「对未来时点的距离感」都是受影响的维度**,于是「还早」这个错觉可以坚挺地活到下午四点。自责无用,装仪表盘有用。

Motion 的本质就是这块仪表盘:任务(带时长)进去,算法把它们铺满日历——**于是「今天还剩多少时间 vs 还剩多少任务」第一次变成一个可以看的东西**:日历上填不下了,就是超载了;下午的块被会议吃掉了,晚上的块会自动亮起来提醒你代价。按仪表盘的逻辑用它:

**一、让「一天的总量」先可见。** 每天开始时看一眼铺满的日历——不是为了记住细节,是为了**校准「今天时间很多」这个默认错觉**:你看到的通常是「其实只有四个真正可用的块」。这三十秒的直视,是对时间盲最直接的暴露疗法。

**二、用「块的边界」替代「流逝的感知」。** 你感受不到 90 分钟过去了,但你能听到块结束的提醒。**把时间感知外包给块边界**:块开始=启动信号,块结束=强制抬头(做完没有?没做完,是估短了还是被打断了?)。一天六次抬头,「一抬头四点半」的惊恐就被拆成了六次小校准。

**三、看着重排,学习真实汇率。** 中午超时四十分钟,下午的日历实时重排、有任务被推到明天——**这一刻是时间盲最好的课堂:上午的超支,以「具体哪个任务被牺牲」的形式可视化了**。传统日程表上超时是抽象的,这里超时有名有姓。几周后,很多用户报告「答应事情之前会先想日历装不装得下」——那就是仪表盘开始内化的信号。

**四、给一天留 20% 空白块。** 资源规划的通则:预算打满的系统没有弹性,一次超支就雪崩。日历同理——**排到 80%,留 20% 吸收超时和意外**;天天排满天天崩,不是你不行,是规划参数错了。

用错的姿势:**只装不看**(仪表盘的价值在「被看见」,提醒全关等于没装);**把重排当赦免**(反正会自动推明天→今天随便超——重排是减震器,不是免责条款,周五看一眼「本周被推次数」,那是你的超支报表);**用它管理不该被管理的时间**(留白、休息、发呆是合法支出,不是待优化的浪费)。

## 边界

同构强度 B 级:资源预算监控是真实的 agent 工程实践,ADHD 时间感知的多维度受损有文献支撑,Motion 无 ADHD 对照研究,「仪表盘」是功能映射。声明:时间盲是 ADHD 的核心表现之一,工具提供外部代偿,不修复内部时钟——两者可以长期共存,不必以「摆脱工具」为目标;若时间管理的崩坏伴随睡眠昼夜节律的紊乱,那一层请找医生,仪表盘管不到生物钟。

## 今天就能试的 3 件事

1. **明早花三十秒直视铺满的日历**:数一数真正可用的块有几个,把这个数字说出声。
2. **打开块边界提醒**:每个块结束时强制抬头一次,问「做完没有,为什么」。
3. **检查你的排载率**:日历排到百分之多少?超过 80%,现在删掉或移走一块。

感受不到时间流逝,不是性格缺陷,是仪表盘缺失——**agent 没有资源监控会烧穿预算,人没有时间仪表盘会烧穿一天**。装上它,看着它,剩下的交给校准:四点半依然会到来,但你会在两点就知道它正在路上。

## 参考来源

- [LBD同构对：自我调节与元认知 — Inhibitory control and emotion regulation in preschool child ↔ ObjexMT: Objective Extraction and Metacognitive Calibration ](https://doi.org/10.1016/j.cogdev.2007.08.002) — 证据等级：低（GRADE）
- [LBD同构对：自我调节与元认知 — Emotion-related self-regulation and its relation to children ↔ A Reproducibility Study of Metacognitive Retrieval-Augmented](https://doi.org/10.1146/annurev.clinpsy.121208.131208) — 证据等级：低（GRADE）
- [The 12 Best AI Tools for 2026 (That People Actually Use)](https://www.synthesia.io/post/ai-tools) — 证据等级：低（GRADE）
- [The AI Powered SuperApp for Work | Motion](https://www.usemotion.com/) — 证据等级：低（GRADE）
- [11 Best ADHD Productivity Apps for Fluctuating Energy - rivva blog](https://blog.rivva.app/p/11-best-adhd-productivity-apps-for) — 证据等级：低（GRADE）
- [ADHD Apps: We tested 44 Apps and Here're the Best 9 in 2026](https://blog.saner.ai/best-adhd-apps/) — 证据等级：低（GRADE）

---

*本文是「ADHD × AI」系列的第 324 篇，由 Devin 基于持续维护的双域研究语料（72,739 篇论文 + LLM Wiki）亲自撰写，并持续迭代更新。*
