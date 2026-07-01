---
title: "为什么用 ChatGPT 治 ADHD 的情绪失调，和给 agent 套 会褪去的脚手架 是一回事？"
subtitle: "ChatGPT 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
description: "ChatGPT 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
date: "2025-05-16"
category: "情绪调节"
categoryId: "emotion"
categoryEn: "Emotional Regulation"
tags:
  - "ADHD"
  - "AI"
  - "情绪调节"
  - "反直觉同构"
  - "焦虑"
readingTime: 13
slug: "为什么用-chatgpt-治-adhd-的情绪失调和给-agent-套-会褪去的脚手架-是一回事"
topicId: "evolved-emotion-1643"
angle: "反直觉同构"
rank: 12
score: 8.11
sourceCount: 6
toolsCited:
  - "ChatGPT"
  - "Inflow"
  - "Goblin Tools"
  - "Saner.AI"
thesis: "ADHD的情绪失调与LLM的调度失败本质是同一类问题——高产但缺乏执行调度层的生成核心；两者的解法也同构：用可撤除的外部脚手架（harness）补偿调度缺陷，而非制造永久拐杖。"
problem: "为什么用 ChatGPT 治 ADHD 的情绪失调，和给 agent 套 会褪去的脚手架 是一回事？"
spine: "拐杖与脚手架"
spineKind: ""
isEvolved: true
llmGenerated: true
---
# 为什么用 ChatGPT 治 ADHD 的情绪失调，和给 agent 套 会褪去的脚手架 是一回事？

> ChatGPT 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。

## 问题：为什么我用ChatGPT治情绪失调，感觉像在给一个失控的AI套缰绳？

如果你是一个ADHD患者，你一定经历过这种时刻：明明脑子里有无数想法，却像被锁在椅子上，无法启动任何一件事；情绪突然崩盘，因为工作记忆里塞满了未完成的任务，时间感彻底失灵。你打开ChatGPT，让它帮你分解任务、提醒下一步、甚至当个情绪树洞——它确实有用，但你隐约担心：我是不是在依赖一个拐杖？会不会越来越离不开它？

如果你是一个Agentic Harness工程师，你也熟悉另一种崩溃：你精心构建的LLM agent，明明有强大的生成能力，却在执行多步任务时丢失上下文、决策混乱、卡在无限循环里。你给它套上脚手架——上下文管理、工具调用、验证循环——它才勉强跑通。但你心里清楚：这个脚手架一旦撤掉，agent立刻瘫痪。

这两个场景，看似风马牛不相及。但它们的核心问题完全同构：**一个高产但缺乏执行调度层的生成核心，如何在不被永久拐杖绑架的前提下，获得临时的、可撤除的调度支持？**

## 同构：ADHD大脑与LLM，共享同一个脆弱架构

ADHD大脑的本质，wiki资料总结得很清楚：**“高产但无序的生成能力，同时缺乏可靠的执行调度层”**（来源：ADHD 大脑与 LLM 的同构）。你智力不低，创意爆棚，但工作记忆像漏水的桶，任务启动像踩油门时手刹没松，时间盲让你永远活在“现在”或“来不及”两个极端。情绪失调，本质上是调度层崩溃的副产品——当执行功能无法处理信息流，情绪就成了第一个被冲垮的堤坝。

LLM呢？它同样是一个强大的生成核心（海量参数、流畅文本），但本身**无状态、无内置调度**。你需要harness来包裹它：**“包裹LLM或AI agent的软件基础设施，处理模型本身之外的一切”**（来源：ADHD 大脑与 LLM 的同构）。Harness负责上下文管理、工具调用、工作流编排——这些，恰好对应ADHD大脑缺失的执行功能。

看这张对应表：

| ADHD大脑 | LLM + Harness |
|----------|---------------|
| 高产但缺执行调度层的生成核心 | 高生成能力但需外部调度的LLM |
| 工作记忆易丢失上下文 | LLM无状态，需外部记忆管理 |
| 需要AI助手减少决策、保留上下文 | Harness负责上下文工程和决策路由 |
| 外部工具（如Goblin Tools）作为执行功能支架 | Harness中的模型连接器、工具调用 |
| 多巴胺驱动任务启动困难 | 缺乏内在奖励机制，需外部提示 |

（来源：ADHD 大脑与 LLM 的同构）

所以，当你用ChatGPT治情绪失调时，你其实是在为自己设计一个**个人版harness**——你把“下一步做什么”外包给AI，让它帮你记住上下文、分解任务、提供情绪锚点。这和工程师给LLM套脚手架，本质是同一件事。

## 证据：两边都站得住脚的真实案例

在ADHD侧，工具如**Goblin Tools**的Magic ToDo功能，能将“整理房间”自动分解为“捡起地板上的衣服”“擦桌子”等步骤，**“将压倒性的事情变成一系列不压倒性的事情”**（来源：Goblin Tools）。这直接降低了任务启动门槛，减少了因拖延引发的自责情绪。**Saner.AI**则通过本地记忆存储和快速检索，减少搜索循环和标签切换，**直接针对ADHD用户常见的“信息丢失”和“注意力分散”问题**（来源：Saner.AI）。**Inflow**更进一步，通过AI算法个性化训练工作记忆，靶向背外侧前额叶皮层——**研究指出该区域功能连接性与工作记忆表现正相关**（来源：Inflow）。这些工具都在做同一件事：为ADHD大脑提供临时的外部执行功能层。

在LLM/agent侧，harness工程的定义是：**“设计围绕AI代理的脚手架——上下文交付、工具接口、规划工件、验证循环、记忆系统和沙箱”**（来源：外部执行功能层）。具体实现包括用Git仓库存储项目上下文（类似ADHD侧的Second Brain），通过MCP连接器访问外部数据，以及将控制逻辑外化为可移植的自然语言工件。这些组件，和ADHD工具中的“任务分解”“上下文保存”“决策提示”一一对应。

两边共享同一个设计原则：**不要试图修复生成核心，而是围绕它构建可撤除的调度层。**

## 核心判断：脚手架 vs 拐杖——边界在哪里？

这里必须诚实指出争议。wiki资料中的**矛盾与存疑**页面明确警告：**“脚手架应设计为可逐步撤除的临时支撑，但多数工具（如Goblin Tools、Saner.AI）设计为长期使用，未提及撤除机制”**（来源：矛盾与存疑）。过度依赖的风险真实存在——AI工具可能**“削弱内在情绪调节能力”**（来源：AI 与 ADHD 的情绪调节）。

我的判断是：**脚手架和拐杖的边界，在于你是否主动设计“褪去机制”。** 一个合格的harness，应该在每个交互中同时提供两样东西：①即时的调度支持（帮你完成当前任务）；②一条隐性的学习线索（让你逐渐内化这个调度模式）。比如，Goblin Tools分解任务时，可以额外显示“为什么这样分解”的思路；ChatGPT在帮你梳理情绪时，可以引导你识别触发模式，而不是只给安慰。工程侧同样：agent的harness应该记录每次决策的上下文，并在任务完成后生成可复用的“决策模板”，让下一次执行更少依赖外部编排。

遗憾的是，当前大多数工具和harness只做到了第一点。**“长期效果证据缺乏”**（来源：AI 与 ADHD 的情绪调节）是两边共同的短板。

## 今天就能试的3个行动

1. **为你的ChatGPT对话设计“褪去提示”**：每次让AI帮你分解任务或调节情绪时，在最后加一句：“请用一句话总结这个过程中最关键的一步，以便我下次自己尝试。”这相当于在harness中嵌入学习回路。

2. **用“上下文保存”替代“从头开始”**：如果你用ChatGPT做项目，每次结束前让它生成一个“上下文摘要”（类似agent的checkpoint）。下次开始时，先粘贴摘要再提问。这模仿了harness中的记忆系统，同时训练你主动管理上下文。

3. **在情绪崩溃时，让AI只做“调度员”而非“疗愈师”**：明确告诉它：“不要安慰我，只帮我列出接下来3个可操作的步骤，每个步骤不超过5分钟。”这直接对应agent harness中的“决策路由”——把情绪能量导向具体行动，而非沉溺在情绪中。

## 局限：同构不是万能钥匙

这个同构框架目前**“证据主要来自概念类比和工具案例，缺乏大规模实证”**（来源：矛盾与存疑）。它提供了一个有力的思考模型，但不能替代临床治疗或工程验证。情绪失调的根源可能涉及神经递质、共病焦虑等复杂因素，不是所有harness都能覆盖。同样，agent harness的挑战（如安全执行、多代理协调）也超越了简单的“上下文管理”类比。

但恰恰是这种不完美，让同构有价值——它让ADHD患者看到：你的大脑不是坏的，只是缺一个可设计的调度层；也让工程师看到：你造的脚手架，本质上是在为另一个“大脑”做同样的事。两边的人，可以互相学习。

## 参考来源

- [Dynamic causal brain circuits during working memory and their functional controllability](https://doi.org/10.1038/s41467-021-23509-x)
- [Best AI Tools for ADHD Productivity in 2026 (Honest Review) - Iwo Szapar](https://www.iwoszapar.com/p/best-ai-tools-adhd-productivity-2026)
- [AI Tools for ADHD: Boosting Productivity and Reducing Burnout](https://www.vktr.com/ai-platforms/ai-tools-for-adhd-boosting-productivity-and-reducing-burnout/)
- [The Best AI-Powered ADHD Productivity Tools in 2026 (That ...](https://nexasphere.io/blog/ai-adhd-productivity-tools-2026)
- [“A Cognitive Collaborator:” How Adults with ADHD Are Using ChatGPT](https://www.additudemag.com/how-to-use-chatgpt-executive-function-adhd/?srsltid=AfmBOoq-REuSO0UJC656kbLBAd5u3CDNmGeVNrZ79iouVqrFlN919a39)
- [Harnessing Artificial Intelligence to Live Better with ADHD - CHADD](https://chadd.org/attention-article/harnessing-artificial-intelligence-to-live-better-with-adhd/)

---

*本文是「ADHD × AI」系列的第 12 篇，由 AI 智能体从持续维护的 LLM Wiki（全网真实情报）中取材整合生成，并持续迭代更新。*
