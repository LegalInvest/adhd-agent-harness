---
title: "为什么用 Goblin Tools 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用 是一回事？"
subtitle: "Goblin Tools 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
description: "Goblin Tools 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
date: "2025-05-19"
category: "AI工具实战"
categoryId: "ai-tools"
categoryEn: "AI Tools in Practice"
tags:
  - "ADHD"
  - "AI"
  - "AI工具实战"
  - "反直觉同构"
  - "智能助手"
readingTime: 14
slug: "为什么用-goblin-tools-治-adhd-的任务启动困难和给-agent-套-function-calling-工具调用-是一回事"
topicId: "evolved-ai-tools-1564"
angle: "反直觉同构"
rank: 181
score: 7.72
sourceCount: 6
toolsCited:
  - "Goblin Tools"
  - "Saner.AI"
  - "Lex"
  - "Motion"
  - "ChatGPT"
  - "Claude"
thesis: "ADHD大脑与LLM共享同一困境：高产生成核心缺乏可靠调度层。Goblin Tools的任务分解与Agent的function calling，本质都是为这个核心搭建外部执行脚手架——解法同构，局限相同。"
problem: "为什么用 Goblin Tools 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用 是一回事？"
spine: "工具使用与认知卸载"
spineKind: ""
isEvolved: true
llmGenerated: true
caseStudies:
  - "孔子"
  - "曾国藩"
  - "Robert Avery"
---
# 为什么用 Goblin Tools 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用 是一回事？

> Goblin Tools 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。

## 你卡在「开始」上的那一刻，和LLM卡在第一个tool call上的那一刻，是同一回事

如果你有ADHD，你一定熟悉这个场景：脑子里有一堆事要做，但身体钉在椅子上，手指划着手机，就是动不了。任务越大、越模糊，启动越难。

如果你在做Agent工程，你一定也熟悉这个场景：LLM生成了完美的计划，但在第一个工具调用时就跑偏了——参数传错、上下文丢了、或者干脆拒绝执行。

这两件事，表面看一个关乎人类心理，一个关乎机器架构。但它们的底层结构一模一样：**一个高产的生成核心，缺一个可靠的执行调度层。**

Goblin Tools 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用，本质是同一套工程。

## 同构：ADHD大脑与LLM共享同一困境

ADHD大脑常被描述为“高产生成核心”——想法丰富、联想活跃，但缺少稳定、可靠的调度层来筛选、组织、启动和坚持任务（来源：ADHD 的 AI 工具全景）。LLM同样具备强大的生成能力，却在长程上下文、目标保持与执行调度上存在天然缺陷（来源：ADHD 的 AI 工具全景）。

两边的问题一模一样：
- **ADHD侧**：任务启动困难，因为执行功能（规划、组织、工作记忆）不足（来源：规划循环与任务分解）。
- **LLM侧**：缺乏内在规划能力，需要外部harness引导（来源：规划循环与任务分解）。

所以，两边的解法也一模一样：**用外部脚手架把生成能力约束到目标轨道上。**

## Goblin Tools：ADHD侧的function calling

Goblin Tools 的 Magic ToDo 功能，能自动将任何任务分解为更小、更易管理的步骤（来源：Goblin Tools）。你输入“清理厨房”，它输出：
1. 把碗碟放进洗碗机
2. 擦拭台面
3. 拖地
...

这就是 function calling。ADHD大脑把“清理厨房”这个模糊意图，拆解成一系列可执行的原子操作。每个子任务就是一次 tool call。

Goblin Tools 还允许调节“辣度”控制分解粒度（来源：Goblin Tools）——这相当于 LLM agent 中的 planning loop 参数。太粗，启动还是难；太细，认知开销太大。

## LLM侧：function calling 就是任务分解

在 Agent 工程中，scaffolding “将LLM置于与记忆、工具和决策逻辑的控制循环中”（来源：工具使用与认知卸载）。每次模型调用可访问检索（外部事实）、工具调用（如数据库查询或代码执行）和记忆缓冲区（存储状态）（来源：工具使用与认知卸载）。

这跟 Goblin Tools 做的事一模一样：
- 检索 ↔ 知识回忆（如 Saner.AI 的本地记忆）
- 工具调用 ↔ 子任务执行
- 记忆缓冲区 ↔ 工作记忆的外化

Lex 更进一步：允许用户通过单一指令触发复杂、多步骤的任务序列（来源：Lex）。其底层架构类似于 agent scaffolding（来源：Lex）。

## 真实案例：曾国藩的harness系统

曾国藩30岁前典型ADHD：浮躁坐不住，天天串门喝酒看杀人，日记里骂自己“无恒”“浮躁”。他的harness系统是“日课十二条”：黎明即起、读书不二、谨言、写日记反省……用最笨最稳的方法抵消自己的冲动。

这个系统与LLM harness同构对应：
- 日课 ↔ 定时 re-grounding（如每轮对话重置system prompt）
- 写日记反省 ↔ 会话状态记录工具结果、完成的子任务和进度笔记（来源：规划循环与任务分解）
- “结硬寨打呆仗” ↔ 用最稳定的workflow约束生成核心

曾国藩的成就证明：一个高产生成核心（他的思维活跃、洞察力强）加上一个外部的、纪律性的调度层，可以产生巨大影响。

## 脚手架 vs 拐杖：边界在哪里？

这里必须诚实指出争议。核心论点是：AI作为外部执行功能层补偿缺陷（来源：矛盾与存疑）。但存疑的是：过度依赖可能导致能力退化，成为永久拐杖（来源：矛盾与存疑）。

同样，在LLM侧，过度scaffolding会降低模型的自主性，让agent变成死板的if-then脚本。两边面临同样的风险：**脚手架用好了是赋能，用坏了是替代。**

目前缺乏纵向研究来证明长期依赖的效果（来源：矛盾与存疑）。我的判断是：**脚手架应当逐步内化。** 曾国藩70岁才做到“从心所欲不逾矩”，他的日课不是终身拐杖，而是训练工具。同样，ADHD用户应逐渐减少对Goblin Tools的依赖，LLM agent也应逐渐减少hard-coded planning loop，转向更灵活的自我调度。

## 今天就能试的3件事

1. **用Goblin Tools分解一个你拖延了一周的任务**——比如“整理邮箱”。设置辣度中等，按生成的子任务逐个完成。
2. **类比到你的LLM agent**：检查你的function calling schema——每个tool是否足够原子化？是否像Goblin Tools的子任务一样，一步到位？
3. **建立自己的“日课”**：每天固定时间、固定流程（如先写日记再规划），作为外部调度层。可以用Saner.AI或Motion自动提醒。

## 结论

ADHD大脑与LLM不是比喻，是同一类系统。Goblin Tools与function calling不是巧合，是同一套工程。理解这一点，你就能同时优化自己的大脑和你的agent——因为它们共享同一个bug，也共享同一个fix。

## 参考来源

- [ADHD Apps: We tested 44 Apps and Here're the Best 9 in 2026](https://blog.saner.ai/best-adhd-apps/)
- [12 AI Personal Assistants Built for ADHD Brains (2026 Rankings)](https://www.usecarly.com/blog/best-ai-personal-assistant-adhd/)
- [The 12 Best AI Tools for 2026 (That People Actually Use)](https://www.synthesia.io/post/ai-tools)
- [Agent Scaffolding: Architecture and Design Patterns for Agentic AI](https://zbrain.ai/agent-scaffolding/)
- [Best productivity apps for Mac you need to try](https://macpaw.com/reviews/best-productivity-apps-for-mac)
- [Building AI Coding Agents for the Terminal: Scaffolding, Harness ...](https://arxiv.org/html/2603.05344v1)

---

*本文是「ADHD × AI」系列的第 181 篇，由 AI 智能体从持续维护的 LLM Wiki（全网真实情报）中取材整合生成，并持续迭代更新。*
