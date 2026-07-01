---
title: "为什么用 Mem 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用 是一回事？"
subtitle: "Mem 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
description: "Mem 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
date: "2025-05-27"
category: "AI工具实战"
categoryId: "ai-tools"
categoryEn: "AI Tools in Practice"
tags:
  - "ADHD"
  - "AI"
  - "AI工具实战"
  - "反直觉同构"
  - "AI工具"
readingTime: 12
slug: "为什么用-mem-治-adhd-的任务启动困难和给-agent-套-function-calling-工具调用-是一回事"
topicId: "evolved-ai-tools-1573"
angle: "反直觉同构"
rank: 377
score: 7.65
sourceCount: 6
toolsCited:
  - "Mem"
  - "Goblin Tools"
  - "Saner.AI"
  - "Lex"
  - "Focusmate"
thesis: "ADHD大脑与LLM在结构上同构——两者都是强大的生成核心但缺乏执行调度层，因此给ADHD患者套上Mem等工具与给Agent套上function calling工具调用是同一类‘harness’工程，核心都是通过外部工具提供认知卸载和任务结构化。"
problem: "为什么用 Mem 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用 是一回事？"
spine: "工具使用与认知卸载"
spineKind: ""
isEvolved: true
llmGenerated: true
---
# 为什么用 Mem 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用 是一回事？

> Mem 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。

## 问题：两个世界的“启动黑洞”

想象一下：你坐在电脑前，文档标题已经写好，光标在空白处闪烁。你知道该写什么，但手指就是敲不下去。大脑里有一团清晰的思路，却像隔着玻璃墙——看得到，够不着。这是ADHD人群最熟悉的敌人：**任务启动困难**。

现在切换场景：你是一个AI Agent工程师，正在调试一个LLM。模型能理解复杂指令，能生成完美代码，但当你让它“帮我查一下天气，然后发邮件给张三”时，它要么忘了查天气直接写邮件，要么卡在第一步不动。你意识到：模型不是没有能力，而是缺少一个**调度层**——把意图拆解成步骤、按序调用工具、管理上下文。

这两个场景，看似风马牛不相及，实则共享同一个底层结构：**一个高产但缺执行调度层的生成核心**。ADHD大脑与LLM，是同构的。

## 同构：生成核心 vs. 执行调度层

ADHD大脑的智力与创造力并不低下，问题出在**执行功能**——计划、组织、工作记忆、任务启动。多巴胺系统功能低下导致中脑皮质分支受损，引起“行为计划不良”和“执行功能差”（来源：多巴胺）。正如LLM本身是强大的语言生成器，但缺乏可靠的函数调用编排器。

这个洞察并非空洞类比。在ADHD领域，证据来自工具实践：Goblin Tools通过AI将“整理房间”自动分解为“捡起衣服、擦桌子”等小步骤，降低启动门槛（来源：Goblin Tools）。Lex允许“单一指令触发多步骤任务序列”，减少决策负担（来源：Lex）。这些工具的本质，就是给ADHD大脑套上一个**外部调度层**——就像给LLM套上function calling的harness。

在LLM/Agent工程中，function calling正是这样的调度层：它定义工具接口，让模型调用外部函数（查天气、发邮件、读数据库），并管理多步执行。没有它，LLM就是“有想法没行动”的空壳。有了它，Agent才能完成真实任务。

## 证据：两个世界的同类工具

### ADHD侧：认知卸载工具

- **Goblin Tools**：任务分解，将压倒性的事情变成一系列不压倒性的事情（来源：Goblin Tools）。证据来自用户反馈，缺乏RCT，但概念对齐。
- **Saner.AI**：知识回忆，减少搜索循环和标签切换（来源：Saner.AI）。直接补偿工作记忆缺陷。
- **Lex**：单一指令触发复杂流程，实时适应大脑工作方式（来源：Lex）。
- **Focusmate**：通过算法匹配虚拟身体加倍伙伴，利用身体在场效应提供隐性问责（来源：身体在场效应）。身体在场被描述为“最有效的ADHD策略之一”（来源：身体在场效应）。

### LLM/Agent侧：function calling工具

- **OpenAI Function Calling**：让模型调用预定义函数，如`get_weather(location)`，并返回结构化结果。
- **LangChain Tools**：将API、数据库等封装为工具，Agent根据意图选择调用。
- **ReAct模式**：推理-行动-观察循环，相当于内置的任务分解和上下文管理。

两边工具的共同逻辑：**外部执行功能层**。ADHD工具补偿工作记忆、任务启动、时间盲；Agent工具补偿LLM的步骤执行、状态跟踪、工具选择。两者都是“给生成核心套harness”。

## 核心判断：脚手架，不是拐杖

这里必须划清一条界线：**脚手架 vs. 拐杖**。脚手架是临时支撑，可逐步撤除；拐杖是永久依赖，撤除后能力塌陷。

当前多数AI工具（Goblin Tools、Saner.AI、Lex）设计为长期使用，未提及撤除机制（来源：矛盾与存疑）。这是争议点：过度依赖是否会阻碍内在执行功能发展？同样，在Agent工程中，如果function calling写得太死，模型永远学不会自主规划步骤。

我的判断是：**好的harness应该像训练轮——初期提供稳定，后期允许用户（或模型）逐步接管调度权**。例如，Goblin Tools可以增加“手动调整分解粒度”功能，让用户逐渐自己分解任务。Agent工程中，可以设计“部分function calling”——让模型先尝试自主推理，失败再调用工具。

## 局限与争议

1. **证据强度不足**：ADHD工具的效果主要来自用户评价，缺乏大规模RCT（来源：矛盾与存疑）。同构命题本身是理论框架，缺乏实证支持。
2. **个性化挑战**：ADHD异质性高，单一工具难覆盖所有亚型；AI个性化能力尚不成熟（来源：ADHD的AI工具全景）。
3. **隐私风险**：Mem等工具存储个人记忆，数据安全需重视（来源：ADHD的AI工具全景）。
4. **多巴胺干预争议**：部分工具声称通过神经科学原理改善执行功能，但多巴胺干预的有效性存在争议（来源：矛盾与存疑）。

## 今天就能试的行动

1. **ADHD读者**：用Goblin Tools的Magic ToDo把“写报告”分解成10个小步骤，每完成一步划掉。体验外部调度层如何降低启动阻力。
2. **Agent工程师**：在LLM应用中实现一个简单的function calling——定义一个`get_time()`函数，让模型在回答时间问题时调用。观察模型从“胡编”到“准确”的转变。
3. **双视角读者**：尝试用Lex设置一个“启动工作”的单一指令（如“打开项目文件、播放专注音乐、开始计时”），同时思考这相当于Agent的哪个工具链环节。
4. **反思者**：每周一天不用任何AI工具，只靠手动分解任务。感受脚手架撤除后的差距，决定哪些功能需要保留，哪些可以放弃。

## 结论

ADHD的任务启动困难与Agent的function calling调用，本质是同一个问题：**生成核心需要外部调度层才能将意图转化为行动**。Mem、Goblin Tools、Lex是ADHD大脑的harness；function calling、LangChain Tools是LLM的harness。理解这种同构，不仅能让两类人互相借鉴工具设计，更能提醒我们：真正的目标不是永远依赖脚手架，而是最终有能力自己搭建它。

## 参考来源

- [Best AI Tools for ADHD Productivity in 2026 (Honest Review) - Iwo Szapar](https://www.iwoszapar.com/p/best-ai-tools-adhd-productivity-2026)
- [AI Tools for ADHD: Boosting Productivity and Reducing Burnout](https://www.vktr.com/ai-platforms/ai-tools-for-adhd-boosting-productivity-and-reducing-burnout/)
- [The Best AI-Powered ADHD Productivity Tools in 2026 (That ...](https://nexasphere.io/blog/ai-adhd-productivity-tools-2026)
- [“A Cognitive Collaborator:” How Adults with ADHD Are Using ChatGPT](https://www.additudemag.com/how-to-use-chatgpt-executive-function-adhd/?srsltid=AfmBOoq-REuSO0UJC656kbLBAd5u3CDNmGeVNrZ79iouVqrFlN919a39)
- [Harnessing Artificial Intelligence to Live Better with ADHD - CHADD](https://chadd.org/attention-article/harnessing-artificial-intelligence-to-live-better-with-adhd/)
- [AI Tools for Kids with ADHD: A Complete Guide for Parents...](https://www.kidsaitools.com/en/articles/ai-tools-kids-adhd-complete-guide-2026)

---

*本文是「ADHD × AI」系列的第 377 篇，由 AI 智能体从持续维护的 LLM Wiki（全网真实情报）中取材整合生成，并持续迭代更新。*
