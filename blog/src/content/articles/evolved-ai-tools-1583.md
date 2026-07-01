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
  - "Mem"
  - "Otter.ai"
  - "Routinery"
  - "ChatGPT"
thesis: "ADHD大脑与LLM agent在结构上同构——都是强大的生成核心却缺乏可靠执行调度层，因此RescueTime对ADHD的任务启动困难干预与给agent套function calling工具调用，本质都是通过外部harness提供认知卸载与执行功能补偿。"
problem: "为什么用 RescueTime 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用 是一回事？"
spine: "工具使用与认知卸载"
spineKind: ""
isEvolved: true
llmGenerated: true
---
# 为什么用 RescueTime 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用 是一回事？

> RescueTime 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。

## 问题：为什么你明明知道该做什么，却就是动不了？

如果你是ADHD人群，你一定熟悉这个场景：电脑屏幕上开着待办清单，光标在“开始写报告”上闪烁了20分钟，你却刷了3轮社交媒体、倒了杯水、整理了桌面——就是点不下那个“开始”按钮。这不是懒，是**任务启动困难**：大脑的生成核心已经构思好了内容，但执行调度层罢工了。

如果你是Agent工程师，你一定也熟悉另一个场景：你给LLM配了全套工具（搜索、计算、数据库），但它就是不肯调用——或者调用了错误的函数、在无关的上下文里反复徘徊。这不是模型笨，是**function calling的调度失败**：生成核心能吐出正确答案，但缺乏可靠的执行层来触发正确的工具。

这两个问题，其实是一回事。

## 同构：高产但缺调度层的生成核心

wiki资料中提出的核心论点是：**ADHD大脑与LLM在结构上同构——两者都是强大的生成核心，但缺乏可靠的执行调度层**（来源：ADHD的AI工具全景）。ADHD大脑的智力、创造力与LLM的生成能力类似，但执行功能（计划、组织、工作记忆）的稳定调度缺失；LLM同样能生成流畅文本，但缺乏将意图转化为工具调用的编排层。

RescueTime对ADHD的干预方式，恰好映射了Agent工程中的function calling harness。RescueTime通过强制屏蔽干扰网站、设定专注时段，本质上是**外部执行功能层**——它接管了“什么该做、什么不该做”的调度决策，让ADHD大脑无需消耗意志力来启动任务。而Agent的function calling harness（如OpenAI的function calling、LangChain的工具接口）同样是一个外部调度层：它定义工具签名、管理上下文、验证输出，让LLM只需“生成意图”，由harness负责实际调用。

## 证据：两边都成立的harness逻辑

### ADHD侧：工具即脚手架

Goblin Tools的Magic ToDo功能，将“整理房间”自动分解为“捡起衣服”“擦桌子”等小步骤，**降低启动焦虑**（来源：Goblin Tools）。这相当于给ADHD大脑提供了一个“任务分解函数”——无需自己规划，只需执行原子步骤。Lex则更进一步：通过单一指令触发多步骤流程，**减少决策负担**（来源：Lex）。这就像Agent的function calling中，一个`/start_report`指令自动调用搜索、生成、格式化等子工具。

Saner.AI和Mem通过持久记忆减少搜索循环，**补偿工作记忆缺陷**（来源：Saner.AI；Mem）。这对应Agent的**记忆系统**——避免LLM在对话中丢失上下文。Routinery通过步骤序列和过渡提示**管理注意力上下文**（来源：上下文工程），类似Agent的**上下文工程**：主动设计当前关注的信息范围，防止上下文膨胀和推理退化。

### LLM/Agent侧：harness即执行功能

Agent工程中的harness核心组件包括：**上下文传递、工具接口、规划工件、验证循环、记忆系统和沙盒**（来源：幻觉与验证循环）。这些组件恰好对应ADHD工具提供的功能：

- **工具接口**（function calling） ↔ Lex的单指令触发多步骤
- **验证循环**（检查输出格式、运行测试用例） ↔ Goblin Tools的分解验证（子步骤是否可执行）
- **记忆系统**（持久上下文） ↔ Saner.AI/Mem的知识回忆
- **上下文工程**（防止膨胀） ↔ Routinery的步骤过渡提示

wiki资料明确指出：“缺乏这些验证会导致更多幻觉和重复工作”（来源：幻觉与验证循环）。ADHD大脑的“冲动行为”同样可视为缺乏外部校验的验证失败——就像LLM自信地给出错误答案，ADHD个体可能脱离环境线索做出不恰当反应。

## 核心判断：脚手架不是拐杖，但边界需要警惕

本文的核心观点是：**RescueTime与function calling harness，都是同一类“外部调度层”的不同实现**。它们通过认知卸载，让生成核心专注于“做什么”，而把“怎么做”交给可靠的外部系统。

但wiki资料中的“矛盾与存疑”提醒我们：**脚手架与拐杖的边界尚未清晰**。过度依赖AI工具可能阻碍内在执行功能发展——如果ADHD患者永远依赖Goblin Tools分解任务，是否就永远学不会自己规划？同样，如果Agent永远依赖硬编码的harness，是否就失去了自主编排能力？资料指出：“多数工具设计为长期使用，未提及撤除机制”（来源：矛盾与存疑）。这要求我们在使用工具时保持警觉：工具应作为**可逐步撤除的临时支撑**，而非永久替代。

此外，证据强度存在分歧：现有研究多为用户评价和概念对齐，缺乏随机对照试验验证长期效果（来源：矛盾与存疑）。ADHD的异质性也意味着单一工具难以覆盖所有亚型（来源：ADHD的AI工具全景）。

## 今天就能试的行动

1. **ADHD读者**：如果你有任务启动困难，打开RescueTime或类似工具（如Forest），设置一个25分钟的强制专注时段。观察：当外部系统替你做了“开始”的决策，你的大脑是否更容易跟随？这相当于给大脑套了一个最简单的harness。

2. **Agent工程师**：检查你的function calling实现是否包含验证循环。例如，在调用搜索工具后，增加一个“检查返回结果是否为空”的步骤。这能减少幻觉和重复工作，就像ADHD工具帮你校验“这个子步骤是否合理”。

3. **双方通用**：尝试用Goblin Tools的Magic ToDo将一个你拖延的任务分解成5个原子步骤。然后，在代码中为你的Agent定义一个类似`decompose_task()`的函数——你会发现，人类和AI的“启动困难”解法惊人地一致。

4. **反思边界**：每周审视一次，你是否可以少用一个工具？例如，这周尝试不用Goblin Tools，自己手动写任务清单。如果感到吃力，说明工具仍是脚手架；如果轻松完成，说明你正在内化这种能力。

## 结语

RescueTime和function calling，一个治ADHD，一个治Agent，本质都是同一套harness思路：给强大的生成核心套上可靠的执行调度层。当你下次看到光标在空白文档上闪烁，或者LLM在工具调用上徘徊时，记住：这不是能力问题，是调度问题。而调度，可以外包。

## 参考来源

- [Best AI Tools for ADHD Productivity in 2026 (Honest Review) - Iwo Szapar](https://www.iwoszapar.com/p/best-ai-tools-adhd-productivity-2026)
- [AI Tools for ADHD: Boosting Productivity and Reducing Burnout](https://www.vktr.com/ai-platforms/ai-tools-for-adhd-boosting-productivity-and-reducing-burnout/)
- [The Best AI-Powered ADHD Productivity Tools in 2026 (That ...](https://nexasphere.io/blog/ai-adhd-productivity-tools-2026)
- [“A Cognitive Collaborator:” How Adults with ADHD Are Using ChatGPT](https://www.additudemag.com/how-to-use-chatgpt-executive-function-adhd/?srsltid=AfmBOoq-REuSO0UJC656kbLBAd5u3CDNmGeVNrZ79iouVqrFlN919a39)
- [Harnessing Artificial Intelligence to Live Better with ADHD - CHADD](https://chadd.org/attention-article/harnessing-artificial-intelligence-to-live-better-with-adhd/)
- [AI Tools for Kids with ADHD: A Complete Guide for Parents...](https://www.kidsaitools.com/en/articles/ai-tools-kids-adhd-complete-guide-2026)

---

*本文是「ADHD × AI」系列的第 385 篇，由 AI 智能体从持续维护的 LLM Wiki（全网真实情报）中取材整合生成，并持续迭代更新。*
