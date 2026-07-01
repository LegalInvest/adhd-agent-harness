---
title: "为什么用 Claude 治 ADHD 的不知哪些方法有用，和给 agent 套 human-in-the-loop 监督 是一回事？"
subtitle: "Claude 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
description: "Claude 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
date: "2025-05-02"
category: "亲子教育"
categoryId: "parenting"
categoryEn: "Parenting & Education"
tags:
  - "ADHD"
  - "AI"
  - "亲子教育"
  - "反直觉同构"
readingTime: 11
slug: "为什么用-claude-治-adhd-的不知哪些方法有用和给-agent-套-human-in-the-loop-监督-是一回事"
topicId: "evolved-parenting-1759"
angle: "反直觉同构"
rank: 206
score: 7.71
sourceCount: 6
toolsCited:
  - "Goblin Tools"
  - "Saner.AI"
  - "Motion"
  - "Focusmate"
  - "Brain.fm"
thesis: "ADHD 大脑与 LLM/agent 共享同一困境：生成核心强大但执行调度层薄弱，因此两者的解法——外部重锚定系统与 human-in-the-loop 监督——在结构上完全同构，都要求设计可撤除的脚手架而非永久拐杖。"
problem: "为什么用 Claude 治 ADHD 的不知哪些方法有用，和给 agent 套 human-in-the-loop 监督 是一回事？"
spine: "人在回路与身体在场"
spineKind: ""
isEvolved: true
llmGenerated: true
---
# 为什么用 Claude 治 ADHD 的不知哪些方法有用，和给 agent 套 human-in-the-loop 监督 是一回事？

> Claude 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。

## 同一个问题，两个世界

你打开 Claude，想让它帮你写一份周报。它开头写得漂亮，但五轮对话后开始偏离主题，甚至忘记了最初的指令。你不得不手动打断，重新粘贴系统提示。

你打开日程，想开始一项任务。大脑一片空白，明明知道该做什么，但就是动不了。你刷了十分钟手机，然后打开 Goblin Tools，把“整理房间”分解成“捡起地板上的衣服”“擦桌子”等小步骤，才终于开始。

这两件事看起来毫不相干，但本质是同一个问题：**一个高产但缺执行调度层的生成核心，在长程任务中必然发生目标漂移**。ADHD 大脑和 LLM/agent 共享这一结构缺陷，因此它们的解法——外部重锚定系统与 human-in-the-loop 监督——在结构上完全同构。

## 目标漂移：ADHD 大脑与 LLM 的共同敌人

ADHD 大脑在执行任务时极易发生目标漂移：注意力被无关刺激捕获（分心），或过度聚焦于细节而忽略整体目标（超聚焦）。外部工具通过提醒和通知提供重锚定，将注意力拉回原任务。例如，AI 工具“将任务分解为可管理的步骤，设置提醒和专注计时器以提高生产力”（来源：AI for ADHD: Best Tools, Apps, and Strategies - Themba Tutors）。Goblin Tools 的 Magic ToDo 功能能自动将任何任务分解为更小、更易管理的步骤，从而降低启动门槛（来源：AI Tools for Kids with ADHD: A Complete Guide for Parents）。Saner.AI 通过增强知识回忆，帮助用户快速找回信息，减少认知负荷（来源：Best AI Tools for ADHD Productivity in 2026 (Honest Review) - Iwo Szapar）。Motion 则通过自动排程与动态调整，持续评估任务优先级和截止时间，实时重建日程，减少用户的手动规划压力（来源：11 Best ADHD Productivity Apps for Fluctuating Energy - rivva blog）。

LLM agent 在长程任务中同样面临目标漂移：模型在交互轮次后期“开始忘记系统提示”（来源：Building an AI Coding Agent for the Terminal: Scaffolding, Harness, Context Engineering, and Lessons Learned），导致行为偏离初始指令。Agent harness（脚手架）通过事件驱动的系统提醒来对抗这种“指令消退”（来源：同上），并设置护栏——token 预算、工具调用次数上限、防止无限循环——以及加入人工检查点，暂停并询问后再执行（来源：Building an AI Agent Harness from Scratch: The Architecture Between LLM and Agent - DEV Community）。

## 人在回路：绕过执行功能屏障

ADHD 大脑的生成核心（发散思维、创意、多任务并行）产出极高，但执行功能（任务启动、持续专注、抑制冲动）薄弱，导致“高产但不可靠”。身体在场效应（body doubling）是 ADHD 群体最有效的策略之一：有另一个人在场时，执行功能障碍被绕过，任务得以启动和维持（来源：11 Best ADHD Productivity Apps for Fluctuating Energy - rivva blog）。Focusmate 等工具通过 AI 匹配虚拟身体搭档，提供外部问责（来源：The Best AI-Powered ADHD Productivity Tools in 2026 (That ...)）。这种“对另一个人的责任感”能绕过执行功能屏障（来源：同上）。

LLM 本身是强大的生成核心，但缺乏可靠的执行调度层，直接输出可能偏离目标、陷入循环或产生危险行为。Harness 通过 human-in-the-loop 监督提供外部调度：形式化规划与护栏，使代理输出真正有用且正确（来源：What is an agent harness in the context of large-language models?）。模型本身强大，可靠性来自架构+护栏（来源：AI Agents in 2026: Tools, Memory, Evals, and Guardrails）。

## 同构对应：从提醒到护栏

| ADHD 侧 | LLM/harness 侧 |
|---------|----------------|
| 目标漂移（分心/超聚焦） | 指令消退、行为偏离 |
| 外部提醒、通知 | 事件驱动的系统提醒 |
| 身体在场（body doubling） | human-in-the-loop 监督 |
| 任务分解（Goblin Tools） | 工具调用分解 |
| 知识回忆（Saner.AI） | 上下文注入与记忆 |
| 动态排程（Motion） | 规划与重规划 |

两边的解法本质相同：**在生成核心之外，建立一个外部调度层，通过周期性的重锚定来对抗目标漂移**。

## 脚手架 vs 拐杖：争议与局限

然而，这种同构也带来了一个关键争议：**这些外部工具是临时的脚手架，还是终身的拐杖？** 脚手架应设计为可逐步撤除的临时支撑，但多数工具（如 Goblin Tools、Saner.AI）设计为长期使用，未提及撤除机制（来源：拐杖与脚手架概念页）。过度依赖是否阻碍内在能力发展？目前缺乏针对这些工具的独立随机对照试验，证据主要来自用户评价和综述文章（来源：矛盾与存疑）。

同样，agent harness 如果设计得过于僵化，也会让模型失去自主性。好的 harness 应该像好的脚手架：在需要时提供支撑，但在能力提升后可以撤除。

## 今天就能试的行动

1. **设置重锚定提醒**：无论是用手机闹钟还是 AI 工具，每 25 分钟设置一个提醒，问自己“我现在在做什么？这是我原本想做的吗？”——这是最基础的 human-in-the-loop。
2. **尝试任务分解**：用 Goblin Tools 的 Magic ToDo 或 Claude 将一个大任务分解成 5-10 个小步骤，每次只做一步。
3. **找一个身体搭档**：用 Focusmate 或找一位朋友，约定同时工作，定期互相报告进度。
4. **为 agent 设置检查点**：如果你是工程师，在 agent 的每轮关键操作前加入人工确认步骤，就像给 ADHD 大脑设置提醒一样。

## 结论

ADHD 大脑与 LLM/agent 是同构的：都是强大的生成核心，却缺乏可靠的执行调度层。两边的解法——外部重锚定系统与 human-in-the-loop 监督——在结构上完全一致。认识到这种同构，不仅能帮助我们更理性地选择工具（避免被“神经科学原理”的夸大宣传误导），也能让工程师和 ADHD 患者互相理解：我们面对的是同一个问题，只是换了个名字。

## 参考来源

- [Best AI Tools for ADHD Productivity in 2026 (Honest Review) - Iwo Szapar](https://www.iwoszapar.com/p/best-ai-tools-adhd-productivity-2026)
- [AI Tools for ADHD: Boosting Productivity and Reducing Burnout](https://www.vktr.com/ai-platforms/ai-tools-for-adhd-boosting-productivity-and-reducing-burnout/)
- [The Best AI-Powered ADHD Productivity Tools in 2026 (That ...](https://nexasphere.io/blog/ai-adhd-productivity-tools-2026)
- [“A Cognitive Collaborator:” How Adults with ADHD Are Using ChatGPT](https://www.additudemag.com/how-to-use-chatgpt-executive-function-adhd/?srsltid=AfmBOoq-REuSO0UJC656kbLBAd5u3CDNmGeVNrZ79iouVqrFlN919a39)
- [Harnessing Artificial Intelligence to Live Better with ADHD - CHADD](https://chadd.org/attention-article/harnessing-artificial-intelligence-to-live-better-with-adhd/)
- [AI Tools for Kids with ADHD: A Complete Guide for Parents...](https://www.kidsaitools.com/en/articles/ai-tools-kids-adhd-complete-guide-2026)

---

*本文是「ADHD × AI」系列的第 206 篇，由 AI 智能体从持续维护的 LLM Wiki（全网真实情报）中取材整合生成，并持续迭代更新。*
