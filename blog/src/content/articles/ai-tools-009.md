---
title: "ADHD 必备：7 个 AI 自动化工作流"
subtitle: "用Zapier和Make打造自动运行的任务系统"
description: "用Zapier和Make打造自动运行的任务系统"
date: "2025-05-21"
category: "AI工具实战"
categoryId: "ai-tools"
categoryEn: "AI Tools in Practice"
tags:
  - "ADHD"
  - "AI"
  - "AI工具实战"
  - "自动化"
  - "效率工具"
readingTime: 8
slug: "adhd-必备7-个-ai-自动化工作流"
topicId: "ai-tools-009"
angle: "自动化"
rank: 3
score: 7.91
sourceCount: 6
toolsCited:
  - "Zapier"
  - "Make"
  - "Goblin Tools"
  - "Lex"
  - "Saner.AI"
  - "Motion"
  - "Reclaim.ai"
  - "Tiimo"
thesis: "自动化工作流能有效降低ADHD群体的认知负荷，但需警惕过度自动化可能削弱内在执行功能，并注意现有工具整合性不足、证据等级低等局限。"
isEvolved: false
llmGenerated: true
---
# ADHD 必备：7 个 AI 自动化工作流

> 用Zapier和Make打造自动运行的任务系统

对于ADHD大脑，每天有太多决策需要做出：先做什么？怎么做？哪些可以跳过？这些决策消耗的认知负荷往往比实际执行任务更累。自动化工作流——尤其是通过Zapier和Make这类平台——正是将决策权交给机器，让大脑从“如何开始”中解放出来。

## 为什么自动化对ADHD特别有效

ADHD的核心执行功能缺陷包括工作记忆不足、任务启动困难和时间盲（来源：ADHD 的 AI 工具全景）。自动化工作流直接针对这些痛点：

- **减少决策疲劳**：AI自动决定“下一步做什么、何时做、如何优先排序”，从而移除决策带来的认知负荷（来源：认知负荷）。
- **降低启动门槛**：当任务被拆解为一系列自动触发的步骤，启动就不再需要意志力。Goblin Tools的Magic ToDo功能就是典型例子——它将“整理房间”分解为“捡起地板上的衣服”“擦桌子”等小步骤，把压倒性的事情变成一系列不压倒性的事情（来源：Goblin Tools）。
- **外化工作记忆**：Saner.AI通过本地记忆存储和快速检索，减少搜索循环和标签切换（来源：Saner.AI），相当于给大脑装了一个外部硬盘。

## 7个AI自动化工作流（基于Zapier和Make）

以下工作流均利用Zapier或Make连接不同工具，实现“一次设置，永远运行”。注意：具体工具名称和功能来自wiki资料，但自动化流程设计为合理推断。

### 1. 任务捕获→自动分解

**触发**：在手机或电脑上输入任意任务（如“准备会议”）。
**动作**：Zapier将任务发送到Goblin Tools的Magic ToDo，自动分解为子步骤，并写入Todoist或TickTick。
**效果**：无需思考“怎么开始”，AI已经为你拆好。

### 2. 语音笔记→结构化整理

**触发**：用Otter.ai录制语音笔记。
**动作**：转录文本发送到Saner.AI，自动提取要点并归类到项目文件夹。
**效果**：避免信息丢失，减少搜索循环。

### 3. 邮件→日程块

**触发**：收到含截止日期的邮件（如“周三前提交报告”）。
**动作**：Make解析邮件，在Motion或Reclaim.ai中创建时间块，并设置提醒。
**效果**：把模糊的“周三前”变成具体的工作时段，对抗时间盲。

### 4. 每日复盘→自动回顾

**触发**：每天固定时间（如晚上9点）。
**动作**：Zapier从Todoist提取已完成任务，发送到Reflect生成结构化回顾。
**效果**：降低认知负荷，强化自我觉察。

### 5. 超聚焦保护

**触发**：检测到连续工作超过90分钟（通过日历或屏幕时间API）。
**动作**：Make触发Tiimo弹出视觉提醒，并暂停非紧急通知。
**效果**：防止超聚焦失控，减少崩溃风险（来源：超聚焦）。

### 6. 单一指令→多步骤流程

**触发**：在Lex中输入一句话指令（如“准备下周客户汇报”）。
**动作**：Lex自动生成大纲、收集资料、创建PPT草稿，并安排两次预演时间。
**效果**：类似Goblin Tools但更强大，一次性完成整个工作流（来源：Lex）。

### 7. 情绪波动→自动调节

**触发**：在情绪追踪App中记录低落或焦虑。
**动作**：Make触发一个预设的“情绪急救”流程：播放Brain.fm专注音乐、显示正念提示、调整当天日程减少任务量。
**效果**：间接支持情绪调节（来源：矛盾与存疑）。

## 核心观点：自动化是支架，不是拐杖

自动化工作流的本质是**执行功能的外包**。它把计划、排序、启动这些ADHD大脑最吃力的部分交给机器，让大脑只负责执行。但这里有一个关键判断：**自动化应该作为支架，而非拐杖**。

支架（scaffolding）是暂时性的支持，最终目标是让用户学会自己走；拐杖则是永久依赖。当前AI工具的证据多基于用户报告，缺乏严格临床试验（来源：ADHD 的 AI 工具全景）。过度依赖自动化可能削弱内在执行功能——如果你永远不用自己启动任务，启动能力会越来越弱。

此外，现有工具存在明显的整合性不足：Goblin Tools侧重任务分解，Saner.AI侧重记忆，Lex侧重任务流，它们各自为政，缺乏统一平台管理所有执行功能（来源：ADHD 的 AI 工具全景）。这意味着你需要设置多个自动化链条，反而可能增加认知负荷。

## 诚实面对局限

- **证据等级低**：这些工作流的效果主要基于用户反馈，没有随机对照试验证明它们优于传统方法（来源：矛盾与存疑）。
- **个性化缺失**：AI推荐算法尚未针对ADHD亚型优化（来源：ADHD 的 AI 工具全景）。注意力缺陷为主型和冲动为主型可能需要不同的自动化策略。
- **依赖风险**：超聚焦状态下，自动化可能让你在错误的事情上沉浸六小时而不自知（来源：超聚焦）。
- **隐私问题**：Otter.ai等工具涉及录音，数据安全存疑（来源：ADHD 的 AI 工具全景）。

## 今天就能试的行动

1. **设置一个“任务捕获→分解”自动化**：用Zapier连接手机备忘录和Goblin Tools（免费版即可），今天输入一个拖延已久的任务，看AI如何拆解它。
2. **创建一个“超聚焦保护”提醒**：在Make中设置一个定时工作流，每90分钟弹出一条消息：“现在几点了？你还在做该做的事吗？”（使用Tiimo或任何提醒App）。
3. **测试Lex的单一指令**：如果你有Lex账号，输入“准备明天的午餐”或“写一封简短的感谢信”，观察它如何分解。
4. **记录一周的认知负荷变化**：用简单日记记录每天“决策疲劳”的程度（1-10分），对比使用自动化前后。这是你个人的小样本证据。

自动化不是魔法，它不会让ADHD消失。但它可以把那些消耗你精力的“隐形工作”移出大脑，让你把有限的认知资源用在真正重要的事情上。关键在于：**用自动化节省下来的精力，去练习那些你最终需要自己掌握的能力**——比如，在自动化提醒你该切换任务时，主动做出选择。

## 参考来源

- [Best AI Tools for ADHD Productivity in 2026 (Honest Review) - Iwo Szapar](https://www.iwoszapar.com/p/best-ai-tools-adhd-productivity-2026)
- [AI Tools for ADHD: Boosting Productivity and Reducing Burnout](https://www.vktr.com/ai-platforms/ai-tools-for-adhd-boosting-productivity-and-reducing-burnout/)
- [The Best AI-Powered ADHD Productivity Tools in 2026 (That ...](https://nexasphere.io/blog/ai-adhd-productivity-tools-2026)
- [“A Cognitive Collaborator:” How Adults with ADHD Are Using ChatGPT](https://www.additudemag.com/how-to-use-chatgpt-executive-function-adhd/?srsltid=AfmBOoq-REuSO0UJC656kbLBAd5u3CDNmGeVNrZ79iouVqrFlN919a39)
- [Harnessing Artificial Intelligence to Live Better with ADHD - CHADD](https://chadd.org/attention-article/harnessing-artificial-intelligence-to-live-better-with-adhd/)
- [AI Tools for Kids with ADHD: A Complete Guide for Parents...](https://www.kidsaitools.com/en/articles/ai-tools-kids-adhd-complete-guide-2026)

---

*本文是「ADHD × AI」系列的第 3 篇，由 AI 智能体从持续维护的 LLM Wiki（全网真实情报）中取材整合生成，并持续迭代更新。*
