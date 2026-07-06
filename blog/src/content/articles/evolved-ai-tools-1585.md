---
title: "为什么用 Perplexity 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用 是一回事？"
subtitle: "Perplexity 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
description: "Perplexity 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
date: "2025-05-14"
category: "AI工具实战"
categoryId: "ai-tools"
categoryEn: "AI Tools in Practice"
tags:
  - "ADHD"
  - "AI"
  - "AI工具实战"
  - "反直觉同构"
  - "智能助手"
readingTime: 13
slug: "为什么用-perplexity-治-adhd-的任务启动困难和给-agent-套-function-calling-工具调用-是一回事"
topicId: "evolved-ai-tools-1585"
angle: "反直觉同构"
rank: 183
score: 7.72
sourceCount: 6
toolsCited:
  - "Goblin Tools"
  - "Lex"
  - "Saner.AI"
  - "Perplexity"
thesis: "ADHD 大脑与 LLM 在结构上同构——都是高产生成核心但缺乏内置执行调度层——因此两者的解决方案（外部脚手架/harness）本质相同：用工具调用（function calling）将生成能力约束到目标轨道上。"
problem: "为什么用 Perplexity 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用 是一回事？"
spine: "工具使用与认知卸载"
spineKind: ""
isEvolved: true
llmGenerated: true
caseStudies:
  - "孔子"
  - "老子"
  - "Aaron Myers"
---
# 为什么用 Perplexity 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用 是一回事？

> Perplexity 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。

## 问题：任务启动困难，ADHD 与 LLM 的同一道坎

你是一个 ADHD 成人。你坐在桌前，脑子里有一百个想法在炸，但就是启动不了写报告这件事。你打开 Perplexity，输入一个模糊问题，期望它帮你搞定——却发现自己又陷入了搜索循环，半小时后还在读无关的维基百科。

你是一个 Agent 工程师。你给 LLM 套上了 function calling，期待它自动调用工具完成任务。结果它要么在同一个 API 上反复重试，要么生成了一堆无用的中间输出——模型很强，但就是“不干活”。

这两个场景，表面上是不同的困境：一个是人，一个是机器。但它们的底层结构完全相同——都是一个高产的生成核心，卡在了“启动”这一步。

## 同构：ADHD 大脑与 LLM 共享的“生成-调度”缺口

ADHD 大脑常被描述为一个高产的生成核心——想法丰富、联想活跃，但缺少稳定、可靠的调度层来筛选、组织、启动和坚持任务（来源：ADHD 的 AI 工具全景）。大语言模型同样具备强大的生成能力，却在长程上下文、目标保持与执行调度上存在天然缺陷。两者都需要外部脚手架来约束生成能力，使其指向目标轨道。

这个脚手架，在 ADHD 侧是“外部执行功能层”（如任务分解、提醒、身体在场），在 LLM 侧是 agent harness（如 token 预算、工具调用次数上限、人在回路）。它们的核心机制一致：**用工具调用（function calling）将生成能力接入一个可维护的执行调度系统**。

## 证据一：ADHD 侧的 harness 系统——孔子与 Lex

孔子是典型的 ADHD 大脑：精力旺盛、冲动爱骂人、思维跳跃、对音乐超专注而对种地零耐心。《论语》全是场景化语录，无系统著作，正是生成核心高产但调度层缺失的表现。他的 harness 系统是“克己复礼”：用外在的“礼”作为行为边界，每日反省（“吾日三省吾身”），70 岁才做到从心所欲不逾矩。这套系统本质上是一个外部调度层：**日课（定时 re-grounding）对应 LLM 的定期 re-grounding，礼的约束对应 harness 的护栏**。

现代 ADHD 工具如 **Lex** 提供了类似的“单一指令触发多步骤”功能，将复杂任务自动分解并顺序执行（来源：Lex）。这相当于给 ADHD 大脑套了一个微型的 function calling 系统：输入一个目标，自动调用子任务序列，降低启动门槛。**Goblin Tools** 的 Magic ToDo 更进一步，允许用户调节“辣度”控制分解粒度（来源：Goblin Tools）。这些都是外部调度层的具体实现。

## 证据二：LLM/Agent 侧的 harness 系统——function calling 与护栏

LLM 的 agent harness 通过形式化规划与护栏使输出真正有用且正确（来源：What is an agent harness in the context of large-language models?）。具体来说，harness 集成 MCP 工具、遥测、代码仓库，并引入人在回路治理（来源：GitHub - ai-boost/awesome-harness-engineering）。其核心功能包括：任务拆解（将复杂目标分解为工具调用）、外部记忆（通过向量数据库补偿上下文窗口限制）、重锚定（通过 token 预算和调用次数上限防止漂移）。

例如，Perplexity 本身是一个搜索工具，但当你用它来“写一篇关于 ADHD 的文章”时，它需要被 harness 到你的工作流中：先搜索资料，再整理提纲，最后生成正文。如果缺乏 harness，它就会像 ADHD 大脑一样，在搜索循环中漂移。这正是为什么许多工程师用 Perplexity 时，需要手动将其输出“喂”给另一个工具——本质上是在搭建一个跨工具的外部调度层。

## 核心观点：Perplexity 治 ADHD 与 function calling 治 LLM 是同一件事

**Perplexity 对 ADHD 用户的价值，不在于它本身是“智能助手”，而在于它提供了一个低门槛的工具调用接口——你输入一个模糊问题，它返回一个结构化答案。这个接口降低了启动所需的认知负荷。同样，function calling 对 agent 的价值，不在于 LLM 变聪明了，而在于它提供了一个标准化的外部调度通道——LLM 不再需要自己“想”怎么执行，而是调用预定义工具。**

两者共享同一个原理：**将生成核心的“发散”通过工具调用转化为“收敛”的行动序列**。ADHD 用户使用 Perplexity 时，实际上是在进行一场“工具调用”——将大脑中的模糊意图转化为对搜索工具的调用，从而绕过执行功能缺陷。工程师给 agent 套 function calling 时，也是在将 LLM 的生成能力约束到工具调用轨道上，避免它自由发散。

## 矛盾与局限：脚手架还是拐杖？

然而，这一同构框架存在争议。首先，ADHD 大脑与 LLM 同构的论点目前多为类比推理，缺乏神经科学或计算机科学的直接证据（来源：矛盾与存疑）。其次，AI 工具作为外部执行功能层，长期依赖可能导致能力退化——成为永久拐杖而非临时脚手架（来源：矛盾与存疑）。最后，个体差异巨大：有些 ADHD 用户需要强力打断（如番茄钟），有些则偏好柔性引导（来源：矛盾与存疑）。

因此，本文的观点并非“AI 工具万能”，而是强调：**理解这一同构，可以帮助两类人互相借鉴设计思路**。ADHD 用户可以从 agent harness 中学到“护栏”的重要性（如设置时间限制、调用次数上限），工程师则可以从 ADHD 策略中学到“身体在场”和“重锚定”的机制。

## 今天就能试的行动

1. **用 Perplexity 做一次“工具调用”实验**：写下一个你拖延的任务（如“整理桌面”），然后问 Perplexity“帮我列出整理桌面的前 3 个步骤”。观察它是否降低了你的启动门槛。
2. **为自己的 agent 添加一个“重锚定”护栏**：在 function calling 中加入一个“每 3 次工具调用后，暂停并输出当前状态”的检查点，防止目标漂移。
3. **尝试 Lex 的单一指令触发**：如果你有 ADHD，用 Lex 输入“帮我规划明天的三个优先任务”，看它是否自动拆解并执行。
4. **建立个人“日课”系统**：像孔子的“三省吾身”一样，每天固定时间用 AI 工具（如 Reflect）做一次 5 分钟的结构化反思，对抗目标漂移。

## 参考来源

- [ADHD Apps: We tested 44 Apps and Here're the Best 9 in 2026](https://blog.saner.ai/best-adhd-apps/)
- [12 AI Personal Assistants Built for ADHD Brains (2026 Rankings)](https://www.usecarly.com/blog/best-ai-personal-assistant-adhd/)
- [The 12 Best AI Tools for 2026 (That People Actually Use)](https://www.synthesia.io/post/ai-tools)
- [Agent Scaffolding: Architecture and Design Patterns for Agentic AI](https://zbrain.ai/agent-scaffolding/)
- [Best productivity apps for Mac you need to try](https://macpaw.com/reviews/best-productivity-apps-for-mac)
- [Building AI Coding Agents for the Terminal: Scaffolding, Harness ...](https://arxiv.org/html/2603.05344v1)

---

*本文是「ADHD × AI」系列的第 183 篇，由 AI 智能体从持续维护的 LLM Wiki（全网真实情报）中取材整合生成，并持续迭代更新。*
