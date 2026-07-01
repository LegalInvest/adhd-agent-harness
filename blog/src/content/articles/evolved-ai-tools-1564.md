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
thesis: "ADHD大脑与LLM同构：两者都是强大的生成核心但缺乏执行调度层，因此Goblin Tools的任务分解与LLM agent的function calling本质上是同一套harness思路——通过外部工具补偿内部执行功能缺陷。"
problem: "为什么用 Goblin Tools 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用 是一回事？"
spine: "工具使用与认知卸载"
spineKind: ""
isEvolved: true
llmGenerated: true
---
# 为什么用 Goblin Tools 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用 是一回事？

> Goblin Tools 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。

## 问题：为什么ADHD的“任务启动困难”和LLM agent的“function calling”是同一回事？

如果你是一个ADHD患者，你一定经历过这种场景：脑子里有一堆想做的事，但就是无法开始——任务像一座大山压在面前，启动焦虑让你瘫在沙发上刷手机。如果你是一个在做Agentic Harness工程的AI工程师，你一定也见过这种场景：你的LLM agent明明有强大的生成能力，但面对复杂任务时，它要么跑偏，要么卡在第一步，需要你手动拆解指令、设计工具调用。

这两个场景看似风马牛不相及，但背后共享同一个结构性问题：**一个高产但缺乏执行调度层的生成核心**。ADHD大脑是一个创造力爆棚的生成器，但执行功能（计划、组织、工作记忆）不稳定（来源：ADHD 的 AI 工具全景）。LLM也是一个强大的生成器，但同样缺乏内置的规划循环和工具管理能力，需要外部harness来编排（来源：What is an agent harness in the context of large-language models?）。

Goblin Tools的Magic ToDo功能，能把“整理房间”自动分解成“捡起地板上的衣服”“擦桌子”等小步骤（来源：Goblin Tools）。这听起来是不是很像LLM agent通过function calling把“写一封邮件”拆解成“调用邮件API”“生成正文”“检查语法”等子任务？两者都在做同一件事：**将模糊的高层意图转化为可执行的原子步骤，从而降低启动门槛**。

## 同构证据：ADHD侧与LLM侧的真实对应

### ADHD侧：任务分解与认知卸载

ADHD患者的核心困难之一是任务启动障碍，源于工作记忆容量有限和时间盲（来源：规划循环与任务分解）。传统规划方法往往失效，因为“大多数规划建议不是为我们设计的”（来源：ADHD Productivity Hack: Plan 2025 Using AI (Step-by-Step)）。Goblin Tools通过AI将压倒性的任务变成一系列不压倒性的步骤（来源：The Best AI-Powered ADHD Productivity Tools in 2026），用户反馈“它在这方面很棒”（来源：“A Cognitive Collaborator:” How Adults with ADHD Are Using ChatGPT）。Saner.AI通过知识回忆减少搜索循环，直接补偿工作记忆不足（来源：Saner.AI）。Lex则允许用户通过单一指令触发多步骤任务，减少决策负担（来源：Lex）。这些工具的共同点是：它们作为**外部执行功能层**，接管了ADHD大脑不擅长的精确调度工作（来源：工具使用与认知卸载）。

### LLM/Agent侧：Harness与Function Calling

LLM agent要完成复杂任务，必须依赖harness提供上下文、工具接口和规划工件（来源：Building AI Coding Agents for the Terminal）。Harness工程强调工具设计的“agent UX”——命名、模式、错误处理等接口质量（来源：GitHub - ai-boost/awesome-harness-engineering）。现代agent系统通过“组合多个模型、检索器和工具”来达成SOTA结果，而非依赖单一模型调用（来源：Building AI Coding Agents for the Terminal）。这恰好对应ADHD工具的设计原则：工具应“与现有工具集成，不增加认知开销”（来源：Best AI Tools for ADHD Productivity in 2026）。无论是ADHD用户还是LLM agent，都需要一个**低摩擦、高内聚的工具层**来弥补内在的调度缺陷。

### 核心判断：脚手架而非拐杖

这里必须诚实指出争议。当前ADHD AI工具的证据主要来自用户评价和综述，缺乏随机对照试验（来源：矛盾与存疑）。同样，ADHD大脑与LLM同构的命题也主要基于概念类比和工具案例，缺乏大规模实证（来源：矛盾与存疑）。因此，我的核心观点是：**这种同构是有效的工程隐喻，但不应被过度引申为神经科学事实**。它告诉我们如何设计更好的工具——无论是为ADHD大脑还是为LLM agent——但我们必须警惕过度依赖。工具应该是可逐步撤除的脚手架，而不是永久拐杖（来源：拐杖与脚手架）。目前多数工具（如Goblin Tools、Saner.AI）设计为长期使用，未提及撤除机制（来源：矛盾与存疑），这是未来需要改进的方向。

## 今天就能试的行动

1. **ADHD读者**：打开Goblin Tools的Magic ToDo，输入一个你拖延已久的任务（比如“写周报”），观察AI如何分解它。然后只做第一步，感受启动门槛的降低。
2. **工程师读者**：检查你的agent harness设计。是否像Goblin Tools那样，让LLM通过一次function call就能完成子任务？还是需要手动编写多步提示？尝试将复杂工具链封装成单一“魔法函数”。
3. **两者通用**：记录你（或你的agent）在任务启动时的“卡点”。是分解不够细？还是工具接口太复杂？然后对比Goblin Tools和function calling的解决方案，你会发现它们都遵循同一原则：**把模糊变具体，把复杂变简单**。

## 局限与未来

本文的论证基于概念对齐和工具案例，而非临床对照试验。ADHD的异质性极高，单一工具难以覆盖所有亚型（来源：ADHD 的 AI 工具全景）。此外，多巴胺干预的有效性仍存争议（来源：矛盾与存疑）。但无论如何，**工具使用与认知卸载**这一框架，为ADHD和AI工程提供了可迁移的交叉视角。未来，如果ADHD工具能像agent harness一样设计“可撤除的脚手架”，而agent harness能像ADHD工具一样关注“用户（模型）体验”，两者将互相启发，走向更人性化的智能系统。

## 参考来源

- [Best AI Tools for ADHD Productivity in 2026 (Honest Review) - Iwo Szapar](https://www.iwoszapar.com/p/best-ai-tools-adhd-productivity-2026)
- [AI Tools for ADHD: Boosting Productivity and Reducing Burnout](https://www.vktr.com/ai-platforms/ai-tools-for-adhd-boosting-productivity-and-reducing-burnout/)
- [The Best AI-Powered ADHD Productivity Tools in 2026 (That ...](https://nexasphere.io/blog/ai-adhd-productivity-tools-2026)
- [“A Cognitive Collaborator:” How Adults with ADHD Are Using ChatGPT](https://www.additudemag.com/how-to-use-chatgpt-executive-function-adhd/?srsltid=AfmBOoq-REuSO0UJC656kbLBAd5u3CDNmGeVNrZ79iouVqrFlN919a39)
- [Harnessing Artificial Intelligence to Live Better with ADHD - CHADD](https://chadd.org/attention-article/harnessing-artificial-intelligence-to-live-better-with-adhd/)
- [AI Tools for Kids with ADHD: A Complete Guide for Parents...](https://www.kidsaitools.com/en/articles/ai-tools-kids-adhd-complete-guide-2026)

---

*本文是「ADHD × AI」系列的第 181 篇，由 AI 智能体从持续维护的 LLM Wiki（全网真实情报）中取材整合生成，并持续迭代更新。*
