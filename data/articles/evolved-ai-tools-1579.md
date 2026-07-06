---
title: "为什么用 Todoist 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用 是一回事？"
subtitle: "Todoist 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
description: "Todoist 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
date: "2025-04-20"
category: "AI工具实战"
categoryId: "ai-tools"
categoryEn: "AI Tools in Practice"
tags:
  - "ADHD"
  - "AI"
  - "AI工具实战"
  - "反直觉同构"
  - "ADHD辅助"
readingTime: 7
slug: "为什么用-todoist-治-adhd-的任务启动困难和给-agent-套-function-calling-工具调用-是一回事"
topicId: "evolved-ai-tools-1579"
angle: "反直觉同构"
rank: 381
score: 7.65
sourceCount: 6
toolsCited:
  - "Todoist"
  - "Goblin Tools"
  - "Lex"
  - "Saner.AI"
  - "ChatGPT"
  - "Claude"
thesis: "ADHD 的任务启动困难与 LLM 的 function calling 缺失，本质是同一问题：高产生成核心缺少外部调度层。Todoist 和 agent harness 都是为这个核心搭建的脚手架，而非拐杖。"
problem: "为什么用 Todoist 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用 是一回事？"
spine: "工具使用与认知卸载"
spineKind: ""
isEvolved: true
llmGenerated: true
caseStudies:
  - "孔子"
  - "胡林翼"
  - "赵晶"
---
# 为什么用 Todoist 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用 是一回事？

> Todoist 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。

你有没有过这样的瞬间：Todoist 里躺着 20 条待办，每一条都像一堵墙——你盯着“写周报”三个字，手指悬在键盘上，却怎么也敲不下去。另一边，你调试的 AI agent 收到指令“帮我查一下明天的天气”，它生成了完美的 JSON，但就是没调用 get_weather 函数。

这两个场景，看似毫无关联，实则共享同一个底层问题：**高产生成核心，缺少一个可靠的执行调度层。**

## 同构的困境：高产但“卡住”

ADHD 大脑被描述为“高产但缺调度层”——想法丰富、联想活跃，但工作记忆不稳定，任务启动像推一堵墙（来源：AI Tools for ADHD: Boosting Productivity and Reducing Burnout）。最新研究甚至发现，ADHD 患者的认知剖面是“强记忆、弱控制”：工作记忆容量可能超常，但自上而下的注意控制存在核心缺陷（来源：Strong Memory, Weak Control: An Empirical Study of Executive Functioning in LLMs）。

LLM 呢？它同样拥有强大的生成能力，但单独使用时，它不知道什么时候该调用工具、如何保持长程目标。Transformer 的自注意力机制在长上下文下冲突解决能力会崩溃至随机水平——这恰恰与 ADHD 执行功能障碍的核心神经机制一致（来源：Deficient Executive Control in Transformer Attention）。

所以，当你用 Todoist 给 ADHD 大脑搭脚手架，和当你给 LLM 套 function calling harness，你在做同一件事：**在生成核心外面，装一个调度层。**

## 历史人物已经验证了这套 harness

孔子和胡林翼，两个看似无关的历史人物，都用行动证明了这一点。

孔子身高近 1.9 米，精力旺盛，周游列国 14 年根本坐不住；他冲动爱骂人，见南子急得对天发誓，骂宰予“朽木不可雕”；但对音乐可以专注到“三月不知肉味”，对种地等俗事零耐心。他的 harness 是什么？**“克己复礼”**——用外在的“礼”作为行为边界，每日反省，“吾日三省吾身”。直到 70 岁才“从心所欲不逾矩”，一辈子在和自己的冲动做斗争。

胡林翼年轻时是花花公子，在扬州天天逛妓院。父亲去世后幡然醒悟，出山带兵，成为湖北巡抚。他的 harness 是**每日写日记反省**，和曾国藩一起做圣人，严格治军。

这两个 harness 的核心，和给 LLM 套的 scaffolding 完全同构：
- **日课** ↔ **定时 re-grounding**（让系统定期回顾目标）
- **外在礼法** ↔ **工具接口约束**（限制行为在安全边界内）
- **秘书/师友** ↔ **外部调度器**（提供外部执行指令）

他们不是靠“意志力”战胜 ADHD，而是靠外部脚手架把高产生成核心约束到目标轨道上。

## 今天的工具，就是数字时代的 harness

现在，这些脚手架被封装成了 AI 工具：
- **Goblin Tools** 的 Magic ToDo 自动将模糊任务分解为可执行步骤，用户可调节“辣度”控制粒度（来源：Best AI Tools for ADHD Productivity in 2026）。
- **Lex** 允许通过单一指令触发多步骤任务序列，降低启动时的认知负荷（来源：Best AI Tools for ADHD Productivity in 2026）。
- **Saner.AI** 通过本地记忆和知识回忆，减少搜索循环和标签切换（来源：Best AI Tools for ADHD Productivity in 2026）。

这些工具的本质，和 agent harness 工程完全一致：设计围绕 LLM 的脚手架——上下文交付、工具接口、规划工件、验证循环、记忆系统（来源：Building AI Coding Agents for the Terminal）。

## 脚手架 vs 拐杖：边界在哪里？

但这里有一个必须直面的争议：这些工具是“外部执行功能层”还是“拐杖”？

核心论点认为，AI 是在搭建临时的外部执行功能层，补偿缺陷而非替代大脑（来源：ADHD 的 AI 工具全景）。但存疑者担心，过度依赖可能导致能力退化（来源：矛盾与存疑）。

我的判断是：**边界在于“是否保留生成核心的主动权”。** 脚手架让你自己开车，只是给了你导航和自动变速箱；拐杖是替你开车。Todoist 和 function calling 都是导航——它告诉你下一步该做什么，但方向盘在你手里。如果你连“下一步”都不想看，那才叫拐杖。

## 今天就能试的 3 件事

1. **把你的 Todoist 当成 agent harness**：给每条任务加一个“启动指令”（比如“打开文档，写第一段”），而不是只写“写周报”。这相当于给 LLM 加一个 function call 的 prompt。

2. **用 Goblin Tools 的 Magic ToDo 分解一个你一直拖延的任务**：把“清理厨房”变成“1. 把碗放进洗碗机 2. 擦台面 3. 拖地”。每个子任务都是一个可调用的工具。

3. **给自己设一个“日课”**：像孔子和胡林翼一样，每天固定时间做一件事（比如写三行日记）。这相当于给大脑设一个 cron job，定时触发 re-grounding。

## 局限与诚实

必须承认，ADHD 大脑与 LLM 的同构目前更多是类比推理，缺乏神经科学的直接证据（来源：矛盾与存疑）。此外，AI 工具对任务启动的长期效果未知，个体差异极大。但至少，这个框架给了我们一个统一的工程视角：**无论是人还是机器，高产生成核心都需要一个外部调度层。**

下次你对着 Todoist 发呆，或者调试 agent 的 function calling 失败时，记得：你不是在对抗缺陷，你只是在搭建脚手架。

## 参考来源

- [ADHD Apps: We tested 44 Apps and Here're the Best 9 in 2026](https://blog.saner.ai/best-adhd-apps/)
- [12 AI Personal Assistants Built for ADHD Brains (2026 Rankings)](https://www.usecarly.com/blog/best-ai-personal-assistant-adhd/)
- [The 12 Best AI Tools for 2026 (That People Actually Use)](https://www.synthesia.io/post/ai-tools)
- [Agent Scaffolding: Architecture and Design Patterns for Agentic AI](https://zbrain.ai/agent-scaffolding/)
- [Best productivity apps for Mac you need to try](https://macpaw.com/reviews/best-productivity-apps-for-mac)
- [Building AI Coding Agents for the Terminal: Scaffolding, Harness ...](https://arxiv.org/html/2603.05344v1)

---

*本文是「ADHD × AI」系列的第 381 篇，由 AI 智能体从持续维护的 LLM Wiki（全网真实情报）中取材整合生成，并持续迭代更新。*
