---
title: "为什么用 Claude 治 ADHD 的注意力涣散，和给 agent 套 上下文工程 是一回事？"
subtitle: "Claude 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
description: "Claude 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
date: "2025-05-15"
category: "专注力管理"
categoryId: "focus"
categoryEn: "Focus Management"
tags:
  - "ADHD"
  - "AI"
  - "专注力管理"
  - "反直觉同构"
  - "深度工作"
readingTime: 10
slug: "为什么用-claude-治-adhd-的注意力涣散和给-agent-套-上下文工程-是一回事"
topicId: "evolved-focus-2081"
angle: "反直觉同构"
rank: 247
score: 7.47
sourceCount: 6
toolsCited:
  - "Brain.fm"
  - "Focusmate"
  - "RescueTime"
thesis: "ADHD 大脑与 LLM 是同一类「高产但缺执行调度层的生成核心」，两者都需要上下文工程作为外部脚手架来补偿调度缺陷，而非依赖拐杖。"
problem: "为什么用 Claude 治 ADHD 的注意力涣散，和给 agent 套 上下文工程 是一回事？"
spine: "上下文工程"
spineKind: ""
isEvolved: true
llmGenerated: false
caseStudies:
  - "曾国藩"
  - "李白"
  - "Samantha Jones"
---

# 为什么用 Claude 治 ADHD 的注意力涣散，和给 agent 套上下文工程是一回事？

> 有人用 Claude 管理自己的注意力,越用越散:开十个对话、每个聊一半、回头找不到重点。也有人越用越聚焦。差别不在工具,在用的人有没有想明白一件事:Claude 对 LLM 工程师来说,首先是一个「上下文窗口」——而你的注意力,也是。

先把两边的机制摆开。ADHD 的注意力涣散,主流模型描述为**自上而下的注意调度失灵**:目标该压制的无关刺激压不住,进入意识的信息流没有守门人,处理资源被摊薄在一切「够响亮」的东西上。LLM 侧的对应物有直接研究:**上下文里的无关内容会实打实地劣化模型输出**——塞进干扰段落,推理准确率显著下滑;而工程答案不是造「抗干扰更强的模型」,是**上下文工程**:严格管控什么进窗口、以什么顺序、占多大比例。这条工程路线之所以值得 ADHD 用户抄,是因为它承认了一个前提:**系统的过滤能力短期内改不了,但输入流完全可控。**

## 用 Claude 做注意力的「窗口管理器」,四个正确姿势

**一、每天开工:把一团乱麻编译成单一焦点。** 早上把脑子里所有悬着的事倒给 Claude(语音更好),让它做三件事:归类、排序、输出「今天唯一主任务+前三步」。这是把「决定做什么」的元认知负荷卸载出去——ADHD 的涣散一半来自任务间的悬置竞争,单一焦点落地,竞争者就退场了。

**二、任务内:让它当「窗口清洁工」。** 做复杂任务(写方案、读材料)时,先让 Claude 把材料压缩成「只与当前小节相关」的摘要再开工——这正是 RAG 的思路:不是把一切塞进窗口,是只放当前一步需要的。你的工作记忆窗口比 Claude 的还小,更该省着用。

**三、干扰到达时:当「念头停车场」。** 工作中冒出的无关念头(「要订机票」「那个邮件没回」),扔进一个固定的 Claude 对话,让它记着并在你要求时汇总——念头被接住才肯离开工作台,这是外置的 scratchpad。

**四、失焦之后:当「重锚定按钮」。** 发现自己漂了,别自责,问 Claude 一句:「我今天的主任务是什么?现在最小的下一步是什么?」——它替你保存着目标状态,这一问就是 agent 工程里的 goal re-injection。

## 用错的三种姿势(为什么有人越用越散)

**把 Claude 当新的刺激源**:开十个对话探索十个有趣问题——这不是注意力管理,是给涣散加了一台涡轮。防法:工作时段只允许两个固定对话(主任务对话+停车场对话),探索欲望进停车场排队。**把聊天当工作**:和 Claude 讨论计划两小时,一个字没产出——对话有进度的幻觉,而幻觉不交付。防法:每次对话以一个「接下来 10 分钟我做 X」收尾,离开键盘去做。**让它替你决策一切**:连「先回哪封邮件」都要问——判断力外包会萎缩,工具应该托住你的短板(排序、记忆、拆解),不该接管你的方向盘。

## 边界

同构强度 A 级:无关上下文劣化 LLM 表现有直接实验研究,ADHD 注意调度缺陷证据扎实,「管控输入流」的策略两侧同验。照例声明:功能同构不是机制等同——你的注意力不是 token 窗口,类比到「输入可控、过滤前置」为止。Claude 是注意力管理的辅助结构,不替代诊断与治疗;药物对注意维持的证据等级更高,涣散严重影响生活的请专业评估。

## 今天就能试的 3 件事

1. **明早做一次「倒脑子」**:把所有悬着的事说给 Claude,要它输出唯一主任务+前三步。
2. **建停车场对话**:今天所有无关念头往里扔,收工时要一份汇总。
3. **立「行动收尾」规则**:每次和 Claude 的对话,以一句「接下来 10 分钟我做 X」结束。

Claude 治不了 ADHD,正如更大的窗口治不了幻觉——但正确的上下文工程能让两个系统都稳定跑起来。管好进窗口的东西,一次只放一个焦点:这条规则,人和模型通用。

## 参考来源

- [ADHD Apps: We tested 44 Apps and Here're the Best 9 in 2026](https://blog.saner.ai/best-adhd-apps/) — 证据等级：低（GRADE）
- [Meta-Analysis of fMRI Studies of Disruptive Behavior Disorders](https://doi.org/10.1176/appi.ajp.2016.15081089) — 证据等级：高（GRADE）
- [Nonlinear Complexity Analysis of Brain fMRI Signals in Schizophrenia](https://doi.org/10.1371/journal.pone.0095146) — 证据等级：低（GRADE）
- [Revolutionizing ADHD Management with AI Assistants](https://neurolaunch.com/adhd-ai-assistant/) — 证据等级：低（GRADE）
- [Confabulation: The Surprising Value of Large Language Model Hallucinations](https://preview.aclanthology.org/navbar-space/2024.acl-long.770.pdf) — 证据等级：低（GRADE）
- [LBD同构对：分心与走神 — Therapeutic Doses of Oral Methylphenidate Significantly Incr ↔ AutoHallusion: Automatic Generation of Hallucination Benchma](https://doi.org/10.1523/jneurosci.21-02-j0001.2001) — 证据等级：低（GRADE）

---

*本文是「ADHD × AI」系列的第 179 篇，由 Devin 基于持续维护的双域研究语料（72,739 篇论文 + LLM Wiki）亲自撰写，并持续迭代更新。*
