---
title: "为什么用 Lex 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用 是一回事？"
subtitle: "Lex 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
description: "Lex 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
date: "2025-03-12"
category: "AI工具实战"
categoryId: "ai-tools"
categoryEn: "AI Tools in Practice"
tags:
  - "ADHD"
  - "AI"
  - "AI工具实战"
  - "反直觉同构"
  - "效率工具"
readingTime: 10
slug: "为什么用-lex-治-adhd-的任务启动困难和给-agent-套-function-calling-工具调用-是一回事"
topicId: "evolved-ai-tools-1572"
angle: "反直觉同构"
rank: 376
score: 7.65
sourceCount: 6
toolsCited:
  - "Lex"
  - "Goblin Tools"
  - "Saner.AI"
  - "Focusmate"
  - "Motion"
  - "Reclaim.ai"
thesis: "ADHD 的任务启动困难与 LLM/Agent 的 function calling 是同一结构问题：两者都是强大的生成核心缺乏可靠的执行调度层，而 Lex 和 function calling 本质上都是通过外部工具（harness）来提供执行功能，实现认知卸载。"
problem: "为什么用 Lex 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用 是一回事？"
spine: "工具使用与认知卸载"
spineKind: ""
isEvolved: true
llmGenerated: true
---
# 为什么用 Lex 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用 是一回事？

> Lex 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。

## 问题：为什么启动一件事这么难？

如果你是 ADHD 患者，你一定经历过这种场景：脑子里有一个清晰的计划——比如“整理房间”或“写一份报告”——但身体就是动不了。你明明知道要做什么，却像被钉在椅子上，手指悬在键盘上方，大脑一片空白。这种“任务启动困难”是 ADHD 最令人沮丧的症状之一，它源于执行功能缺陷：工作记忆容量有限、时间盲、多巴胺调节异常，导致大脑无法将意图转化为行动（来源：AI Tools for ADHD: Boosting Productivity and Reducing Burnout）。

如果你是 Agent 工程师，你肯定也遇到过类似场景：你精心设计了一个 LLM agent，给它丰富的知识库和强大的生成能力，但它在执行多步骤任务时频频卡壳——要么忘记上一步的结果，要么在函数调用时选错工具，要么干脆陷入死循环。你发现，模型本身很聪明，但缺少一个可靠的“执行调度层”来管理步骤、状态和工具调用。

这两个问题，听起来风马牛不相及。但本文要论证的是：**它们本质上是同一个问题**——ADHD 大脑与 LLM 在结构上同构，都是强大的生成核心缺乏可靠的执行调度层。而 Lex 这类 AI 工具与 Agent 的 function calling 机制，正是同一套解决方案：通过外部工具（harness）提供执行功能，实现认知卸载。

## 同构：生成核心 vs 执行调度层

ADHD 大脑的典型特征是高创造力、跳跃性思维，但执行功能（计划、组织、工作记忆）薄弱。这就像一个顶级生成器，却缺少一个稳定的调度系统来把生成的内容按顺序执行。LLM 也是如此：它能生成流畅的文本、推理复杂问题，但一旦需要多步操作（比如“先查数据库，再调用 API，最后汇总结果”），就会迷失在步骤中，忘记上下文或选错工具。

这正是“ADHD 大脑与 LLM 同构”命题的核心：**两者都是高产但缺执行调度层的生成核心**（来源：ADHD 的 AI 工具全景）。对于 ADHD，这个调度层是前额叶的执行功能；对于 LLM，它是 Agent 的编排层（如 function calling 框架）。当内在调度不足时，外部工具可以充当“脚手架”。

## 解法：Lex 与 function calling 是一回事

Lex 是一款 AI 生产力工具，核心功能是“通过单一指令触发复杂、多步骤的任务序列”（来源：Lex）。例如，你输入“准备下周的会议”，Lex 会自动分解为“查日历→找资料→写议程→发邀请”等步骤，并逐一执行。这直接解决了 ADHD 的任务启动困难：用户只需做一次决策（输入指令），后续的分解和执行由工具接管，降低了启动门槛和认知负荷（来源：Best AI Tools for ADHD Productivity in 2026）。

在 Agent 工程中，function calling 做的是同样的事。工程师定义一系列工具（函数），LLM 根据用户意图选择并调用它们，按顺序执行多步操作。例如，用户说“帮我订一张明天飞北京的机票”，Agent 会分解为“查航班→比较价格→预订→发确认”等步骤，通过调用不同的 API 完成。这个过程与 Lex 的“单一指令触发多步骤”完全一致：**都是将复杂意图自动分解为可执行的子任务序列，由外部系统管理执行顺序和状态**。

证据在于，ADHD 工具如 Goblin Tools 也采用类似思路：它的 Magic ToDo 功能将“整理房间”分解为“捡起衣服→擦桌子→扫地”等小步骤，降低启动焦虑（来源：Goblin Tools）。而 Agent 的 function calling 同样需要任务分解——只是面向的是机器而非人类。两者共享同一核心机制：**通过外部工具提供步骤管理，弥补内在调度缺陷**。

## 脚手架 vs 拐杖：边界在哪里？

这里必须诚实指出争议。虽然 Lex 和 function calling 都能有效补偿执行功能，但长期使用存在“拐杖化”风险。ADHD 的 AI 工具全景中明确指出，过度依赖 AI 工具可能阻碍内在执行功能的发展，如何设计可逐步撤除的“脚手架”仍是挑战（来源：ADHD 的 AI 工具全景）。同样，Agent 工程中，如果 function calling 框架过于僵化，模型可能丧失自主规划能力，变成只会按脚本执行的“提线木偶”。

边界在于：**脚手架是辅助学习，拐杖是替代能力**。一个好的脚手架应该让用户（或模型）逐渐内化执行步骤，最终减少对外部工具的依赖。但目前多数工具（包括 Lex、Goblin Tools）设计为长期使用，未提及撤除机制（来源：矛盾与存疑）。这提醒我们，在使用这些工具时，要有意识地训练自己的执行功能，而不是完全交给 AI。

## 今天就能试的行动

1. **用 Lex 启动一个卡了很久的任务**：比如写一封复杂的邮件或整理项目计划。只输入一句话指令，让 Lex 分解并执行，体验“一次决策”带来的启动流畅感。
2. **用 Goblin Tools 的 Magic ToDo 分解一个日常任务**：输入“打扫厨房”，观察 AI 如何将压倒性任务变成可管理的小步骤。这能让你直观感受“任务分解”对启动困难的缓解。
3. **尝试用 Focusmate 进行“身体加倍”**：即使没有 AI 工具，找一个朋友视频连线，各自工作。身体在场效应被证明是 ADHD 最有效的策略之一（来源：身体在场效应），它也是一种外部执行功能层——通过社会存在感提供隐性问责。
4. **如果你是工程师，为你的 Agent 写一个简单的 function calling 框架**：定义 2-3 个工具（如“搜索”“计算”“保存”），让 LLM 通过自然语言调用它们完成多步任务。你会立刻发现，这和帮助 ADHD 朋友启动任务用的是同一套逻辑。

## 局限与展望

本文的核心论点——ADHD 与 LLM 同构——目前主要基于概念类比和工具案例，缺乏大规模实证研究（来源：矛盾与存疑）。此外，ADHD 的异质性很高，Lex 对某些人可能无效，而 function calling 框架也需要根据具体场景定制。但即便如此，这种“同构视角”提供了一个强大的设计原则：**无论是帮助人类还是帮助模型，解决执行调度问题的核心思路都是外部 harness**。未来，随着 AI 个性化能力的提升，我们或许能设计出真正可撤除的脚手架，让 ADHD 患者和 Agent 都能逐步内化执行功能，最终摆脱外部依赖。

## 参考来源

- [Best AI Tools for ADHD Productivity in 2026 (Honest Review) - Iwo Szapar](https://www.iwoszapar.com/p/best-ai-tools-adhd-productivity-2026)
- [AI Tools for ADHD: Boosting Productivity and Reducing Burnout](https://www.vktr.com/ai-platforms/ai-tools-for-adhd-boosting-productivity-and-reducing-burnout/)
- [The Best AI-Powered ADHD Productivity Tools in 2026 (That ...](https://nexasphere.io/blog/ai-adhd-productivity-tools-2026)
- [“A Cognitive Collaborator:” How Adults with ADHD Are Using ChatGPT](https://www.additudemag.com/how-to-use-chatgpt-executive-function-adhd/?srsltid=AfmBOoq-REuSO0UJC656kbLBAd5u3CDNmGeVNrZ79iouVqrFlN919a39)
- [Harnessing Artificial Intelligence to Live Better with ADHD - CHADD](https://chadd.org/attention-article/harnessing-artificial-intelligence-to-live-better-with-adhd/)
- [AI Tools for Kids with ADHD: A Complete Guide for Parents...](https://www.kidsaitools.com/en/articles/ai-tools-kids-adhd-complete-guide-2026)

---

*本文是「ADHD × AI」系列的第 376 篇，由 AI 智能体从持续维护的 LLM Wiki（全网真实情报）中取材整合生成，并持续迭代更新。*
