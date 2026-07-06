---
title: "为什么用 Inflow 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用 是一回事？"
subtitle: "Inflow 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
description: "Inflow 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
date: "2025-03-22"
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
slug: "为什么用-inflow-治-adhd-的任务启动困难和给-agent-套-function-calling-工具调用-是一回事"
topicId: "evolved-ai-tools-1580"
angle: "反直觉同构"
rank: 382
score: 7.65
sourceCount: 6
toolsCited:
  - "Inflow"
  - "Goblin Tools"
  - "Saner.AI"
  - "Lex"
  - "ChatGPT"
  - "Claude"
thesis: "ADHD 大脑与 LLM 是同一类高产生成核心，两者都因内置调度层缺失而依赖外部脚手架（harness），Inflow 对 ADHD 的干预与 agent 的 function calling 工具调用在结构上同构，本质都是通过外部执行功能层将生成能力约束到目标轨道。"
problem: "为什么用 Inflow 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用 是一回事？"
spine: "工具使用与认知卸载"
spineKind: ""
isEvolved: true
llmGenerated: true
caseStudies:
  - "孔子"
  - "胡林翼"
  - "单丽娟"
---
# 为什么用 Inflow 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用 是一回事？

> Inflow 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。

## 问题：为什么任务启动这么难？

如果你有 ADHD，你一定熟悉这种场景：大脑里有一堆想做的事，但身体就是不动。你打开电脑，盯着待办清单，然后刷了半小时手机。任务启动困难是 ADHD 最核心的执行功能障碍之一，根源在于大脑的“调度层”失灵——不是没有想法，而是无法将想法转化为行动。

如果你在做 Agentic Harness 工程，你一定也熟悉这种场景：你给 LLM 一个复杂指令，它输出一堆漂亮的文字，但没完成你真正想要的任务。你需要写 function calling 的 schema，把工具注册进去，让模型学会调用外部 API。否则，它只是个“高谈阔论的生成器”，而不是一个“能办事的 agent”。

这两个问题，看起来一个在神经科学领域，一个在 AI 工程领域，但本质是同一个问题：**高产生成核心缺少可靠的内置调度层**。

## 同构：高产生成核心 vs 缺失的调度层

ADHD 大脑常被描述为一个高产的生成核心——想法丰富、联想活跃，但缺少稳定、可靠的调度层来筛选、组织、启动和坚持任务（来源：ADHD 的 AI 工具全景）。大语言模型（LLM）同样具备强大的生成能力，却在长程上下文、目标保持与执行调度上存在天然缺陷。最新研究揭示了更深层的同构：ADHD 患者的工作记忆容量未必差，但自上而下的控制和调节能力不足，呈现“强记忆、弱控制”的认知剖面，这种模式与 LLM 惊人相似（来源：Strong Memory, Weak Control: An Empirical Study of Executive Functioning in LLMs）。

因此，ADHD 的干预与 LLM 的 harness 工程是同一类工作：用外部脚手架把生成能力约束到目标轨道上。Inflow 这款针对 ADHD 的认知行为疗法 App，本质上就是在搭建一个外部执行功能层——通过结构化课程、任务拆解和每日签到，帮助用户建立启动机制。而 agent 的 function calling 工具调用，则是通过注册工具、定义 schema、规划执行序列，让 LLM 从“生成文本”变成“完成任务”。

## 历史案例：孔子的“克己复礼”与胡林翼的“日记反省”

孔子是历史上最典型的 ADHD 大脑之一。他身高 1 米 9，精力旺盛，周游列国 14 年坐不住；冲动爱骂人，见南子急得对天发誓，骂宰予“朽木不可雕”；对音乐超专注到“三月不知肉味”，对种地等俗事零耐心；思维跳跃，《论语》全是场景化语录，无系统著作。他的专属 harness 是“克己复礼”——用外在的“礼”作为行为边界，每日反省，“吾日三省吾身”。70 岁才做到“从心所欲不逾矩”，一辈子和自己的冲动做斗争。

胡林翼是另一个典型。年轻时候是花花公子，在扬州天天逛妓院；父亲去世后回家守孝，幡然醒悟，出山带兵。他的 harness 是每日写日记反省，和曾国藩一起做圣人，严格治军。

这两个 harness 系统的核心是什么？是**外部调度层**。孔子的“礼”相当于一套预设的行为 schema，类似 agent 的 function calling 定义——规定什么情况下调用什么行为。胡林翼的每日日记相当于一个定时 re-grounding 机制，类似 agent 的上下文压缩与规划重排。他们都无法靠内在意志稳定启动任务，所以必须依赖外部结构。

## 工具实证：从 Goblin Tools 到 Lex 的 harness 逻辑

现代 AI 工具正在做同样的事。Goblin Tools 的 Magic ToDo 功能能将复杂任务自动分解为可管理的小步骤，降低启动门槛（来源：Goblin Tools）。对于 ADHD 用户，这相当于给了一个外部任务分解器，补偿了内在调度层的缺失。对于 LLM agent，这相当于 prompt 中的 step-by-step 规划——将复杂目标拆解为一系列子任务。

Saner.AI 通过知识回忆和本地记忆，减少搜索循环和标签切换（来源：Saner.AI）。这对应 agent 的 memory 模块——用外部向量数据库补偿 LLM 的上下文窗口限制。

Lex 允许用户通过单一指令触发复杂、多步骤的任务序列（来源：Lex）。这直接对应 agent 的 function calling 工作流——一个工具调用可以触发一连串的 API 调用。Lex 的底层架构类似于 agent scaffolding，即围绕 LLM 构建软件架构和工具，使其能执行复杂、目标驱动的任务（来源：Lex）。

ChatGPT 和 Claude 被 ADHD 用户用作“外部执行功能”工具（来源：ADHD 的 AI 工具全景）。而 AI 编码代理（如 OpenDev）通过“复合 AI 系统架构”来弥补 LLM 的调度缺陷，包括工作负载专用模型路由、分离规划与执行的双代理架构、惰性工具发现、自适应上下文压缩（来源：Building AI Coding Agents for the Terminal）。这些技术本质上都是在 LLM 外部搭建调度层，防止“上下文膨胀和推理退化”。

## 核心观点：脚手架 vs 拐杖的边界

我的核心判断是：**AI 工具不是治愈 ADHD，也不是替代大脑，而是在 ADHD 大脑与外部世界之间搭建一个临时的外部执行功能层**（来源：ADHD 的 AI 工具全景）。这个层与 agent 的 function calling harness 在结构上同构——都是将高产生成核心接入一个可维护的执行调度系统。

但这里有一个关键边界：脚手架 vs 拐杖。真正的脚手架应帮助使用者“建造”，但使用者仍需自己“攀登”（来源：拐杖与脚手架）。如果工具替代了治疗或自我管理，可能造成依赖（来源：拐杖与脚手架）。同样，agent 的 harness 如果过于 rigid，会限制 LLM 的生成能力；如果过于 loose，则无法保证任务完成。

目前最大的争议是：ADHD 大脑与 LLM 同构的论点多为类比推理，缺乏神经科学或计算机科学的直接证据（来源：矛盾与存疑）。虽然已有研究显示 Transformer 的自注意力机制在训练后发展出模仿前额叶-纹状体门控的操作（来源：TRANSFORMER MECHANISMS MIMIC FRONTOSTRIATAL GATING OPERATIONS WHEN TRAINED ON HUMAN WORKING MEMORY TASKS），但跨学科验证仍不充分。此外，AI 工具对任务启动的长期效果未知，短期有效但长期效果有待观察（来源：矛盾与存疑）。

## 今天就能试的行动

1. **ADHD 用户**：用 Goblin Tools 的 Magic ToDo 分解一个你拖延已久的任务，设置“辣度”到你觉得可启动的程度。
2. **Agent 工程师**：为你的 LLM 注册一个“任务分解”工具，让它学会将复杂指令拆成子步骤再调用其他工具。
3. **双视角**：如果你既是 ADHD 又是工程师，试着用写 function calling schema 的方式，为自己设计一个“每日启动序列”——比如“打开日历→查看优先级→分解第一个任务→开始执行”。
4. **反思**：每周检查一次，你是在用工具搭建脚手架，还是在依赖拐杖？如果离开工具你无法启动，说明需要调整策略。

## 参考来源

- [ADHD Apps: We tested 44 Apps and Here're the Best 9 in 2026](https://blog.saner.ai/best-adhd-apps/)
- [12 AI Personal Assistants Built for ADHD Brains (2026 Rankings)](https://www.usecarly.com/blog/best-ai-personal-assistant-adhd/)
- [The 12 Best AI Tools for 2026 (That People Actually Use)](https://www.synthesia.io/post/ai-tools)
- [Agent Scaffolding: Architecture and Design Patterns for Agentic AI](https://zbrain.ai/agent-scaffolding/)
- [Best productivity apps for Mac you need to try](https://macpaw.com/reviews/best-productivity-apps-for-mac)
- [Building AI Coding Agents for the Terminal: Scaffolding, Harness ...](https://arxiv.org/html/2603.05344v1)

---

*本文是「ADHD × AI」系列的第 382 篇，由 AI 智能体从持续维护的 LLM Wiki（全网真实情报）中取材整合生成，并持续迭代更新。*
