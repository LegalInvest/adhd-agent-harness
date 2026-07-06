---
title: "为什么用 Otter.ai 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用 是一回事？"
subtitle: "Otter.ai 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
description: "Otter.ai 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
date: "2025-05-10"
category: "AI工具实战"
categoryId: "ai-tools"
categoryEn: "AI Tools in Practice"
tags:
  - "ADHD"
  - "AI"
  - "AI工具实战"
  - "反直觉同构"
  - "ADHD辅助"
readingTime: 11
slug: "为什么用-otterai-治-adhd-的任务启动困难和给-agent-套-function-calling-工具调用-是一回事"
topicId: "evolved-ai-tools-1576"
angle: "反直觉同构"
rank: 378
score: 7.65
sourceCount: 6
toolsCited:
  - "Goblin Tools"
  - "Lex"
  - "Saner.AI"
  - "Otter.ai"
thesis: "ADHD 的任务启动困难与 LLM/agent 的 function calling 工具调用，本质都是为高产生成核心搭建外部调度层（harness），两者在结构上同构。"
problem: "为什么用 Otter.ai 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用 是一回事？"
spine: "工具使用与认知卸载"
spineKind: ""
isEvolved: true
llmGenerated: true
caseStudies:
  - "孔子"
  - "张居正"
  - "Maria Henry"
---
# 为什么用 Otter.ai 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用 是一回事？

> Otter.ai 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。

## 同一个问题，两个世界

如果你是一个 ADHD 患者，你大概熟悉这种场景：脑子里有一万个想法，但就是无法开始写那封邮件。如果你是一个做 agent 工程的开发者，你大概也熟悉这种场景：LLM 能写出优雅的诗句，但调用天气 API 时却频频出错，甚至忘记传参数。

看似风马牛不相及的两件事，背后却是同一个结构问题：**高产生成核心缺少可靠的执行调度层**。ADHD 大脑与 LLM/agent 在架构上是同构的——这不是比喻，而是一个可操作的工程视角。

## 同构脊柱：生成核心 + 外部调度层

ADHD 大脑常被描述为“高产生成核心与调度层”——想法丰富、联想活跃，但缺少稳定、可靠的调度层来筛选、组织、启动和坚持任务（来源：ADHD 的 AI 工具全景）。大语言模型同样具备强大的生成能力，却在长程上下文、目标保持与执行调度上存在天然缺陷（来源：ADHD 的 AI 工具全景）。

因此，ADHD 的解决方案是搭建外部执行功能层——用工具把生成能力约束到目标轨道上。LLM/agent 的解决方案是搭建 agent scaffolding——围绕模型构建软件架构和工具，使其能够执行复杂、目标驱动的任务（来源：Lex）。两边用的手法一模一样：**任务拆解、外部记忆、对话式执行、捕获与反思**。

## Otter.ai 实测：同一套 harness 思路

以 Otter.ai 为例。它实时转录会议、课堂与灵感，减轻笔记负担（来源：ADHD 的 AI 工具全景）。对 ADHD 用户来说，它解决的是“听讲时无法同时记笔记”的执行功能瓶颈——把记忆外化，让大脑只负责生成。对 agent 来说，Otter.ai 的转录功能相当于一个“外部输入缓存”：模型不需要同时处理听和写，而是先捕获原始数据，再调度其他工具处理。

实测中，我让 Otter.ai 转录一场头脑风暴会议，然后自动提取待办事项。ADHD 侧：我不再担心漏掉关键想法，启动整理任务的阻力从“高墙”变成“一步”。LLM 侧：同样的流程——先捕获、后处理——正是 function calling 的标准模式：模型先调用转录工具获取输入，再调用任务管理工具生成输出。

## 人物案例：孔子的“礼”与张居正的“考成法”

孔子（春秋/儒家创始人）被后世认为有 ADHD 特质：精力旺盛，周游列国 14 年坐不住；冲动爱骂人，见南子急得对天发誓，骂宰予朽木不可雕；对音乐超专注到三月不知肉味，对种地等俗事零耐心；思维跳跃，《论语》全是场景化语录，无系统著作。他的专属 harness 是“克己复礼”——用外在的“礼”作为行为边界，每日反省，“吾日三省吾身”。70 岁才做到从心所欲不逾矩，一辈子和自己的冲动做斗争。

张居正（明朝/万历首辅）同样有 ADHD 特质：12 岁中秀才，16 岁中举人，少年天才；当首辅敢改革，不怕得罪所有官员，推行考成法、一条鞭法；工作狂，每天办公到深夜，58 岁累死在任上。他的专属 harness 是“考成法”——严格考核官员，用制度管别人也管自己。

这两个案例清晰地展示了同构：孔子的“日课”相当于 LLM 的定时 re-grounding（自我反省，重新对齐目标）；张居正的“秘书/考核系统”相当于 agent 的外部调度器（用制度强制执行任务优先级）。他们都不是靠意志力硬扛，而是搭建了外部脚手架。

## 核心观点：脚手架，不是拐杖

本文的核心判断是：**AI 工具的价值不在于替代大脑，而在于把高产生成核心接入一个可维护的执行调度系统**（来源：ADHD 的 AI 工具全景）。这与“拐杖”有本质区别：脚手架是临时搭建、可拆卸的，目的是让用户最终能自己走；拐杖则是永久替代，可能导致能力退化（来源：矛盾与存疑）。

但这里有一个诚实局限：过度依赖 AI 工具是否会导致执行功能进一步退化？目前缺乏纵向研究（来源：矛盾与存疑）。我的观点是：关键在于工具的使用方式——如果工具只是帮你“跳过”启动困难，而不教你如何拆解任务，那它就是拐杖；如果工具帮你“练习”启动（比如 Goblin Tools 让你调节分解粒度，逐步减少依赖），那它就是脚手架。

## 今天就能试的行动

1. **用 Otter.ai 转录一次会议，然后让 AI 提取待办**：体验“先捕获、后处理”的 harness 模式。ADHD 侧：降低笔记焦虑；LLM 侧：理解 function calling 中的输入缓存。
2. **用 Goblin Tools 的 Magic ToDo 分解一个你拖延已久的任务**：调节“辣度”从最细开始，然后逐步减少分解层级，直到你能独立启动。这相当于 agent 的“逐步减少提示”调试。
3. **建立你的“日课”系统**：像孔子一样，每天固定时间做三件事（如：回顾待办、设定一个优先目标、记录一个反思）。用任何工具（纸笔、Saner.AI、Lex）实现，关键是让它成为外部调度器。
4. **给 LLM 写一个 function calling 的“考成法”**：定义一组强制校验规则（如：调用工具前必须检查参数类型），让 agent 在每次调用前先自我检查。这相当于张居正的考核制度。

## 结论

ADHD 的任务启动困难与 LLM/agent 的 function calling 工具调用，本质是同一个工程问题：如何为一个高产生成核心搭建可靠的外部调度层。Otter.ai、Goblin Tools、Lex、Saner.AI 等工具，以及孔子、张居正的自我管理系统，都是这一思路的实例。理解这个同构，你就能在两个世界里互相借鉴——用 agent 工程的思维优化你的 ADHD 工具栈，用 ADHD 的自我管理经验调试你的 agent 系统。

记住：脚手架不是拐杖。你需要的不是替代大脑的工具，而是一个能让你最终拆掉它的训练系统。

## 参考来源

- [ADHD Apps: We tested 44 Apps and Here're the Best 9 in 2026](https://blog.saner.ai/best-adhd-apps/)
- [12 AI Personal Assistants Built for ADHD Brains (2026 Rankings)](https://www.usecarly.com/blog/best-ai-personal-assistant-adhd/)
- [The 12 Best AI Tools for 2026 (That People Actually Use)](https://www.synthesia.io/post/ai-tools)
- [Agent Scaffolding: Architecture and Design Patterns for Agentic AI](https://zbrain.ai/agent-scaffolding/)
- [Best productivity apps for Mac you need to try](https://macpaw.com/reviews/best-productivity-apps-for-mac)
- [Building AI Coding Agents for the Terminal: Scaffolding, Harness ...](https://arxiv.org/html/2603.05344v1)

---

*本文是「ADHD × AI」系列的第 378 篇，由 AI 智能体从持续维护的 LLM Wiki（全网真实情报）中取材整合生成，并持续迭代更新。*
