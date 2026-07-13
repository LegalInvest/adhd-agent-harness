---
title: "为什么用 Perplexity 治 ADHD 的时间盲，和给 agent 套 planner-executor 任务分解 是一回事？"
subtitle: "Perplexity 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
description: "Perplexity 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
date: "2025-03-05"
category: "时间管理"
categoryId: "time-mgmt"
categoryEn: "Time Management"
tags:
  - "ADHD"
  - "AI"
  - "时间管理"
  - "反直觉同构"
  - "拖延"
readingTime: 9
slug: "为什么用-perplexity-治-adhd-的时间盲和给-agent-套-planner-executor-任务分解-是一回事"
topicId: "evolved-time-mgmt-2114"
angle: "反直觉同构"
rank: 164
score: 7.71
sourceCount: 6
toolsCited:
  - "Motion"
  - "Reclaim.ai"
  - "Tiimo"
  - "Focusmate"
  - "Todoist"
thesis: "ADHD 大脑和 LLM/agent 都是高产生成核心但缺乏可靠调度层，因此两者的解法——给 ADHD 搭外部执行功能脚手架与给 agent 套 planner-executor harness——在结构上完全同构。"
problem: "为什么用 Perplexity 治 ADHD 的时间盲，和给 agent 套 planner-executor 任务分解 是一回事？"
spine: "规划循环与任务分解"
spineKind: ""
isEvolved: true
llmGenerated: false
caseStudies:
  - "孔子"
  - "王阳明"
  - "王桂珍"
---

# 为什么用 Perplexity 治 ADHD 的时间盲，和给 agent 套 planner-executor 任务分解 是一回事？

> 时间盲的清单上有一项很少被点名,却每周都在偷走几个小时:「查一下」的时间黑洞。计划里写着「查签证材料,半小时」,实际吞掉整个下午——不是因为信息难找,是因为「查资料」这类任务在你的时间账本上根本没有边界:它没有明确的完成判据,没有步骤结构,像一团气体,给多少时间就膨胀成多少时间。planner-executor 架构对这团气体有一套标准处理,而 Perplexity 是执行它的顺手工具。

先看架构侧怎么处理「开放式子任务」。planner 拆解任务时,最忌讳产出这样的步骤:「研究一下相关方案」——**没有完成判据的步骤,executor 要么草草带过,要么无限深挖,时间消耗完全不可控**。成熟的 planner 会把它改写成封闭形式:「列出三个候选方案及各自的主要缺点」——有产出物、有数量、有边界,执行时间立刻从「不可估」变成「可估」。**开放任务的时间不可估,不是因为它大,是因为它没形状;给它形状,时间就有了容器。**

「查一下」正是你日程里的无形状步骤。对 ADHD 来说它加倍危险:检索环境的新异刺激(上一批讲过的兔子洞)拉长它,时间流逝感的钝化(仪表盘缺失)掩护它,完成判据的缺失(「查到什么程度算完?」)使它永不闭合——**三个短板在同一个任务类型上会师,「半小时」变成一下午是结构必然,不是当天状态差。**

处理方案照抄 planner 的改写术,Perplexity 负责执行层:

**一、把每个「查一下」改写成封闭问题。** 「查签证材料」→「列出 X 国旅游签所需材料清单+官方受理时长」;「研究下这个工具」→「这个工具的三个核心功能和两个最大槽点」。**改写的判据:能不能想象「答案已拿到」的样子?能,才允许进日程。** 这三十秒的改写,是整个方法的核心——它把气体装进了瓶子。

**二、封闭问题直接喂 Perplexity,给它一个时间盒。** 封闭问题+综合式答案(没有结果页兔子洞)=可预估的执行时间——**大多数封闭问题,十五分钟内可以闭合**。日程里于是可以诚实地写:「查签证(15min)」——一个时间盲患者第一次能对「查资料」类任务报出准数,这件事本身就是胜利。

**三、答案落进产出物,宣布闭合。** 材料清单抄进任务列表、结论写进文档——**有落地物,才有「完成」;有完成,才有时间边界。** 查完不落地的检索,五天后必然重查一遍,时间黑洞的另一半就是这些重复劳动。

**四、深挖冲动进「第二时间盒」。** 查着查着觉得「这个话题值得深入」——可能是真的,但**深入是另一个任务,需要另一次改写和另一个时间盒**,不是现在这个十五分钟的合法延长。写进稍后清单,让当前问题先闭合。时间盲患者最需要防的,就是任务在执行中悄悄换了身份。

用错的姿势:**改写偷懒**(「查一下 X」改成「了解一下 X」——还是气体,换了个瓶子标签);**时间盒虚设**(设了十五分钟,响了不理——时间盒的权威和日历块一样,靠每一次服从养大);**万物皆查**(有些「查一下」是决策恐惧的伪装:材料早就查过三遍了,你缺的是「开始办」——识别这种,直接跳到行动)。

## 边界

同构强度 B 级:开放式步骤对执行时间的失控是工程共识,封闭化改写是任务设计的标准手法,ADHD 时间感知与检索失控有文献支撑,组合方案无对照研究。声明:反复以「再查查」推迟行动,若伴随明显的决策焦虑或完美主义,值得和专业者谈——那不是信息问题;时间盲的底层是神经性的,工具是代偿不是治愈,长期共存是正常形态。

## 今天就能试的 3 件事

1. **抓出本周日程里的「查一下」**:逐个改写成封闭问题,写不出封闭形式的,先问自己要它干嘛。
2. **今天执行一个「15 分钟检索时间盒」**:封闭问题→Perplexity→落地→闭合,全程计时。
3. **建稍后深挖清单**:本周冒出的「值得深入」先停在那里,周末挑一个,正式改写、正式给时间。

时间盲不只发生在钟表上,更发生在任务的形状上——**无边界的任务,神仙也估不了时**。把「查一下」们逐个装进瓶子,你的下午会突然多出两个小时:它们一直都在,只是从前被气体占着。

## 参考来源

- [LBD同构对：自我调节与元认知 — Inhibitory control and emotion regulation in preschool child ↔ ObjexMT: Objective Extraction and Metacognitive Calibration ](https://doi.org/10.1016/j.cogdev.2007.08.002) — 证据等级：低（GRADE）
- [LBD同构对：自我调节与元认知 — Emotion-related self-regulation and its relation to children ↔ A Reproducibility Study of Metacognitive Retrieval-Augmented](https://doi.org/10.1146/annurev.clinpsy.121208.131208) — 证据等级：低（GRADE）
- [The 12 Best AI Tools for 2026 (That People Actually Use)](https://www.synthesia.io/post/ai-tools) — 证据等级：低（GRADE）
- [The AI Powered SuperApp for Work | Motion](https://www.usemotion.com/) — 证据等级：低（GRADE）
- [11 Best ADHD Productivity Apps for Fluctuating Energy - rivva blog](https://blog.rivva.app/p/11-best-adhd-productivity-apps-for) — 证据等级：低（GRADE）
- [ADHD Apps: We tested 44 Apps and Here're the Best 9 in 2026](https://blog.saner.ai/best-adhd-apps/) — 证据等级：低（GRADE）

---

*本文是「ADHD × AI」系列的第 325 篇，由 Devin 基于持续维护的双域研究语料（72,739 篇论文 + LLM Wiki）亲自撰写，并持续迭代更新。*
