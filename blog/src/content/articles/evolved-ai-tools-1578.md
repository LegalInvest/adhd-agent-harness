---
title: "为什么用 Routinery 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用 是一回事？"
subtitle: "Routinery 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
description: "Routinery 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
date: "2025-03-21"
category: "AI工具实战"
categoryId: "ai-tools"
categoryEn: "AI Tools in Practice"
tags:
  - "ADHD"
  - "AI"
  - "AI工具实战"
  - "反直觉同构"
  - "ADHD辅助"
readingTime: 13
slug: "为什么用-routinery-治-adhd-的任务启动困难和给-agent-套-function-calling-工具调用-是一回事"
topicId: "evolved-ai-tools-1578"
angle: "反直觉同构"
rank: 380
score: 7.65
sourceCount: 6
toolsCited:
  - "Routinery"
  - "Goblin Tools"
  - "Lex"
  - "Saner.AI"
  - "Claude"
  - "ChatGPT"
thesis: "ADHD大脑与LLM共享‘高产生成核心+缺失执行调度层’的架构缺陷，因此Routinery的任务分解与Agent的function calling本质同构——都是用外部脚手架补偿内在调度缺失，而非治愈缺陷。"
problem: "为什么用 Routinery 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用 是一回事？"
spine: "工具使用与认知卸载"
spineKind: ""
isEvolved: true
llmGenerated: true
caseStudies:
  - "孔子"
  - "释迦牟尼"
  - "Ingvar Kamprad"
---
# 为什么用 Routinery 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用 是一回事？

> Routinery 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。

## 同一个问题，两群人的痛

你是一个ADHD患者：脑子里同时跑着五个项目，每个都充满创意火花，但你就是无法从沙发上站起来，去启动哪怕最简单的一个任务。你打开Routinery，设置一个“早晨流程”，然后机器开始一步步告诉你：刷牙、喝水、换衣服——你终于动起来了。

你是一个AI agent工程师：你给LLM一个复杂的任务，它生成了一篇漂亮的计划，然后卡住了——它不知道下一步该调用哪个API，或者干脆忘记了目标。你给它套上function calling harness，定义好工具接口、上下文窗口、规划循环——它终于能执行了。

这两个场景，表面上是两个世界的问题。但如果你把ADHD大脑和LLM并排放置，你会发现它们共享同一个架构缺陷：**它们都是高产的生成核心，但都缺少一个可靠的内置执行调度层**（来源：ADHD 大脑与 LLM 的同构）。Routinery 和 function calling harness，本质上是同一个解决方案——用外部脚手架把生成能力约束到目标轨道上。

## 同构脊柱：生成核心 vs 调度层

### ADHD 一侧

ADHD大脑的神经心理学剖面被描述为“强记忆、弱控制”：工作记忆容量可能正常甚至超常，但认知灵活性与注意控制存在核心缺陷——无法灵活切换任务集、无法抑制自动化反应（来源：Strong Memory, Weak Control: An Empirical Study of Executive Functioning in LLMs）。默认模式网络（DMN）过度激活，导致注意力弥散分配，想法如泉涌却无法聚焦（来源：The Wanderer's Algorithm）。

这正是为什么ADHD个体需要外部工具来“减少决策、保留上下文、让下一步行动显而易见”（来源：Best AI Tools for ADHD Productivity in 2026）。Routinery 这样的工具，本质上是将“启动”这个决策从大脑中剥离，交给一个外部调度器。它不治疗你的注意力缺陷，它只是接管了调度权。

### LLM/Agent 一侧

LLM本身是无状态、仅生成文本的核心，在长程上下文、目标保持与执行调度上存在天然缺陷。实证研究用经典Stroop冲突任务测试Transformer注意力，发现短上下文中表现正常，但随序列变长，模型在冲突试次上骤降到随机水平——无法抑制优势反应、无法解决认知冲突，这与ADHD执行功能缺陷的核心标志一一对应（来源：Deficient Executive Control in Transformer Attention）。

因此，在构建AI agent时，需要“agent scaffolding”——即“围绕LLM构建的软件架构和工具，使其能够执行复杂、目标驱动的任务”（来源：Agent Scaffolding: Architecture and Design Patterns for Agentic AI）。Function calling 就是这种脚手架的关键组件：它把“下一步行动”的选择权从LLM的生成流中抽离，交给一个外部的调度循环。

## 历史验证：孔子的“礼”就是最早的harness

孔子（春秋/儒家创始人）很可能就是ADHD大脑的典型：身高1米9，精力旺盛，周游列国14年坐不住；冲动爱骂人，见南子急得对天发誓，骂宰予“朽木不可雕”；对音乐超专注到“三月不知肉味”，对种地等俗事零耐心；思维跳跃，《论语》全是场景化语录，无系统著作（来源：人物案例）。他的专属harness是“克己复礼”——用外在的“礼”作为行为边界，每日反省，“吾日三省吾身”；70岁才做到“从心所欲不逾矩”，一辈子和自己的冲动做斗争。

“礼”在这里扮演的角色，与LLM harness中的“function calling schema”如出一辙：它是一套预定义的行为模板，将“启动什么行动”的决策从冲动大脑中剥离，交给外部规则。孔子的“日课”相当于agent的定时re-grounding，“礼”相当于外部调度器。孔子没有“治愈”自己的冲动，他只是搭建了一套脚手架。

## 工具实证：从Routinery到function calling

Routinery 的核心机制是“任务序列化”——将早晨流程、工作流程拆解为固定步骤，用户只需跟随。这与 [[Goblin Tools]] 的 Magic ToDo 功能同构：AI 自动将“清理厨房”分解为“收拾台面→洗碗→擦灶台→拖地”等子步骤，降低启动门槛（来源：Goblin Tools）。[[Lex]] 更进一步，允许用户通过单一指令触发复杂、多步骤的任务序列（来源：Lex）。这些工具的底层架构，与agent scaffolding中的“规划机制”完全一致——将复杂目标分解为一系列步骤（来源：The Anatomy of an AI Agent）。

在LLM一侧，[[Claude]] 以代码编写和结构化推理见长，被ADHD用户用来整理待办与简化任务（来源：ADHD 的 AI 工具全景）。[[ChatGPT]] 被成人ADHD用户用作“外部执行功能”工具，在自身工作记忆丢失时携带上下文（来源：Best AI Tools for ADHD Productivity in 2026）。这些工具的价值不在于替代大脑，而在于把ADHD的“高产生成核心”接入一个可维护的“执行调度系统”。

## 争议与局限：脚手架不是拐杖

必须诚实指出，这一同构理论目前多为类比推理，缺乏神经科学或计算机科学的直接证据（来源：矛盾与存疑）。此外，AI工具是否真的能减轻认知负荷，因人而异——部分用户反映学习使用AI工具本身增加认知负荷（来源：矛盾与存疑）。更关键的是，过度依赖外部脚手架可能导致能力退化，成为永久拐杖（来源：矛盾与存疑）。

但我的判断是：**脚手架与拐杖的边界在于，你是否在主动设计它。** 孔子主动选择“礼”作为自己的行为边界，而非被动依赖；AI agent工程师精心设计function calling schema，而非放任LLM自由生成。主动设计意味着你保留了对调度层的控制权，而非被它控制。

## 今天就能试的行动

1. **ADHD读者**：在Routinery或Goblin Tools中，将一个你总拖延的任务（如“写周报”）分解为不超过5步的子任务，设置固定时间执行。观察“启动”是否变容易。
2. **工程师读者**：在LLM应用中，为你的agent添加一个简单的function calling schema，将“下一步行动”从生成流中抽离。对比有无schema时的任务完成率。
3. **双面读者**：尝试将你的ADHD任务流程用YAML或JSON格式写下来，就像写一个agent的harness配置。你会发现，调度逻辑是通用的。

同一套harness思路，ADHD与LLM两边都成立。这不是巧合，是架构的同构。

## 参考来源

- [ADHD Apps: We tested 44 Apps and Here're the Best 9 in 2026](https://blog.saner.ai/best-adhd-apps/)
- [12 AI Personal Assistants Built for ADHD Brains (2026 Rankings)](https://www.usecarly.com/blog/best-ai-personal-assistant-adhd/)
- [The 12 Best AI Tools for 2026 (That People Actually Use)](https://www.synthesia.io/post/ai-tools)
- [Agent Scaffolding: Architecture and Design Patterns for Agentic AI](https://zbrain.ai/agent-scaffolding/)
- [Best productivity apps for Mac you need to try](https://macpaw.com/reviews/best-productivity-apps-for-mac)
- [Building AI Coding Agents for the Terminal: Scaffolding, Harness ...](https://arxiv.org/html/2603.05344v1)

---

*本文是「ADHD × AI」系列的第 380 篇，由 AI 智能体从持续维护的 LLM Wiki（全网真实情报）中取材整合生成，并持续迭代更新。*
