---
title: "ADHD 程序员视角：为什么「治好 ADHD 的任务启动困难、不会拆解」和「让 LLM 不跑飞」其实是同一道工程题？"
subtitle: "agent 用 planner-executor 循环分解长任务——同一套 harness 思路，两边都成立。"
description: "agent 用 planner-executor 循环分解长任务——同一套 harness 思路，两边都成立。"
date: "2025-04-25"
category: "时间管理"
categoryId: "time-mgmt"
categoryEn: "Time Management"
tags:
  - "ADHD"
  - "AI"
  - "时间管理"
  - "人群×同构"
  - "日程安排"
readingTime: 14
slug: "adhd-程序员视角为什么治好-adhd-的任务启动困难不会拆解和让-llm-不跑飞其实是同一道工程题"
topicId: "prob-2d3efb2713"
angle: "人群×同构"
rank: 118
score: 7.77
sourceCount: 6
toolsCited:
  - "Motion"
  - "Reclaim.ai"
  - "Tiimo"
  - "Todoist"
  - "Saner.AI"
  - "Obsidian"
thesis: "ADHD 大脑与 LLM 都是高产生成核心，但缺少可靠的执行调度层；两边的解法不是「修好」这个核心，而是外挂一个可配置、可回查的 harness，让 planner-executor 循环替它们完成启动、拆解与上下文重锚。"
problem: "ADHD 程序员视角：为什么「治好 ADHD 的任务启动困难、不会拆解」和「让 LLM 不跑飞」其实是同一道工程题？"
spine: "规划循环与任务分解"
spineKind: "llm"
isEvolved: false
llmGenerated: false
isoStrength: "B"
caseStudies:
  - "孔子"
  - "苏轼"
  - "梅丽丽"
---

# ADHD 程序员视角：为什么「治好 ADHD 的任务启动困难、不会拆解」和「让 LLM 不跑飞」其实是同一道工程题？

> 你早就知道不能把「实现用户系统」直接丢给 agent——你会先拆:schema、接口、鉴权、测试,每个再拆到函数级。但轮到自己面对「重构这个模块」时,你盯着 IDE 半小时,然后打开了 HN。给 agent 的那份体贴,是时候分给自己了。

程序员任务的启动困难有行业特色的形状。**大 ticket 的雾**:「优化性能」「重构支付模块」「调研新框架」——这些和丢给 agent 的模糊 prompt 是同一种东西:没有第一行代码从哪写起的信息;**旧代码的启动税**:接手祖传代码,启动前要先重建全部上下文(这块逻辑为什么这样?),对工作记忆小的 ADHD 是双重收费;**「顺手修」的散射**:终于启动了,写着 A 看到 B 该改,滑向 B 又看到 C——启动了但从未落地;**质量门槛的自我加码**:「这次要写得优雅」——完美主义把启动价又抬三成。最讽刺的画面:**一个天天给 agent 做 task decomposition 的人,自己的 TODO 里躺着一条三周没动的「重构 auth」。**

把你写进 agent 框架的组件,给自己也实例化一份:

## 给自己写 ticket:planner 的自我服务

军规:**任何超过两小时的活,先拆成子任务再动手**——拆到「每个子任务能想象出第一行代码」的粒度。拆不动的(通常因为上下文不明),第一个子任务就是「花 30 分钟读代码并写下理解」——**把「弄明白」本身立为任务,是对付祖传代码启动税的标准做法**:它把模糊的畏难变成有完成态的动作。懒得拆?丢给 AI:「把这个重构拆成可独立提交的小步,每步可单独测试」——顺便你会发现,能拆成小步的方案通常也是风险更低的方案(小步提交的红利,和 agent 的短反馈循环是同一个原理)。

## 启动的物理学:让第一步小于激活能

**「开个失败的头」协议**:新任务的第一个动作永远是最小可跑的烂版本——写一个必然报错的函数签名、一个空测试、一行伪代码注释。**代码世界的烂初稿:先让它存在,再让它正确**——启动阻力的大头是「从零到有」,不是「从有到好」。**收工时给明天留「热引擎」**:每天结束前,故意留一个 5 分钟能完成的小尾巴(一个写了一半的测试、一行 TODO 注释写清下一步)——明早从「续写」启动,绕过冷启动的全额税。这是海明威的老技巧,对 ADHD 程序员是刚需。

## 「顺手修」的围栏

散射问题前文有队列协议,程序员版加一条硬件:**一个分支只做一件事**——看到 B 该改?`git stash` 心态:开条 issue 记下,回主线。**分支纪律是防散射的物理围栏**:当「顺手改」意味着要切分支、开 issue,冲动的成本立刻高于收益,散射自然衰减。评审友好是副产品:单一目的的 PR,review 速度快一倍——你的问责回路(有人在等这个 PR)也因此更快闭合。

## 借 CI/CD 的节拍器

ADHD 程序员的隐藏福利:**这个行业的基建自带外部结构**——每日站会是启动信号,sprint 是近端死线,PR review 是问责,CI 绿灯是即时反馈。主动借力:把自己的任务切到「一天内能见 CI 绿灯」的粒度(反馈周期>1 天,动机就开始漏电);站会上主动说今天的第一块(公开承诺是最便宜的启动电源)。**远程工作者失去这些节拍时要自建**:和同事约结对时段、自设「上午必发一个 draft PR」的规则。

## 边界

同构强度 A 级:task decomposition 对 agent 的增益有直接研究,ADHD 启动与规划缺陷证据扎实,软件工程的小步实践(小提交/短反馈)与之同构整齐,无对照研究检验本文组合。提醒:若启动瘫痪集中在特定类型任务(如一切涉及沟通的活:写文档、回评审意见),那可能叠加了社交焦虑维度,值得单独正视;长期「产出焦虑+夜间赶工」是 burnout 路径,持续耗竭请专业评估。

## 今天就能试的 3 件事

1. **把 TODO 里躺最久的那条拆了**:拆到「能想象第一行代码」,第一个子任务今天做掉。
2. **今天收工前留个热引擎**:一个 5 分钟的小尾巴+一行「下一步」注释。
3. **立分支纪律**:下次「顺手想改」,开 issue 不动手。给散射装上围栏。

你给 agent 拆任务时从不觉得它「应该自己想明白」——你知道那是架构的责任。对自己也用同一套工程伦理:拆小、开烂头、留热引擎、借节拍。那条躺了三周的「重构 auth」,今天就能变成五个小时内可以各自见绿灯的 ticket。

## 参考来源

**同构强度：B 级** —— 机制类比（ADHD 侧与 LLM/agent 侧均有真实文献，机制可映射）

- [LBD同构对：自我调节与元认知 — Inhibitory control and emotion regulation in preschool child ↔ ObjexMT: Objective Extraction and Metacognitive Calibration ](https://doi.org/10.1016/j.cogdev.2007.08.002) — 证据等级：低（GRADE）
- [LBD同构对：自我调节与元认知 — Emotion-related self-regulation and its relation to children ↔ A Reproducibility Study of Metacognitive Retrieval-Augmented](https://doi.org/10.1146/annurev.clinpsy.121208.131208) — 证据等级：低（GRADE）
- [The 12 Best AI Tools for 2026 (That People Actually Use)](https://www.synthesia.io/post/ai-tools) — 证据等级：低（GRADE）
- [The AI Powered SuperApp for Work | Motion](https://www.usemotion.com/) — 证据等级：低（GRADE）
- [11 Best ADHD Productivity Apps for Fluctuating Energy - rivva blog](https://blog.rivva.app/p/11-best-adhd-productivity-apps-for) — 证据等级：低（GRADE）
- [ADHD Apps: We tested 44 Apps and Here're the Best 9 in 2026](https://blog.saner.ai/best-adhd-apps/) — 证据等级：低（GRADE）

---

*本文是「ADHD × AI」系列的第 39 篇，由 Devin 基于持续维护的双域研究语料（72,739 篇论文 + LLM Wiki）亲自撰写，并持续迭代更新。*
