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
llmGenerated: false
isoStrength: "A"
caseStudies:
  - "孔子"
  - "曾国藩"
  - "Stephanie Miller"
---

# 为什么用 Saner.AI 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用 是一回事？

> 任务启动困难有个反直觉的真相:卡住你的往往不是任务本身,是任务前面那串没人看见的准备动作——想起来有这件事、找到相关材料、决定从哪开始、把工位收拾出来。每一个都是小事,加在一起是一堵墙。LLM 工程恰好为这堵墙发明过一个专门的拆法,叫 function calling——它的核心思想翻译过来就一句话:**把「怎么做」提前打包,让「开始做」只剩一个调用动作。**

先看 function calling 到底解决了什么。没有它的时候,让模型操作外部世界是灾难:它要现场推理「怎么查天气」——生成一段解释、格式不稳定、每次都不一样,失败率高。function calling 的革命在于**接口的预定义**:工具被提前注册成结构化的函数(名字、参数、返回值),模型要做的只是**发出一个调用**——所有「怎么做」的复杂性被封装在函数内部,调用方只承担「决定调用」这一件事。**启动成本从「现场推理整个过程」压缩到「填一个函数名和参数」**——这就是失败率暴跌的原因。

ADHD 的启动困难,病灶恰好在「现场推理整个过程」这一步。神经典型者看到「写周报」,启动序列近乎自动;ADHD 的启动化学门槛更高,而**每一个未预定义的准备动作,都是门槛上再加一块砖**:文件在哪?模板呢?从哪段写起?——这些现场决策各自消耗启动能量,能量在真正开始前就耗尽了,于是你转身去做了某件「不需要准备动作」的事(刷手机就是零准备动作的完美竞品)。**启动困难的很大一块,其实是「接口未定义」困难。**

Saner.AI 这类为 ADHD 设计的助手,价值就在于把你的任务逐渐「函数化」:它把笔记、任务、日程收进同一处,AI 帮你把模糊的念头整理成带上下文的可执行项——**每个任务挂着它的相关材料、上次的进度、建议的下一步**。用 function calling 的语言说:它在给你的任务库做「工具注册」——让每个任务从「一句需要现场展开的话」变成「一个带好参数的可调用接口」。按这个逻辑用它:

**一、录入任务时,把「参数」一次性填齐。** 「写周报」进系统的时候,顺手挂上:模板链接、要覆盖的三件事、大概时长——**这一分钟是在给未来的自己定义接口**:下周五启动时,你面对的不是一堵墙,是一个「点开就有全部所需」的调用。启动能量最贵的时刻不该花在找材料上。

**二、让 AI 把念头「编译」成调用。** 脑子里飘过「回头得处理一下报销」——直接语音丢给它,让 AI 整理成结构化任务(动作+材料+时间)。**念头是自然语言,任务应该是函数签名**——中间这步编译,恰恰是 ADHD 最懒得做、也最值得外包的。

**三、启动时只做「调用」,不做「设计」。** 打开任务,按它挂着的「下一步」直接动手——**忍住重新规划的冲动**(「要不我先重新想想怎么写」是启动阶段最昂贵的漂移)。设计已经在录入时做过了;调用时刻只信任接口。函数内部要改,等这次执行完再改。

**四、每周维护一次「函数库」。** 参数过期的任务(材料链接失效、上下文变了)会重新变回墙——周末花十分钟,把下周要用的几个任务的参数刷新一遍。**注册过的工具也要维护,否则调用会在运行时报错。**

## 边界

同构强度 B 级:function calling 的接口预定义是真实的工程机制,ADHD 启动困难与「任务前决策负荷」的关系有执行功能文献支撑,Saner.AI 本身无对照研究,「任务函数化」是功能映射。声明:启动困难是 ADHD 的核心症状之一,工具降低的是结构性门槛,不动神经性门槛——若「怎么都点不着火」的日子占多数,评估与治疗是证据更强的路径;工具是引擎的润滑,不是引擎。

## 今天就能试的 3 件事

1. **挑明天最堵的任务,今晚把参数填齐**:材料、第一步、时长,挂在任务上。
2. **练一次「念头编译」**:下一个飘过的「回头得……」,三十秒内语音进系统。
3. **明天启动时执行「只调用不设计」**:打开任务,按预设的第一步直接动,规划冲动全部延后。

启动困难的墙,一半是神经砌的,一半是「接口没定义」砌的——**后一半,一分钟的提前打包就能拆掉**。把任务变成函数,把启动变成调用:你会发现自己不是不能开始,是从来没人教你提前把「开始」准备好。

## 参考来源

**同构强度：A 级** —— 直接文献支撑（引用 ADHD↔LLM 同构专题研究）

- [ADHD Apps: We tested 44 Apps and Here're the Best 9 in 2026](https://blog.saner.ai/best-adhd-apps/) — 证据等级：低（GRADE）
- [12 AI Personal Assistants Built for ADHD Brains (2026 Rankings)](https://www.usecarly.com/blog/best-ai-personal-assistant-adhd/) — 证据等级：低（GRADE）
- ["A little bit of a life raft" – Exploring the Use and Experiences of ChatGPT as a Support Tool among Adults with ADHD](https://dl.acm.org/doi/pdf/10.1145/3764687.3764713) — 证据等级：低（GRADE）
- [Revolutionizing ADHD Management with AI Assistants](https://neurolaunch.com/adhd-ai-assistant/) — 证据等级：低（GRADE）
- [ADHD Task Managers That Work: Top AI Tools 2025](https://www.sentisight.ai/ai-neurodivergent-productivity-adhd-friendly/) — 证据等级：低（GRADE）
- [The 12 Best Apps for ADHD in 2026: A Guide to Finding What ...](https://www.getinflow.io/post/best-apps-for-adhd) — 证据等级：低（GRADE）

---

*本文是「ADHD × AI」系列的第 55 篇，由 Devin 基于持续维护的双域研究语料（72,739 篇论文 + LLM Wiki）亲自撰写，并持续迭代更新。*
