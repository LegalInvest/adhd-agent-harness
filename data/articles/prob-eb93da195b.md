---
title: "Perplexity 之于 ADHD，就像 self-critique 验证循环 之于 LLM——但有人用错了"
subtitle: "从同构视角实测 Perplexity：它到底补上了哪一层执行功能？"
description: "从同构视角实测 Perplexity：它到底补上了哪一层执行功能？"
date: "2025-04-07"
category: "科学研究"
categoryId: "science"
categoryEn: "Scientific Research"
tags:
  - "ADHD"
  - "AI"
  - "科学研究"
  - "工具×同构"
  - "脑科学"
readingTime: 8
slug: "perplexity-之于-adhd就像-self-critique-验证循环-之于-llm但有人用错了"
topicId: "prob-eb93da195b"
angle: "工具×同构"
rank: 187
score: 7.53
sourceCount: 4
toolsCited:
  - "Goblin Tools"
  - "Saner.AI"
  - "Motion"
  - "Tiimo"
problem: "Perplexity 之于 ADHD，就像 self-critique 验证循环 之于 LLM——但有人用错了"
spine: "幻觉与验证循环"
spineKind: "llm"
isEvolved: false
llmGenerated: false
---

# Perplexity 之于 ADHD，就像 self-critique 验证循环 之于 LLM——但有人用错了

> 发出去的那份行业分析,第二天被客户一句话打回:「第三部分引的那个数据,原文说的不是这个意思。」他愣住了——那段正是他用 Perplexity 查的,答案带着引用链接,看起来无懈可击,他就直接搬了。复盘时他点开那个链接才发现:原文确实被引用了,但 AI 的概括悄悄偏了十五度。他一直以为带引用的搜索=自带验证;这次翻车教他的是:**引用只是验证的入场券,不是验证本身。**

收敛:本文只回答——**「带引用的 AI 搜索」在验证链条里的真实位置是什么?ADHD 用户(冲动决策+核对倦怠的高发人群)怎么用它才算真的过了验证关?**

## 穿透:self-critique 的工程真相,恰好是用对它的说明书

LLM 侧先讲透。self-critique 循环的设计前提是一个反直觉的事实:**生成答案的能力和验证答案的能力是两种能力**——模型常常能识别出自己刚才生成的错误(验证比生成容易),所以让它「再看一遍」有真实收益。但工程界同样清楚它的三个失效模式:①自我验证会遗传自我偏差(它检查不出自己的系统性盲区);②表面核对(检查格式与流畅度,放过事实);③**验证步骤被跳过**——当输出「看起来可信」时,下游直接消费。Perplexity 类产品的引用机制,本质是把 self-critique 的中间产物(证据链)暴露给人——**它的设计意图是邀请你当最后一环验证器,而不是替你当。**

ADHD 侧的错配点位精确:①「看起来可信」对冲动决策系统是绿灯——带链接的答案消解了怀疑的冲动,直接进剪贴板;②点开引用逐条核对是典型的「低刺激高摩擦」任务,正是 ADHD 核对倦怠的重灾区;③超聚焦赶工态里,验证环节是第一个被隧道视野裁掉的步骤。于是出现本文开头的结构:工具把验证的门递到你面前,你拿着门票走了过去,没进门。

用对的姿势,工程上叫「分级验证」:不是每条信息都全量核对(那会压垮任何人),而是**按下游风险分级**——要进交付物/要对外发言/要做决策依据的信息,强制点开引用读原文(哪怕只读关键段);仅供自己了解的背景信息,AI 概括可直接用。把有限的核对预算,花在出错代价最高的地方。

利益视角:AI 搜索产品的体验目标是「让你感觉已经得到答案」,停留时长和信任感是它的指标——「请再花三分钟读原文」不在任何产品的转化漏斗里,这道工序永远只能自己加。

## 验证

两周协议:给自己立「红线清单」——哪三类场景的信息必须读原文(如:交给客户的/涉及数字的/反常识的)?两周内记录红线场景的执行率和抓到的偏差数。多数人两周内至少抓到一次「引用偏移」——那一次就够建立肌肉记忆。可证伪:若两周全程零偏差,要么你的信息源风险低(好事),要么你的「核对」还停在扫一眼标题(用客户那种追问反查自己一次)。

## 决策

做什么:装分级验证——红线场景强制读原文,背景场景放行;把「点开引用」绑进物理流程(复制答案前先点一次链接,像 PR checklist 一样)。

不做什么:不要试图核对一切(全量核对的下场是三天后彻底放弃核对);不要因一次翻车弃用 AI 搜索——它把找证据的成本降了十倍,你只需付剩下的那一份。

先做什么:现在写下你的三条红线——什么信息必须读原文?贴在显示器边。

## 边界

「self-critique↔引用核对」为 B 级机制类比(验证与生成分离这一架构原则两侧成立,实现机制不同);AI 搜索的引用偏移率随产品与版本变化,本文不针对特定产品评测。ADHD 的核对倦怠是执行功能特征而非态度问题——分级正是为真实的预算有限而设计,不必为做不到全量核对羞耻。

## 今天就能试的 3 件事

1. 写下三条红线场景,贴在屏幕边——你的验证预算分配表。
2. 翻出最近一次直接引用 AI 搜索的交付物,现在补查那条最关键的引用——体验一次「十五度偏移」被抓住的感觉。
3. 给复制动作加一个前置仪式:复制答案前,先点开第一条引用扫十秒——把验证焊进手指的路径里。

本文服务于人生 Harness 金字塔的**执行层**:AI 搜索递给你的是证据链的入口,不是免检章——最后一道验证,永远是人的工位,而聪明的人只在贵的地方设岗。

## 参考来源

- [Attention-Deficit/Hyperactivity Disorder and Very Preterm/Very Low Birth Weight: A Meta-analysis](https://doi.org/10.1542/peds.2017-1645) — 证据等级：高（GRADE）
- [3D CNN Based Automatic Diagnosis of Attention Deficit Hyperactivity Disorder Using Functional and Structural MRI](https://doi.org/10.1109/access.2017.2762703) — 证据等级：低（GRADE）
- [Structure and Diagnosis of Adult Attention-Deficit/Hyperactivity Disorder](https://doi.org/10.1001/archgenpsychiatry.2010.146) — 证据等级：低（GRADE）
- [ENIGMA and global neuroscience: A decade of large-scale studies of the brain in health and disease across more than 40 countries](https://doi.org/10.1038/s41398-020-0705-1) — 证据等级：低（GRADE）

---

*本文是「ADHD × AI」系列的第 56 篇，由 Devin 基于持续维护的双域研究语料（72,739 篇论文 + LLM Wiki）亲自撰写，并持续迭代更新。*
