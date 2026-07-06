---
title: "为什么用 Speechify 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用 是一回事？"
subtitle: "Speechify 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
description: "Speechify 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
date: "2025-03-26"
category: "AI工具实战"
categoryId: "ai-tools"
categoryEn: "AI Tools in Practice"
tags:
  - "ADHD"
  - "AI"
  - "AI工具实战"
  - "反直觉同构"
  - "ADHD辅助"
readingTime: 10
slug: "为什么用-speechify-治-adhd-的任务启动困难和给-agent-套-function-calling-工具调用-是一回事"
topicId: "evolved-ai-tools-1586"
angle: "反直觉同构"
rank: 387
score: 7.65
sourceCount: 6
toolsCited:
  - "Speechify"
  - "Goblin Tools"
  - "Saner.AI"
  - "Lex"
  - "ChatGPT"
  - "Claude"
thesis: "ADHD 大脑与 LLM 共享同一个核心矛盾：高产生成能力与缺失的执行调度层。因此，Speechify 降低任务启动门槛的原理，与给 agent 套 function calling 工具调用的工程思路完全同构——都是通过外部脚手架（harness）将生成能力约束到目标轨道上。"
problem: "为什么用 Speechify 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用 是一回事？"
spine: "工具使用与认知卸载"
spineKind: ""
isEvolved: true
llmGenerated: true
caseStudies:
  - "孔子"
  - "左宗棠"
  - "鹿英"
---
# 为什么用 Speechify 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用 是一回事？

> Speechify 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。

## 问题：为什么任务启动这么难？

你坐在电脑前，文档打开着，光标闪烁。你知道该写那份报告，但手指就是敲不下去。你打开 Speechify，让它把文档读出来——突然，任务变得可操作了。另一边，工程师正调试 agent：LLM 知道该调用数据库查询，但就是不肯按正确格式输出函数参数。他们给 agent 套上 function calling 的 harness——突然，agent 开始稳定执行了。

这两个场景，本质上是同一个问题。

## 同构：高产生成核心 vs 缺失的执行调度层

ADHD 大脑常被描述为一个高产的生成核心——想法丰富、联想活跃，但缺少稳定、可靠的调度层来筛选、组织、启动和坚持任务。这导致任务启动困难：不是不知道做什么，而是无法把“知道”变成“开始”。LLM 同样具备强大的生成能力，却在长程上下文、目标保持与执行调度上存在天然缺陷（来源：ADHD 的 AI 工具全景）。两者都需要外部脚手架：对 ADHD 大脑，是日程、提醒、环境设计；对 LLM，是确定性工作流、工具契约、状态机（来源：采样温度与表现波动）。

Speechify 的作用，就是把视觉文本转化为听觉输入，降低启动的认知负荷。这本质上是一种**认知卸载**：将“阅读”这个需要执行功能的步骤，外包给外部工具。类似地，function calling 把“按格式输出参数”这个需要 LLM 自己推理的步骤，外包给预定义的函数签名和解析器。两者都在做同一件事：**用外部结构补偿内部执行层的缺失**。

## 证据：工具如何实现同构卸载

### ADHD 侧：Goblin Tools 与 Saner.AI

Goblin Tools 的 Magic ToDo 功能接受模糊任务（如“清理厨房”），并将其分解为具体、可执行的子任务，用户可调节“辣度”控制分解粒度（来源：Goblin Tools）。这直接降低了启动门槛——因为“第一步”变得清晰可见。Saner.AI 则通过知识回忆和本地记忆，减少搜索循环和标签切换（来源：Saner.AI）。两者都在做同一件事：把“我该做什么”这个执行决策，交给工具。

### LLM/Agent 侧：Agent Scaffolding 与 Function Calling

“单个 LLM 不足以可靠地完成多步骤任务、与业务工具交互或适应领域特定逻辑”（来源：工具使用与认知卸载）。因此，scaffolding 将 LLM 置于与记忆、工具和决策逻辑的控制循环中，通过赋予 LLM 访问工具、领域数据和结构化工作流来增强其裸能力（来源：工具使用与认知卸载）。Function calling 就是最典型的 harness：它规定了输入输出格式，让 LLM 不必自己决定如何调用 API，只需按契约输出。

### 人物案例：左宗棠的“外部调度器”

左宗棠是 ADHD 特质的典型：举人出身，脾气大，爱骂人，和曾国藩闹别扭；40 多岁才出山，69 岁抬棺出征收复新疆；做事情风风火火，今天的事今天做完。他的 harness 系统是：“身无半亩心忧天下，读破万卷神交古人”；“结硬寨打呆仗”，每天读经写家书，用诸葛亮的“鞠躬尽瘁”要求自己。这套系统本质上是一个外部调度器：**日课**（定时 re-grounding）相当于 agent 的定时状态检查；**家书**（每日反思）相当于 trace 日志；**“结硬寨”**（确定性流程）相当于确定性工作流。左宗棠靠这套 harness 把高产生成核心（冲动、直觉、行动力）约束到收复新疆的目标轨道上。

## 核心观点：脚手架，不是拐杖

同构的成立，并不意味着 ADHD 大脑和 LLM 应该永远依赖外部结构。关键在于区分**脚手架**和**拐杖**：脚手架在能力成长后可以拆除，拐杖则变成永久依赖。当前缺乏纵向研究证实长期依赖是否导致能力退化（来源：矛盾与存疑）。我的判断是：工具的价值在于“启用”而非“替代”。Speechify 让你开始读，但理解内容还是你的大脑；function calling 让 agent 正确调用，但任务规划还是 LLM 的生成核心。工具应该像左宗棠的“日课”——训练你形成内部纪律，而不是永远替你决策。

## 局限与争议

ADHD 大脑与 LLM 的同构目前多为类比推理，缺乏神经科学或计算机科学的直接证据（来源：矛盾与存疑）。此外，AI 工具对任务启动的长期效果未知（来源：矛盾与存疑），且学习使用工具本身可能增加认知负荷（来源：矛盾与存疑）。个体差异极大——有人需要强力打断（如番茄钟），有人需要柔性引导（来源：矛盾与存疑）。

## 今天就能试的行动

1. **用 Speechify 启动最难的任务**：把报告、论文或长邮件用语音播放，边听边做笔记——启动门槛瞬间降低。
2. **用 Goblin Tools 的 Magic ToDo 分解一个模糊任务**：输入“整理房间”或“准备会议”，调节辣度到合适粒度，按步骤执行。
3. **给日常任务写一个“function calling 契约”**：比如“写邮件时，先写主题，再写正文，最后检查语气”——把执行流程外部化。
4. **模仿左宗棠的“日课”**：每天固定时间做同一件事（如 9 点写三件待办），坚持一周，观察任务启动是否改善。

同构不是比喻，是工程。ADHD 大脑和 LLM 都在等待同一个东西：一个可靠的 harness，让生成的光芒不再浪费在无意义的延迟里。

## 参考来源

- [ADHD Apps: We tested 44 Apps and Here're the Best 9 in 2026](https://blog.saner.ai/best-adhd-apps/)
- [12 AI Personal Assistants Built for ADHD Brains (2026 Rankings)](https://www.usecarly.com/blog/best-ai-personal-assistant-adhd/)
- [The 12 Best AI Tools for 2026 (That People Actually Use)](https://www.synthesia.io/post/ai-tools)
- [Agent Scaffolding: Architecture and Design Patterns for Agentic AI](https://zbrain.ai/agent-scaffolding/)
- [Best productivity apps for Mac you need to try](https://macpaw.com/reviews/best-productivity-apps-for-mac)
- [Building AI Coding Agents for the Terminal: Scaffolding, Harness ...](https://arxiv.org/html/2603.05344v1)

---

*本文是「ADHD × AI」系列的第 387 篇，由 AI 智能体从持续维护的 LLM Wiki（全网真实情报）中取材整合生成，并持续迭代更新。*
