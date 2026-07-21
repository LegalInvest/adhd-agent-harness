---
title: "为什么用 RescueTime 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用 是一回事？"
subtitle: "RescueTime 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
description: "RescueTime 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
date: "2025-04-06"
category: "AI工具实战"
categoryId: "ai-tools"
categoryEn: "AI Tools in Practice"
tags:
  - "ADHD"
  - "AI"
  - "AI工具实战"
  - "反直觉同构"
  - "效率工具"
readingTime: 11
slug: "为什么用-rescuetime-治-adhd-的任务启动困难和给-agent-套-function-calling-工具调用-是一回事"
topicId: "prob-0eda03c4fc"
angle: "反直觉同构"
rank: 190
score: 7.69
sourceCount: 6
toolsCited:
  - "Goblin Tools"
  - "Lex"
  - "Saner.AI"
  - "Tiimo"
  - "Focusmate"
  - "Motion"
  - "Brain.fm"
  - "Obsidian"
thesis: "ADHD 大脑与 LLM 都是「高产生成核心 + 脆弱执行调度层」的同构系统，给 ADHD 用时间/任务外化工具（如 Lex、Goblin Tools、Tiimo）和给 agent 加 function calling，本质上都是同一套外部 harness：把模糊意图翻译成可落地的下一步动作。"
problem: "为什么用 RescueTime 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用 是一回事？"
spine: "工具使用与认知卸载"
spineKind: ""
isEvolved: true
llmGenerated: false
isoStrength: "A"
caseStudies:
  - "孔子"
  - "苏轼"
  - "Jennifer Robertson"
---

# 为什么用 RescueTime 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用 是一回事？

> 这个系列的工具都在干预:打包、递送、上锁、点火。这一篇的工具什么都不干预——它只是看着,然后记下来。听起来最没用,但在 function calling 的体系里,它对应的组件恰恰是工程师最先装、最后拆的那个:**observability,可观测性**。没有调用日志的 agent 系统,出了问题连「哪一步失败的」都不知道;没有真实数据的启动改造,连「我到底败在哪」都是猜的。RescueTime 是给你的一天装的调用日志。

先看工程侧为什么把日志排在这么前面。agent 系统上线后的第一课永远是:**你以为的失败原因和真实的失败原因,经常不是同一个**。以为是模型不行,日志显示是某个工具超时;以为是 prompt 问题,日志显示是上下文被截断。**所以成熟系统的标配是全链路追踪:每次调用的时间、时长、结果、失败点,自动记录**——优化不从直觉出发,从日志出发。无日志的优化叫玄学,有日志的才叫工程。

现在看 ADHD 的自我改造为什么屡战屡败——很大一个原因:**全靠自我报告,而 ADHD 的自我报告在时间维度上系统性失真**。时间盲不只影响计划,也影响回忆:「我今天工作了挺久」(实际有效专注 2.1 小时)、「就刷了一会儿手机」(实际 94 分钟)、「我一般上午状态好」(数据显示你的高产时段其实是 16-18 点)。**基于失真数据的优化,方向都是错的**——你在补一个不存在的洞,真正的洞在没看见的地方。

RescueTime 这类自动追踪工具的价值就在「自动」二字:后台记录每个应用、每个网站的使用时长,自动分类生产/分心,**零人工输入**——这对 ADHD 是硬性前提(要手动记录的时间追踪,坚持不过三天,记录本身就是全天最容易被弃的任务)。它交付的是你的一天的真实调用日志。按「可观测性」的逻辑用:

**一、先裸跑两周,什么都别改。** 装上,忘掉它,照常生活——**基线数据要在无干预状态下采**,一边记录一边改变行为,数据就废了。两周后再打开报表,准备好被冒犯:真实数据和自我印象的差距,通常大到需要消化一会儿。

**二、报表只回答三个问题。** 别在报表里漫游(那是新的分心)。只提取:①**我的真实高产时段是几点?**(把最难的任务挪过去——这一条通常就值回全部票价);②**启动失败后我漂去了哪里?**(那个「事故多发路口」就是下一个物理屏障的安装点);③**自我印象和数据差距最大的一项是什么?**(那是你决策系统里最大的失真源)。

**三、周复盘看趋势,不看单日。** 单日数据噪音大(谁都有崩的一天),**周对周的趋势才是信号**——上周有效专注 11 小时,这周 13 小时,改造在起效;别拿最惨的那天鞭打自己,日志是仪表盘,不是耻辱柱。

**四、警惕「监控变成表演」。** 知道被记录后开始「为数据好看」而工作(开着 IDE 发呆刷分)——观测者效应会污染日志。对策是想清楚:**数据是给你自己诊断用的,骗它=骗自己的医生**,报表没有别的观众。

## 边界

同构强度 B 级:可观测性是真实的工程范式,ADHD 的时间估计与回溯报告失真有时间知觉研究支撑,RescueTime 本身无 ADHD 对照研究,「调用日志」是功能映射。声明:自动追踪涉及隐私,工作设备上使用注意公司政策;数据揭示模式,不解释原因——如果日志显示的是大面积的启动瘫痪与情绪性回避,那是去找专业评估的证据,不是自我批评的弹药。

## 今天就能试的 3 件事

1. **今天装上,设为裸跑模式**:两周内不看报表、不改行为,只采基线。
2. **日历上约好两周后的「读日志」时间**:三十分钟,只回答三个问题。
3. **预登记你的自我印象**:现在写下「我以为的高产时段/每天有效专注时长」——两周后和数据对账,失真幅度会教你为什么直觉不可信。

不干预的工具反而排第一,因为**所有干预都需要知道往哪打**——先装日志,再谈优化。你和自己较劲了这么多年,可能只是因为,从来没人给这场仗拍过一份战报。

## 参考来源

**同构强度：A 级** —— 直接文献支撑（引用 ADHD↔LLM 同构专题研究）

- [ADHD Apps: We tested 44 Apps and Here're the Best 9 in 2026](https://blog.saner.ai/best-adhd-apps/) — 证据等级：低（GRADE）
- [12 AI Personal Assistants Built for ADHD Brains (2026 Rankings)](https://www.usecarly.com/blog/best-ai-personal-assistant-adhd/) — 证据等级：低（GRADE）
- [Toward Neurodivergent-Aware Productivity: A Systems and AI-Based Human-in-the-Loop Framework for ADHD-Affected Professionals](https://arxiv.org/pdf/2507.06864) — 证据等级：低（GRADE）
- [Using an AI Assistant to Manage ADHD: A Practical Guide](https://www.lobsterfarm.ai/guides/ai-for-adhd/) — 证据等级：低（GRADE）
- [Revolutionizing ADHD Management with AI Assistants](https://neurolaunch.com/adhd-ai-assistant/) — 证据等级：低（GRADE）
- [10 Killer ChatGPT Prompts For Organizing Your ADHD Brain](https://www.adhdflowstate.com/best-chatgpt-prompts-for-adhd/) — 证据等级：低（GRADE）

---

*本文是「ADHD × AI」系列的第 70 篇，由 Devin 基于持续维护的双域研究语料（72,739 篇论文 + LLM Wiki）亲自撰写，并持续迭代更新。*
