---
title: "为什么用 ChatGPT 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用 是一回事？"
subtitle: "ChatGPT 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
description: "ChatGPT 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
date: "2025-05-11"
category: "AI工具实战"
categoryId: "ai-tools"
categoryEn: "AI Tools in Practice"
tags:
  - "ADHD"
  - "AI"
  - "AI工具实战"
  - "反直觉同构"
  - "效率工具"
readingTime: 14
slug: "为什么用-chatgpt-治-adhd-的任务启动困难和给-agent-套-function-calling-工具调用-是一回事"
topicId: "evolved-ai-tools-1574"
angle: "反直觉同构"
rank: 24
score: 8.0
sourceCount: 6
toolsCited:
  - "ChatGPT"
  - "Goblin Tools"
  - "Lex"
  - "Saner.AI"
  - "Tiimo"
  - "Motion"
thesis: "ADHD 大脑与 LLM/agent 在结构上同构——都是高产生成核心但缺乏可靠调度层——因此用 ChatGPT 治疗任务启动困难与给 agent 套 function calling 工具调用是同一类工程：用外部脚手架约束生成能力到目标轨道上。"
problem: "为什么用 ChatGPT 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用 是一回事？"
spine: "工具使用与认知卸载"
spineKind: ""
isEvolved: true
llmGenerated: true
caseStudies:
  - "孔子"
  - "彭玉麟"
  - "徐萍"
---
# 为什么用 ChatGPT 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用 是一回事？

> ChatGPT 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。

你坐在电脑前，一个任务在脑子里盘旋了三天。你知道该做什么，但就是启动不了。于是你打开 ChatGPT，输入：“帮我把‘写季度报告’拆成小步骤。”几秒后，它吐出一个清单：打开数据表、整理前三季度数据、写摘要……你长舒一口气，终于能开始了。

另一边，一位工程师正在调试 agent。她发现 LLM 在复杂任务中容易跑偏，于是给它套上 function calling 工具调用——把“搜索数据库”和“发送邮件”封装成函数，让 agent 按步骤调用。她意识到：这不就是给大脑装了一个外部调度器吗？

这两件事，本质上是同一个问题。

## 同构：ADHD 大脑与 LLM 都是“高产但缺调度层”的生成核心

ADHD 大脑常被描述为一个高产的生成核心——想法丰富、联想活跃，但缺少稳定、可靠的调度层来筛选、组织、启动和坚持任务（来源：【主题综述：ADHD 的 AI 工具全景】）。LLM 同样如此：它能生成惊艳的文本，但在长程上下文保持、目标坚持和执行调度上天然缺陷。两者都需要外部脚手架来把生成能力约束到目标轨道上。

这种脚手架，在 ADHD 侧叫“执行功能补偿策略”，在 LLM/agent 侧叫“agent scaffolding”或“function calling 工具调用”。它们干的是同一件事：把模糊的目标拆解为可执行的步骤，并提供外部记忆和提醒。

## 真实案例：孔子与彭玉麟的“harness”系统

孔子是典型的 ADHD 大脑。他身高 1 米 9，精力旺盛，周游列国 14 年坐不住；冲动爱骂人，见南子急得对天发誓，骂宰予“朽木不可雕”；对音乐超专注到“三月不知肉味”，对种地等俗事零耐心；思维跳跃，《论语》全是场景化语录，无系统著作。他的专属 harness 是“克己复礼”——用外在的“礼”作为行为边界，每日反省，“吾日三省吾身”。70 岁才做到“从心所欲不逾矩”，一辈子和自己的冲动做斗争。

彭玉麟同样如此。他性格刚直，冲动敢杀李鸿章的侄子；一生只爱梅姑，画梅花画了一辈子；不要官不要钱不要命，六次辞官。他的 harness 是“三不要”原则和每天画梅花磨练心性，严格军纪，和士兵同甘共苦。

这两位历史人物用自己的方式搭建了外部调度层。孔子的“日课”相当于 LLM 的定时 re-grounding——每天重新对齐目标；彭玉麟的“秘书”（如果他有）相当于外部调度器——把冲动和精力约束到画梅和治军上。他们的成就证明：harness 不是削弱，而是释放。

## 工具证据：AI 如何实现“外部执行功能层”

当前 AI 工具在 ADHD 侧和 LLM 侧都提供了具体实现。

**ADHD 侧：**
- **Goblin Tools** 的 Magic ToDo 功能将复杂任务分解为小步骤，用户可调节“辣度”控制粒度（来源：Goblin Tools）。这直接降低任务启动门槛，对抗执行功能障碍。
- **Lex** 允许通过单一指令触发复杂多步骤任务序列，底层架构类似于 agent scaffolding（来源：Lex）。
- **Saner.AI** 通过知识回忆和本地记忆减少搜索循环，补偿工作记忆不足（来源：Saner.AI）。
- **Tiimo** 用视觉时间表让时间变得可触摸，缓解时间盲（来源：时间盲）。

**LLM/agent 侧：**
- Function calling 工具调用将外部 API（如搜索、计算）封装为函数，让 agent 按步骤调用，避免自由生成跑偏。
- Agent scaffolding 架构围绕 LLM 构建记忆、工具和规划模块，使其能执行复杂目标驱动任务（来源：Lex）。
- 这些工程实践与 ADHD 工具的设计理念完全一致：把高产生成核心接入一个可维护的执行调度系统。

## 核心判断：脚手架，不是拐杖

我的核心观点是：AI 工具的价值不在于替代大脑，而在于把 ADHD 的“高产生成核心”接入一个可维护的“执行调度系统”（来源：【主题综述】）。对 LLM 同样如此——function calling 不是限制，而是让 agent 真正可用的关键。

但这里有一个诚实界限：脚手架 vs 拐杖。过度依赖 AI 可能导致能力退化，这是真实风险（来源：【矛盾与存疑】）。孔子 70 岁才做到“从心所欲”，彭玉麟一辈子画梅——他们的 harness 是内化的，不是外包的。AI 工具应当是训练轮，最终要帮助大脑建立内部调度能力，而不是永久依赖外部指令。

## 局限与争议

- ADHD 大脑与 LLM 同构目前是类比推理，缺乏神经科学或计算机科学的直接证据（来源：【矛盾与存疑】）。
- AI 工具对任务启动的长期效果未知，短期有效但缺乏纵向研究（来源：【矛盾与存疑】）。
- 部分用户反映学习使用 AI 工具本身增加认知负荷，净效果因人而异（来源：【矛盾与存疑】）。

## 今天就能试的行动

1. **用 ChatGPT 拆解一个你拖延的任务**：输入“帮我把 [任务名] 拆成 5 个可执行的小步骤”，然后从第一步开始。
2. **尝试 Goblin Tools 的 Magic ToDo**：输入模糊任务，调节“辣度”到你觉得可行的粒度。
3. **设置一个定时 re-grounding 提醒**：每 30 分钟用手机闹钟问自己“我现在在做什么？应该做什么？”——这就是你的外部调度器。
4. **如果你是工程师，为你的 agent 显式定义 function calling 接口**：把每个子任务封装成函数，观察 agent 的执行稳定性提升。

ADHD 大脑和 LLM 共享同一个秘密：它们都不是坏掉的大脑或模型，只是缺少一个可靠的调度层。而 harness——无论是孔子的“礼”、彭玉麟的“三不要”，还是 ChatGPT 的任务分解、agent 的 function calling——都在做同一件事：让高产生成核心，终于能开始做事。

## 参考来源

- [ADHD Apps: We tested 44 Apps and Here're the Best 9 in 2026](https://blog.saner.ai/best-adhd-apps/)
- [12 AI Personal Assistants Built for ADHD Brains (2026 Rankings)](https://www.usecarly.com/blog/best-ai-personal-assistant-adhd/)
- [The 12 Best AI Tools for 2026 (That People Actually Use)](https://www.synthesia.io/post/ai-tools)
- [Agent Scaffolding: Architecture and Design Patterns for Agentic AI](https://zbrain.ai/agent-scaffolding/)
- [Best productivity apps for Mac you need to try](https://macpaw.com/reviews/best-productivity-apps-for-mac)
- [Building AI Coding Agents for the Terminal: Scaffolding, Harness ...](https://arxiv.org/html/2603.05344v1)

---

*本文是「ADHD × AI」系列的第 24 篇，由 AI 智能体从持续维护的 LLM Wiki（全网真实情报）中取材整合生成，并持续迭代更新。*
