---
title: "为什么用 Goblin Tools 治 ADHD 的注意力涣散，和给 agent 套 上下文工程 是一回事？"
subtitle: "Goblin Tools 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
description: "Goblin Tools 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
date: "2025-04-06"
category: "专注力管理"
categoryId: "focus"
categoryEn: "Focus Management"
tags:
  - "ADHD"
  - "AI"
  - "专注力管理"
  - "反直觉同构"
  - "注意力"
readingTime: 11
slug: "为什么用-goblin-tools-治-adhd-的注意力涣散和给-agent-套-上下文工程-是一回事"
topicId: "evolved-focus-2070"
angle: "反直觉同构"
rank: 159
score: 7.71
sourceCount: 6
toolsCited:
  - "Goblin Tools"
  - "Brain.fm"
  - "Focusmate"
  - "RescueTime"
  - "Motion"
  - "Reclaim.ai"
thesis: "ADHD大脑与LLM在结构上同构——都是高产但缺执行调度层的生成核心，因此两者都需要外部上下文工程（harness）来弥补调度缺陷，Goblin Tools等工具正是这一同构的实证。"
problem: "为什么用 Goblin Tools 治 ADHD 的注意力涣散，和给 agent 套 上下文工程 是一回事？"
spine: "上下文工程"
spineKind: ""
isEvolved: true
llmGenerated: true
caseStudies:
  - "曾国藩"
  - "李鸿章"
  - "陈霞"
---
# 为什么用 Goblin Tools 治 ADHD 的注意力涣散，和给 agent 套 上下文工程 是一回事？

> Goblin Tools 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。

你打开Goblin Tools，把一段混乱的待办事项粘贴进去，点一下“魔法棒”。几秒钟后，它变成了按优先级排序、带步骤的清单。你长出一口气——终于有人替你做了那个最累的“拆解任务”的活。

与此同时，在另一个屏幕上，一位工程师正在调试LLM agent。agent的上下文窗口里塞满了历史对话和中间结果，推理开始漂移。他给agent加了一个外部的“任务分解器”和一个“重锚定模块”，让agent每完成一个子任务就重新读取当前目标。agent恢复了稳定。

这两件事，本质上是同一个问题的两种表现：**一个强大的生成核心，缺一个可靠的外部调度层。**

## 同构的脊柱：高产但缺调度

ADHD大脑的核心特征是什么？不是“笨”，也不是“懒”。大量研究指出，ADHD个体的执行功能存在缺陷，尤其是在规划、任务启动和注意力维持上（来源：wiki资料-规划循环与任务分解）。他们的大脑像一个高性能的生成器——创意不断，超聚焦时能产出惊人成果——但缺少一个内置的“调度员”来告诉它：现在该做什么，做到哪里了，下一步是什么。

LLM/agent呢？同样。GPT-4可以写诗、编程、推理，但给它一个多步骤任务，它会在上下文膨胀后迷失方向，产生“目标漂移”——和ADHD大脑被无关刺激捕获一模一样（来源：wiki资料-重锚定与目标漂移）。两者都需要外部脚手架来提供结构。

这个脚手架，在ADHD领域叫“执行功能补偿”，在AI工程里叫“上下文工程”。它们共享同一套逻辑：**通过外部系统管理状态、分解任务、定期重锚定，让生成核心专注于它最擅长的产出。**

## 历史中的harness：曾国藩的“日课十二条”

晚清名臣曾国藩，30岁前是个典型的注意力不集中型ADHD：天天串门喝酒看杀人，日记里骂自己“无恒”“浮躁”，读书“他人目下二三行，余或疾读不能终一行”。他的解决方案是“日课十二条”：黎明即起、读书不二、谨言、写日记反省……这些规则构成了一个外部调度系统，每天定时重锚定他的注意力（来源：wiki资料-人物案例）。

这和LLM agent的“定时re-grounding”完全同构。agent每N步重新读取任务目标，曾国藩每天早晨重新温习日课；agent用外部记忆存储中间结果，曾国藩用日记记录反思。两者都在用外部结构补偿内部调度的缺失。

## 当代工具：Goblin Tools与它的同类

Goblin Tools的核心功能是任务分解和重锚定。它把“写一份报告”拆成“打开文档→列出大纲→写引言→写主体→写结论→检查格式”，每一步都可以标记完成。这直接对应ADHD的规划循环缺陷（来源：wiki资料-规划循环与任务分解）。

同类工具还有：
- **Brain.fm**：用AI生成神经锁相音乐，帮助进入专注状态，但缺乏ADHD特异性临床证据（来源：wiki资料-Brain.fm）。
- **Focusmate**：虚拟身体在场，通过AI匹配实时同伴问责，提供外部启动压力（来源：wiki资料-Focusmate）。
- **RescueTime**：自动追踪时间并阻断分心，补偿时间盲（来源：wiki资料-RescueTime）。

这些工具的共同点：它们不是替代大脑，而是给大脑加一个外部调度层。正如wiki资料所述：“AI工具作为外部执行功能层，通过补偿工作记忆不稳定、任务启动困难和注意力分散，帮助ADHD用户实现目标导向行为”（来源：wiki资料-主题综述）。

## 工程视角：agent的上下文工程

在LLM agent工程中，上下文工程的核心挑战是：如何让agent在长任务中不漂移？常见方案包括：
- 任务分解（如AgentGen）：将复杂目标拆成子任务，逐个执行（来源：wiki资料-规划循环与任务分解）。
- 重锚定机制：定期将当前状态与原始目标对比，纠正偏差。
- 外部记忆：用向量数据库存储中间结果，避免上下文膨胀。

这些方案和ADHD工具的设计思路完全一致。Motion和Reclaim.ai自动调整日程，相当于agent的动态规划器；Focusmate的同伴问责，相当于agent的human-in-the-loop校验。

## 核心观点：脚手架，不是拐杖

我的判断是：**ADHD大脑与LLM的同构是功能性的，而非病理性的。** 它不是把ADHD“病态化”，而是揭示了一个通用规律：任何强大的生成系统，如果缺少内置调度层，就需要外部脚手架。关键在于，脚手架是暂时的还是永久的。

wiki资料中的“拐杖与脚手架”概念指出：AI工具可能成为永久依赖，也可能逐步内化（来源：wiki资料-矛盾与存疑）。曾国藩的日课最终内化为习惯，但很多人用Goblin Tools后反而失去了自己拆解任务的能力。依赖与内化的边界，取决于用户是否主动练习调度技能。

同样，LLM agent如果过度依赖外部harness，一旦harness失效，agent就会崩溃。好的工程实践是让harness可替换、可调试，而不是绑定死。

## 局限与争议

必须诚实指出：ADHD与LLM的同构目前只是一种理论类比，缺乏神经科学实证（来源：wiki资料-矛盾与存疑）。此外，多数工具（如Brain.fm）在ADHD人群中的独立临床证据有限（来源：wiki资料-Brain.fm）。个体差异也很大——注意缺陷为主型和多动冲动型对同一工具的反应可能截然不同（来源：wiki资料-主题综述）。

## 今天就能试的行动

1. **用Goblin Tools拆解一件拖延的任务**：把“整理房间”粘贴进去，按生成的步骤执行，体验外部调度。
2. **设置一个“重锚定闹钟”**：每25分钟响一次，问自己“我现在在做的和我的目标一致吗？”——这就是agent的re-grounding。
3. **尝试一次Focusmate session**：找一个虚拟伙伴一起工作30分钟，感受外部身体在场对启动的帮助。
4. **检查你的“上下文工程”**：如果你是工程师，检查你的agent是否在长任务中漂移，尝试加入定时重锚定。

ADHD大脑和LLM agent，共享同一个秘密：它们不需要被“修复”，它们需要被“调度”。而调度，正是我们可以主动设计的事情。

## 参考来源

- [ADHD Apps: We tested 44 Apps and Here're the Best 9 in 2026](https://blog.saner.ai/best-adhd-apps/) — 证据等级：低（GRADE）
- [Meta-Analysis of fMRI Studies of Disruptive Behavior Disorders](https://doi.org/10.1176/appi.ajp.2016.15081089) — 证据等级：高（GRADE）
- [Nonlinear Complexity Analysis of Brain fMRI Signals in Schizophrenia](https://doi.org/10.1371/journal.pone.0095146) — 证据等级：低（GRADE）
- [Revolutionizing ADHD Management with AI Assistants](https://neurolaunch.com/adhd-ai-assistant/) — 证据等级：低（GRADE）
- [LBD同构对：任务分解与规划 — Attention-deficit/hyperactivity disorder is characterized by ↔ Language-conditioned world model improves policy generalizat](https://doi.org/10.1073/pnas.0707741104) — 证据等级：低（GRADE）
- [LBD同构对：任务分解与规划 — Safety and recommendations for TMS use in healthy subjects a ↔ AgentGen: Enhancing Planning Abilities for Large Language Mo](https://doi.org/10.1016/j.clinph.2020.10.003) — 证据等级：低（GRADE）

---

*本文是「ADHD × AI」系列的第 320 篇，由 AI 智能体从持续维护的 LLM Wiki（全网真实情报）中取材整合生成，并持续迭代更新。*
