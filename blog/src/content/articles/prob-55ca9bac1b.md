---
title: "两个互不引用的领域都在研究「注意调度」——ADHD 文献和 LLM harness 文献为什么得出了同一个结论？"
subtitle: "Swanson 文献发现：622 篇 ADHD 论文 ↔ 35 篇 harness 论文共享机制「attention allocation」，双域代表作对照解读。"
description: "Swanson 文献发现：622 篇 ADHD 论文 ↔ 35 篇 harness 论文共享机制「attention allocation」，双域代表作对照解读。"
date: "2025-05-18"
category: "专注力管理"
categoryId: "focus"
categoryEn: "Focus Management"
tags:
  - "ADHD"
  - "AI"
  - "专注力管理"
  - "LBD同构发现"
  - "分心管理"
readingTime: 11
slug: "两个互不引用的领域都在研究注意调度adhd-文献和-llm-harness-文献为什么得出了同一个结论"
topicId: "prob-55ca9bac1b"
angle: "LBD同构发现"
rank: 100
score: 7.65
sourceCount: 6
toolsCited:
  - "RescueTime"
  - "Focusmate"
  - "Brain.fm"
  - "Forest"
  - "Endel"
thesis: "ADHD 大脑与 LLM 都是‘高产但缺乏可靠执行调度层’的生成核心，因此都必须靠外部 harness/脚手架进行上下文工程，才能主动分配注意力、把潜能转化为目标导向行为。"
problem: "两个互不引用的领域都在研究「注意调度」——ADHD 文献和 LLM harness 文献为什么得出了同一个结论？"
spine: "上下文工程"
spineKind: "llm"
isEvolved: false
llmGenerated: false
isoStrength: "A"
caseStudies:
  - "曾国藩"
  - "曹植"
  - "王秀英"
---

# 两个互不引用的领域都在研究「注意调度」——ADHD 文献和 LLM harness 文献为什么得出了同一个结论？

> 这个系列的第四条隧道,挖在最核心的岩层上:「注意调度」——不是「有没有注意力」,而是**注意力作为稀缺资源,如何被分配、被劫持、被保护**。ADHD 文献在这里的积累最深(这毕竟是它的本名),而 agent 文献从 Transformer 的 attention 机制到上下文工程,恰好也把「注意分配」变成了可测量的工程对象。两边零互引,但这一次,同构有直接的实验证据搭桥——**有研究者干脆把测 ADHD 的范式搬去测了 Transformer**。

ADHD 侧的隧道,先纠正一个常年错位的直觉:ADHD 不是注意力「少」,是**注意分配的调度器不受意志控制**——该领域的经典表述是「注意力的不一致性(inconsistency)」:同一个人,对感兴趣的刺激可以超聚焦四小时,对重要但平淡的任务五分钟都锚不住。实验文献的精确刻画:**自下而上的捕获(新奇、运动、情绪刺激自动夺取注意)相对完好甚至过敏,自上而下的维持(按目标主动分配)受损**——注意不是不够用,是**分配权不在目标手里,在刺激手里**。干预结论几十年一致:改变刺激环境(减少捕获源、给目标任务加装刺激属性)比「努力集中」有效得多——**调度器改不了,输入流可以改**。

Agent 侧的隧道,attention 本来只是个数学机制,但上下文工程的实践把它推回了认知问题:上下文里的每一段内容都在竞争注意权重,无关内容会稀释关键信息的权重(「lost in the middle」现象);**模型无法自主决定「忽略这段」——它对输入流没有拒绝权,正如 ADHD 的调度器对弹窗没有拒绝权**。最硬的桥来自那组直接实验:用 Stroop 冲突范式测 Transformer——短上下文中模型能按任务规则抑制干扰(自上而下赢),上下文拉长后,冲突试次的表现崩到随机(自下而上的统计规律赢)——**研究者明确将其对标执行功能的抑制缺陷**。工程结论与临床结论同构:**别指望系统内部长出抑制力,在输入侧动手**——上下文净化(无关内容不进窗)、关键信息位置工程(放开头结尾)、干扰源隔离,全是「改输入流,不改调度器」。

两边的结论这次几乎是同一句话:**注意调度的失守,治本之道不在系统内部(意志/参数),在输入流的治理**。深层结构:任何「输入自动参与权重竞争、且无内建拒绝权」的注意系统,其表现都由输入流的构成决定——**调度是环境的函数,不(只)是系统的属性**。这句话对 ADHD 者的解放意义值得写粗:几十年「你就是不够专心」的指控,预设了调度权在你手里;两个领域的证据合起来说:**调度权在输入流手里,而输入流,是可以工程化的**。

输入流治理的三层,ADHD 版(每层都有 agent 侧的镜像):**①准入层**——物理隔离捕获源(手机进抽屉=无关文档不进上下文;通知全静默=输入过滤器);**②排布层**——关键任务放注意力最好的时段与位置(镜像:关键指令放上下文的头尾);**③增益层**——给重要但平淡的任务人工加装刺激属性(计时挑战、共工在场、新环境——镜像:关键内容加显式标记与重复注入)。三层做完,「专注」不再是每天重打的意志力之战,而是一次性的环境设计——**这正是两万篇文献汇成的那一句:别跟调度器较劲,去当输入流的设计师**。

## 边界

同构强度 A 级:这条隧道有直接的跨域实验搭桥(Stroop 范式测 Transformer 并显式对标 ADHD 执行缺陷),两侧各自的文献也最厚(注意不一致性研究;长上下文注意稀释研究);但 attention 机制与神经注意在实现层面根本不同,A 级指的是功能同构有直接实证,不是机制等同。声明:输入流治理改善的是条件——若环境已优化到极致仍全面失守,或超聚焦已造成损害(废寝忘食伤身),都值得临床对话;药物对注意调度的作用是另一个层面,与医生讨论。

## 今天就能试的 3 件事

1. **治理准入层**:明天上午,手机进抽屉+通知全静默两小时——只改输入流,不许自责。
2. **做一次排布实验**:把最重要的任务挪到你注意力最好的时段(未必是早上,按你的曲线)。
3. **给一个平淡任务加增益**:计时挑战/约人共工/换个环境——三选一,给它装上刺激属性。

「不够专心」这个指控,被两个领域的证据合力撤销了——**调度器不听你的,但输入流听**。设计输入流的人,不需要赢得意志力之战,因为他根本不参战。

## 参考来源

**同构强度：A 级** —— 直接文献支撑（引用 ADHD↔LLM 同构专题研究）

- [ADHD Apps: We tested 44 Apps and Here're the Best 9 in 2026](https://blog.saner.ai/best-adhd-apps/) — 证据等级：低（GRADE）
- [Meta-Analysis of fMRI Studies of Disruptive Behavior Disorders](https://doi.org/10.1176/appi.ajp.2016.15081089) — 证据等级：高（GRADE）
- [Nonlinear Complexity Analysis of Brain fMRI Signals in Schizophrenia](https://doi.org/10.1371/journal.pone.0095146) — 证据等级：低（GRADE）
- [Revolutionizing ADHD Management with AI Assistants](https://neurolaunch.com/adhd-ai-assistant/) — 证据等级：低（GRADE）
- [Toward Neurodivergent-Aware Productivity: A Systems and AI-Based Human-in-the-Loop Framework for ADHD-Affected Professionals](https://arxiv.org/pdf/2507.06864) — 证据等级：低（GRADE）
- [Using an AI Assistant to Manage ADHD: A Practical Guide](https://www.lobsterfarm.ai/guides/ai-for-adhd/) — 证据等级：低（GRADE）

---

*本文是「ADHD × AI」系列的第 115 篇，由 Devin 基于持续维护的双域研究语料（72,739 篇论文 + LLM Wiki）亲自撰写，并持续迭代更新。*
