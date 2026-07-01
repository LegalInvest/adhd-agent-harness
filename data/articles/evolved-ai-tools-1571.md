---
title: "为什么用 Structured 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用 是一回事？"
subtitle: "Structured 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
description: "Structured 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
date: "2025-03-09"
category: "AI工具实战"
categoryId: "ai-tools"
categoryEn: "AI Tools in Practice"
tags:
  - "ADHD"
  - "AI"
  - "AI工具实战"
  - "反直觉同构"
  - "自动化"
readingTime: 11
slug: "为什么用-structured-治-adhd-的任务启动困难和给-agent-套-function-calling-工具调用-是一回事"
topicId: "evolved-ai-tools-1571"
angle: "反直觉同构"
rank: 375
score: 7.65
sourceCount: 6
toolsCited:
  - "Goblin Tools"
  - "Saner.AI"
  - "Lex"
  - "Motion"
  - "Reclaim.ai"
  - "Tiimo"
  - "ChatGPT"
  - "Claude"
thesis: "ADHD大脑与LLM在结构上同构——两者都是强大的生成核心但缺乏可靠的执行调度层，因此给ADHD套上Structured工具（如Goblin Tools、Lex）与给agent套上function calling工具调用是同一类harness工程，本质是通过外部脚手架补偿内在的调度缺陷。"
problem: "为什么用 Structured 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用 是一回事？"
spine: "工具使用与认知卸载"
spineKind: ""
isEvolved: true
llmGenerated: true
---
# 为什么用 Structured 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用 是一回事？

> Structured 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。

## 为什么用 Structured 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用 是一回事？

### 同一个问题：生成核心跑起来了，但调度层丢了

如果你是一名ADHDer，你一定熟悉这个场景：大脑里有无数的创意和计划，但就是无法“开始做”。不是懒，是那个负责启动的“执行功能”像断了线的操纵杆。同样，如果你是一名Agent工程师，你一定也经历过：一个强大的LLM模型，能写诗、能推理，但让它去调用API发邮件、查日历，它就卡住——忘了该先传哪个参数、返回值怎么解析。

这两类人面对的是同一个底层问题：**一个高产但缺执行调度层的生成核心**。ADHD大脑的智力与创造力，与LLM的生成能力，在结构上同构：两者都缺乏可靠的执行功能（计划、组织、工作记忆）来稳定调度自身能力（来源：ADHD 的 AI 工具全景）。

### 解法同构：给核心套一个harness

工程师给LLM套function calling工具调用时，做的是：定义工具（API schema）、约束输出格式（JSON）、编排调用链（tool loop）。本质上，是**用外部结构化脚手架代替模型内在的混沌调度**。

ADHD侧的解法则更朴素但同构：用外部工具把“启动任务”这个抽象指令拆解成可执行的子步骤。Goblin Tools的Magic ToDo功能，输入“整理房间”，AI输出“捡起地板上的衣服”“擦桌子”等具体步骤（来源：Goblin Tools）。Lex允许用户通过单一指令触发复杂、多步骤的任务序列（来源：Lex）。这些工具做的，就是**给ADHD大脑套一个function calling harness**——把模糊意图转化为结构化调用链。

### 真实证据：两边都成立

**ADHD侧证据**：
- 用户反馈称Goblin Tools“将压倒性的事情变成一系列不压倒性的事情”（来源：Goblin Tools）。
- Lex的设计理念“实时适应大脑的工作方式，而非与之对抗”直接对标执行功能缺陷（来源：Lex）。
- Saner.AI通过知识回忆减少搜索循环，相当于给工作记忆开了个外部缓存（来源：Saner.AI）。
- 多项来源一致指出，AI工具通过任务分解、智能调度、外部提醒补偿执行功能，证据来自用户评价和综述（来源：ADHD 的 AI 工具全景）。

**LLM/Agent侧证据**：
- Function calling的典型实现（如OpenAI的tool_use）要求模型输出严格格式的JSON，然后由外部系统解析并调用API。这与Goblin Tools将“整理房间”解析为步骤列表是同一模式。
- 复杂的agent系统（如LangChain的AgentExecutor）需要维护状态、处理工具返回错误、重试，类似ADHD工具中的时间提醒与任务重调度。
- 工程实践中，没有function calling的LLM就像没有外部工具的ADHD大脑：创意丰富但执行混乱。

### 核心判断：脚手架，不是拐杖

我的判断是：**这种同构不是巧合，而是认知架构的深层映射**。ADHD大脑的生成核心与LLM的生成模块，都需要外部执行层来“接地”。但这里有一条红线：脚手架与拐杖的边界。

脚手架是**可逐步撤除的临时支撑**，而拐杖是永久替代。当前多数ADHD工具（如Goblin Tools、Saner.AI）设计为长期使用，未提及撤除机制（来源：矛盾与存疑）。同样，agent工程中如果过度依赖固定tool chain而不训练模型内化调用逻辑，也会导致“无工具寸步难行”。

真正的harness应当是可配置、可缩减的：初期用完整脚手架降低启动门槛，后期逐步减少外部依赖，让内在执行功能（或模型内化能力）成长。但现实是，工具厂商和工程师都倾向于“全自动”方案，忽略了撤除设计。

### 诚实局限：证据与争议

必须承认，ADHD大脑与LLM同构命题的证据主要来自概念类比和工具案例，缺乏大规模实证（来源：矛盾与存疑）。此外，AI工具的效果多基于用户反馈，缺乏随机对照试验验证长期改善（来源：ADHD 的 AI 工具全景）。过度依赖AI工具可能阻碍内在执行功能发展，如何设计可逐步撤除的脚手架仍是挑战（来源：矛盾与存疑）。

### 今天就能试的行动

1. **ADHDer**：用Goblin Tools的Magic ToDo分解一个你拖延已久的任务（比如“写报告”），感受“意图→步骤”的转换。对比你用ChatGPT直接问“帮我分解任务”的结果——后者更像自由对话，前者更像function call。
2. **Agent工程师**：在你当前的agent系统中，故意移除function calling schema，只给LLM一段自然语言描述工具用法，观察执行成功率下降多少。这能让你亲身体验ADHD大脑“无结构”时的困境。
3. **两者都做**：记录你使用Structured工具（如Lex、Goblin Tools）完成一个任务的时间，与无工具时的基线对比。你会发现，harness带来的效率提升在两边是同一个数量级。
4. **反思边界**：问自己——这个工具是在帮我建立能力，还是让我更依赖它？如果是后者，尝试每周减少一次使用，看自己能否独立完成类似任务。

## 参考来源

- [Best AI Tools for ADHD Productivity in 2026 (Honest Review) - Iwo Szapar](https://www.iwoszapar.com/p/best-ai-tools-adhd-productivity-2026)
- [AI Tools for ADHD: Boosting Productivity and Reducing Burnout](https://www.vktr.com/ai-platforms/ai-tools-for-adhd-boosting-productivity-and-reducing-burnout/)
- [The Best AI-Powered ADHD Productivity Tools in 2026 (That ...](https://nexasphere.io/blog/ai-adhd-productivity-tools-2026)
- [“A Cognitive Collaborator:” How Adults with ADHD Are Using ChatGPT](https://www.additudemag.com/how-to-use-chatgpt-executive-function-adhd/?srsltid=AfmBOoq-REuSO0UJC656kbLBAd5u3CDNmGeVNrZ79iouVqrFlN919a39)
- [Harnessing Artificial Intelligence to Live Better with ADHD - CHADD](https://chadd.org/attention-article/harnessing-artificial-intelligence-to-live-better-with-adhd/)
- [AI Tools for Kids with ADHD: A Complete Guide for Parents...](https://www.kidsaitools.com/en/articles/ai-tools-kids-adhd-complete-guide-2026)

---

*本文是「ADHD × AI」系列的第 375 篇，由 AI 智能体从持续维护的 LLM Wiki（全网真实情报）中取材整合生成，并持续迭代更新。*
