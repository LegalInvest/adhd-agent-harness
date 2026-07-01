---
title: "为什么用 Goblin Tools 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用 是一回事？"
subtitle: "Goblin Tools 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
description: "Goblin Tools 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
date: "2025-05-19"
category: "AI工具实战"
categoryId: "ai-tools"
categoryEn: "AI Tools in Practice"
tags:
  - "ADHD"
  - "AI"
  - "AI工具实战"
  - "反直觉同构"
  - "智能助手"
readingTime: 14
slug: "为什么用-goblin-tools-治-adhd-的任务启动困难和给-agent-套-function-calling-工具调用-是一回事"
topicId: "evolved-ai-tools-1564"
angle: "反直觉同构"
rank: 181
score: 7.72
sourceCount: 6
toolsCited:
  - "Goblin Tools"
  - "Saner.AI"
  - "Lex"
  - "Motion"
  - "Tiimo"
thesis: "ADHD 大脑与 LLM/agent 是同一类「高产但缺执行调度层的生成核心」：Goblin Tools 的任务分解和 agent 的 function calling 本质都是通过外部 harness 补偿内部调度缺陷，两者同构。"
problem: "为什么用 Goblin Tools 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用 是一回事？"
spine: "工具使用与认知卸载"
spineKind: ""
isEvolved: true
llmGenerated: true
---
# 为什么用 Goblin Tools 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用 是一回事？

> Goblin Tools 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。

## 问题：为什么任务启动这么难？

如果你是一个 ADHD 患者，你一定熟悉这种场景：明明知道该做什么，但就是无法开始。大脑像是一台高性能引擎，却缺少点火装置。同样，如果你是一个在做 Agentic Harness 工程的开发者，你可能也遇到过：LLM 模型本身能力强大，但一旦需要执行多步任务、调用外部工具，它就卡住了——要么忘记上下文，要么在第一步就偏离轨道。

这两个问题看起来毫不相关，但本质上是一回事：**生成核心（ADHD 大脑或 LLM）本身高产，但缺乏执行调度层**。ADHD 大脑的「执行功能」缺陷（工作记忆不足、时间盲、任务启动困难）与 LLM 的「上下文控制」缺陷（冷启动、上下文膨胀、时序推理弱）一一对应（来源：ADHD 大脑与 LLM 的同构）。而解决方案也惊人地相似：给核心套上一个外部 harness（脚手架）。

## 同构一：任务分解 vs. function calling

ADHD 侧最直接的痛点是任务启动困难。传统规划方法往往失效：「Planners and sticky notes worked for a week before falling apart.」（来源：AI Tools for ADHD: Boosting Productivity and Reducing Burnout）。Goblin Tools 的 Magic ToDo 功能正是为此而生：它通过 AI 将模糊的大任务（如「整理房间」）自动分解为具体的小步骤（「捡起地板上的衣服」「擦桌子」等），从而降低启动门槛（来源：Goblin Tools）。用户反馈称它「将压倒性的事情变成一系列不压倒性的事情」（来源：The Best AI-Powered ADHD Productivity Tools in 2026）。

LLM/agent 侧呢？一个 LLM agent 要完成复杂任务，同样需要将目标拆解为一系列工具调用（function calling）。Harness 工程正是设计这种脚手架——定义工具接口、管理上下文、处理错误（来源：What is an agent harness in the context of large-language models?）。Goblin Tools 的任务分解模式，本质上是为 ADHD 大脑提供了一种「多步推理+工具调用」的脚本，与 agent 的 function calling 完全同构。

**关键判断**：两者都在做同一件事——将「模糊意图」转化为「可执行的原子步骤」。ADHD 大脑的「任务分解困难」和 LLM 的「冷启动问题」，根源都是生成核心缺乏内置的规划循环。外部 harness 通过显式分解来补偿。

## 同构二：认知卸载 vs. 外部记忆

ADHD 的工作记忆容量保留但控制弱，易被干扰；LLM 同样有强记忆容量但弱上下文控制（来源：工作记忆）。因此，外部记忆系统成为关键。Saner.AI 通过知识回忆功能，帮助用户快速找回信息，减少搜索循环和标签切换（来源：Saner.AI）。这相当于为 ADHD 大脑提供了持久化上下文。

在 agent 工程中，外部记忆（如向量数据库、对话历史管理）同样是标准做法。现代 agent 系统通过「组合多个模型、检索器和工具」来达成 SOTA 结果（来源：Building AI Coding Agents for the Terminal: Scaffolding, Harness, Context Engineering, and Lessons Learned）。两者都在将「需要记住的东西」卸载到外部系统，以释放生成核心的认知带宽。

## 同构三：自适应规划 vs. 动态调度

ADHD 的时间盲（time blindness）导致传统计划器失效：「Traditional planners never solved time blindness.」（来源：AI Tools for ADHD: Boosting Productivity and Reducing Burnout）。自适应规划工具如 Motion 和 Tiimo 通过动态调整来应对：「Adaptive planners like Motion and Tiimo go further, reshuffling the day when it collapses.」（来源：规划循环与任务分解）。Lex 则允许用户通过单一指令触发多步骤序列，实时适应大脑工作方式（来源：Lex）。

在 agent 领域，动态调度同样重要。Harness 需要根据中间结果调整后续步骤，处理异常情况。这种「规划-执行-调整」的循环，与 ADHD 工具的自适应规划异曲同工。两者都承认：静态计划注定失败，必须实时反馈和调整。

## 脚手架 vs. 拐杖：诚实面对局限

同构视角还揭示了「脚手架与拐杖」的辩证关系。AI 工具应作为脚手架促进能力发展，而非永久拐杖（来源：拐杖与脚手架）。例如，Otter.ai 减轻笔记负担，但过度依赖可能削弱主动记笔记的能力。同样，Goblin Tools 的任务分解如果长期使用，可能让用户失去自己分解任务的能力。

当前证据主要来自用户报告，缺乏大规模对照实验（来源：矛盾与存疑）。个体差异也很大：有些用户觉得 Goblin Tools 的分解太细，有些人觉得不够细。工具设计者声称是「脚手架」，但实际使用中可能沦为「拐杖」。作为用户和工程师，我们需要保持批判：工具是辅助，不是替代。

## 今天就能试的行动

1. **ADHD 用户**：打开 Goblin Tools 的 Magic ToDo，输入一个你拖延已久的任务（比如「写报告」），观察它分解出的步骤。对比你自己写待办清单的方式——注意启动焦虑的变化。
2. **Agent 工程师**：检查你当前 agent 的 function calling 设计。是否像 Goblin Tools 一样，把每个工具调用当作「最小可执行步骤」？尝试将复杂任务拆解为 3-5 个原子工具，减少 LLM 的决策负担。
3. **双方通用**：记录一次「任务启动失败」的场景。问自己：如果有一个外部 harness 帮我分解第一步，我能开始吗？然后尝试用任何工具（Goblin Tools、Lex、甚至 ChatGPT）做一次分解。观察结果。

## 结论

Goblin Tools 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用，本质是同一件事：**为高产但缺调度层的生成核心，套上一个外部执行 harness**。这个视角不仅解释了为什么这些工具对 ADHD 有效，也为 agent 工程提供了设计原则——工具即用户界面，接口要简单、无认知开销。同时，它提醒我们：脚手架和拐杖只有一线之隔，保持觉察才能让工具真正成为能力的延伸，而非依赖的陷阱。

## 参考来源

- [Best AI Tools for ADHD Productivity in 2026 (Honest Review) - Iwo Szapar](https://www.iwoszapar.com/p/best-ai-tools-adhd-productivity-2026)
- [AI Tools for ADHD: Boosting Productivity and Reducing Burnout](https://www.vktr.com/ai-platforms/ai-tools-for-adhd-boosting-productivity-and-reducing-burnout/)
- [The Best AI-Powered ADHD Productivity Tools in 2026 (That ...](https://nexasphere.io/blog/ai-adhd-productivity-tools-2026)
- [“A Cognitive Collaborator:” How Adults with ADHD Are Using ChatGPT](https://www.additudemag.com/how-to-use-chatgpt-executive-function-adhd/?srsltid=AfmBOoq-REuSO0UJC656kbLBAd5u3CDNmGeVNrZ79iouVqrFlN919a39)
- [Harnessing Artificial Intelligence to Live Better with ADHD - CHADD](https://chadd.org/attention-article/harnessing-artificial-intelligence-to-live-better-with-adhd/)
- [AI Tools for Kids with ADHD: A Complete Guide for Parents...](https://www.kidsaitools.com/en/articles/ai-tools-kids-adhd-complete-guide-2026)

---

*本文是「ADHD × AI」系列的第 181 篇，由 AI 智能体从持续维护的 LLM Wiki（全网真实情报）中取材整合生成，并持续迭代更新。*
