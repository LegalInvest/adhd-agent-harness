---
title: "为什么用 Claude 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用 是一回事？"
subtitle: "Claude 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
description: "Claude 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
date: "2025-05-03"
category: "AI工具实战"
categoryId: "ai-tools"
categoryEn: "AI Tools in Practice"
tags:
  - "ADHD"
  - "AI"
  - "AI工具实战"
  - "反直觉同构"
  - "自动化"
readingTime: 14
slug: "为什么用-claude-治-adhd-的任务启动困难和给-agent-套-function-calling-工具调用-是一回事"
topicId: "evolved-ai-tools-2058"
angle: "反直觉同构"
rank: 155
score: 7.79
sourceCount: 6
toolsCited:
  - "Goblin Tools"
  - "Saner.AI"
  - "Lex"
  - "Claude"
  - "ChatGPT"
thesis: "ADHD 大脑与 LLM agent 共享同一类缺陷——强大生成核心缺乏可靠执行调度层，因此两者都需要外部 harness 来补偿任务启动困难与上下文管理缺陷，而 function calling 工具调用正是为 LLM 提供这种调度层的工程实现。"
problem: "为什么用 Claude 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用 是一回事？"
spine: "工具使用与认知卸载"
spineKind: ""
isEvolved: true
llmGenerated: true
caseStudies:
  - "孔子"
  - "左宗棠"
  - "Jacob Avery"
---
# 为什么用 Claude 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用 是一回事？

> Claude 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。

## 问题：为什么你写了 50 个待办，却一个都没开始？

如果你是一个 ADHD 患者，你一定熟悉这种场景：大脑里塞满了想法、计划、灵感，但坐到电脑前，光标闪烁，就是按不下第一个键。任务启动困难——这是 ADHD 执行功能缺陷中最折磨人的一种。同样，如果你是一个在做 Agentic Harness 工程的开发者，你一定也遇到过：LLM 能写出漂亮的代码、生成流畅的文案，但让它去调用一个 API、执行一个函数，它就「幻觉」给你看——要么编造参数，要么跳过验证，要么上下文膨胀到推理退化。

这两个问题，表面看毫无关系。一个在神经科学领域，一个在 AI 工程领域。但它们的底层结构，惊人地同构。

## 同构：高产但缺调度层的生成核心

ADHD 大脑常被描述为「高产但缺乏可靠执行调度层的生成核心」（来源：主题综述）。它擅长发散、联想、模式识别，但不擅长「启动→执行→验证→关闭」这个闭环。任务启动困难本质上是调度层缺失——大脑的「前额叶执行功能」无法将意图转化为行动序列。

LLM 同样如此。GPT-4、Claude 3.5 是强大的生成核心，但它们无状态、缺乏内置调度。让 LLM 独立完成一个多步骤任务，它会在第三步忘记第一步的目标，或者生成一个格式错误的 JSON 就自信地返回。这就是为什么 agent 工程的核心是 harness——一套外部脚手架，提供上下文传递、工具接口、规划工件、验证循环和记忆系统（来源：幻觉与验证循环）。

换句话说：ADHD 需要一个外部调度器来「启动任务」；LLM agent 需要 function calling 来「调用工具」。两者都是为生成核心套上执行层。

## 证据：两边都成立的 harness 系统

### ADHD 侧：从孔子到 Goblin Tools

孔子可能是历史上最著名的 ADHD 患者之一。他身高 1 米 9，精力旺盛，周游列国 14 年坐不住；冲动爱骂人，见南子急得对天发誓，骂宰予「朽木不可雕」；对音乐超专注到「三月不知肉味」，对种地等俗事零耐心。他的 harness 是什么？「克己复礼」——用外在的「礼」作为行为边界，每日反省，「吾日三省吾身」。70 岁才做到「从心所欲不逾矩」。这套系统本质上就是一个外部调度层：用日课（定时 re-grounding）、用礼仪（行为模板）、用反省（验证循环）来补偿内在执行功能的不足。

现代工具更直接。Goblin Tools 的 Magic ToDo 能把「清理厨房」分解成 15 个子步骤，用户可调节「辣度」控制粒度（来源：Goblin Tools）。这相当于把 LLM 的「工具调用」拆成原子动作。Saner.AI 通过本地记忆减少搜索循环（来源：Saner.AI），相当于给 LLM 加了一个记忆系统。Lex 允许「单一指令触发多步骤任务」（来源：Lex），正是 LLM agent 中「规划→执行→验证」的完整 pipeline。

### LLM/agent 侧：function calling 就是 ADHD 的「外部执行层」

在 agent harness 工程中，function calling 不是简单的 API 调用。它是一个完整的调度框架：定义工具 schema → 上下文注入 → 规划分解 → 执行验证 → 结果反馈 → 记忆更新。缺少任何一环，agent 就会陷入「更多幻觉和重复工作」（来源：幻觉与验证循环）。这正是 ADHD 大脑的写照——没有外部脚手架，就会陷入「任务瘫痪」和「搜索循环」。

一个典型的 agent harness 包含：上下文传递、工具接口、规划工件、验证循环、记忆系统和沙盒（来源：幻觉与验证循环）。对比 ADHD 的经典干预：上下文传递 ↔ 环境设计（如关掉手机通知）；工具接口 ↔ 清单与模板；规划工件 ↔ 任务分解（如 Goblin Tools）；验证循环 ↔ 自我检查（如孔子的「三省吾身」）；记忆系统 ↔ 外部笔记（如 Saner.AI）；沙盒 ↔ 安全环境试错。

## 核心观点：脚手架不是拐杖

同构不是等同。ADHD 大脑不是 LLM，LLM 也不是大脑。但「生成核心 + 外部调度层」这个架构，在两边都成立。关键区别在于：脚手架（scaffold）是临时性的，最终要拆除；拐杖（crutch）是永久依赖。对 ADHD 来说，过度依赖 AI 工具可能削弱内在执行功能（来源：矛盾与存疑）。对 agent 来说，过度依赖硬编码的调度逻辑会导致系统僵化、无法泛化。

好的 harness 设计，应该像孔子的「礼」——一开始是外部约束，最终内化为「从心所欲不逾矩」。Goblin Tools 的「辣度」调节，Lex 的渐进式自主，都是这种思路：工具提供结构，但用户保留控制权。

## 争议与局限

必须诚实指出：ADHD 大脑与 LLM 的同构目前仅是一种理论类比，缺乏实证基础（来源：矛盾与存疑）。不同工具的证据基础薄弱，多数依赖用户报告而非临床验证（来源：矛盾与存疑）。依赖风险真实存在——工具可能从脚手架变成拐杖。此外，通用工具如 ChatGPT 可能增加分心风险（来源：主题综述）。

## 今天就能试的行动

1. **用 Goblin Tools 分解一个你拖延了一周的任务**：打开 Magic ToDo，输入「写周报」，设置辣度 3，看它拆成几步。执行第一步，感受启动门槛降低。
2. **给 Claude 写一个「function calling prompt」**：明确告诉它你需要它做什么、输出格式是什么、验证条件是什么。比如：「请将以下任务分解为可执行的子步骤，每一步用 JSON 表示，包含 action、input、expected_output 三个字段。完成后请自我检查是否遗漏。」
3. **模仿孔子的「日课」**：每天固定时间用 Saner.AI 或笔记工具记录三件事——今天要启动的任务、今天的验证点（如「我是否完成了第一步？」）、今天的反思（如「哪个环节卡住了？为什么？」）。
4. **检查你的工具是否成了拐杖**：问自己——如果这个工具明天消失，我还能完成这个任务吗？如果不能，说明你在依赖它完成核心执行功能，需要逐步训练内在调度能力。

同构不是巧合。ADHD 大脑和 LLM agent 共享同一个工程问题：如何让一个强大的生成核心，可靠地执行现实世界的任务。答案都是 harness——外部脚手架，通过工具调用、上下文管理、验证循环来补偿调度缺陷。理解这一点，你就能同时优化自己的大脑和你的 agent。

## 参考来源

- [ADHD Apps: We tested 44 Apps and Here're the Best 9 in 2026](https://blog.saner.ai/best-adhd-apps/) — 证据等级：低（GRADE）
- [12 AI Personal Assistants Built for ADHD Brains (2026 Rankings)](https://www.usecarly.com/blog/best-ai-personal-assistant-adhd/) — 证据等级：低（GRADE）
- [Toward Neurodivergent-Aware Productivity: A Systems and AI-Based Human-in-the-Loop Framework for ADHD-Affected Professionals](https://arxiv.org/pdf/2507.06864) — 证据等级：低（GRADE）
- [Agent Scaffolding: Architecture and Design Patterns for Agentic AI](https://zbrain.ai/agent-scaffolding/) — 证据等级：低（GRADE）
- [Confabulation: The Surprising Value of Large Language Model Hallucinations](https://preview.aclanthology.org/navbar-space/2024.acl-long.770.pdf) — 证据等级：低（GRADE）
- [LBD同构对：分心与走神 — Therapeutic Doses of Oral Methylphenidate Significantly Incr ↔ AutoHallusion: Automatic Generation of Hallucination Benchma](https://doi.org/10.1523/jneurosci.21-02-j0001.2001) — 证据等级：低（GRADE）

---

*本文是「ADHD × AI」系列的第 155 篇，由 AI 智能体从持续维护的 LLM Wiki（全网真实情报）中取材整合生成，并持续迭代更新。*
