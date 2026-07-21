---
title: "为什么用 Motion 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用 是一回事？"
subtitle: "Motion 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
description: "Motion 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
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
readingTime: 11
slug: "为什么用-motion-治-adhd-的任务启动困难和给-agent-套-function-calling-工具调用-是一回事"
topicId: "evolved-ai-tools-2049"
angle: "反直觉同构"
rank: 140
score: 7.75
sourceCount: 6
toolsCited:
  - "Motion"
  - "Goblin Tools"
  - "Saner.AI"
  - "Lex"
  - "ChatGPT"
thesis: "ADHD大脑与LLM都是高产生成核心却缺乏内置调度层，两者都需要外部harness（脚手架）来补偿执行功能缺陷——Motion的任务启动辅助与agent的function calling在架构上同构。"
problem: "为什么用 Motion 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用 是一回事？"
spine: "工具使用与认知卸载"
spineKind: ""
isEvolved: true
llmGenerated: false
caseStudies:
  - "孔子"
  - "孙策"
  - "Brittney Campbell"
---

# 为什么用 Motion 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用是一回事？

> 任务启动难,不止「不知从哪下手」一种。还有一种更隐蔽的:知道第一步,也拆好了,但「什么时候做」永远悬而未决——于是永远是「等会儿」。Goblin Tools 解决前者;Motion 瞄准的是后者。用 function calling 的语言说:前者外包的是「拆解」函数,后者外包的是「调度」函数——两个不同的短板,两次不同的注册。

先分清这两种启动失败。**拆解型**:任务是雾,没有把手——上一篇的辖区。**调度型**:把手有了,但「现在做还是等会儿做」这个决策每小时都在被重新评估,而 ADHD 的评估器天然偏向「等会儿」(当下的任何刺激都比未来的任务响亮)。调度型失败的隐蔽之处在于它不像瘫痪,像忙碌:你一天都在做事,只是永远在做「刚好出现在面前的事」,而不是「该做的事」。**决策疲劳是它的放大器**:「现在干嘛」一天要决策几十次,每次都消耗执行资源,到下午,评估器直接躺平,刺激接管全场。

Motion 注册的正是这个函数:**你把任务(带死线、时长)交出去,「什么时候做什么」由算法返回**——日历上此刻高亮的块,就是调用的返回值。启动的决策成本从「几十次/天」压缩到「零」:不需要评估,不需要选择,只需要服从当前块。这对调度型启动困难是外科手术式的精确——**它删除的恰好是你反复失败的那个决策环节。**

## 用成真正的 function calling,三条纪律

**一、认清自己调的是哪个函数。** 如果你的卡点是拆解型,Motion 帮不了你——它拿到「写年终总结」只会排出一个四小时巨块,你照样启动不了。**先用拆解函数(自己拆/Goblin Tools/Claude),再把小块喂给调度函数**——两个工具串联,恰似 agent 把 planner 的输出喂给 scheduler。很多人退订 Motion 的真实原因,是拿调度工具治拆解问题,药不对症。

**二、信任返回值,但设超时。** function calling 的要义是「调了就用,不二次怀疑」——每个块到点就做,不重新评估「要不要现在做」(重新评估=把删掉的决策环节又装回来了)。配 25 分钟超时:确实进不去,让它重排,不自责。**服从上有弹性,弹性下有底线:一天主动跳过不超过 2 块。**

**三、保住本体的职责。** 调度外包了,两样不能外包:**任务准入**(什么值得进日历——算法只排你给的,垃圾进垃圾出)和**估时诚实**(录入时长×1.5,否则返回值永远失真)。每周五花 10 分钟看被推最多的任务——那是调用日志,里面写着你的真实短板地图。

## 用错的姿势速查

**用调度逃避拆解**:日历上躺着「写论文(4h)」连续被推两周——那不是调度失败,是它在提醒你先调拆解函数。**过度调用**:周末、休息、社交也全部排块——调度函数的辖区是「该做但启动不了的事」,不是人生的全部;给自发性留出未注册的空间,否则工具会把你最好的东西(即兴、漫游、遇见)也调度掉。**返回值权威崩塌**:频繁跳过高亮块又不砍任务量——每一次无后果的违约都在给「日历说话不算数」投票,三周后这个工具对你就失效了;宁可排一半,保住权威。

## 边界

同构强度 B 级:外部调度是真实的系统设计模式,ADHD 的延迟折扣与决策疲劳有文献支撑,Motion 无 ADHD 对照研究,「两函数串联」是本文的操作化框架。声明:若「等会儿」的背后是对任务的恐惧或完美主义冻结,调度解决不了——那需要处理的是情绪层;启动困难广泛且顽固时,请专业评估,药物+行为结构的组合证据最好。

## 今天就能试的 3 件事

1. **诊断你的启动失败类型**:拆解型(任务是雾)还是调度型(把手有了但永远等会儿)?写下来。
2. **串联一次两个函数**:把一个任务拆成三小块,喂进日历(手动排也行),到点服从。
3. **看一眼你的「被推榜」**:哪个任务被推最多?它需要的是拆细、砍掉,还是另一种帮助?

function calling 的智慧在于精确:什么短板,注册什么函数。拆解的雾,交给拆解器;调度的悬置,交给调度器;而「这一切为了什么」——那个函数,永远跑在你自己的本体上。

## 参考来源

- [ADHD Apps: We tested 44 Apps and Here're the Best 9 in 2026](https://blog.saner.ai/best-adhd-apps/) — 证据等级：低（GRADE）
- [12 AI Personal Assistants Built for ADHD Brains (2026 Rankings)](https://www.usecarly.com/blog/best-ai-personal-assistant-adhd/) — 证据等级：低（GRADE）
- [¡Hacia una IA neurodivergente! (迈向神经多样性AI)](https://ddd.uab.cat/pub/uabdivulga/uabdivulga_a2026m1/uabdivulga_a2026m1a4iSPA.pdf) — 证据等级：低（GRADE）
- [Monotropic Artificial Intelligence: Toward a Cognitive Taxonomy of Domain-Specialized Language Models](https://arxiv.org/pdf/2603.00350v1) — 证据等级：低（GRADE）
- [Transient Frontal Fracturing: A Theoretical Account of Hyperfocus](https://watermark02.silverchair.com/jocn.a.2428.pdf) — 证据等级：低（GRADE）
- [Getting Started with AI for ADHD for ADHD: AI Tools... | Blue Orchid](https://www.blueorchid.world/adhd/guides/getting-started-with-ai-for-adhd) — 证据等级：低（GRADE）

---

*本文是「ADHD × AI」系列的第 210 篇，由 Devin 基于持续维护的双域研究语料（72,739 篇论文 + LLM Wiki）亲自撰写，并持续迭代更新。*
