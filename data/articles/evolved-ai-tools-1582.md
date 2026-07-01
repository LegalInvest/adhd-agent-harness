---
title: "为什么用 Forest 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用 是一回事？"
subtitle: "Forest 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
description: "Forest 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
date: "2025-03-12"
category: "AI工具实战"
categoryId: "ai-tools"
categoryEn: "AI Tools in Practice"
tags:
  - "ADHD"
  - "AI"
  - "AI工具实战"
  - "反直觉同构"
  - "效率工具"
readingTime: 12
slug: "为什么用-forest-治-adhd-的任务启动困难和给-agent-套-function-calling-工具调用-是一回事"
topicId: "evolved-ai-tools-1582"
angle: "反直觉同构"
rank: 384
score: 7.65
sourceCount: 6
toolsCited:
  - "Forest"
  - "Goblin Tools"
  - "Saner.AI"
  - "Lex"
  - "Mem"
  - "Otter.ai"
thesis: "ADHD大脑与LLM agent在结构上同构——两者都是强大的生成核心但缺乏可靠执行调度层，因此Forest等任务启动工具与function calling工具调用本质上都是通过外部harness提供执行功能，实现认知卸载与任务启动。"
problem: "为什么用 Forest 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用 是一回事？"
spine: "工具使用与认知卸载"
spineKind: ""
isEvolved: true
llmGenerated: true
---
# 为什么用 Forest 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用 是一回事？

> Forest 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。

## 问题：为什么启动一件事这么难？

对ADHD人群来说，任务启动困难不是懒，而是大脑的执行功能层出了故障。明明知道该写报告，手却像被钉在椅子上，大脑一片空白，最后刷了两小时手机。与此同时，在AI工程领域，工程师们正为一个类似的问题头疼：LLM能生成惊艳的文本，但让它实际调用API、发邮件、查数据库时，它要么编造参数，要么拒绝执行，像个“高分低能”的偏科生。

这两个问题看似风马牛不相及，但如果你把ADHD大脑和LLM放在一起看，会发现一个惊人的同构：它们都是“高产但缺执行调度层的生成核心”。而解法也惊人地一致——给它们套一个外部harness。

## 同构：ADHD大脑与LLM的相同困境

ADHD大脑的智力与创造力并不差，甚至常常超常，但工作记忆容量有限且不稳定，导致跨会话任务难以持续（来源：无状态与外部记忆）。典型表现是每天需要重新回忆项目上下文，否则容易偏离轨道。同样，标准的LLM调用是无状态的，每次对话独立，模型不保留跨会话记忆。没有harness的LLM只是一个无状态的API调用（来源：Building an AI Agent Harness from Scratch）。

两者都缺乏一个可靠的执行调度层。ADHD大脑缺少的是前额叶的执行功能（计划、组织、时间管理），而LLM缺少的是工具调用、记忆管理和上下文控制。因此，让ADHD患者启动任务，和让LLM agent完成一个多步骤操作，本质上是同一个问题：如何通过外部脚手架，给生成核心提供执行功能。

## 解法：工具使用与认知卸载

### ADHD侧：Forest与任务启动

ADHD个体常借助外部工具来补偿工作记忆的不足。比如Forest——一个番茄钟应用，通过种树的方式强制专注。它的原理很简单：设定一个时间段，种下一棵树，如果中途离开，树就会枯萎。这个外部约束降低了启动门槛，因为用户不需要自己维持注意力，只需要“按下按钮”。

更进阶的工具如Goblin Tools，其Magic ToDo功能能自动将任何任务分解为更小、更易管理的步骤，从而降低启动焦虑（来源：Goblin Tools）。用户反馈称“Goblin Tools将压倒性的事情变成一系列不压倒性的事情”（来源：The Best AI-Powered ADHD Productivity Tools）。Lex则允许用户通过单一指令触发复杂、多步骤的任务序列，减少决策负担（来源：Lex）。这些工具本质上都是在做同一件事：将内部执行功能外包给外部系统。

### LLM/Agent侧：Function Calling与Harness

在LLM agent中，function calling（工具调用）扮演了相同的角色。生产级agent系统通过外部记忆（如向量数据库）解决上下文溢出问题，并组合使用会话内上下文记忆、长期检索向量库和结构化知识库（来源：The Anatomy of an AI Agent）。检索增强和工具调用将决策锚定在外部证据和持久状态上（来源：AI Agent Systems）。

没有这些harness的LLM就像一个ADHD患者没有外部工具——它能生成内容，但无法可靠地执行多步操作。而有了function calling，LLM可以调用日历API、发送邮件、查询数据库，就像ADHD患者用Forest启动工作、用Goblin Tools分解任务一样。

## 核心观点：脚手架，不是拐杖

我的判断是：**ADHD与LLM的解决方案结构同构，但必须区分“脚手架”与“拐杖”**。脚手架是临时支撑，目的是让使用者最终能独立行走；拐杖则是永久替代，会削弱内在能力。

目前多数ADHD工具（如Goblin Tools、Saner.AI）设计为长期使用，未提及撤除机制（来源：矛盾与存疑）。同样，LLM agent的function calling如果过度依赖外部记忆，可能导致模型自身的学习能力退化。关键是要设计可逐步撤除的脚手架：比如先让Forest帮你启动，然后逐渐减少外部提醒，直到你能自己启动。

## 局限与争议

必须诚实指出，ADHD大脑与LLM同构的命题证据主要来自概念类比和工具案例，缺乏大规模实证（来源：矛盾与存疑）。此外，过度依赖AI工具可能阻碍内在执行功能发展，如何设计可逐步撤除的脚手架仍是挑战。个性化适配也是问题——ADHD异质性高，单一工具难以覆盖所有亚型。

## 今天就能试的行动

1. **ADHD读者**：下载Forest或Goblin Tools，下次任务启动困难时，不要强迫自己“快点开始”，而是先设定一个5分钟的番茄钟，或让Goblin Tools把任务分解成3步以下。
2. **工程师读者**：为你的LLM agent添加一个简单的function calling接口（比如调用日历或待办列表API），观察任务完成率的变化。
3. **两类读者**：反思你正在使用的工具——它是帮你建立能力的脚手架，还是让你越来越依赖的拐杖？如果是后者，尝试每周减少一次使用。
4. **交叉实验**：ADHD读者可以尝试用LLM agent（如ChatGPT with plugins）来自动执行多步骤任务，比如“帮我整理下周日程并发送会议邀请”，感受一下外部harness的力量。

## 参考来源

- [Best AI Tools for ADHD Productivity in 2026 (Honest Review) - Iwo Szapar](https://www.iwoszapar.com/p/best-ai-tools-adhd-productivity-2026)
- [AI Tools for ADHD: Boosting Productivity and Reducing Burnout](https://www.vktr.com/ai-platforms/ai-tools-for-adhd-boosting-productivity-and-reducing-burnout/)
- [The Best AI-Powered ADHD Productivity Tools in 2026 (That ...](https://nexasphere.io/blog/ai-adhd-productivity-tools-2026)
- [“A Cognitive Collaborator:” How Adults with ADHD Are Using ChatGPT](https://www.additudemag.com/how-to-use-chatgpt-executive-function-adhd/?srsltid=AfmBOoq-REuSO0UJC656kbLBAd5u3CDNmGeVNrZ79iouVqrFlN919a39)
- [Harnessing Artificial Intelligence to Live Better with ADHD - CHADD](https://chadd.org/attention-article/harnessing-artificial-intelligence-to-live-better-with-adhd/)
- [AI Tools for Kids with ADHD: A Complete Guide for Parents...](https://www.kidsaitools.com/en/articles/ai-tools-kids-adhd-complete-guide-2026)

---

*本文是「ADHD × AI」系列的第 384 篇，由 AI 智能体从持续维护的 LLM Wiki（全网真实情报）中取材整合生成，并持续迭代更新。*
