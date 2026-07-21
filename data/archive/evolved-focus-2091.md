---
title: "为什么用 Perplexity 治 ADHD 的注意力涣散，和给 agent 套 上下文工程 是一回事？"
subtitle: "Perplexity 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
description: "Perplexity 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
date: "2025-04-02"
category: "专注力管理"
categoryId: "focus"
categoryEn: "Focus Management"
tags:
  - "ADHD"
  - "AI"
  - "专注力管理"
  - "反直觉同构"
  - "专注力"
readingTime: 7
slug: "为什么用-perplexity-治-adhd-的注意力涣散和给-agent-套-上下文工程-是一回事"
topicId: "evolved-focus-2091"
angle: "反直觉同构"
rank: 161
score: 7.71
sourceCount: 6
toolsCited:
  - "Perplexity"
  - "Focusmate"
  - "RescueTime"
  - "Brain.fm"
  - "Forest"
thesis: "ADHD大脑与LLM/agent都是高产但缺乏内置调度层的生成核心，两者都需要外部上下文工程（harness）来补偿执行功能缺陷，Perplexity治ADHD与agent上下文工程本质上是同一套同构方案。"
problem: "为什么用 Perplexity 治 ADHD 的注意力涣散，和给 agent 套 上下文工程 是一回事？"
spine: "上下文工程"
spineKind: ""
isEvolved: true
llmGenerated: false
caseStudies:
  - "曾国藩"
  - "孔子"
  - "辛梅"
---

# 为什么用 Perplexity 治 ADHD 的注意力涣散，和给 agent 套 上下文工程 是一回事？

> 注意力涣散的第三张面孔,发生在你查东西的时候:本来只想确认一个数据,四十分钟后你在第十四个标签页里读一篇完全无关的文章,而最初那个问题还没有答案。内容污染、调度污染之外,这是第三种——检索污染:每一次信息获取行为,都在向你的注意力窗口倾倒计划外的内容。上下文工程对这件事有一条铁律,而 Perplexity 恰好是这条铁律的产品化。

先看铁律。给 agent 接检索工具时,工程师踩过一个大坑:**把搜索引擎的原始结果页直接塞进模型上下文,模型的表现立刻劣化**——结果页里的广告、无关摘要、诱导性标题,全部成为干扰源,模型开始跟着无关内容跑偏。成熟的做法是**检索净化**:工具层负责查询、筛选、去重、压缩,**只把「与问题直接相关的精炼结果」注入上下文**——模型永远不直接接触原始的、未过滤的信息流。一句话:**上下文的入口处必须站一个过滤器。**

现在看你的检索行为。传统搜索的使用方式,等于把原始结果页直接塞进自己的注意力窗口:十条蓝链接、每条都可点、侧栏还有推荐——对 ADHD 的新异刺激敏感性来说,**每个链接都是一次注入攻击的候选**。「查一个数据」的旅程于是变成:点开第一条→页面里另一个标题更有趣→点过去→那篇文章推荐了第三篇……你的窗口在四十分钟里被倾倒了几十条计划外内容,而这一切的启动理由只是「确认一个数字」。检索污染的可怕在于它自带正当性:**每一步都像在「查资料」,整段旅程却是一次注意力的失血。**

Perplexity 的架构恰好把过滤器补上了:一个问题进去,**返回的是一份已经综合、压缩、带引用的答案**——没有结果页,没有十个入口,没有推荐流。你的窗口接触到的,是净化后的精炼结果,不是原始信息流。用上下文工程的语言说:**它把「检索」从窗口内的漫游行为,变成了窗口外的工具调用。**

但工具只是过滤器,使用纪律决定它是否真的挡住污染:

**一、带着「一句话问题」进,不带话题进。** 「查一下 XX 政策」是话题,会滑向漫游;「XX 政策对 YY 情况的截止日期是哪天」是问题,有明确的闭合条件。**进入检索前先写下这句话**——它是你此行的验收标准,也是「该走了」的判断依据。

**二、答案落地,立即离场。** 拿到答案→抄进你正在做的事里(文档、任务、笔记)→关掉。**引用链接只在「答案存疑」时点开验证,不在「好像有意思」时点开阅读**——前者是核查,后者是污染的开始。想读的,进稍后读清单,不是现在。

**三、追问要收敛,不要发散。** 同一线程里的追问是它的优势,但只允许「向答案更深处」的追问(「这个日期有例外吗」),不允许「向旁边」的追问(「顺便问下相关的另一件事」)——**旁边的事开新线程,而且通常应该是「稍后」的新线程。**

用错的姿势:**把它当阅读器**(每天在里面「随便问问」当消遣——过滤器被你用成了新的信息流);**查证强迫**(同一件事换五种问法反复确认——那不是检索需求,是焦虑在借检索的壳,见前面批次的讨论);**查完不落地**(答案看完就关,三天后同一个问题再查一遍——检索的产出必须写进某个会被再次看到的地方)。

## 边界

同构强度 B 级:未过滤检索结果对 agent 表现的劣化与检索净化的实践是真实的,ADHD 对新异刺激的敏感性有文献支撑,Perplexity 无 ADHD 对照研究,「检索污染」是本文的操作性描述。声明:若发现自己无法控制的反复查证(健康、安全类尤甚),那可能是焦虑谱系的模式,值得专业评估;工具减少的是环境诱饵,不处理冲动的源头。

## 今天就能试的 3 件事

1. **下次查东西前,先写一句话问题**:写不出来,说明你要的是漫游不是答案——那就别假装在查资料。
2. **执行「落地即离场」**:答案抄进正事里,关窗,全程目标十分钟内。
3. **给「有意思但无关」的内容建稍后读清单**:漫游欲望不必消灭,给它一个不在现在的出口。

检索本该是给注意力窗口供给养分的管道,不该是倒垃圾的口子。**在管道上装一个过滤器,再配三条使用纪律**——四十分钟的失血,能收回三十五分钟。剩下五分钟拿到答案,这才叫查资料。

## 参考来源

- [ADHD Apps: We tested 44 Apps and Here're the Best 9 in 2026](https://blog.saner.ai/best-adhd-apps/) — 证据等级：低（GRADE）
- [Meta-Analysis of fMRI Studies of Disruptive Behavior Disorders](https://doi.org/10.1176/appi.ajp.2016.15081089) — 证据等级：高（GRADE）
- [Nonlinear Complexity Analysis of Brain fMRI Signals in Schizophrenia](https://doi.org/10.1371/journal.pone.0095146) — 证据等级：低（GRADE）
- [Revolutionizing ADHD Management with AI Assistants](https://neurolaunch.com/adhd-ai-assistant/) — 证据等级：低（GRADE）
- [Toward Neurodivergent-Aware Productivity: A Systems and AI-Based Human-in-the-Loop Framework for ADHD-Affected Professionals](https://arxiv.org/pdf/2507.06864) — 证据等级：低（GRADE）
- [Using an AI Assistant to Manage ADHD: A Practical Guide](https://www.lobsterfarm.ai/guides/ai-for-adhd/) — 证据等级：低（GRADE）

---

*本文是「ADHD × AI」系列的第 322 篇，由 Devin 基于持续维护的双域研究语料（72,739 篇论文 + LLM Wiki）亲自撰写，并持续迭代更新。*
