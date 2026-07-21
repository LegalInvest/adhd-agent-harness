---
title: "为什么用 Focusmate 治 ADHD 的时间盲，和给 agent 套 planner-executor 任务分解 是一回事？"
subtitle: "Focusmate 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
description: "Focusmate 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
date: "2025-03-23"
category: "时间管理"
categoryId: "time-mgmt"
categoryEn: "Time Management"
tags:
  - "ADHD"
  - "AI"
  - "时间管理"
  - "反直觉同构"
readingTime: 11
slug: "为什么用-focusmate-治-adhd-的时间盲和给-agent-套-planner-executor-任务分解-是一回事"
topicId: "prob-2562dc3cdc"
angle: "反直觉同构"
rank: 288
score: 7.65
sourceCount: 6
toolsCited:
  - "Focusmate"
  - "Motion"
  - "Reclaim.ai"
  - "Tiimo"
  - "Todoist"
  - "Structured"
  - "Saner.AI"
  - "Goblin Tools"
thesis: "ADHD 大脑与 LLM 都是高产的发散核心，真正的问题不是生成能力不足，而是缺少一个稳定的外部执行调度层；Focusmate 给 ADHD 提供的人类在场-会话-反馈闭环，与 agent 的 planner-executor 分解在结构上是同一种 harness。"
problem: "为什么用 Focusmate 治 ADHD 的时间盲，和给 agent 套 planner-executor 任务分解 是一回事？"
spine: "规划循环与任务分解"
spineKind: ""
isEvolved: true
llmGenerated: false
isoStrength: "B"
caseStudies:
  - "孔子"
  - "曹植"
  - "Allison Lopez"
---

# 为什么用 Focusmate 治 ADHD 的时间盲，和给 agent 套 planner-executor 任务分解 是一回事？

> 时间盲系列讲到这,组件快齐了:planner 编译(Saner)、调度器绑定(Reclaim)、运行时仪表(Tiimo)、单元容器(Brain.fm)。但所有这些都有一个共同的软肋:**它们都是「我对我自己」的系统——而 ADHD 对自己发出的信号,有一种特异的豁免权**:闹钟可以按掉,色块可以无视,日历块可以「再五分钟」。Focusmate 的 50 分钟视频共工,给执行栈补上的是最后一块,也是最硬的一块:**把计划的时间边界,交给一个不能按掉的东西——另一个人类**。用架构语言说:**外部时钟源(external clock)+ 执行见证(execution witness)——分布式系统同款方案**。

先讲 agent 侧这个对应,它比 body doubling 涣散篇的「社会性上下文」更结构化。分布式系统的一条铁律:**不信任节点的本地时钟**——本地时钟会漂(drift),所以关键时序必须锚定外部时钟源(NTP);同理,agent 的执行时限不由 agent 自己掌握——「你自己看着办,差不多就停」是不存在的设计,**超时由 harness 层强制执行**,因为执行中的节点对自己的时间消耗没有可信判断(它正忙着,或正漂着)。翻译成人类语言:**执行中的你,是全系统里最不适合掌管时钟的节点**——这不是道德指控,是架构常识。

ADHD 侧的证据,恰好说明这个「本地时钟漂移」有多严重:时间知觉研究显示 ADHD 在任务沉浸中的时长估计偏差显著更大;更麻烦的是**自我豁免的单向性**——对自己定的边界,「再五分钟」的谈判永远开着,而谈判对手(也是你)永远心软。于是出现那个熟悉的悖论:计划做得越多,违约经验越多,计划系统的自我信用越破产(「反正我也不会遵守」),最后连计划都不做了——**时间盲的终点,是对一切自我时序承诺的失效预期**。

Focusmate 的机制,就是把时序承诺从「我对我」改写成「我对人」:**①预约=不可豁免的开始时刻**——15:00 的共工,对面的人 15:00 会出现:开始时间第一次有了外部强制力(对自己:再五分钟;对等着你的人:做不到)——**执行意图(Reclaim 篇)+社会承诺,是行为研究里最强的组合之一**;**②开头宣告=把 plan 装进这个块**——「这 50 分钟我做初稿」:计划的一个 step 被显式绑定到这个被见证的时间块,planner 的输出终于接上了一个不能赖账的 executor 时段;**③50 分钟硬边界=外部时钟的 tick**——块的结束不由你的感受决定(沉浸了也得停,漂了也到点)——过度专注和无限拖延,被同一个机制拦住;**④结尾汇报=执行结果的见证**——「完成了/完成一半」要说出口:这是最小的执行验证(verifier 篇的人类版),而且它反向修复自我信用:**一次次「宣告→兑现→被见证」,是重建「我的计划可以被相信」的唯一路径**——自我豁免毁掉的,由外部见证一点点赚回来。

边界:**其一,共工覆盖的是「块级」时序**——50 分钟内部的漂移它管不细(那是 Tiimo 层的事),跨天跨周的编排它不管(那是 Reclaim 层的事)——它是栈里的一层,不是全栈;**其二,社交成本因人而异**——涣散篇讲过社交焦虑的门槛,时间盲场景多一条:迟到共工本身对时间盲者是新的焦虑源,选宽容的搭子或宽进入窗口的平台;**其三,别把见证变监工**——见证的力量在「有人知道」,不在「有人管着」;如果汇报开始引发羞耻而非动力,降低频率或换搭子,机制为你服务,不是反过来。

## 边界

同构强度 B 级:社会承诺对执行意图的增强有行为研究支持,外部时钟与超时强制是分布式/agent 工程的真实设计,「本地时钟不可信」的同构清晰;body doubling 的 ADHD 直接研究仍以小规模与社区证据为主。声明:若一切外部结构都无法阻止全面拖延且伴随情绪恶化,评估优先;共工是辅助不是治疗。

## 今天就能试的 3 件事

1. **把本周最怕的 step 挂上共工**:预约一场,开头宣告就做它——给计划找一个不能赖账的时段。
2. **测你的豁免率**:本周自设边界(闹钟/计时)被你谈判掉几次,外部约定(会议/共工)几次?——差值就是你需要外部时钟的程度。
3. **建一个兑现台账**:每次「宣告→兑现」记一笔——自我信用的修复,需要看得见的账本。

对自己按掉的第十个闹钟不会内疚,对等着你的人做不到——**这不是弱点,是可利用的架构特性**:本地时钟漂了,就锚一个外部时钟源;全世界的分布式系统都这么活着,你也可以。

## 参考来源

**同构强度：B 级** —— 机制类比（ADHD 侧与 LLM/agent 侧均有真实文献，机制可映射）

- [LBD同构对：自我调节与元认知 — Inhibitory control and emotion regulation in preschool child ↔ ObjexMT: Objective Extraction and Metacognitive Calibration ](https://doi.org/10.1016/j.cogdev.2007.08.002) — 证据等级：低（GRADE）
- [LBD同构对：自我调节与元认知 — Emotion-related self-regulation and its relation to children ↔ A Reproducibility Study of Metacognitive Retrieval-Augmented](https://doi.org/10.1146/annurev.clinpsy.121208.131208) — 证据等级：低（GRADE）
- [The 12 Best AI Tools for 2026 (That People Actually Use)](https://www.synthesia.io/post/ai-tools) — 证据等级：低（GRADE）
- [The AI Powered SuperApp for Work | Motion](https://www.usemotion.com/) — 证据等级：低（GRADE）
- [11 Best ADHD Productivity Apps for Fluctuating Energy - rivva blog](https://blog.rivva.app/p/11-best-adhd-productivity-apps-for) — 证据等级：低（GRADE）
- [ADHD Apps: We tested 44 Apps and Here're the Best 9 in 2026](https://blog.saner.ai/best-adhd-apps/) — 证据等级：低（GRADE）

---

*本文是「ADHD × AI」系列的第 139 篇，由 Devin 基于持续维护的双域研究语料（72,739 篇论文 + LLM Wiki）亲自撰写，并持续迭代更新。*
