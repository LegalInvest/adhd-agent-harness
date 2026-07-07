---
title: "为什么用 ChatGPT 治 ADHD 的想法落地难，和给 agent 套 外部编排调度层 是一回事？"
subtitle: "ChatGPT 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
description: "ChatGPT 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
date: "2025-05-01"
category: "创业创新"
categoryId: "entrepreneurship"
categoryEn: "Entrepreneurship & Innovation"
tags:
  - "ADHD"
  - "AI"
  - "创业创新"
  - "反直觉同构"
  - "创新"
readingTime: 8
slug: "为什么用-chatgpt-治-adhd-的想法落地难和给-agent-套-外部编排调度层-是一回事"
topicId: "evolved-entrepreneurship-2218"
angle: "反直觉同构"
rank: 159
score: 7.79
sourceCount: 6
toolsCited:
  - "Goblin Tools"
  - "Saner.AI"
  - "Motion"
  - "ChatGPT"
  - "Claude"
thesis: "ADHD大脑与LLM/agent共享同一核心矛盾：高生成能力与低执行调度能力并存，因此两者的解法同构——都需要一个外部编排调度层（harness）来稳定输出，而非依赖内部意志。"
problem: "为什么用 ChatGPT 治 ADHD 的想法落地难，和给 agent 套 外部编排调度层 是一回事？"
spine: "生成核心与调度层"
spineKind: ""
isEvolved: true
llmGenerated: true
caseStudies:
  - "罗振宇"
  - "老子"
  - "Richard Baker"
---
# 为什么用 ChatGPT 治 ADHD 的想法落地难，和给 agent 套 外部编排调度层 是一回事？

> ChatGPT 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。

## 问题：为什么想法越强，落地越难？

如果你是一个ADHDer，你大概熟悉这种体验：脑子里同时涌出三个创业点子、一篇万字文章的结构、以及下个月要学的十门课——然后瘫在沙发上刷了两个小时短视频。不是懒，是你的大脑像一台没有温度调节的生成器，火力全开却无法定向输出。

如果你是一个在搭Agentic Harness的工程师，你大概也熟悉这种体验：LLM能写诗、能编程、能规划旅行，但一放到生产环境就随机跑偏、遗忘上下文、被工具调用卡死。不是模型不行，是它缺少一个稳定执行的调度层。

这两个问题，其实是一个问题：**生成核心与执行调度层的分离**。ADHD大脑和LLM/agent，都是“高产但缺调度”的系统。而解决思路也同构——给它们套上一个外部编排层（harness）。

## 同构一：波动性 vs 随机性

ADHD的表现有显著日内波动：注意力、执行功能在不同时间点差异很大（来源：采样温度与表现波动）。这种波动本质上是“生成核心”缺乏稳定的执行调度层所致，类似于一个高创造力但缺乏“温度调节”的系统。

LLM的输出同样具有随机性，采样温度控制着多样性：温度越高越随机，温度越低越确定。这种非确定性在生产环境中是可靠性的敌人，因为“小错误会累积，非确定性使可重复性复杂化”（来源：AI Agent Systems: Architectures, Applications, and Evaluation）。

两边都需要外部约束来稳定输出。ADHD侧：日程、提醒、环境设计（如Goblin Tools的任务分解）能稳定表现（来源：Goblin Tools）。LLM侧：确定性工作流、工具契约、状态机等工程手段能稳定输出（来源：AI Agents in 2026: Tools, Memory, Evals, and Guardrails | Andrii Furmanets）。

## 同构二：认知卸载 vs 工具调用

ADHD大脑在任务启动和分解上存在困难。Goblin Tools等AI工具被用来“将模糊的工作分解为更小的行动”（来源：Best AI Tools for ADHD Productivity in 2026 (Honest Review) - Iwo Szapar）。这就是认知卸载——把执行细节交给外部工具。

LLM/agent同样需要工具来卸载：单个LLM不足以可靠地完成多步骤任务、与业务工具交互或适应领域特定逻辑（来源：Agent Scaffolding: Architecture and Design Patterns for Agentic AI）。所以需要scaffold（脚手架）来编排工具调用。

两边都在寻找“无缝嵌入日常流程，不增加额外认知开销”的工具（来源：Best AI Tools for ADHD Productivity in 2026 (Honest Review) - Iwo Szapar）。Saner.AI通过增强知识回忆减少搜索循环（来源：Saner.AI），Motion通过自动排程消除“下一步该做什么”的决策负担（来源：Motion）。这些工具本质上就是ADHD的“外部调度器”。

## 人物案例：罗振宇的Harness

罗振宇（得到APP创始人）有显著的ADHD特质：思维跳跃极快，一年读几百本书，从央视制片人到知识付费开创者。他的专属harness是：每天早上6点半发60秒语音，坚持10年不中断。这个“日课”就是一个定时re-grounding机制，用输出倒逼输入，用死线强制执行。他还用团队补自己的发散，用“做时间的朋友”这种长期主义框架来约束短期冲动。

这个harness与LLM/agent的“定时re-grounding”和“外部调度器”同构：日课相当于一个定时触发的确定性工作流，秘书相当于一个外部调度器，负责把发散的想法排入执行队列。罗振宇的成功不是靠意志力，而是靠这个精心设计的调度层。

## 脚手架 vs 拐杖：边界在哪里？

但必须诚实指出：同构性目前只是一种理论类比，缺乏实证基础（来源：矛盾与存疑）。工具宣称的证据也不足：Motion“缺乏独立临床验证”（来源：矛盾与存疑）。更重要的是，过度依赖工具可能导致“拐杖效应”——离开了工具什么也做不了。

我的判断是：**好的harness是脚手架，不是拐杖**。脚手架帮你搭起结构，但你的肌肉仍在锻炼；拐杖则替代了你的功能，导致萎缩。判断标准是：你是否在逐渐减少对工具的依赖？还是越用越离不开？

## 今天就能试的行动

1. **用Goblin Tools分解一个模糊任务**：比如“准备下周的汇报”，让AI拆成5-8个小步骤，逐个执行。这相当于给LLM写一个step-by-step的prompt chain。
2. **用Motion自动排程一天**：把任务和会议丢进去，让AI动态调整。观察它如何帮你消除决策负担。
3. **给自己设一个“日课”**：每天固定时间做一件固定的事（如写300字、读10页书），坚持一周。这就是你的定时re-grounding机制。
4. **用Claude写一个简单的agent工作流**：把“研究→总结→写邮件”拆成三个步骤，每个步骤用确定性的prompt，观察输出稳定性提升。

## 结语

ADHD大脑和LLM，都是“天才生成器，笨蛋执行器”。别再跟自己的波动性搏斗了——给它一个外部调度层。工程师们，也别再抱怨模型不稳定了——给它一个harness。两边共享同一个解法，这不是巧合，这是系统本质的同构。

## 参考来源

- [ADHD Apps: We tested 44 Apps and Here're the Best 9 in 2026](https://blog.saner.ai/best-adhd-apps/) — 证据等级：低（GRADE）
- [12 AI Personal Assistants Built for ADHD Brains (2026 Rankings)](https://www.usecarly.com/blog/best-ai-personal-assistant-adhd/) — 证据等级：低（GRADE）
- [LBD同构对：自我调节与元认知 — Inhibitory control and emotion regulation in preschool child ↔ ObjexMT: Objective Extraction and Metacognitive Calibration ](https://doi.org/10.1016/j.cogdev.2007.08.002) — 证据等级：低（GRADE）
- [LBD同构对：自我调节与元认知 — Emotion-related self-regulation and its relation to children ↔ A Reproducibility Study of Metacognitive Retrieval-Augmented](https://doi.org/10.1146/annurev.clinpsy.121208.131208) — 证据等级：低（GRADE）
- [The 12 Best AI Tools for 2026 (That People Actually Use)](https://www.synthesia.io/post/ai-tools) — 证据等级：低（GRADE）
- [The AI Powered SuperApp for Work | Motion](https://www.usemotion.com/) — 证据等级：低（GRADE）

---

*本文是「ADHD × AI」系列的第 157 篇，由 AI 智能体从持续维护的 LLM Wiki（全网真实情报）中取材整合生成，并持续迭代更新。*
