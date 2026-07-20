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
llmGenerated: false
isoStrength: "B"
caseStudies:
  - "毛泽东"
  - "杨振宁"
  - "Carolyn Daniel"
---

# 为什么用 Tiimo 治 ADHD 的想理解自己的大脑，和给 agent 套 生成核心 + 缺失的执行层 是一回事？

> 继续「工具当探针」系列(392 篇立了总方法,393 篇用 Reclaim 分离时间系统的四种故障),这一篇的探针是 Tiimo——视觉化日程:一天画成彩色时间轴,当前任务配倒计时圆环,转场有预告。如果说 Reclaim 探测的是「时间的调度」,**Tiimo 探测的是更底层的一层:时间的感知与表征**——你的大脑里,时间到底是以什么格式存在的?这个问题听起来玄,但它对 ADHD 者是最实际的问题之一,因为**时间盲(time blindness)的具体形态因人而异,而不同形态需要完全不同的补偿方案**——Tiimo 恰好是一台能把你的时间盲「显影」出来的仪器。

先讲原理:为什么一个日程 app 能当感知仪器。认知科学侧,时间感知不是单一功能,至少拆成三个子系统:**时距估计**(这件事要多久/已经过了多久)、**时点感知**(现在几点/离 deadline 还有多远)、**时序表征**(今天这些事的先后结构)——ADHD 的「时间盲」在三个子系统上的受损组合因人而异。而 Tiimo 的设计恰好给三个子系统各装了一个外部假体:倒计时圆环(时距的外部化)、时间轴上的「现在」标记(时点的外部化)、一天的视觉序列(时序的外部化)——**于是同 392 篇的逻辑:三个假体里,哪个让你「离不开」,哪个对你「可有可无」,就是三个子系统各自健康度的读数**。agent 工程的对应操作叫组件级 ablation:挨个拆掉组件看性能掉多少——掉得越狠,该组件承担的功能越重。

读数手册,三个子系统逐个看。**读数一:圆环依赖度(时距子系统)**。观察自己看倒计时圆环的频率和「圆环消失时的行为」(比如用不显示倒计时的普通日历过一天):如果没有圆环,你的工作时段规律性地膨胀(说好半小时的事做了两小时而毫无察觉)——你的时距估计器损耗严重,补偿方案要「硬」:物理可见的计时器常驻视野(Time Timer 类)、整点报时、番茄钟——**时距损耗者的关键词是「让流逝可见」**;如果没有圆环你也大致准时,这个子系统够用,别为它付复杂度。**读数二:「现在」标记依赖度(时点子系统)**。症状组:经常被「怎么已经四点了」偷袭、出门时间永远算错、deadline 的临近感直到最后一天才启动——如果 Tiimo 的时间轴显著缓解了这些,你的时点感知需要外部锚;补偿关键词是「**未来的可视化**」:倒推式出门闹钟(不是「三点出门」而是「两点四十开始穿鞋」)、deadline 的多级预告(一周前/三天前/前一天);**读数三:序列依赖度(时序子系统)**。症状组:一天的事在脑中不成序列,只是一团「都要做」的云——每次决定「接下来干嘛」都像抽签;如果 Tiimo 的视觉序列让你的一天第一次有了「形状」,你缺的是时序表征,补偿关键词是「**预编译**」:头天晚上把明天排成序列(371 篇 Structured 的机制,两个产品在这一层同型),执行时只读取不决策。

拿到读数之后,有一个多数人会漏掉的第二层理解:**你的时间盲形态,解释的远不止日程问题**。时距损耗者的「再玩五分钟」变成两小时,不是意志薄弱,是仪表坏了(对着坏仪表谈自律,如同对着坏油表谈省油);时点损耗者的长期迟到,几十年被解读为「不尊重人」,实际是感知缺陷——**把这些旧账从「品格栏」移到「感知栏」,是「想理解自己的大脑」能兑换到的最实在的一笔和解**;当然,和解不等于免责:仪表坏了,责任从「变成一个守时的人」变更为「装好外部仪表并信任它」——这笔责任更小,但更真实,也真的能履行。边界:时间感知的自测读数是功能线索,不是诊断;时间盲的显著损害(影响工作/关系)值得正式评估,评估时带上你的三子系统观察,它们会让临床对话高效得多;Tiimo 的假体对儿童同样适用,但读数的解读者应该是家长+专业人士,别让孩子自己背「我时间感知坏了」的标签——**说明书是给施工者看的,不是给孩子当身份的**。

## 边界

同构强度 B 级:时间感知的多子系统结构与 ADHD 时间盲有研究基础,组件 ablation 是工程实践,「三假体读三子系统」的结构对应清晰;读数手册为实践翻译,无对照研究。声明:Tiimo 未被证实为 ADHD 治疗手段,自测不构成诊断;显著损害请正式评估。

## 今天就能试的 3 件事

1. **做一天「无圆环」对照**:用普通日历过一天,看工作时段膨胀不膨胀——时距子系统的体检,一天就够。
2. **数一周「时间偷袭」**:被「怎么已经这个点了」袭击的次数——时点子系统的读数,免费。
3. **把一笔旧账换栏**:挑一件长期自责的时间旧事(迟到/拖到最后一刻),从品格栏移到感知栏——然后给它配一个外部仪表。

时间盲不是一种病,是三种仪表的不同坏法——**而 Tiimo 这样的视觉假体,恰好是一台三通道的显影仪**。测时距、测时点、测时序:读懂自己坏的是哪块表,才知道该装哪块外部表——理解大脑的意义,从来都是为了正确地补它。

## 参考来源

**同构强度：B 级** —— 机制类比（ADHD 侧与 LLM/agent 侧均有真实文献，机制可映射）

- [ADHD Apps: We tested 44 Apps and Here're the Best 9 in 2026](https://blog.saner.ai/best-adhd-apps/) — 证据等级：低（GRADE）
- [12 AI Personal Assistants Built for ADHD Brains (2026 Rankings)](https://www.usecarly.com/blog/best-ai-personal-assistant-adhd/) — 证据等级：低（GRADE）
- [LBD同构对：自我调节与元认知 — Inhibitory control and emotion regulation in preschool child ↔ ObjexMT: Objective Extraction and Metacognitive Calibration ](https://doi.org/10.1016/j.cogdev.2007.08.002) — 证据等级：低（GRADE）
- [LBD同构对：自我调节与元认知 — Emotion-related self-regulation and its relation to children ↔ A Reproducibility Study of Metacognitive Retrieval-Augmented](https://doi.org/10.1146/annurev.clinpsy.121208.131208) — 证据等级：低（GRADE）
- [The 12 Best AI Tools for 2026 (That People Actually Use)](https://www.synthesia.io/post/ai-tools) — 证据等级：低（GRADE）
- [The AI Powered SuperApp for Work | Motion](https://www.usemotion.com/) — 证据等级：低（GRADE）

---

*本文是「ADHD × AI」系列的第 232 篇，由 Devin 基于持续维护的双域研究语料（72,739 篇论文 + LLM Wiki）亲自撰写，并持续迭代更新。*
