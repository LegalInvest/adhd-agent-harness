---
title: "为什么「治好 ADHD 的注意力容易被环境带偏」和「让 LLM 不跑飞」其实是同一道工程题？"
subtitle: "LLM 受上下文窗口内容左右，需要上下文工程——同一套 harness 思路，两边都成立。"
description: "LLM 受上下文窗口内容左右，需要上下文工程——同一套 harness 思路，两边都成立。"
date: "2025-04-20"
category: "专注力管理"
categoryId: "focus"
categoryEn: "Focus Management"
tags:
  - "ADHD"
  - "AI"
  - "专注力管理"
  - "反直觉同构"
  - "深度工作"
readingTime: 9
slug: "为什么治好-adhd-的注意力容易被环境带偏和让-llm-不跑飞其实是同一道工程题"
topicId: "prob-5c9ec28a15"
angle: "反直觉同构"
rank: 95
score: 7.77
sourceCount: 6
toolsCited:
  - "RescueTime"
  - "Focusmate"
  - "Brain.fm"
  - "Endel"
  - "Forest"
  - "Routinery"
thesis: "ADHD 大脑与 LLM 都是高产但缺乏可靠执行调度层的生成核心，二者真正需要治的不是‘注意力’或‘模型’本身，而是上下文工程：用外部 harness 主动管理‘当下注意什么’。"
problem: "为什么「治好 ADHD 的注意力容易被环境带偏」和「让 LLM 不跑飞」其实是同一道工程题？"
spine: "上下文工程"
spineKind: "llm"
isEvolved: false
llmGenerated: true
isoStrength: "B"
caseStudies:
  - "曾国藩"
  - "孙策"
  - "Barbara Corcoran"
---
# 为什么「治好 ADHD 的注意力容易被环境带偏」和「让 LLM 不跑飞」其实是同一道工程题？

> LLM 受上下文窗口内容左右，需要上下文工程——同一套 harness 思路，两边都成立。

你有没有这种早晨：打开电脑想写一份方案，结果三小时后，你刷了二十条新闻、回了几条消息、整理了一遍桌面，方案的第一行还没写出来？你的大脑不是不能产出，而是产出被环境中每一个新刺激重新定向了。

如果你是做 Agentic Harness 的工程师，这个画面应该也很熟悉：LLM 的推理能力越来越强，但把它放进一个长会话里，上下文窗口一旦膨胀、任务描述被前面的噪声稀释，模型就会开始“跑飞”——回答的不是你当前想问的，而是它此刻窗口里最容易被激活的内容。你调的不是模型不够聪明，而是它“注意错了地方”。

这两件事，表面上一个关乎人脑、一个关乎机器，但其实是同一道工程题：怎么给一个高产但缺执行调度层的生成核心，套上可靠的 harness（缰绳/脚手架）？

## 同一套故障模式：上下文不是背景，而是方向盘

ADHD 一侧的核心痛点常被描述为“注意力容易被环境带偏”。其背后是一组相互放大的执行功能缺陷：工作记忆不稳定、时间感知扭曲、多巴胺调节异常，导致“hours slipping away unnoticed or that drag on forever”（来源：上下文工程）。结果不是不专注，而是专注被错误的东西劫持。更有趣的是，当 ADHD 用户去用通用聊天机器人时，工具本身又会变成新的碎片源：“they often add another inbox, another prompt, and another place to lose the thread”（来源：上下文工程）。

LLM 一侧的对应故障是“上下文膨胀导致推理退化”。大模型没有跨会话的持久状态，它唯一能“记得”的，就是当前上下文窗口里的内容。如果窗口里混杂了过时的指令、用户临时插话、无关的日志，模型就会像被环境带偏的注意力一样，偏离目标任务。工程上需要“strict safety controls and highly efficient context management to prevent...”（来源：上下文工程）。

所以两边的根本问题都不是“生成能力不足”，而是“上下文没有被工程化地管理”。

## 同一套解法：上下文工程 / Context Engineering

“上下文工程”不是简单加提示词，而是主动设计“系统当下应该关注什么、不关注什么”。对 ADHD 大脑，这意味着外挂一个外部执行功能层；对 LLM agent，这意味着在模型前面加调度层、过滤层和 grounding 机制。

ADHD 工具生态已经按这个思路在演化：

- **RescueTime** 自动追踪时间、阻断分心网站，直接补偿“时间盲”和工作记忆不稳定（来源：RescueTime）。
- **Focusmate** 用虚拟身体在场（body doubling）提供外部社会问责，借助算法匹配伙伴，提升任务启动和维持（来源：Focusmate）。
- **Brain.fm** 与 **Endel** 用 AI 生成个性化声音环境，帮助调节专注状态，但 ADHD 特异性证据仍有限（来源：Brain.fm；Endel）。
- **Forest** 用游戏化番茄钟和多巴胺机制增强动机（来源：AI 与 ADHD 的专注力）。
- **Routinery** 把日常任务拆成带过渡提示的序列，本质是在为人脑做“上下文切换调度”（来源：上下文工程）。

LLM 一侧的 harness 对应物则是：上下文窗口管理、检索增强生成（RAG）、指令重述、工具调用前的意图过滤、human-in-the-loop 检查点。这些都不在模型权重里，而在模型之外的“调度层”。

两边共同遵循一个结构：生成核心留在里面，执行调度层放在外面。

## 曾国藩的日课十二条：一个 19 世纪的“Re-Grounding”系统

要理解 harness 思路，曾国藩是个极好的真实案例。他的 ADHD 特质非常典型：30 岁前“浮躁坐不住”，天天串门、喝酒、看杀人；读书“他人目下二三行，余或疾读不能终一行”；情绪极不稳定，打败仗就跳水自杀；一辈子受银屑病困扰（来源：人物案例·曾国藩）。

他给自己搭的 harness 是“日课十二条”：黎明即起、读书不二、谨言、写日记反省等。更核心的战略是“结硬寨、打呆仗”——用最笨、最稳的方法，把冲动和注意力漂移硬顶回去。他每天写日记骂自己，用外部文字把“当下应该关注什么”重新锚定。

这不是意志力，这是工程：

- 黎明即起 ≈ 每日定时 re-grounding，重置上下文。
- 日记反省 ≈ 外部日志系统，补偿工作记忆衰减。
- 读书不二 ≈ 单任务上下文，禁止窗口内混入多任务噪声。
- 结硬寨打呆仗 ≈ 确定性 guardrail，用规则而非即时灵感做决策。

对 LLM 工程师来说，这套东西并不陌生：每天清空并重载上下文、维护外部记忆、限制单次任务范围、用硬规则兜底。曾国藩的日课，本质上就是一个没有计算机时代的“Agentic Harness”。

## 脚手架 vs 拐杖：同构的边界

同构不是等同。ADHD 大脑与 LLM 的类比是功能层面的工程类比，而不是已被验证的神经机制对应（来源：矛盾与存疑）。而且工具既可以成为脚手架，也可以成为拐杖：如果 AI 永远替你做调度，你可能永远学不会自己调度；如果 LLM 的 harness 设计得太硬，又会限制模型的创造力。

现有工具的证据也还不够硬。Brain.fm 和 Endel 在 ADHD 人群中的独立随机对照试验极少；多数推荐基于用户报告或小样本研究（来源：AI 与 ADHD 的专注力）。RescueTime 的自动分类和阻断规则仍需要用户调整，对执行功能弱的用户本身也是负担（来源：RescueTime）。

所以关键边界在于：harness 是让你恢复自己的调度能力，还是永久替代它？

## 核心判断：把 harness 当作基础设施，而不是权宜之计

我的判断是：ADHD 的“注意力容易被环境带偏”和 LLM 的“上下文跑飞”是同一个问题的两种表现形式。治好前者，靠的不是逼自己更专注，而是像工程师设计 agent 一样，设计自己的上下文；让 LLM 不跑飞，靠的也不是把模型做得更大，而是在模型外面建一个稳定、可审计的调度层。

这个判断还有一个重要推论：既然 ADHD 人群在适当 harness 下可以表现出高于常人的创意产出率（有研究显示 ADHD 组创意产出率为对照组的 1.8 倍，来源：Lifted Ventures 2024），那么 harness 的目标就不是“把人变正常”，而是“让高产核心稳定地接入现实任务”。对 LLM 也一样： harness 的目标不是压制模型的生成能力，而是让它在正确的时间、正确的上下文里生成正确的东西。

## 今天就能试：4 条行动

1. **给工作开一个“上下文重置”仪式**：每天开始任务前，用 2 分钟把当前目标、下一步动作、禁止事项写进一个固定位置（曾国藩的“黎明即起”现代版）。
2. **把 LLM 的 prompt 当成上下文工程来设计**：每次交互前先重述任务目标和约束，把无关历史从窗口中清掉，必要时用 RAG 或外部状态替代长对话记忆。
3. **用身体在场或外部问责补启动**：用 Focusmate 这类虚拟 co-working 时段，或者找一个真人同步工作，把“启动”外包给外部结构。
4. **每周做一次“拐杖检查”**：问自己：这个工具是让我更自主了，还是让我更离不开它了？如果答案偏向后者，就减少一层自动化，手动恢复一部分调度能力。

## 参考来源

**同构强度：B 级** —— 机制类比（ADHD 侧与 LLM/agent 侧均有真实文献，机制可映射）

- [ADHD Apps: We tested 44 Apps and Here're the Best 9 in 2026](https://blog.saner.ai/best-adhd-apps/) — 证据等级：低（GRADE）
- [Meta-Analysis of fMRI Studies of Disruptive Behavior Disorders](https://doi.org/10.1176/appi.ajp.2016.15081089) — 证据等级：高（GRADE）
- [Nonlinear Complexity Analysis of Brain fMRI Signals in Schizophrenia](https://doi.org/10.1371/journal.pone.0095146) — 证据等级：低（GRADE）
- [Revolutionizing ADHD Management with AI Assistants](https://neurolaunch.com/adhd-ai-assistant/) — 证据等级：低（GRADE）
- [LBD同构对：工作记忆 — Toward Systems Neuroscience of ADHD: A Meta-Analysis of 55 f ↔ OCR-Memory: Optical Context Retrieval for Long-Horizon Agent](https://doi.org/10.1176/appi.ajp.2012.11101521) — 证据等级：高（GRADE）
- [LBD同构对：注意调度 — Norepinephrine ignites local hotspots of neuronal excitation ↔ Who is in the Spotlight: The Hidden Bias Undermining Multimo](https://doi.org/10.1017/s0140525x15000667) — 证据等级：低（GRADE）

---

*本文是「ADHD × AI」系列的第 16 篇，由 AI 智能体从持续维护的 LLM Wiki（全网真实情报）中取材整合生成，并持续迭代更新。*
