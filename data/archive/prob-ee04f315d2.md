---
title: "为什么用 Perplexity 治 ADHD 的不知哪些方法有用，和给 agent 套 human-in-the-loop 监督 是一回事？"
subtitle: "Perplexity 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
description: "Perplexity 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
date: "2025-03-22"
category: "亲子教育"
categoryId: "parenting"
categoryEn: "Parenting & Education"
tags:
  - "ADHD"
  - "AI"
  - "亲子教育"
  - "反直觉同构"
  - "ADHD儿童"
readingTime: 12
slug: "为什么用-perplexity-治-adhd-的不知哪些方法有用和给-agent-套-human-in-the-loop-监督-是一回事"
topicId: "prob-ee04f315d2"
angle: "反直觉同构"
llmGenerated: false
rank: 238
score: 7.68
sourceCount: 4
toolsCited:
  - "Goblin Tools"
  - "Saner.AI"
  - "Motion"
  - "Tiimo"
problem: "为什么用 Perplexity 治 ADHD 的不知哪些方法有用，和给 agent 套 human-in-the-loop 监督 是一回事？"
spine: "人在回路与身体在场"
spineKind: ""
isEvolved: true
---

# 为什么用 Perplexity 治 ADHD 的不知哪些方法有用，和给 agent 套 human-in-the-loop 监督 是一回事？

> 这个小系列的前两篇讲了方法实验(Goblin)和日程决策(Motion)的监督位,这一篇讲最上游的环节:**信息获取**。「不知哪些方法有用」的第一现场,往往是深夜的搜索框:「ADHD 怎么治拖延」——然后掉进一个内容沼泽:小红书的玄学、油管的贩卖焦虑、论坛里互相矛盾的个人经验、以及包装成科普的补剂广告。ADHD 在这个沼泽里有双重劣势:**冲动性让「看起来有道理」直接跳过查证变成「今晚就试」,而执行功能的短缺让「系统地交叉验证多个来源」这件事根本不会发生**。Perplexity 这类带引用的 AI 搜索,是这个环节的结构性升级——但它的正确用法,依然是那六个字:**human-in-the-loop**。

先说升级在哪。传统搜索给你十个链接,合成的活全在你这边(恰恰是短缺的能力);Perplexity 反过来:**先给合成好的答案,每个论断挂着来源角标**——认知负荷的分配从「你来合成」变成「你来核查」,而核查比合成便宜得多,这个负荷转移对执行功能短缺者是真实的可及性增益。工程对应:RAG 架构的本质就是「生成必须挂引用」,让输出从「不可验证的断言」变成「可审计的合成」——**可审计性不保证正确,但它让『验证』第一次变得可行**。

然后是监督位,一共三个,对应 AI 搜索的三个系统性弱点:

**第一,角标要抽查,因为「有引用」不等于「引用支持该论断」。** RAG 系统的已知毛病:引用真实存在,但内容与论断的关系可能是弱相关甚至错配(引用幻觉的温和版)。监督动作:**凡是打算据此行动的论断(尤其补剂、作息、干预方法),点开角标看原文**——十秒钟,只确认一件事:原文真的说了这个吗?对「今晚就想试」的冲动,这十秒就是安全审批流程。

**第二,证据要问级别,因为合成会抹平证据等级。** AI 的综述语气是均质的:一项荟萃分析和一篇小样本预印本,在流畅的段落里读起来一样可信——**合成的代价是证据地形被压扁了**。监督动作:养成追问的习惯,「这个结论的证据等级是什么?有 RCT 吗?样本多大?」——**AI 搜索的美妙之处是追问免费**:一句话就能把地形问回来,这在传统搜索里要自己读十篇文献。

**第三,行动前过人类闸门,因为「读到」和「适合我」之间隔着个体差异。** Goblin 篇讲过:ADHD 干预反应高度个体化,任何来源的「有用」都只是先验概率——**最终判决权在你的自我实验数据里**(每次只试一个变量、记录两周、看你自己的结果)。监督动作:把 Perplexity 的产出定位成「实验候选清单」,不是「行动指令」——**信息层的监督拦截错误信念,实验层的监督拦截不适配的方法**,两道闸,缺一不可。

误用一句话带过:**把带引用的答案当免检产品**(角标从来不点开,追问从来不问,读完直接改作息买补剂)——那你只是把「轻信论坛」升级成了「轻信更流畅的论坛」,监督位全空,系统性风险原样保留。

## 边界

同构强度 B 级:RAG 与引用机制是真实的工程架构,健康信息素养与 ADHD 冲动性的交互有文献基础,「负荷从合成转向核查」的分析有认知科学依据;Perplexity 无 ADHD 相关对照研究。声明:任何 AI 搜索的产出都不构成医疗建议——药物、剂量、停药、补剂与处方药的相互作用,这些问题的闸门只有一个:你的医生;AI 帮你带着更好的问题走进诊室,而不是替代诊室。

## 今天就能试的 3 件事

1. **给上一个「打算试」的结论补一次抽查**:点开角标读原文——原文真说了这个吗?
2. **练一次证据追问**:对任何 ADHD 建议追问「有 RCT 吗?样本多大?」——一句话的事。
3. **建一个「实验候选清单」**:AI 搜到的方法先进清单,每次只放行一个进两周实验。

带引用的答案是更好的起点,但仍然只是起点——**角标你来点,等级你来问,行动你来批**。三个监督位守住了,AI 搜索才是你的研究助理,而不是又一个更会说话的沼泽。

## 参考来源

- [Distinct neuropsychological subgroups in typically developing youth inform heterogeneity in children with ADHD](https://doi.org/10.1073/pnas.1115365109) — 证据等级：低（GRADE）
- [Twenty-Year Trends in Diagnosed Attention-Deficit/Hyperactivity Disorder Among US Children and Adolescents, 1997-2016](https://doi.org/10.1001/jamanetworkopen.2018.1471) — 证据等级：中（GRADE）
- [Striatal Dysfunction in Attention Deficit and Hyperkinetic Disorder](https://doi.org/10.1001/archneur.1989.00520370050018) — 证据等级：低（GRADE）
- [Cognitive, motor, behavioural and academic performances of children born preterm: a meta‐analysis and systematic review involving 64 061 children](https://doi.org/10.1111/1471-0528.14832) — 证据等级：高（GRADE）

---

*本文是「ADHD × AI」系列的第 94 篇，由 Devin 基于持续维护的双域研究语料（72,739 篇论文 + LLM Wiki）亲自撰写，并持续迭代更新。*
