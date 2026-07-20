---
title: "为什么「治好 ADHD 的有想法有能力，却卡在执行与落地」和「让 LLM 不跑飞」其实是同一道工程题？"
subtitle: "LLM 智力强但需要外部编排才能完成长任务——同一套 harness 思路，两边都成立。"
description: "LLM 智力强但需要外部编排才能完成长任务——同一套 harness 思路，两边都成立。"
date: "2025-04-24"
category: "职场发展"
categoryId: "career"
categoryEn: "Career Development"
tags:
  - "ADHD"
  - "AI"
  - "职场发展"
  - "反直觉同构"
  - "领导力"
readingTime: 11
slug: "为什么治好-adhd-的有想法有能力却卡在执行与落地和让-llm-不跑飞其实是同一道工程题"
topicId: "prob-f6c966a4e7"
angle: "反直觉同构"
rank: 329
score: 7.63
sourceCount: 6
toolsCited:
  - "Goblin Tools"
  - "Saner.AI"
  - "Motion"
thesis: "ADHD 大脑与 LLM 本质上都属于“生成核心强、执行调度层弱”的系统：二者都不缺想法与智力，却都依赖外部 harness（脚手架、上下文、验证循环、记忆与确定性工作流）才能把长任务真正落地。"
problem: "为什么「治好 ADHD 的有想法有能力，却卡在执行与落地」和「让 LLM 不跑飞」其实是同一道工程题？"
spine: "生成核心与调度层"
spineKind: "bridge"
isEvolved: false
llmGenerated: false
isoStrength: "B"
caseStudies:
  - "屠呦呦"
  - "孔子"
  - "刘丽华"
---

# 为什么「治好 ADHD 的有想法有能力，却卡在执行与落地」和「让 LLM 不跑飞」其实是同一道工程题？

> ADHD 最残忍的画像不是「什么都不行」,是**「什么都行,除了落地」**:想法密度惊人、单点能力在线(聊起来头头是道,做起来某个环节还特别强),但从想法到交付的链条,永远断在中间某处——项目启动了七个,完成了零个;方案想清楚了,执行卡在第一步的第三天。旁观者困惑:「你明明有能力」。这个画像,LLM 工程师一眼就能认出来:**这就是裸模型——生成核心强大到惊人,但没有调度层:能写出任何代码,却管不了一个三天的项目;能推理任何步骤,却串不起二十步的链条**。「有想法有能力却卡在执行」不是能力问题,是**架构问题:生成核心与调度层是两个组件,强生成核心不自带调度层**。

先把 LLM 侧这个架构事实讲透。GPT-4 级别的模型,单轮能力毋庸置疑,但让它裸跑一个长任务,必然跑飞:目标在长上下文里稀释、中间状态没有存储、步骤间没有依赖管理、完成没有判据——**这些不是「模型不够聪明」,是这些功能压根不在模型里**;它们属于另一个组件:调度层(orchestration)——planner 拆解任务、状态机追踪进度、队列管理依赖、验证器判定完成;**agent 工程两年的核心共识:能力在模型里,可靠性在调度层里,两者不可互相替代**——用更强的模型补调度层的缺失,是行业反复踩空的坑。

这个架构区分,对 ADHD 的自我理解是釜底抽薪式的翻转。ADHD 的神经心理画像,恰恰是「生成核心完好甚至超常(发散思维、快速联想、危机时刻的爆发力),调度组件受损(任务分解、顺序维持、进度监控、完成判定——执行功能的清单)」;而主流的自我归因全部打错了组件:「我有能力却做不成,所以我懒/我不够想要/我人格有缺陷」——**这等于看着一个没接调度层的 GPT-4 骂它「明明会写代码却不肯完成项目」**;归因到品格,解药就成了「更狠地逼自己」,而意志力恰恰也是调度层的功能(受损的那部分),于是越逼越败,越败越确信自己有病的是品格——错误归因的死循环。

正确归因给出的解药清单,本系列三百篇其实一直在写,这里给出架构总图:**你缺的不是能力,是四个调度组件的外部实现**——**①planner:分解**(把想法拆成预算可估的步骤——Goblin Tools/AI 分解/一张纸,任选实现);**②状态机:进度**(每个项目一个进度指针+四行状态笔记——Tiimo/Saner 篇);**③队列:调度**(步骤绑定时间坐标进日历,next_run 永远非空——Structured/Reclaim 篇);**④验证器:完成判据+外部校验**(每步有产物定义,关键节点有人在回路——Lex 篇的输出/上一篇的检查点)。四个组件装齐,生成核心的输出才能变成交付——**和 agent 的公式一字不差:能力 × 调度层 = 产出;任何一项为零,乘积为零**。旁观者说「你明明有能力」,说得对——**能力从来不是缺的那一项**。

边界:**其一,同构是架构层面的**——执行功能不是字面上的「调度软件」,前额叶-纹状体环路远比 planner 复杂;共享的是「生成与调度可分离、且强生成不自带调度」的结构;**其二,外部调度层不是万能**——情绪层(RSD、焦虑)、动机层(兴趣崩塌)、生理层(睡眠、共病)都可能卡住执行,那些战场另有工具与专业支持;**其三,「有能力」的自我评估也要校准**——想法多不等于每个想法值得落地,调度层的第一个功能其实是筛选(大部分想法应该进「以后也许」,Todoist 篇的豁免区)。

## 边界

同构强度 B 级:执行功能与创造性认知可分离有神经心理研究方向,生成核心与调度层的分离是 agent 工程的实体架构,「强生成不自带调度」的结构对应清晰;外部调度组件的组合为实践框架。声明:执行困难若伴随情绪或生理层问题,专业评估优先;本文不做诊断。

## 今天就能试的 3 件事

1. **重写一次归因**:把「我有能力却做不成,因为我懒」改成「我的生成核心在线,缺的是调度组件 X」——X 是分解、进度、排程还是验证?对照四件套自查。
2. **给一个卡住的想法装 planner**:今天只做一件事——把它拆成五个预算可估的步骤,第一步小于 15 分钟。
3. **停掉一次品格审判**:下次「明明会却没做」的时刻,问「哪个组件没接」而不是「我怎么回事」——组件能装,品格审判只会攒债。

「明明有能力」的困惑,答案早就写在 agent 架构图上:**能力在生成核心里,落地在调度层里——它们从来就是两个组件**。裸的 GPT-4 完不成项目,不裸的你可以:四个组件,今天装第一个。

## 参考来源

**同构强度：B 级** —— 机制类比（ADHD 侧与 LLM/agent 侧均有真实文献，机制可映射）

- [ADHD Apps: We tested 44 Apps and Here're the Best 9 in 2026](https://blog.saner.ai/best-adhd-apps/) — 证据等级：低（GRADE）
- [12 AI Personal Assistants Built for ADHD Brains (2026 Rankings)](https://www.usecarly.com/blog/best-ai-personal-assistant-adhd/) — 证据等级：低（GRADE）
- [LBD同构对：自我调节与元认知 — Inhibitory control and emotion regulation in preschool child ↔ ObjexMT: Objective Extraction and Metacognitive Calibration ](https://doi.org/10.1016/j.cogdev.2007.08.002) — 证据等级：低（GRADE）
- [LBD同构对：自我调节与元认知 — Emotion-related self-regulation and its relation to children ↔ A Reproducibility Study of Metacognitive Retrieval-Augmented](https://doi.org/10.1146/annurev.clinpsy.121208.131208) — 证据等级：低（GRADE）
- [The 12 Best AI Tools for 2026 (That People Actually Use)](https://www.synthesia.io/post/ai-tools) — 证据等级：低（GRADE）
- [The AI Powered SuperApp for Work | Motion](https://www.usemotion.com/) — 证据等级：低（GRADE）

---

*本文是「ADHD × AI」系列的第 179 篇，由 Devin 基于持续维护的双域研究语料（72,739 篇论文 + LLM Wiki）亲自撰写，并持续迭代更新。*
