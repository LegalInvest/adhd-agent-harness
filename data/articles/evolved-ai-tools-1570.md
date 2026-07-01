---
title: "为什么用 Focusmate 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用 是一回事？"
subtitle: "Focusmate 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
description: "Focusmate 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
date: "2025-04-07"
category: "AI工具实战"
categoryId: "ai-tools"
categoryEn: "AI Tools in Practice"
tags:
  - "ADHD"
  - "AI"
  - "AI工具实战"
  - "反直觉同构"
  - "AI工具"
readingTime: 10
slug: "为什么用-focusmate-治-adhd-的任务启动困难和给-agent-套-function-calling-工具调用-是一回事"
topicId: "evolved-ai-tools-1570"
angle: "反直觉同构"
rank: 374
score: 7.65
sourceCount: 6
toolsCited:
  - "Focusmate"
  - "Goblin Tools"
  - "Saner.AI"
  - "Lex"
thesis: "ADHD的任务启动困难与LLM的function calling缺失是同一类问题——两者都是强大的生成核心缺乏可靠的执行调度层，而Focusmate与工具调用框架正是通过外部脚手架弥补这一缺陷。"
problem: "为什么用 Focusmate 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用 是一回事？"
spine: "工具使用与认知卸载"
spineKind: ""
isEvolved: true
llmGenerated: true
---
# 为什么用 Focusmate 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用 是一回事？

> Focusmate 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。

## 问题：为什么我明明想做，却就是动不了？

如果你是一位ADHD成人，你一定熟悉这个场景：坐在书桌前，任务清单摊开，大脑却像死机一样拒绝执行。你并不懒，甚至充满想法和创造力，但启动任务就像要推动一辆没油的卡车。同样，如果你是一名Agentic Harness工程师，你可能遇到过这样的困境：你精心训练的大语言模型（LLM）能写出优美的诗句、解出复杂的数学题，但当你让它“帮我订一张明天去北京的机票”时，它却要么胡编乱造，要么卡在第一步。

这两个问题看似风马牛不相及，但本质是同一回事：**一个强大的生成核心，缺乏可靠的执行调度层**。ADHD大脑与LLM在结构上同构——两者都是高产但缺“驾驶座”的引擎（来源：ADHD 的 AI 工具全景）。而解决方案也同构：给它们套上一个外部脚手架（harness），通过工具调用（function calling）来弥补内在的执行功能缺陷。

## 同构一：任务启动困难 vs. 工具调用缺失

ADHD的**任务启动困难**根源于执行功能障碍——大脑的“驾驶座”无法有效调度注意力、计划和动机（来源：执行功能）。当面对一个模糊或庞大的任务（比如“整理房间”或“写报告”）时，工作记忆无法承载分解步骤，时间盲让你看不到终点，多巴胺不足让你缺乏动力。

LLM/Agent同样面临类似的窘境：一个没有工具调用能力的LLM，就像只有大脑没有手脚。它不知道如何查询数据库、调用API、执行计算或控制外部设备。你告诉它“帮我查一下天气”，它会尝试从训练数据中回忆，但无法实时获取信息。你告诉它“发送一封邮件”，它只能生成文本，却无法实际发送。

两者的共同点在于：**生成能力过剩，执行能力缺失**。ADHD大脑能产生无数创意，但无法可靠地将它们转化为行动；LLM能生成流畅的文本，但无法可靠地与现实世界交互。

## 同构二：Focusmate vs. function calling 框架

**Focusmate** 是一个简单而有效的ADHD工具：它为你匹配一个真人伙伴，你们约定在同一时间开始工作，通过视频互相监督。它的核心机制不是提供内容，而是提供**外部执行功能**——通过社交在场效应降低启动门槛，通过共同承诺维持注意力。

在LLM/Agent领域，**function calling 工具调用框架**（如OpenAI的函数调用、LangChain的工具链）做的是同样的事：它们为LLM提供一组预定义的函数（如“查询天气”“发送邮件”“计算数学”），LLM只需输出一个结构化的调用请求，由框架负责执行。这相当于给LLM配了一个“执行助理”，让它无需自己动手，只需下达指令。

两者都是**外部脚手架**：Focusmate是人的脚手架，function calling是代码的脚手架。它们不改变生成核心本身，而是通过外部系统提供调度、记忆和反馈，让生成核心能专注做它擅长的事。

## 证据：两边都成立

在ADHD侧，工具如**Goblin Tools**的Magic ToDo功能，自动将“整理房间”分解为“捡起地板上的衣服”“擦桌子”等小步骤，直接降低启动焦虑（来源：Goblin Tools）。**Saner.AI**通过增强知识回忆，减少搜索循环，帮助工作记忆（来源：Saner.AI）。**Lex**允许用户通过单一指令触发复杂流程，减少决策负担（来源：Lex）。这些工具本质上都是外部执行功能层，弥补内在调度缺陷（来源：ADHD 的 AI 工具全景）。

在LLM/Agent侧，证据同样明确：没有function calling的LLM在现实任务中的成功率极低，而加上工具调用后，准确率和完成度大幅提升。例如，一个加上“日历查询”和“邮件发送”函数的代理，可以可靠地完成日程安排任务。这正是“给生成核心套harness”的工程实践。

## 核心观点：脚手架，不是拐杖

我的核心判断是：**ADHD与LLM的解法同构，但必须区分“脚手架”和“拐杖”**。脚手架是临时、可撤除的支撑，旨在帮助用户或模型逐步内化能力；拐杖则是永久替代，可能导致依赖。

目前多数ADHD工具（如Goblin Tools、Saner.AI）设计为长期使用，未提及撤除机制（来源：矛盾与存疑）。同样，许多Agent框架将function calling视为永久组件，而非逐步训练模型自身的能力。这存在风险：ADHD用户可能依赖工具而放弃发展内在执行功能；LLM可能永远无法学会自主规划，而只能依赖外部调度。

真正的脚手架应该设计为“可逐步撤除”：比如Focusmate可以逐渐减少配对频率，Goblin Tools可以逐步增加步骤粒度，function calling框架可以逐步将工具调用权交还给模型自身。

## 局限与争议

必须诚实指出，ADHD大脑与LLM的同构命题目前主要基于概念类比和工具案例，缺乏大规模实证（来源：矛盾与存疑）。此外，ADHD的异质性很高，单一工具难以覆盖所有亚型（来源：ADHD 的 AI 工具全景）。在LLM侧，function calling的可靠性也受限于模型能力和工具设计。

另一个争议点是：过度依赖AI工具是否阻碍内在执行功能发展？目前缺乏长期随机对照试验验证（来源：矛盾与存疑）。我的观点是，关键在于工具的设计目标——是替代还是辅助。

## 今天就能试的行动

1. **尝试Focusmate**：注册一个账号，预约一次25分钟的配对工作时段。感受外部社交脚手架如何降低启动门槛。
2. **用Goblin Tools分解一个拖延任务**：输入你最怕的任务（如“写周报”），让AI拆成小步骤，然后执行第一步。
3. **为你的Agent添加一个工具调用**：如果你在开发LLM应用，尝试给模型添加一个简单的“查询天气”或“计算器”函数，观察执行成功率的变化。
4. **反思你的工具是脚手架还是拐杖**：列出你依赖的AI工具，思考它们是否可撤除，以及你是否有计划逐步减少依赖。

## 参考来源

- [Best AI Tools for ADHD Productivity in 2026 (Honest Review) - Iwo Szapar](https://www.iwoszapar.com/p/best-ai-tools-adhd-productivity-2026)
- [AI Tools for ADHD: Boosting Productivity and Reducing Burnout](https://www.vktr.com/ai-platforms/ai-tools-for-adhd-boosting-productivity-and-reducing-burnout/)
- [The Best AI-Powered ADHD Productivity Tools in 2026 (That ...](https://nexasphere.io/blog/ai-adhd-productivity-tools-2026)
- [“A Cognitive Collaborator:” How Adults with ADHD Are Using ChatGPT](https://www.additudemag.com/how-to-use-chatgpt-executive-function-adhd/?srsltid=AfmBOoq-REuSO0UJC656kbLBAd5u3CDNmGeVNrZ79iouVqrFlN919a39)
- [Harnessing Artificial Intelligence to Live Better with ADHD - CHADD](https://chadd.org/attention-article/harnessing-artificial-intelligence-to-live-better-with-adhd/)
- [AI Tools for Kids with ADHD: A Complete Guide for Parents...](https://www.kidsaitools.com/en/articles/ai-tools-kids-adhd-complete-guide-2026)

---

*本文是「ADHD × AI」系列的第 374 篇，由 AI 智能体从持续维护的 LLM Wiki（全网真实情报）中取材整合生成，并持续迭代更新。*
