---
title: "为什么用 Claude 治 ADHD 的不知哪些方法有用，和给 agent 套 human-in-the-loop 监督 是一回事？"
subtitle: "Claude 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
description: "Claude 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
date: "2025-05-02"
category: "亲子教育"
categoryId: "parenting"
categoryEn: "Parenting & Education"
tags:
  - "ADHD"
  - "AI"
  - "亲子教育"
  - "反直觉同构"
readingTime: 11
slug: "为什么用-claude-治-adhd-的不知哪些方法有用和给-agent-套-human-in-the-loop-监督-是一回事"
topicId: "evolved-parenting-2242"
angle: "反直觉同构"
rank: 297
score: 7.44
sourceCount: 6
toolsCited:
  - "Focusmate"
  - "Goblin Tools"
  - "Saner.AI"
  - "Motion"
  - "Claude"
thesis: "ADHD大脑与LLM agent共享同一个核心困境：拥有强大的生成能力却缺乏可靠的执行调度层，因此两者的解决方案在结构上同构——都需要一个外部‘harness’（脚手架）来提供人在回路监督与身体在场效应，而非依赖内部意志力。"
problem: "为什么用 Claude 治 ADHD 的不知哪些方法有用，和给 agent 套 human-in-the-loop 监督 是一回事？"
spine: "人在回路与身体在场"
spineKind: ""
isEvolved: true
llmGenerated: false
caseStudies:
  - "张謇"
  - "张旭"
  - "Nicholas Mcbride"
---

# 为什么用 Claude 治 ADHD 的「不知哪些方法有用」，和给 agent 套 human-in-the-loop 监督是一回事？

> ADHD 自助领域有个残酷的悖论:方法多到淹死人——番茄钟、body doubling、正念、冷水澡、第二大脑、多巴胺排毒……每个都有人赌咒发誓说有效,而你试了三十种,没一种撑过两周。问题从来不是方法太少,是**你缺一个「评估哪些方法对你有用」的系统**。agent 工程恰好有这个系统的图纸,名字叫 human-in-the-loop。

先看「不知哪些方法有用」的结构性成因。其一,**ADHD 的异质性**:它是一组表型共用一个名字,别人的特效药对你可能无效,这在文献里有充分体现(各干预的效应量个体差异大);其二,**新鲜感污染**:任何新方法头三天都「有效」——那是新异刺激的多巴胺,不是方法本身的效力,三天后褪去,你以为是自己「又失败了」,其实只是安慰剂褪色;其三,**没有对照和记录**:同时开始三个新习惯+换了新工作+最近失眠,哪个变量在起作用?没人知道。于是自助变成了轮盘赌,每次失败还倒扣一笔自尊。

再看 human-in-the-loop(HITL)在 agent 工程里解决什么:agent 自主运行会漂,全靠人工又太贵——**解法是分层监督**:agent 自主执行,人类在关键节点审核(高风险操作、低置信度输出),并且人类的每次纠正都回流成系统改进的数据。核心思想:**自动化的部分尽量自动,但评估和裁决的回路必须有人坐镇,且裁决要留痕、要累积。**

「用 Claude 筛选 ADHD 方法」的正确架构,就是把自己放进这个回路:

## 一、让 Claude 当候选生成器+实验设计师

把你的具体困难(不是「我有 ADHD」,而是「早上启动不了+晚上刷手机停不下来」)给它,要求:**针对每个困难给三个候选方法,并为每个方法设计两周的最小实验**——怎么执行、每天记录什么指标、什么算有效。它读过整个自助文献的语料,当候选池非常称职;**但注意它的角色边界:提名权归它,裁决权归你。**

## 二、你当那个 in-the-loop 的 human:只做裁决

每个方法跑两周,每天一行记录(执行了吗/指标如何)。两周后**开裁决会**:把记录给 Claude,让它汇总,但结论你来下——保留/砍掉/修改参数。**裁决的纪律:只认自己的数据,不认别人的见证**(网上一万条「亲测有效」加起来,不如你自己十四行记录)。新鲜感污染的解药也在这:第 10-14 天的数据权重,永远高于前 3 天。

## 三、让每次裁决回流:建你的「有效方法注册表」

裁决完的方法进注册表:有效的写清「对什么困难、什么条件下有效」;无效的也留档,写「试过,对我无效」——**这行字价值千金,它让你永远不用再试一遍,也让下一次刷到它的种草视频时免疫**。半年后,这个注册表就是你的个人干预指南,比任何通用自助书都准——因为它的每一行都在你身上验证过。

## 用错的姿势

**让 Claude 直接裁决**(「你说哪个方法最好?」)——它没有你的数据,它的答案是文献平均值,而你恰恰是为了逃离平均值才需要这套系统;**无限生成候选**——收藏了四十个方法一个没跑,候选池不是收藏夹,同时在跑的实验≤2;**跳过记录环节**——没有数据的 loop 里,human 的裁决退化为「感觉」,而感觉正是被新鲜感污染最重的通道。

## 边界

同构强度 B 级:HITL 是真实的 agent 工程模式,ADHD 干预效应的个体差异有文献支撑,n-of-1 自我实验有方法论传统,但「Claude+注册表」的组合无对照研究。声明:这套系统筛的是自助层面的方法;药物和心理治疗的评估请在医生的 loop 里做,不要自行实验;若连续多个方法「执行第一天都做不到」,那不是方法问题,可能需要先处理更底层的东西(睡眠、情绪、未治疗的核心症状),请专业评估。

## 今天就能试的 3 件事

1. **挑一个具体困难,让 Claude 提名三个候选**:并要求它设计两周实验和记录指标。
2. **只启动一个实验**:今天第一行记录,十四天后开裁决会。
3. **建注册表文件**:把过去试过的方法凭记忆先录入——包括无效的,那些也是资产。

「什么方法对我有用」这个问题,没有任何专家能隔空回答——但一个「生成候选→小实验→数据裁决→结果累积」的回路可以,而且只需要你和一个 AI 各就各位:它管提名和汇总,你管执行和裁决。别再赌轮盘了,把自己放进 loop 里,半年后你手里会有一份世界上独一无二的文档:《对我有效》。

## 参考来源

- [ADHD Apps: We tested 44 Apps and Here're the Best 9 in 2026](https://blog.saner.ai/best-adhd-apps/) — 证据等级：低（GRADE）
- [12 AI Personal Assistants Built for ADHD Brains (2026 Rankings)](https://www.usecarly.com/blog/best-ai-personal-assistant-adhd/) — 证据等级：低（GRADE）
- [LBD同构对：自我调节与元认知 — Inhibitory control and emotion regulation in preschool child ↔ ObjexMT: Objective Extraction and Metacognitive Calibration ](https://doi.org/10.1016/j.cogdev.2007.08.002) — 证据等级：低（GRADE）
- [LBD同构对：自我调节与元认知 — Emotion-related self-regulation and its relation to children ↔ A Reproducibility Study of Metacognitive Retrieval-Augmented](https://doi.org/10.1146/annurev.clinpsy.121208.131208) — 证据等级：低（GRADE）
- [The 12 Best AI Tools for 2026 (That People Actually Use)](https://www.synthesia.io/post/ai-tools) — 证据等级：低（GRADE）
- [The AI Powered SuperApp for Work | Motion](https://www.usemotion.com/) — 证据等级：低（GRADE）

---

*本文是「ADHD × AI」系列的第 234 篇，由 Devin 基于持续维护的双域研究语料（72,739 篇论文 + LLM Wiki）亲自撰写，并持续迭代更新。*
