---
title: "为什么用 ChatGPT 治 ADHD 的日常混乱不稳定，和给 agent 套 调低采样温度 是一回事？"
subtitle: "ChatGPT 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
description: "ChatGPT 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
date: "2025-05-20"
category: "生活方式"
categoryId: "lifestyle"
categoryEn: "Lifestyle"
tags:
  - "ADHD"
  - "AI"
  - "生活方式"
  - "反直觉同构"
  - "人际关系"
readingTime: 7
slug: "为什么用-chatgpt-治-adhd-的日常混乱不稳定和给-agent-套-调低采样温度-是一回事"
topicId: "evolved-lifestyle-2264"
angle: "反直觉同构"
rank: 47
score: 7.8
sourceCount: 6
toolsCited:
  - "Routinery"
  - "Habitica"
  - "Goblin Tools"
  - "Motion"
  - "Reclaim.ai"
thesis: "ADHD大脑与LLM共享同一核心困境：两者都是强大的生成引擎，但缺乏可靠的执行调度层。因此，为ADHD大脑搭建外部脚手架（如任务分解、时间锚点），与给LLM agent调低采样温度、套上规划循环，本质上是同一类工程——用结构化的外部系统约束高熵的生成核心。"
problem: "为什么用 ChatGPT 治 ADHD 的日常混乱不稳定，和给 agent 套 调低采样温度 是一回事？"
spine: "采样温度与表现波动"
spineKind: ""
isEvolved: true
llmGenerated: false
caseStudies:
  - "孔子"
  - "张居正"
  - "陈霞"
---

# 为什么用 ChatGPT 治 ADHD 的日常混乱不稳定，和给 agent 套调低采样温度是一回事？

> 工程师想让 LLM 输出稳定时,动的第一个参数是采样温度:调低它,输出从天马行空收敛到可预期。ADHD 的日常混乱——作息漂移、习惯断裂、每天像新的一天从零开始——本质上也是一个「温度过高」的系统:每个时刻都在全量可能性里重新采样,而不是沿着既有轨道走。

先看「日常混乱不稳定」的采样视角。神经典型者的日常,大部分决策是「低温」的:几点起、早餐吃什么、到工位先干什么——这些被习惯固化成默认路径,基本不消耗决策资源。ADHD 的日常则常年「高温」:**每个决策点都是开放的**——几点睡?今晚可能刷手机到两点也可能十点就困;先干什么?可能是正事也可能突然开始重新整理书架。习惯难以自动化(ADHD 的习惯养成比常人慢且脆),导致每天都要在无数分叉口现场采样,采样结果又受当天状态调制——于是日常呈现出高方差:好的日子行云流水,坏的日子从起床就散架。

这里的同构点很实在:LLM 的温度参数控制的是「从概率分布里选下一个 token 时的随机性」;调低温度=让高概率路径胜出,输出可预期。人当然没有温度旋钮,但**「减少每个决策点的开放性」这件事,功能上等价于降温**——路径被预先固定得越多,现场采样就越少,日常方差就越小。ChatGPT 在这里的角色,是帮你把「降温结构」设计出来:

## 给日常降温的四个工程点

**第一点:锚点作息,不是全日计划表**。全天排满的时间表对 ADHD 是必崩的(一处失守全盘皆输,然后弃疗)。降温的正确粒度是**锚点**:每天只固定三四个不可移动的桩(起床时间、开工仪式、晚饭、关机仪式),桩与桩之间保留自由。让 ChatGPT 帮你设计:「根据我的生活,帮我选四个最值得固定的日常锚点,每个配一个两分钟的固定动作。」锚点的作用是把一天从「无限开放」切成几段「有边界的开放」——**温度不必降到零,降到方差可控就赢了。**

**第二点:预制默认选项,消灭现场采样**。日常混乱的大头来自高频小决策(吃什么、穿什么、先干哪个)。给高频决策预制默认值:早餐固定两选一、工作日着装模板化、「到工位第一个动作」永远是同一个。可以让 ChatGPT 一次性帮你把「本周晚餐七选」「明早的前三个动作」排出来。**默认值不剥夺自由——你随时可以偏离——它只是把「必须现场决定」改成「不决定也能走」**,这正是低温采样的含义:高概率路径兜底。

**第三点:给「脱轨」预写回轨协议**。ADHD 日常管理的真正杀手不是脱轨(必然发生),是**脱轨后的全盘崩溃**——一次熬夜→第二天全乱→「这周废了」→彻底弃疗。这相当于系统没有异常处理。预先和 ChatGPT 写好回轨协议:「如果我熬夜了/错过锚点了,最小回轨动作是什么?」答案要小得可笑(「不管几点醒,先执行开工仪式那两分钟」)。**回轨协议的核心思想:脱轨只污染脱轨的那一段,不许它污染叙事**——「今天从现在开始」永远合法。

**第四点:每周一次「温度复盘」**。周日 10 分钟,和 ChatGPT 过一遍:哪些锚点守住了?哪个决策点本周采样最失控(最该加默认值)?下周只改一处。**一次只拧一个旋钮**——同时上马五个新习惯是 ADHD 式的经典高温行为,它本身就违反降温原则。

## 一个重要的反面告诫:别把温度调到零

有人会把降温做成军事化管理:全日程、全默认、零弹性——两周后系统性报复(报复性熬夜、报复性摆烂)。记住工程事实:**温度为零的模型输出无聊且脆,遇到分布外输入表现更差**。ADHD 的新奇需求是真实的神经需求,降温设计必须给它留出口:锚点之间的自由段、每周的「无计划时段」、默认值的「今天就想换」豁免权。目标从来不是把你改造成规律的人,是**让混乱发生在无害的区段里**。

## 边界

同构强度 B 级:温度参数是真实工程机制,ADHD 的习惯养成困难与日常执行方差有文献支撑,「锚点+默认值+回轨协议」属机制映射的实践,无对照研究。注意:作息混乱若已达到昼夜节律紊乱量级(长期凌晨三四点入睡、白天功能受损),或伴随情绪周期,请专业评估——那一层是生理问题,结构设计是辅助不是治疗。

## 今天就能试的 3 件事

1. **选你的四个锚点**:今天和 ChatGPT 定下来,每个配两分钟固定动作。明天只守锚点,其余随意。
2. **给一个最失控的高频决策装默认值**:比如「到家后第一个动作」。预制好,明天试跑。
3. **预写你的回轨协议**:「脱轨后的最小回轨动作」,写下来贴在看得见的地方。它会在你最需要的那天救场。

混乱不是你的本性,是系统温度没人管的自然结果。不必羡慕那些「天生规律」的人——他们只是出厂温度低。你的旋钮在结构里:几个锚点、一批默认值、一份回轨协议,方差就从「失控」降到「有风格」。

## 参考来源

- [AI for ADHD: Best Tools, Apps, and Strategies - Themba Tutors](https://thembatutors.com/ai-for-adhd-tools-and-apps/) — 证据等级：低（GRADE）
- [11 Best ADHD Productivity Apps for Fluctuating Energy - rivva blog](https://blog.rivva.app/p/11-best-adhd-productivity-apps-for) — 证据等级：低（GRADE）
- [ADHD Apps: We tested 44 Apps and Here're the Best 9 in 2026](https://blog.saner.ai/best-adhd-apps/) — 证据等级：低（GRADE）
- [12 AI Personal Assistants Built for ADHD Brains (2026 Rankings)](https://www.usecarly.com/blog/best-ai-personal-assistant-adhd/) — 证据等级：低（GRADE）
- [Agent Scaffolding: Architecture and Design Patterns for Agentic AI](https://zbrain.ai/agent-scaffolding/) — 证据等级：低（GRADE）
- [LBD同构对：任务分解与规划 — Attention-deficit/hyperactivity disorder is characterized by ↔ Language-conditioned world model improves policy generalizat](https://doi.org/10.1073/pnas.0707741104) — 证据等级：低（GRADE）

---

*本文是「ADHD × AI」系列的第 158 篇，由 Devin 基于持续维护的双域研究语料（72,739 篇论文 + LLM Wiki）亲自撰写，并持续迭代更新。*
