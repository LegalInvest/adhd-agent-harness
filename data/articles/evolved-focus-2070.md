---
title: "为什么用 Goblin Tools 治 ADHD 的注意力涣散，和给 agent 套 上下文工程 是一回事？"
subtitle: "Goblin Tools 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
description: "Goblin Tools 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
date: "2025-04-06"
category: "专注力管理"
categoryId: "focus"
categoryEn: "Focus Management"
tags:
  - "ADHD"
  - "AI"
  - "专注力管理"
  - "反直觉同构"
  - "注意力"
readingTime: 11
slug: "为什么用-goblin-tools-治-adhd-的注意力涣散和给-agent-套-上下文工程-是一回事"
topicId: "evolved-focus-2070"
angle: "反直觉同构"
rank: 159
score: 7.71
sourceCount: 6
toolsCited:
  - "Goblin Tools"
  - "Brain.fm"
  - "Focusmate"
  - "RescueTime"
  - "Motion"
  - "Reclaim.ai"
thesis: "ADHD大脑与LLM在结构上同构——都是高产但缺执行调度层的生成核心，因此两者都需要外部上下文工程（harness）来弥补调度缺陷，Goblin Tools等工具正是这一同构的实证。"
problem: "为什么用 Goblin Tools 治 ADHD 的注意力涣散，和给 agent 套 上下文工程 是一回事？"
spine: "上下文工程"
spineKind: ""
isEvolved: true
llmGenerated: false
caseStudies:
  - "曾国藩"
  - "李鸿章"
  - "陈霞"
---

# 为什么用 Goblin Tools 治 ADHD 的注意力涣散，和给 agent 套 上下文工程 是一回事？

> 注意力涣散最气人的地方,不是「没有注意力」,而是注意力明明在,却糊成一片:桌上摊着三件事,脑子里悬着七件事,每件都在拉扯,结果哪件都没真正开始。上下文工程师看到这幅图会立刻给出诊断:这不是算力问题,是上下文污染——窗口里塞了太多互相竞争的内容,每一条都在稀释对当前任务的注意力分配。而 Goblin Tools 恰好是一把窗口清洁工具,只是很多人没按这个用法用。

先看 LLM 侧的机制,因为它出奇地准确。上下文工程这几年成为显学,核心发现就一条:**模型的表现不取决于上下文里「有多少信息」,取决于「信息的信噪比」**——无关内容、互相冲突的指令、堆积的历史消息,都会实际劣化输出:模型开始东拉西扯、忘记主任务、在几个话题间摇摆。工程师的对策不是换更强的模型,是**上下文净化**:删除无关内容、每次只呈现当前步骤、把暂时不用的信息移出窗口存到外部。

ADHD 的注意力涣散,机件层面高度平行:**你的「工作记忆窗口」本来就小,而未完成任务的残留(心理学里那些未闭合的事项会持续占用认知资源)、环境刺激、情绪噪音,把窗口塞满了竞争内容**——注意力不是消失了,是被摊薄到没有一个对象能拿到启动阈值以上的份额。「我今天特别散」翻译成工程语言就是:「我的上下文今天信噪比极低。」

Goblin Tools 的正确用法,就是按上下文工程的三个动作来用:

**一、Brain Dump 当「窗口清空」用。** 感到糊成一片的那一刻,先别试图开始任何任务——打开 Goblin Tools 把脑子里悬着的所有东西倒进去(它的界面对「破碎输入」很友好,不要求你组织好)。**倒空这个动作的意义是物理性的:悬着的事项一旦有了外部存储,大脑对它们的后台占用会显著松开**——这是认知卸载研究里反复验证的效应。窗口清空,才谈得上装载。

**二、Magic ToDo 拆解后,只保留「当前一步」在视野里。** 拆出的子任务列表,别整个摊开盯着(那等于把七件事又搬回了窗口)——**遮住后面的,只看第一条**。上下文工程的铁律:executor 的窗口里只放当前步骤,全局计划放外部。一张便签盖住屏幕下半段,土办法,管用。

**三、用「辣度」控制装载粒度。** 状态越散的日子,拆得越细(辣度调高)——因为窗口越糊,能稳定持有的任务块越小。**「今天状态差」不该翻译成「今天完了」,该翻译成「今天用更小的粒度运行」**——这是把状态波动从道德问题降格为参数问题,而参数是可以调的。

用错的姿势:**把工具本身变成新的窗口污染**——拆解了十个任务,列表越攒越长,打开工具先看到一堆积压,涣散加倍(对策:每天只对当天的事用它,历史列表定期清空);**倒完脑子不回来**(Brain Dump 变成又一次逃逸入口——倒空之后的下一个动作必须是「看第一条,做」);**指望它治「情绪性涣散」**(焦虑或情绪淹没造成的糊,不是任务糊,清洁窗口清不掉它,需要先安顿情绪)。

## 边界

同构强度 B 级:上下文内容对 LLM 输出质量的影响有实证研究,ADHD 的工作记忆负荷与认知卸载效应有文献支撑,Goblin Tools 本身无对照研究,「窗口清洁」是功能映射。声明:持续的、跨场景的注意力涣散值得正式评估——工具管理的是负荷,不是神经层面的注意调节;若涣散伴随明显的情绪低落或焦虑,先处理那一层。

## 今天就能试的 3 件事

1. **下次「糊成一片」时,先倒后做**:Brain Dump 三分钟,然后只看第一条。
2. **物理遮挡**:便签盖住任务列表的「后面所有条目」,窗口里只留一条。
3. **建「状态-粒度」对照**:状态好=正常拆,状态散=辣度拉满拆到 5 分钟块。

注意力涣散的日子,你缺的常常不是注意力,是一次窗口大扫除。**上下文工程师从不骂模型「不专心」,他们清理上下文**——对自己,同样的手法,同样的温柔。

## 参考来源

- [ADHD Apps: We tested 44 Apps and Here're the Best 9 in 2026](https://blog.saner.ai/best-adhd-apps/) — 证据等级：低（GRADE）
- [Meta-Analysis of fMRI Studies of Disruptive Behavior Disorders](https://doi.org/10.1176/appi.ajp.2016.15081089) — 证据等级：高（GRADE）
- [Nonlinear Complexity Analysis of Brain fMRI Signals in Schizophrenia](https://doi.org/10.1371/journal.pone.0095146) — 证据等级：低（GRADE）
- [Revolutionizing ADHD Management with AI Assistants](https://neurolaunch.com/adhd-ai-assistant/) — 证据等级：低（GRADE）
- [LBD同构对：任务分解与规划 — Attention-deficit/hyperactivity disorder is characterized by ↔ Language-conditioned world model improves policy generalizat](https://doi.org/10.1073/pnas.0707741104) — 证据等级：低（GRADE）
- [LBD同构对：任务分解与规划 — Safety and recommendations for TMS use in healthy subjects a ↔ AgentGen: Enhancing Planning Abilities for Large Language Mo](https://doi.org/10.1016/j.clinph.2020.10.003) — 证据等级：低（GRADE）

---

*本文是「ADHD × AI」系列的第 320 篇，由 Devin 基于持续维护的双域研究语料（72,739 篇论文 + LLM Wiki）亲自撰写，并持续迭代更新。*
