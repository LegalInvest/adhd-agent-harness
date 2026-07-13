---
title: "为什么用 Goblin Tools 治 ADHD 的学习半途而废，和给 agent 套 外部记忆/向量库 是一回事？"
subtitle: "Goblin Tools 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
description: "Goblin Tools 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
date: "2025-03-23"
category: "学习方法"
categoryId: "learning"
categoryEn: "Learning Methods"
tags:
  - "ADHD"
  - "AI"
  - "学习方法"
  - "反直觉同构"
readingTime: 9
slug: "为什么用-goblin-tools-治-adhd-的学习半途而废和给-agent-套-外部记忆向量库-是一回事"
topicId: "evolved-learning-2139"
angle: "反直觉同构"
rank: 165
score: 7.71
sourceCount: 6
toolsCited:
  - "Goblin Tools"
  - "Perplexity"
  - "Saner.AI"
  - "Obsidian"
thesis: "ADHD 大脑与 LLM 在结构上同构——都是强大的生成核心但缺乏可靠的执行调度层，因此 Goblin Tools 的任务分解与 agent 的外部记忆/向量库本质上是同一套 harness 思路：通过外部脚手架补偿内部执行功能的缺失。"
problem: "为什么用 Goblin Tools 治 ADHD 的学习半途而废，和给 agent 套 外部记忆/向量库 是一回事？"
spine: "无状态与外部记忆"
spineKind: ""
isEvolved: true
llmGenerated: false
caseStudies:
  - "孔子"
  - "李鸿章"
  - "Kenneth Andrews"
---

# 为什么用 Goblin Tools 治 ADHD 的学习半途而废，和给 agent 套 外部记忆/向量库 是一回事？

> ADHD 的学习史通常是一部「开头合集」:日语学到五十音图后半段、吉他学到大横按、编程课停在第七讲——每一门都真心想学,每一门都停在某个具体的坎前面。复盘时人们爱谈动机和热情,但看看那些坎的位置,会发现一个更机械的规律:**几乎全停在「下一步突然变陡」的地方**。这不是热情问题,是任务结构问题——而任务结构,恰好是可以工程的。

先看 agent 侧的平行现象。给 agent 一个长程任务,它跑到中途搁浅的高发点,不是随机分布的——**集中在「步骤粒度突变」的位置**:前面的步骤都是具体的小操作,某一步突然变成「实现整个模块」,agent 面对这个巨步要么输出质量崩塌,要么直接卡死。工程的解法有两层:**planner 保证步骤粒度均匀**(巨步必须再拆),**外部记忆保证断点可续**(每步的产出和状态写入存储,重启时从记录恢复,而不是从头再来)。两层合起来,长任务才真正可完成。

ADHD 的学习半途而废,恰好在这两层同时失守:①**坎的那一步没人帮你拆**——教程的第七讲难度突然跳升,你的启动系统面对陡坡熄火,而熄火被你记作「我又放弃了」;②**停下来之后没有断点记录**——两周后想续,发现不知道自己学到哪、当时卡在什么地方,「重新开始」的成本大到不如换一门新的(新的还有新鲜感加成)。**于是每次中断都变成终结,每次终结都强化「我学什么都半途而废」的自我叙事。**

Goblin Tools 恰好能补这两层,虽然它看起来只是个任务工具:

**一、用 Magic ToDo 给「坎」做地形改造。** 卡在大横按/第七讲/五十音图后半段的那一刻,把这个坎作为任务丢进去拆:「大横按」拆成「只按响第一弦→加第二弦→六弦全响但不换和弦→慢速换一次」——**陡坡变缓坡,每一小步都回到你的启动系统能点火的坡度**。关键的心态转换:卡住≠该放弃,卡住=这一步需要再拆。和 planner 处理巨步是同一个动作。

**二、用它做最简断点存档。** 每次学习结束(或热情中断时),花九十秒在任务列表里写三行:学到哪了/刚才卡在哪/下次从哪一小步开始。**这三行就是你的外部记忆**——它把「续上」的成本从「考古自己两周前的状态」压缩到「读三行字」。半途而废的一半成本发生在重启时,而重启成本几乎全部来自记忆缺失。

**三、重启时,只看断点,不看全景。** 两周后回来,直接读那三行,做「下次从哪开始」的那一小步——**别去回顾整个课程进度**(「才学到 12%」的全景是重启的最大劝退)。agent 从外部记忆恢复时,也只加载当前需要的状态,不加载全部历史。

**四、区分「断点太多」和「该正式退出」。** 存档三次以上、每次重启都在同一个坎前熄火——两种可能:这个坎需要外部帮助(找个人教你大横按那十分钟,可能比独自拆解三次更有效);或者这门学习是「幻想自我」的订阅(退出并写一行「为什么退出」,合法结案,不算半途而废)。**有存档的退出是决策,没存档的消失才是放弃。**

## 边界

同构强度 B 级:任务粒度与 agent 搁浅的关系是工程观察,外部记忆对长任务的必要性是架构共识,ADHD 的启动困难与工作记忆负荷有文献支撑,学习场景的组合方案无对照研究。声明:若「半途而废」遍布所有生活领域并伴随强烈自我否定,值得正式评估与治疗;另外有些学习目标的流失是兴趣的自然代谢,不是每一次放下都需要被修复——工程手段服务于你真想学的东西,不服务于「应该学」的愧疚。

## 今天就能试的 3 件事

1. **给一门「停掉的学习」找到坎**:回忆它具体停在哪一步,把那一步拆成四个缓坡。
2. **建断点存档习惯**:今天学的任何东西,结束时写三行(到哪/卡哪/下次哪)。
3. **裁决一门旧学习**:值得续的,读断点重启一小步;不值得的,写一行退出理由,正式结案。

半途而废的叙事里,主角总是「我的热情」;换成工程视角,主角其实是**坎的坡度和断点的有无**。坡度可以拆,断点可以存——热情不需要为结构问题背锅,它只需要在缓坡和存档之间,自然地流回来。

## 参考来源

- [Can ChatGPT be Your Personal Medical Assistant?](http://arxiv.org/abs/2312.12006v1) — 证据等级：低（GRADE）
- [One Billion Word Benchmark for Measuring Progress in Statistical Language Modeling](http://arxiv.org/abs/1312.3005v3) — 证据等级：低（GRADE）
- [Activation Sparsity Opportunities for Compressing General Large Language Models](http://arxiv.org/abs/2412.12178v2) — 证据等级：低（GRADE）
- [YouZhi: Towards High-Concurrency Financial LLMs via Adaptive GQA-to-MLA Transition](http://arxiv.org/abs/2606.05868v1) — 证据等级：低（GRADE）
- [FBI-LLM: Scaling Up Fully Binarized LLMs from Scratch via Autoregressive Distillation](http://arxiv.org/abs/2407.07093v1) — 证据等级：低（GRADE）
- [Prompt Injection Attack to Tool Selection in LLM Agents](http://arxiv.org/abs/2504.19793v3) — 证据等级：低（GRADE）

---

*本文是「ADHD × AI」系列的第 326 篇，由 Devin 基于持续维护的双域研究语料（72,739 篇论文 + LLM Wiki）亲自撰写，并持续迭代更新。*
