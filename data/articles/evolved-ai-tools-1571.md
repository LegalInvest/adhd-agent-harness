---
title: "为什么用 Structured 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用 是一回事？"
subtitle: "Structured 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
description: "Structured 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
date: "2025-03-09"
category: "AI工具实战"
categoryId: "ai-tools"
categoryEn: "AI Tools in Practice"
tags:
  - "ADHD"
  - "AI"
  - "AI工具实战"
  - "反直觉同构"
  - "自动化"
readingTime: 11
slug: "为什么用-structured-治-adhd-的任务启动困难和给-agent-套-function-calling-工具调用-是一回事"
topicId: "evolved-ai-tools-1571"
angle: "反直觉同构"
rank: 375
score: 7.65
sourceCount: 6
toolsCited:
  - "Goblin Tools"
  - "Lex"
  - "Saner.AI"
  - "Focusmate"
  - "ChatGPT"
  - "Claude"
thesis: "ADHD 的任务启动困难与 LLM/agent 的 function calling 缺陷，本质都是「高产生成核心缺乏可靠调度层」的同一类问题，因此用 structured 脚手架（如任务分解、外部记忆、定时问责）来治理两者，是同一套 harness 工程。"
problem: "为什么用 Structured 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用 是一回事？"
spine: "工具使用与认知卸载"
spineKind: ""
isEvolved: true
llmGenerated: true
caseStudies:
  - "孔子"
  - "曹植"
  - "James Mishreki"
---
# 为什么用 Structured 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用 是一回事？

> Structured 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。

你坐在电脑前，盯着一个空白文档，大脑里塞满了想法，但就是无法打出第一个字。另一边，你调用的 LLM agent 收到指令后，像脱缰野马一样生成了三页无关内容，完全偏离了原始目标。这两件事——ADHD 的任务启动困难，和 agent 的 function calling 跑偏——听起来风马牛不相及，但它们的底层结构完全同构：都是一个高产的生成核心，却缺少一个可靠的执行调度层（来源：ADHD 大脑与 LLM 的同构）。治理它们的解法，也因此是一回事：用 structured 脚手架（harness）把生成能力约束到目标轨道上。

## 问题：大脑与模型共享的「启动瘫痪」

ADHD 大脑常被描述为一个高产的生成核心——想法丰富、联想活跃，但缺少稳定、可靠的调度层来筛选、组织、启动和坚持任务（来源：ADHD 的 AI 工具全景）。这种「启动瘫痪」的根源在于执行功能缺陷，尤其是工作记忆瓶颈：ADHD 患者的工作记忆常常成为瓶颈，导致难以记住任务细节、丢失上下文（来源：工作记忆）。最新研究揭示了 ADHD 与 LLM 在工作记忆上的深层同构：明尼苏达大学系统测试 LLM 的执行功能，发现“强记忆、弱控制”剖面——工作记忆容量甚至超过常人，但认知灵活性与注意控制存在核心缺陷，无法灵活切换任务集、无法抑制自动化反应，这正是 ADHD 的经典神经心理模式（来源：工作记忆）。耶鲁大学进一步发现，自注意力机制本身导致工作记忆容量限制：随 N-back 任务 N 值增加，注意力分数熵增、注意力弥散、表现下降，与人类注意分散机制同源——“注意力资源的弥散分配”正是 ADHD 注意缺陷的计算本质（来源：工作记忆）。

这意味着，LLM 和 ADHD 大脑一样，不是缺乏生成能力，而是缺乏一个能稳定调度这些能力的 orchestration 层——在 agent 语境下，就是 function calling 工具调用。当 agent 无法正确选择或调用工具时，它就会像 ADHD 患者一样，在任务启动时卡住，或者跑偏。

## 解药：同一套 harness 工程

既然问题同构，解法也同构。所谓的结构化脚手架（structured harness），就是为生成核心搭建一个外部执行调度系统。在 ADHD 侧，这表现为任务分解、外部记忆、身体在场效应等策略；在 LLM/agent 侧，这表现为 function calling 工具调用、外部知识库、定时 re-grounding 等机制。

以 Goblin Tools 为例，它的 Magic ToDo 功能将复杂任务自动分解为可管理的小步骤，并允许用户调节“辣度”控制分解粒度（来源：Goblin Tools）。这本质上就是一个任务拆解调度器——把“清理厨房”这样的模糊目标，转化为“把碗放进洗碗机”“擦台面”“拖地”等可执行步骤。在 agent 侧，这对应着将复杂目标分解为一系列 function call 的规划机制（来源：Lex）。Lex 允许用户通过单一指令触发复杂、多步骤的任务序列，其底层架构类似于 agent scaffolding——围绕大语言模型构建软件架构和工具，使其能够执行复杂、目标驱动的任务（来源：Lex）。两者都在做同一件事：把高层次的意图，拆解为低层次的、可执行的原子操作。

再看外部记忆与知识管理。Saner.AI 通过增强知识回忆，帮助用户快速找回信息，减少搜索循环和标签切换（来源：Saner.AI）。这直接补偿了 ADHD 的工作记忆缺陷。在 agent 侧，这对应着外部知识库和长期记忆机制——当 agent 的上下文窗口有限时，它需要外挂一个记忆系统来维持任务上下文。两者都是认知卸载：把本应由大脑（或模型）维持的信息，交给外部系统存储和检索。

身体在场效应（Body Doubling）是 ADHD 侧最有效的策略之一：有另一个人（物理或虚拟）在场时，即使不直接互动，也能显著提升专注度和执行力（来源：身体在场效应）。AI 驱动的工具如 Focusmate 利用算法匹配虚拟身体加倍伙伴，实现“AI 匹配的身体加倍”（来源：身体在场效应）。在 agent 侧，这对应着定时 re-grounding 和外部问责——比如让 agent 每完成一个步骤就向用户报告进度，或者设置一个“监督 agent”来检查输出是否偏离目标。定期问责检查可将目标达成可能性从 25% 提升至 95%（来源：身体在场效应），这在 ADHD 和 agent 两边都成立。

## 人物案例：孔子与曹植的 harness 系统

孔子是 ADHD 特质与 harness 系统的经典案例。他身高 1 米 9，精力旺盛，周游列国 14 年坐不住；冲动爱骂人，见南子急得对天发誓，骂宰予朽木不可雕；对音乐超专注到三月不知肉味，对种地等俗事零耐心；思维跳跃，《论语》全是场景化语录，无系统著作。他的专属 harness 是“克己复礼”——用外在的“礼”作为行为边界，每日反省，“吾日三省吾身”。70 岁才做到从心所欲不逾矩，一辈子和自己的冲动做斗争。这个“礼”系统，本质上就是一个外部调度层：它把孔子的高产生成核心（思想、教学、政治抱负）约束到社会可接受的轨道上。在 LLM/agent 侧，这对应着 function calling 的 schema 和约束——用预定义的函数签名、参数类型、调用顺序，来约束模型的输出，防止它跑偏。孔子的“日课”相当于定时 re-grounding，而他的“秘书”（如果有的话）则相当于外部调度器。

曹植则是另一个例子。他文学超专注，铜雀台作赋一挥而就；但对政治零兴趣，冲动，醉闯司马门，醉酒不能受命救曹仁；情绪波动大，在冲动和后悔间循环。他的 harness 是以诗赋为核心，把所有政治上的失意注入诗歌，用酒精麻痹自己，在文学世界里找到寄托。这个 harness 虽然不健康（酒精），但它确实起到了约束和疏导作用——把曹植的生成能量（文学才华）引导到一个特定领域。在 agent 侧，这对应着给 LLM 一个明确的输出格式和领域限制，比如“只输出 JSON”或“只调用天气 API”。

## 脚手架 vs 拐杖：诚实的边界

这里必须诚实指出一个争议：AI 工具到底是“外部执行功能层”还是“拐杖”？核心论点认为 AI 作为外部执行功能层补偿缺陷，但过度依赖可能导致能力退化，成为永久拐杖（来源：矛盾与存疑）。长期依赖风险缺乏实证，需更多纵向研究（来源：矛盾与存疑）。我的判断是：脚手架与拐杖的边界在于是否可迁移。一个好的 harness 应该教会用户（或 agent）如何自己搭建结构，而不是永远依赖外部系统。比如，Goblin Tools 的任务分解功能，如果用户学会了分解方法，即使没有工具也能自己拆解任务，那它就是脚手架；如果用户永远只能靠工具才能启动，那就是拐杖。同样，agent 的 function calling 如果只是硬编码调用，而没有让模型学会从错误中调整，那也只是拐杖。

## 今天就能试的行动

1. **ADHD 侧**：用 Goblin Tools 的 Magic ToDo 分解你卡住的任务。输入“写周报”，看它分解出的步骤，然后从第一步开始做。
2. **Agent 侧**：给 LLM 一个明确的 function calling schema。比如，让 ChatGPT 调用一个“task_breakdown”函数，输入是任务描述，输出是步骤列表。观察它是否比自由输出更聚焦。
3. **身体加倍**：用 Focusmate 或找一位朋友，约定 25 分钟一起工作。对 agent，可以设置一个每 5 分钟输出一次进度报告的“监督 agent”。
4. **外部记忆**：用 Saner.AI 或类似工具捕获灵感和任务，减少大脑的存储负担。对 agent，外挂一个知识库（如向量数据库），让它每次调用前先检索相关上下文。

结构化不是限制，而是解放。无论是 ADHD 大脑还是 LLM agent，当它们被套上合适的 harness，高产生成核心才能真正释放其潜力。

## 参考来源

- [ADHD Apps: We tested 44 Apps and Here're the Best 9 in 2026](https://blog.saner.ai/best-adhd-apps/)
- [12 AI Personal Assistants Built for ADHD Brains (2026 Rankings)](https://www.usecarly.com/blog/best-ai-personal-assistant-adhd/)
- [The 12 Best AI Tools for 2026 (That People Actually Use)](https://www.synthesia.io/post/ai-tools)
- [Agent Scaffolding: Architecture and Design Patterns for Agentic AI](https://zbrain.ai/agent-scaffolding/)
- [Best productivity apps for Mac you need to try](https://macpaw.com/reviews/best-productivity-apps-for-mac)
- [Building AI Coding Agents for the Terminal: Scaffolding, Harness ...](https://arxiv.org/html/2603.05344v1)

---

*本文是「ADHD × AI」系列的第 375 篇，由 AI 智能体从持续维护的 LLM Wiki（全网真实情报）中取材整合生成，并持续迭代更新。*
