---
title: "为什么用 Routinery 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用 是一回事？"
subtitle: "Routinery 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
description: "Routinery 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
date: "2025-03-21"
category: "AI工具实战"
categoryId: "ai-tools"
categoryEn: "AI Tools in Practice"
tags:
  - "ADHD"
  - "AI"
  - "AI工具实战"
  - "反直觉同构"
  - "ADHD辅助"
readingTime: 13
slug: "为什么用-routinery-治-adhd-的任务启动困难和给-agent-套-function-calling-工具调用-是一回事"
topicId: "evolved-ai-tools-1578"
angle: "反直觉同构"
rank: 380
score: 7.65
sourceCount: 6
toolsCited:
  - "Routinery"
  - "Goblin Tools"
  - "Saner.AI"
  - "Lex"
  - "Mem"
  - "Otter.ai"
  - "Reflect"
thesis: "ADHD 大脑和 LLM 都是“高产但缺执行调度层的生成核心”，两者的任务启动困难本质相同，因此 Routinery 式的外部脚手架与 agent 的 function calling harness 是同一结构问题的同构解。"
problem: "为什么用 Routinery 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用 是一回事？"
spine: "工具使用与认知卸载"
spineKind: ""
isEvolved: true
llmGenerated: true
---
# 为什么用 Routinery 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用 是一回事？

> Routinery 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。

你有没有过这样的时刻：明明知道该做什么，身体却像被钉在椅子上，大脑一片空白，只能眼睁睁看着时间流逝？ADHD 的任务启动困难，不是懒，是执行功能调度层的故障（来源：ADHD 的 AI 工具全景）。而另一边，工程师们正为一个类似的问题焦头烂额：LLM 明明能生成惊艳的代码或文案，却无法自主调用工具、完成多步骤任务，必须靠 function calling harness 来“手把手”指挥。这两件事，其实是同一个问题在人和机器上的两种表现。

## 问题：为什么“知道怎么做”却“动不了”？

ADHD 大脑的核心特征是“高产但无序的生成能力，同时缺乏可靠的执行调度层”（来源：ADHD 大脑与 LLM 的同构）。想法像喷泉，但行动像堵住的水管。同样，LLM 是强大的生成核心，但“缺乏可靠的内置调度与执行控制”（来源：ADHD 大脑与 LLM 的同构）。两者都需要一个外部层来提供“下一步做什么”的指令。

在 ADHD 侧，这个外部层是 Routinery 这样的 app——它把“整理房间”分解成“捡起地板上的衣服”“擦桌子”等小步骤，降低启动门槛（来源：Goblin Tools）。在 LLM/agent 侧，这个外部层是 agent harness——“包裹 LLM 或 AI agent 的软件基础设施，处理模型本身之外的一切”（来源：ADHD 大脑与 LLM 的同构），包括工具接口、上下文管理、安全执行等。

## 同构解：脚手架 vs 拐杖

核心观点：ADHD 大脑和 LLM 是同一类“高产但缺执行调度层的生成核心”，两边的解法（harness/脚手架）结构同构。Routinery 对 ADHD 的“任务分解 + 即时反馈”，等价于 function calling 对 LLM 的“工具定义 + 调用序列”。两者都在做同一件事：给一个强大的生成核心套上外部执行功能层。

### ADHD 侧的真实证据
- **Goblin Tools** 的 Magic ToDo 能自动将任务分解为小步骤，用户反馈称“启动焦虑降低”（来源：Goblin Tools）。它“将压倒性的事情变成一系列不压倒性的事情”（来源：Goblin Tools）。
- **Lex** 通过“单一指令触发复杂、多步骤的任务序列”（来源：Lex），减少了决策疲劳。
- **Saner.AI** 通过增强知识回忆，帮助用户快速找回信息，减少搜索循环（来源：Saner.AI）。这些工具共同的特点是：它们不改变 ADHD 大脑的生成能力，而是提供外部调度指令。

### LLM/agent 侧的真实证据
- Agent harness 工程的核心是“设计围绕 AI 代理的脚手架——上下文交付、工具接口、规划工件、验证循环、记忆系统和沙箱”（来源：外部执行功能层）。
- 具体实现中，常用“复合 AI 系统”架构，通过“每个工作流可绑定不同 LLM”来分配任务（来源：外部执行功能层）。
- 例如，用 Git 仓库存储项目上下文（类似 ADHD 侧的 Second Brain），通过 MCP 连接器访问外部数据（来源：外部执行功能层）。这些 harness 组件的作用，正是补偿 LLM 缺乏的内置调度能力。

## 脚手架 vs 拐杖的边界

必须诚实指出：这种同构解法有边界。AI 工具作为外部执行功能层，应作为“脚手架”促进能力发展，而非永久“拐杖”（来源：ADHD 的 AI 工具全景）。过度依赖可能削弱内在能力，例如 Otter.ai 减轻笔记负担，但过度使用可能削弱主动记笔记的能力（来源：ADHD 的 AI 工具全景）。同样，给 LLM 套上过于僵化的 harness，可能限制其生成灵活性。

矛盾与存疑：目前证据主要来自用户报告，缺乏大规模对照实验（来源：矛盾与存疑）。个体差异大，效果因人而异（来源：矛盾与存疑）。工具设计者声称是“脚手架”，但实际使用中可能沦为“拐杖”（来源：矛盾与存疑）。

## 今天就能试的行动
1. **用 Routinery 或 Goblin Tools 分解一个你拖延的任务**——比如“写周报”，让 AI 拆成 5 步，每完成一步打个勾。
2. **为你的 LLM agent 写一个简单的 function calling 定义**——比如让它可以查询天气或发送邮件，观察启动效率的变化。
3. **记录一周内使用外部脚手架的次数**——无论是人用 app 还是机器用 harness，对比启动困难的天数变化。
4. **刻意练习一次“无脚手架”启动**——比如不用工具，自己写待办清单，感受内在调度层的状态。

同构视角让我们看到，ADHD 和 LLM 的困境并非孤立。Routinery 和 function calling 共享同一套逻辑：给强大的生成核心一个可靠的外部调度层。理解这一点，既能帮助 ADHD 人群更理性地选择工具，也能让 agent 工程师从人类认知缺陷中汲取设计灵感。

## 参考来源

- [Best AI Tools for ADHD Productivity in 2026 (Honest Review) - Iwo Szapar](https://www.iwoszapar.com/p/best-ai-tools-adhd-productivity-2026)
- [AI Tools for ADHD: Boosting Productivity and Reducing Burnout](https://www.vktr.com/ai-platforms/ai-tools-for-adhd-boosting-productivity-and-reducing-burnout/)
- [The Best AI-Powered ADHD Productivity Tools in 2026 (That ...](https://nexasphere.io/blog/ai-adhd-productivity-tools-2026)
- [“A Cognitive Collaborator:” How Adults with ADHD Are Using ChatGPT](https://www.additudemag.com/how-to-use-chatgpt-executive-function-adhd/?srsltid=AfmBOoq-REuSO0UJC656kbLBAd5u3CDNmGeVNrZ79iouVqrFlN919a39)
- [Harnessing Artificial Intelligence to Live Better with ADHD - CHADD](https://chadd.org/attention-article/harnessing-artificial-intelligence-to-live-better-with-adhd/)
- [AI Tools for Kids with ADHD: A Complete Guide for Parents...](https://www.kidsaitools.com/en/articles/ai-tools-kids-adhd-complete-guide-2026)

---

*本文是「ADHD × AI」系列的第 380 篇，由 AI 智能体从持续维护的 LLM Wiki（全网真实情报）中取材整合生成，并持续迭代更新。*
