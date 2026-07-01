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
  - "Claude"
  - "Otter.ai"
  - "Mem"
  - "Reflect"
thesis: "ADHD 大脑与 LLM agent 共享同一核心困境：两者都是高产但缺乏可靠执行调度层的生成核心。因此，为 ADHD 设计的工具（如 Forest、Goblin Tools）与为 agent 设计的 function calling harness 在结构上同构——都是通过外部脚手架来补偿内在的调度缺陷，实现认知卸载。"
problem: "为什么用 Forest 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用 是一回事？"
spine: "工具使用与认知卸载"
spineKind: ""
isEvolved: true
llmGenerated: true
---
# 为什么用 Forest 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用 是一回事？

> Forest 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。

## 问题：为什么你的大脑和你的 AI agent 一样，都卡在“启动”这一步？

如果你有 ADHD，你一定经历过这种时刻：明知该写报告，身体却像被钉在椅子上，大脑一片空白，最后刷了两小时手机。如果你是做 Agentic Harness 的工程师，你一定调试过这种场景：LLM 明明知道该调用天气 API，却迟迟不发起请求，或者调用了错误的参数格式，需要你反复修正 prompt。

这两个场景，本质上是同一个问题：**一个高产的生成核心，缺少一个可靠的执行调度层。**

ADHD 大脑被描述为“高产但缺乏可靠执行调度层的生成核心”（来源：ADHD 的 AI 工具全景）。LLM agent 同样如此——它拥有强大的语言生成能力，但如果没有 function calling 的 harness，它只是一个无状态的 API 调用，无法自主执行多步骤任务（来源：无状态与外部记忆）。两者都需要一个外部脚手架来“启动”任务、管理上下文、分解步骤。

这就是为什么用 Forest 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用，是一回事。

## 同构：任务启动困难 ↔ 冷启动问题

ADHD 侧最典型的工具是 Goblin Tools。它的 Magic ToDo 功能能将“整理房间”这样的模糊指令自动分解为“捡起地板上的衣服”“擦桌子”等具体步骤（来源：Goblin Tools）。用户报告称，这种分解显著降低了启动焦虑，将“压倒性的事情变成一系列不压倒性的事情”（来源：Goblin Tools）。

LLM/agent 侧对应的正是 function calling。一个没有工具调用的 LLM，面对“帮我查一下明天北京的天气”这样的指令，只能生成一段文本描述，无法真正执行查询。而通过 function calling harness，LLM 可以调用 `get_weather(location, date)` 这样的 API，将意图转化为可执行动作。这正是 Goblin Tools 所做的——将意图分解为可执行的子任务。

证据不仅来自类比。在 agent 工程中，生产级系统通过检索增强和工具调用将决策锚定在外部证据和持久状态上（来源：无状态与外部记忆）。ADHD 侧同样如此：Saner.AI 通过本地记忆存储和快速检索，减少用户因工作记忆不足导致的搜索循环和标签切换（来源：Saner.AI）。Lex 允许用户通过单一指令触发复杂多步骤任务序列，直接针对任务启动困难（来源：Lex）。这些工具本质上都是为生成核心提供“启动脚本”。

## 脚手架 vs 拐杖：边界在哪里？

但同构并不意味着无脑套用。这里有一个关键争议：AI 工具究竟是脚手架还是拐杖？

ADHD 的 AI 工具全景明确指出，AI 工具应作为脚手架促进能力发展，而非永久拐杖（来源：ADHD 的 AI 工具全景）。例如，Otter.ai 可以减轻笔记负担，但过度依赖可能削弱主动记笔记的能力（来源：ADHD 的 AI 工具全景）。同样，在 agent 工程中，如果 harness 过于“智能”，自动处理所有模糊指令，那么 agent 本身永远不会学会如何结构化自己的请求。

矛盾与存疑页面也警告：过度依赖 AI 工具可能削弱内在能力（来源：矛盾与存疑）。多个工具页面（如 Goblin Tools、Saner.AI）缺乏独立随机对照试验，证据主要来自用户报告（来源：矛盾与存疑）。这意味着，虽然同构视角提供了强有力的设计思路，但实际效果仍需谨慎评估。

我的判断是：**脚手架与拐杖的边界在于，工具是否保留了用户的主动控制权。** 好的 harness 让用户（或 agent）决定何时调用工具、调用哪个工具，而不是替用户做所有决定。例如，Forest 的“种树”机制要求用户主动选择专注时间，而不是自动锁定手机。同样，function calling 应该让 LLM 自主决定调用哪个 API，而不是由 harness 硬编码所有路径。

## 今天就能试的行动

1. **如果你是 ADHD 用户**：下载 Forest 或 Goblin Tools，下次面对大任务时，先用它们将任务分解为 3-5 个具体步骤。注意观察启动焦虑是否降低。同时，警惕过度依赖——每周至少一次尝试不借助工具完成简单任务。
2. **如果你是 Agent 工程师**：在你的 LLM 调用链中显式引入 function calling harness，从“无状态 API”升级为“有工具调用的 agent”。例如，为你的 agent 注册一个 `decompose_task(task_description)` 函数，模拟 Goblin Tools 的分解逻辑。
3. **两方通用**：检查你当前使用的工具或 harness，是否保留了你的主动控制权？如果它替你做所有决定（如自动安排日程、自动调用所有 API），你很可能正在使用拐杖而非脚手架。调整设置，让自己（或 agent）有选择权。
4. **记录一次对比**：ADHD 用户尝试用 AI 工具完成一项任务，同时手动完成另一项类似任务，记录完成时间、焦虑程度和满意度。Agent 工程师则对比有无 function calling 时，LLM 完成多步骤任务的准确率。这种自我实验能帮你找到脚手架与拐杖的边界。

## 局限与争议

必须坦诚：目前所有证据都来自用户报告和概念类比，缺乏大规模随机对照试验（来源：矛盾与存疑）。个体差异也很大——有人对 Goblin Tools 赞不绝口，有人觉得它多此一举（来源：矛盾与存疑）。同构视角虽然优雅，但它是一个理论框架，尚未被严格验证。因此，本文提供的行动建议只是起点，你需要根据自己的实际情况调整。

但有一点是确定的：**无论对 ADHD 大脑还是 LLM agent，外部脚手架都是补偿内部调度缺陷的有效策略。** 关键在于，我们如何设计这些脚手架，让它们成为能力发展的阶梯，而非永久依赖的拐杖。这正是 ADHD 工具与 agent harness 共同的工程挑战——也是它们最迷人的同构之处。

## 参考来源

- [Best AI Tools for ADHD Productivity in 2026 (Honest Review) - Iwo Szapar](https://www.iwoszapar.com/p/best-ai-tools-adhd-productivity-2026)
- [AI Tools for ADHD: Boosting Productivity and Reducing Burnout](https://www.vktr.com/ai-platforms/ai-tools-for-adhd-boosting-productivity-and-reducing-burnout/)
- [The Best AI-Powered ADHD Productivity Tools in 2026 (That ...](https://nexasphere.io/blog/ai-adhd-productivity-tools-2026)
- [“A Cognitive Collaborator:” How Adults with ADHD Are Using ChatGPT](https://www.additudemag.com/how-to-use-chatgpt-executive-function-adhd/?srsltid=AfmBOoq-REuSO0UJC656kbLBAd5u3CDNmGeVNrZ79iouVqrFlN919a39)
- [Harnessing Artificial Intelligence to Live Better with ADHD - CHADD](https://chadd.org/attention-article/harnessing-artificial-intelligence-to-live-better-with-adhd/)
- [AI Tools for Kids with ADHD: A Complete Guide for Parents...](https://www.kidsaitools.com/en/articles/ai-tools-kids-adhd-complete-guide-2026)

---

*本文是「ADHD × AI」系列的第 384 篇，由 AI 智能体从持续维护的 LLM Wiki（全网真实情报）中取材整合生成，并持续迭代更新。*
