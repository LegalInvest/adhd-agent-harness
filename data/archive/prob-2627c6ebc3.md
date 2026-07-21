---
title: "为什么用 Saner.AI 治 ADHD 的注意力涣散，和给 agent 套 上下文工程 是一回事？"
subtitle: "Saner.AI 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
description: "Saner.AI 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
date: "2025-05-17"
category: "专注力管理"
categoryId: "focus"
categoryEn: "Focus Management"
tags:
  - "ADHD"
  - "AI"
  - "专注力管理"
  - "反直觉同构"
  - "专注力"
readingTime: 10
slug: "为什么用-sanerai-治-adhd-的注意力涣散和给-agent-套-上下文工程-是一回事"
topicId: "prob-2627c6ebc3"
angle: "反直觉同构"
rank: 266
score: 7.65
sourceCount: 6
toolsCited:
  - "Saner.AI"
  - "Brain.fm"
  - "Focusmate"
  - "RescueTime"
  - "Forest"
  - "Endel"
thesis: "ADHD 大脑与 LLM/agent 都是「高产但缺执行调度层的生成核心」，因此都需要用上下文工程（context engineering）在外部搭建一个 harness/脚手架，把工作记忆不稳定、注意力弥散和任务启动困难转化为可控的目标导向行为。"
problem: "为什么用 Saner.AI 治 ADHD 的注意力涣散，和给 agent 套 上下文工程 是一回事？"
spine: "上下文工程"
spineKind: ""
isEvolved: true
llmGenerated: false
isoStrength: "A"
caseStudies:
  - "曾国藩"
  - "文天祥"
  - "Brian Gregory"
---

# 为什么用 Saner.AI 治 ADHD 的注意力涣散，和给 agent 套 上下文工程 是一回事？

> Saner.AI 把自己定位成「ADHD 友好的 AI 笔记与助理」,主打的卖点很朴素:笔记、任务、日程收进一处,AI 帮你在需要时把相关的东西找出来递到眼前。听起来像又一个笔记 app,但对准注意力涣散这个痛点看,它做的事有一个精确的工程名字:**上下文工程(context engineering)**——不是让模型(或大脑)更强,而是**严格控制「此刻工作区里放什么」**。理解了这一点,你就能看懂这类产品的真实价值边界:它治的不是「注意力不足」,是「工作区被错误内容占据」。

先讲 agent 侧的共识,因为它把问题定义得最干净。上下文工程在 LLM 工程里的兴起,基于一个反直觉的教训:**模型表现的天花板,经常不由参数决定,由上下文构成决定**——无关内容进窗会稀释关键信息的注意权重(lost in the middle 的研究),矛盾内容进窗会诱发混乱,而「把所有资料全塞进去」是新手最常犯的错。成熟做法:**按当前任务动态装配上下文**——只放本步骤需要的,其余留在外部存储,用检索按需调入。一句话:**智能系统的表现=f(工作区内容),所以治理工作区就是治理表现**。

ADHD 侧的「注意力涣散」,用这个框架重新描述会突然变得可操作。涣散的现场是什么?桌面上摊着三个项目的材料、屏幕上开着十四个标签、脑子里还挂着「下午要回那条消息」——**你的工作区(视野+工作记忆)里装满了与当前任务无关但持续竞争注意的内容**;注意调度篇讲过,ADHD 的调度器对这些竞争者没有拒绝权——自下而上的捕获自动发生。所以涣散经常不是「注意力弱」,是**上下文污染**:同样的大脑,在只有一件事可看的环境里,表现判若两人(许多 ADHD 者在酒店房间、图书馆隔间的超常发挥,就是天然的上下文净化实验)。

Saner.AI 这类产品的价值,就是把上下文工程从「靠自律维持」变成「系统代劳」,对应三个具体机制:**①单一收纳**——笔记/任务/日程进一个系统,等于把散落各处的「潜在干扰源」收进外部存储(不收纳的信息会以「我是不是忘了什么」的形式常驻工作记忆——认知负荷篇的后台占用);**②按需装配**——AI 在你处理某任务时把相关笔记和材料递出来,而不是让你去翻(翻找的过程本身就是漂移的高发区:去找资料,顺路看到别的,回不来了);**③视野净化**——「今天只看这几件事」的聚焦视图,本质是给你的注意系统做输入过滤。三个机制没有一个在「增强注意力」——**全部在治理进入工作区的内容流**,和 harness 工程师给 agent 做的事逐条同构。

边界也随之清晰,两条:**第一,上下文工程治污染,不治点火**——工作区干净了,启动困难和动机缺失依然是另外的战场(启动篇的四种故障,这里只解决其一);干净的桌面上照样可以瘫痪。**第二,收纳系统自己会变成新的干扰源**——如果整理笔记变成新的拖延方式(程序员篇的「配置预算」问题),或系统复杂到维护成本超过收益,上下文工程就异化成了上下文装修。判据:**系统好不好,看「进入专注的耗时」有没有变短,不看笔记有多整齐**。

## 边界

同构强度 A 级:上下文构成影响 LLM 表现有直接实证(注意稀释、lost in the middle),环境刺激治理对 ADHD 注意表现的影响有实验与临床支持,两者的「工作区治理」同构有跨域研究显式对标;但 Saner.AI 作为具体产品无 ADHD 对照研究,本文是机制分析非疗效背书。声明:严重的注意涣散若伴随全面功能损害,工具是辅助,评估是正路;任何笔记系统都不应成为逃避临床对话的理由。

## 今天就能试的 3 件事

1. **做一次上下文审计**:此刻你的视野和标签页里,几成内容与当前任务相关?——低于一半,先净化再工作。
2. **试一天「按需装配」**:开工前只打开本任务需要的三样东西,其余全关——感受工作区干净的差别。
3. **给收纳系统计时**:本周记录「维护系统」花的时间——超过它帮你省的,降级系统复杂度。

注意力涣散的现场,经常不是大脑坏了,是**工作区里塞满了不该在场的东西**——agent 工程师管这叫上下文污染,他们的解法你可以直接抄:别修引擎,先清窗口。

## 参考来源

**同构强度：A 级** —— 直接文献支撑（引用 ADHD↔LLM 同构专题研究）

- [ADHD Apps: We tested 44 Apps and Here're the Best 9 in 2026](https://blog.saner.ai/best-adhd-apps/) — 证据等级：低（GRADE）
- [Meta-Analysis of fMRI Studies of Disruptive Behavior Disorders](https://doi.org/10.1176/appi.ajp.2016.15081089) — 证据等级：高（GRADE）
- [Nonlinear Complexity Analysis of Brain fMRI Signals in Schizophrenia](https://doi.org/10.1371/journal.pone.0095146) — 证据等级：低（GRADE）
- [Revolutionizing ADHD Management with AI Assistants](https://neurolaunch.com/adhd-ai-assistant/) — 证据等级：低（GRADE）
- [Strong Memory, Weak Control: An Empirical Study of Executive Functioning in LLMs](https://preview.aclanthology.org/evt-to-venues/2026.eacl-long.281.pdf) — 证据等级：低（GRADE）
- [Self-Attention Limits Working Memory Capacity of Transformer-Based Models](https://arxiv.org/pdf/2409.10715) — 证据等级：低（GRADE）

---

*本文是「ADHD × AI」系列的第 117 篇，由 Devin 基于持续维护的双域研究语料（72,739 篇论文 + LLM Wiki）亲自撰写，并持续迭代更新。*
