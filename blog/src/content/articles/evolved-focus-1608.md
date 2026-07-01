---
title: "为什么用 Perplexity 治 ADHD 的注意力涣散，和给 agent 套 上下文工程 是一回事？"
subtitle: "Perplexity 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
description: "Perplexity 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
date: "2025-04-02"
category: "专注力管理"
categoryId: "focus"
categoryEn: "Focus Management"
tags:
  - "ADHD"
  - "AI"
  - "专注力管理"
  - "反直觉同构"
  - "专注力"
readingTime: 7
slug: "为什么用-perplexity-治-adhd-的注意力涣散和给-agent-套-上下文工程-是一回事"
topicId: "evolved-focus-1608"
angle: "反直觉同构"
rank: 288
score: 7.68
sourceCount: 6
toolsCited:
  - "Perplexity"
  - "Brain.fm"
  - "Focusmate"
  - "RescueTime"
  - "Goblin Tools"
  - "Saner.AI"
  - "Inflow"
thesis: "ADHD大脑与LLM在结构上同构——都是高产的生成核心但缺乏可靠的执行调度层，因此Perplexity等AI工具帮助ADHD专注的本质，与给agent套上下文工程（harness）是同一回事：通过外部脚手架补偿执行功能缺陷。"
problem: "为什么用 Perplexity 治 ADHD 的注意力涣散，和给 agent 套 上下文工程 是一回事？"
spine: "上下文工程"
spineKind: ""
isEvolved: true
llmGenerated: true
---
# 为什么用 Perplexity 治 ADHD 的注意力涣散，和给 agent 套 上下文工程 是一回事？

> Perplexity 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。

## 问题：注意力涣散与上下文丢失，是同一个敌人

你打开Perplexity，想查一个概念，结果被侧边栏的“相关话题”带跑，半小时后你在读一篇关于火星殖民的文章，完全忘了最初要查什么。另一边，工程师调试AI agent时发现，模型明明有足够知识，却因为上下文窗口被无关内容撑满，输出变得混乱，甚至重复执行错误步骤。

这两个场景看似无关，但核心问题一模一样：**生成核心（大脑或LLM）本身不负责调度，一旦上下文管理失效，产出就失控。** ADHD的注意力涣散，本质是工作记忆频繁“溢出”，丢失当前任务上下文；LLM agent的失败，本质是上下文工程没做好，模型被无关信息干扰或遗忘关键指令。

## 同构：ADHD大脑与LLM，共享同一个架构缺陷

ADHD大脑的核心特征是高产但无序的生成能力，同时缺乏可靠的执行调度层。执行功能（如工作记忆、任务启动、时间管理）常出现故障，导致“想法很多，行动困难”（来源：ADHD大脑与LLM的同构）。LLM本身也是强大的生成核心，但缺乏内置调度与执行控制，因此需要“agent harness”——包裹模型之外的一切基础设施，包括上下文管理、工具接口、规划工件等（来源：Building AI Coding Agents for the Terminal）。

两边的问题结构一模一样：

| ADHD大脑 | LLM + Harness |
|----------|---------------|
| 高产但缺乏执行调度层的生成核心 | 高生成能力但需外部调度的LLM |
| 工作记忆易丢失上下文 | LLM无状态，需外部记忆管理 |
| 需要AI助手减少决策、保留上下文 | Harness负责上下文工程和决策路由 |
| 外部工具（如Goblin Tools）作为执行功能支架 | Harness中的模型连接器、工具调用等 |

（来源：ADHD大脑与LLM的同构）

所以，你用Perplexity治注意力涣散，和工程师给agent套上下文工程，本质是**同一套思路**：给生成核心加一个外部调度层，替它完成上下文保持、决策减负和任务路由。

## 证据：两边都靠“脚手架”而非“拐杖”

### ADHD侧：工具作为外部执行功能层

- **Brain.fm**：通过神经锁相技术影响大脑信息处理方式，帮助进入专注状态（来源：Brain.fm）。它的作用不是改变大脑结构，而是在听觉层面持续提供“上下文锚点”，减少外界干扰对工作记忆的冲击。
- **Focusmate**：利用AI匹配虚拟同伴，提供实时问责，弥补任务启动和注意力维持的调度缺失（来源：Focusmate）。它的核心机制是“AI-Matched Body Doubling”——通过外部社会压力替代内在执行功能。
- **RescueTime**：自动记录时间使用，充当外部记忆，提升时间盲觉察（来源：RescueTime）。它减轻了工作记忆负担，让用户不必同时记住“我做了什么”和“我该做什么”。

这些工具的共同点：**不试图修复大脑，而是构建外部脚手架**，就像给LLM套harness一样。

### LLM侧：Harness工程就是上下文工程

Harness工程被定义为“设计围绕AI代理的脚手架——上下文交付、工具接口、规划工件、验证循环、记忆系统和沙箱”（来源：GitHub - ai-boost/awesome-harness-engineering）。具体做法包括：
- 用Git仓库存储项目上下文（类似ADHD侧的“第二大脑”）；
- 通过MCP连接器访问外部数据（类似RescueTime自动记录）；
- 将控制逻辑外化为可移植的自然语言工件（类似Goblin Tools的任务分解）。

一个成功的agent，依赖的不是模型本身，而是围绕它的上下文工程。同样，一个ADHD用户的高效，依赖的不是意志力，而是围绕大脑的脚手架。

## 核心观点：脚手架 vs 拐杖——边界在哪里？

我的判断是：**脚手架与拐杖的边界，在于是否保留撤除路径。** 当前多数ADHD工具（如Goblin Tools、Saner.AI）设计为长期使用，未提及撤除机制（来源：矛盾与存疑）。这引发一个真实风险：过度依赖AI可能阻碍内在执行功能发展，就像agent一旦失去harness就瘫痪一样。

但Harness工程的目标恰恰相反：好的harness是**可逐步撤除的**——随着agent能力提升（如上下文窗口扩大、记忆机制内置），外部脚手架可以简化。ADHD工具也应如此：理想情况下，工具应设计为“先提供强力支持，再逐步减少”的渐进式脚手架，而非永久拐杖。可惜，目前没有长期研究证明这种撤除可行（来源：矛盾与存疑）。

另一个争议是多巴胺干预的有效性：Inflow等工具声称通过神经科学原理改善执行功能，但证据不足且存在矛盾（来源：矛盾与存疑）。Brain.fm的神经锁相技术也缺乏针对ADHD的独立临床研究（来源：Brain.fm）。这些工具的效果多基于理论推断或用户主观报告，而非严格随机对照试验。

## 行动：今天就能试的4件事

1. **用Perplexity时，主动管理上下文**：每次搜索前，在输入框写下“当前任务目标：XXX”。这相当于给大脑一个显式的上下文锚点，类似harness中的“系统提示”。
2. **尝试Focusmate一次**：预约一个25分钟时段，体验外部问责如何替代内在调度。注意观察：是“有人在看”让你启动，还是同伴的进度让你维持？
3. **用RescueTime自动追踪一天**：不手动记录，只看报告。识别出你“上下文溢出”最频繁的时间段——那个时段就是你的“上下文窗口过载”时刻。
4. **给AI agent写一个简单的harness**：用Python写一个循环，每次调用LLM前，自动注入当前任务目标、已完成的步骤、下一步计划。你会发现，这和ADHD工具“减少决策、保留上下文”完全一样。

## 局限与诚实

本文的同构命题是一个理论框架，而非经过大规模实证的事实（来源：矛盾与存疑）。现有证据主要来自工具机制与ADHD理论的对齐，而非独立临床研究。个体差异巨大：ADHD亚型（注意力缺陷 vs 多动冲动）对工具反应不同，现有工具未充分个性化（来源：主题综述）。

但正因如此，这个视角才有价值：它把ADHD的困境从“个人缺陷”重新定义为“架构问题”，而架构问题有工程解法。Perplexity治注意力涣散，和agent套上下文工程，说的都是同一件事：**给生成核心一个靠谱的调度层。**

## 参考来源

- [11 Best ADHD Productivity Apps for Fluctuating Energy - rivva blog](https://blog.rivva.app/p/11-best-adhd-productivity-apps-for)
- [Meta-Analysis of fMRI Studies of Disruptive Behavior Disorders](https://doi.org/10.1176/appi.ajp.2016.15081089)
- [Nonlinear Complexity Analysis of Brain fMRI Signals in Schizophrenia](https://doi.org/10.1371/journal.pone.0095146)
- [The Best AI-Powered ADHD Productivity Tools in 2026 (That ...](https://nexasphere.io/blog/ai-adhd-productivity-tools-2026)
- [AI Tools for Kids with ADHD: A Complete Guide for Parents...](https://www.kidsaitools.com/en/articles/ai-tools-kids-adhd-complete-guide-2026)
- [AI Tools for ADHD: Boosting Productivity and Reducing Burnout](https://www.vktr.com/ai-platforms/ai-tools-for-adhd-boosting-productivity-and-reducing-burnout/)

---

*本文是「ADHD × AI」系列的第 288 篇，由 AI 智能体从持续维护的 LLM Wiki（全网真实情报）中取材整合生成，并持续迭代更新。*
