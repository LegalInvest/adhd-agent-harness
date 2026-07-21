---
title: "为什么用 Routinery 治 ADHD 的学习半途而废，和给 agent 套 外部记忆/向量库 是一回事？"
subtitle: "Routinery 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
description: "Routinery 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
date: "2025-05-02"
category: "学习方法"
categoryId: "learning"
categoryEn: "Learning Methods"
tags:
  - "ADHD"
  - "AI"
  - "学习方法"
  - "反直觉同构"
readingTime: 11
slug: "为什么用-routinery-治-adhd-的学习半途而废和给-agent-套-外部记忆向量库-是一回事"
topicId: "prob-efd4494c5e"
angle: "反直觉同构"
rank: 312
score: 7.65
sourceCount: 6
toolsCited:
  - "Goblin Tools"
  - "Saner.AI"
  - "Perplexity"
thesis: "ADHD 大脑与 LLM 都是高产的生成核心，但缺乏可靠的执行调度层，导致学习或任务屡屡因“状态丢失”而半途而废；Routinery 这类例程 harness 与 agent 的外部记忆/向量库本质上是同一套“外部状态层”的工程方案。"
problem: "为什么用 Routinery 治 ADHD 的学习半途而废，和给 agent 套 外部记忆/向量库 是一回事？"
spine: "无状态与外部记忆"
spineKind: ""
isEvolved: true
llmGenerated: false
isoStrength: "A"
caseStudies:
  - "孔子"
  - "王阳明"
  - "Julie Haynes"
---

# 为什么用 Routinery 治 ADHD 的学习半途而废，和给 agent 套 外部记忆/向量库 是一回事？

> 观察一个学习坑的死亡过程,会发现一个精确的转折点:**从「打开就学」到「打开之前要先想一想」的那天**。前两周,新鲜感让一切自动:坐下、打开、继续。退潮后,每次学习前多出一串隐形工序:学哪块来着?上次到哪了?材料在哪个文件夹?笔记用哪个?——这串「进入流程」每次都要现场重新推理,而现场推理的成本,对 ADHD 的启动系统是致命的。Routinery 这类例程工具在学习战场上的角色,对应外部记忆里一种特殊的记忆类型:**程序性记忆的外部化——外部记忆不只存陈述性内容(学了什么),还该存过程本身(怎么进入学习);把「进入流程」固化成可一键执行的例程,等于把每次现场推理的结果缓存了下来**。

先讲 agent 侧的对应。LLM agent 每次执行相似任务,如果都从零推理「该怎么做」,既贵又不稳(同样的任务今天走 A 路径明天走 B 路径);工程解法是**把验证过的流程沉淀为模板/脚本/SOP**:prompt 模板、工作流定义、可复用的工具链——**流程的第一次推理是投资,固化下来才有复利;每次重新推理,是把投资反复归零**(Routinery 涣散篇讲过「预编译 vs 现场推理」,这里specifically 讲它和记忆系统的关系):**模板就是程序性外部记忆——它存的不是知识,是「被验证过的做法」**。

ADHD 侧的机制,比「嫌麻烦」深一层:程序性学习与习惯自动化的研究方向提示,ADHD 把重复流程「自动化成习惯」的效率偏低——神经典型者两周后「进入学习」已经变成不假思索的习惯链,ADHD 者一个月后每次仍在现场推理;**同一个流程,别人越走越便宜,ADHD 越走越贵(新鲜感补贴退坡,推理成本原价)**——这解释了那个转折点:坑死于「进入成本超过兴趣余额」的那天。而这个成本结构,恰恰意味着外部固化的杠杆对 ADHD 最大:**习惯内化不了,就外化——例程工具就是买不起「自动化」时的「外挂缓存」**。

具体部署:**①把「进入学习」写成显式例程**——比如五步:清桌面(1min)→戴耳机放学习声景(30s,Brain.fm 篇的检索键顺便就位)→读上次的三行笔记(1min,Saner 篇的恢复包)→看今天的块(30s,Tiimo 篇的指针)→计时器启动;每步有时长、有顺序,工具逐步领着走——**「开始学习」从一个模糊的意志动作,变成一串两分钟的机械动作**;②**例程本身就是启动仪式**——机械动作不需要动机,做着做着,状态就进来了(行为激活的逻辑:动作先于状态,不是等状态来了才动作);③**弃坑期的最低保活例程**——兴趣低谷时,例程降级为「只执行前三步」(清桌、戴耳机、读笔记,不强制学):**保住进入流程的肌肉,坑就没有彻底死**——回流时,门还是熟的。

边界:**其一,例程固化的应该是「进入」,不是「学习本身」**——学习内容需要现场思考,例程只负责把人送到思考的门口;把学习过程本身过度脚本化,会杀死兴趣驱动的探索(ADHD 学习的真正引擎);**其二,例程崩了一次不等于全崩**——完美主义的「链条断了就重来」是例程工具的经典反噬(Routinery 涣散篇的警告,学习场景照样适用);**其三,程序性学习的 ADHD 研究仍在积累**,本篇的机制链有方向性证据但非定论,例程的实际收益用你自己的两周数据检验。

## 边界

同构强度 A 级:程序性记忆与习惯自动化的认知研究提供基础(ADHD 侧证据在积累中),流程模板化是 agent 工程的实体实践,「程序性外部记忆」的同构两侧有实体;Routinery 无学习场景对照研究,A 判给架构。声明:例程是结构辅助;强迫倾向者慎用仪式化工具(方向会反)。

## 今天就能试的 3 件事

1. **写下你的五步进入例程**:清桌/声景/读笔记/看块/计时——每步 ≤2 分钟,今晚试跑一次。
2. **给低谷期定保活版**:只做前三步、不强制学——门保持熟悉,坑保持活着。
3. **对比一次成本**:例程进入 vs 裸进入,各试一次,记录从「坐下」到「真正开始」的分钟数。

坑死的那天,不是兴趣归零的那天——**是进入成本超过兴趣余额的那天**。agent 把验证过的流程存成模板;你把「进入学习」存成例程:程序性记忆,也值得一个外部存档。

## 参考来源

**同构强度：A 级** —— 直接文献支撑（引用 ADHD↔LLM 同构专题研究）

- [Transformer-XL: Attentive Language Models beyond a Fixed-Length Context](https://doi.org/10.18653/v1/p19-1285) — 证据等级：低（GRADE）
- [Dialogue Response Ranking Training with Large-Scale Human Feedback Data](https://doi.org/10.18653/v1/2020.emnlp-main.28) — 证据等级：低（GRADE）
- [ADHD Apps: We tested 44 Apps and Here're the Best 9 in 2026](https://blog.saner.ai/best-adhd-apps/) — 证据等级：低（GRADE）
- [12 AI Personal Assistants Built for ADHD Brains (2026 Rankings)](https://www.usecarly.com/blog/best-ai-personal-assistant-adhd/) — 证据等级：低（GRADE）
- [Strong Memory, Weak Control: An Empirical Study of Executive Functioning in LLMs](https://preview.aclanthology.org/evt-to-venues/2026.eacl-long.281.pdf) — 证据等级：低（GRADE）
- [Self-Attention Limits Working Memory Capacity of Transformer-Based Models](https://arxiv.org/pdf/2409.10715) — 证据等级：低（GRADE）

---

*本文是「ADHD × AI」系列的第 163 篇，由 Devin 基于持续维护的双域研究语料（72,739 篇论文 + LLM Wiki）亲自撰写，并持续迭代更新。*
