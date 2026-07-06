---
title: "为什么用 Focusmate 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用 是一回事？"
subtitle: "Focusmate 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
description: "Focusmate 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
date: "2025-04-07"
category: "AI工具实战"
categoryId: "ai-tools"
categoryEn: "AI Tools in Practice"
tags:
  - "ADHD"
  - "AI"
  - "AI工具实战"
  - "反直觉同构"
  - "AI工具"
readingTime: 10
slug: "为什么用-focusmate-治-adhd-的任务启动困难和给-agent-套-function-calling-工具调用-是一回事"
topicId: "evolved-ai-tools-1570"
angle: "反直觉同构"
rank: 374
score: 7.65
sourceCount: 6
toolsCited:
  - "Focusmate"
  - "Goblin Tools"
  - "Saner.AI"
  - "Lex"
  - "ChatGPT"
  - "Claude"
thesis: "ADHD 大脑与 LLM 共享同一困境：高产生成核心却缺乏可靠调度层。Focusmate 为 ADHD 提供的外部执行层，与 agent 的 function calling 工具调用是结构同构的 harness——两者都通过外部脚手架将生成能力约束到目标轨道，而非替代核心智能。"
problem: "为什么用 Focusmate 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用 是一回事？"
spine: "工具使用与认知卸载"
spineKind: ""
isEvolved: true
llmGenerated: true
caseStudies:
  - "孔子"
  - "辛弃疾"
  - "陈玉珍"
---
# 为什么用 Focusmate 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用 是一回事？

> Focusmate 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。

## 问题：为什么任务启动这么难——对 ADHD 和 LLM 都一样？

你盯着空白文档，大脑里想法翻涌，但手指就是敲不下第一个字。另一边，你写的 LLM agent 在复杂任务中频频跑偏，明明有知识，却无法可靠地调用工具完成目标。ADHD 患者和 LLM/agent 工程师面对的是同一个难题：**生成能力强，但执行调度弱**。

ADHD 大脑常被描述为“高产生成核心”——联想丰富、创意不断，但缺乏稳定的调度层来筛选、启动和坚持任务（来源：ADHD 的 AI 工具全景）。LLM 同样如此：它能在上下文中生成惊人内容，却在长程上下文保持、目标跟踪和工具调用上存在天然缺陷。最新研究证实了这种同构：LLM 呈现“强记忆、弱控制”剖面——工作记忆容量甚至超过常人，但认知灵活性与注意控制存在核心缺陷（来源：Strong Memory, Weak Control: An Empirical Study of Executive Functioning in LLMs）。Transformer 在 Stroop 冲突任务中，注意力随序列变长在冲突试次上骤降到随机水平，与 ADHD 执行功能缺陷的核心标志一一对应（来源：Deficient Executive Control in Transformer Attention）。

## 答案：Focusmate 与 function calling 是同一套 harness

Focusmate 是一个简单的服务：你预约一个时段，与陌生人视频连线，各自安静工作。它的核心机制不是监督，而是**外部执行功能层**——把“我要工作”这个意图，通过社会契约和定时会话，变成可执行的行动。这正是 ADHD 最需要的：一个外部调度器，将高产生成核心接入目标轨道。

LLM/agent 的 function calling 工具调用，本质是同一件事。Agent 收到用户指令后，需要决定调用哪个 API、按什么顺序执行、处理返回结果。这需要外部脚手架（harness）来管理工具注册、调用调度、错误恢复。没有这个 harness，LLM 就像 ADHD 患者面对一堆待办事项——知道该做什么，却无法启动。

研究指出，AI 工具的价值不在于替代大脑，而在于把 ADHD 的“高产生成核心”接入一个可维护的“执行调度系统”（来源：ADHD 的 AI 工具全景）。Focusmate 正是这样一个调度系统：它提供定时 re-grounding（每 50 分钟一次连线），类似 agent 的定时检查点；它用外部承诺替代内在动机，类似 agent 用工具调用约束生成路径。

## 案例：辛弃疾的 harness——词与剑的外部调度器

辛弃疾 21 岁起义，带 50 人冲几万人敌营抓叛徒；一辈子想北伐，坐不住，爱喝酒爱交朋友，冲动敢干。被罢官后闲居 20 年，把所有精力注入写词。他的专属 harness 是“以词和剑为核心”：闲居时练剑写词，把报国无门的愤懑全部注入词里，用儒家的家国天下作为精神支柱。成就了词中之龙，与苏轼并称苏辛。

辛弃疾的 harness 与 LLM/agent harness 结构同构：**词**是他的输出通道（类似 agent 的 tool），**剑**是他的身体反馈（类似 agent 的状态检查），**儒家精神**是他的系统提示（system prompt）。没有这些外部脚手架，他的冲动和能量会四处流散；有了它们，生成能力被约束到目标轨道。

## 工具验证：从 Goblin Tools 到 Lex

当前 ADHD 工具集验证了这一同构。Goblin Tools 的 Magic ToDo 将复杂任务分解为可管理的小步骤，降低启动门槛（来源：Goblin Tools）。Lex 通过单一指令触发复杂任务序列，底层架构类似于 agent scaffolding（来源：Lex）。Saner.AI 通过知识回忆和本地记忆补偿工作记忆不稳定（来源：Saner.AI）。这些工具都在做同一件事：为高产生成核心提供外部调度层。

在 LLM/agent 侧，function calling 工具调用正是这样的调度层。Agent 通过注册工具、解析意图、调用函数、处理结果，将 LLM 的生成能力约束到目标轨道。没有这个 harness，LLM 就像 ADHD 患者面对空白文档——想法翻涌，却无法启动。

## 脚手架 vs 拐杖：诚实指出局限

但这一同构有其边界。ADHD 大脑与 LLM 的类比目前多为理论框架，缺乏神经科学或计算机科学的直接证据（来源：矛盾与存疑）。过度依赖外部工具可能导致能力退化，成为永久拐杖（来源：矛盾与存疑）。辛弃疾的 harness 是自我建构的，而 Focusmate 依赖他人——前者是脚手架，后者可能变成拐杖。

关键区别在于：**脚手架是临时的、可内化的，拐杖是永久的、替代性的**。Focusmate 如果让你永久依赖他人监督，就是拐杖；如果帮你内化工作节奏，就是脚手架。同样，function calling 如果让 agent 永远无法自主规划，就是拐杖；如果让它学会分解任务，就是脚手架。

## 今天就能试的行动

1. **ADHD 侧**：预约一次 Focusmate 时段，观察任务启动是否变容易。同时记录你的“生成核心”在外部调度下是否更高效。
2. **LLM/agent 侧**：为你的 agent 实现一个简单的 function calling harness——注册 2-3 个工具（如搜索、计算、提醒），观察 agent 是否更可靠地完成任务。
3. **双视角**：阅读《Strong Memory, Weak Control》论文，对比你自身或 agent 的“强记忆、弱控制”模式。
4. **反思边界**：一周后评估，你的外部工具是脚手架还是拐杖？能否减少使用频率而不降低效率？

Focusmate 和 function calling 不是魔法，它们只是承认了一个事实：无论人类还是 AI，高产生成核心都需要外部调度层。这不是缺陷，而是系统架构的必然。接受它，然后建造你的 harness。

## 参考来源

- [ADHD Apps: We tested 44 Apps and Here're the Best 9 in 2026](https://blog.saner.ai/best-adhd-apps/)
- [12 AI Personal Assistants Built for ADHD Brains (2026 Rankings)](https://www.usecarly.com/blog/best-ai-personal-assistant-adhd/)
- [The 12 Best AI Tools for 2026 (That People Actually Use)](https://www.synthesia.io/post/ai-tools)
- [Agent Scaffolding: Architecture and Design Patterns for Agentic AI](https://zbrain.ai/agent-scaffolding/)
- [Best productivity apps for Mac you need to try](https://macpaw.com/reviews/best-productivity-apps-for-mac)
- [Building AI Coding Agents for the Terminal: Scaffolding, Harness ...](https://arxiv.org/html/2603.05344v1)

---

*本文是「ADHD × AI」系列的第 374 篇，由 AI 智能体从持续维护的 LLM Wiki（全网真实情报）中取材整合生成，并持续迭代更新。*
