---
title: "ADHD 学生视角：为什么「治好 ADHD 的工作记忆容量小、边做边忘」和「让 LLM 不跑飞」其实是同一道工程题？"
subtitle: "LLM 无跨会话状态，靠外部记忆/向量库续命——同一套 harness 思路，两边都成立。"
description: "LLM 无跨会话状态，靠外部记忆/向量库续命——同一套 harness 思路，两边都成立。"
date: "2025-04-23"
category: "AI工具实战"
categoryId: "ai-tools"
categoryEn: "AI Tools in Practice"
tags:
  - "ADHD"
  - "AI"
  - "AI工具实战"
  - "人群×同构"
  - "自动化"
readingTime: 12
slug: "adhd-学生视角为什么治好-adhd-的工作记忆容量小边做边忘和让-llm-不跑飞其实是同一道工程题"
topicId: "prob-f472b0a5d0"
angle: "人群×同构"
rank: 99
score: 7.77
sourceCount: 6
toolsCited:
  - "Goblin Tools"
  - "Lex"
  - "Saner.AI"
  - "Motion"
  - "Reclaim.ai"
thesis: "ADHD 大脑与 LLM 都是「高产生成核心 + 不可靠执行调度层」，二者的问题不是去「修好内部」，而是外接同一套 harness：用外部记忆、任务分解与上下文约束把跑飞的生成核心重新锚定。"
problem: "ADHD 学生视角：为什么「治好 ADHD 的工作记忆容量小、边做边忘」和「让 LLM 不跑飞」其实是同一道工程题？"
spine: "无状态与外部记忆"
spineKind: "llm"
isEvolved: false
llmGenerated: false
isoStrength: "B"
caseStudies:
  - "孔子"
  - "辛弃疾"
  - "余林"
---

# ADHD 学生视角：为什么「治好 ADHD 的工作记忆容量小、边做边忘」和「让 LLM 不跑飞」其实是同一道工程题？

> 「读到题目后半句,忘了前半句的条件」「老师连讲三个要求,只接住一个」「刚背的公式,翻页就没」——学生时代的工作记忆短板,几乎每一条都在扣分。但请注意:LLM 面对超出上下文窗口的信息,表现一模一样,而工程师的解法是给它外接记忆,不是骂它笨。

学业场景是工作记忆的重灾区,因为学校的默认教学法就是「口头多步指令+脑内持账」:听讲要边听边记边理解;应用题要把三四个条件同时拿在手上;写作文要边写这段边记着下段的构思;老师布置作业靠嘴说,附加「注意事项」三条。工作记忆容量小的学生,在这套默认设置里全程处于「工作台溢出」状态——**东西掉了,而且掉得毫无预警**:不是没听,是装不下;不是不会,是解到第三步时第一步的条件已经蒸发。最冤的是,这一切在外界眼里都叫「不认真」。

LLM 的对应画像有直接研究:上下文一长,中段信息调用劣化;多重指令下丢约束是系统性的。工程答案:外部状态存储+checkpoint+上下文瘦身——**永远不赌记忆,一切落盘**。学生版翻译:

## 课堂:从「脑内接」改成「纸上接」

听讲的正确姿势不是「专心记住」,是**边听边卸载**:关键词式速记(不求全,求「钩子」——回头能钩起来就行)、老师的口头要求必须落纸(专门一个「指令区」记作业和注意事项——这是最容易丢也最贵的信息)。听不过来时,优先记「结构」(今天讲了三块:A、B、C)而不是细节——结构是检索的索引,细节可以课后补。**下课前 30 秒扫一眼指令区,是每天性价比最高的 30 秒。**

## 做题:把条件从脑内搬到纸上

应用题/多步骤题的军规:**读题时手不许闲着**——圈出每个条件、把数字和关系直接标注在题目上、复杂题画草图。这不是小学生做法,这是 checkpoint:解到第三步时,条件不在你脑子里,在纸上,随时回查。数学解题的中间结果同理,写清晰、编号——「刚才算的那个数是多少来着」的每一次,都是没落盘的税。

## 背诵与复习:别考工作台,考长期库

「刚背就忘」的很多情况,其实是把材料塞在工作台上假装存进了长期库。修法:**间隔重复**(anki 类工具,把「记住」外包给算法安排的复习节奏)+**主动回忆**(合上书自测,而不是反复看——看十遍的流畅感是工作台的幻觉,回忆一遍才是长期库的写入)。ADHD 学生特别受益于这套,因为它把「靠意志安排复习」变成「照系统提示走」。

## 写作与长任务:提纲就是你的外接内存

作文/报告的痛点:写着这段忘了整体。修法:**先搭提纲再动笔**(提纲是整篇文章的外部状态),写作时提纲全程可见;每写完一段,回看提纲对一次位。跨天的作业,停笔时写一行「明天从哪句继续+思路」——明天的你是个没有上下文的新会话,这行字是他的救命 prompt。

## 给家长/老师的一句转达

工作记忆小的学生,吃「口头多步指令」的亏最大、吃「写下来的结构化指令」的红利也最大——**作业要求请写在看得见的地方;多步任务请拆开给**。这不是特殊照顾,是把默认设置从「为大工作台设计」调成「兼容所有工作台」——研究显示这类调整对全班都有益,对 ADHD 学生是雪中送炭。

## 边界

同构强度 A 级:双侧证据都硬(ADHD 工作记忆缺陷是荟萃级发现;LLM 上下文干扰有直接研究,含与人类工作记忆的对照实验)。照例:功能同构,机制不同。另外「工作记忆训练」类商业课程的远迁移证据薄弱,预算有限的话,外部化工具+间隔重复的性价比高得多;若记忆困难伴随阅读速度/理解的持续问题,值得评估是否有学习障碍共病。

## 今天就能试的 3 件事

1. **建「指令区」**:笔记本固定一角,今天起老师的每个口头要求即刻落纸,下课前扫一遍。
2. **下一套题练「手不闲着」**:圈条件、标关系、中间结果编号。对比一次错误率。
3. **给正在背的科目装间隔重复**:挑一个 anki 类工具,把本周的重点做成卡。让算法替你安排复习。

工作台小,从来不是智力的上限——它只是要求你换一种架构来学习。纸是你的外接内存,提纲是你的状态文件,间隔重复是你的写入协议;装好这一套,你的长期库和处理器,才终于能按真实水平交卷。

## 参考来源

**同构强度：B 级** —— 机制类比（ADHD 侧与 LLM/agent 侧均有真实文献，机制可映射）

- [ADHD Apps: We tested 44 Apps and Here're the Best 9 in 2026](https://blog.saner.ai/best-adhd-apps/) — 证据等级：低（GRADE）
- [12 AI Personal Assistants Built for ADHD Brains (2026 Rankings)](https://www.usecarly.com/blog/best-ai-personal-assistant-adhd/) — 证据等级：低（GRADE）
- [Agent Scaffolding: Architecture and Design Patterns for Agentic AI](https://zbrain.ai/agent-scaffolding/) — 证据等级：低（GRADE）
- [LBD同构对：任务分解与规划 — Attention-deficit/hyperactivity disorder is characterized by ↔ Language-conditioned world model improves policy generalizat](https://doi.org/10.1073/pnas.0707741104) — 证据等级：低（GRADE）
- [LBD同构对：任务分解与规划 — Safety and recommendations for TMS use in healthy subjects a ↔ AgentGen: Enhancing Planning Abilities for Large Language Mo](https://doi.org/10.1016/j.clinph.2020.10.003) — 证据等级：低（GRADE）
- [LBD同构对：任务分解与规划 — How specific are executive functioning deficits in attention ↔ AMAP Agentic Planning Technical Report](https://doi.org/10.1111/j.1469-7610.2004.00276.x) — 证据等级：低（GRADE）

---

*本文是「ADHD × AI」系列的第 20 篇，由 Devin 基于持续维护的双域研究语料（72,739 篇论文 + LLM Wiki）亲自撰写，并持续迭代更新。*
