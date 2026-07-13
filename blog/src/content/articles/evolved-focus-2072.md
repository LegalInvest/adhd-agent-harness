---
title: "为什么用 Motion 治 ADHD 的注意力涣散，和给 agent 套 上下文工程 是一回事？"
subtitle: "Motion 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
description: "Motion 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
date: "2025-04-15"
category: "专注力管理"
categoryId: "focus"
categoryEn: "Focus Management"
tags:
  - "ADHD"
  - "AI"
  - "专注力管理"
  - "反直觉同构"
  - "深度工作"
readingTime: 12
slug: "为什么用-motion-治-adhd-的注意力涣散和给-agent-套-上下文工程-是一回事"
topicId: "evolved-focus-2072"
angle: "反直觉同构"
rank: 160
score: 7.71
sourceCount: 6
toolsCited:
  - "Motion"
  - "Focusmate"
  - "Brain.fm"
  - "RescueTime"
  - "Forest"
thesis: "ADHD 大脑与 LLM 是同一类「高产但缺执行调度层的生成核心」，两者都需要外部脚手架（harness）来补偿调度缺陷，因此用 Motion 治注意力涣散与给 agent 套上下文工程在结构上完全同构。"
problem: "为什么用 Motion 治 ADHD 的注意力涣散，和给 agent 套 上下文工程 是一回事？"
spine: "上下文工程"
spineKind: ""
isEvolved: true
llmGenerated: true
caseStudies:
  - "曾国藩"
  - "孙策"
  - "颜淑华"
---
# 为什么用 Motion 治 ADHD 的注意力涣散，和给 agent 套 上下文工程 是一回事？

> Motion 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。

你打开 Motion，设置一个任务：“每周一三五，下午 3 点，写报告 45 分钟”。Motion 会自动排进日历，到点推送提醒，如果没完成，它会重新调度。你觉得它像一个靠谱的秘书，帮你把大脑里那团乱麻理成一条时间线。

但如果你换个角度——把 Motion 看作一个 **agent harness**，它做的事和工程师给 LLM 套的上下文工程一模一样：设置护栏（时间窗口）、注入外部记忆（日历）、加入重锚定（推送提醒）、通过人在回路（你确认完成）来防止目标漂移。

这不是比喻，这是同构。

## 同一个问题：高产但缺调度

ADHD 大脑的核心困境是什么？不是不聪明，不是没创意，而是 **执行功能缺陷**：工作记忆容量小，任务启动困难，注意力极易漂移。wiki 资料里说得好：ADHD 大脑是“高产但缺执行调度层的生成核心”（来源：AI 与 ADHD 的专注力）。你脑子里每秒能冒出 10 个想法，但一个都抓不住，就像一台 GPU 算力爆表却没有操作系统的电脑。

LLM 也一样。GPT-4 能写诗、写代码、解数学题，但如果你不给它任何指令结构，它会跑题、重复、陷入循环。Agent 直接调用 LLM 而不加 harness，就像让 ADHD 患者直接开始工作——灾难。

两边共享同一个底层问题：**生成能力强，调度能力弱**。

## 同一套解法：上下文工程

工程师怎么治 LLM 的“注意力涣散”？他们做的是 **上下文工程**：
- 设置 system prompt（相当于给 LLM 一个“日课十二条”）
- 限制 token 预算（防止上下文膨胀导致推理退化）
- 加入 human-in-the-loop 检查点（来源：人在回路与身体在场）
- 用工具调用（MCP）和外部记忆（RAG）来补偿无状态缺陷

ADHD 怎么治自己的注意力涣散？也是同一套：
- 曾国藩的 **日课十二条**：黎明即起、读书不二、谨言、写日记反省——这就是他的 system prompt。他 30 岁前浮躁坐不住，日记里天天骂自己“无恒”，但就是靠这套 rigid 的脚手架，把自己从一个“注意力不集中型ADHD”变成了半个圣人。
- 他的“结硬寨打呆仗”：像 token 预算一样，限制自己的冲动，不用奇谋，用最稳的方法。
- 一辈子写日记反省：像 agent 的遥测日志，每天回放自己的行为，修正偏差。

再看孙策：17 岁起兵，26 岁遇刺，9 年扫平江东。他坐不住，身先士卒，单骑出猎——典型的 ADHD 冲动型。他的 harness 是什么？用张昭张纮等文臣管行政，自己只负责打仗。这就是 **外部调度器**：把执行功能外包给靠谱的团队，自己只做最擅长的生成（打仗）。和 agent 架构里把工具调用交给 MCP、把记忆交给向量数据库，完全一样。

## 工具即脚手架

现在看具体的 AI 工具，它们本质上都是 **上下文工程的具体实现**：
- **Focusmate**：通过虚拟身体在场提供外部调度。你约一个时段，AI 匹配一个伙伴，你们同时在线工作。这不就是 human-in-the-loop 吗？伙伴的存在相当于一个“外部检查点”，防止你中途跑神（来源：Focusmate）。
- **Brain.fm**：用神经锁相技术生成专注音乐，帮助大脑进入状态。这相当于给 LLM 加一个“专注模式”的 system prompt，调整它的“激活函数”（来源：Brain.fm）。
- **RescueTime**：自动追踪时间，阻断分心网站。这就是 agent 的 **遥测与护栏**：实时监控行为，超出边界就干预（来源：RescueTime）。
- **Forest**：游戏化番茄钟，用多巴胺奖励来增强动机。这相当于给 agent 加一个 **reward model**，每次完成任务给一个 token 奖励（来源：AI 与 ADHD 的专注力）。

## 脚手架 vs 拐杖：边界在哪里

但这里有一个争议：这些工具是脚手架还是拐杖？wiki 资料明确警告：AI 工具可能成为永久依赖，阻碍执行功能的内化（来源：矛盾与存疑）。

我的判断是：**边界在于是否逐步内化**。曾国藩的日课十二条，他坚持了一辈子，但后来他不需要刻意提醒也能做到“黎明即起”——脚手架内化成了习惯。而 Motion 如果只是替你排日程，你从不自己规划，那它就是拐杖。

同样，agent harness 如果只是硬编码规则，agent 永远学不会自己调度，那它也是拐杖。好的 harness 应该在运行中让 agent 逐步学会如何管理上下文，比如通过反馈学习何时需要 re-grounding。

## 局限与诚实

必须承认，这个同构目前只是一个功能类比，缺乏神经科学层面的实证（来源：矛盾与存疑）。ADHD 大脑的神经机制（多巴胺调节异常、前额叶功能不足）与 LLM 的 transformer 架构是否有更深层的对应？不知道。但作为 **工程视角**，它极其有用：它告诉我们，治 ADHD 和调 agent 可以共用同一套方法论。

另外，现有工具的证据大多来自用户报告或小样本研究，缺乏大规模 RCT（来源：AI 与 ADHD 的专注力）。Brain.fm 在 2026 年一项 44 款 ADHD 应用测试中位列最佳 9 款之一，但独立临床证据仍有限（来源：Brain.fm）。Focusmate 的效果与身体在场效应一致，但 AI 是否真的能替代真人互动？存疑。

## 今天就能试的行动

1. **给自己设一个“日课十二条”**：每天固定 3-5 件必须做的事，写在 Motion 或日历里，定时推送提醒。这就是你的 system prompt。
2. **用 Focusmate 做一次 body doubling session**：约 25 分钟，和陌生人一起工作。感受一下“外部调度器”的效果。
3. **打开 RescueTime 的自动追踪**：看一周报告，识别你的“上下文膨胀”点（比如刷社交媒体的时间）。然后设置阻断规则。
4. **如果写代码或做 agent 项目**：给你的 LLM 调用加上 token 预算和 human-in-the-loop 检查点。不要让它无限生成。

你不是“懒”或“笨”，你只是一个缺调度层的生成核心。而 harness，你自己可以造。

## 参考来源

- [ADHD Apps: We tested 44 Apps and Here're the Best 9 in 2026](https://blog.saner.ai/best-adhd-apps/) — 证据等级：低（GRADE）
- [Meta-Analysis of fMRI Studies of Disruptive Behavior Disorders](https://doi.org/10.1176/appi.ajp.2016.15081089) — 证据等级：高（GRADE）
- [Nonlinear Complexity Analysis of Brain fMRI Signals in Schizophrenia](https://doi.org/10.1371/journal.pone.0095146) — 证据等级：低（GRADE）
- [Revolutionizing ADHD Management with AI Assistants](https://neurolaunch.com/adhd-ai-assistant/) — 证据等级：低（GRADE）
- [DeepSeek - AI Assistant - Apps on Google Play](https://play.google.com/store/apps/details?id=com.deepseek.chat) — 证据等级：低（GRADE）
- [AI Assistant for ADHD: Finally, a Productivity Tool That Requires Less...](https://get-alfred.ai/blog/ai-assistant-for-adhd) — 证据等级：低（GRADE）

---

*本文是「ADHD × AI」系列的第 321 篇，由 AI 智能体从持续维护的 LLM Wiki（全网真实情报）中取材整合生成，并持续迭代更新。*
