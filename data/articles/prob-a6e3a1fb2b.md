---
title: "ADHD 程序员视角：为什么「治好 ADHD 的怕过度依赖工具、又怕没有支撑就崩」和「让 LLM 不跑飞」其实是同一道工程题？"
subtitle: "harness 应是会褪去的脚手架，而非永久拐杖——同一套 harness 思路，两边都成立。"
description: "harness 应是会褪去的脚手架，而非永久拐杖——同一套 harness 思路，两边都成立。"
date: "2025-03-08"
category: "情绪调节"
categoryId: "emotion"
categoryEn: "Emotional Regulation"
tags:
  - "ADHD"
  - "AI"
  - "情绪调节"
  - "人群×同构"
  - "情绪管理"
readingTime: 10
slug: "adhd-程序员视角为什么治好-adhd-的怕过度依赖工具又怕没有支撑就崩和让-llm-不跑飞其实是同一道工程题"
topicId: "prob-a6e3a1fb2b"
angle: "人群×同构"
rank: 249
score: 7.67
sourceCount: 6
toolsCited:
  - "Inflow"
  - "Goblin Tools"
  - "Saner.AI"
  - "Motion"
  - "Brain.fm"
thesis: "ADHD 大脑与 LLM/agent 都是高产但缺乏可靠执行调度层的生成核心，两边的「依赖恐惧」与「跑飞恐惧」本质同一道题：harness 不是永久拐杖，而是可随能力增长逐步褪去的脚手架，核心目标是让外部调度层最终被内化为自身的执行功能。"
problem: "ADHD 程序员视角：为什么「治好 ADHD 的怕过度依赖工具、又怕没有支撑就崩」和「让 LLM 不跑飞」其实是同一道工程题？"
spine: "拐杖与脚手架"
spineKind: "bridge"
isEvolved: false
llmGenerated: true
isoStrength: "A"
caseStudies:
  - "释迦牟尼"
  - "于谦"
  - "雷英"
---
# ADHD 程序员视角：为什么「治好 ADHD 的怕过度依赖工具、又怕没有支撑就崩」和「让 LLM 不跑飞」其实是同一道工程题？

> harness 应是会褪去的脚手架，而非永久拐杖——同一套 harness 思路，两边都成立。

## 一个被两面夹击的问题

很多 ADHD 程序员都熟悉这种折磨：不用工具，项目启动不了、时间感崩坏、情绪随任务堆积而爆炸；用了工具，又立刻担心「我是不是越来越依赖它了？如果明天这个 App 下架、API 涨价、提示词失效，我是不是直接回到解放前？」

这种「怕过度依赖工具，又怕没有支撑就崩」的心态，在工程领域其实有精确对应。今天做 LLM/agent 工程的团队同样在问：模型生成能力很强，但容易幻觉、漂移、任务链断裂，于是我们必须加 harness（约束、验证、记忆、调度器）；可 harness 一旦太重，又怕系统永远离不开这层外部结构，变成「拐杖系统」。

我想提出的判断是：**这两边的恐惧是同一道题。** ADHD 大脑与 LLM/agent 是同一类「高产但缺执行调度层的生成核心」，两边需要的 harness 在结构上同构，而且都应该是会褪去的脚手架，而非永久拐杖。

## 同构：为什么两边是同一类系统

从工程视角看，一个智能系统可以拆成两层：生成核心（负责联想、创造、快速输出）与执行调度层（负责计划、抑制、维持上下文、时间估计、任务切换）。ADHD 大脑与当前 LLM 的共同点是：生成核心极强，执行调度层薄弱。

ADHD 侧的证据很直接。执行功能障碍（Executive Dysfunction）是 ADHD 的核心特征之一，它不是「不努力」，而是大脑在计划、组织、时间管理、任务启动、抑制控制等执行功能上效率低下（来源：A review of executive function deficits in autism spectrum disorder and attention-deficit/hyperactivity disorder）。工作记忆弱控制、注意力漂移、时间盲（time blindness）都是同一调度层缺陷的不同表现。

LLM/agent 侧的证据也对应：LLM 有强大的记忆容量，但弱控制；它容易上下文漂移、产生幻觉、在长任务链中丢失目标。这正是为什么 agent 工程需要外部记忆、工具调用、验证循环、人在回路（human-in-the-loop）等 harness 结构。两边的现象不同，但底层结构一致：**一个高产的生成核心，在没有外部调度约束时，会输出失控结果。**

## ADHD 侧的 harness：工具如何成为脚手架

把情绪调节困难重新理解为「执行调度失败」，再用 AI 作为外部 harness 去补偿，是目前 ADHD × AI 领域最站得住脚的框架。工具形态不重要，关键是它们是否构成有效的 harness。

Inflow 是典型例子。它基于认知行为疗法（CBT）原则，通过训练工作记忆和认知控制来改善 ADHD 症状，其核心概念来自大脑因果回路研究：背外侧前额叶皮层被识别为「因果流入中枢」，其功能连接性与工作记忆表现正相关（来源：Dynamic causal brain circuits during working memory and their functional controllability）。Inflow 不只是任务管理器，更像一个结构化技能训练系统，帮助用户把外部调度逐步内化。

Goblin Tools 则解决另一个子问题：任务启动。它的 Magic ToDo 能把模糊任务（如「清理厨房」）自动分解为可执行的子步骤，用户可以调节「辣度」控制粒度（来源：12 AI Personal Assistants Built for ADHD Brains (2026 Rankings)）。这对 ADHD 用户至关重要，因为启动困难往往源于多巴胺不足与任务粒度过大，而不是能力不足。

Saner.AI 解决的是「无状态」问题。ADHD 工作记忆弱，导致频繁在标签页和应用之间搜索、切换，形成认知负荷。Saner.AI 通过本地记忆和知识回忆减少这种搜索循环（来源：Best AI Tools for ADHD Productivity in 2026 (Honest Review) - Iwo Szapar）。这与 LLM 需要外部记忆系统（如 vector store、RAG）来补偿上下文限制，是同一类工程解法。

这些工具的共同点是：它们不替代你的大脑，而是替你维持「上下文」——让你的生成核心能在一个被约束、被结构化的环境中工作。

## 一个跨越两千年的 harness 案例：释迦牟尼

要理解「harness 不是拐杖，而是可褪去的脚手架」，释迦牟尼的案例非常贴切。他的 ADHD 式特质在史料中很明显：29 岁放弃王位、妻子、孩子，说走就走出家求道；之后六年里不断试错——先跟仙人学禅定，再尝试极端苦行，最后发现不对又放弃；一生 49 年游行说法，直到 80 岁仍在路上；他善用场景化比喻，自己却不写一字。

他的专属 harness 系统是「八正道」与「持戒」。这不是道德说教，而是一套外部调度协议：戒律管行为，正念拴住乱跑的念头，「自依止、法依止」则是不依赖任何权威，最终靠自己证悟。换句话说，他给自己装上了一套可操作的脚手架，让自己那个高产出、高漂移的「求道核心」不会彻底跑飞。

这与 LLM/agent harness 的对应非常清晰：「持戒」相当于系统的约束与护栏（guardrails）；「正念」相当于定时 re-grounding，让模型回到任务上下文；「自依止」相当于最终让系统能在减少外部干预的情况下自治。更妙的是，佛教的整个目标不是让你永远持戒，而是通过戒定慧的训练，最终把稳定的觉知内化为自身能力——这正是「脚手架会褪去」的古典版本。

## 拐杖与脚手架的边界在哪

但这里必须诚实划界：harness 不是越多越好，也不是越依赖越好。如果外部结构永远替代了内部调度，那就是拐杖；如果它帮助内部调度成长，并逐步退出，就是脚手架。

判断边界有三条标准：

1. **是否指向内化能力**：Inflow 的训练目标、Goblin 的分解练习、正念的觉察训练，都是在培养用户自身的执行功能；而有些工具只是替你完成任务，没有训练痕迹。
2. **是否可逐步减重**：好的 harness 应该允许你减少依赖而不崩溃。如果你关掉提醒就无法启动，说明它还没变成脚手架。
3. **是否增加认知负担**：有些工具本身反而制造了新的管理负担（更多标签、更多配置、更多订阅），这违背了 harness 的初衷。认知负荷页面也提到，需警惕工具本身增加负担（来源：认知负荷）。

## 我的核心判断与必须承认的局限

核心判断是：**ADHD 与 LLM 的「依赖恐惧」都是一种误诊。** 我们恐惧的并不是工具本身，而是把工具当成拐杖；真正该追求的是一套可退出的 harness——先靠外部结构稳定输出，再用神经可塑性把外部结构内化为自身执行功能。研究也表明，训练可以诱导抑制控制的行为与脑可塑性，从而正常化抑制控制能力及其底层脑网络（来源：Training-induced behavioral and brain plasticity in inhibitory control）。

但这套同构视角有明确的局限，必须指出：

- **同构性是理论类比，不是实证事实**。ADHD 大脑与 LLM 在结构上同构的说法，目前缺乏直接实证基础，不同页面在表述时有时把它当事实，有时当假设（来源：全局矛盾与存疑）。
- **工具证据参差不齐**。例如 Motion 被指出缺乏独立临床验证，Brain.fm 在 ADHD 人群中的独立临床证据也有限（来源：全局矛盾与存疑）。我们不应把工具宣传直接等同于疗效。
- **依赖风险真实存在**。ChatGPT、Claude 等工具页面往往只强调益处，较少讨论依赖风险。身体在场效应能否被 AI 真正替代，也仍有争议（来源：全局矛盾与存疑）。

所以，同构视角是一把双刃剑：它帮助我们理解问题结构，但不能替代个体化验证。

## 今天就能试的 4 步

1. **把一次崩溃写成 bug 报告**：下次任务链断裂或情绪爆炸时，不要只骂自己，而是记录：上下文在哪丢失的？是启动、记忆、时间估计还是抑制控制？这对应 LLM 的哪类失败？
2. **选一种 harness，只做最小闭环**：例如用 Goblin Tools 把今天最拖延的一个任务分解到第一步能执行的程度，不追求完整规划，只追求启动。
3. **设置「退出检查点」**：每使用工具两周，尝试关闭一次提醒或手动执行一次任务，观察自己是否能独立维持上下文。能，就是在褪去脚手架；不能，就再训练一轮。
4. **建立个人「八正道」清单**：像释迦牟尼那样，用 3-5 条极简规则（如「先写测试再写代码」「情绪上头时不发消息」）作为你的 guardrails，它们比任何工具都更不容易下架。

最终，无论是 ADHD 人还是 LLM 工程师，我们追求的都不是一个没有依赖的系统，而是一个知道何时需要 harness、何时能放下 harness 的系统。脚手架会褪去，但脚手架存在的证明，不是它永远被需要，而是你曾经需要它，然后学会了不再需要它。

## 参考来源

**同构强度：A 级** —— 直接文献支撑（引用 ADHD↔LLM 同构专题研究）

- [The 12 Best Apps for ADHD in 2026: A Guide to Finding What ...](https://www.getinflow.io/post/best-apps-for-adhd) — 证据等级：低（GRADE）
- [Dynamic causal brain circuits during working memory and their functional controllability](https://doi.org/10.1038/s41467-021-23509-x) — 证据等级：低（GRADE）
- [ADHD Apps: We tested 44 Apps and Here're the Best 9 in 2026](https://blog.saner.ai/best-adhd-apps/) — 证据等级：低（GRADE）
- [12 AI Personal Assistants Built for ADHD Brains (2026 Rankings)](https://www.usecarly.com/blog/best-ai-personal-assistant-adhd/) — 证据等级：低（GRADE）
- [Deficient Executive Control in Transformer Attention](https://www.biorxiv.org/content/10.1101/2025.01.22.634394v1.full.pdf) — 证据等级：低（GRADE）
- [Executive Dysfunction by Design: A Cognitive Accessibility Analysis of AI Support vs. Healthcare Barriers](https://dl.acm.org/doi/pdf/10.1145/3663547.3749831) — 证据等级：低（GRADE）

---

*本文是「ADHD × AI」系列的第 102 篇，由 AI 智能体从持续维护的 LLM Wiki（全网真实情报）中取材整合生成，并持续迭代更新。*
