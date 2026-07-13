---
title: "为什么用 Lex 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用 是一回事？"
subtitle: "Lex 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
description: "Lex 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
date: "2025-03-12"
category: "AI工具实战"
categoryId: "ai-tools"
categoryEn: "AI Tools in Practice"
tags:
  - "ADHD"
  - "AI"
  - "AI工具实战"
  - "反直觉同构"
  - "效率工具"
readingTime: 10
slug: "为什么用-lex-治-adhd-的任务启动困难和给-agent-套-function-calling-工具调用-是一回事"
topicId: "prob-a99db3832c"
angle: "反直觉同构"
rank: 181
score: 7.69
sourceCount: 6
toolsCited:
  - "Lex"
  - "Goblin Tools"
  - "Saner.AI"
  - "Obsidian"
  - "Motion"
  - "Focusmate"
  - "Brain.fm"
thesis: "ADHD 大脑与 LLM/agent 都是「高产生成核心 + 不可靠执行调度层」，Lex 治 ADHD 的任务启动困难，与给 agent 加 function calling 工具调用，本质是同一种 harness：用外部脚手架把「想做的目标」翻译为「可执行的下一步」。"
problem: "为什么用 Lex 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用 是一回事？"
spine: "工具使用与认知卸载"
spineKind: ""
isEvolved: true
llmGenerated: false
isoStrength: "A"
caseStudies:
  - "孔子"
  - "文天祥"
  - "Nicole Garcia"
---

# 为什么用 Lex 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用 是一回事？

> 所有启动困难里,写作的启动困难有自己的名字:空白页恐惧。文档打开了、时间留出来了、大纲甚至都有了——光标在空白页上闪,你在椅子上僵。这个场景值得单独一篇,因为它暴露了启动困难的一个特殊成分:**有些任务的「第一步」,本身就是全任务里最难的一步**——而 function calling 的思想对这种任务有个狡猾的解法:别让自己做第一步,让工具先返回一个「可以反应的东西」。

先看工程侧这个模式。agent 处理开放式任务时,最脆弱的时刻是「从零生成第一个结构」——没有任何约束的生成,方差最大、质量最不稳定。成熟的做法是**先调用一个工具拿到「初始材料」**:检索几段相关文档、跑一个模板生成器、取一份草稿——然后让模型做它更擅长的事:**对已有材料进行批评、修改、扩写**。同一个模型,「从零写」和「改一份烂稿」的表现差距巨大,因为后者把开放式生成转化成了有锚点的编辑。**先调用,再反应——这是对付「第一步最难」型任务的标准架构。**

写作的空白页问题,机制完全平行。对 ADHD 尤甚:开放式任务的启动需要同时做无数个微决策(从哪开始?什么语气?第一句怎么写?)——**决策的并发数超过工作记忆容量,系统直接挂起**,这就是「僵住」的时刻。而一旦页面上有了任何东西——哪怕是一段写得很差的开头——任务性质立刻改变:从「创造」变成「反应」,从并发决策变成逐个修改,启动门槛断崖式下降。**很多 ADHD 写作者早就自发发现:「我不会开始写,但我很会改。」——这不是缺陷,这是你的调用顺序应该反过来的信号。**

Lex 这类 AI 写作编辑器,恰好把「先调用再反应」内置成了工作流:写不动的地方按一下,它续写一段;开头卡住,让它先扔三个版本的开头;写完让它当编辑批注。按这个架构用:

**一、把「让它先写」正式合法化为你的第一步。** 打开文档的标准动作不再是「开始写」,而是**「让它生成一个可以反应的烂开头」**——注意心态:你不是在要一个好开头,是在要一个锚点。它写得平庸反而是好事:「这也太平了,应该是——」的那股嫌弃劲儿,就是你的启动能量。**嫌弃比创造容易点燃,这是被低估的写作动力学。**

**二、卡住时调用,别硬扛。** 写到一半僵住(ADHD 写作的第二死点:中途的每个段落衔接都是一次小启动),按续写——**它给的方向哪怕是错的,「不对,其实应该往这边」的反驳也会把你重新点着**。工具的价值一半在内容,一半在打破僵持的状态本身。

**三、你写的和它写的,主权要分清。** 反应式写作的风险是滑成「全程让它写,我只点头」——那产出的是它的平均水平,不是你的东西。协议:**它的文字默认全部要被你改写**,保留的每一句都必须过你的手;它是脚手架和陪练,署名的人是你。

**四、编辑模式收尾。** 完稿后让它跑一遍:逻辑断点?冗余段落?语气不一致?——ADHD 的自我校对经常跳行漏读,外部验证层在写作上格外划算。

## 边界

同构强度 B 级:「先取材料再编辑」是真实的 agent 设计模式,开放式任务的决策负荷与 ADHD 启动困难的关系有执行功能文献支撑,Lex 本身无对照研究,「反应式写作」是功能映射。声明:写作瘫痪若伴随强烈的完美主义焦虑或自我审查(每句都觉得配不上发表),那一层值得和咨询师谈——工具解决启动力学,不解决「我写的东西没价值」这个信念;后者是认知议题,不是流程议题。

## 今天就能试的 3 件事

1. **下次写作,第一个动作是「要一个烂开头」**:让 AI 先扔三个版本,挑最不烂的开始嫌弃。
2. **建立「卡住即调用」反射**:僵住超过两分钟,按续写,用反驳重新点火。
3. **给成稿跑一次编辑调用**:逻辑、冗余、语气三项,让它批注,你裁决。

空白页恐惧的解法,不是更勇敢地面对空白,是**别让页面空着**——先调用,拿到一个可以嫌弃的东西,然后用你最擅长的「反应」接管。从零创造是神话,从锚点出发是工程。

## 参考来源

**同构强度：A 级** —— 直接文献支撑（引用 ADHD↔LLM 同构专题研究）

- [ADHD Apps: We tested 44 Apps and Here're the Best 9 in 2026](https://blog.saner.ai/best-adhd-apps/) — 证据等级：低（GRADE）
- [12 AI Personal Assistants Built for ADHD Brains (2026 Rankings)](https://www.usecarly.com/blog/best-ai-personal-assistant-adhd/) — 证据等级：低（GRADE）
- [Human-like Working Memory Interference in Large Language Models](https://arxiv.org/pdf/2604.09670) — 证据等级：低（GRADE）
- [Working Memory Identifies Reasoning Limits in Language Models](https://aclanthology.org/2024.emnlp-main.938.pdf) — 证据等级：低（GRADE）
- [TRANSFORMER MECHANISMS MIMIC FRONTOSTRIATAL GATING OPERATIONS WHEN TRAINED ON HUMAN WORKING MEMORY TASKS](https://openreview.net/pdf?id=CN2bmVVpOh) — 证据等级：低（GRADE）
- [Executive Dysfunction by Design: A Cognitive Accessibility Analysis of AI Support vs. Healthcare Barriers](https://dl.acm.org/doi/pdf/10.1145/3663547.3749831) — 证据等级：低（GRADE）

---

*本文是「ADHD × AI」系列的第 61 篇，由 Devin 基于持续维护的双域研究语料（72,739 篇论文 + LLM Wiki）亲自撰写，并持续迭代更新。*
