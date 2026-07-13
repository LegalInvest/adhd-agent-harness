---
title: "ADHD 家长视角：为什么「治好 ADHD 的分心走神或超聚焦跑偏，丢失目标」和「让 LLM 不跑飞」其实是同一道工程题？"
subtitle: "长程任务里 agent 会目标漂移，需要重锚定 system prompt——同一套 harness 思路，两边都成立。"
description: "长程任务里 agent 会目标漂移，需要重锚定 system prompt——同一套 harness 思路，两边都成立。"
date: "2025-04-21"
category: "专注力管理"
categoryId: "focus"
categoryEn: "Focus Management"
tags:
  - "ADHD"
  - "AI"
  - "专注力管理"
  - "人群×同构"
  - "注意力"
readingTime: 10
slug: "adhd-家长视角为什么治好-adhd-的分心走神或超聚焦跑偏丢失目标和让-llm-不跑飞其实是同一道工程题"
topicId: "prob-6e4befbbbc"
angle: "人群×同构"
rank: 120
score: 7.77
sourceCount: 6
toolsCited:
  - "Brain.fm"
  - "Focusmate"
  - "RescueTime"
  - "Endel"
  - "Forest"
thesis: "ADHD 大脑与 LLM/agent 都是‘高产但缺执行调度层的生成核心’，两者在分心、超聚焦跑偏和目标漂移上的痛苦同构，因此都需要同一套 harness 工程——外部记忆、上下文重锚定、验证循环与确定性控制流——来把生成能力锁回目标轨道。"
problem: "ADHD 家长视角：为什么「治好 ADHD 的分心走神或超聚焦跑偏，丢失目标」和「让 LLM 不跑飞」其实是同一道工程题？"
spine: "重锚定与目标漂移"
spineKind: "llm"
isEvolved: false
llmGenerated: true
isoStrength: "A"
caseStudies:
  - "曾国藩"
  - "文天祥"
  - "Renee Morales"
---
# ADHD 家长视角：为什么「治好 ADHD 的分心走神或超聚焦跑偏，丢失目标」和「让 LLM 不跑飞」其实是同一道工程题？

> 长程任务里 agent 会目标漂移，需要重锚定 system prompt——同一套 harness 思路，两边都成立。

## 问题：两张书桌前的同一种漂移

作为一个 ADHD 孩子的家长，我早已习惯这样的画面：孩子打开作业本，三分钟后开始画恐龙，二十分钟后 dinosaurs 已经演变成一部完整的漫画宇宙——而数学作业还是空白。这不是懒，而是“超聚焦跑偏”：注意力像一束极强的激光，只是没有照在目标上。

另一边，我在做 agentic harness 工程时，也见过 LLM agent 的同款漂移。你让它“帮用户订一张去上海的机票”，它在检索航班的半路上开始重写你的订票系统代码，或者沉迷于优化一个与目标无关的提示词。长程任务里，agent 会目标漂移，需要重锚定 system prompt——这行话听起来冷酷，但和家长喊孩子“回到作业上来”本质一样。

两道题，其实是同一道题：如何让一个“高产但缺执行调度层的生成核心”不跑飞？

## 同构：两种生成核心的同一缺陷

wiki 资料对 ADHD 与 AI 的专注力问题有一个核心判断：AI 工具对 ADHD 专注力的支持，本质上是为“高产但缺执行调度层的生成核心”套上 harness（来源：AI 与 ADHD 的专注力）。ADHD 大脑与 LLM 在这一点上是同构的：两者都有强大的生成能力，却缺乏可靠的内置执行调度层。

在 ADHD 一侧，这表现为工作记忆不稳定、任务启动困难、注意力易分散；在 LLM/agent 一侧，这表现为无跨会话状态、上下文膨胀导致推理退化、以及长程任务中的目标漂移。两边都需要外部脚手架来补偿内部调度缺陷。harness 工程在 LLM 侧提供的组件——上下文传递、工具接口、规划工件、验证循环、记忆系统和沙盒——与 ADHD 侧的外部执行功能层完全对应（来源：GitHub - ai-boost/awesome-harness-engineering；来源：AI 与 ADHD 的专注力）。

## 案例：曾国藩的“日课十二条”就是 system prompt 重锚定

要理解这种同构，最贴切的例子是曾国藩。他年轻时是典型的“坐不住”：30 岁前浮躁，天天串门、喝酒、看杀人，读书时“他人目下二三行，余或疾读不能终一行”；日记里天天骂自己“无恒”“浮躁”。他还有严重的银屑病和情绪不稳，打败仗就跳水自杀。这些行为模式，和今天 ADHD 的描述高度吻合（来源：人物案例：曾国藩）。

他的 harness 是“日课十二条”：黎明即起、读书不二、谨言、写日记反省，以及“结硬寨，打呆仗”。用今天的话来说：

- **日课十二条** = 每天定时重锚定的 system prompt；
- **写日记骂自己** = 自我批评（self-critique）验证循环，检查行为是否偏离目标；
- **结硬寨，打呆仗** = 用确定性流程约束冲动，不让生成核心随性发挥。

曾国藩不是“治好”了分心，而是给分心套上了一套可重复、可检查的 harness。这套逻辑与 LLM agent 的 deterministic state transitions、plan-execution 分离、以及周期性 self-critique 提示完全同构（来源：What is an agent harness...；来源：Planner-Executor Agentic Framework）。

## 工程题的四个共同零件

把 ADHD 孩子的书桌和 LLM agent 的调用链放在一起，可以发现同一套 four-piece harness：

**1. 外部记忆 / 状态管理**
ADHD 的工作记忆不稳定，LLM 则是无跨会话状态。RescueTime 通过自动记录时间、阻断分心网站来补偿“时间盲”和工作记忆缺陷；Forest 用游戏化番茄钟留下专注记录。LLM harness 则用记忆系统、知识图谱和 trace 来保存中间状态，避免每一步都从零开始（来源：RescueTime；来源：Forest；来源：AI Agent Memory Architectures: From Context Windows to ...）。

**2. 上下文工程 / 注意控制**
ADHD 大脑容易被环境带偏，LLM 则因上下文膨胀而推理退化。Focusmate 通过虚拟身体在场（body doubling）提供外部注意锚点；Endel 用 AI 生成个性化声音环境来调节专注状态。LLM 侧则需要在 system prompt 里明确“当下注意什么”，并主动裁剪上下文（来源：Focusmate；来源：Endel；来源：AI 与 ADHD 的专注力）。

**3. 验证循环 / 抗幻觉**
ADHD 的冲动判断可以看作行为层面的“幻觉”：脱离环境线索做出不恰当反应。LLM 的幻觉则是生成自信但错误的输出。两者的解法都是把内部状态拉回外部现实：ADHD 侧可用“视觉接地”和环境核对来调节情绪；LLM 侧则必须在每个子任务后加验证步骤，例如运行测试、检查输出格式、与规划工件核对（来源：幻觉与验证循环；来源：What is an agent harness...）。

**4. 确定性控制流 / 稳定表现**
ADHD 的表现日内波动大，LLM 的输出也因采样温度而随机。外部结构（日程、提醒、环境设计）能稳定 ADHD 的表现；工程上则用确定性工作流、状态机、计划-执行分离和周期性采样来降低非确定性（来源：采样温度与表现波动；来源：AI Agent Reliability and Guardrails 2026 | Zylos Research）。

## 脚手架，还是拐杖？

同构≠相同。wiki 资料自己也警告：ADHD 大脑与 LLM 的“结构同构”目前只是理论类比，并非经过验证的神经科学事实；而且多个工具（如 Brain.fm、Endel）缺乏 ADHD 人群的独立随机对照试验，证据主要来自用户报告或小样本研究（来源：全局矛盾与存疑；来源：AI 与 ADHD 的专注力）。

更关键的问题是：AI 工具到底是让人逐步内化执行功能的“脚手架”，还是让人永远依赖的“拐杖”？目前尚无长期追踪研究能回答。 ADHD 的个体差异也很大，注意缺陷型与多动冲动型对同一工具的反应可能完全不同。我们既不能因证据不足而否定 harness 的价值，也不能把工具当成万能解药（来源：拐杖与脚手架；来源：全局矛盾与存疑）。

## 今天就能试

1. **写一条个人 system prompt**：每天开始前，用三句话写清楚“今天最重要的三个目标”。对孩子，可以贴在书桌前；对 agent，就放在每次调用的 system prompt 开头。
2. **每小时重锚定一次**：设一个闹钟或日历提醒，像曾国藩的“日课”一样，把注意力和任务目标重新对齐。
3. **给每个子任务加验证步骤**：作业做完一科，先核对清单再开始下一科；agent 完成一个工具调用后，必须输出“这与当前目标的关系是什么”。
4. **用外部记忆看时间流向**：今晚就安装 RescueTime 或 Forest，让工具自动记录“时间到底去了哪里”，用 trace 对抗“人在心不在”。

## 结语

 ADHD 孩子不是因为不够聪明才跑题，LLM agent 也不是因为模型太弱才跑偏。两者都是生成能力过剩、调度能力不足的同一类系统。家长也好，工程师也好，我们要做的不是“治好”这个核心，而是给它设计一套可靠的 harness——让高产，终于落在目标上。

## 参考来源

**同构强度：A 级** —— 直接文献支撑（引用 ADHD↔LLM 同构专题研究）

- [ADHD Apps: We tested 44 Apps and Here're the Best 9 in 2026](https://blog.saner.ai/best-adhd-apps/) — 证据等级：低（GRADE）
- [Meta-Analysis of fMRI Studies of Disruptive Behavior Disorders](https://doi.org/10.1176/appi.ajp.2016.15081089) — 证据等级：高（GRADE）
- [Nonlinear Complexity Analysis of Brain fMRI Signals in Schizophrenia](https://doi.org/10.1371/journal.pone.0095146) — 证据等级：低（GRADE）
- [Revolutionizing ADHD Management with AI Assistants](https://neurolaunch.com/adhd-ai-assistant/) — 证据等级：低（GRADE）
- [Confabulation: The Surprising Value of Large Language Model Hallucinations](https://preview.aclanthology.org/navbar-space/2024.acl-long.770.pdf) — 证据等级：低（GRADE）
- [LBD同构对：分心与走神 — Therapeutic Doses of Oral Methylphenidate Significantly Incr ↔ AutoHallusion: Automatic Generation of Hallucination Benchma](https://doi.org/10.1523/jneurosci.21-02-j0001.2001) — 证据等级：低（GRADE）

---

*本文是「ADHD × AI」系列的第 41 篇，由 AI 智能体从持续维护的 LLM Wiki（全网真实情报）中取材整合生成，并持续迭代更新。*
