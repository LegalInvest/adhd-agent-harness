---
title: "为什么用 Saner.AI 治 ADHD 的不知哪些方法有用，和给 agent 套 human-in-the-loop 监督 是一回事？"
subtitle: "Saner.AI 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
description: "Saner.AI 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
date: "2025-04-06"
category: "亲子教育"
categoryId: "parenting"
categoryEn: "Parenting & Education"
tags:
  - "ADHD"
  - "AI"
  - "亲子教育"
  - "反直觉同构"
  - "ADHD儿童"
readingTime: 11
slug: "为什么用-sanerai-治-adhd-的不知哪些方法有用和给-agent-套-human-in-the-loop-监督-是一回事"
topicId: "prob-acf7fcb4c0"
angle: "反直觉同构"
rank: 366
score: 7.62
sourceCount: 6
toolsCited:
  - "Saner.AI"
  - "Motion"
  - "Goblin Tools"
  - "Focusmate"
thesis: "ADHD 大脑与 LLM/agent 都是‘强生成、弱执行调度’的核心，解决它们‘不知哪些方法有用’/输出不可靠的关键，不是加装更多工具，而是搭建同一套人在回路的 harness：用外部目标、护栏、检查点和身体在场来补全缺失的执行层。"
problem: "为什么用 Saner.AI 治 ADHD 的不知哪些方法有用，和给 agent 套 human-in-the-loop 监督 是一回事？"
spine: "人在回路与身体在场"
spineKind: ""
isEvolved: true
llmGenerated: false
isoStrength: "B"
caseStudies:
  - "张謇"
  - "陶行知"
  - "姚佳"
---

# 为什么用 Saner.AI 治 ADHD 的不知哪些方法有用，和给 agent 套 human-in-the-loop 监督 是一回事？

> Saner.AI 把自己定位成「ADHD 友好的 AI 个人助理」——笔记、任务、日程、邮件塞进一个 AI 收件箱,主打「你只管倒进来,它帮你理」。装上一个月后,典型用户会陷入一种特有的迷雾:**「好像有点用,但说不清是哪里有用」**——任务确实都在里面了,AI 也确实会提醒和建议,但生活有没有真的变好?是「都在一个地方」起了作用,还是 AI 排序起了作用,还是仅仅换新工具的头两周新鲜感在起作用?这团迷雾不是 Saner.AI 的独有问题,而是**一切「打包式 AI 助理」的评估难题**——而它在 agent 工程里有个成熟的对答案:**没有人类监督的 agent,连它自己也不知道自己哪些动作创造了价值**。

同构的核心在「多组件系统的归因困难」。agent 工程的铁律:**系统不能自己给自己发成绩单**——一个 agent 汇报「本次任务成功」毫无价值,必须有外部验收(人或可靠的评估器)逐项检查:检索有没有帮助?计划对不对?哪一步是多余的?——**因为多组件的贡献混在一个总体验里,不拆开测,优化就是玄学**。Saner.AI 用户的处境一模一样:它同时动了你的四五个环节(捕获/整理/提醒/排序),你的「好像有点用」是一锅混合信号——**你就是这个系统里缺席的那个 human-in-the-loop:没有你来当验收员,工具的价值永远停在「好像」**。

把监督循环装上,三步。**第一步:先定义「有用」**。对 Saner.AI 这类全家桶,总分问题(「它好不好用」)不可答,要拆成组件问题:捕获环节——「想法/任务的丢失率降了吗」(本周有几件事漏掉了?);整理环节——「找东西的时间降了吗」;提醒环节——「该做的事的按时启动率升了吗」——**挑一个你最痛的环节作为主指标,其余当次要**;定义不清的实验,数据再多也不产结论。**第二步:N-of-1 对照**。新鲜感是 ADHD 工具评估的头号污染源(任何新工具的头两周都「有用」);对策是时间上的对照:**用两周、记两周指标;第五周故意停用一周,再记**——停用周指标不变,说明起作用的是新鲜感或别的东西;明显回落,才是工具的真实贡献(这正是评估 agent 组件的 ablation:拆掉一个组件看性能掉不掉)。**第三步:定期验收会**。每两周十五分钟,像 PM 验收 agent 一样验收它:主指标数据怎么样/哪个功能两周没打开过(没用的功能是认知噪音,关掉)/它的 AI 建议采纳率大概多少(建议总被无视=这个组件对你无效)——**验收的输出必须是决策:续用/关掉某模块/退订**——没有决策的记录只是日记。

一个 Saner.AI 类工具的特有陷阱要点名:**「都倒进去」的安心感本身会被误认为疗效**——收集箱满了,大脑确实松了(外部化的真实价值),但**收集不等于完成**:如果任务进去就再没出来过,你只是给拖延租了一个更漂亮的仓库——验收会上必须有一个指标专门盯这个:**进箱任务的完成率**(不是进箱率)。边界:Saner.AI 是生产力工具,不是 ADHD 的治疗;它的「ADHD 友好」是设计取向,不是临床证据;工具评估做得再好,也替代不了正式评估与治疗——先有地基,工具才有处站。

## 边界

同构强度 B 级:human-in-the-loop 验收与 ablation 是 agent 工程实体,ADHD 的工具依从与新鲜感衰减有实践讨论方向,「用户当验收员」的结构对应清晰;评估协议为实践翻译,无对照研究。声明:Saner.AI 未被证实为 ADHD 治疗手段,本文不构成产品疗效背书;显著功能损害请专业评估。

## 今天就能试的 3 件事

1. **定义你的主指标**:从「丢失率/找东西时间/按时启动率」里挑最痛的一个,今天开始记——「好像有用」从此有了坐标。
2. **在日历上预约 ablation 周**:第五周停用一周——新鲜感和真实贡献,让数据分家。
3. **设一个进箱-完成比**:本周进箱的任务,下周日数一数完成了几件——仓库不算疗效,出货才算。

AI 助理不能自己给自己打分,**你就是这个回路里缺的那个人**。定义指标、做一次停用对照、每两周开验收会——「好像有点用」的迷雾,三步就能变成一张能看的成绩单。

## 参考来源

**同构强度：B 级** —— 机制类比（ADHD 侧与 LLM/agent 侧均有真实文献，机制可映射）

- [ADHD Apps: We tested 44 Apps and Here're the Best 9 in 2026](https://blog.saner.ai/best-adhd-apps/) — 证据等级：低（GRADE）
- [12 AI Personal Assistants Built for ADHD Brains (2026 Rankings)](https://www.usecarly.com/blog/best-ai-personal-assistant-adhd/) — 证据等级：低（GRADE）
- [LBD同构对：自我调节与元认知 — Inhibitory control and emotion regulation in preschool child ↔ ObjexMT: Objective Extraction and Metacognitive Calibration ](https://doi.org/10.1016/j.cogdev.2007.08.002) — 证据等级：低（GRADE）
- [LBD同构对：自我调节与元认知 — Emotion-related self-regulation and its relation to children ↔ A Reproducibility Study of Metacognitive Retrieval-Augmented](https://doi.org/10.1146/annurev.clinpsy.121208.131208) — 证据等级：低（GRADE）
- [The 12 Best AI Tools for 2026 (That People Actually Use)](https://www.synthesia.io/post/ai-tools) — 证据等级：低（GRADE）
- [The AI Powered SuperApp for Work | Motion](https://www.usemotion.com/) — 证据等级：低（GRADE）

---

*本文是「ADHD × AI」系列的第 207 篇，由 Devin 基于持续维护的双域研究语料（72,739 篇论文 + LLM Wiki）亲自撰写，并持续迭代更新。*
