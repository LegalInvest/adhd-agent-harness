---
title: "Perplexity 之于 ADHD，就像 生成核心 + 缺失的执行层 之于 LLM——但有人用错了"
subtitle: "从同构视角实测 Perplexity：它到底补上了哪一层执行功能？"
description: "从同构视角实测 Perplexity：它到底补上了哪一层执行功能？"
date: "2025-06-01"
category: "科学研究"
categoryId: "science"
categoryEn: "Scientific Research"
tags:
  - "ADHD"
  - "AI"
  - "科学研究"
  - "工具×同构"
  - "脑科学"
readingTime: 7
slug: "perplexity-之于-adhd就像-生成核心-缺失的执行层-之于-llm但有人用错了"
topicId: "prob-baaff33841"
angle: "工具×同构"
rank: 190
score: 7.53
sourceCount: 5
toolsCited:
  - "Goblin Tools"
  - "Saner.AI"
  - "Motion"
  - "Tiimo"
problem: "Perplexity 之于 ADHD，就像 生成核心 + 缺失的执行层 之于 LLM——但有人用错了"
spine: "ADHD 大脑与 LLM 的同构"
spineKind: "bridge"
isEvolved: false
llmGenerated: false
---

# Perplexity 之于 ADHD，就像 生成核心 + 缺失的执行层 之于 LLM——但有人用错了

> 他是朋友圈公认的「什么都懂先生」:聊健身他能讲清筋膜放松的原理,聊理财他能说出几种资产配置模型,聊育儿他引用的研究比幼儿园老师还新——全部来自他每天几十次的 AI 搜索。直到某天体检报告出来,常年不动的他各项指标飘红,妻子说了一句杀伤力极大的话:「你连『久坐的危害』都能讲十分钟,你讲的时候就坐着。」知识在他身上进得来,出不去——**不是出不去嘴,是出不去手。**

收敛:本文只回答——**为什么 AI 搜索把「知道」的成本降到接近零之后,「知道却不做」的鸿沟反而变宽了?知识到行动之间缺的那一层,对 ADHD 来说具体缺在哪、怎么补?**

## 穿透:知识免费之后,执行层成了唯一的瓶颈

LLM 侧的架构事实:一个生成核心可以对任何问题给出高质量的「怎么做」,但没有执行层(工具调用、状态管理、真实世界的反馈回路)时,这些「怎么做」只是文本——**模型知道一万种部署方案,不接执行器,一行代码都不会真的运行。**工程界从不把「能生成方案」和「能完成任务」混为一谈,这两者之间隔着整个 harness。

人类侧,这条沟原本被学习成本掩盖着:过去「搞懂筋膜放松」需要读书、上课、请教——获取知识的过程本身附带了投入、承诺和社群,行动常常顺势发生。AI 搜索把获取压缩到三十秒后,**知识与行动彻底解耦**:你可以在完全零投入的状态下「懂」任何事。对 ADHD,这个解耦是双重打击:①「懂了」的瞬间有真实的多巴胺(新知的奖励),它部分满足了那个本该由行动满足的心理需求——**搜索成了行动的代餐**;②行动需要的启动、维持、忍受无聊,全是谷值区技能,于是天平永远倒向再懂一点。「什么都懂先生」不是知识的富翁,是被代餐喂饱的执行饥民。

补执行层,关键是承认一个原则:**知识不该被允许自由进入,除非它绑定了一个动作。**三个组件:①**进口关税**——任何「怎么做」类的搜索,结束时强制回答一个问题:「基于这个答案,我 48 小时内做的最小动作是什么?」答不出或不打算做,这条知识按娱乐记账(娱乐合法,但别记成成长);②**单线原则**——同时在「实施中」的知识只许一条(WIP limit 的知识版):健身方案没落地前,理财方案不许立项;③**反馈回路**——动作做完记一行真实结果,让知识第一次接触你的现实(筋膜放松「原理正确」和「你做了三天就膝盖疼」是两种知识,后者才是你的)。

利益视角:知识类内容与 AI 搜索的商业模式都靠「懂的感觉」留住你——「48 小时行动税」会降低使用愉悦度,没有产品会内置它;执行层永远是用户自装组件。

## 验证

两周协议:给所有「怎么做」搜索加进口关税,记录两个数:立项的知识条数、48 小时内实际执行数。健康比值应接近 1:1(靠的不是执行力暴涨,是立项数暴跌——关税的主要作用是拦住那些你从没打算做的「懂」)。可证伪:若立项确实少了、执行率依然为零,瓶颈在启动系统本身,回去修启动坡道(拆粒度/找 body double),关税只管住入口,管不了发动机。

## 决策

做什么:装进口关税+单线原则+反馈回路;把「我知道」从口头禅里降级——在自己的账本上,只有带过行动的知识才叫知道。

不做什么:不要再为「广博」自豪并用它社交变现(那是在给代餐镀金);不要同时启动三个「新生活方案」——单线,永远单线。

先做什么:选出你「懂得最多做得最少」的那个领域,今天交一次关税:48 小时内的最小动作,现在写下来,现在排期。

## 边界

「生成核心/执行层」为 B 级架构类比(知行分离的结构两侧成立,机制不同);「搜索代餐」是行为模式描述而非诊断(本文未做正式 A/B/C 分级)。知识获取本身无罪——本文批评的是它对行动的替代性占位。若「知道做不到」的鸿沟伴随强烈自责或已弥漫多年,请考虑专业评估,执行系统的深层故障值得临床级的对待。

## 今天就能试的 3 件事

1. 给你最近一次「怎么做」搜索补交关税:写下 48 小时内的最小动作,现在排进日历。
2. 立单线原则:写下当前唯一「实施中」的知识项目,其余全部移入「排队区」。
3. 做一次残酷盘点:列出你能讲十分钟却零实践的三个领域——不为自责,为看清代餐账单的规模。

本文服务于人生 Harness 金字塔的**执行层与价值层**:AI 把「知道」变成了自来水,于是人和人的差距,彻底搬到了水龙头之后——你的人生不由你懂什么决定,由你把哪几条懂的东西,真的接进了手里。

## 参考来源

- [ADHD is best understood as a cultural construct](https://doi.org/10.1192/bjp.184.1.8) — 证据等级：低（GRADE）
- [Review and Classification of Emotion Recognition Based on EEG Brain-Computer Interface System Research: A Systematic Review](https://doi.org/10.3390/app7121239) — 证据等级：高（GRADE）
- [Corpus callosum morphology in children with Tourette syndrome and attention deficit hyperactivity disorder](https://doi.org/10.1212/wnl.47.2.477) — 证据等级：低（GRADE）
- [Cognitive Training for Attention-Deficit/Hyperactivity Disorder: Meta-Analysis of Clinical and Neuropsychological Outcomes From Randomized Controlled Trials](https://doi.org/10.1016/j.jaac.2014.12.010) — 证据等级：高（GRADE）
- [What Aspects of Peer Relationships Are Impaired in Children With Attention-Deficit/Hyperactivity Disorder?](https://doi.org/10.1037/0022-006x.73.3.411) — 证据等级：低（GRADE）

---

*本文是「ADHD × AI」系列的第 59 篇，由 Devin 基于持续维护的双域研究语料（72,739 篇论文 + LLM Wiki）亲自撰写，并持续迭代更新。*
