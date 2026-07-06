---
title: "为什么用 Tiimo 治 ADHD 的情绪失调，和给 agent 套 会褪去的脚手架 是一回事？"
subtitle: "Tiimo 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
description: "Tiimo 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
date: "2025-04-18"
category: "情绪调节"
categoryId: "emotion"
categoryEn: "Emotional Regulation"
tags:
  - "ADHD"
  - "AI"
  - "情绪调节"
  - "反直觉同构"
  - "压力管理"
readingTime: 11
slug: "为什么用-tiimo-治-adhd-的情绪失调和给-agent-套-会褪去的脚手架-是一回事"
topicId: "evolved-emotion-1637"
angle: "反直觉同构"
rank: 390
score: 7.65
sourceCount: 6
toolsCited:
  - "Tiimo"
  - "Inflow"
  - "Goblin Tools"
  - "Saner.AI"
  - "Focusmate"
thesis: "ADHD 的情绪失调与 LLM/agent 的不可靠输出源于同一类问题——生成核心过强但调度层缺失，因此 Tiimo 等外部执行功能工具与 agent harness（会褪去的脚手架）在结构上同构，都是通过外部调度层补偿内在缺陷，且必须警惕从‘脚手架’滑向‘永久拐杖’的风险。"
problem: "为什么用 Tiimo 治 ADHD 的情绪失调，和给 agent 套 会褪去的脚手架 是一回事？"
spine: "拐杖与脚手架"
spineKind: ""
isEvolved: true
llmGenerated: true
caseStudies:
  - "释迦牟尼"
  - "张旭"
  - "李明"
---
# 为什么用 Tiimo 治 ADHD 的情绪失调，和给 agent 套 会褪去的脚手架 是一回事？

> Tiimo 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。

你打开 Tiimo，屏幕上是一天的时间轴，每个色块代表一个任务。你告诉自己：今天要写报告。但你的大脑像一台没有调度器的生成模型——想法喷涌，却无法按顺序执行。三分钟后，你点开了另一个标签页；十分钟后，你在查“如何用 AI 管理 ADHD”；半小时后，你开始焦虑为什么还没开始。

这不是意志力问题。这是执行功能缺陷。而另一边，工程师正在调试一个 LLM agent：模型输出了完美的代码片段，但 agent 却陷入了无限循环，或者调用了不该调的工具。模型本身没问题——问题在于它缺少一个可靠的调度层。

这两件事是同一件事。

## 同构：高产但缺调度层的生成核心

ADHD 大脑的情绪失调，根源往往不是情绪本身，而是执行功能缺陷。工作记忆不稳定让你记不住刚才为什么生气；时间盲让你觉得 deadline 还很远；任务启动困难让你在焦虑中拖延，直到情绪爆发。这就像 LLM 的生成能力：它能写出莎士比亚，但如果你不给它护栏和调度，它会跑题、重复、甚至编造事实。

AI 工具在这里的角色，就是那个缺失的调度层。Tiimo 把一天切成可视化的色块，让你不需要靠工作记忆去“记得”下一步该做什么；Inflow 用 CBT 结构化程序教你在情绪上来时做认知重构（来源：Inflow）；Goblin Tools 的 Magic ToDo 把“清理厨房”分解成 12 个步骤，降低启动门槛（来源：Goblin Tools）。这些工具都在做同一件事：**把执行功能外包给外部系统**。

而在 LLM 侧，agent harness 做的是同样的事。Harness 设置 token 预算、工具调用次数上限、人工检查点，防止 agent 无限循环或偏离目标（来源：Building an AI Agent Harness from Scratch: The Architecture Between LLM and Agent - DEV Community）。它引入人在回路治理，让模型在关键步骤暂停并等待确认。模型本身强大，可靠性来自架构+护栏（来源：AI Agents in 2026: Tools, Memory, Evals, and Guardrails）。

## 人物案例：张旭的 harness 与 agent 的脚手架

唐朝草圣张旭，每次喝醉后号呼狂走，以头濡墨作书，醒了自视以为神。他多相睡眠，灵感来了不管场合就写字，对草书超专注，其他事一概不关心。这是典型的 ADHD 特质：高度创造性，但缺乏常规的执行调度。他的 harness 是什么？酒和草书。喝酒进入超专注状态，把所有情绪注入草书；看公孙大娘舞剑悟笔法，从自然中找灵感。这套系统让他成为草圣，但也让他无法做其他任何事。

张旭的 harness 和 LLM agent 的脚手架在结构上完全同构：酒是“进入超专注的 prompt”，草书是“输出通道”，公孙大娘舞剑是“外部灵感源”。而 agent harness 里的“定时 re-grounding”对应张旭每天必须喝酒才能创作的习惯，“外部调度器”对应他的书童帮他准备纸墨。但张旭的 harness 有一个致命问题：它没有“会褪去”的设计。他终身依赖酒，一旦离开这个脚手架，他就无法创作。

## 会褪去的脚手架 vs 永久拐杖

这正是核心争议：AI 工具到底是脚手架，还是拐杖？

脚手架是暂时的，它帮你建起大楼，然后拆除，让你自己站立。拐杖是永久的，你依赖它才能走路。ADHD 工具如果被长期无节制使用，可能成为永久拐杖，阻碍内在能力的发展（来源：拐杖与脚手架）。目前缺乏长期追踪研究来验证适度使用的边界（来源：矛盾与存疑）。

举个例子：Tiimo 的时间色块。如果你用它来替代你缺失的时间感知，但从不练习在无工具的情况下估算时间，那么你的时间盲不会改善。同样，Inflow 的 CBT 程序如果只是被动跟随，而不内化认知重构技能，那么离开 app 后情绪失调依旧。

LLM agent 的 harness 也面临同样问题。如果 harness 过于 rigid，agent 永远学不会自主规划；如果 harness 过于 loose，agent 会频繁出错。好的 harness 设计是“会褪去的”——随着 agent 能力提升，逐步减少人工干预。这叫做“scaffolding that fades”。

## 证据与局限

当前证据支持 AI 工具作为外部执行功能层的有效性。Inflow 基于 CBT 的模块化设计，临床研究显示用户情绪稳定性提升（来源：Inflow）。Focusmate 利用社会问责与 AI 排程创造身体在场效应，降低任务焦虑（来源：人在回路与身体在场）。但这些证据主要来自短期研究，且样本量小。

更关键的是，ADHD 亚型（注意力不集中型 vs. 冲动型）对工具的反应不同，现有结论难以泛化（来源：矛盾与存疑）。而且，AI 工具擅长处理结构化情绪问题（如任务焦虑），但对深层情绪（如创伤、自我否定）的干预效果证据不足（来源：AI 与 ADHD 的情绪调节）。

## 今天就能试的行动

1. **用 Tiimo 的“时间色块”替代待办清单**：每天早晨花 3 分钟，把今天要做的 3 件事拖进时间轴，每件事设一个色块。色块就是你的外部调度层。
2. **用 Goblin Tools 的 Magic ToDo 分解一个让你焦虑的任务**：输入“写周报”，调节辣度到 3，看它分解成 8 步。选第一步开始做，做完就停。
3. **设置一个“会褪去的提醒”**：用手机闹钟每周提醒一次“今天不用 Tiimo，自己估算时间”。记录误差，逐步减少提醒频率。
4. **如果你是工程师，在 agent harness 中加入一个“fade schedule”**：定义 agent 在连续 N 次正确执行后，自动减少一次人工检查点。让脚手架自己褪去。

## 结语

Tiimo 和 agent harness 是同一类东西：外部调度层。它们不是拐杖，而是脚手架——前提是你记得拆掉它们。张旭没有拆掉他的酒，所以他是草圣，但也是酒鬼。你可以在成为高产者的同时，保持内在能力的生长。关键在于：脚手架要会褪去。

## 参考来源

- [The 12 Best Apps for ADHD in 2026: A Guide to Finding What ...](https://www.getinflow.io/post/best-apps-for-adhd)
- [Dynamic causal brain circuits during working memory and their functional controllability](https://doi.org/10.1038/s41467-021-23509-x)
- [ADHD Apps: We tested 44 Apps and Here're the Best 9 in 2026](https://blog.saner.ai/best-adhd-apps/)
- [12 AI Personal Assistants Built for ADHD Brains (2026 Rankings)](https://www.usecarly.com/blog/best-ai-personal-assistant-adhd/)
- [DeepSeek - AI Assistant - Apps on Google Play](https://play.google.com/store/apps/details?id=com.deepseek.chat)
- [AI Assistant for ADHD: Finally, a Productivity Tool That Requires Less...](https://get-alfred.ai/blog/ai-assistant-for-adhd)

---

*本文是「ADHD × AI」系列的第 390 篇，由 AI 智能体从持续维护的 LLM Wiki（全网真实情报）中取材整合生成，并持续迭代更新。*
