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
topicId: "evolved-ai-tools-1575"
angle: "反直觉同构"
rank: 137
score: 7.79
sourceCount: 6
toolsCited:
  - "Goblin Tools"
  - "Saner.AI"
  - "Lex"
  - "Claude"
  - "Focusmate"
thesis: "ADHD大脑与LLM在结构上同构——都是强大的生成核心但缺乏可靠的执行调度层，因此给Claude套function calling工具调用（harness）与用AI工具治ADHD的任务启动困难，本质上是同一套外部执行功能层的构建逻辑。"
problem: "为什么用 Claude 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用 是一回事？"
spine: "工具使用与认知卸载"
spineKind: ""
isEvolved: true
llmGenerated: true
---
# 为什么用 Claude 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用 是一回事？

> Claude 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。

## 问题：为什么我对着空白文档半小时，Claude也对着空白函数发呆？

如果你是一名ADHD患者，你一定经历过这种场景：脑子里有一整篇文章的轮廓，但光标在空白页上闪烁，你无法按下第一个键。如果你是一名Agentic Harness工程师，你一定也见过这种场景：LLM模型明明有足够的知识，却在工具调用时卡住，输出一个空函数或循环日志。

这两个问题看似分属心理学和工程学，但本质是同一个结构缺陷的两种表现。

## 同构：高产但缺执行调度层的生成核心

ADHD大脑与LLM在结构上高度同构：两者都是强大的生成核心（发散思维、创意、多任务并行），但缺乏可靠的执行调度层（计划、组织、任务启动、持续专注）（来源：ADHD 的 AI 工具全景）。ADHD患者的执行功能缺陷导致任务启动困难——不是不想做，而是大脑的“启动引擎”无法挂挡。LLM同样如此：它能生成流畅的文本，但在长程任务中容易“忘记系统提示”，产生目标漂移，无法可靠地调用工具（来源：重锚定与目标漂移）。

因此，解决ADHD任务启动困难的方法，与让LLM可靠调用工具的方法，在结构上是同构的：都是通过外部工具提供执行功能、记忆管理和上下文控制，弥补内在调度缺陷（来源：ADHD 的 AI 工具全景）。

## 证据：同一套harness思路，两边都成立

### ADHD侧：外部执行功能层

ADHD患者常用的AI工具，本质上都是在构建一个外部执行功能层。

- **任务分解**：Goblin Tools的Magic ToDo功能自动将“整理房间”分解为“捡起地板上的衣服”“擦桌子”等小步骤，降低启动门槛（来源：Goblin Tools）。这相当于给ADHD大脑一个分步执行的“函数链”，避免因目标过大而卡住。
- **单一指令触发多步骤**：Lex允许用户通过一条指令触发复杂任务序列，减少决策负担（来源：Lex）。这相当于给ADHD大脑一个“宏命令”，一键执行多个子任务。
- **记忆管理**：Saner.AI通过本地记忆和快速检索减少搜索循环，补偿工作记忆不足（来源：Saner.AI）。这相当于给ADHD大脑一个外部缓存，避免信息丢失。

这些工具的共同逻辑是：将ADHD大脑的“生成核心”与一个外部调度层连接，让调度层负责启动、排序、记忆，生成核心只负责创造。

### LLM/Agent侧：Harness与Function Calling

在Agent工程中，Harness（脚手架）正是扮演这个外部调度层的角色。

- **防止目标漂移**：LLM agent在长程任务中会“开始忘记系统提示”，Harness通过事件驱动的系统提醒来对抗指令消退（来源：重锚定与目标漂移）。这与ADHD工具通过提醒和通知提供重锚定完全一致。
- **人在回路监督**：Harness引入human-in-the-loop检查点，暂停并询问后再执行（来源：人在回路与身体在场）。ADHD患者使用Focusmate等虚拟身体搭档，通过外部问责绕过执行功能屏障，原理相同（来源：人在回路与身体在场）。
- **护栏与工具调用**：Harness设置token预算、工具调用次数上限、防止无限循环，使代理输出真正有用且正确（来源：人在回路与身体在场）。这类似于ADHD工具通过分解任务、设置提醒来防止“超聚焦”或“分心”。

因此，当你用Claude配合function calling工具（如MCP服务器）构建一个Agent时，你实际上是在给LLM套一个类似ADHD工具的外部执行功能层。

## 核心观点：脚手架而非拐杖

这里必须提出一个鲜明的判断：这种同构虽然强大，但存在一个关键边界——脚手架 vs 拐杖。

脚手架是“可逐步撤除的临时支撑”，目的是帮助内部能力发展；拐杖是“永久替代”，可能导致依赖（来源：矛盾与存疑）。ADHD工具和Agent harness目前都偏向“拐杖”设计：Goblin Tools、Saner.AI等工具未提及撤除机制，长期使用可能阻碍内在执行功能的发展（来源：矛盾与存疑）。同样，Agent harness如果过度依赖外部调度，模型本身的规划能力可能退化。

因此，真正的解决方案不是永远依赖外部工具，而是设计“可撤除的脚手架”：让ADHD患者在使用中逐步内化任务分解、时间管理等技能；让Agent在训练中逐步减少对harness的依赖。但当前证据主要来自概念类比和用户反馈，缺乏大规模实证支持（来源：矛盾与存疑）。

## 今天就能试的行动

1. **ADHD读者**：下次任务启动困难时，用Goblin Tools的Magic ToDo输入你的任务，让AI分解成5个以内的小步骤。完成第一步后，再让AI分解下一步。
2. **Agent工程师**：在Harness中增加一个“重锚定”机制：每5轮工具调用后，自动插入系统提示重申核心目标，防止模型漂移。
3. **两者通用**：尝试用Claude写一个自定义指令，将你的常见任务（如“写周报”“整理笔记”）定义为可复用的“函数”，每次只需调用函数名即可触发多步流程。

## 局限与争议

- **证据强度**：ADHD大脑与LLM同构的命题缺乏大规模实证，主要基于概念类比（来源：矛盾与存疑）。
- **个性化不足**：ADHD异质性高，单一工具难以覆盖所有亚型（来源：ADHD 的 AI 工具全景）。
- **长期效果未知**：现有证据多为短期或个案，缺乏随机对照试验（来源：ADHD 的 AI 工具全景）。

承认这些局限，反而让同构视角更有价值——它提供了一个可验证的框架，等待工程和临床的双重检验。

## 参考来源

- [Best AI Tools for ADHD Productivity in 2026 (Honest Review) - Iwo Szapar](https://www.iwoszapar.com/p/best-ai-tools-adhd-productivity-2026)
- [AI Tools for ADHD: Boosting Productivity and Reducing Burnout](https://www.vktr.com/ai-platforms/ai-tools-for-adhd-boosting-productivity-and-reducing-burnout/)
- [The Best AI-Powered ADHD Productivity Tools in 2026 (That ...](https://nexasphere.io/blog/ai-adhd-productivity-tools-2026)
- [“A Cognitive Collaborator:” How Adults with ADHD Are Using ChatGPT](https://www.additudemag.com/how-to-use-chatgpt-executive-function-adhd/?srsltid=AfmBOoq-REuSO0UJC656kbLBAd5u3CDNmGeVNrZ79iouVqrFlN919a39)
- [Harnessing Artificial Intelligence to Live Better with ADHD - CHADD](https://chadd.org/attention-article/harnessing-artificial-intelligence-to-live-better-with-adhd/)
- [AI Tools for Kids with ADHD: A Complete Guide for Parents...](https://www.kidsaitools.com/en/articles/ai-tools-kids-adhd-complete-guide-2026)

---

*本文是「ADHD × AI」系列的第 137 篇，由 AI 智能体从持续维护的 LLM Wiki（全网真实情报）中取材整合生成，并持续迭代更新。*
