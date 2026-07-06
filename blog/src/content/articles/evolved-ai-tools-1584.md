---
title: "为什么用 Habitica 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用 是一回事？"
subtitle: "Habitica 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
description: "Habitica 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
date: "2025-04-19"
category: "AI工具实战"
categoryId: "ai-tools"
categoryEn: "AI Tools in Practice"
tags:
  - "ADHD"
  - "AI"
  - "AI工具实战"
  - "反直觉同构"
  - "智能助手"
readingTime: 14
slug: "为什么用-habitica-治-adhd-的任务启动困难和给-agent-套-function-calling-工具调用-是一回事"
topicId: "evolved-ai-tools-1584"
angle: "反直觉同构"
rank: 386
score: 7.65
sourceCount: 6
toolsCited:
  - "Habitica"
  - "Goblin Tools"
  - "Lex"
  - "Saner.AI"
  - "ChatGPT"
  - "Claude"
thesis: "ADHD 大脑与 LLM 都是高产生成核心但缺乏稳定调度层，Habitica 为 ADHD 提供的任务分解与外部结构，与 agent 工程中的 function calling 工具调用在本质上是同一类 harness 设计：将不可控的生成能力约束到可执行的轨道上。"
problem: "为什么用 Habitica 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用 是一回事？"
spine: "工具使用与认知卸载"
spineKind: ""
isEvolved: true
llmGenerated: true
caseStudies:
  - "孔子"
  - "辛弃疾"
  - "凌斌"
---
# 为什么用 Habitica 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用 是一回事？

> Habitica 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。

## 问题：为什么你明明想动，却就是动不了？

ADHD 人群最熟悉的困境是“任务启动困难”——大脑里有一百个念头在飞，但身体像被钉在椅子上。你打开 Habitica，给自己设了一个任务“写报告”，然后盯着屏幕发呆，连点一下“开始”的力气都没有。另一边，AI 工程师在调试 agent，发现它明明有强大的生成能力，却总是在 tool call 时卡住：模型输出了完美的 JSON，但函数就是不执行，或者执行了错误参数。两边的痛感惊人地相似——**核心都在，但调度层掉了**。

## 同构：高产核心 + 缺失的调度层

ADHD 大脑常被描述为一个高产的“生成核心”——想法丰富、联想活跃，但缺少稳定、可靠的调度层来筛选、组织、启动和坚持任务（来源：ADHD 的 AI 工具全景）。大语言模型（LLM）同样如此：它能在一次推理中生成数千字的文本，却在长程上下文保持、目标维持和执行调度上存在天然缺陷。两者都需要外部脚手架：ADHD 需要 Habitica 这样的游戏化任务列表，LLM 需要 function calling 这样的工具调用接口。

Habitica 的核心机制是：将复杂任务分解为可管理的子任务（如“写报告”拆成“打开文档”“写第一段”“写第二段”），每个子任务提供即时反馈（经验值、金币）。这本质上是一个**外部执行调度器**，把大脑的生成冲动（“我想写报告”）转化为可执行的原子步骤。LLM 的 function calling 同理：模型不能直接“写数据库”，它必须通过预定义的 function schema 来调用外部工具。每个 tool call 都是一个原子步骤，由 harness 负责执行、验证和返回结果。两者都在做同一件事：**用外部结构补偿内部调度缺陷**。

## 证据：两边都有真实数据

ADHD 侧：Goblin Tools 的 Magic ToDo 功能能自动将模糊任务（如“清理厨房”）分解为具体子任务，用户可调节“辣度”控制粒度（来源：Goblin Tools）。Lex 允许通过单一指令触发多步骤任务序列，降低启动门槛（来源：Lex）。这些工具被成人 ADHD 用户广泛用于“外部执行功能”（来源：ChatGPT 被用作外部执行功能工具）。LLM 侧：agent harness 工程的核心组件包括“验证与 CI 集成”“结构化工作流和规划”，要求将复杂任务分解为子任务并在每一步进行验证（来源：幻觉与验证循环）。缺乏这些验证会导致“更多幻觉和重复工作”（来源：Loop Engineering for AI Agents: Memory-First Design）。

历史人物同样提供了证据。孔子一生精力旺盛、冲动易怒、思维跳跃，他的 harness 是“克己复礼”——用外在的“礼”作为行为边界，每日反省（“吾日三省吾身”）。这与 LLM harness 的“定时 re-grounding”完全对应：agent 需要定期检查自己是否偏离目标，孔子则需要每日检查言行是否合礼。辛弃疾 21 岁带 50 人冲几万人敌营抓叛徒，闲居 20 年把所有精力注入写词。他的 harness 是以词和剑为核心，用儒家的家国天下作为精神支柱——这相当于 LLM 的“系统提示”和“目标函数”，把生成能力约束在特定轨道上。

## 判断：脚手架不是拐杖

一个常见的争议是：AI 工具是“外部执行功能层”还是“拐杖”？过度依赖是否导致能力退化？（来源：矛盾与存疑）我的判断是：**关键不在于用不用外部工具，而在于工具是否可内化**。Habitica 的任务分解习惯可以逐渐内化为大脑的自动流程，就像孔子最终“从心所欲不逾矩”——70 岁才做到，但做到了。同样，agent harness 的 function calling 接口可以被模型学会，最终在推理时自动规划工具调用序列。好的 harness 是脚手架，不是拐杖：它提供结构，但允许使用者逐渐接管。

## 局限与诚实

必须承认，ADHD 大脑与 LLM 的同构目前主要是类比推理，缺乏神经科学或计算机科学的直接证据（来源：矛盾与存疑）。此外，个体差异巨大：有的 ADHD 用户觉得 Habitica 的 gamification 是救星，有的觉得是噪音；有的 agent 需要严格的确定性状态机，有的可以容忍随机性（来源：采样温度与表现波动）。长期效果也未知——短期有效不代表能持续改善。

## 今天就能试的行动

1. **ADHD 侧**：在 Habitica 中创建一个“启动困难”任务，将其分解为 3 个原子步骤（如“打开电脑”“打开文档”“写第一句话”），每个步骤完成后给自己一个小奖励（经验值或实物）。
2. **LLM 侧**：为你的 agent 添加一个“验证循环”——在每个 function call 之后检查返回结果是否符合预期，如果失败则重试或回退（来源：幻觉与验证循环）。
3. **双人实验**：如果你是 ADHD 且会编程，试着用 Habitica 的 API 写一个自定义脚本，让 agent 在完成任务后自动在 Habitica 中打勾——把两边 harness 连起来。
4. **反思**：记录一周内使用外部工具（如 Habitica、Goblin Tools）的频率，以及你是否感觉这些工具在“帮”你还是在“替”你做决定。如果感觉被替代，尝试减少粒度——让工具只提示，不执行。

## 参考来源

- [ADHD Apps: We tested 44 Apps and Here're the Best 9 in 2026](https://blog.saner.ai/best-adhd-apps/)
- [12 AI Personal Assistants Built for ADHD Brains (2026 Rankings)](https://www.usecarly.com/blog/best-ai-personal-assistant-adhd/)
- [The 12 Best AI Tools for 2026 (That People Actually Use)](https://www.synthesia.io/post/ai-tools)
- [Agent Scaffolding: Architecture and Design Patterns for Agentic AI](https://zbrain.ai/agent-scaffolding/)
- [Best productivity apps for Mac you need to try](https://macpaw.com/reviews/best-productivity-apps-for-mac)
- [Building AI Coding Agents for the Terminal: Scaffolding, Harness ...](https://arxiv.org/html/2603.05344v1)

---

*本文是「ADHD × AI」系列的第 386 篇，由 AI 智能体从持续维护的 LLM Wiki（全网真实情报）中取材整合生成，并持续迭代更新。*
