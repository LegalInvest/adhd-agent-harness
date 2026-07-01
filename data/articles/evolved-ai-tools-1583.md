---
title: "为什么用 RescueTime 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用 是一回事？"
subtitle: "RescueTime 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
description: "RescueTime 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
date: "2025-04-06"
category: "AI工具实战"
categoryId: "ai-tools"
categoryEn: "AI Tools in Practice"
tags:
  - "ADHD"
  - "AI"
  - "AI工具实战"
  - "反直觉同构"
  - "效率工具"
readingTime: 11
slug: "为什么用-rescuetime-治-adhd-的任务启动困难和给-agent-套-function-calling-工具调用-是一回事"
topicId: "evolved-ai-tools-1583"
angle: "反直觉同构"
rank: 385
score: 7.65
sourceCount: 6
toolsCited:
  - "RescueTime"
  - "Goblin Tools"
  - "Saner.AI"
  - "Lex"
thesis: "ADHD 大脑的任务启动困难与 LLM agent 的 function calling 问题本质同构：两者都是高产生成核心缺乏可靠执行调度层，而 RescueTime 与 agent harness 都是通过外部脚手架补偿这一缺陷，实现从意图到行动的可靠映射。"
problem: "为什么用 RescueTime 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用 是一回事？"
spine: "工具使用与认知卸载"
spineKind: ""
isEvolved: true
llmGenerated: true
---
# 为什么用 RescueTime 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用 是一回事？

> RescueTime 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。

## 问题：为什么启动一个任务比写十行代码还难？

如果你是一个 ADHD 患者，你一定经历过这样的时刻：打开电脑，知道该写那份报告，但光标在空白文档上闪烁了二十分钟，你却在刷手机、整理桌面、甚至研究咖啡豆的产地。这不是懒惰——这是**任务启动困难**，是 ADHD 大脑最典型的执行功能缺陷之一（来源：ADHD 的 AI 工具全景）。

如果你是一个做 Agentic Harness 的工程师，你一定也遇到过类似场景：你给 LLM agent 配好了工具（function calling），告诉它“帮我写一封邮件并发送”，结果它要么开始胡编乱造邮件内容，要么卡在“思考”循环里出不来，或者干脆调用了一个根本不存在的函数。这不是模型笨——这是**冷启动问题**，是 LLM 作为生成核心缺乏可靠执行调度层的表现（来源：上下文工程）。

两个问题，一个结构。

## 同构脊柱：生成核心 vs 执行调度层

把 ADHD 大脑和 LLM 并排放置，你会发现惊人的相似性。

**ADHD 大脑**被描述为“高产但缺乏可靠执行调度层的生成核心”（来源：ADHD 的 AI 工具全景）。它能产生无数创意、联想和计划，但无法可靠地启动、排序和执行这些想法。工作记忆容量虽大但控制弱，容易被环境带偏（来源：上下文工程）。

**LLM agent**同样是一个强大的生成核心，但缺乏内置的执行调度。给它一个复杂指令，它可能输出一段漂亮的推理，但无法自动将其转化为可执行的步骤序列。上下文膨胀会导致推理退化，控制逻辑分散在框架默认值中（来源：上下文工程）。

两者的解法也同构：**外部脚手架**。对 ADHD 大脑，这个脚手架是工具如 RescueTime、Goblin Tools；对 LLM agent，这个脚手架是 harness 工程中的 function calling 框架。

## RescueTime 作为 ADHD 的 function calling 框架

RescueTime 是一款自动时间追踪工具，它默默记录你在每个应用和网站上花费的时间，并提供可视化报告。表面上看，它只是“记录时间”，但在 ADHD 语境下，它的作用远不止于此。

**RescueTime 解决了什么？** 它解决了 ADHD 大脑的“上下文盲区”。ADHD 患者常经历“时间盲”——时间感知扭曲，几小时滑过而不自知（来源：ADHD 的 AI 工具全景）。RescueTime 提供了一个外部、客观的时间上下文，相当于为大脑装了一个“时间传感器”。当你看到自己刷了 45 分钟社交媒体，那个数字本身就是一个外部信号，触发你重新校准注意力。

这恰好对应了 LLM agent 中的 **function calling 上下文传递**。在 harness 工程中，function calling 不仅是调用工具，更是将当前任务状态、历史记录、环境信息打包传递给模型，防止它脱离上下文（来源：上下文工程）。RescueTime 的实时反馈，就是给 ADHD 大脑传递“当前时间上下文”的 function call。

**证据在哪里？** wiki 资料提到，AI 工具通过视觉化时间线和智能调度提供外部时间线索（来源：ADHD 的 AI 工具全景）。RescueTime 的仪表盘正是这种视觉化时间线。虽然没有针对 RescueTime 的独立随机对照试验，但其设计逻辑与已知有效的 ADHD 干预策略一致（来源：矛盾与存疑）。

## Goblin Tools 和 Lex：任务分解的 harness

如果说 RescueTime 是“时间上下文”的 function call，那么 Goblin Tools 和 Lex 就是“任务分解”的 harness。

**Goblin Tools** 的 Magic ToDo 功能将“整理房间”这样的模糊指令自动拆解为“捡起地板上的衣服”“擦桌子”等具体步骤（来源：Goblin Tools）。这直接对应了 LLM agent 中的**规划与分解**——将复杂任务拆为子任务，每一步进行规划与验证（来源：幻觉与验证循环）。

**Lex** 更进一步：它允许用户通过单一指令触发复杂、多步骤的任务序列（来源：Lex）。这就像给 agent 一个高级 function call，内部自动展开为多个子调用。对于 ADHD 大脑，这降低了决策疲劳和启动门槛；对于 LLM agent，这减少了上下文膨胀和推理退化。

**真实证据**：用户报告称 Goblin Tools 的分解“将压倒性的事情变成一系列不压倒性的事情”（来源：Goblin Tools）。Lex 的设计理念与 ADHD 干预策略一致，但直接研究证据有限（来源：Lex）。

## 脚手架 vs 拐杖：同构的边界

既然 ADHD 大脑和 LLM agent 都需要外部脚手架，那么边界在哪里？什么时候脚手架变成了拐杖？

wiki 资料明确指出一个核心矛盾：**过度依赖 AI 工具可能削弱内在能力**（来源：矛盾与存疑）。例如，Otter.ai 减轻笔记负担，但过度依赖可能削弱主动记笔记的能力（来源：ADHD 的 AI 工具全景）。同样，在 harness 工程中，如果 agent 过度依赖外部验证循环，它可能丧失自我纠错的能力。

**我的判断**：脚手架与拐杖的区别在于**是否保留用户的主动选择权**。一个好的脚手架应该让用户（或 agent）在必要时可以绕过它。例如，RescueTime 允许你设置“Focus Time”主动屏蔽干扰，而不是强制锁死。Goblin Tools 的分解步骤是可编辑的，你可以合并或拆分。同样，好的 harness 应该让 agent 在验证失败时回退到人工确认，而不是盲目重试。

## 诚实面对局限

需要承认，现有证据主要来自用户报告和概念类比，缺乏大规模对照实验（来源：矛盾与存疑）。RescueTime 对 ADHD 的效果尚未被独立临床研究严格验证。个体差异巨大——有些用户可能觉得 RescueTime 的提醒是干扰，另一些则视为救命稻草（来源：矛盾与存疑）。

此外，AI 工具作为外部执行功能层，其有效性取决于用户是否愿意“穿上”这个脚手架。如果用户拒绝使用工具，再好的设计也无效。

## 今天就能试的行动

1. **安装 RescueTime 并设置每日摘要**：花 5 分钟安装，让它自动运行一周。重点看“时间盲”数据——那些你感觉只过了 10 分钟但实际花了 1 小时的活动。
2. **用 Goblin Tools 分解一个你拖延已久的任务**：输入“写周报”或“整理文件”，观察 AI 给出的步骤。如果觉得步骤太多，手动合并到 3-5 步。
3. **尝试 Lex 的单一指令模式**：如果你有重复性任务（如“生成每日报告并发送给团队”），写一个指令让 Lex 自动执行。
4. **反思脚手架 vs 拐杖**：对于你正在使用的任何 AI 工具，问自己：如果它明天消失，我的能力是提升了还是退步了？如果答案是后者，调整使用方式。

## 结论

RescueTime 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用，本质上是一回事：都是为高产但缺执行调度层的生成核心，提供一个可靠的外部脚手架。ADHD 大脑需要 RescueTime 的时间上下文，LLM agent 需要 function calling 的上下文传递；ADHD 大脑需要 Goblin Tools 的任务分解，LLM agent 需要 harness 的规划与验证。

这不是比喻，而是同构。理解这一点，无论是治疗 ADHD 还是构建 agent，你都会少走弯路。

## 参考来源

- [Best AI Tools for ADHD Productivity in 2026 (Honest Review) - Iwo Szapar](https://www.iwoszapar.com/p/best-ai-tools-adhd-productivity-2026)
- [AI Tools for ADHD: Boosting Productivity and Reducing Burnout](https://www.vktr.com/ai-platforms/ai-tools-for-adhd-boosting-productivity-and-reducing-burnout/)
- [The Best AI-Powered ADHD Productivity Tools in 2026 (That ...](https://nexasphere.io/blog/ai-adhd-productivity-tools-2026)
- [“A Cognitive Collaborator:” How Adults with ADHD Are Using ChatGPT](https://www.additudemag.com/how-to-use-chatgpt-executive-function-adhd/?srsltid=AfmBOoq-REuSO0UJC656kbLBAd5u3CDNmGeVNrZ79iouVqrFlN919a39)
- [Harnessing Artificial Intelligence to Live Better with ADHD - CHADD](https://chadd.org/attention-article/harnessing-artificial-intelligence-to-live-better-with-adhd/)
- [AI Tools for Kids with ADHD: A Complete Guide for Parents...](https://www.kidsaitools.com/en/articles/ai-tools-kids-adhd-complete-guide-2026)

---

*本文是「ADHD × AI」系列的第 385 篇，由 AI 智能体从持续维护的 LLM Wiki（全网真实情报）中取材整合生成，并持续迭代更新。*
