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
  - "ChatGPT"
thesis: "ADHD 大脑与 LLM 在结构上同构——两者都是高产但缺乏执行调度层的生成核心，因此解决 ADHD 任务启动困难的工具（如 Routinery）与给 agent 套 function calling 工具调用，本质上是同一套 harness 思路：通过外部脚手架提供执行功能，补偿内在调度缺陷。"
problem: "为什么用 Routinery 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用 是一回事？"
spine: "工具使用与认知卸载"
spineKind: ""
isEvolved: true
llmGenerated: true
---
# 为什么用 Routinery 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用 是一回事？

> Routinery 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。

## 问题：为什么「启动」这么难？

如果你有 ADHD，你一定熟悉这个场景：坐在书桌前，任务清单摆在眼前，大脑却像死机一样，光标闪烁，手指不动。你明明知道该做什么，但「开始」这个动作仿佛需要翻越一座山。这不是懒，而是执行功能——尤其是任务启动——出了故障。ADHD 大脑的核心特征是「高产但无序的生成能力，同时缺乏可靠的执行调度层」（来源：ADHD 大脑与 LLM 的同构）。想法很多，行动困难。

同样的问题，在 AI 工程领域以另一种形式出现：你有一个强大的 LLM（比如 GPT-4），它能写诗、能编程、能推理，但如果你直接问它「帮我发一封邮件」，它只会生成邮件文本，而不会真的调用邮件 API 发送出去。LLM 本身「缺乏可靠的内置调度与执行控制」（来源：ADHD 大脑与 LLM 的同构）。它需要一个「agent harness」——也就是 function calling 工具调用——来把「发邮件」这个意图转化为实际的 API 调用。

这两个问题看似风马牛不相及，但如果你把 ADHD 大脑和 LLM 放在一起看，会发现一个惊人的同构：**两者都是强大的生成核心，但都缺一个执行调度层**。ADHD 大脑需要外部工具来「减少决策、保留上下文、让下一步行动显而易见」（来源：ADHD 大脑与 LLM 的同构）；LLM 需要 harness 来提供上下文管理、工具接口和编排能力（来源：外部执行功能层）。而解决这两个问题的方案，本质上是同一套思路——给生成核心套上脚手架。

## 同构：Routinery 与 function calling 是同一件事

Routinery 是一款专为 ADHD 设计的日常流程应用，它的核心功能是：你把一个复杂任务（比如「早上起床后的流程」）分解成一系列小步骤，然后 Routinery 会一步步引导你执行，每一步都有计时和提醒。这听起来很简单，但它的设计原理与 LLM 的 function calling 如出一辙。

在 LLM 侧，function calling 的工作方式是：你定义一组工具（比如「发送邮件」「查询天气」），LLM 根据用户意图决定调用哪个工具，然后 harness 负责实际执行。这相当于把「意图」转化为「可执行的步骤序列」。在 ADHD 侧，Routinery 做的也是同样的事：你把「完成工作项目」这个模糊意图，分解成「打开文档」「列出大纲」「写第一段」等具体步骤，然后由应用一步步引导你执行。**Routinery 就是 ADHD 大脑的 harness**。

这个类比不是空洞的比喻，而是有真实证据支撑的。在 ADHD 侧，Goblin Tools 的 Magic ToDo 功能「能自动将任何任务分解为更小、更易管理的步骤」（来源：Goblin Tools），用户反馈它「将压倒性的事情变成一系列不压倒性的事情」（来源：Goblin Tools）。Lex 则更进一步，允许用户「通过单一指令触发复杂、多步骤的任务序列」（来源：Lex），这简直是 function calling 的 ADHD 版——你输入一个意图，工具自动编排执行。在 LLM 侧，harness 工程被定义为「设计围绕 AI 代理的脚手架——上下文交付、工具接口、规划工件、验证循环、记忆系统和沙箱」（来源：外部执行功能层）。这些概念在 ADHD 工具中一一对应：Goblin Tools 提供任务分解（规划工件），Saner.AI 提供知识回忆（记忆系统），Lex 提供单指令触发（工具接口）。

## 脚手架 vs 拐杖：同构的边界

然而，这个同构有一个关键边界：**脚手架应该是可撤除的，而拐杖则让人依赖**。在 LLM 工程中，harness 是基础设施，你永远不会撤除它——LLM 永远需要外部工具来执行实际动作。但在 ADHD 侧，工具的使用存在争议：过度依赖 AI 工具可能「阻碍内在执行功能发展」（来源：矛盾与存疑）。一个 ADHD 用户如果永远靠 Goblin Tools 分解任务，可能永远不会学会自己分解。这就是「脚手架 vs 拐杖」的困境。

我的判断是：**对于 ADHD，工具应该像 LLM 的 harness 一样，是永久性的外部模块，而非临时训练轮**。因为 ADHD 的执行功能缺陷是神经性的，不是技能问题——你无法通过练习「治愈」工作记忆不足，就像你无法通过练习让 LLM 学会自己调用 API。但关键在于，工具的设计应该「逐步撤除」吗？目前多数工具（如 Goblin Tools、Saner.AI）设计为长期使用，未提及撤除机制（来源：矛盾与存疑）。这未必是坏事——就像眼镜不需要撤除一样，一个永久性的外部执行功能层可能是更现实的解决方案。但用户需要警惕的是：工具是否在替代你的思考，而非辅助你的行动？例如，如果 Routinery 帮你分解任务后，你连「下一步做什么」都不再思考，那它就变成了拐杖。

## 今天就能试的 3 件事

1. **用 ChatGPT 模拟 Routinery**：下次遇到启动困难的任务，对 ChatGPT 说：「我很难开始写报告，请帮我分解成 5 个可执行的小步骤，每一步用一句话描述，并告诉我第一步具体做什么。」这本质上是手动调用 function calling——你充当了 harness 的角色。

2. **安装 Goblin Tools 并测试 Magic ToDo**：输入一个你拖延已久的任务（比如「整理房间」），观察 AI 如何分解。然后只做第一步。这直接对应 LLM 的「工具调用」——你给了意图，工具返回步骤序列。

3. **反思你的工具使用**：问自己——这个工具是在帮我「执行」还是「思考」？如果它帮你做了所有决策，你只是被动跟随，那它就是拐杖。调整使用方式，让工具只负责「执行调度」，而保留「意图生成」给自己。

## 局限与争议

必须诚实指出，这个同构命题「证据主要来自概念类比和工具案例，缺乏大规模实证」（来源：矛盾与存疑）。目前没有随机对照试验证明 Routinery 或 function calling 的类比能改善 ADHD 核心症状。此外，ADHD 的异质性很高——「单一工具难以覆盖所有亚型」（来源：ADHD 的 AI 工具全景）。对于某些人，Routinery 可能无效，而 function calling 的类比也不适用于所有 LLM 场景。但作为一种思维模型，它提供了一个清晰的工程视角：**ADHD 不是缺陷，而是缺乏 harness 的生成核心**。而你的任务，就是为自己设计那个脚手架。

## 参考来源

- [Best AI Tools for ADHD Productivity in 2026 (Honest Review) - Iwo Szapar](https://www.iwoszapar.com/p/best-ai-tools-adhd-productivity-2026)
- [AI Tools for ADHD: Boosting Productivity and Reducing Burnout](https://www.vktr.com/ai-platforms/ai-tools-for-adhd-boosting-productivity-and-reducing-burnout/)
- [The Best AI-Powered ADHD Productivity Tools in 2026 (That ...](https://nexasphere.io/blog/ai-adhd-productivity-tools-2026)
- [“A Cognitive Collaborator:” How Adults with ADHD Are Using ChatGPT](https://www.additudemag.com/how-to-use-chatgpt-executive-function-adhd/?srsltid=AfmBOoq-REuSO0UJC656kbLBAd5u3CDNmGeVNrZ79iouVqrFlN919a39)
- [Harnessing Artificial Intelligence to Live Better with ADHD - CHADD](https://chadd.org/attention-article/harnessing-artificial-intelligence-to-live-better-with-adhd/)
- [AI Tools for Kids with ADHD: A Complete Guide for Parents...](https://www.kidsaitools.com/en/articles/ai-tools-kids-adhd-complete-guide-2026)

---

*本文是「ADHD × AI」系列的第 380 篇，由 AI 智能体从持续维护的 LLM Wiki（全网真实情报）中取材整合生成，并持续迭代更新。*
