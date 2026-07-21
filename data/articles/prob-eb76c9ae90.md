---
title: "给 ADHD 加一道「核对清单/验证步骤」，和给 agent 加 self-critique 循环，是同一种工程吗？"
subtitle: "ADHD 侧：冲动下结论、想当然；LLM/harness 侧：LLM 自信地编造（幻觉），靠验证与自我批判兜底。用双域证据作答。"
description: "ADHD 侧：冲动下结论、想当然；LLM/harness 侧：LLM 自信地编造（幻觉），靠验证与自我批判兜底。用双域证据作答。"
date: "2025-03-25"
category: "科学研究"
categoryId: "science"
categoryEn: "Scientific Research"
tags:
  - "ADHD"
  - "AI"
  - "科学研究"
  - "同构问答"
  - "治疗"
readingTime: 13
slug: "给-adhd-加一道核对清单验证步骤和给-agent-加-self-critique-循环是同一种工程吗"
topicId: "prob-eb76c9ae90"
angle: "同构问答"
rank: 176
score: 7.54
sourceCount: 5
toolsCited:
  - "Goblin Tools"
  - "Saner.AI"
  - "Motion"
  - "Tiimo"
problem: "给 ADHD 加一道「核对清单/验证步骤」，和给 agent 加 self-critique 循环，是同一种工程吗？"
spine: "幻觉与验证循环"
spineKind: "llm"
isEvolved: false
llmGenerated: false
---

# 给 ADHD 加一道「核对清单/验证步骤」，和给 agent 加 self-critique 循环，是同一种工程吗？

> 她给自己定过无数次「出门前检查钥匙钱包手机」的规矩,全部阵亡——不是不想执行,是出门那一刻大脑根本不会想起还有个规矩存在。直到她在门把手上挂了一块写着三个词的木牌,把检查从「要记得做的事」变成「挡在路上的东西」,阵亡率才归零。多年后她做 AI 产品,看到工程师为 agent 设计 self-critique 循环时争论的问题居然一模一样:验证器放在流程外靠模型「自觉」调用,还是硬编码在管线里想跳都跳不过?

收敛:本文只回答一个工程对齐问题——**人的核对清单和 agent 的 self-critique,在什么层面是同一种工程、什么层面必须分道?搞清这个,能少走多少弯路?**

## 穿透:同一个架构公理,两处不同的工程约束

先讲「同」的部分,它深刻:两者共享同一条架构公理——**生成者不可靠时,不要改进生成者,要外加验证层。**LLM 会自信地产出错误,工程答案不是「训练一个永不出错的模型」(做不到),而是加 self-critique/验证器,让输出在离开系统前过一道关。ADHD 的执行输出同样高变异(遗漏、冲动决策、细节丢失),传统答案「下次仔细点」等价于「训练永不出错的模型」——同样做不到;清单与核对步骤就是人的验证层。航空业早用几十年:检查单的前提假设从来不是飞行员无能,而是**任何生成者在负载下都会漏**。这一层,完全是同一种工程。

再讲「异」的部分,不搞清楚会白干。异之一:**触发机制**。agent 的验证器由代码调用,百分之百执行;人的验证器要靠前瞻记忆去「想起来」——恰恰是 ADHD 最弱的功能。所以人版清单的成败几乎全在触发器设计:必须把触发绑定到**物理路径**(门把手上的牌、屏幕上的便签、打不开文档的强制弹窗),而不是「记得检查」。她的木牌成功,不是清单变好了,是触发从记忆搬进了环境。

异之二:**验证疲劳**。agent 跑一万次 critique 不抱怨,人对重复核对会快速脱敏——第二周的清单已经「看而不见」。对策也是工程的:清单要短(三项封顶)、要轮换形式(换位置/换颜色)、高频项要尽量转自动化(能自动的不留给人)。

异之三:**情绪成本**。self-critique 对 agent 是零成本操作,对 ADHD,「核对」可能激活「我又要出错了」的羞耻回路,让人本能回避整个流程。人版验证层必须做情绪脱敏设计:清单语言用中性动作词(「拿钥匙」而非「别又忘了钥匙」),把核对定义为「专业行为」而非「缺陷补丁」——外科医生和机长都用检查单,没人觉得那是无能。

## 验证

一条清单两周可验证:选你最高频的失误场景(出门/发邮件/交文档),做一个三项清单,配一个物理触发器,记录两周失误率对比基线。可证伪:若失误率不降,先查触发器(它真的挡在路上吗?),再查清单长度(超过三项砍),最后才怀疑方法本身。反例边界:核对若演变成反复检查十几遍无法停止,那可能滑向强迫方向的问题,机制与解法完全不同,请寻求专业评估。

## 决策

做什么:按「同」借架构(给高失误输出加验证层),按「异」改工程(物理触发器+三项封顶+中性语言+能自动则自动)。

不做什么:不要写超过三项的清单(那是给未来的自己埋雷);不要把清单放在需要「记得去看」的地方——放在路上,不是放在心上。

先做什么:选定你的最高频失误场景,今天做出那块「木牌」——一张便签,三项,贴在物理路径的必经处。

## 边界

「清单↔self-critique」在架构层为强同构,在触发/疲劳/情绪三个实现层需独立工程(本文未做正式 A/B/C 分级);检查单在航空与医疗的有效性证据充分,对 ADHD 个体的迁移属实践翻译。若核对行为本身失控或伴随强烈焦虑,请寻求专业评估。

## 今天就能试的 3 件事

1. 做你的三项木牌:最高频失误场景+三个中性动作词+物理必经处,十分钟完成。
2. 审查一条你阵亡过的旧清单:死因是触发器(靠记忆)还是长度(超三项)?写一行验尸报告。
3. 找一项能全自动的核对(自动扣款、日历提醒、拼写检查),今天设好——最好的验证层,是不需要你在场的那种。

本文服务于人生 Harness 金字塔的**执行层**:machine 的验证层写在代码里,你的验证层要钉在门框上——公理相同,工程各异,而懂得这个「异」,才是真的懂了那个「同」。

## 参考来源

- [Unveiling critical ADHD biomarkers in limbic system and cerebellum...](https://www.aimspress.com/article/doi/10.3934/mbe.2024256?viewType=HTML) — 证据等级：低（GRADE）
- [Machine Learning Approaches to Identify and Classify ADHD: A ...](https://www.sciepublish.com/article/pii/1040) — 证据等级：低（GRADE）
- [ADHD Assessment Form Template with Examples - Heidi Health](https://www.heidihealth.com/en-us/blog/adhd-assessment-form-template) — 证据等级：低（GRADE）
- [Subcortical brain volume differences in participants with attention deficit hyperactivity disorder in children and adults: a cross-sectional mega-analysis](https://doi.org/10.1016/s2215-0366(17)30049-4) — 证据等级：低（GRADE）
- [Validity of DSM-IV attention deficit/hyperactivity disorder symptom dimensions and subtypes.](https://doi.org/10.1037/a0027347) — 证据等级：低（GRADE）

---

*本文是「ADHD × AI」系列的第 46 篇，由 Devin 基于持续维护的双域研究语料（72,739 篇论文 + LLM Wiki）亲自撰写，并持续迭代更新。*
