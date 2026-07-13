---
title: "为什么用 Saner.AI 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用 是一回事？"
subtitle: "Saner.AI 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
description: "Saner.AI 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
date: "2025-03-24"
category: "AI工具实战"
categoryId: "ai-tools"
categoryEn: "AI Tools in Practice"
tags:
  - "ADHD"
  - "AI"
  - "AI工具实战"
  - "反直觉同构"
  - "自动化"
readingTime: 12
slug: "为什么用-sanerai-治-adhd-的任务启动困难和给-agent-套-function-calling-工具调用-是一回事"
topicId: "prob-b1202fad7f"
angle: "反直觉同构"
rank: 175
score: 7.69
sourceCount: 6
toolsCited:
  - "Saner.AI"
  - "Goblin Tools"
  - "Lex"
  - "Motion"
  - "Reclaim.ai"
  - "Tiimo"
  - "ChatGPT"
  - "Mem"
thesis: "ADHD 大脑与 LLM 同为『高产生成核心 + 不可靠执行调度层』，Saner.AI 对任务启动的干预与 function calling 对 agent 的 harness 是同一套外部脚手架工程：把意图转译为可调用、可检索、可分解的外部工具链，从而用结构换可控性。"
problem: "为什么用 Saner.AI 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用 是一回事？"
spine: "工具使用与认知卸载"
spineKind: ""
isEvolved: true
llmGenerated: true
isoStrength: "A"
caseStudies:
  - "孔子"
  - "曾国藩"
  - "Stephanie Miller"
---
# 为什么用 Saner.AI 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用 是一回事？

> Saner.AI 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。

## 两种瘫痪：你盯着空白文档，Agent 盯着空白上下文

ADHD 用户最常见的崩溃不是「想不出」，而是「想了很多，就是动不了」。任务目标明明清楚，身体却像被粘在椅子上；大脑在后台疯狂跑线程，前台却弹不出一个可执行窗口。工程师们看 LLM 时也有类似的焦虑：模型能滔滔不绝，但让它真正去查日历、发邮件、订机票、更新数据库，它不会自己伸手——它只会继续生成文本，直到有人给它一套 function calling 工具调用接口。

两种瘫痪表面不同，底层结构却惊人地相似：一个高产的生成核心，配了一个不可靠的执行调度层。ADHD 大脑的创意与检索能力不弱，甚至超常；LLM 的生成能力也极强。但两者都需要外部 harness，把漂浮的意图锚定成可执行的动作序列。Saner.AI 治 ADHD 的任务启动困难，本质上就是在给人脑安装一套类似 LLM function calling 的脚手架。

## 不是懒，是调度层缺了一块

ADHD 的任务启动困难不是意志力问题。多巴胺系统失衡让行动动机难以被点燃，工作记忆容量有限使得任务步骤无法在脑中稳定展开，时间盲又让人低估紧迫感，拒绝敏感性焦虑（RSD）还会把启动前的担忧放大到冻结状态。（来源：任务启动概念页）这些正是执行功能层的故障：不是核心不会想，而是调度不会发令。

最新研究甚至把这种同构推到了神经科学层面。用类 Stroop 冲突任务测试 Transformer 注意力时发现，短上下文表现正常，但序列变长、认知负荷增加后，模型在冲突试次上骤降到随机水平——无法抑制优势反应、无法解决认知冲突。这与 ADHD 执行功能缺陷的核心标志一一对应：注意控制不足、干扰抑制缺陷、随认知负荷增加而崩溃。（来源：Deficient Executive Control in Transformer Attention）

也正因为如此，很多成年人会自发把 ChatGPT 当成「执行功能外挂」——不是让它替自己思考，而是让它把脑中混沌的意图整理成可启动的下一步。研究者把这个现象称为「a little bit of a life raft」。（来源："A little bit of a life raft" – Exploring the Use and Experiences of ChatGPT as a Support Tool among Adults with ADHD）

## 没有 function calling，LLM 只会继续说话

LLM 的困境是镜像的。它能在对话里生成高质量的规划、代码、邮件草稿，但它没有内置的执行调度层：不会自动检查日程，不会主动调用 API，不会在多轮会话中稳定保持目标。上下文窗口有限，也不具备真正的跨会话持久状态。没有外部约束时，它会漂移、会幻觉，会把目标对话变成自由联想。（来源：ADHD 的 AI 工具全景主题综述）

function calling 工具调用就是给 LLM 装的 harness：模型不再只输出文本，而是输出结构化调用指令——调用日历、查询数据库、执行计算、写入记忆。agent scaffolding 的架构设计模式正是围绕这一点：给生成核心套一个能感知、能记忆、能规划、能调用工具的外部层。（来源：Agent Scaffolding: Architecture and Design Patterns for Agentic AI）这套结构与 ADHD 的 AI 辅助工具设计完全相同：外部执行功能层接管调度，核心只负责生成。

## Saner.AI 的 harness 实测

Saner.AI 的设计非常像给人用的 agent 脚手架。它的核心不是让你「更努力」，而是把认知负荷外部化。Universal Inbox 从邮件、文档、日历中提取待办事项，相当于 agent 的感知工具；内部助手检查截止日期、把大型项目拆成小里程碑，相当于规划工具；本地记忆与语义搜索让你不必在多标签之间来回切换，相当于记忆与检索工具。（来源：ADHD Apps: We tested 44 Apps and Here're the Best 9 in 2026；Best AI Tools for ADHD Productivity in 2026 (Honest Review) - Iwo Szapar）

对任务启动困难而言，真正起作用的是「把模糊意图翻译为可调用步骤」。Goblin Tools 的 Magic ToDo 会把「清理厨房」拆成具体动作；Lex 用单一指令触发多步骤任务序列；Saner.AI 则用 AI 助手把项目压成里程碑。它们的共同机制是 micro-chunking：把任务拆到执行功能障碍无法抗拒启动的程度。（来源：ADHD Task Managers That Work: Top AI Tools 2025）这与 LLM 的 function calling 一模一样：模型输出一个意图，系统把它映射为可执行工具调用。

## 同构：曾国藩的日课，就是 agent 的 re-grounding

这种 harness 思路不是新发明。晚清曾国藩的日记几乎是一部 ADHD 自我管理的考古现场：30 岁前浮躁坐不住，读书慢，情绪不稳，打败仗就跳水。他给自己的 harness 是「日课十二条」——黎明即起、读书不二、谨言、写日记反省；作战则用「结硬寨打呆仗」，用最笨最稳的方法抵消冲动。一辈子写日记骂自己，其实是持续做外部状态的重新锚定（re-grounding）。（来源：人物案例：曾国藩）

把他的系统翻译成 agent 语言：黎明即起 = 定时触发任务；读书不二 =

## 参考来源

**同构强度：A 级** —— 直接文献支撑（引用 ADHD↔LLM 同构专题研究）

- [ADHD Apps: We tested 44 Apps and Here're the Best 9 in 2026](https://blog.saner.ai/best-adhd-apps/) — 证据等级：低（GRADE）
- [12 AI Personal Assistants Built for ADHD Brains (2026 Rankings)](https://www.usecarly.com/blog/best-ai-personal-assistant-adhd/) — 证据等级：低（GRADE）
- ["A little bit of a life raft" – Exploring the Use and Experiences of ChatGPT as a Support Tool among Adults with ADHD](https://dl.acm.org/doi/pdf/10.1145/3764687.3764713) — 证据等级：低（GRADE）
- [Revolutionizing ADHD Management with AI Assistants](https://neurolaunch.com/adhd-ai-assistant/) — 证据等级：低（GRADE）
- [ADHD Task Managers That Work: Top AI Tools 2025](https://www.sentisight.ai/ai-neurodivergent-productivity-adhd-friendly/) — 证据等级：低（GRADE）
- [The 12 Best Apps for ADHD in 2026: A Guide to Finding What ...](https://www.getinflow.io/post/best-apps-for-adhd) — 证据等级：低（GRADE）

---

*本文是「ADHD × AI」系列的第 55 篇，由 AI 智能体从持续维护的 LLM Wiki（全网真实情报）中取材整合生成，并持续迭代更新。*
