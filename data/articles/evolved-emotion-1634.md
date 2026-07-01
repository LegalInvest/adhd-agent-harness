---
title: "为什么用 Saner.AI 治 ADHD 的情绪失调，和给 agent 套 会褪去的脚手架 是一回事？"
subtitle: "Saner.AI 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
description: "Saner.AI 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
date: "2025-05-17"
category: "情绪调节"
categoryId: "emotion"
categoryEn: "Emotional Regulation"
tags:
  - "ADHD"
  - "AI"
  - "情绪调节"
  - "反直觉同构"
  - "情绪管理"
readingTime: 8
slug: "为什么用-sanerai-治-adhd-的情绪失调和给-agent-套-会褪去的脚手架-是一回事"
topicId: "evolved-emotion-1634"
angle: "反直觉同构"
rank: 388
score: 7.65
sourceCount: 6
toolsCited:
  - "Saner.AI"
  - "Inflow"
  - "Goblin Tools"
  - "Motion"
  - "Tiimo"
  - "Brain.fm"
thesis: "ADHD 情绪失调与 LLM agent 的脆弱性同构于「强大生成核心 + 不可靠调度层」，Saner.AI 的 harness 与 agent 的「会褪去的脚手架」都是通过外部执行层补偿调度缺陷，且必须设计为可撤除的临时支撑，否则从脚手架沦为拐杖。"
problem: "为什么用 Saner.AI 治 ADHD 的情绪失调，和给 agent 套 会褪去的脚手架 是一回事？"
spine: "拐杖与脚手架"
spineKind: ""
isEvolved: true
llmGenerated: true
---
# 为什么用 Saner.AI 治 ADHD 的情绪失调，和给 agent 套 会褪去的脚手架 是一回事？

> Saner.AI 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。

## 问题：为什么你越努力调节情绪，情绪越失控？

如果你有 ADHD，你一定经历过这样的时刻：明明只是一件小事——一条未回复的消息、一个被临时取消的会议——却突然引爆巨大的情绪波动，像被按下了情绪核弹的按钮。事后你理性分析，知道自己反应过度，但当时就是控制不住。这不是你“矫情”，而是 ADHD 大脑的情绪调节系统出了结构性问题。

与此同时，如果你正在做 Agentic Harness 工程，你一定也遇到过这样的场景：一个强大的 LLM（比如 GPT-4），在复杂任务中突然“胡言乱语”，输出完全偏离轨道，仿佛失去了对上下文的理解。你检查 prompt，调整参数，但问题依然间歇性出现。这不是模型“笨”，而是 LLM 的调度层同样存在结构性的脆弱。

这两个问题，本质上是同一个问题。

## 同构：ADHD 大脑与 LLM 共享的脆弱性

ADHD 大脑与 LLM 之间存在一个被忽视的同构：两者都是“高产但缺执行调度层的生成核心”。ADHD 大脑拥有强大的联想、创造和直觉能力（生成核心），但执行功能（工作记忆、任务启动、时间感知）薄弱，导致情绪调节失效（来源：AI 与 ADHD 的情绪调节）。LLM 拥有强大的语言生成能力（生成核心），但缺乏内生的规划、工具调用和错误恢复能力（调度层），需要外部 harness 来编排（来源：工具使用与认知卸载）。

情绪调节，本质上是调度层的工作。当工作记忆过载——比如你同时想着要赶 deadline、回复消息、准备晚饭——情绪信息无法被维持和加工，大脑就切换到“战斗或逃跑”模式，情绪失控（来源：AI 与 ADHD 的情绪调节）。同样，LLM 在长对话中丢失上下文（相当于工作记忆过载），就会产生不一致的输出。

## 解法：Saner.AI 的 harness 与 agent 的脚手架是同一回事

Saner.AI 的核心功能是“知识回忆”和“本地记忆”，它像一个外部工作记忆，帮你快速找回信息，减少标签切换和搜索循环（来源：Saner.AI）。这本质上是一个 **harness**：它接管了大脑不擅长的信息检索和维持任务，让你能专注于当前目标。同样，LLM agent 的 harness 通过 function calling、上下文工程和规划循环，补偿模型缺乏的调度能力（来源：工具使用与认知卸载）。

但关键区别在于：**脚手架 vs 拐杖**。脚手架是临时支撑，设计为可逐步撤除；拐杖是永久替代，撤除后功能丧失（来源：拐杖与脚手架）。Saner.AI 和大多数 ADHD 工具（如 Goblin Tools、Inflow）目前被设计为长期使用，未明确提供撤除机制（来源：矛盾与存疑）。这带来了过度依赖的风险：如果工具永远替代了你的工作记忆，你的内在情绪调节能力可能反而萎缩。

## 证据：两边都成立的 harness 原则

ADHD 侧的证据：Inflow 通过训练背外侧前额叶皮层（因果流入中枢）来改善工作记忆（来源：Inflow），但缺乏长期效果研究。Goblin Tools 的任务分解功能降低了启动焦虑（来源：Goblin Tools），但用户可能依赖它而不再练习自己分解任务。Motion 和 Tiimo 的动态规划解决了时间盲（来源：规划循环与任务分解），但同样没有撤除设计。

LLM/agent 侧的证据：Harness 工程强调“agent UX”——工具接口应简单、无认知开销（来源：工具使用与认知卸载）。这与 ADHD 工具应“插入现有堆栈，不增加额外负担”的原则完全一致（来源：工具使用与认知卸载）。但优秀的 agent harness 会设计“退化路径”：当模型能力提升时，逐步减少外部支撑。例如，早期 agent 依赖硬编码的规划步骤，现在可以交给模型自主推理，harness 只提供工具接口。

## 争议与局限：脚手架何时变成拐杖？

目前最大的争议在于：**AI 工具是否应该设计为可撤除的脚手架？** 多数工具（Saner.AI、Goblin Tools）定位为长期伴侣，但缺乏撤除机制可能导致依赖。证据显示，基于多巴胺的奖励系统可能强化外在动机而非内在能力（来源：矛盾与存疑）。此外，ADHD 大脑与 LLM 同构命题仍缺乏大规模实证（来源：矛盾与存疑），它更多是一个有用的理论框架而非事实。

我的判断是：**脚手架必须包含撤除计划**。Saner.AI 的 harness 和 agent 的 harness 都应该内置“能力转移”阶段——比如在用户使用一段时间后，逐步减少 AI 提示，鼓励用户自行回忆；或者 agent 在稳定后降低 context 注入量。没有撤除的脚手架，就是拐杖。

## 今天就能试的行动

1. **用 Saner.AI 做一次“情绪归因”练习**：当情绪波动时，打开 Saner.AI 记录触发事件、身体感受和想法，利用其知识回忆功能回顾过去类似情境，识别模式。这相当于为情绪调节装一个外部工作记忆。

2. **给 LLM agent 设计一个“脚手架撤除测试”**：在当前 agent 的 harness 中加入一个参数，控制 context 注入量。从 100% 开始，每轮任务减少 10%，观察模型何时开始出错。记录阈值，作为未来模型升级后的调整依据。

3. **对比两种工具的任务分解方式**：用 Goblin Tools 将一个模糊任务（如“准备下周的汇报”）分解为步骤，再用 Saner.AI 的笔记功能手动分解。比较两者的认知负荷差异。思考：如果你必须撤除工具，哪种分解方式更容易内化？

4. **为你的 ADHD 工具设置一个“撤除闹钟”**：在日历上标记 3 个月后，尝试一天不使用任何 AI 工具（包括 Saner.AI、Goblin Tools），仅用纸笔和闹钟完成工作。记录情绪波动次数和强度，与使用工具时对比。这是检验脚手架是否变成拐杖的简单实验。

## 参考来源

- [Dynamic causal brain circuits during working memory and their functional controllability](https://doi.org/10.1038/s41467-021-23509-x)
- [Best AI Tools for ADHD Productivity in 2026 (Honest Review) - Iwo Szapar](https://www.iwoszapar.com/p/best-ai-tools-adhd-productivity-2026)
- [AI Tools for ADHD: Boosting Productivity and Reducing Burnout](https://www.vktr.com/ai-platforms/ai-tools-for-adhd-boosting-productivity-and-reducing-burnout/)
- [The Best AI-Powered ADHD Productivity Tools in 2026 (That ...](https://nexasphere.io/blog/ai-adhd-productivity-tools-2026)
- [“A Cognitive Collaborator:” How Adults with ADHD Are Using ChatGPT](https://www.additudemag.com/how-to-use-chatgpt-executive-function-adhd/?srsltid=AfmBOoq-REuSO0UJC656kbLBAd5u3CDNmGeVNrZ79iouVqrFlN919a39)
- [Harnessing Artificial Intelligence to Live Better with ADHD - CHADD](https://chadd.org/attention-article/harnessing-artificial-intelligence-to-live-better-with-adhd/)

---

*本文是「ADHD × AI」系列的第 388 篇，由 AI 智能体从持续维护的 LLM Wiki（全网真实情报）中取材整合生成，并持续迭代更新。*
