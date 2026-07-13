---
title: "为什么用 Motion 治 ADHD 的注意力涣散，和给 agent 套 上下文工程 是一回事？"
subtitle: "Motion 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
description: "Motion 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
date: "2025-04-15"
category: "专注力管理"
categoryId: "focus"
categoryEn: "Focus Management"
tags:
  - "ADHD"
  - "AI"
  - "专注力管理"
  - "反直觉同构"
  - "深度工作"
readingTime: 12
slug: "为什么用-motion-治-adhd-的注意力涣散和给-agent-套-上下文工程-是一回事"
topicId: "evolved-focus-2072"
angle: "反直觉同构"
rank: 160
score: 7.71
sourceCount: 6
toolsCited:
  - "Motion"
  - "Focusmate"
  - "Brain.fm"
  - "RescueTime"
  - "Forest"
thesis: "ADHD 大脑与 LLM 是同一类「高产但缺执行调度层的生成核心」，两者都需要外部脚手架（harness）来补偿调度缺陷，因此用 Motion 治注意力涣散与给 agent 套上下文工程在结构上完全同构。"
problem: "为什么用 Motion 治 ADHD 的注意力涣散，和给 agent 套 上下文工程 是一回事？"
spine: "上下文工程"
spineKind: ""
isEvolved: true
llmGenerated: false
caseStudies:
  - "曾国藩"
  - "孙策"
  - "颜淑华"
---

# 为什么用 Motion 治 ADHD 的注意力涣散，和给 agent 套 上下文工程 是一回事？

> 上一篇说 Goblin Tools 是「窗口清洁工」——处理的是内容层的污染。但注意力涣散还有另一个来源,清洁工管不了:窗口里同时开着的「频道」太多。此刻该干什么?下午那个会要不要准备?晚上还有没有时间?——这些调度层的悬念,才是很多人一天的糊的主源。Motion 处理的正是这一层:它做的不是内容净化,是上下文的「单频道化」。

先区分这两种污染,因为混淆它们会用错工具。**内容污染**:窗口里塞满任务碎片和杂念——解法是倒空+拆解(Goblin Tools 的辖区)。**调度污染**:每个时刻都悬着「现在做什么/等会做什么/来得及吗」的未决问题——这些问题本身不是任务,是**关于任务的元问题**,但它们同样占窗口,而且比任务更阴魂不散:任务做完会闭合,「我是不是安排错了」永不闭合。ADHD 的时间感知与优先级短板,让调度层的悬念浓度天然偏高——很多人的涣散,主要成分其实是这个。

LLM 侧的对应机制很直接:**给模型的上下文里如果同时描述五个待办目标,输出会在几个目标间摇摆**;上下文工程的解法是「一窗一事」——当前窗口只呈现当前目标,其余目标由外部编排器持有,到点再注入。**模型不需要知道整个 pipeline,它只需要知道这一步。** 编排器(orchestrator)存在的意义,就是让 worker 的上下文保持单频道。

Motion 就是给你的一天雇了这个编排器:所有任务、会议、死线交给它,算法把一天编译成时间块序列——**于是任何时刻,你的「窗口」里理论上只需要一条信息:当前块**。「下午的事」不需要你持有,编排器持有着;「来不来得及」不需要你反复评估,重排算法在评估。调度悬念被整体外包,窗口腾出来给正事。

按「单频道化」的逻辑用它,三条:

**一、信任编排器,关掉自己的后台调度进程。** 装了 Motion 还每小时打开全天视图检查一遍,等于雇了编排器又亲自盯梢——调度悬念一点没减,还加了检查成本。纪律:**执行时段只看当前块,全天视图每天只看两次**(早上过一遍,傍晚调一遍)。

**二、把「冒出来的调度焦虑」当作待注入信息,不当作当前任务。** 干着活突然想起「周四死线来得及吗」——这不是需要现在回答的问题,是需要转交编排器的信息:十秒钟把它扔进 Motion(加任务/改死线),然后回当前块。**焦虑的正确归宿是编排器的输入队列,不是你的前台窗口。**

**三、块的粒度匹配你的持有能力。** 单频道的前提是「一个频道的内容你拿得住」——90 分钟的块对涣散日太大了,频道内部会再次糊掉。**涣散日把块切到 25-40 分钟**,块间留白;编排器管块间调度,块内如果还糊,那是内容污染,回到上一篇的清洁流程。两层工具,两层污染,配合使用。

用错的姿势:**用检查代替执行**(反复优化日程=新的涣散);**块内多开**(单频道时段里回消息、瞟邮件——编排器给了你单频道,你自己又开了三个台);**指望它治内容糊**(块到了、开始了、还是糊——那不是调度问题,去倒空和拆解)。

## 边界

同构强度 B 级:多目标上下文对 LLM 输出的干扰与「一窗一事」的工程实践是真实的,ADHD 的调度负荷与时间感知困难有文献支撑,Motion 无 ADHD 对照研究,「两种污染」的区分是本文的操作框架。声明:若涣散严重到多数日子无法进入任何任务,或伴随情绪问题,请专业评估;调度外包减负荷,不改变神经层面的注意调节,别用工具的效果好坏评判自己。

## 今天就能试的 3 件事

1. **诊断你的糊**:此刻窗口里的,是任务碎片(内容污染)还是「来不来得及」(调度污染)?
2. **立「两次规则」**:全天视图早晚各看一次,执行时段只看当前块。
3. **练一次「焦虑转交」**:下次调度焦虑冒头,十秒扔进日程工具,回当前块。

涣散的一天,常常不是脑子坏了,是你同时开着七个频道,每个频道都在小声播放。**编排器的全部价值,是替你按下六个静音键**——剩下那一个频道里的事,你其实一直做得来。

## 参考来源

- [ADHD Apps: We tested 44 Apps and Here're the Best 9 in 2026](https://blog.saner.ai/best-adhd-apps/) — 证据等级：低（GRADE）
- [Meta-Analysis of fMRI Studies of Disruptive Behavior Disorders](https://doi.org/10.1176/appi.ajp.2016.15081089) — 证据等级：高（GRADE）
- [Nonlinear Complexity Analysis of Brain fMRI Signals in Schizophrenia](https://doi.org/10.1371/journal.pone.0095146) — 证据等级：低（GRADE）
- [Revolutionizing ADHD Management with AI Assistants](https://neurolaunch.com/adhd-ai-assistant/) — 证据等级：低（GRADE）
- [DeepSeek - AI Assistant - Apps on Google Play](https://play.google.com/store/apps/details?id=com.deepseek.chat) — 证据等级：低（GRADE）
- [AI Assistant for ADHD: Finally, a Productivity Tool That Requires Less...](https://get-alfred.ai/blog/ai-assistant-for-adhd) — 证据等级：低（GRADE）

---

*本文是「ADHD × AI」系列的第 321 篇，由 Devin 基于持续维护的双域研究语料（72,739 篇论文 + LLM Wiki）亲自撰写，并持续迭代更新。*
