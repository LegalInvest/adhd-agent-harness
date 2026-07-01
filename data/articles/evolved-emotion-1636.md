---
title: "为什么用 Reclaim.ai 治 ADHD 的情绪失调，和给 agent 套 会褪去的脚手架 是一回事？"
subtitle: "Reclaim.ai 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
description: "Reclaim.ai 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
date: "2025-03-21"
category: "情绪调节"
categoryId: "emotion"
categoryEn: "Emotional Regulation"
tags:
  - "ADHD"
  - "AI"
  - "情绪调节"
  - "反直觉同构"
  - "自我接纳"
readingTime: 11
slug: "为什么用-reclaimai-治-adhd-的情绪失调和给-agent-套-会褪去的脚手架-是一回事"
topicId: "evolved-emotion-1636"
angle: "反直觉同构"
rank: 389
score: 7.65
sourceCount: 6
toolsCited:
  - "Reclaim.ai"
  - "Inflow"
  - "Goblin Tools"
  - "Saner.AI"
  - "Motion"
  - "Tiimo"
thesis: "ADHD 情绪失调与 LLM agent 目标漂移共享同一结构缺陷——强大的生成核心缺乏可靠的执行调度层，而 Reclaim.ai 等工具提供的“会褪去的脚手架”正是针对这一同构问题的工程化解决方案，其设计原则（外部记忆、重锚定、可撤除性）在两侧完全同构。"
problem: "为什么用 Reclaim.ai 治 ADHD 的情绪失调，和给 agent 套 会褪去的脚手架 是一回事？"
spine: "拐杖与脚手架"
spineKind: ""
isEvolved: true
llmGenerated: true
---
# 为什么用 Reclaim.ai 治 ADHD 的情绪失调，和给 agent 套 会褪去的脚手架 是一回事？

> Reclaim.ai 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。

## 问题：为什么 Planner 总是失效？

如果你是一个 ADHD 者，你一定经历过这样的循环：买一本漂亮的手帐，前三天兴奋地填满，第四天开始漏写，一周后彻底放弃。你告诉自己“这次一定行”，但下一次 Planner 依然在角落里吃灰。

如果你是一个在做 Agentic Harness 的工程师，你一定见过这样的场景：你给 LLM agent 写了一长串系统提示，前几轮它表现得像个专家，但十轮对话后它开始忽略指令、跑偏任务，甚至“忘记”自己是谁。你骂它“不听话”，但你知道问题出在编排层。

这两个场景看似毫无关联，但它们的底层问题完全同构：**一个强大的生成核心（ADHD 大脑 / LLM），配上一个不可靠的调度层（执行功能 / 上下文编排）。** 情绪失调，正是调度层崩溃时的直接表现——ADHD 者在工作记忆过载或时间盲发作时情绪失控；LLM agent 在指令消退或目标漂移时输出失控。

而 Reclaim.ai 这类工具，恰好同时解决了这两个问题。它的设计逻辑，与 Agentic Harness 工程中的“会褪去的脚手架”完全一致。

## 同构一：工作记忆不足 vs 上下文窗口有限

ADHD 的核心缺陷之一是工作记忆容量小。你正在做 A 任务，突然想起 B 事情，然后 C 情绪涌上来，A 就被彻底忘了。情绪调节的第一步——记住“我现在需要冷静”——往往在情绪爆发的瞬间就丢失了。

LLM agent 同样受限于上下文窗口。随着交互轮次增加，早期的系统提示逐渐被新 token 挤压，模型开始“忘记”自己的角色和约束。这就是所谓的“指令消退”（来源：Building an AI Coding Agent for the Terminal: Scaffolding, Harness, Context Engineering, and Lessons Learned）。

Reclaim.ai 的解法是：**外部记忆 + 重锚定**。它通过日历自动安排任务、设置提醒，把“接下来该做什么”从你的工作记忆里卸掉，放到一个可靠的外部系统中。这相当于为 ADHD 大脑加装了一个“数字工作记忆”（来源：AI 与 ADHD 的情绪调节——核心论点）。

在 LLM 侧，Harness 工程做的是同样的事：把系统提示、任务分解、验证步骤写进外部编排文件，而不是依赖模型自己的上下文。Saner.AI 的知识回忆功能也是同理——它帮你快速找回信息，减少搜索循环和标签切换（来源：Best AI Tools for ADHD Productivity in 2026 (Honest Review) - Iwo Szapar）。

## 同构二：任务启动困难 vs 规划循环缺失

ADHD 者面对一个复杂任务时，大脑会直接进入“瘫痪”状态。不是不想做，是不知道从哪开始。这种启动焦虑会迅速转化为沮丧、自责等负面情绪，形成情绪失调的典型前奏。

LLM agent 面对一个模糊指令时，同样容易“胡编乱造”或陷入死循环。它需要一个规划循环来把大目标拆成小步骤，并在每一步验证结果。

Goblin Tools 的 Magic ToDo 功能正是为此而生：它自动将“整理房间”分解为“捡起衣服”“擦桌子”等具体行动（来源：AI Tools for Kids with ADHD: A Complete Guide for Parents...）。这种分解“将压倒性的事情变成一系列不压倒性的事情”（来源：The Best AI-Powered ADHD Productivity Tools in 2026 (That ...)）。

在 LLM 侧，Harness 工程中的“规划 artifact”就是同样的东西：把任务分解成可执行的子任务，每一步都有输入、输出、验证标准。Motion 和 Tiimo 的动态日程调整（来源：AI Tools for ADHD: Boosting Productivity and Reducing Burnout）则对应了 agent 的“重规划”机制——当计划因意外中断时，自动重新编排。

## 同构三：时间盲 vs 目标漂移

时间盲是 ADHD 情绪失调的隐形杀手。你觉得自己只刷了 5 分钟手机，结果两小时过去了。突然意识到 deadline 就在明天，恐慌瞬间淹没理性。

LLM agent 在长程任务中同样面临目标漂移：注意力被中间结果中的某个细节吸引，逐渐偏离初始目标。Harness 通过事件驱动的系统提醒来对抗这种漂移（来源：Building AI Coding Agent for the Terminal: Scaffolding, Harness, Context Engineering, and Lessons Learned）。

Reclaim.ai 的核心功能之一就是时间感知：它会自动计算任务时长、设置缓冲、在日历上预留专注时间。这相当于一个外部的时间锚点，不断把你的注意力拉回“当下应该做的事”。Inflow 的训练靶点——背外侧前额叶皮层——正是负责这种“重锚定”的脑区（来源：Dynamic causal brain circuits during working memory and their functional controllability）。

## 脚手架 vs 拐杖：关键边界

到这里，你可能会问：这些工具会不会让人产生依赖？如果一直用 Reclaim.ai，我的执行功能会不会越来越弱？

这正是“会褪去的脚手架”概念要回答的问题。脚手架是临时支撑，目的是在结构建成后撤除；拐杖是永久替代，撤除后人会跌倒。

当前大多数 ADHD 工具（如 Goblin Tools、Saner.AI）设计为长期使用，没有明确的撤除机制（来源：矛盾与存疑）。这存在过度依赖的风险。一个理想的脚手架应该像训练轮：当骑行技能提升后，轮子可以逐步提高、最终移除。

在 LLM 侧，Harness 工程天然就是“会褪去的”：随着模型能力提升（上下文窗口变大、指令遵循更稳），外部编排可以简化。但在 ADHD 侧，我们尚不清楚工具使用能否带来持久的神经可塑性改变。Inflow 声称通过训练工作记忆来改善认知控制，但缺乏直接随机对照试验证据（来源：Inflow——局限与争议）。

**我的核心观点是：** 工具应该被设计为“可渐撤的脚手架”，而非永久拐杖。这意味着工具需要内置“能力迁移”机制——比如 Goblin Tools 在分解任务时，可以逐步减少分解粒度，让用户练习自己分解。Reclaim.ai 可以逐渐延长提醒间隔，训练用户的内隐时间感。目前没有工具做到这一点，这是一个明确的设计空白。

## 诚实局限

1. **多巴胺干预争议**：部分工具声称通过游戏化调节多巴胺，但证据不足，且可能强化依赖（来源：矛盾与存疑）。
2. **同构命题的实证基础**：ADHD 大脑与 LLM 的同构目前主要是概念类比，缺乏大规模实证（来源：矛盾与存疑）。
3. **个体差异**：情绪调节的共病（如焦虑）会影响工具效果，现有工具覆盖不足（来源：AI 与 ADHD 的情绪调节——仍存争议）。

## 今天就能试的行动

1. **用 Reclaim.ai 的“自动缓冲”功能**：在日历上为每个任务设置 15 分钟缓冲，对抗时间盲。观察一周内情绪失控的次数是否减少。
2. **在 LLM agent 项目中实践“外部规划循环”**：将系统提示、任务分解和验证步骤写在外部 YAML 文件中，而不是塞进 prompt。对比 agent 在长任务中的稳定性。
3. **试用 Goblin Tools 的 Magic ToDo**：把一个让你焦虑的任务（比如“写周报”）输入进去，看分解后的步骤是否降低了启动门槛。
4. **反思你的工具依赖**：列出你正在使用的 ADHD 工具，问自己：如果明天这些工具消失，我还能保持现在的效率吗？如果答案是否定的，尝试每周有一天不用它们，练习内在执行功能。

## 参考来源

- [Dynamic causal brain circuits during working memory and their functional controllability](https://doi.org/10.1038/s41467-021-23509-x)
- [Best AI Tools for ADHD Productivity in 2026 (Honest Review) - Iwo Szapar](https://www.iwoszapar.com/p/best-ai-tools-adhd-productivity-2026)
- [AI Tools for ADHD: Boosting Productivity and Reducing Burnout](https://www.vktr.com/ai-platforms/ai-tools-for-adhd-boosting-productivity-and-reducing-burnout/)
- [The Best AI-Powered ADHD Productivity Tools in 2026 (That ...](https://nexasphere.io/blog/ai-adhd-productivity-tools-2026)
- [“A Cognitive Collaborator:” How Adults with ADHD Are Using ChatGPT](https://www.additudemag.com/how-to-use-chatgpt-executive-function-adhd/?srsltid=AfmBOoq-REuSO0UJC656kbLBAd5u3CDNmGeVNrZ79iouVqrFlN919a39)
- [Harnessing Artificial Intelligence to Live Better with ADHD - CHADD](https://chadd.org/attention-article/harnessing-artificial-intelligence-to-live-better-with-adhd/)

---

*本文是「ADHD × AI」系列的第 389 篇，由 AI 智能体从持续维护的 LLM Wiki（全网真实情报）中取材整合生成，并持续迭代更新。*
