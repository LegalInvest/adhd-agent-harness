---
title: "为什么「治好 ADHD 的独自做事缺乏问责、容易放弃」和「让 LLM 不跑飞」其实是同一道工程题？"
subtitle: "高风险 agent 需要 human-in-the-loop 监督——同一套 harness 思路，两边都成立。"
description: "高风险 agent 需要 human-in-the-loop 监督——同一套 harness 思路，两边都成立。"
date: "2025-03-28"
category: "社群与文化"
categoryId: "community"
categoryEn: "Community & Culture"
tags:
  - "ADHD"
  - "AI"
  - "社群与文化"
  - "反直觉同构"
  - "社群"
readingTime: 8
slug: "为什么治好-adhd-的独自做事缺乏问责容易放弃和让-llm-不跑飞其实是同一道工程题"
topicId: "prob-51e4faf16d"
angle: "反直觉同构"
rank: 328
score: 7.63
sourceCount: 6
toolsCited:
  - "Goblin Tools"
  - "Motion"
  - "Saner.AI"
thesis: "ADHD 大脑与 LLM agent 本质上是同一类「高产但缺执行调度层的生成核心」，它们需要的不是被「修好」，而是一个外挂的 harness（上下文管理、验证循环、记忆与调度）来补全执行层，把「人在回路」和「身体在场」变成可工程化的约束。"
problem: "为什么「治好 ADHD 的独自做事缺乏问责、容易放弃」和「让 LLM 不跑飞」其实是同一道工程题？"
spine: "人在回路与身体在场"
spineKind: "llm"
isEvolved: false
llmGenerated: false
isoStrength: "B"
caseStudies:
  - "张一鸣"
  - "王传福"
  - "Donna Wilson"
---

# 为什么「治好 ADHD 的独自做事缺乏问责、容易放弃」和「让 LLM 不跑飞」其实是同一道工程题？

> 同一个 ADHD 者,在两种条件下判若两人:有同事等着、有客户催着、有搭档看着的事,能做完;只对自己负责的事——自己的项目、自己的学习、自己的健康——烂尾率接近百分之百。常见的自我诊断是「我只是需要压力」,但更精确的表述是:**「只对自己负责」在执行系统里等于「没有外部校验点」——而没有外部校验点的长任务,对 ADHD 和对 LLM agent,是同一种高危配置**。LLM 工程给这个配置起过名字,也给出过答案:**human-in-the-loop(人在回路)——完全自主的 agent 在长任务上会静默地跑飞,解药是在关键节点插入外部检查**。

先讲 agent 侧「跑飞」的解剖。让一个 agent 完全自主地跑长任务,失败模式高度可预测:**目标漂移**(做着做着偏离原始意图,越偏越远且毫无自觉)、**质量滑坡**(错误不被指出就成为后续步骤的地基)、**静默放弃**(卡住后在原地打转,却不上报)——三种失败共享一个根源:**系统内部没有「他者视角」来校验状态**,自己检查自己,检查器和被检查的是同一个有偏系统。工程解法不是造一个更强的自检模块(还是同一个系统),是**在回路里插入外部检查点**:关键步骤需要人审批、定期产出进度报告给人看、异常时升级给人裁决——**外部性本身就是校验的效力来源**。

ADHD 侧的机制,精确对应:**其一,自我监控是执行功能的一部分**——也就是说,它恰恰是受损的那套系统的组件:用受损的监控器监控自己,漂移与滑坡同样不被察觉;**其二,自我承诺的奖赏结构太弱**——对自己食言没有立刻的社会后果,而 ADHD 的动机系统对「无即时后果」的约束几乎免疫(延迟折扣);对他人食言则有即时的社会痛感——**「有人在等」是少数能穿透延迟折扣的信号之一**;**其三,放弃的静默性**——独自做的事,放弃不需要向任何人宣告,于是它以「再也没碰」的方式无声发生(和坑的渐近线死法同构)。三条合起来:**独自 = 无外部校验 + 无社会后果 + 放弃零成本**——这个配置下烂尾,是系统行为,不是品格。

解法就是给自己的事装人在回路,强度可调,丰俭由人:**①轻量:进度广播**——把项目进度定期发给一个人(朋友/社群/甚至公开发帖):不需要对方做什么,「有人可能在看」已经改变了放弃的成本结构(静默放弃变成了可见食言);**②中量:定期检查点**——找一个同路人,每周固定 15 分钟互相汇报(说了要做什么/做到没/下周做什么)——**这是 scrum 站会的原理,也是 Focusmate 篇口头序列化的复利版**:汇报即校验,说不清就是跑飞的信号;**③重量:利益绑定**——付费的教练/课程/协作承诺,让放弃有真金白银的成本(承诺机制的行为经济学);④**关键设计:回路的颗粒度**——检查点太密是微观管理(窒息),太疏则两次检查之间足够跑飞十次;经验法则:**按「你历史上平均多久烂尾」定周期**——两周烂尾的人,检查点至少一周一次。

边界:**其一,问责不等于羞辱**——检查点的功能是校验与再锚定,不是审判;找的人要能说「卡住了?那调整计划」而不是「你怎么又没做」(后者激活羞耻→回避,焚烧炉篇的债务机制,反而加速放弃);**其二,外部问责是结构,不是治疗**——它补的是自我监控的缺口,不改变底层的执行功能;**其三,人在回路的工程有效性是实践共识,body doubling/问责伙伴的 ADHD 直接证据仍有限**(教练干预的研究方向存在但规模小)——同构的两侧,工程侧更硬,临床侧在积累。

## 边界

同构强度 B 级:自我监控作为执行功能组件受损有研究基础,human-in-the-loop 是 agent 工程的实体实践,「外部校验点」的结构对应清晰;问责伙伴与教练干预的 ADHD 证据有限。声明:关系中的问责注意羞耻边界;广泛的功能困难,评估优先。

## 今天就能试的 3 件事

1. **给一个烂尾中的项目装广播**:今天把它的现状发给一个人,并说「我下周五给你发进展」——回路今天接通。
2. **算你的烂尾周期**:历史上独自项目平均活多久?——检查点的频率,定在它的一半。
3. **写好检查点脚本**:三个问题——上次说做什么/做到没/下次做什么——15 分钟,说不清的地方就是跑飞的位置。

完全自主的 agent 会静默跑飞,**完全独自的 ADHD 项目会无声烂尾——两者缺的是同一个组件:回路里的他者**。给最重要的独自事务,插一个人进去;校验的效力,恰恰来自那个人不是你。

## 参考来源

**同构强度：B 级** —— 机制类比（ADHD 侧与 LLM/agent 侧均有真实文献，机制可映射）

- [ADHD Apps: We tested 44 Apps and Here're the Best 9 in 2026](https://blog.saner.ai/best-adhd-apps/) — 证据等级：低（GRADE）
- [12 AI Personal Assistants Built for ADHD Brains (2026 Rankings)](https://www.usecarly.com/blog/best-ai-personal-assistant-adhd/) — 证据等级：低（GRADE）
- [LBD同构对：自我调节与元认知 — Inhibitory control and emotion regulation in preschool child ↔ ObjexMT: Objective Extraction and Metacognitive Calibration ](https://doi.org/10.1016/j.cogdev.2007.08.002) — 证据等级：低（GRADE）
- [LBD同构对：自我调节与元认知 — Emotion-related self-regulation and its relation to children ↔ A Reproducibility Study of Metacognitive Retrieval-Augmented](https://doi.org/10.1146/annurev.clinpsy.121208.131208) — 证据等级：低（GRADE）
- [The 12 Best AI Tools for 2026 (That People Actually Use)](https://www.synthesia.io/post/ai-tools) — 证据等级：低（GRADE）
- [The AI Powered SuperApp for Work | Motion](https://www.usemotion.com/) — 证据等级：低（GRADE）

---

*本文是「ADHD × AI」系列的第 178 篇，由 Devin 基于持续维护的双域研究语料（72,739 篇论文 + LLM Wiki）亲自撰写，并持续迭代更新。*
