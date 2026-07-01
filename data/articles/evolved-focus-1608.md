---
title: "为什么用 Perplexity 治 ADHD 的注意力涣散，和给 agent 套 上下文工程 是一回事？"
subtitle: "Perplexity 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
description: "Perplexity 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
date: "2025-04-02"
category: "专注力管理"
categoryId: "focus"
categoryEn: "Focus Management"
tags:
  - "ADHD"
  - "AI"
  - "专注力管理"
  - "反直觉同构"
  - "专注力"
readingTime: 7
slug: "为什么用-perplexity-治-adhd-的注意力涣散和给-agent-套-上下文工程-是一回事"
topicId: "evolved-focus-1608"
angle: "反直觉同构"
rank: 288
score: 7.68
sourceCount: 6
toolsCited:
  - "Perplexity"
  - "Focusmate"
  - "RescueTime"
  - "Brain.fm"
  - "Forest"
thesis: "ADHD 大脑与 LLM 共享相同的核心矛盾——强大的生成能力与脆弱的执行调度层——因此，用 Perplexity 等工具为 ADHD 搭建外部上下文工程，与为 AI agent 设计 harness 脚手架，本质上是同一套架构思维：通过主动管理注意力上下文，让生成核心稳定输出。"
problem: "为什么用 Perplexity 治 ADHD 的注意力涣散，和给 agent 套 上下文工程 是一回事？"
spine: "上下文工程"
spineKind: ""
isEvolved: true
llmGenerated: true
---
# 为什么用 Perplexity 治 ADHD 的注意力涣散，和给 agent 套 上下文工程 是一回事？

> Perplexity 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。

## 问题：为什么你刚打开 Perplexity 想查个东西，半小时后却发现自己刷了十条无关链接？

如果你有 ADHD，这个场景再熟悉不过：大脑像一台没有刹车的跑车，创意爆棚但方向失控。如果你在做 Agentic Harness 工程，你也会熟悉另一个场景：LLM 明明能写出漂亮代码，却因为上下文膨胀、工具调用混乱，输出变成垃圾。

这两件事，其实是同一个问题的两面。

## 同构：ADHD 大脑与 LLM 共享同一个架构缺陷

最新研究揭示了一个惊人的平行结构：ADHD 大脑与 Transformer 模型在认知架构上高度同构。两者都拥有强大的生成核心——ADHD 的创意发散、LLM 的文本生成——但缺乏可靠的执行调度层（来源：ADHD 大脑与 LLM 的同构）。

具体来说：
- **ADHD 侧**：工作记忆容量可能正常甚至超常，但认知灵活性与注意控制存在核心缺陷；注意力资源的弥散分配是其注意缺陷的计算本质（来源：Strong Memory, Weak Control: An Empirical Study of Executive Functioning in LLMs；Self-Attention Limits Working Memory Capacity of Transformer-Based Models）。
- **LLM 侧**：自注意力机制在长上下文下冲突解决能力崩溃至随机水平，这与 ADHD 执行功能障碍的核心神经机制一致（来源：Deficient Executive Control in Transformer Attention）。

换句话说，ADHD 大脑和 LLM 都是“高产但缺调度层”的生成机器。

## 解法：上下文工程——给生成核心套上 harness

既然问题同构，解法也应同构。

在 LLM/agent 领域，这个解法叫 **harness 工程**：设计围绕 AI 代理的脚手架——上下文交付、工具接口、规划工件、验证循环、记忆系统和沙箱（来源：GitHub - ai-boost/awesome-harness-engineering）。Harness 的核心是“上下文工程”：主动决定模型“当下注意什么”，而不是让上下文自然膨胀。

在 ADHD 侧，这个解法叫 **外部执行功能层**：通过工具补偿工作记忆、任务启动、时间感知等缺陷（来源：外部执行功能层）。本质上，这同样是上下文工程——主动设计“当下注意什么”的方案。

## 证据：两边都能找到的真实工具

### ADHD 侧：Focusmate 与 RescueTime

- **Focusmate**：通过虚拟身体在场提供实时同伴问责（来源：Focusmate）。它本质上是一个外部“调度层”：当你注意力漂移时，视频中的伙伴把你拉回上下文。这不是 AI 工具，但它的算法匹配优化了身体在场体验（来源：The Best AI-Powered ADHD Productivity Tools in 2026）。
- **RescueTime**：自动追踪时间使用，减轻工作记忆负担，帮助识别注意力漂移模式（来源：RescueTime）。它像一个“上下文监控器”，让你看到自己实际在关注什么。

### LLM/agent 侧：Perplexity 与 Agent Harness

- **Perplexity**：当你用它搜索时，它的界面本身就是一个上下文工程工具：把搜索过程拆解为“提问→获取答案→追问”，每一步都锚定注意力。但如果你不加节制地连续追问，它也会变成注意力黑洞——这正是 ADHD 用户常掉进的坑。
- **Agent Harness**：在构建 AI agent 时，需要“包裹 LLM 的软件基础设施，处理模型本身之外的一切”（来源：What is an agent harness in the context of large-language models?）。这包括上下文管理、工具接口、记忆系统等，与 ADHD 工具的设计思路完全一致。

## 核心观点：脚手架 vs 拐杖——同构解法的边界

我的核心判断是：**上下文工程对 ADHD 和 LLM 都有效，但关键在于保持“脚手架”而非“拐杖”的性质。**

- **脚手架**：工具在你使用时提供结构，但离开后你仍能独立运作。例如，Focusmate 的实时问责——当你习惯了外部结构，可能逐渐内化任务启动能力。
- **拐杖**：工具替代了你的内在能力，一旦离开就瘫痪。例如，过度依赖 RescueTime 的时间追踪，可能让你失去对时间的主观感知（来源：矛盾与存疑）。

争议在于：当前多数工具的证据强度不足。Brain.fm 宣称通过神经锁相帮助专注，但缺乏针对 ADHD 的独立临床研究（来源：Brain.fm）。Focusmate 的用户报告积极，但缺乏随机对照试验（来源：证据脉络）。个体差异也很大：同一工具对 ADHD 不同亚型效果迥异（来源：矛盾与存疑）。

## 行动：今天就能试的 4 条上下文工程策略

1. **用 Perplexity 时，每次只问一个具体问题，写下来**：打开一个文档，把当前问题写下来，回答后关闭标签。这模仿了 harness 的“上下文交付”——限制模型（和你自己）的注意范围。
2. **预约一次 Focusmate 时段**：哪怕只是 25 分钟，体验一下外部问责如何锚定注意力。注意观察：它是在帮你启动，还是让你依赖？
3. **安装 RescueTime 并设置每日 5 分钟回顾**：不要盯着实时数据，而是每天看一次总结，识别自己的“上下文膨胀”模式。
4. **给你的 AI agent 也画一个上下文边界**：如果你在用任何 LLM 工具，明确告诉它“只回答这个问题，不要延伸”，然后观察输出质量的变化。

## 局限与诚实

同构是隐喻，不是严格等价。LLM 的“注意力机制”与人类注意力存在本质差异（来源：ADHD 大脑与 LLM 的同构）。此外，过度依赖 AI 工具可能削弱内在执行功能（来源：矛盾与存疑）。本文的论点基于现有研究，但多数证据来自用户报告或小样本研究，缺乏大规模对照实验。

但无论你是被注意力涣散折磨的 ADHD 患者，还是被上下文工程困扰的工程师，核心教训一致：**不要试图修复生成核心，去修复它周围的上下文。**

## 参考来源

- [11 Best ADHD Productivity Apps for Fluctuating Energy - rivva blog](https://blog.rivva.app/p/11-best-adhd-productivity-apps-for)
- [Meta-Analysis of fMRI Studies of Disruptive Behavior Disorders](https://doi.org/10.1176/appi.ajp.2016.15081089)
- [Nonlinear Complexity Analysis of Brain fMRI Signals in Schizophrenia](https://doi.org/10.1371/journal.pone.0095146)
- [The Best AI-Powered ADHD Productivity Tools in 2026 (That ...](https://nexasphere.io/blog/ai-adhd-productivity-tools-2026)
- [AI Tools for Kids with ADHD: A Complete Guide for Parents...](https://www.kidsaitools.com/en/articles/ai-tools-kids-adhd-complete-guide-2026)
- [AI Tools for ADHD: Boosting Productivity and Reducing Burnout](https://www.vktr.com/ai-platforms/ai-tools-for-adhd-boosting-productivity-and-reducing-burnout/)

---

*本文是「ADHD × AI」系列的第 288 篇，由 AI 智能体从持续维护的 LLM Wiki（全网真实情报）中取材整合生成，并持续迭代更新。*
