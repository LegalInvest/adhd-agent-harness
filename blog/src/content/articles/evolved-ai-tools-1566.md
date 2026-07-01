---
title: "为什么用 Motion 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用 是一回事？"
subtitle: "Motion 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
description: "Motion 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
date: "2025-05-14"
category: "AI工具实战"
categoryId: "ai-tools"
categoryEn: "AI Tools in Practice"
tags:
  - "ADHD"
  - "AI"
  - "AI工具实战"
  - "反直觉同构"
  - "智能助手"
readingTime: 11
slug: "为什么用-motion-治-adhd-的任务启动困难和给-agent-套-function-calling-工具调用-是一回事"
topicId: "evolved-ai-tools-1566"
angle: "反直觉同构"
rank: 182
score: 7.72
sourceCount: 6
toolsCited:
  - "Motion"
  - "Goblin Tools"
  - "Lex"
  - "Saner.AI"
  - "Otter.ai"
  - "Mem"
  - "Claude"
  - "ChatGPT"
thesis: "ADHD 的任务启动困难与 LLM agent 的 function calling 工具调用共享同一本质——两者都是“高产但缺执行调度层的生成核心”需要外部 harness 来补偿，而 Motion 这类自适应规划工具正是这一同构思想的双向实证。"
problem: "为什么用 Motion 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用 是一回事？"
spine: "工具使用与认知卸载"
spineKind: ""
isEvolved: true
llmGenerated: true
---
# 为什么用 Motion 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用 是一回事？

> Motion 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。

## 问题：为什么我的大脑像一台没有操作系统的超级计算机？

你打开 Motion，看着它自动把“写报告”拆成“收集资料→列大纲→写初稿→修改”，然后排进日历。你松了口气，任务终于启动了。

但你知道吗？LLM agent 工程师也在做几乎一模一样的事——他们给大模型套上 function calling 工具调用，让模型能调用 API、查询数据库、执行代码。没有这个 harness，模型再聪明也只是一个“会说话但不会干活”的聊天框。

为什么两个看似无关的场景，解法如此相似？

因为 ADHD 大脑和 LLM agent 共享同一个底层困境：**两者都是“高产但缺执行调度层的生成核心”**。ADHD 大脑能产生无数创意，却卡在“开始做”这一步；LLM 能生成流畅文本，却无法自主完成多步操作。两边的解决方案——自适应规划工具（如 Motion）和 function calling harness——在结构上完全同构：**都是通过外部执行功能层（harness/脚手架）来补偿内在的调度缺陷。**

## 同构一：任务启动困难 vs 冷启动问题

ADHD 侧最典型的痛点是任务启动困难。面对一个模糊的大任务（比如“整理房间”），大脑像被冻住一样，无法拆解为可执行的步骤。Goblin Tools 的 Magic ToDo 功能自动将“整理房间”分解为“捡起地板上的衣服”“擦桌子”等小步骤，用户反馈称“启动焦虑降低”（来源：Goblin Tools 页面）。Lex 更进一步，允许用单一指令触发多步骤序列，减少决策疲劳（来源：Lex 页面）。Motion 则通过自适应调度，在日程被打乱时自动重排，解决“计划赶不上变化”的崩溃（来源：规划循环与任务分解页面）。

LLM/agent 侧对应的是“冷启动”问题：模型在没有任何上下文或工具时，无法执行具体操作。Function calling 工具调用相当于给模型一个“启动脚本”——定义好可用的函数（如 `search_web`、`send_email`），模型只需选择调用哪个函数、传什么参数。这与 Goblin Tools 的任务分解异曲同工：**把“做什么”的决策从生成核心转移到外部 harness，降低启动门槛。**

## 同构二：目标漂移 vs 指令消退

ADHD 大脑在执行任务时极易被无关刺激捕获，导致目标漂移。外部工具通过提醒和通知提供重锚定，例如 AI 工具“提供提醒和通知以保持正轨”（来源：重锚定与目标漂移页面）。Otter.ai 的实时转录和 Reflect 的结构化提问，相当于虚拟的“身体在场效应”，帮助用户持续聚焦。

LLM agent 在长程任务中同样会“忘记系统提示”，行为逐渐偏离初始指令（来源：重锚定与目标漂移页面）。Harness 通过事件驱动的系统提醒（如每轮交互后注入当前目标）来对抗这种“指令消退”。这与 ADHD 工具的重锚定机制完全同构：**都是外部系统定期注入“当前目标”信号，防止生成核心漂移。**

## 同构三：时间盲 vs 时序推理弱点

ADHD 的时间感知缺陷（时间盲）导致无法准确估计任务时长和截止时间。自适应规划工具如 Motion 和 Tiimo 通过动态调整日程来应对：“Adaptive planners like Motion and Tiimo go further, reshuffling the day when it collapses.”（来源：规划循环与任务分解页面）

LLM 的时序推理弱点同样明显——模型难以自主规划多步操作的顺序和时间分配。Function calling harness 通过定义函数调用的先后依赖关系（如先搜索再总结），以及设置超时限制，来补偿这一缺陷。**两者都是通过外部系统管理时间维度，让生成核心无需操心“什么时候做什么”。**

## 脚手架 vs 拐杖：关键边界

看到这里，你可能会问：既然工具这么好用，会不会让我变得更依赖、更不会自己启动任务？

这正是“脚手架 vs 拐杖”的辩证关系（来源：ADHD 的 AI 工具全景页面）。AI 工具应作为脚手架促进能力发展，而非永久拐杖。例如，Otter.ai 减轻笔记负担，但过度依赖可能削弱主动记笔记的能力（来源：ADHD 的 AI 工具全景页面）。同样，给 LLM 套 function calling 是必要的脚手架，但如果模型永远依赖外部调度，就无法进化出内在的规划能力。

**我的判断是：** 对于 ADHD 用户，自适应规划工具（如 Motion）在初期可以作为“拐杖”快速启动，但长期应逐步过渡到“脚手架”——例如，先让 AI 分解任务，然后尝试自己分解，最后只在卡住时求助。对于 LLM agent，function calling 是必需的底层能力，但未来的方向是让模型学会在缺少工具时自主生成调用逻辑，而非死板依赖预定义函数。

## 局限与争议

必须诚实指出，当前证据主要来自用户报告和概念类比，缺乏大规模对照实验（来源：矛盾与存疑页面）。Motion 等工具的效果因人而异，部分用户可能发现其分解步骤不够精准（来源：Goblin Tools 页面）。此外，过度依赖 AI 工具可能削弱内在能力，但现有工具设计缺乏如何避免依赖的具体指导（来源：矛盾与存疑页面）。对于 LLM agent，function calling 虽然有效，但模型仍可能因上下文膨胀而忽略工具调用，需要持续优化 harness 设计。

## 今天就能试的行动

1. **ADHD 用户：** 下载 Motion 或 Goblin Tools，将一个你拖延了一周的大任务（比如“写周报”）输入进去，观察 AI 如何分解。然后只做第一步——通常这一步小到不会让你抗拒。
2. **工程师：** 如果你在用 LLM 做 agent，手动将系统提示中“你可以调用以下函数”的部分改为动态注入，每轮交互后重新注入当前目标，观察任务完成率是否提升。
3. **双向启发：** 如果你是 ADHD 用户且懂技术，尝试用 AI 工具（如 ChatGPT 或 Claude）创建一个自定义 GPT，定义好“任务启动助手”的函数（如 `break_down_task`、`set_reminder`），然后对 AI 说“帮我启动‘整理桌面’”——你会发现自己既是用户也是工程师。
4. **反思：** 每周选一天，不用任何 AI 规划工具，自己手动分解一个任务。记录下哪里卡住了，下次再用 AI 工具对比——这能帮你找到“脚手架”与“拐杖”的边界。

Motion 和 function calling 看似分属两个世界，但它们的本质都是同一个问题的两种解法：**当我们的大脑或模型像一台没有操作系统的超级计算机时，外部 harness 就是那个让一切跑起来的调度层。** 理解这一点，你就能同时用好工具，也设计好工具。

## 参考来源

- [Best AI Tools for ADHD Productivity in 2026 (Honest Review) - Iwo Szapar](https://www.iwoszapar.com/p/best-ai-tools-adhd-productivity-2026)
- [AI Tools for ADHD: Boosting Productivity and Reducing Burnout](https://www.vktr.com/ai-platforms/ai-tools-for-adhd-boosting-productivity-and-reducing-burnout/)
- [The Best AI-Powered ADHD Productivity Tools in 2026 (That ...](https://nexasphere.io/blog/ai-adhd-productivity-tools-2026)
- [“A Cognitive Collaborator:” How Adults with ADHD Are Using ChatGPT](https://www.additudemag.com/how-to-use-chatgpt-executive-function-adhd/?srsltid=AfmBOoq-REuSO0UJC656kbLBAd5u3CDNmGeVNrZ79iouVqrFlN919a39)
- [Harnessing Artificial Intelligence to Live Better with ADHD - CHADD](https://chadd.org/attention-article/harnessing-artificial-intelligence-to-live-better-with-adhd/)
- [AI Tools for Kids with ADHD: A Complete Guide for Parents...](https://www.kidsaitools.com/en/articles/ai-tools-kids-adhd-complete-guide-2026)

---

*本文是「ADHD × AI」系列的第 182 篇，由 AI 智能体从持续维护的 LLM Wiki（全网真实情报）中取材整合生成，并持续迭代更新。*
