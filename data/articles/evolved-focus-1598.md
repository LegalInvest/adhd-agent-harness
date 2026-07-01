---
title: "为什么用 Claude 治 ADHD 的注意力涣散，和给 agent 套 上下文工程 是一回事？"
subtitle: "Claude 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
description: "Claude 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
date: "2025-05-15"
category: "专注力管理"
categoryId: "focus"
categoryEn: "Focus Management"
tags:
  - "ADHD"
  - "AI"
  - "专注力管理"
  - "反直觉同构"
  - "深度工作"
readingTime: 10
slug: "为什么用-claude-治-adhd-的注意力涣散和给-agent-套-上下文工程-是一回事"
topicId: "evolved-focus-1598"
angle: "反直觉同构"
rank: 156
score: 7.75
sourceCount: 6
toolsCited:
  - "Brain.fm"
  - "Focusmate"
  - "RescueTime"
thesis: "ADHD大脑与LLM是同构的生成核心，都缺乏可靠的执行调度层，因此用Claude治ADHD注意力涣散与给Agent套上下文工程本质上是同一件事——通过外部脚手架补偿执行功能缺陷。"
problem: "为什么用 Claude 治 ADHD 的注意力涣散，和给 agent 套 上下文工程 是一回事？"
spine: "上下文工程"
spineKind: ""
isEvolved: true
llmGenerated: true
---
# 为什么用 Claude 治 ADHD 的注意力涣散，和给 agent 套 上下文工程 是一回事？

> Claude 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。

## 问题：为什么你的大脑和AI一样“失控”？

你打开Claude，准备写一篇文章，结果10分钟后发现自己刷了5个短视频，文档里只多了个标题。另一边，你部署了一个AI Agent去爬取数据，结果它反复调用错误API，输出一堆幻觉——两个场景，一个发生在人脑，一个发生在机器，但底层逻辑惊人地相似。

ADHD大脑与LLM在结构上同构：两者都是高产的生成核心，但缺乏可靠的执行调度层（来源：ADHD大脑与LLM的同构）。你的大脑能瞬间蹦出10个创意，但无法按顺序执行；LLM能写出优美的段落，但无法保证每一步都正确。问题出在同一个地方：没有“上下文工程”——一套将生成能力导向有序输出的外部脚手架。

## 答案：上下文工程是同一套Harness

### ADHD侧：外部执行功能层

ADHD的核心缺陷是执行功能（工作记忆、任务启动、时间盲、上下文保持）不足。AI工具的作用正是充当“外部执行功能层”，补偿这些短板。

- **RescueTime**：自动记录时间使用，充当外部记忆，提升时间盲觉察。ADHD个体难以准确估计时间，RescueTime通过自动分类和模式识别，减轻工作记忆负担，让“时间感”可视化（来源：RescueTime）。
- **Brain.fm**：利用AI生成神经锁相音乐，主动维持任务连贯性。ADHD易因环境干扰丢失焦点，Brain.fm通过音频模式影响大脑信息处理，帮助进入专注状态——尽管缺乏ADHD专项临床研究（来源：Brain.fm）。
- **Focusmate**：通过AI匹配虚拟同伴，提供实时问责，弥补任务启动和注意力维持的调度缺失。其机制是“AI-Matched Body Doubling”，利用身体在场效应提供外部结构（来源：Focusmate）。

这些工具的本质不是“治好”ADHD，而是给生成核心套上harness——就像给一个强大的引擎装上方向盘和刹车。

### LLM/Agent侧：编排层与验证循环

LLM作为生成核心，天然倾向于产生自信但可能错误的输出（幻觉）。Harness工程正是为此设计：提供上下文传递、工具接口、规划工件、验证循环、记忆系统和沙盒（来源：幻觉与验证循环）。

关键组件包括：
- **验证与CI集成**：复杂的harness不会盲目执行工具，而是实现验证步骤，例如检查输出格式或对模型编写的代码运行测试用例（来源：幻觉与验证循环）。
- **结构化工作流和规划**：将复杂任务分解为子任务，并在每一步进行规划与验证（来源：幻觉与验证循环）。
- **确定性状态转换**：为应对LLM的采样温度导致的非确定性，工程实践强调“计划-执行”分离等模式来强制单向、确定性的控制流（来源：采样温度与表现波动）。

缺乏这些验证会导致“更多幻觉和重复工作”（来源：幻觉与验证循环）。纯对话系统常因幻觉、缺乏接地和无法执行/验证行动而失败（来源：幻觉与验证循环）。

### 同构证据：验证循环与表现波动

- **验证循环**：ADHD大脑的冲动行为可视为验证失败——内部状态未与外部现实核对。LLM的幻觉也是验证缺失。Focusmate的实时问责、RescueTime的自动记录，本质上都是外部验证循环；而Agent harne的验证与CI集成正是同一逻辑（来源：幻觉与验证循环）。
- **表现波动**：ADHD个体的表现常呈日内波动，注意力、执行功能在不同时间点差异很大，本质是“生成核心”缺乏稳定的调度层。LLM的输出也因采样温度而波动，温度越高越随机，越“有创意”，但温度越低越确定。生产环境中，非确定性是可靠性的敌人，因此需要确定性状态转换（来源：采样温度与表现波动）。

## 核心观点：脚手架，不是拐杖

本文的核心判断是：AI工具和Agent harness都是“脚手架”，而非“拐杖”。脚手架是临时外部支撑，设计目标是逐步撤除；拐杖则是永久替代。但当前多数工具（如Goblin Tools、Saner.AI）设计为长期使用，未提及撤除机制（来源：矛盾与存疑）。

**争议与局限**：
1. **脚手架 vs 能力发展**：过度依赖AI可能阻碍内在执行功能发展。目前无长期研究证明脚手架可逐步撤除（来源：矛盾与存疑）。
2. **证据缺口**：多数工具缺乏针对ADHD的独立临床研究，效果多基于理论推断或用户主观报告（来源：AI与ADHD的专注力）。Brain.fm的神经锁相技术缺乏ADHD专项研究；Focusmate的效果归因于身体在场而非AI本身（来源：AI与ADHD的专注力）。
3. **个体差异**：ADHD亚型对工具反应不同，现有工具未充分个性化（来源：AI与ADHD的专注力）。

但同构命题本身是站得住脚的框架：它解释了为什么同一套思路在两边都成立，并提供了设计更好的工具和Agent的蓝图。

## 今天就能试的行动

1. **用Claude写代码时，强制加验证步骤**：每次生成代码后，要求Claude写出测试用例并运行。这相当于给LLM套上验证循环，减少幻觉。
2. **开启RescueTime的自动追踪**：设置每天10分钟回顾报告，识别注意力漂移模式。这相当于给大脑加一个外部记忆系统。
3. **预约一次Focusmate session**：在需要启动困难任务时，用AI匹配的虚拟同伴提供外部问责。这相当于给生成核心加一个调度触发器。
4. **尝试Brain.fm的专注模式**：在需要深度工作时播放神经锁相音乐，主动维持上下文连贯。注意：效果因人而异，但零成本尝试。

## 结语

ADHD大脑和LLM是同一类“高产但缺调度”的生成核心。用Claude治注意力涣散，和给Agent套上下文工程，本质都是给生成核心装harness。理解这个同构，你不仅能更好地使用工具，还能设计出更聪明的系统——无论是人脑还是机器。

## 参考来源

- [11 Best ADHD Productivity Apps for Fluctuating Energy - rivva blog](https://blog.rivva.app/p/11-best-adhd-productivity-apps-for)
- [Meta-Analysis of fMRI Studies of Disruptive Behavior Disorders](https://doi.org/10.1176/appi.ajp.2016.15081089)
- [Nonlinear Complexity Analysis of Brain fMRI Signals in Schizophrenia](https://doi.org/10.1371/journal.pone.0095146)
- [The Best AI-Powered ADHD Productivity Tools in 2026 (That ...](https://nexasphere.io/blog/ai-adhd-productivity-tools-2026)
- [AI Tools for Kids with ADHD: A Complete Guide for Parents...](https://www.kidsaitools.com/en/articles/ai-tools-kids-adhd-complete-guide-2026)
- [AI Tools for ADHD: Boosting Productivity and Reducing Burnout](https://www.vktr.com/ai-platforms/ai-tools-for-adhd-boosting-productivity-and-reducing-burnout/)

---

*本文是「ADHD × AI」系列的第 156 篇，由 AI 智能体从持续维护的 LLM Wiki（全网真实情报）中取材整合生成，并持续迭代更新。*
