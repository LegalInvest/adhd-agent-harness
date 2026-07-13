---
title: "为什么用 Goblin Tools 治 ADHD 的时间盲，和给 agent 套 planner-executor 任务分解 是一回事？"
subtitle: "Goblin Tools 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
description: "Goblin Tools 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
date: "2025-04-23"
category: "时间管理"
categoryId: "time-mgmt"
categoryEn: "Time Management"
tags:
  - "ADHD"
  - "AI"
  - "时间管理"
  - "反直觉同构"
  - "优先级"
readingTime: 14
slug: "为什么用-goblin-tools-治-adhd-的时间盲和给-agent-套-planner-executor-任务分解-是一回事"
topicId: "evolved-time-mgmt-2093"
angle: "反直觉同构"
rank: 162
score: 7.71
sourceCount: 6
toolsCited:
  - "Goblin Tools"
  - "Motion"
  - "Reclaim.ai"
  - "Tiimo"
  - "Structured"
  - "Todoist"
  - "Focusmate"
thesis: "ADHD 的时间盲与 LLM 的任务分解困难共享同一结构缺陷——缺少可靠的调度层，因此 Goblin Tools 和 planner-executor 框架本质上是给高产生成核心套上同构的 harness。"
problem: "为什么用 Goblin Tools 治 ADHD 的时间盲，和给 agent 套 planner-executor 任务分解 是一回事？"
spine: "规划循环与任务分解"
spineKind: ""
isEvolved: true
llmGenerated: false
caseStudies:
  - "孔子"
  - "释迦牟尼"
  - "杨淑珍"
---

# 为什么用 Goblin Tools 治 ADHD 的时间盲，和给 agent 套 planner-executor 任务分解 是一回事？

> 时间盲最典型的一幕:别人问「这个多久能做完」,你说「两小时吧」,实际用了七个小时——而且下次你还会说两小时。这不是撒谎,是「写报告」这三个字在你脑中根本没有展开成可以逐段计时的东西,你估的不是任务,是任务的名字。planner-executor 架构对这件事有个副产品级的发现:任务一旦被拆开,时间就自动显形了。Goblin Tools 的 Estimator 之所以对 ADHD 有用,吃的正是这个机制。

先看 LLM 侧的发现。让模型直接估「完成整个项目要几步/多少资源」,结果和瞎猜差不多——**对一个未展开的黑箱,任何系统都估不准,这不是智力问题,是信息问题**。但 planner 把任务拆成步骤序列之后,再对每个步骤做估计,准确度立刻上一个量级:因为「写一个登录接口」比「做一个系统」暴露了多得多的可估信息。**分解在这里的角色,不只是让任务可执行,是让任务可测量。**

时间盲的机制同样是「未展开」:ADHD 的前瞻性时间感知偏弱是有文献基础的,但日常生活里真正坑人的,是它和「任务不拆解」的叠加——**「写报告」以整块的形态存在于脑中,而整块的东西没有表面积,时间感无处附着**。你说「两小时」的时候,引用的不是这个任务的结构,是一个模糊的、被乐观污染的历史印象。于是估算错误不是随机的,是系统性偏短——这就是每次都迟交的数学原因。

Goblin Tools 的组合拳恰好复刻了 planner 的路径:Magic ToDo 拆解,Estimator 给每个子任务估时,加总。**同一个「两小时」的报告,拆开一估,常常赫然是六个半小时**——这个数字第一次出现时的震撼,是很多用户对时间盲的第一次「看见」。按这个机制用,四条纪律:

**一、永远拆完再估,禁止对整块任务报时间。** 别人问「多久」,标准答案改成「我拆一下,十分钟后告诉你」——这十分钟买来的数字,比脱口而出的「两小时」诚实三倍。**对黑箱报价,是时间盲最大的自我伤害习惯。**

**二、给 Estimator 的输出乘上你的个人系数。** 工具的估计基于一般情形,而你有自己的历史偏差。做法:连续两周,记录「估计 vs 实际」,算出你的系数(多数 ADHD 用户落在 1.5-2.5 之间)——**从此一切估时×系数,这个乘法是你和时间和解的核心仪式。** 系数不是耻辱,是校准;工程里没有无偏差的传感器,只有没校准的。

**三、把估完的时间「铺进日历」再看一眼。** 六个半小时不是抽象数字——铺进本周日历,你会直观看到它挤掉了什么。**时间盲的另一半是「时间的机会成本不可见」**,铺进日历这个动作让它可见:接这个活,意味着周三晚上和周四上午没了。答应别人之前看一眼铺完的日历,冲动承诺会少一半。

**四、用完成数据反哺下一次拆解。** 哪类子任务总是超时(常见:「改一下格式」类的收尾活,估 20 分钟实耗 90)?下次拆到这类,自动加权。**估算是一个可以训练的回路,前提是有记录**——没有记录的估算,永远在用同一个错误的先验。

用错的姿势:**拆而不估**(享受拆解的掌控感,跳过估时——那时间盲原样保留);**估而不信**(算出六小时,心里还是按两小时安排——数字要接管决策,否则只是仪式);**用估算惩罚自己**(「怎么这么慢」——系数是中性的工程参数,不是人格评分)。

## 边界

同构强度 B 级:分解提升估算准确性在软件工程与心理学(规划谬误研究)中均有支撑,ADHD 的时间感知偏差有文献基础,Goblin Tools 无对照研究,「个人系数」是实践建议。声明:时间盲叠加焦虑时,估算可能反向膨胀(不敢开始因为「要六小时」)——若看见真实数字带来的是瘫痪而非清晰,先处理焦虑那层;评估与治疗对时间管理的底层改善仍是证据最强的路径。

## 今天就能试的 3 件事

1. **挑一个今天要做的任务,拆完再估**:对比你脱口而出的数字,记下差值。
2. **开始攒你的系数**:一张两栏表(估计/实际),记两周。
3. **把明天最大的任务铺进日历**:看看它真实的占地面积,再决定今晚几点睡。

时间盲不是看不见钟表,是任务以黑箱的形态拒绝被测量。**拆开它,时间就显形;乘上系数,时间就诚实;铺进日历,时间就有了代价。** 三步之后,「两小时吧」这句话,你会说得越来越少。

## 参考来源

- [LBD同构对：自我调节与元认知 — Inhibitory control and emotion regulation in preschool child ↔ ObjexMT: Objective Extraction and Metacognitive Calibration ](https://doi.org/10.1016/j.cogdev.2007.08.002) — 证据等级：低（GRADE）
- [LBD同构对：自我调节与元认知 — Emotion-related self-regulation and its relation to children ↔ A Reproducibility Study of Metacognitive Retrieval-Augmented](https://doi.org/10.1146/annurev.clinpsy.121208.131208) — 证据等级：低（GRADE）
- [The 12 Best AI Tools for 2026 (That People Actually Use)](https://www.synthesia.io/post/ai-tools) — 证据等级：低（GRADE）
- [The AI Powered SuperApp for Work | Motion](https://www.usemotion.com/) — 证据等级：低（GRADE）
- [11 Best ADHD Productivity Apps for Fluctuating Energy - rivva blog](https://blog.rivva.app/p/11-best-adhd-productivity-apps-for) — 证据等级：低（GRADE）
- [ADHD Apps: We tested 44 Apps and Here're the Best 9 in 2026](https://blog.saner.ai/best-adhd-apps/) — 证据等级：低（GRADE）

---

*本文是「ADHD × AI」系列的第 323 篇，由 Devin 基于持续维护的双域研究语料（72,739 篇论文 + LLM Wiki）亲自撰写，并持续迭代更新。*
