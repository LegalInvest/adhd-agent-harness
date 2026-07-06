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
topicId: "evolved-focus-1598"
angle: "反直觉同构"
rank: 156
score: 7.75
sourceCount: 6
toolsCited:
  - "Focusmate"
  - "RescueTime"
  - "Brain.fm"
thesis: "ADHD 大脑与 LLM 在结构上同构：两者都是高产但缺乏可靠执行调度层的生成核心，因此解决注意力涣散与 agent 上下文工程共享同一套 harness 思路——通过外部结构（上下文工程）补偿内部调度缺陷。"
problem: "为什么用 Claude 治 ADHD 的注意力涣散，和给 agent 套 上下文工程 是一回事？"
spine: "上下文工程"
spineKind: ""
isEvolved: true
llmGenerated: true
caseStudies:
  - "曾国藩"
  - "老子"
  - "Tommy Walter"
---
# 为什么用 Claude 治 ADHD 的注意力涣散，和给 agent 套 上下文工程 是一回事？

> Claude 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。

## 问题：为什么你的大脑和 LLM 一样“失控”？

如果你是一位 ADHD 患者，你一定熟悉这种感觉：脑子里有无数想法在同时奔涌，但就是无法让其中任何一个落地。你打开文档，准备写报告，结果十分钟后发现自己正在刷手机。你明明知道该做什么，但就是“启动不了”。

如果你是一位在做 Agentic Harness 工程的工程师，你同样熟悉这种感觉：你精心设计的 agent 在简单任务上表现惊艳，但一旦上下文变长、任务变复杂，它就开始“幻觉”——生成自信但错误的输出，重复工作，甚至完全偏离目标。

这两个场景看似毫无关联，但它们的底层结构惊人地一致。本文要论证的核心观点是：

> **ADHD 大脑与 LLM 在结构上同构——两者都是高产但缺乏可靠执行调度层的生成核心。因此，解决 ADHD 注意力涣散的方法，与给 agent 套上上下文工程（harness）的方法，本质上是一回事。**

这不是一个空洞的类比。让我们看看证据。

## 同构一：生成核心 vs 执行调度层

ADHD 大脑的“生成核心”极其强大——发散思维、创意联想、风险承担能力都比普通人强。Tommy Walter（IDG资本投资人）的研究显示，ADHD 群体的风险承受能力是普通人的 2.3 倍（来源：Hypt Health 2025）。但问题在于，这个生成核心缺乏可靠的执行调度层（执行功能），导致输出不稳定：注意力波动、任务启动困难、时间盲。

LLM 同样如此。GPT-4 能写出漂亮的文章，但它的输出天然具有随机性，受采样温度控制。温度越高，输出越随机；温度越低，输出越确定。这种非确定性在生产环境中是可靠性的大敌，因为“小错误会累积，非确定性使可重复性复杂化”（来源：AI Agent Systems: Architectures, Applications, and Evaluation）。

解决方案也同构：为生成核心套上外部调度层。

## 同构二：无状态 vs 外部记忆

ADHD 的工作记忆缺陷是核心痛点。你刚想好要做三件事，走进另一个房间就全忘了。LLM 同样是无状态的——它不记住之前的对话，除非你把上下文塞进窗口。

ADHD 的解决方案是外部记忆系统：清单、日历、第二大脑。LLM 的解决方案是向量数据库、记忆系统、上下文窗口管理。两者都在做同一件事：用外部存储补偿内部工作记忆的不足。

## 同构三：上下文工程——控制“当下注意什么”

ADHD 患者极易被环境带偏：手机通知、窗外声音、甚至一个突然冒出的念头都能让你分心。LLM 同样容易被上下文膨胀干扰：当上下文窗口塞满无关信息时，模型就会“忘记”真正的目标，开始产生幻觉。

两者的解法都是主动设计“当下注意什么”的工程方案。对 ADHD 来说，这可能是 Focusmate 的实时同伴问责——通过视频会议和一个活人一起工作，利用身体在场效应提升专注（来源：Revolutionizing ADHD Management with AI Assistants）。对 LLM 来说，这可能是确定性工作流、计划-执行分离、验证循环等 harness 组件（来源：What is an agent harness...）。

## 人物案例：曾国藩的“日课”就是最早的 harness

曾国藩是典型的注意力不集中型 ADHD。他 30 岁前浮躁坐不住，天天串门喝酒看杀人，日记里骂自己“无恒”“浮躁”；读书慢，“他人目下二三行，余或疾读不能终一行”。他的解决方案是“日课十二条”：黎明即起、读书不二、谨言、写日记反省……用最笨最稳的方法抵消自己的冲动。

这就是一个手工打造的 harness。每条日课都是一个“上下文约束”：读书不二 = 单线程工作，谨言 = 输出过滤，写日记 = 反思循环。对应到 LLM harness：读书不二 ↔ 确定性工作流（一次只做一个子任务），谨言 ↔ 输出验证（检查格式和内容），写日记 ↔ trace 与日志（记录行为以便复盘）。

曾国藩的“结硬寨打呆仗”也是同样的哲学：不依赖灵光一现，而是靠系统化的外部结构来保证稳定输出。这正是上下文工程的精髓。

## 工具证据：Focusmate、RescueTime、Brain.fm

Focusmate 利用“AI-Matched Body Doubling”提供实时问责（来源：The Best AI-Powered ADHD Productivity Tools in 2026）。其本质是为 ADHD 大脑提供一个外部“调度器”——一个活人帮你维持任务专注。对应到 LLM，就是 harness 中的“验证与 CI 集成”（来源：GitHub - ai-boost/awesome-harness-engineering）：系统在每一步检查输出是否合规，防止偏离轨道。

RescueTime 自动记录时间使用，揭示“时间到底去了哪里”（来源：Revolutionizing ADHD Management with AI Assistants）。它解决的是 ADHD 的“时间盲”——无法感知时间流逝。对应到 LLM，就是 trace 和日志系统：记录 agent 每一步的行为，让你知道它“时间花在了哪里”。

Brain.fm 用 AI 生成音乐，通过神经锁相技术影响大脑状态，帮助进入专注状态（来源：11 Best ADHD Productivity Apps for Fluctuating Energy - rivva blog）。这相当于 LLM 的“温度控制”——通过外部信号调节系统的“采样温度”，使其进入稳定输出模式。

## 脚手架 vs 拐杖：一个必须诚实的局限

但同构不是等同。ADHD 大脑与 LLM 的注意力机制存在本质差异（来源：矛盾与存疑）。更关键的是依赖风险：AI 工具作为外部执行功能层，长期使用是否会导致 ADHD 患者内在执行功能进一步退化？这个“拐杖与脚手架”的边界尚不明确（来源：矛盾与存疑）。

我的判断是：**关键在于使用方式。** 如果工具只是替你做事（如自动排程让你完全不用思考时间管理），那就是拐杖；如果工具帮你建立结构和习惯（如 Focusmate 让你学会与他人协作专注），那就是脚手架。一个好的 harness 应该像曾国藩的日课——一开始需要刻意坚持，但最终会内化为习惯。

## 今天就能试的行动

1. **ADHD 侧：尝试一次 Focusmate 会话。** 预约一个 25 分钟的时段，和一个陌生人视频一起工作。观察“身体在场”如何改变你的任务启动能力。
2. **LLM 侧：给你的 agent 加一个“日课”。** 在提示词中加入“每完成一个子任务，输出当前进度并检查是否偏离目标”。这就是最简单的验证循环。
3. **两边通用：建立外部记忆。** ADHD 用户用 RescueTime 自动记录时间；LLM 用户用向量数据库存储关键信息。两者都在做同一件事：让系统不再“无状态”。
4. **反思：你的工具是脚手架还是拐杖？** 问自己：如果明天这个工具消失了，我还能保持同样的效率吗？如果答案是“不能”，说明你在依赖拐杖，需要逐步减少使用，建立内在能力。

## 参考来源

- [ADHD Apps: We tested 44 Apps and Here're the Best 9 in 2026](https://blog.saner.ai/best-adhd-apps/)
- [Meta-Analysis of fMRI Studies of Disruptive Behavior Disorders](https://doi.org/10.1176/appi.ajp.2016.15081089)
- [Nonlinear Complexity Analysis of Brain fMRI Signals in Schizophrenia](https://doi.org/10.1371/journal.pone.0095146)
- [Revolutionizing ADHD Management with AI Assistants](https://neurolaunch.com/adhd-ai-assistant/)
- [Confabulation: The Surprising Value of Large Language Model Hallucinations](https://preview.aclanthology.org/navbar-space/2024.acl-long.770.pdf)
- [The 12 Best AI Tools for 2026 (That People Actually Use)](https://www.synthesia.io/post/ai-tools)

---

*本文是「ADHD × AI」系列的第 156 篇，由 AI 智能体从持续维护的 LLM Wiki（全网真实情报）中取材整合生成，并持续迭代更新。*
