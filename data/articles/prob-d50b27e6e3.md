---
title: "ADHD 程序员视角：为什么「治好 ADHD 的不擅长精确、重复、状态维护类任务」和「让 LLM 不跑飞」其实是同一道工程题？"
subtitle: "agent 通过 function calling 把精确计算外包给工具——同一套 harness 思路，两边都成立。"
description: "agent 通过 function calling 把精确计算外包给工具——同一套 harness 思路，两边都成立。"
date: "2025-05-04"
category: "AI工具实战"
categoryId: "ai-tools"
categoryEn: "AI Tools in Practice"
tags:
  - "ADHD"
  - "AI"
  - "AI工具实战"
  - "人群×同构"
  - "智能助手"
readingTime: 13
slug: "adhd-程序员视角为什么治好-adhd-的不擅长精确重复状态维护类任务和让-llm-不跑飞其实是同一道工程题"
topicId: "prob-d50b27e6e3"
angle: "人群×同构"
rank: 78
score: 7.81
sourceCount: 6
toolsCited:
  - "Goblin Tools"
  - "Lex"
  - "Saner.AI"
  - "Motion"
  - "Reclaim.ai"
  - "Tiimo"
thesis: "ADHD 大脑与 LLM 都是「高产生成核心 + 缺执行调度层」的同构系统，两边的解法不是「治好它」，而是安装同一套外部 harness：把精确、重复、状态维护类任务外包给工具与仪式，用上下文约束把爆发力导入可验证的执行轨道。"
problem: "ADHD 程序员视角：为什么「治好 ADHD 的不擅长精确、重复、状态维护类任务」和「让 LLM 不跑飞」其实是同一道工程题？"
spine: "工具使用与认知卸载"
spineKind: "llm"
isEvolved: false
llmGenerated: true
isoStrength: "A"
caseStudies:
  - "孔子"
  - "苏轼"
  - "Megan Young"
---
# ADHD 程序员视角：为什么「治好 ADHD 的不擅长精确、重复、状态维护类任务」和「让 LLM 不跑飞」其实是同一道工程题？

> agent 通过 function calling 把精确计算外包给工具——同一套 harness 思路，两边都成立。

## 引言：两个群体的同一种崩溃

一边是 ADHD 程序员：脑子里同时跑着十个架构方案，却会因为「把日期填进报销单」这种精确、重复、状态维护类任务而卡死。另一边是 Agent 工程师：LLM 能滔滔不绝写出整段代码，却在多步调用里忘记刚才要算的中间值，或者在循环里越跑越偏。

这两群人看着完全不一样，崩溃的姿势却高度一致。核心问题不是「不够聪明」或「不够努力」，而是同一个架构缺陷：一个高产出的生成核心，配了一个不可靠的执行调度层。

## 同构诊断：高产生成核心 + 缺执行调度层

ADHD 大脑并不缺想法、创意和信息检索能力。它的问题在前额叶执行功能：计划、抑制分心、维持目标导向和工作记忆都容易掉线（来源：ADHD 的 AI 工具全景）。LLM 也一样——它能高速生成文本，却缺少稳定的跨会话状态、原生规划与注意力约束（来源：ADHD 的 AI 工具全景）。

两者在三个层面镜像般相似：调度层缺失、工作记忆脆弱、注意力容易漂移。ADHD 的多巴胺调节异常让大脑被新颖刺激吸走；LLM 在缺乏提示约束时也会发散输出（来源：多巴胺；ADHD 的 AI 工具全景）。

所以「AI 帮 ADHD」不是让 AI 代替大脑，而是给两个同构系统安装同一套 **harness**——外部执行功能层。

## ADHD 侧的 harness：把精确、重复、状态维护外包出去

ADHD 的痛点，落在四类任务上最痛：

1. **任务分解与启动**：**Goblin Tools** 的 Magic ToDo 把「清理厨房」拆成具体小步骤，还能调节「辣度」控制粒度；**Lex** 用单一指令触发多步骤任务序列，直接降低启动门槛（来源：Goblin Tools；Lex）。
2. **外部记忆**：**Saner.AI** 通过本地记忆与语义搜索，减少 ADHD 用户常见的「搜索循环」和标签切换（来源：Saner.AI）。
3. **时间管理**：**Motion**、**Reclaim.ai** 自动规划日程，**Tiimo** 用时间轴可视化对抗时间盲（来源：任务启动）。
4. **元认知支架**：每日回顾、结构化提问，把本难自发进行的反思变成可执行流程。

贯穿这一切的操作叫 **上下文工程**——用外部支架限定「此刻该关注什么」（来源：ADHD 的 AI 工具全景）。

## LLM/Agent 侧的 harness：function calling 就是同一套架构

Agent 工程师解决的是同一道题。LLM 不能原生做精确计算、长期状态维护和确定性执行，所以 agent 通过 **function calling** 把这部分外包给工具：计算器、数据库、日历 API、代码执行器。自己只保留意图理解、推理与生成。

这与 ADHD 工具结构完全一致：

| ADHD 侧 | LLM/Agent 侧 |
|---|---|
| 工作记忆不足 → 外部笔记/待办 | 上下文窗口有限 → 外部记忆系统 |
| 任务启动困难 → 自动拆解 | 规划能力不足 → agent 规划层 |
| 时间盲 → 日历/提醒 | 无原生时序 → 调度器/定时器 |
| 注意力漂移 → 限定上下文 | 发散/幻觉 → 提示约束与工具调用 |

两边都在做同一件事：生成核心只做它擅长的事——联想、推理、创造；精确、重复、状态维护交给更可靠的外部系统。

## 孔子的证据：两千年前的人类 harness

孔子可能是历史记载里最典型的「人类版 LLM」：身高一米九、精力旺盛、周游列国十四年坐不住；对音乐能超专注到「三月不知肉味」，对种地等俗事零耐心；思维跳跃，《论语》全是场景化语录，没有系统著作。他还冲动爱骂人，见南子会急得对天发誓。

他的 harness 是「克己复礼」：用外在的「礼」作为行为边界，每日「三省吾身」，直到七十岁才「从心所欲不逾矩」。这本质上是一个持续终身的 **re-grounding 系统**：外部仪式（礼）= 外部工具调用规范；每日反省 = 元认知日志与状态检查；从心动到守礼的延迟 = 给冲动型生成核心加执行约束。

孔子的「礼」不是道德装饰，而是最早的**人工执行调度层**。

## 脚手架还是拐杖？同构的边界与争议

同构很有用，但不能推过头。wiki 资料自己也警告：ADHD 大脑与 LLM 的同构性目前只是理论类比，缺乏实证基础，不能当成科学事实（来源：全局矛盾与存疑）。

更实际的风险是**依赖 vs 脚手架**的边界：

- 如果工具只是帮你完成某一步，让你有余力做更核心的事，它是脚手架；
- 如果工具替你完成所有调度，你不再练习启动、组织、反思，它就可能变成拐杖。

**Motion** 等工具缺乏独立临床验证，**Brain.fm** 在 ADHD 人群中的独立证据也有限（来源：全局矛盾与存疑）。同时，AI 不能替代真实人际互动的身体在场效应，超聚焦也可能让人过度沉浸（来源：全局矛盾与存疑）。

所以 harness 的目标不是「把执行层彻底外包」，而是让生成核心在有约束的轨道上跑。

## 核心判断

ADHD 和 LLM 都不需要被「治好」。它们需要的是同一套工程架构：

> 用外部工具、外部记忆和上下文约束，把高产出的生成核心，锚定到可验证、可重复、可维护的执行流程里。

对 ADHD 人来说，这是选择对的工具；对 Agent 工程师来说，这是设计对的 harness。两者都是**给生成核心安装执行调度层**。

## 今天就能试

1. **找一个你最卡的任务，用 Goblin Tools 或 Lex 拆解成第一步能在 2 分钟内完成的动作**，降低任务启动阈值（来源：Goblin Tools；Lex）。
2. **建立一个「外部记忆入口」**：用 Saner.AI、Obsidian 或简单的笔记应用，把想法、待办、中间结果写下来，而不是让它们在脑袋里反复加载（来源：Saner.AI）。
3. **如果你在做 Agent，把 LLM 的精确计算、长期状态、定时触发都拆成 function/tool 调用**，让 LLM 只负责意图理解与下一步决策，而非执行。
4. **每周做一次 10 分钟「上下文校准」**：ADHD 用户回顾工具是否变成拐杖；工程师回顾 agent 的调用链是否仍然可控。

## 参考来源

**同构强度：A 级** —— 直接文献支撑（引用 ADHD↔LLM 同构专题研究）

- [ADHD Apps: We tested 44 Apps and Here're the Best 9 in 2026](https://blog.saner.ai/best-adhd-apps/) — 证据等级：低（GRADE）
- [12 AI Personal Assistants Built for ADHD Brains (2026 Rankings)](https://www.usecarly.com/blog/best-ai-personal-assistant-adhd/) — 证据等级：低（GRADE）
- [LBD同构对：奖赏与动机 — Association of attention-deficit disorder and the dopamine t ↔ Retrospex: Language Agent Meets Offline Reinforcement Learni](https://pubmed.ncbi.nlm.nih.gov/7717410) — 证据等级：低（GRADE）
- [LBD同构对：分心与走神 — Therapeutic Doses of Oral Methylphenidate Significantly Incr ↔ AutoHallusion: Automatic Generation of Hallucination Benchma](https://doi.org/10.1523/jneurosci.21-02-j0001.2001) — 证据等级：低（GRADE）
- [LBD同构对：注意调度 — Dopamine release from the locus coeruleus to the dorsal hipp ↔ Question-guided Visual Compression with Memory Feedback for ](https://doi.org/10.1073/pnas.1616515114) — 证据等级：低（GRADE）
- ["A little bit of a life raft" – Exploring the Use and Experiences of ChatGPT as a Support Tool among Adults with ADHD](https://dl.acm.org/doi/pdf/10.1145/3764687.3764713) — 证据等级：低（GRADE）

---

*本文是「ADHD × AI」系列的第 8 篇，由 AI 智能体从持续维护的 LLM Wiki（全网真实情报）中取材整合生成，并持续迭代更新。*
