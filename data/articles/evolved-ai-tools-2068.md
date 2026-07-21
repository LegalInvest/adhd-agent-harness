---
title: "为什么用 Perplexity 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用 是一回事？"
subtitle: "Perplexity 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
description: "Perplexity 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
date: "2025-05-14"
category: "AI工具实战"
categoryId: "ai-tools"
categoryEn: "AI Tools in Practice"
tags:
  - "ADHD"
  - "AI"
  - "AI工具实战"
  - "反直觉同构"
  - "智能助手"
readingTime: 13
slug: "为什么用-perplexity-治-adhd-的任务启动困难和给-agent-套-function-calling-工具调用-是一回事"
topicId: "evolved-ai-tools-2068"
angle: "反直觉同构"
rank: 282
score: 7.45
sourceCount: 6
toolsCited:
  - "Perplexity"
  - "Goblin Tools"
  - "Saner.AI"
  - "Lex"
  - "ChatGPT"
thesis: "ADHD 大脑与 LLM 在结构上同构——都是强大的生成核心但缺乏可靠的内置执行调度层，因此用 Perplexity 等 AI 工具辅助任务启动，与给 agent 套 function calling 工具调用，本质是同一类工程：通过外部脚手架补偿执行功能缺陷。"
problem: "为什么用 Perplexity 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用 是一回事？"
spine: "工具使用与认知卸载"
spineKind: ""
isEvolved: true
llmGenerated: false
caseStudies:
  - "孔子"
  - "辛弃疾"
  - "李静"
---

# 为什么用 Perplexity 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用是一回事？

> 任务启动困难的第三张面孔,既不是「不知道第一步」,也不是「永远等会儿」,而是:第一步是「先搞清楚一个东西」,而「搞清楚」本身就是一片沼泽。办签证卡在「要什么材料」,报税卡在「新政策怎么算」,修简历卡在「这行业现在要什么」——任务没启动,是因为它的入口处站着一个未解决的信息问题。

先给这类启动失败画像:**信息前置型**。它的结构是:任务的第一步依赖某个知识缺口→填补缺口需要检索→而检索对 ADHD 是高危路段(十七个标签页、越查越散、一小时后在看无关内容)→于是「查一下」被无限期搁置→任务连第一步都没有。**最气人的是,这类任务往往缺的只是十分钟的信息**——但「预计会掉进检索沼泽」的隐性成本评估,让大脑直接把整个任务标记为「今天别碰」。研究执行功能的人会认出这个模式:任务启动的成本评估是前瞻性的,**评估的是感知成本,不是真实成本**——而 ADHD 的检索体验史,把「查东西」的感知成本推得极高。

function calling 视角一摆,解法清晰了:LLM 碰到知识缺口不会自己硬想(那叫幻觉),它调用检索工具,拿到结果继续推理。**Perplexity 就是给「信息前置型启动困难」注册的检索函数**:一个问题进去,一份综合好的答案带引用出来——没有十七个入口,没有沼泽;感知成本从「一下午」跌回「十分钟」,任务入口的路障清除。

## 用成真正的 function calling,三条纪律

**一、把「查一下」识别为函数调用,而不是任务本身。** 触发判据:**一个任务搁置超过三天,自查「它是不是卡在某个没搞清楚的问题上?」**——是,就把那个问题写成一句具体的话(「办 X 签证需要哪些材料+多久出签」),丢给 Perplexity,十分钟内拿到答案。**写成一句话这个动作本身就是半个解药**:沼泽感的来源常常是「要查的东西」从未被明确过。

**二、返回值直接接执行,不落中转站。** 拿到材料清单,立即做下一个物理动作(把清单抄进任务、约时间、下载表格)——**答案落地为动作,调用才算闭环**。最常见的浪费:查完了,「今天先这样」,三天后又忘了查过什么,任务退回原点(这就是为什么上一批文章反复强调「查过了」存档)。

**三、限定辖区:它是检索函数,不是启动函数。** 三种启动困难,三个函数:任务是雾→拆解函数;把手有了但永远等会儿→调度函数;入口有信息路障→检索函数。**误诊会浪费工具**:如果查完材料清单还是启动不了,说明真正的卡点在别处(拆解、调度,或情绪),该换函数了,不是再查一遍。

## 用错的姿势速查

**用检索模拟进度**:查了三遍攻略,签证依然没办——第三遍检索时你缺的不是信息,是第一步;检索的舒适感(有产出、无风险)恰是它作为拖延姿势的危险之处。**范围膨胀**:查「签证材料」查着查着在研究「目的地美食」——即便在 Perplexity 里,相关推荐依然是下一跳;产出物落袋即关,纪律不变。**用它查「不可检索的问题」**:「我该不该换工作」丢给检索,返回的是通用建议的拼盘——价值决策是本体职责,函数越界调用,返回值必然失真。

## 边界

同构强度 C 级:如实标注——function calling 与检索工具的对应是真实的,ADHD 启动困难与感知成本的关系有执行功能文献的间接支撑,但「信息前置型启动困难」是本文提出的操作性分类,无直接研究验证;把它当一个可能有用的透镜,不是诊断类别。声明:启动困难普遍且顽固、或检索行为已强迫化(反复查证求安心)时,请专业评估;本文是使用策略,不是治疗。

## 今天就能试的 3 件事

1. **扫一遍搁置超过三天的任务**:哪几个卡着一个「没搞清楚的问题」?把问题各写成一句话。
2. **今天清掉一个**:一句话→Perplexity→答案落地为下一个物理动作,全程 15 分钟内。
3. **给一个「查过三遍」的任务判刑**:承认信息已够,写下第一步,现在做。

给 agent 接检索工具的道理,是让「不知道」不再堵塞「推理」;给自己接 Perplexity 的道理,是让「没查」不再堵塞「开始」。信息路障十分钟可拆——拆完发现还是不动,恭喜你:真正的卡点现身了,换对函数,继续。

## 参考来源

- [ADHD Apps: We tested 44 Apps and Here're the Best 9 in 2026](https://blog.saner.ai/best-adhd-apps/) — 证据等级：低（GRADE）
- [12 AI Personal Assistants Built for ADHD Brains (2026 Rankings)](https://www.usecarly.com/blog/best-ai-personal-assistant-adhd/) — 证据等级：低（GRADE）
- [Getting Started with AI for ADHD for ADHD: AI Tools... | Blue Orchid](https://www.blueorchid.world/adhd/guides/getting-started-with-ai-for-adhd) — 证据等级：低（GRADE）
- [An ADHD ChatGPT Guide: Helpful Prompts & ADHD Hacks - I'm Busy Being Awesome](https://imbusybeingawesome.com/chatgpt-adhd/) — 证据等级：低（GRADE）
- [ADHD Task Managers That Work: Top AI Tools 2025](https://www.sentisight.ai/ai-neurodivergent-productivity-adhd-friendly/) — 证据等级：低（GRADE）
- [ADHD Assessment Form Template with Examples - Heidi Health](https://www.heidihealth.com/en-us/blog/adhd-assessment-form-template) — 证据等级：低（GRADE）

---

*本文是「ADHD × AI」系列的第 211 篇，由 Devin 基于持续维护的双域研究语料（72,739 篇论文 + LLM Wiki）亲自撰写，并持续迭代更新。*
