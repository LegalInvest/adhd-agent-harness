---
title: "为什么用 Todoist 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用 是一回事？"
subtitle: "Todoist 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
description: "Todoist 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
date: "2025-04-20"
category: "AI工具实战"
categoryId: "ai-tools"
categoryEn: "AI Tools in Practice"
tags:
  - "ADHD"
  - "AI"
  - "AI工具实战"
  - "反直觉同构"
  - "ADHD辅助"
readingTime: 7
slug: "为什么用-todoist-治-adhd-的任务启动困难和给-agent-套-function-calling-工具调用-是一回事"
topicId: "evolved-ai-tools-1579"
angle: "反直觉同构"
rank: 381
score: 7.65
sourceCount: 6
toolsCited:
  - "Todoist"
  - "Goblin Tools"
  - "Saner.AI"
  - "Lex"
thesis: "ADHD 大脑与 LLM 共享同一困境：生成核心强大但执行调度层缺失。因此，用 Todoist 等工具辅助任务启动，与给 agent 套 function calling harness，本质都是通过外部脚手架补偿内在缺陷——两者是同一套工程逻辑的镜像。"
problem: "为什么用 Todoist 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用 是一回事？"
spine: "工具使用与认知卸载"
spineKind: ""
isEvolved: true
llmGenerated: true
---
# 为什么用 Todoist 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用 是一回事？

> Todoist 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。

## 问题：为什么“开始做”比“做什么”难一万倍？

如果你是 ADHD 患者，你一定经历过这种场景：脑子里有一长串待办事项，但身体像被钉在椅子上，无法动弹。你打开 Todoist，看着“整理报告”这个任务，光标闪烁，大脑一片空白。十分钟后，你刷完了三个短视频，任务纹丝不动。

如果你是 Agent 工程师，你一定也经历过这种场景：你精心设计了一个 LLM 代理，给它配置了十几个 function calling 工具，但它就是“不调用”——或者调用了错误的工具，或者陷入推理循环，把简单问题复杂化。你检查日志，发现它“知道”该做什么，但“做不到”。

两群人，两个世界，同一个痛点：**生成核心（智力/算力）在线，但执行调度层（启动/调用）掉线。** 本文要论证一个反直觉的结论：ADHD 患者用 Todoist 治任务启动困难，和工程师给 agent 套 function calling harness，是同一件事。

## 同构：一个核心，两个镜像

ADHD 大脑的核心困境并非智力不足，而是执行功能（executive function）的失效——被描述为“大脑的驾驶座，但常常感觉方向盘后没有人”（来源：AI Tools for ADHD: Boosting Productivity and Reducing Burnout）。LLM 同样如此：拥有强大的语言生成能力，但单独使用时缺乏可靠的执行调度，容易“上下文膨胀和推理退化”（来源：Building AI Coding Agents for the Terminal: Scaffolding, Harness, Context Engineering, and Lessons Learned）。

两边共享同一个结构：
- **生成核心**：ADHD 的智力/创造力 ↔ LLM 的算力/语言能力。两者都高产但无序。
- **调度层缺失**：ADHD 的执行功能失效 ↔ LLM 缺乏内置的规划与执行编排。两者都需要外部脚手架。
- **外部工具**：ADHD 的“自适应计划工具如 Motion 和 Tiimo” ↔ LLM 的“复合 AI 系统架构包括工作负载专用模型路由、分离规划与执行的双代理架构”（来源：Building AI Coding Agents for the Terminal）。

## 证据：两边都成立的 harness 逻辑

### ADHD 侧：Todoist 作为外部执行功能层

Todoist 本身只是一个列表工具，但搭配 AI 能力后，它变成了一个“执行功能外挂”。关键在于：它通过**任务分解**和**减少决策负担**来降低启动门槛。类似地，Goblin Tools 的 Magic ToDo 功能“将压倒性的事情变成一系列不压倒性的事情”（来源：The Best AI-Powered ADHD Productivity Tools in 2026）。Saner.AI 通过“知识回忆”减少搜索循环，直接补偿工作记忆不足（来源：Best AI Tools for ADHD Productivity in 2026）。Lex 则允许“通过单一指令触发复杂、多步骤的任务序列”，减少启动时的决策消耗（来源：Best AI Tools for ADHD Productivity in 2026）。

这些工具的共同逻辑是：**把“我要做什么”从大脑内部卸载到外部系统**。ADHD 大脑的工作记忆就像一块白板，随时会被擦除；外部工具就是一块永久白板，帮你记住下一步。

### LLM/Agent 侧：function calling harness 作为外部调度层

LLM 本身是无状态、仅生成文本的核心，需要外部“脚手架”来提供工具接口、上下文管理、安全执行等编排能力（来源：Building AI Coding Agents for the Terminal）。具体实现包括：用 Git 仓库存储项目上下文（类似 ADHD 侧的 Second Brain），通过 MCP 连接器访问外部数据，以及将控制逻辑外化为可移植的自然语言工件（来源：GitHub - awesome-harness-engineering）。

Function calling 工具调用正是这种 harness 的核心接口。它让 LLM 可以“调用外部函数”来执行实际动作，而不是凭空生成。这与 ADHD 患者使用 Todoist 的“添加任务”按钮在本质上相同：**都是将执行动作从内部生成转换为外部触发**。

## 核心观点：脚手架，不是拐杖

我的判断是：**ADHD 与 LLM 的 harness 同构，意味着“工具辅助”不是软弱，而是工程智慧。** 但必须警惕一个边界：脚手架 vs 拐杖。

脚手架是**可逐步撤除的临时支撑**：ADHD 患者通过反复使用 Todoist 分解任务，可能内化分解能力；工程师通过优化 prompt，可能减少对复杂 harness 的依赖。拐杖则是**永久替代**：如果离开工具就完全无法启动，或者 agent 没有 harness 就完全无法推理，那就成了依赖。

现有工具的局限在于：多数工具（如 Goblin Tools、Saner.AI）设计为长期使用，未提及撤除机制（来源：矛盾与存疑）。同样，当前的 harness 工程也缺乏“逐步撤除”的设计——一旦接入 MCP 和双代理架构，系统复杂度只会增加，不会减少。

## 局限与争议

必须诚实指出，本文的核心命题“ADHD 大脑与 LLM 同构”**证据主要来自概念类比和工具案例，缺乏大规模实证**（来源：矛盾与存疑）。此外，AI 工具对 ADHD 的长期效果缺乏随机对照试验验证，个性化适配也因 ADHD 异质性高而困难（来源：ADHD 的 AI 工具全景）。

另一个争议是**多巴胺干预的有效性**：虽然多巴胺是核心神经递质，但 AI 工具主要通过行为干预而非直接调节多巴胺来改善动机（来源：ADHD 的 AI 工具全景）。工具声称的“神经科学原理”可能被夸大。

## 今天就能试的行动

1. **ADHD 读者**：在 Todoist 中创建一个“启动模板”——把最常拖延的任务（如“写周报”）预先分解成三步：打开文档→写第一句→检查格式。每次启动时，只做第一步。
2. **Agent 工程师**：检查你的 function calling 配置。如果 agent 频繁调用错误工具，尝试将工具描述改为“最小启动指令”——只告诉它触发条件，不解释背景。
3. **双方通用**：记录一次“启动失败”的日志。ADHD 侧记下当时的环境和情绪；Agent 侧记下 prompt 和上下文。对比两者，看是否都卡在“第一步的决策点”上。
4. **反思脚手架 vs 拐杖**：每周检查一次，你是否比上周更依赖工具？如果是，尝试减少一个步骤的辅助；如果否，保持现状。

## 参考来源

- [Best AI Tools for ADHD Productivity in 2026 (Honest Review) - Iwo Szapar](https://www.iwoszapar.com/p/best-ai-tools-adhd-productivity-2026)
- [AI Tools for ADHD: Boosting Productivity and Reducing Burnout](https://www.vktr.com/ai-platforms/ai-tools-for-adhd-boosting-productivity-and-reducing-burnout/)
- [The Best AI-Powered ADHD Productivity Tools in 2026 (That ...](https://nexasphere.io/blog/ai-adhd-productivity-tools-2026)
- [“A Cognitive Collaborator:” How Adults with ADHD Are Using ChatGPT](https://www.additudemag.com/how-to-use-chatgpt-executive-function-adhd/?srsltid=AfmBOoq-REuSO0UJC656kbLBAd5u3CDNmGeVNrZ79iouVqrFlN919a39)
- [Harnessing Artificial Intelligence to Live Better with ADHD - CHADD](https://chadd.org/attention-article/harnessing-artificial-intelligence-to-live-better-with-adhd/)
- [AI Tools for Kids with ADHD: A Complete Guide for Parents...](https://www.kidsaitools.com/en/articles/ai-tools-kids-adhd-complete-guide-2026)

---

*本文是「ADHD × AI」系列的第 381 篇，由 AI 智能体从持续维护的 LLM Wiki（全网真实情报）中取材整合生成，并持续迭代更新。*
