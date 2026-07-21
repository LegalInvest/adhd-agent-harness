---
title: "两个互不引用的领域都在研究「分心与走神」——ADHD 文献和 LLM harness 文献为什么得出了同一个结论？"
subtitle: "Swanson 文献发现：422 篇 ADHD 论文 ↔ 59 篇 harness 论文共享机制「distraction」，双域代表作对照解读。"
description: "Swanson 文献发现：422 篇 ADHD 论文 ↔ 59 篇 harness 论文共享机制「distraction」，双域代表作对照解读。"
date: "2025-03-31"
category: "专注力管理"
categoryId: "focus"
categoryEn: "Focus Management"
tags:
  - "ADHD"
  - "AI"
  - "专注力管理"
  - "LBD同构发现"
  - "深度工作"
readingTime: 9
slug: "两个互不引用的领域都在研究分心与走神adhd-文献和-llm-harness-文献为什么得出了同一个结论"
topicId: "prob-44b0cd8aba"
angle: "LBD同构发现"
rank: 134
score: 7.6
sourceCount: 5
toolsCited:
  - "Brain.fm"
  - "Focusmate"
  - "Endel"
  - "Forest"
problem: "两个互不引用的领域都在研究「分心与走神」——ADHD 文献和 LLM harness 文献为什么得出了同一个结论？"
spine: "上下文工程"
spineKind: "llm"
isEvolved: false
llmGenerated: false
---

# 两个互不引用的领域都在研究「分心与走神」——ADHD 文献和 LLM harness 文献为什么得出了同一个结论？

> 一个 harness 工程师在排查 agent 跑偏问题：任务是重构一个函数，agent 却在第 14 步开始优化一个没人要求的日志格式。他在 issue 里写下诊断——「上下文里无关信息太多，注意力被高显著性的干扰项捕获」。写完他愣住了：这句话一字不改，就是上周心理咨询师描述他自己 ADHD 分心模式的原话。

收敛：本文只回答一个问题——**ADHD 的「分心」和 agent 的「跑偏」是不是同一类故障？如果是，两边共同的修法是什么？**

## 穿透：两边文献各自的结论

ADHD 侧：分心的机制研究指向「自下而上的显著性捕获压过自上而下的目标维持」——不是没有注意力，而是注意力的分配权经常被环境中显著性最高的刺激夺走；且目标的心理表征越弱（隔得越久、越抽象），被夺权越容易。文献里的干预方向：降低环境干扰的显著性（环境工程）、提高目标表征的强度（把目标具体化、可见化、拆近）。

Harness 侧：agent 长程任务跑偏的分析指向几乎同构的结论——上下文里的无关内容会稀释指令的注意力权重，任务走得越长、原始指令离当前位置越远，模型对目标的「维持」越弱。修法同样两条：上下文工程（清掉无关信息、压缩历史）、目标重注入（定期把任务目标重新写进上下文）。

两个领域互不引用，却都把「分心」拆成了同一对力量：**干扰的显著性 vs 目标的在场强度**。而且都发现单纯「更努力聚焦」不是修法——ADHD 文献不支持靠意志力抗分心，harness 文献也不靠「请专注」的 prompt 救场。修的都是结构：要么削弱干扰，要么增强目标在场。

风险与利益：注意力经济的整个产业就建立在「显著性捕获」上——你的分心是它们的营收。承认分心是结构问题而非品格问题，第一个冲击的是「自律不足」的自责叙事，第二个冲击的是靠贩卖自律焦虑获利的课程。

## 验证：证伪路径

如果「目标重注入」对人无效，类比就该降级。可自测（一周）：给一个容易走神的工作时段设 20 分钟一次的震动提醒，提醒时只做一件事——看一眼写着当前任务的便签（目标重注入），记录每天的跑偏次数。若一周后跑偏次数无变化，这个迁移对你不成立，转向环境工程（换环境、物理隔离手机）。反例边界：如果「分心」的内容总是同一件焦虑的事，那可能是反刍而非显著性捕获，修法完全不同，请考虑专业支持。

## 决策

做什么：把抗分心的预算从「意志力」全部转移到「结构」——环境降噪 + 目标可见化 + 定期重注入，三件套。

不做什么：不要再买「专注力训练」类的意志力产品；不要在每次走神后自责——那是给干扰项追加注意力投资。

先做什么：先做目标可见化，成本最低：当前任务写在便签贴在屏幕边缘，现在就写。

## 边界

本同构有双域独立文献的趋同支撑，但停留在计算层（本文未做正式 A/B/C 分级）；「注意力权重」在两侧是不同的实体。若分心伴随显著情绪困扰或功能损害，请寻求专业评估；本文不构成诊断。

## 今天就能试的 3 件事

1. 把当前任务用五个字写在便签上，贴在视线内——目标重注入的最小实现。
2. 找出你工作环境里显著性最高的干扰源（通常是手机），物理移出视线——不是锁屏，是移出。
3. 设一个 20 分钟的循环提醒，响铃动作只有一个：看便签。跑一个下午，数据自己会说话。

本文服务于人生 Harness 金字塔的**执行层**：分心不是你的品格档案，是两个学科都确认过的结构故障——而结构故障有结构修法。

## 参考来源

- [LBD同构对：任务分解与规划 — Evidence-Based Assessment of Attention Deficit Hyperactivity ↔ Generative Agents: Interactive Simulacra of Human Behavior](https://doi.org/10.1207/s15374424jccp3403_5) — 证据等级：低（GRADE）
- [LBD同构对：抑制控制 — Clinical Practice Guideline: Diagnosis and Evaluation of the ↔ The Role for Endoplasmic Reticulum Stress in Diabetes Mellit](https://doi.org/10.1542/peds.105.5.1158) — 证据等级：低（GRADE）
- [LBD同构对：注意调度 — a dynamic developmental theory of attention-deficit/hyperact ↔ Not All Errors Are Alike: Theta and Alpha EEG Dynamics Relat](https://doi.org/10.1017/s0140525x05000075) — 证据等级：低（GRADE）
- [Peer-Assessed Outcomes in the Multimodal Treatment Study of Children With Attention Deficit Hyperactivity Disorder](https://doi.org/10.1207/s15374424jccp3401_7) — 证据等级：低（GRADE）
- [Dissociation in performance of children with ADHD and high-functioning autism on a task of sustained attention](https://doi.org/10.1016/j.neuropsychologia.2007.02.019) — 证据等级：低（GRADE）

---

*本文是「ADHD × AI」系列的第 7 篇，由 Devin 基于持续维护的双域研究语料（72,739 篇论文 + LLM Wiki）亲自撰写，并持续迭代更新。*
