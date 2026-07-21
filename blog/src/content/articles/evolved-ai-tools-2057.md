---
title: "为什么用 ChatGPT 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用 是一回事？"
subtitle: "ChatGPT 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
description: "ChatGPT 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
date: "2025-05-11"
category: "AI工具实战"
categoryId: "ai-tools"
categoryEn: "AI Tools in Practice"
tags:
  - "ADHD"
  - "AI"
  - "AI工具实战"
  - "反直觉同构"
  - "效率工具"
readingTime: 14
slug: "为什么用-chatgpt-治-adhd-的任务启动困难和给-agent-套-function-calling-工具调用-是一回事"
topicId: "evolved-ai-tools-2057"
angle: "反直觉同构"
rank: 15
score: 7.99
sourceCount: 6
toolsCited:
  - "ChatGPT"
  - "Goblin Tools"
  - "Saner.AI"
  - "Lex"
  - "Mem"
  - "Otter.ai"
thesis: "ADHD大脑与LLM在结构上同构——都是高产生成核心但缺乏可靠执行调度层，因此用ChatGPT辅助任务启动困难与为agent套function calling工具调用是同一类工程：通过外部脚手架补偿执行功能缺陷。"
problem: "为什么用 ChatGPT 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用 是一回事？"
spine: "工具使用与认知卸载"
spineKind: ""
isEvolved: true
llmGenerated: false
caseStudies:
  - "孔子"
  - "王阳明"
  - "Laura Riley"
---

# 为什么用 ChatGPT 治 ADHD 的任务启动困难，和给 agent 套 function calling 是一回事？

> 启动困难的本质是「第一个动作的激活能太高」。function calling 的本质是「把高成本子任务路由给低成本执行器」。把这两句话放在一起，ChatGPT 的正确用法自己浮现了出来。

先把「启动困难」说准，因为它是 ADHD 最被误读的症状。它不是不想做——多数时候你极度想做，deadline 的火已经烧到脚面。它是想做和身体开始动之间隔着一堵透明的墙：你盯着那个任务，大脑里空转的是它的整体重量（要写的全部、要查的全部、可能搞砸的全部），而不是第一个动作。神经科学的解释指向启动这个动作本身需要的激活能：对 ADHD 的奖赏系统，一个模糊、庞大、远期回报的任务提供的激活能趋近于零。

## function calling 视角：启动是一个可以外包的子任务

LLM 遇到超出架构强项的子任务时怎么办？生成一个工具调用，让擅长的组件去干,拿回结果继续。关键洞见是：**任务里最卡的那一段，往往可以被识别为独立子任务并路由出去**。

对启动困难,最卡的那一段是什么？不是执行（一旦动起来你常常停不下来，甚至过冲成超聚焦），是**从模糊整体到第一个具体动作的转换**。这恰好是一个完美的可外包子任务——而 ChatGPT 恰好是干这个的神器：

- 「我要写年终总结，帮我把它变成一个 5 分钟就能开始的第一步」——它会说「打开空白文档，先只列你今年记得的三件事」。
- 「我有一封拖了一周不敢回的邮件,内容是 X，帮我出个草稿」——草稿烂没关系,**修改的激活能远低于从零开始**，这是被反复验证的心理学事实。
- 「我现在瘫在沙发上不想动，任务是收拾厨房，给我一个荒谬地小的开头」——「站起来,只把一个杯子放进水槽」。

三个用法的共同结构：把「转换」这个高激活能子任务路由给外部函数，你只负责消费它的返回值——一个足够小的动作。

## 为什么它有效：借来的激活能

这里有真实的机制,不只是技巧。和 ChatGPT 的对话本身是一个低门槛、即时反馈、轻度新奇的活动——恰好是 ADHD 奖赏系统的有效射程。你启动不了写报告，但你启动得了「跟 AI 聊两句报告」。对话产生的轻微投入感和清晰感，形成一小笔多巴胺预付款——用这笔预付款支付真正任务的启动费,趁热转移。**所以 60 秒规则是铁律：拿到第一步后一分钟内开始做，预付款的有效期极短。**

## 用错的形态（快速重申）

本系列已详细写过工具误用，这里只标记与启动相关的两种：把「跟 AI 聊任务」本身当成了启动（聊了五十分钟，激活能花光在对话里）；以及对每个微小任务都依赖它给开头，从不尝试自己做转换（转换能力也是肌肉,全外包会萎缩——留几个低风险任务给自己练）。判断标准依然是那一条：用完之后,你离开始更近了还是更远了。

## 边界

同构强度 B 级：function calling 是成熟工程模式，任务启动的激活能与奖赏系统解释有 ADHD 文献支撑，「对话产生启动动量」属于机制合理但未经对照研究的实践观察。老规矩：连续多日连「跟 AI 聊两句」都启动不了,那可能是抑郁发作而非普通启动困难，请找医生。

## 今天就能试的 3 件事

1. **现在就路由一个**：挑你此刻拖得最痛的任务，让 ChatGPT 给你一个 5 分钟第一步。60 秒内执行。
2. **建一条「烂草稿」快捷指令**：把「帮我为 X 写个粗糙的初稿，质量不重要」存成常用提示词。从零到一外包，从一到一百留给自己。
3. **记录一周的启动数据**：每次成功启动，记一笔用了什么方法。你会发现自己的启动函数库——那是比任何通用建议都值钱的东西。

启动困难不是懒的证据，是激活能的算术问题。而算术问题的好消息是：可以借。ChatGPT 就是那个永远开门的激活能银行——只要你借了就花，别把贷款存回它的对话框里。

## 参考来源

- [ADHD Apps: We tested 44 Apps and Here're the Best 9 in 2026](https://blog.saner.ai/best-adhd-apps/) — 证据等级：低（GRADE）
- [12 AI Personal Assistants Built for ADHD Brains (2026 Rankings)](https://www.usecarly.com/blog/best-ai-personal-assistant-adhd/) — 证据等级：低（GRADE）
- [LBD同构对：奖赏与动机 — Association of attention-deficit disorder and the dopamine t ↔ Retrospex: Language Agent Meets Offline Reinforcement Learni](https://pubmed.ncbi.nlm.nih.gov/7717410) — 证据等级：低（GRADE）
- [LBD同构对：分心与走神 — Therapeutic Doses of Oral Methylphenidate Significantly Incr ↔ AutoHallusion: Automatic Generation of Hallucination Benchma](https://doi.org/10.1523/jneurosci.21-02-j0001.2001) — 证据等级：低（GRADE）
- [LBD同构对：注意调度 — Dopamine release from the locus coeruleus to the dorsal hipp ↔ Question-guided Visual Compression with Memory Feedback for ](https://doi.org/10.1073/pnas.1616515114) — 证据等级：低（GRADE）
- ["A little bit of a life raft" – Exploring the Use and Experiences of ChatGPT as a Support Tool among Adults with ADHD](https://dl.acm.org/doi/pdf/10.1145/3764687.3764713) — 证据等级：低（GRADE）

---

*本文是「ADHD × AI」系列的第 32 篇，由 Devin 基于持续维护的双域研究语料（72,739 篇论文 + LLM Wiki）亲自撰写，并持续迭代更新。*
