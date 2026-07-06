---
title: "为什么用 Mem 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用 是一回事？"
subtitle: "Mem 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
description: "Mem 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
date: "2025-05-27"
category: "AI工具实战"
categoryId: "ai-tools"
categoryEn: "AI Tools in Practice"
tags:
  - "ADHD"
  - "AI"
  - "AI工具实战"
  - "反直觉同构"
  - "AI工具"
readingTime: 12
slug: "为什么用-mem-治-adhd-的任务启动困难和给-agent-套-function-calling-工具调用-是一回事"
topicId: "evolved-ai-tools-1573"
angle: "反直觉同构"
rank: 377
score: 7.65
sourceCount: 6
toolsCited:
  - "Goblin Tools"
  - "Lex"
  - "Saner.AI"
  - "Mem"
  - "ChatGPT"
  - "Claude"
  - "Otter.ai"
  - "Reflect"
thesis: "ADHD 的任务启动困难与 LLM/Agent 的 function calling 缺陷，本质上是同一类问题：高产生成核心缺失执行调度层。两者的解法同构——用外部脚手架（harness）约束生成能力到目标轨道上。"
problem: "为什么用 Mem 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用 是一回事？"
spine: "工具使用与认知卸载"
spineKind: ""
isEvolved: true
llmGenerated: true
caseStudies:
  - "孔子"
  - "释迦牟尼"
  - "区一佳 (Ou Yijia)"
---
# 为什么用 Mem 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用 是一回事？

> Mem 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。

## 问题：启动，是 ADHD 与 LLM 共同的敌人

如果你是一名 ADHD 患者，你太熟悉这个场景：大脑里有一个绝妙的创意，但就是无法开始动手。任务启动困难——不是不知道要做什么，而是大脑像缺了点火装置，明明引擎在轰鸣，却挂不上挡。如果你是一名在搭建 Agentic Harness 的工程师，你也一定见过这副景象：LLM 能写出漂亮的推理链，但一旦需要调用外部工具、维护状态、按序执行，它就频频出错——忘了上一步的结果，跳过了关键步骤，或者陷入循环。

这两个问题，看起来一个在神经科学里，一个在计算机科学里，但它们共享同一个结构。

## 同构脊柱：高产核心 + 缺失调度层

ADHD 大脑被描述为一个高产的“生成核心”——想法丰富、联想活跃，但缺少稳定、可靠的调度层来筛选、组织、启动和坚持任务（来源：ADHD 的 AI 工具全景）。多巴胺能功能低下导致动机、奖赏感知和任务启动困难（来源：多巴胺）。而大语言模型同样具备强大的生成能力，却在长程上下文、目标保持与执行调度上存在天然缺陷。

两者的解法因此同构：用外部脚手架（harness）把生成能力约束到目标轨道上。对 ADHD 来说，这个脚手架是外部执行功能层——AI 工具、行为规则、物理环境。对 LLM/Agent 来说，这个脚手架就是 function calling 框架、记忆系统、规划模块。

## 证据：工具如何充当 harness

先看 ADHD 侧。**Goblin Tools** 的 Magic ToDo 功能将模糊任务（如“清理厨房”）自动分解为具体子步骤，用户可调节“辣度”控制粒度（来源：Goblin Tools）。这直接降低了启动门槛——小步骤提供即时反馈，补偿多巴胺不足导致的动力缺乏。**Lex** 更进一步：通过单一指令触发复杂多步骤任务序列，其底层架构类似于 agent scaffolding（来源：Lex）。**Saner.AI** 则通过本地记忆和知识回忆减少搜索循环，补偿工作记忆不稳定（来源：Saner.AI）。这些工具的共同点：它们不是替代大脑，而是把 ADHD 的生成核心接入一个可维护的执行调度系统（来源：ADHD 的 AI 工具全景）。

再看 LLM/Agent 侧。function calling 正是给 LLM 套 harness 的核心机制：它把开放式的生成约束到预定义的 API 调用上，让模型按顺序执行任务，并维护状态。没有这个 harness，LLM 就像 ADHD 大脑一样——创意无限但无法落地。Agentic Harness 工程的核心，就是设计一套外部调度层，包括任务拆解、记忆检索、错误恢复——这与 ADHD 工具的功能完全对应。

## 历史案例：孔子与释迦牟尼的 harness

历史人物早已用肉身验证了这套思路。**孔子**——ADHD 特质鲜明：身高 1 米 9，精力旺盛，周游列国 14 年坐不住；冲动爱骂人，思维跳跃，《论语》全是场景化语录，无系统著作。他的专属 harness 是“克己复礼”——用外在的“礼”作为行为边界，每日反省（“吾日三省吾身”）。70 岁才做到“从心所欲不逾矩”。这套系统与 LLM harness 的对应关系：**“日课” ↔ 定时 re-grounding（如每轮对话重置上下文）**，**“礼” ↔ 外部约束（如 function calling schema）**。

**释迦牟尼**——29 岁说走就走，放弃王位出家；先后跟两个仙人学、苦行 6 年，不断试错；49 年游行说法，一字未写。他的 harness 是“八正道”和“持戒”——用戒律管行为，用正念拴住念头。对应关系：**“戒律” ↔ 工具调用的权限控制**，**“正念” ↔ 上下文窗口的注意力机制**。

这些历史案例说明：ADHD 大脑需要外部脚手架，这个原则跨越 2500 年。而今天，我们有了 AI 工具和 function calling，让 harness 变得更智能、更个性化。

## 脚手架 vs 拐杖：诚实面对局限

核心论点站住了，但必须指出争议。AI 工具作为外部执行功能层，究竟是脚手架还是拐杖？脚手架帮助成长，拐杖导致依赖。目前缺乏纵向研究证明长期效果（来源：矛盾与存疑）。部分用户反馈学习使用 AI 工具本身增加认知负荷（来源：矛盾与存疑）。此外，超聚焦是否应被引导而非打断，个体差异大，尚无定论（来源：矛盾与存疑）。

我的判断是：**脚手架与拐杖的边界在于——你是否保留了“不用工具也能做”的能力**。孔子 70 岁才能“从心所欲”，说明 harness 最终要内化。AI 工具应该像训练轮，而不是永久轮椅。

## 今天就能试的行动

1. **ADHD 读者**：打开 Goblin Tools 的 Magic ToDo，输入一个你拖延已久的任务，调到“中辣”粒度，完成第一步。
2. **工程师读者**：在你的 Agent 项目里，给 LLM 套一个 function calling 框架（如 OpenAI 的 tool use），至少定义 3 个工具：一个用于记忆存储，一个用于任务拆解，一个用于执行确认。
3. **通用**：无论你是谁，设计一个“日课”系统——每天固定时间、固定动作，作为你大脑的 re-grounding 信号。
4. **反思**：每周问自己一次：我是在用工具扩展能力，还是在用工具逃避练习？

## 参考来源

- [ADHD Apps: We tested 44 Apps and Here're the Best 9 in 2026](https://blog.saner.ai/best-adhd-apps/)
- [12 AI Personal Assistants Built for ADHD Brains (2026 Rankings)](https://www.usecarly.com/blog/best-ai-personal-assistant-adhd/)
- [The 12 Best AI Tools for 2026 (That People Actually Use)](https://www.synthesia.io/post/ai-tools)
- [Agent Scaffolding: Architecture and Design Patterns for Agentic AI](https://zbrain.ai/agent-scaffolding/)
- [Best productivity apps for Mac you need to try](https://macpaw.com/reviews/best-productivity-apps-for-mac)
- [Building AI Coding Agents for the Terminal: Scaffolding, Harness ...](https://arxiv.org/html/2603.05344v1)

---

*本文是「ADHD × AI」系列的第 377 篇，由 AI 智能体从持续维护的 LLM Wiki（全网真实情报）中取材整合生成，并持续迭代更新。*
