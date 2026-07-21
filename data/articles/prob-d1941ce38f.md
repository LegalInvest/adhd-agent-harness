---
title: "Perplexity 之于 ADHD，就像 human-in-the-loop 监督 之于 LLM——但有人用错了"
subtitle: "从同构视角实测 Perplexity：它到底补上了哪一层执行功能？"
description: "从同构视角实测 Perplexity：它到底补上了哪一层执行功能？"
date: "2025-05-05"
category: "社群与文化"
categoryId: "community"
categoryEn: "Community & Culture"
tags:
  - "ADHD"
  - "AI"
  - "社群与文化"
  - "工具×同构"
  - "去污名化"
readingTime: 10
slug: "perplexity-之于-adhd就像-human-in-the-loop-监督-之于-llm但有人用错了"
topicId: "prob-d1941ce38f"
angle: "工具×同构"
rank: 188
score: 7.53
sourceCount: 5
toolsCited:
  - "Goblin Tools"
  - "Saner.AI"
  - "Motion"
  - "Tiimo"
problem: "Perplexity 之于 ADHD，就像 human-in-the-loop 监督 之于 LLM——但有人用错了"
spine: "人在回路与身体在场"
spineKind: "llm"
isEvolved: false
llmGenerated: false
---

# Perplexity 之于 ADHD，就像 human-in-the-loop 监督 之于 LLM——但有人用错了

> 她给自己的「研究流程」感到骄傲:任何决定之前——买课、换工作方向、给孩子选干预方案——她都会用 AI 搜索做足功课,收藏夹里躺着几十份「调研结论」。直到闺蜜问了一句:「你研究换工作研究半年了,面试投了几个?」她卡住了。答案是零。那几十次搜索给她的不是决策,是**决策的感觉**——每查一轮,焦虑降一点,行动的紧迫感也跟着降一点,然后生活原样继续。

收敛:本文只回答——**「查询」在决策回路里的正确位置是什么?为什么 ADHD 用户特别容易把「持续查询」用成「无限延期的批准流程」?怎么把 human-in-the-loop 的工程纪律搬过来治它?**

## 穿透:HITL 的核心从来不是「人参与」,是「环会闭合」

LLM 侧把概念讲干净。human-in-the-loop 监督的工程含义:agent 在关键节点暂停,把中间结果交给人审批,人给出 go/no-go,**然后流程必须继续**——HITL 的设计红线是人这一环不能变成流程的黑洞,所以成熟系统都带超时机制:审批悬置超过阈值,要么升级要么按默认策略放行。**「环」的价值在于闭合;一个永不闭合的审批环,比没有环更糟——它既阻塞了执行,又制造了「正在处理」的假象。**

她的用法错在哪就清楚了:每一轮 AI 搜索都是一次「提交审批」,但审批人(她自己)从不签发 go/no-go——查询结果不落到决策,落到收藏夹,然后触发下一轮查询。这个模式对 ADHD 格外致命,机制有三:①**查询是完美的伪行动**——它有信息摄入的充实感、有「负责任」的道德光环、且启动成本远低于真行动(投简历要面对被拒,搜索不用);②**延迟折扣让「再查查」永远显得划算**——行动的收益在远期,查询的安抚在当下;③**没有外部超时**——工作流程里的审批有 deadline,人生决策的审批没人催,环就永远敞着。

修法是把工程纪律逐条搬回来:①**查询配额**——任何决策立项时先定「调研预算」(如:三次搜索/两小时/五个来源),预算烧完必须出一个中间产物;②**强制签发格式**——每轮调研的产出不许是收藏,必须是一句 go/no-go/需要补查 X(具体到一项);③**超时默认策略**——预设「若两周内未决,则执行默认选项」(默认选项在冷静时定好:通常是「做可逆的最小尝试」——投三份简历、约一次试听,而不是全有或全无)。

利益视角:AI 搜索的产品指标是查询量与回访率——「帮你结束搜索」不在任何产品的利益里;审批环的闭合装置,只能装在你这一侧。

## 验证

自查有一个残忍但有效的指标:**收藏夹/行动比。**过去三个月,你的调研产物里有多少转化成了一次真实的、不可撤销的行动(发出的申请、付的定金、说出口的决定)?比值低于 10:1,你的 HITL 已经变成了 human-is-the-loophole。协议可测:下一个决策用「配额+签发+超时」三件套,对照过去的同类决策,比较从立项到首个真实行动的天数。可证伪:若三件套下你做出了草率的坏决定,说明你的配额定得太紧——调宽预算,但保留闭环结构;结构的敌人是「敞着」,不是「快」。

## 决策

做什么:给当前悬置最久的那个决策补装三件套;把「我再查查」重新翻译为它的真实含义之一:「我暂时不敢行动」——然后处理「不敢」,而不是喂它更多信息。

不做什么:不要用新一轮搜索安抚决策焦虑(焦虑要用「可逆的最小行动」治,不用信息治);不要收藏任何没有附带 go/no-go 判断的调研结果。

先做什么:找出你收藏夹里躺得最久的那个「研究项目」,现在给它签发一个动作:go(今天做最小一步)或 no-go(正式关闭,删除收藏)。

## 边界

「HITL↔决策回路」为 B 级架构类比(审批环闭合的原则两侧成立);「查询成瘾式拖延」是行为模式描述,非诊断类别(本文未做正式 A/B/C 分级)。若决策回避伴随广泛的焦虑或已显著影响生活,请考虑专业评估——那可能是焦虑议题而非信息问题,值得被专业地对待。

## 今天就能试的 3 件事

1. 算一次你的收藏夹/行动比——过去三个月的调研,落地了几个真动作?
2. 给悬置最久的决策签发 go/no-go:go 则今天完成最小可逆一步,no-go 则删收藏关项目。
3. 给下一个新决策立项时写下三行:调研配额__/默认选项__/超时日期__——贴在收藏夹的第一位。

本文服务于人生 Harness 金字塔的**执行层与价值层**:信息的意义是喂给决策,决策的意义是喂给人生——环闭合的那一刻,搜索才终于值回了它承诺你的东西。

## 参考来源

- [Subtyping Attention-Deficit/Hyperactivity Disorder Using Temperament Dimensions](https://doi.org/10.1001/jamapsychiatry.2014.763) — 证据等级：中（GRADE）
- [Changes and challenges in 20 years of research into the development of executive functions](https://doi.org/10.1002/icd.736) — 证据等级：低（GRADE）
- [Treatment of Attention-Deficit/Hyperactivity Disorder: Overview of the Evidence](https://doi.org/10.1542/peds.2004-2560) — 证据等级：低（GRADE）
- [Adolescents' Intense and Problematic Social Media Use and Their Well-Being in 29 Countries](https://doi.org/10.1016/j.jadohealth.2020.02.014) — 证据等级：低（GRADE）
- [Maternal depression and early positive parenting predict future conduct problems in young children with attention-deficit/hyperactivity disorder.](https://doi.org/10.1037/0012-1649.43.1.70) — 证据等级：低（GRADE）

---

*本文是「ADHD × AI」系列的第 57 篇，由 Devin 基于持续维护的双域研究语料（72,739 篇论文 + LLM Wiki）亲自撰写，并持续迭代更新。*
