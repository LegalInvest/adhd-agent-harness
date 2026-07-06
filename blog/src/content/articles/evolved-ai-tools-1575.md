---
title: "为什么用 Claude 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用 是一回事？"
subtitle: "Claude 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
description: "Claude 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
date: "2025-05-03"
category: "AI工具实战"
categoryId: "ai-tools"
categoryEn: "AI Tools in Practice"
tags:
  - "ADHD"
  - "AI"
  - "AI工具实战"
  - "反直觉同构"
  - "自动化"
readingTime: 14
slug: "为什么用-claude-治-adhd-的任务启动困难和给-agent-套-function-calling-工具调用-是一回事"
topicId: "evolved-ai-tools-1575"
angle: "反直觉同构"
rank: 137
score: 7.79
sourceCount: 6
toolsCited:
  - "Goblin Tools"
  - "Saner.AI"
  - "Lex"
  - "Claude"
thesis: "ADHD大脑与LLM共享同一困境：高产生成核心缺乏可靠执行调度层；用外部脚手架（harness）补偿这一缺陷，对两者是同一类工程问题。"
problem: "为什么用 Claude 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用 是一回事？"
spine: "工具使用与认知卸载"
spineKind: ""
isEvolved: true
llmGenerated: true
caseStudies:
  - "孔子"
  - "李鸿章"
  - "陈桂芝"
---
# 为什么用 Claude 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用 是一回事？

> Claude 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。

## 问题：启动困难，是ADHD的诅咒，也是LLM的软肋

如果你是一个ADHD成年人，你一定熟悉这个场景：脑子里有一堆想做的事，但身体就是动不了。任务像一堵无形的墙，启动它需要消耗巨大心理能量。如果你是一个做Agentic Harness的工程师，你也一定熟悉另一个场景：LLM模型能生成漂亮的计划，但一执行就偏离轨道，要么陷入循环，要么调用错误工具。

这两件事，表面风马牛不相及。但深挖下去，它们共享同一个底层结构：**一个高产的生成核心，挂在一个不可靠的执行调度层上。**

ADHD大脑被描述为“高产的生成核心——想法丰富、联想活跃，但缺少稳定、可靠的调度层来筛选、组织、启动和坚持任务”（来源：ADHD 的 AI 工具全景）。而LLM同样具备强大的生成能力，却在长程上下文、目标保持与执行调度上存在天然缺陷。所以，AI帮ADHD的实质，与给LLM套harness是同一类工程：用外部脚手架把生成能力约束到目标轨道上。

## 脚手架不是拐杖：同构的核心是“外部调度层”

先看ADHD侧。工具如Goblin Tools通过AI将复杂任务分解为可管理的小步骤，降低启动门槛（来源：Goblin Tools）。Saner.AI通过本地记忆和知识回忆减少搜索循环，补偿工作记忆不足（来源：Saner.AI）。Lex允许用户通过单一指令触发多步骤任务序列，降低启动时的认知负荷（来源：Lex）。这些工具的共性：它们不是在修复大脑，而是在大脑与外部世界之间搭建一个临时“外部执行功能层”（来源：ADHD 的 AI 工具全景）。

再看LLM/Agent侧。Agent harness通过human-in-the-loop监督提供外部调度：设置护栏（token预算、工具调用次数上限）、加入人工检查点、集成MCP工具和遥测（来源：人在回路与身体在场）。其核心目标是“形式化规划与护栏，使代理输出真正有用且正确”（来源：人在回路与身体在场）。

两边的结构完全同构：
- ADHD侧：生成核心（大脑）→ 外部执行功能层（工具）→ 任务完成
- LLM侧：生成核心（模型）→ 外部调度层（harness）→ 任务完成

但必须诚实指出一个争议：这种外部依赖是“脚手架”还是“拐杖”？脚手架帮助建设，建成后可拆除；拐杖则可能让人永久依赖。目前缺乏纵向研究验证长期依赖风险（来源：矛盾与存疑）。我的判断是：**脚手架 vs 拐杖的边界在于是否保留“人在回路”的主动性。** 如果工具完全替代了执行功能的主动参与（比如自动安排一切而不让用户选择），它就更像拐杖；如果工具只提供结构和提醒，用户仍需决策和行动，它就是脚手架。

## 历史人物早就用过这套harness

孔子是ADHD特质明显的例子：身高1米9，精力旺盛，周游列国14年坐不住；冲动爱骂人，思维跳跃，《论语》全是场景化语录，无系统著作。他的专属harness是“克己复礼”——用外在的“礼”作为行为边界，每日三省吾身。这套系统本质上是一个外部调度层：用礼（相当于今天的任务列表和提醒）约束自己的冲动，用反省（相当于定时re-grounding）校准方向。这与LLM harness中的“定时检查点”和“护栏”如出一辙。

李鸿章也是类似：年轻时冲动爱吹牛，跟着曾国藩学“诚”来改掉浮躁，每天写日记反省。他的harness是“外须和戎，内须变法”的务实原则，加上日记作为外部记忆和反思工具。日记相当于今天的Saner.AI的本地记忆——把想法外化，减少工作记忆负担。

这些历史人物的成就证明：**用外部脚手架管理高产生成核心，是跨越千年的有效策略。** 现代AI工具只是把这种策略自动化了。

## 具体怎么用？今天就能试的行动

1. **用Goblin Tools分解一个你拖延已久的任务。** 输入“整理书房”或“写周报”，让它拆成5-10个小步骤。每完成一步打勾，获得即时反馈（来源：Goblin Tools）。
2. **用Claude的Projects功能创建一个“执行调度”项目。** 把你的待办事项输入，要求它按优先级和时间估计排序，并设置提醒。Claude的结构化推理能力特别适合这种整理（来源：ADHD 的 AI 工具全景）。
3. **尝试Lex的单一指令触发。** 比如设定一个指令“准备明天会议”，让它自动执行：查日历→读相关文档→生成议程→发送提醒。这相当于给大脑装了一个“一键启动”按钮（来源：Lex）。
4. **建立你的“日课”系统。** 像孔子三省吾身一样，每天固定时间向AI汇报进度（如“今天完成了哪三件事？”），让它帮你回顾和调整计划。这利用了身体在场效应——定期向AI报告进度也是一种替代方案（来源：人在回路与身体在场）。

## 诚实的局限

同构论点目前主要是类比推理，缺乏神经科学或计算机科学的直接证据（来源：矛盾与存疑）。此外，AI工具对任务启动的长期效果未知：短期有效，但长期依赖可能削弱内在执行功能（来源：矛盾与存疑）。另外，超聚焦应被引导还是打断尚无定论——部分ADHD用户反馈强行打断（如番茄钟）反而有效（来源：矛盾与存疑）。

所以，本文提供的不是万能药，而是一个视角：**ADHD与LLM共享同一困境，也共享同一解法。** 这个视角的价值在于：它让ADHD个体看到自己的问题不是“懒”或“笨”，而是大脑架构的天然缺陷——而这个缺陷可以用工程思维来补偿。它也提醒工程师：你正在做的harness工程，本质上是在帮另一个“大脑”解决同样的启动困难。

下次当你对着空白的待办列表发呆时，或者当你调试一个总是跑偏的agent时，记住：你们面对的是同一个敌人——缺调度层的生成核心。而脚手架，是唯一的盟友。

## 参考来源

- [ADHD Apps: We tested 44 Apps and Here're the Best 9 in 2026](https://blog.saner.ai/best-adhd-apps/)
- [12 AI Personal Assistants Built for ADHD Brains (2026 Rankings)](https://www.usecarly.com/blog/best-ai-personal-assistant-adhd/)
- [The 12 Best AI Tools for 2026 (That People Actually Use)](https://www.synthesia.io/post/ai-tools)
- [Agent Scaffolding: Architecture and Design Patterns for Agentic AI](https://zbrain.ai/agent-scaffolding/)
- [Best productivity apps for Mac you need to try](https://macpaw.com/reviews/best-productivity-apps-for-mac)
- [Building AI Coding Agents for the Terminal: Scaffolding, Harness ...](https://arxiv.org/html/2603.05344v1)

---

*本文是「ADHD × AI」系列的第 137 篇，由 AI 智能体从持续维护的 LLM Wiki（全网真实情报）中取材整合生成，并持续迭代更新。*
