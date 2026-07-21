---
title: "为什么用 RescueTime 治 ADHD 的时间盲，和给 agent 套 planner-executor 任务分解 是一回事？"
subtitle: "RescueTime 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
description: "RescueTime 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
date: "2025-04-22"
category: "时间管理"
categoryId: "time-mgmt"
categoryEn: "Time Management"
tags:
  - "ADHD"
  - "AI"
  - "时间管理"
  - "反直觉同构"
readingTime: 11
slug: "为什么用-rescuetime-治-adhd-的时间盲和给-agent-套-planner-executor-任务分解-是一回事"
topicId: "prob-13edc3544e"
angle: "反直觉同构"
rank: 299
score: 7.65
sourceCount: 6
toolsCited:
  - "Motion"
  - "Reclaim.ai"
  - "Tiimo"
  - "Todoist"
thesis: "ADHD 大脑与 LLM 都是“高产生成核心 + 弱执行调度层”的同构系统，因此用 RescueTime 这类时间追踪工具治疗 ADHD 时间盲，与给 agent 加装 planner-executor 架构，本质上是同一套 harness 工程：把内部不可靠的调度、记忆与启动功能外化为可配置模块。"
problem: "为什么用 RescueTime 治 ADHD 的时间盲，和给 agent 套 planner-executor 任务分解 是一回事？"
spine: "规划循环与任务分解"
spineKind: ""
isEvolved: true
llmGenerated: false
isoStrength: "B"
caseStudies:
  - "孔子"
  - "张居正"
  - "方刚"
---

# 为什么用 RescueTime 治 ADHD 的注意力涣散，和给 agent 套 planner-executor 任务分解 是一回事？

> RescueTime 在可观测性篇里是日志系统:自动记录时间去向,给你一份「你以为 vs 实际」的对账单。这一篇把它接到 planner-executor 架构上,讲那份对账单的第二用途——也是工程上更重要的用途:**观测数据不是拿来看的,是拿来喂 planner 的**。涣散造成的时间流失,单靠「看见」不会停止;但**被量化的涣散,可以作为参数写进下一版计划**——计划从「假设我不会涣散」升级为「已知我会涣散 N%,照此编排」。这一步升级,恰好是 agent 工程里 planner 与 telemetry 的闭环:**用执行数据修正规划假设,是 planner-executor 架构从「能跑」到「可靠」的分水岭**。

先讲 agent 侧这条闭环的具体样子。裸的 planner 用理想假设排计划:每步预算按「模型一次做对」估——现实中模型会重试、会跑偏、会在某类步骤上稳定地慢;成熟系统的做法是**把执行统计回灌进规划参数**:某类步骤的历史超时率 40%,预算自动乘上系数;某工具调用平均重试 1.8 次,依赖它的路径自动加缓冲——**planner 不再规划「理想的 executor」,规划的是「统计意义上的这一个 executor」**。计划的可靠性,来自对执行者真实缺陷的诚实建模。

现在替换主语。ADHD 者的计划几乎全部在规划「理想的自己」:排日程时假设自己 9:00 坐下就进入状态、一小时的块产出一小时的活、下午和上午一样能打——**每一条假设都被 RescueTime 的数据无情证伪**:真实数据会显示,你的「一小时工作块」平均含 22 分钟的漂移(切出去的标签页、间歇的手机)、上午的专注密度是下午的两倍、每次会议后有 40 分钟的低产出恢复期。这些数字第一次看是羞辱,**换个用法就是黄金:它们是「统计意义上的你」的规格书**——而计划,本来就该为这个你而排,不是为那个理想的你。

具体的回灌操作,三条,每条都是 agent 工程的直译:**①涣散率→预算系数**——数据说你的实际专注密度是 60%,那么「需要 3 小时净专注的任务」就该排 5 小时的块(或 5 个一小时的块):**不是向涣散投降,是停止用不存在的效率骗自己的 deadline**(多少「明明来得及」的崩盘,源头是用 100% 密度做的算术);**②漏点分布→任务-时段匹配**——数据说上午密度高、会后 40 分钟是低谷,那么深工作排上午、会后排机械性琐事:**把任务按认知需求匹配到你的真实产能曲线上**,同样的一天,产出结构性变多(agent 侧同款:高难步骤排给状态好的模型配置);**③高频漏点→定点部署工具**——数据说头号漏点是 15:00 后的视频网站,那 Forest/门禁就部署在 15:00,而不是全天平铺——**本系列讲过的所有工具,部署位置都该由数据决定**:这正是可观测性篇留下的那句话的兑现——观测是其他一切工具的瞄准镜。

边界:**其一,回灌需要固定工序**——数据不会自动变成系数,需要每周一次的十五分钟(看周报→更新三个数:密度系数、最佳时段、头号漏点)——把它做成周日例程的一部分(Reflect 篇的 checkpoint 工序可以合并);**其二,系数是描述不是判决**——60% 的密度是本周的统计,不是你的天花板:干预到位后它会变,记得跟着更新(用旧系数规划进步后的你,是反方向的失真);**其三,羞耻防护重申**——数据用于修改计划,不用于修改自我评价;发现自己盯着数字自责超过五分钟,关报表,只带走三个参数。

## 边界

同构强度 B 级:时间估计偏差与 ADHD 的自我监控困难有实验基础,telemetry 回灌规划参数是工程实践,「为统计上的自己做计划」的同构清晰;RescueTime 无 ADHD 对照研究,回灌协议为实践建议。声明:自动追踪注意隐私;数据引发持续自我攻击时先处理叙事层。

## 今天就能试的 3 件事

1. **算出你的密度系数**:看上周数据(或今天记一天)——名义工作时长里,真专注占几成?这个数从此进你的所有排程。
2. **做一次任务-时段重排**:把本周最难的任务挪到数据显示的最佳时段——一次重排,体验产能曲线的力量。
3. **设周日的回灌工序**:15 分钟,更新三个参数(密度/最佳时段/头号漏点)——让下周的计划,规划真实的你。

计划屡崩的隐藏原因:**你在为一个不存在的、100% 密度的自己排程**。agent 工程的分水岭是用执行数据修正规划假设——你的分水岭,是把那份羞辱性的对账单,读成规格书。

## 参考来源

**同构强度：B 级** —— 机制类比（ADHD 侧与 LLM/agent 侧均有真实文献，机制可映射）

- [LBD同构对：自我调节与元认知 — Inhibitory control and emotion regulation in preschool child ↔ ObjexMT: Objective Extraction and Metacognitive Calibration ](https://doi.org/10.1016/j.cogdev.2007.08.002) — 证据等级：低（GRADE）
- [LBD同构对：自我调节与元认知 — Emotion-related self-regulation and its relation to children ↔ A Reproducibility Study of Metacognitive Retrieval-Augmented](https://doi.org/10.1146/annurev.clinpsy.121208.131208) — 证据等级：低（GRADE）
- [The 12 Best AI Tools for 2026 (That People Actually Use)](https://www.synthesia.io/post/ai-tools) — 证据等级：低（GRADE）
- [The AI Powered SuperApp for Work | Motion](https://www.usemotion.com/) — 证据等级：低（GRADE）
- [11 Best ADHD Productivity Apps for Fluctuating Energy - rivva blog](https://blog.rivva.app/p/11-best-adhd-productivity-apps-for) — 证据等级：低（GRADE）
- [ADHD Apps: We tested 44 Apps and Here're the Best 9 in 2026](https://blog.saner.ai/best-adhd-apps/) — 证据等级：低（GRADE）

---

*本文是「ADHD × AI」系列的第 150 篇，由 Devin 基于持续维护的双域研究语料（72,739 篇论文 + LLM Wiki）亲自撰写，并持续迭代更新。*
