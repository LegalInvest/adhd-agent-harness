---
title: "为什么用 Claude 治 ADHD 的感到孤立缺问责，和给 agent 套 human-in-the-loop 监督 是一回事？"
subtitle: "Claude 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
description: "Claude 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
date: "2025-03-11"
category: "社群与文化"
categoryId: "community"
categoryEn: "Community & Culture"
tags:
  - "ADHD"
  - "AI"
  - "社群与文化"
  - "反直觉同构"
  - "去污名化"
readingTime: 7
slug: "为什么用-claude-治-adhd-的感到孤立缺问责和给-agent-套-human-in-the-loop-监督-是一回事"
topicId: "prob-be31e3d8e4"
angle: "反直觉同构"
rank: 385
score: 7.62
sourceCount: 6
toolsCited:
  - "Goblin Tools"
  - "Saner.AI"
  - "Motion"
  - "Claude"
thesis: "ADHD 大脑与 LLM 是同一类'高产但缺乏稳定执行调度层的生成核心'，'用 Claude 治 ADHD 感到孤立缺问责'与'给 agent 加 human-in-the-loop 监督'本质都是在生成核心之外补上一层身体在场式的外部问责结构。"
problem: "为什么用 Claude 治 ADHD 的感到孤立缺问责，和给 agent 套 human-in-the-loop 监督 是一回事？"
spine: "人在回路与身体在场"
spineKind: ""
isEvolved: true
llmGenerated: true
isoStrength: "B"
caseStudies:
  - "张一鸣"
  - "胡林翼"
  - "Wesley White"
---
# 为什么用 Claude 治 ADHD 的感到孤立缺问责，和给 agent 套 human-in-the-loop 监督 是一回事？

> Claude 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。

用 Claude 整理任务、写日程、拆解目标，ADHD 用户常有的体验是：输出确实更快了，但执行却依旧漂浮。它像一位永远在线、从不抱怨的秘书，问题是——它也不盯着你。你让它列清单，它列；你让它改，它改；但它不会在你刷了三小时短视频之后，把屏幕扳过来说"现在做第 3 步"。这正是"孤立缺问责"的来源：AI 填满了认知劳动，却没有补上那个让行动落地的"外部身体在场"。

另一边，做 agentic harness 的工程师对这个困境并不陌生。一个 LLM 能生成一百个主意，却可能在多步任务里一步踏错、步步走偏。两边的核心问题其实是同一件事：**生成核心极强，执行调度层却极弱**。把 ADHD 大脑和 LLM 并列，不是修辞游戏，而是一种结构性的诊断。

## 同一套 bug：波动与缺层

ADHD 侧的真实表现是剧烈的日内波动。注意力、执行功能在不同时间点差异很大，诊断本身就需要多次捕捉这种波动性（来源：采样温度与表现波动）。这种波动并不只是"意志力不够"，而是大脑的生成系统缺少一个稳定的执行调度层。LLM 侧则是另一套波动：采样温度越高，输出越随机；温度再低，也无法消除非确定性（来源：采样温度与表现波动）。工程实践因此强调"确定性状态转换"，用计划-执行分离、状态机、预定义步骤来强制单向控制流（来源：采样温度与表现波动）。简言之：ADHD 用日程和提醒稳定表现，agent 用确定性工作流稳定输出。

## 同一套 harness：工具与认知卸载

工具证据两边都有。ADHD 用户用 Goblin Tools 把"清理厨房"这种模糊任务拆成可执行的子步骤，用"辣度"调节粒度，以降低启动门槛（来源：Goblin Tools）。Saner.AI 用本地记忆和知识回忆减少搜索循环与标签切换，对抗工作记忆不足（来源：Saner.AI）。Motion 则自动根据任务、会议和截止日期动态排程，消除"下一步该做什么"的决策负担，并在任务可能延期前数周发出警告（来源：Motion）。这些都不是"让大脑变聪明"，而是给大脑外挂一个执行调度层。

LLM/agent 侧的工具化思路几乎镜像。因为"单个 LLM 不足以可靠地完成多步骤任务、与业务工具交互或适应领域特定逻辑"，工程上引入 scaffold 来规划、调用工具、监控状态（来源：工具使用与认知卸载）。确定性工作流、周期性采样监控质量、知识图谱提升精度，本质上都是把 LLM 的生成冲动约束在一个可追踪的框架里（来源：采样温度与表现波动）。

## 同一套 human-in-the-loop：从人物案例到工程架构

这种同构在真实人物的 harness 系统里也能看到。张一鸣的 ADHD 特质是思维极度发散、永远在研究新东西、沉迷组织和产品；他的 harness 是延迟满足感、OKR 管理系统、Context not Control，用系统和文化而非个人集权来管公司（来源：人物案例）。这对应到 agent 工程，就是"外部调度器"：不是让 CEO（生成核心）即兴拍板，而是让 OKR 和流程（状态机、审批点）决定下一步。胡林翼年轻时放浪，后来以"每日写日记反省"做圣人功课，以"治私事之心治官事"严格治军（来源：人物案例）。他的"日课"对应 agent 的定时 re-grounding：不是信任生成核心实时自我调节

## 参考来源

**同构强度：B 级** —— 机制类比（ADHD 侧与 LLM/agent 侧均有真实文献，机制可映射）

- [ADHD Apps: We tested 44 Apps and Here're the Best 9 in 2026](https://blog.saner.ai/best-adhd-apps/) — 证据等级：低（GRADE）
- [12 AI Personal Assistants Built for ADHD Brains (2026 Rankings)](https://www.usecarly.com/blog/best-ai-personal-assistant-adhd/) — 证据等级：低（GRADE）
- [LBD同构对：自我调节与元认知 — Inhibitory control and emotion regulation in preschool child ↔ ObjexMT: Objective Extraction and Metacognitive Calibration ](https://doi.org/10.1016/j.cogdev.2007.08.002) — 证据等级：低（GRADE）
- [LBD同构对：自我调节与元认知 — Emotion-related self-regulation and its relation to children ↔ A Reproducibility Study of Metacognitive Retrieval-Augmented](https://doi.org/10.1146/annurev.clinpsy.121208.131208) — 证据等级：低（GRADE）
- [The 12 Best AI Tools for 2026 (That People Actually Use)](https://www.synthesia.io/post/ai-tools) — 证据等级：低（GRADE）
- [The AI Powered SuperApp for Work | Motion](https://www.usemotion.com/) — 证据等级：低（GRADE）

---

*本文是「ADHD × AI」系列的第 226 篇，由 AI 智能体从持续维护的 LLM Wiki（全网真实情报）中取材整合生成，并持续迭代更新。*
