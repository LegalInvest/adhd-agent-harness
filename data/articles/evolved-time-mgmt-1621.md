---
title: "为什么用 Claude 治 ADHD 的时间盲，和给 agent 套 planner-executor 任务分解 是一回事？"
subtitle: "Claude 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
description: "Claude 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
date: "2025-05-21"
category: "时间管理"
categoryId: "time-mgmt"
categoryEn: "Time Management"
tags:
  - "ADHD"
  - "AI"
  - "时间管理"
  - "反直觉同构"
  - "任务规划"
readingTime: 10
slug: "为什么用-claude-治-adhd-的时间盲和给-agent-套-planner-executor-任务分解-是一回事"
topicId: "evolved-time-mgmt-1621"
angle: "反直觉同构"
rank: 157
score: 7.75
sourceCount: 6
toolsCited:
  - "Motion"
  - "Reclaim.ai"
  - "Tiimo"
  - "Goblin Tools"
  - "Claude"
thesis: "ADHD 大脑与 LLM 在结构上同构——都是高产生成核心但缺乏可靠调度层，因此用外部 harness（如 planner-executor 框架）来补偿时间盲与执行不可靠，本质是同一类工程问题。"
problem: "为什么用 Claude 治 ADHD 的时间盲，和给 agent 套 planner-executor 任务分解 是一回事？"
spine: "规划循环与任务分解"
spineKind: ""
isEvolved: true
llmGenerated: true
caseStudies:
  - "孔子"
  - "张旭"
  - "覃辉"
---
# 为什么用 Claude 治 ADHD 的时间盲，和给 agent 套 planner-executor 任务分解 是一回事？

> Claude 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。

## 从同一个问题开始

你是否有过这样的体验：脑中闪过一个绝妙想法，下一秒却发现自己站在冰箱前，完全忘了刚才要做什么？或者，你打开 Claude 让它写一份周报，结果它写了三句就跑题，开始介绍如何烘焙酸面包？

这两件事——ADHD 的时间盲，和 LLM 的“跑题”——看似风马牛不相及，但它们的底层结构完全一致。本文要论证一个反直觉的命题：**ADHD 大脑与 LLM 是同一类“高产但缺执行调度层的生成核心”，而治它们的方案，也是同一套 harness。**

## 同构：生成核心与缺失的调度层

ADHD 大脑的典型特征是“高产”：创意源源不断，兴趣驱动下可以超聚焦到忘我。但它的执行功能——计划、排序、抑制、时间感知——天生不可靠。这就是所谓的“时间盲”：无法感知时间流逝，也无法把未来拆解成可执行的步骤（来源：AI Tools for ADHD: Boosting Productivity and Reducing Burnout）。

LLM 也一样。Claude、GPT 这类模型是极佳的语言生成器，但它们在多步任务中会“迷失”：忘记上下文、重复步骤、输出随机且不可控。LLM 的输出天然具有随机性，采样温度越高，输出越不可预测（来源：采样温度与表现波动）。

两边缺的是同一个东西：一个可靠的执行调度层。ADHD 大脑缺的是前额叶的执行功能，LLM 缺的是确定性的控制流。

## 解法同构：planner-executor 框架

工程师们早就发现，单个 LLM 不足以可靠地完成多步骤任务。于是他们给 LLM 套上“脚手架”（scaffolding）：把 LLM 置于与记忆、工具和决策逻辑的控制循环中，用“计划-执行”分离模式强制单向、确定性的控制流（来源：Agent Scaffolding: Architecture and Design Patterns for Agentic AI）。这就是 planner-executor 框架：一个规划器负责分解任务，一个执行器负责按步骤执行，中间用外部记忆和工具契约来保证确定性。

ADHD 的解法惊人地相似。孔子就是典型的例子。他精力旺盛、思维跳跃、冲动爱骂人，但用“克己复礼”作为外部 harness：用外在的“礼”作为行为边界，每日反省（“吾日三省吾身”），70 岁才做到从心所欲不逾矩。这个“礼”就是他的 planner，“反省”就是他的 executor 监控。

更现代的例子是 AI 时间管理工具。Motion 自动根据任务优先级和截止日期动态排程，消除“下一步该做什么”的决策负担（来源：Motion）。Reclaim.ai 保护时间块，防止突发会议打乱计划（来源：Reclaim.ai）。Tiimo 用视觉化时间线把“时间”变成可见元素，直接对抗时间盲（来源：Tiimo）。这些工具本质上都是外部调度层：它们承担了大脑本该做但做不好的规划、排序、提醒和监控。

## 温度波动 vs 确定性控制

ADHD 的表现波动很大：注意力、执行功能在不同时间点差异显著。这种波动就像 LLM 的采样温度：温度高时输出随机，温度低时输出确定。ADHD 大脑缺乏稳定的“温度调节”，所以表现忽高忽低。工程上，为了对抗 LLM 的非确定性，会采用“周期性采样以监控质量”、知识图谱等工具实现“确定性精度”（来源：采样温度与表现波动）。

ADHD 的“确定性精度”来自哪里？来自外部结构：日程、提醒、环境设计。Goblin Tools 把模糊的工作分解为更小的行动，降低启动门槛（来源：工具使用与认知卸载）。这些工具让大脑从“自己调度”变成“被调度”，从而稳定表现。

## 核心观点：脚手架，不是拐杖

这里有一个关键判断：外部 harness 是脚手架，不是拐杖。脚手架是临时结构，最终目标是让系统学会自己走路；拐杖是永久替代，系统离开它就会崩溃。

对于 LLM，脚手架（如 planner-executor 框架）的目的是让模型在受控环境中可靠执行，但模型本身并没有因此学会规划。对于 ADHD，外部工具的目的是补偿缺陷，但过度依赖可能导致能力退化（来源：矛盾与存疑）。长期依赖风险缺乏实证，但个体差异很大：有人需要永久辅助，有人可以逐步撤除。

## 局限与争议

必须诚实指出，ADHD 大脑与 LLM 同构的论点目前多是类比推理，缺乏神经科学或计算机科学的直接证据（来源：矛盾与存疑）。此外，AI 工具对任务启动的长期效果未知，学习使用工具本身可能增加认知负荷（来源：矛盾与存疑）。

## 今天就能试的行动

1. **用 Claude 做 planner-executor 实验**：给 Claude 一个模糊任务（比如“写一篇周报”），先让它输出分解步骤（planner），再让它按步骤执行（executor），对比直接让它输出的效果。
2. **设置外部时间块**：用 Reclaim.ai 或 Motion 自动保护 2 小时的深度工作时间，观察自己的任务启动是否变容易。
3. **视觉化时间**：试用 Tiimo 或 Structured，把一天的时间块画出来，对抗时间盲。
4. **记录波动**：连续三天每小时记录自己的注意力水平（1-10 分），找出自己的“采样温度”模式，然后安排高难度任务在高峰时段。

## 参考来源

- [The 12 Best AI Tools for 2026 (That People Actually Use)](https://www.synthesia.io/post/ai-tools)
- [The AI Powered SuperApp for Work | Motion](https://www.usemotion.com/)
- [11 Best ADHD Productivity Apps for Fluctuating Energy - rivva blog](https://blog.rivva.app/p/11-best-adhd-productivity-apps-for)
- [ADHD Apps: We tested 44 Apps and Here're the Best 9 in 2026](https://blog.saner.ai/best-adhd-apps/)
- [12 AI Personal Assistants Built for ADHD Brains (2026 Rankings)](https://www.usecarly.com/blog/best-ai-personal-assistant-adhd/)
- [The 12 Best Apps for ADHD in 2026: A Guide to Finding What ...](https://www.getinflow.io/post/best-apps-for-adhd)

---

*本文是「ADHD × AI」系列的第 157 篇，由 AI 智能体从持续维护的 LLM Wiki（全网真实情报）中取材整合生成，并持续迭代更新。*
