---
title: "为什么用 Goblin Tools 治 ADHD 的情绪失调，和给 agent 套 会褪去的脚手架 是一回事？"
subtitle: "Goblin Tools 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
description: "Goblin Tools 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
date: "2025-03-25"
category: "情绪调节"
categoryId: "emotion"
categoryEn: "Emotional Regulation"
tags:
  - "ADHD"
  - "AI"
  - "情绪调节"
  - "反直觉同构"
  - "心理健康"
readingTime: 13
slug: "为什么用-goblin-tools-治-adhd-的情绪失调和给-agent-套-会褪去的脚手架-是一回事"
topicId: "evolved-emotion-1633"
angle: "反直觉同构"
rank: 162
score: 7.74
sourceCount: 6
toolsCited:
  - "Goblin Tools"
  - "Inflow"
  - "Saner.AI"
  - "Motion"
  - "Reclaim.ai"
  - "Tiimo"
  - "Brain.fm"
thesis: "ADHD 的情绪失调与 LLM/Agent 的编排缺陷是同一类问题——强大的生成核心缺乏可靠的调度层；Goblin Tools 等工具提供的“会褪去的脚手架”正是双方通用的 harness 方案。"
problem: "为什么用 Goblin Tools 治 ADHD 的情绪失调，和给 agent 套 会褪去的脚手架 是一回事？"
spine: "拐杖与脚手架"
spineKind: ""
isEvolved: true
llmGenerated: true
---
# 为什么用 Goblin Tools 治 ADHD 的情绪失调，和给 agent 套 会褪去的脚手架 是一回事？

> Goblin Tools 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。

## 问题：为什么情绪失调和 Agent 编排失败是同一回事？

如果你是一个 ADHD 成人，你一定经历过这种时刻：明明知道该做什么，就是迈不出第一步；情绪突然崩盘，却说不清为什么。如果你是一个 Agentic Harness 工程师，你一定也经历过：LLM 明明有足够的知识和推理能力，却总是在多步骤任务中迷失方向、重复循环、甚至编造幻觉。这两类痛苦，共享同一个底层结构——**一个高产但缺执行调度层的生成核心**。

ADHD 大脑的情绪失调，根源在于执行功能缺陷：工作记忆容量有限，任务启动困难，时间感知失灵（来源：情绪失调）。当这些调度层失效，情绪便失去约束，像没有护栏的瀑布。LLM/Agent 的“情绪”则是输出失控：上下文窗口溢出、编排逻辑断裂、工具调用顺序错误。两边都需要一个外部调度层——一个会褪去的脚手架，而非永久的拐杖。

## 同构一：任务启动 vs. 上下文启动

ADHD 侧最典型的痛点：任务启动。Goblin Tools 的“魔法待办”功能将“整理房间”分解为“捡起地板上的衣服”“擦桌子”等小步骤，降低启动门槛（来源：Goblin Tools）。这本质上是在给大脑加装一个“启动引导器”——把模糊意图转化为具体操作序列。

LLM/Agent 侧对应的是“上下文启动”：当模型需要执行一个复杂任务时，直接给出“写一篇报告”往往输出空洞。有效的做法是将其分解为“收集资料→列大纲→写引言→分段撰写→总结”等子步骤，并逐步注入上下文。这就是 Agentic Harness 中的“任务分解”模式。Goblin Tools 的分步逻辑，与工程师为 Agent 设计的“Chain of Thought”或“Step-by-Step”提示词，是同一个结构——**用外部脚手架补偿调度层的缺失**。

## 同构二：工作记忆 vs. 上下文窗口

ADHD 的工作记忆缺陷导致情绪信息难以维持：你刚感到焦虑，却忘了触发原因。AI 工具如 Inflow 通过提醒、笔记和进度追踪充当外部记忆载体（来源：AI 与 ADHD 的情绪调节）。Saner.AI 则专注于知识回忆，减少搜索循环（来源：Saner.AI）。

LLM/Agent 的“工作记忆”就是上下文窗口。当窗口溢出，模型会忘记早期指令或关键事实，导致输出偏离。工程师通过检索增强生成（RAG）或外部记忆模块来扩展上下文——这与 ADHD 用户使用笔记和提醒完全同构。**两者都在用外部存储补偿内部容量的不足。**

## 同构三：时间盲 vs. 时间感知

ADHD 的时间盲导致对任务耗时感知失真，产生时间压力或拖延。Tiimo 通过时间轴可视化帮助用户感知时间流逝（来源：任务启动）。Motion 和 Reclaim.ai 自动规划日程，在最佳时间推送任务（来源：任务启动）。

Agent 同样需要时间感知：长时间运行的任务需要进度条、超时机制和重试逻辑。工程师为 Agent 设计的“心跳检测”和“进度报告”，本质上就是 Tiimo 的可视化时间轴。**两边都在对抗“时间盲”——只是 ADHD 侧是神经性的，Agent 侧是架构性的。**

## 边界：脚手架 vs. 拐杖

这里必须诚实指出争议：AI 工具可能削弱内在能力（来源：矛盾与存疑）。Goblin Tools 被设计为长期使用，未提及撤除机制。但真正的脚手架应该“会褪去”——随着用户能力提升逐步移除支撑。同样，Agent 的 harness 也应在模型能力增强后简化。当前多数工具和框架都未解决“撤除”问题，这是一个未竟的工程挑战。

## 今天就能试的行动

1. **ADHD 侧**：用 Goblin Tools 的 Magic ToDo 分解一个让你焦虑的任务，体验“启动门槛降低”的效果。注意：使用一周后，尝试自己先手动分解，再对比 AI 结果，逐步内化分解能力。
2. **工程师侧**：为你的 Agent 写一个“任务分解”提示词，将复杂指令拆成 5 步以内的小步骤，并加入进度反馈。观察执行成功率的变化。
3. **共同行动**：记录一周内情绪失控或 Agent 失败的场景，识别是否都发生在“调度层过载”时。你会惊讶于两者的相似性。
4. **反思**：每周检查一次，哪些脚手架可以撤除？例如，如果某类任务已能自动完成，就减少 AI 介入——无论是对自己还是对 Agent。

## 局限

本文论证基于概念同构，缺乏大规模实证（来源：矛盾与存疑）。ADHD 大脑与 LLM 的同构命题主要来自工具案例和类比，需要更多神经科学和系统研究的验证。此外，情绪调节的个体差异（如共病焦虑）可能使单一工具无效。但作为思考框架，它已经能帮两类人找到彼此的镜像，从而更清醒地设计和使用“会褪去的脚手架”。

## 参考来源

- [Dynamic causal brain circuits during working memory and their functional controllability](https://doi.org/10.1038/s41467-021-23509-x)
- [Best AI Tools for ADHD Productivity in 2026 (Honest Review) - Iwo Szapar](https://www.iwoszapar.com/p/best-ai-tools-adhd-productivity-2026)
- [AI Tools for ADHD: Boosting Productivity and Reducing Burnout](https://www.vktr.com/ai-platforms/ai-tools-for-adhd-boosting-productivity-and-reducing-burnout/)
- [The Best AI-Powered ADHD Productivity Tools in 2026 (That ...](https://nexasphere.io/blog/ai-adhd-productivity-tools-2026)
- [“A Cognitive Collaborator:” How Adults with ADHD Are Using ChatGPT](https://www.additudemag.com/how-to-use-chatgpt-executive-function-adhd/?srsltid=AfmBOoq-REuSO0UJC656kbLBAd5u3CDNmGeVNrZ79iouVqrFlN919a39)
- [Harnessing Artificial Intelligence to Live Better with ADHD - CHADD](https://chadd.org/attention-article/harnessing-artificial-intelligence-to-live-better-with-adhd/)

---

*本文是「ADHD × AI」系列的第 162 篇，由 AI 智能体从持续维护的 LLM Wiki（全网真实情报）中取材整合生成，并持续迭代更新。*
