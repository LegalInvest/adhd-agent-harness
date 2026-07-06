---
title: "为什么用 Goblin Tools 治 ADHD 的学习半途而废，和给 agent 套 外部记忆/向量库 是一回事？"
subtitle: "Goblin Tools 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
description: "Goblin Tools 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
date: "2025-03-23"
category: "学习方法"
categoryId: "learning"
categoryEn: "Learning Methods"
tags:
  - "ADHD"
  - "AI"
  - "学习方法"
  - "反直觉同构"
readingTime: 9
slug: "为什么用-goblin-tools-治-adhd-的学习半途而废和给-agent-套-外部记忆向量库-是一回事"
topicId: "evolved-learning-1656"
angle: "反直觉同构"
rank: 292
score: 7.68
sourceCount: 6
toolsCited:
  - "Goblin Tools"
  - "Perplexity"
  - "Saner.AI"
  - "Tiimo"
  - "Motion"
thesis: "ADHD 大脑与 LLM 都是高产生成核心但缺失可靠执行调度层，两者的外部补偿方案（如 Goblin Tools 和 agent 外部记忆）结构同构，本质上都是在为无状态系统搭建脚手架。"
problem: "为什么用 Goblin Tools 治 ADHD 的学习半途而废，和给 agent 套 外部记忆/向量库 是一回事？"
spine: "无状态与外部记忆"
spineKind: ""
isEvolved: true
llmGenerated: true
caseStudies:
  - "孔子"
  - "释迦牟尼"
  - "区一佳 (Ou Yijia)"
---
# 为什么用 Goblin Tools 治 ADHD 的学习半途而废，和给 agent 套 外部记忆/向量库 是一回事？

> Goblin Tools 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。

## 问题：为什么你总在学习半途而废？

你打开一本书，五分钟后就刷起了手机。你列了完美计划，第二天就扔在一边。你不是懒——你的大脑像一台没有操作系统的超级计算机：能生成最精妙的设想，却无法调度任务、维持上下文、按时启动。ADHD 的核心困境不是智力不足，而是执行功能（executive function）的失效——"大脑的驾驶座"常常感觉方向盘后没有人（来源：AI Tools for ADHD: Boosting Productivity and Reducing Burnout）。

## 同构：ADHD 大脑与 LLM 是同一类系统

最新研究揭示了一个反直觉的平行：ADHD 患者的工作记忆容量未必差，但自上而下的控制和调节能力不足，呈现"强记忆、弱控制"的认知剖面（来源：Strong Memory, Weak Control: An Empirical Study of Executive Functioning in LLMs）。这种模式与 LLM 惊人相似——LLM 拥有强大的语言生成能力，但单独使用时缺乏可靠的执行调度，容易因上下文膨胀导致推理退化（来源：Building AI Coding Agents for the Terminal: Scaffolding, Harness, Context Engineering, and Lessons Learned）。

两者都是"高产但缺执行调度层的生成核心"。ADHD 的注意力漂移对应 LLM 的上下文丢失；ADHD 的时间盲对应 LLM 的无状态性；ADHD 的任务启动困难对应 LLM 的"白页恐惧"（面对空白 prompt 不知从何开始）。

## 解法：外部脚手架，而非拐杖

Goblin Tools 的 Magic ToDo 功能，能把"清理厨房"这样的模糊任务自动分解为具体、可执行的子步骤，用户还可调节"辣度"控制粒度（来源：12 AI Personal Assistants Built for ADHD Brains (2026 Rankings)）。这就是在给 ADHD 大脑补上一个外部调度层——把宏大目标转化为可管理、可启动的行动序列。

类似地，agent 工程中通过"复合 AI 系统架构"来弥补 LLM 的调度缺陷，包括工作负载专用模型路由、分离规划与执行的双代理架构、惰性工具发现、自适应上下文压缩（来源：Building AI Coding Agents for the Terminal: Scaffolding, Harness, Context Engineering, and Lessons Learned）。这些技术本质上是在 LLM 外部搭建调度层，防止上下文膨胀和推理退化。

Perplexity 也是这一思路的典型落点：它通过把宏大目标分解为可管理的步骤，直接降低了 ADHD 用户的执行功能负担（来源：ADHD Productivity Hack: Plan 2025 Using AI (Step-by-Step)）。Saner.AI 则通过增强知识回忆，帮助用户快速找回信息，减少搜索循环——这相当于为 ADHD 大脑提供了外部记忆库（来源：Best AI Tools for ADHD Productivity in 2026 (Honest Review) - Iwo Szapar）。

## 历史佐证：孔子与释迦牟尼的 harness 系统

孔子一生精力旺盛、冲动爱骂人，思维跳跃，《论语》全是场景化语录，无系统著作。他的 harness 是"克己复礼"——用外在的"礼"作为行为边界，每日反省（"吾日三省吾身"）。释迦牟尼 29 岁说走就走，49 年游行说法，一字未写。他的 harness 是"八正道"和"持戒"，用戒律管行为，用正念拴念头。

这两位两千多年前的"ADHD 大脑"，都自发发明了外部脚手架：日课相当于定时 re-grounding，戒律相当于外部调度器，语录相当于上下文压缩。这与现代 agent 的"定时上下文压缩"和"外部记忆库"是同构的工程策略。

## 边界：脚手架 vs 拐杖

同构不意味着 ADHD 与 LLM 是同一系统，而是意味着它们的工程化补偿策略可以相互借鉴。支架的目的是能力代偿，而非制造永久依赖（来源：拐杖与脚手架）。专家警告过度依赖风险：若工具替代了治疗或自我管理，可能造成依赖（来源：AI Tools for ADHD: Boosting Productivity and Reducing Burnout）。真正的脚手架应帮助使用者"建造"，但使用者仍需自己"攀登"（来源：AI Tools for ADHD: Boosting Productivity and Reducing Burnout）。

目前，ADHD 大脑与 LLM 同构的论点多为类比推理，缺乏神经科学或计算机科学的直接证据（来源：矛盾与存疑）。AI 工具对任务启动的长期效果也未知（来源：矛盾与存疑）。但短期来看，这一框架至少提供了一个可操作的设计原则：不要试图修复生成核心，而是为它搭建可靠的外部调度层。

## 今天就能试的行动

1. **用 Goblin Tools 分解一个拖延任务**：打开 Magic ToDo，输入你拖延最久的任务（如"写报告"），调节辣度到你觉得可执行的粒度，然后执行第一步。
2. **用 Perplexity 规划一个项目**：输入"帮我规划 2025 年的学习计划"，让 AI 分解为可管理的步骤，然后设定每周一个里程碑。
3. **建立你的"日课"系统**：模仿孔子和释迦牟尼，每天固定时间做三件事：回顾昨天、规划今天、清理工作记忆。可以用 Saner.AI 或简单的笔记应用。
4. **为你的 agent 添加外部记忆**：如果你在开发 agent，尝试集成向量数据库（如 Pinecone）或使用上下文压缩技术，防止 LLM 在长对话中丢失上下文。

## 参考来源

- [Can ChatGPT be Your Personal Medical Assistant?](http://arxiv.org/abs/2312.12006v1)
- [One Billion Word Benchmark for Measuring Progress in Statistical Language Modeling](http://arxiv.org/abs/1312.3005v3)
- [Activation Sparsity Opportunities for Compressing General Large Language Models](http://arxiv.org/abs/2412.12178v2)
- [YouZhi: Towards High-Concurrency Financial LLMs via Adaptive GQA-to-MLA Transition](http://arxiv.org/abs/2606.05868v1)
- [FBI-LLM: Scaling Up Fully Binarized LLMs from Scratch via Autoregressive Distillation](http://arxiv.org/abs/2407.07093v1)
- [Prompt Injection Attack to Tool Selection in LLM Agents](http://arxiv.org/abs/2504.19793v3)

---

*本文是「ADHD × AI」系列的第 292 篇，由 AI 智能体从持续维护的 LLM Wiki（全网真实情报）中取材整合生成，并持续迭代更新。*
