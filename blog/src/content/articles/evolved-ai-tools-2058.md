---
title: "为什么用 Claude 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用 是一回事？"
subtitle: "Claude 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
description: "Claude 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
date: "2025-05-03"
category: "AI工具实战"
categoryId: "ai-tools"
categoryEn: "AI Tools in Practice"
tags:
  - "ADHD"
  - "AI"
  - "AI工具实战"
  - "反直觉同构"
  - "自动化"
readingTime: 14
slug: "为什么用-claude-治-adhd-的任务启动困难和给-agent-套-function-calling-工具调用-是一回事"
topicId: "evolved-ai-tools-2058"
angle: "反直觉同构"
rank: 205
score: 7.51
sourceCount: 6
toolsCited:
  - "Goblin Tools"
  - "Saner.AI"
  - "Lex"
  - "Claude"
  - "ChatGPT"
thesis: "ADHD 大脑与 LLM agent 共享同一类缺陷——强大生成核心缺乏可靠执行调度层，因此两者都需要外部 harness 来补偿任务启动困难与上下文管理缺陷，而 function calling 工具调用正是为 LLM 提供这种调度层的工程实现。"
problem: "为什么用 Claude 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用 是一回事？"
spine: "工具使用与认知卸载"
spineKind: ""
isEvolved: true
llmGenerated: false
caseStudies:
  - "孔子"
  - "左宗棠"
  - "Jacob Avery"
---

# 为什么用 Claude 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用是一回事？

> function calling 解决的问题很朴素:模型知道「该做什么」,却没有「做」的通道——它只能生成文字,不能真的查数据库、发请求。ADHD 的启动困难惊人地同形:知道该做什么(常常比谁都清楚),却接不通「开始做」的那条通道。

先把 ADHD 的启动困难从「拖延」的道德叙事里捞出来。它的现象学很特别:你坐在电脑前,任务清清楚楚,后果明明白白,甚至内心在呐喊「开始啊」——身体却像断了传动。这不是不想做(想的),不是不会做(会的),是**意图到动作之间的挂挡机制失灵**。执行功能研究里这属于任务启动(task initiation)缺陷,和多巴胺驱动的动机激活直接相关:任务的「认知存在」和「行动启动」走的是不同回路,ADHD 坏的是后者的点火器。

LLM 侧的对应结构:模型能在文字里完美描述「接下来应该调用天气 API」,但没有 function calling 机制时,这句描述只是文字——**知与行之间缺一个把「描述」翻译成「执行」的接口**。function calling 的本质就是这个翻译层:把模型的意图输出,变成结构化的、可被系统直接执行的调用。

所以「用 Claude 治启动困难」的正确姿势,不是让它讲道理鼓励你(那是给一个挂挡失灵的车加油门),而是**让它当你的意图→动作翻译层**:

## 启动困难的 function calling 三件套

**第一件:把任务编译成「可调用格式」**。function calling 的前提是把模糊意图变成带参数的结构化调用。人类版:启动不了的任务,九成是以「模糊大块」的格式存着的(「弄一下那个报告」)。丢给 Claude:「把这个任务编译成第一个 10 分钟动作,要具体到打开哪个文件、写下哪句话。」拿到的产出必须满足**「无需再思考即可执行」**——「打开 report.docx,把三个小标题打出来」是合格调用;「开始写报告」不是。启动的阻力和第一步的模糊度成正比,这是可工程化的杠杆。

**第二件:启动仪式当「调用协议」**。function calling 有固定的调用格式,人的启动也需要固定协议——因为**协议的意义是移除临场决策**(临场决策正是启动回路最卡的地方)。设计你的固定启动序列:同一杯水、同一个计时器拧到 25 分钟、读一遍 Claude 给的第一步、动手。序列固定到无聊,效果才好:仪式不是玄学,是把「要不要开始」这个高阻力决策,替换成「按协议走」这个低阻力执行。

**第三件:5 分钟合同当「超时参数」**。每次调用只承诺 5 分钟——「做 5 分钟,到点可以光荣退出」。机制:启动回路怕的是任务的总重量,5 分钟合同把重量从「两小时的报告」骗降到「5 分钟的开头」;而一旦启动,继续的阻力远小于启动的阻力(多数 5 分钟合同会自动续期)。注意「光荣退出」条款必须真实有效——骗自己一次,合同信用就破产了。

## 反模式:把 Claude 用成「关于启动的聊天」

最常见的翻车:启动不了→打开 Claude 聊「我为什么总是启动不了」→聊了四十分钟,获得了深刻的自我认知和零行动——**对话本身成了新的逃避舱**,还带着「我在积极解决问题」的完美伪装。护栏一条:与启动相关的对话,产出必须是一个 10 分钟动作,且对话时长不得超过动作时长。Claude 是翻译层,不是谈心层——在启动这个场景里,翻译完就执行,执行完再回来汇报。

另一个边界要诚实:**翻译层不解决点火能量本身**。任务拆到极致、协议完美,有些日子还是启动不了——那是燃料问题(睡眠、情绪、药物时效),不是接口问题。区分方法:如果连「5 分钟合同」都连续多日失败,查燃料,别再优化接口。

## 边界

同构强度 B 级:function calling 是真实且核心的 LLM 工程机制,ADHD 任务启动缺陷有执行功能文献支撑,「翻译层」是机制映射的实践框架,无对照研究。药物对启动回路的改善是一线证据支持的路径,本文协议是行为层配合——两条腿,不互替。

## 今天就能试的 3 件事

1. **挑今天最启动不了的任务,让 Claude 编译**:产出一个「无需思考即可执行」的 10 分钟动作。立刻执行,不许先收藏。
2. **写下你的启动协议**:三步以内,固定顺序。明早第一个任务试运行。
3. **签一份 5 分钟合同**:今天对最抗拒的事只承诺 5 分钟,退出条款真实有效。

知道该做什么,你从来不缺;缺的是那个把「知道」接进「做」的接口。工程师给模型焊了 function calling,你的版本今天就能上线:一个编译器、一套协议、一份 5 分钟合同——挂挡机制,是可以外装的。

## 参考来源

- [ADHD Apps: We tested 44 Apps and Here're the Best 9 in 2026](https://blog.saner.ai/best-adhd-apps/) — 证据等级：低（GRADE）
- [12 AI Personal Assistants Built for ADHD Brains (2026 Rankings)](https://www.usecarly.com/blog/best-ai-personal-assistant-adhd/) — 证据等级：低（GRADE）
- [Toward Neurodivergent-Aware Productivity: A Systems and AI-Based Human-in-the-Loop Framework for ADHD-Affected Professionals](https://arxiv.org/pdf/2507.06864) — 证据等级：低（GRADE）
- [Agent Scaffolding: Architecture and Design Patterns for Agentic AI](https://zbrain.ai/agent-scaffolding/) — 证据等级：低（GRADE）
- [Confabulation: The Surprising Value of Large Language Model Hallucinations](https://preview.aclanthology.org/navbar-space/2024.acl-long.770.pdf) — 证据等级：低（GRADE）
- [LBD同构对：分心与走神 — Therapeutic Doses of Oral Methylphenidate Significantly Incr ↔ AutoHallusion: Automatic Generation of Hallucination Benchma](https://doi.org/10.1523/jneurosci.21-02-j0001.2001) — 证据等级：低（GRADE）

---

*本文是「ADHD × AI」系列的第 155 篇，由 Devin 基于持续维护的双域研究语料（72,739 篇论文 + LLM Wiki）亲自撰写，并持续迭代更新。*
