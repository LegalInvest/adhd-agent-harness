---
title: "为什么用 Reclaim.ai 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用 是一回事？"
subtitle: "Reclaim.ai 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
description: "Reclaim.ai 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
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
readingTime: 8
slug: "为什么用-reclaimai-治-adhd-的任务启动困难和给-agent-套-function-calling-工具调用-是一回事"
topicId: "prob-e2eeba71c6"
angle: "反直觉同构"
llmGenerated: false
rank: 176
score: 7.69
sourceCount: 4
toolsCited:
  - "Goblin Tools"
  - "Saner.AI"
  - "Lex"
  - "Mem"
problem: "为什么用 Reclaim.ai 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用 是一回事？"
spine: "工具使用与认知卸载"
spineKind: ""
isEvolved: true
---

# 为什么用 Reclaim.ai 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用 是一回事？

> 上一篇讲了启动困难的「接口未定义」成分——把任务提前打包成可调用的函数。但 function calling 还有另一半机制,常被忽略,而它恰好对着启动困难的另一个病灶:**函数注册好了,谁来发起调用?** 模型不会凭空调用工具,需要运行时在恰当的时机把工具递到它面前。ADHD 版的同一个问题:任务参数都齐了,可「打开它」这个动作,依然没有发生。Reclaim.ai 治的是这一半。

先看工程侧这半个机制。function calling 的完整链路是:工具注册→**运行时把「当前可用的工具+当前上下文」呈现给模型**→模型决定调用→执行。中间那步很关键:**模型看不见没被呈现的工具**——注册了一百个函数,如果运行时不在此刻的上下文里递出相关的那几个,模型不会用它们。所以成熟的 agent 框架都做「工具的情境化呈现」:按当前任务筛选、在正确的步骤注入、附带调用示例。**调用的发生,一半靠模型的决策,一半靠运行时的递送。**

ADHD 的启动困难同构地缺这个「递送层」。任务列表就是你注册好的函数库——但列表躺在 App 里,**不会在周二下午三点、你恰好有空档的那一刻,把「写周报」递到你面前**。你要「想起来去看列表」,而想起来恰恰是稀缺品;等你偶然看到列表,又常常是错的时机(没空档/没状态),于是看了等于没看。**注册没问题,呈现缺失——多数任务系统对 ADHD 失效,死因都在这里。**

Reclaim.ai 的机制恰好是把「呈现」自动化:任务(带时长、死线、优先级)交给它,**算法把任务转译成日历上的具体时间块,而且是动态的**——会议来了自动避让,今天没做完自动重排到下一个空档。用工程语言说:**它是你的运行时,负责在正确的时机,把正确的函数递到你眼前**——周二 15:00,日历弹出「写周报(材料在任务里)」,调用请求送达,你只需要决定「执行」。按递送层的逻辑用它:

**一、任务必须全部进系统,列表外无任务。** 递送层只能递送它知道的东西——散落在脑子里、聊天记录里、便签上的任务,对运行时不可见,永远不会被呈现。**「凡任务必注册」是这套架构的第一戒律**,配合上一篇的参数打包,注册的质量决定递送的质量。

**二、信任自动重排,消灭「补课式自责」。** 传统日程表上,没做的任务变成红色的过期项,堆积成耻辱柱;Reclaim 的重排让它悄悄挪到下一个可行空档——**这不是纵容,是工程正确**:一次调用失败,运行时应该重试,而不是把失败日志糊在你脸上。ADHD 任务系统的头号死因是「积压的过期项让人不敢打开 App」,自动重排在结构上消灭了这个死因。

**三、给「呈现」加物理音量。** 日历块无声地存在≠递送成功——**块开始时的通知必须开,且最好带声音/震动**:递送要真的送到注意力面前,而不是送到一个没人看的收件箱。对 ADHD,静默的呈现等于没有呈现。

**四、保护「决策余额」:每天的头两个递送最值钱。** 你的「接受调用」的能量有限,而算法不知道这一点——所以每天早上看一眼今天的块序列,**确认头两个块是你真正想推进的事**;不是的话手动调整。运行时递送,模型仍握否决权——这一票你要留着。

## 边界

同构强度 B 级:工具的情境化呈现是真实的 agent 框架设计,ADHD 的前瞻记忆与时机捕捉困难有文献支撑,Reclaim.ai 无 ADHD 对照研究,「递送层」是功能映射。声明:递送解决「想不起来+时机错配」,不解决「递到眼前还是点不动」——后者是启动的神经门槛,请回到评估与治疗的主线;工具叠工具之前,先确认底层的那台引擎得到了照顾。

## 今天就能试的 3 件事

1. **执行「凡任务必注册」**:现在把脑子里悬着的任务全部倒进系统,列表外清零。
2. **开日历块的声音通知**:让递送真的响,静默呈现对你无效。
3. **明早做一次「头两块审查」**:今天算法排的前两个块,是你真想推进的吗?不是就换。

函数注册好只是一半,另一半是有人在正确的时机把它递出来——**agent 靠运行时,你靠一个会自动重排的日历**。启动依然要你按下那个键,但至少从今以后,键会自己出现在你手边。

## 参考来源

- [LBD同构对：自我调节与元认知 — Self-regulatory processes in early personality development:  ↔ Self-Assessment in the Health Professions: A Reformulation a](https://doi.org/10.1017/s095457940200305x) — 证据等级：低（GRADE）
- [LBD同构对：自我调节与元认知 — Methodological Note: Neurofeedback: A Comprehensive Review o ↔ The evolution of self-control](https://doi.org/10.15412/j.bcn.03070208) — 证据等级：低（GRADE）
- [Attention-deficit/hyperactivity disorder is characterized by a delay in cortical maturation](https://doi.org/10.1073/pnas.0707741104) — 证据等级：低（GRADE）
- [The sustainability of new programs and innovations: a review of the empirical literature and recommendations for future research](https://doi.org/10.1186/1748-5908-7-17) — 证据等级：低（GRADE）

---

*本文是「ADHD × AI」系列的第 56 篇，由 Devin 基于持续维护的双域研究语料（72,739 篇论文 + LLM Wiki）亲自撰写，并持续迭代更新。*
