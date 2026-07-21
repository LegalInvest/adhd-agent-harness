---
title: "用 ChatGPT 给 ADHD 补上工具使用与认知卸载，是脚手架还是拐杖？"
subtitle: "ChatGPT 接进 ADHD 工作流：哪些交给它、哪些必须自己留着。"
description: "ChatGPT 接进 ADHD 工作流：哪些交给它、哪些必须自己留着。"
date: "2025-05-01"
category: "AI工具实战"
categoryId: "ai-tools"
categoryEn: "AI Tools in Practice"
tags:
  - "ADHD"
  - "AI"
  - "AI工具实战"
  - "权衡评测"
  - "效率工具"
readingTime: 10
slug: "用-chatgpt-给-adhd-补上工具使用与认知卸载是脚手架还是拐杖"
topicId: "prob-0ef02de363"
angle: "权衡评测"
rank: 129
score: 7.61
sourceCount: 3
toolsCited:
  - "Goblin Tools"
  - "Saner.AI"
  - "Lex"
  - "Mem"
problem: "用 ChatGPT 给 ADHD 补上工具使用与认知卸载，是脚手架还是拐杖？"
spine: "工具使用与认知卸载"
spineKind: "llm"
isEvolved: false
---

# 用 ChatGPT 给 ADHD 补上工具使用与认知卸载，是脚手架还是拐杖？

> 一个考研二战的 ADHD 学生，把「让 ChatGPT 帮我拆解今天的复习任务」变成了每天的第一个动作。三个月后他发现一件可怕的事：某天 ChatGPT 打不开，他对着书桌坐了两个小时，连「先看哪一科」都决定不了——这个决定，他已经九十天没有自己做过了。

把问题收敛到能回答的粒度：不是「该不该用 AI」，而是**同一个卸载动作，什么条件下是脚手架（用完能拆），什么条件下是拐杖（拆了就倒）？**这两种结局用的可能是同一个工具、同一个 prompt，区别不在工具里，在结构里。

## 穿透：卸载的机制两边完全对称

ADHD 侧：认知卸载（cognitive offloading）本身是被研究支持的策略——工作记忆和任务分解是 ADHD 的高成本操作，externalize 出去是合理的工程决策。但卸载有一个隐藏参数：**被卸载的功能是否还有练习机会。**肌肉不用会萎缩的说法在认知功能上要谨慎类比，但「决策路径依赖」是真实的：每天让外部系统做第一个决定，你的启动回路就每天少一次点火。

LLM/agent 侧的对应物是脚手架式训练（scaffolded learning）与工具依赖的区别：好的 harness 设计会让模型在工具辅助下完成任务，同时保留模型自身的推理步骤（先让模型给出计划，再调用工具验证）；坏的设计是直接把答案喂给模型，模型学会的是「等待注入」而不是「推理」。工程上早有共识：**辅助的位置决定了它是放大能力还是替换能力。**

谁在获利？「AI 帮你做一切」是产品叙事的最优解——依赖越深，留存越高。没有一个订阅制产品有动机提醒你「今天试试别用我」。

## 验证：怎么区分自己在哪条路上

可证伪的判据只有一个：**断供测试。**脚手架的定义是拆掉之后结构还在。N-of-1 协议：正常使用两周，记录每天的启动时间和完成量；第三周随机抽三天完全不用（提前定好，不许临时换），对比这三天的表现。三种结果：断供日只是慢一点——脚手架，继续用；断供日完全瘫痪——拐杖，需要重构用法；断供日反而更好——你外包的可能不是执行功能，是逃避的借口。

反例也要承认：对功能损害严重的时期（如重度发作期、共病抑郁），拐杖就是正确答案——骨折的人不需要被教育「别依赖拐杖」。这时请优先寻求专业评估，而不是自我训练。

## 决策

做什么：把 ChatGPT 的位置从「替你做决定」挪到「陪你做决定」——让它提问而不是给答案（「今天三科里你最不想碰哪科？为什么？」），保留你自己的最后一步拍板。

不做什么：不要把「第一个决定」外包。一天的启动决定是执行系统的点火器，可以让 AI 准备燃料（列选项、摆信息），点火必须自己来。也不要在断供测试失败后羞愧地卸载所有工具——那是从拐杖直接跳到裸奔。

先做什么：先跑断供测试，拿到自己的数据再调整用法。没有数据的「依赖焦虑」和没有数据的「工具信仰」一样不可靠。

## 边界

本文的同构是计算层的结构类比（本文未做正式 A/B/C 分级）：ChatGPT 未被证实为 ADHD 的治疗手段，认知卸载的长期效应在 ADHD 人群中尚缺乏高质量纵向研究。若你处于明显的功能损害期或伴随情绪问题，请寻求精神科/心理专业支持，工具策略不能替代临床干预。

## 今天就能试的 3 件事

1. 把你最常用的那条「帮我拆解任务」prompt 改成提问式：「问我 3 个问题，帮我自己想清楚先做什么」——今天就换。
2. 在日历上随机圈出下周的一天作为断供日，现在就圈，写上「不用 AI，记录启动时间」。
3. 今天的第一个任务决定自己做，做完后才允许打开 ChatGPT——顺序反过来，结构就反过来。

本文服务于人生 Harness 金字塔的**执行层**：目标不是少用工具，而是让工具装在正确的位置——放大你的启动权，而不是持有它。

## 参考来源

- [Machine Learning Approaches to Identify and Classify ADHD: A ...](https://www.sciepublish.com/article/pii/1040) — 证据等级：低（GRADE）
- [Executive Dysfunction by Design: A Cognitive Accessibility Analysis of AI Support vs. Healthcare Barriers](https://dl.acm.org/doi/pdf/10.1145/3663547.3749831) — 证据等级：低（GRADE）
- [ADHD and Knowledge Work: Exploring Strategies, Challenges and Opportunities for AI](https://www.cecchinato.me/wp-content/uploads/2023/08/Interact-2023_ADHD-productivity.pdf) — 证据等级：低（GRADE）

---

*本文是「ADHD × AI」系列的第 2 篇，由 Devin 基于持续维护的双域研究语料（72,739 篇论文 + LLM Wiki）亲自撰写，并持续迭代更新。*
