---
title: "为什么用 Focusmate 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用 是一回事？"
subtitle: "Focusmate 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
description: "Focusmate 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
date: "2025-04-07"
category: "AI工具实战"
categoryId: "ai-tools"
categoryEn: "AI Tools in Practice"
tags:
  - "ADHD"
  - "AI"
  - "AI工具实战"
  - "反直觉同构"
  - "AI工具"
readingTime: 10
slug: "为什么用-focusmate-治-adhd-的任务启动困难和给-agent-套-function-calling-工具调用-是一回事"
topicId: "prob-fe3d1c1b20"
angle: "反直觉同构"
rank: 179
score: 7.69
sourceCount: 6
toolsCited:
  - "Focusmate"
  - "Goblin Tools"
  - "Lex"
  - "Saner.AI"
thesis: "ADHD 大脑与 LLM 都是「高产生成核心 + 不可靠执行调度层」；用 Focusmate 帮 ADHD 启动任务，和给 LLM 套上 function calling 工具 harness，本质是在同一套结构里补同一块短板：把模糊的意图转译成可执行、可验证、可回滚的外部动作接口。"
problem: "为什么用 Focusmate 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用 是一回事？"
spine: "工具使用与认知卸载"
spineKind: ""
isEvolved: true
llmGenerated: false
isoStrength: "A"
caseStudies:
  - "孔子"
  - "左宗棠"
  - "辛梅"
---

# 为什么用 Focusmate 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用 是一回事？

> function calling 系列讲了打包、递送、schema、环境——全是系统自己的事。这一篇讲一个更狠的机制:当一个调用怎么都不肯发生时,工程上还有最后一招——**把它绑进一个「必须履约的外部协议」里**。Focusmate 的原理,五十分钟的视频对坐、一个陌生人、一句「我要做 X」——听起来和工具调用毫无关系,但拆开看,它恰恰是 agent 工程里最可靠的一种调用保障:带外部承诺的同步调用。

先看工程侧这个机制。异步的、无人等待的调用,失败是廉价的:没执行就没执行,重试就是了——**系统对「不执行」毫无压力**。但有一类调用被设计成「协议绑定」:另一端有服务在等待响应、有超时会报错、有下游依赖这次返回——**调用被嵌进一个「不执行会立刻产生外部后果」的结构里,执行率完全不同**。工程师深谙此道:要保证一段代码真的跑,最强的办法不是优化它,是让别的东西等着它的结果。

现在看 ADHD 启动困难里最顽固的那部分。前四篇的手段(打包/递送/格式/环境)都在降低启动的成本,但**成本降到零,启动仍可能不发生——因为「不启动」同样零成本**:没人知道、没人等待、后果远在天边(死线还有三天)。ADHD 对远期后果的折扣率又特别高,于是「今天不开始」在主观账本上几乎是免费的。**启动方程的另一半,从来不是降低启动的成本,是提高「不启动」的成本——而且必须是即时的成本,远期的吓不动这颗大脑。**

Focusmate 的设计精确地补上这一半:预约一个五十分钟的时段→另一头有个真人也预约了→开场互相说一句「我这节做 X」→各自干活→结束互相汇报。拆解它的机制:①**预约=签订协议**(爽约会让一个具体的人空等,即时、具体、有脸有名的社交成本——不是「未来的我会失望」那种虚拟货币);②**开场宣告=调用参数公示**(说出「我做 X」之后,五十分钟后要交代,含糊不得);③**对方的存在=持续的低强度监督**(镜头里有人,刷手机的动作突然变得很难做出来——body doubling 的核心效应,ADHD 社区多年的经验共识,近年也有初步研究关注)。**三层合起来:启动从「可以无限推迟的私事」变成「有人等着的履约」。** 按协议的逻辑用它:

**一、把最推不动的任务,绑进最早的时段。** 别用宝贵的协议时段做本来就会做的事——**专治「三天了还没打开的那个文件」**:预约明早第一节,开场宣告就说它。协议的威力要用在市场失灵的地方。

**二、宣告要具体到可验收。** 「我做论文」是逃逸友好型宣告;「我写完方法部分的前两段」才是协议——**结束时的汇报环节,是这套机制的验证层,给它一个能核对的标的。**

**三、爽约成本要保护,不要架空。** 连续取消预约、或人在镜头前心在手机里——协议被你驯化成了摆设。对策:预约后立刻把时段写进日历并告诉一个人「我九点有个专注会」;**协议的牙齿是你自己喂出来的,也能被你自己拔掉。**

**四、认清它的辖区:启动与维持,不含质量。** 有人对坐能保证你打开文件、坐满五十分钟,不能保证写得好——质量问题回到拆解与验证的辖区。另外,社交敏感高的日子(镜头本身造成焦虑),换异步版本:告诉朋友「一小时后我发你进度截图」——协议的形式可以降级,结构保持。

## 边界

同构强度 B 级:协议绑定对执行率的影响是真实的工程与行为经济学机制(承诺装置有较多研究),body doubling 在 ADHD 社区有广泛经验支持、实证研究尚初步,Focusmate 本身无对照研究。声明:社交监督对多数人是助力,对社交焦虑者可能是负担——形式可调,别硬扛;若「不启动」的背后是抑郁性的动力缺失(什么都不想动、伴随情绪低落),那不是承诺装置的辖区,请专业评估。

## 今天就能试的 3 件事

1. **给「那个文件」预约一个协议时段**:明早第一节,Focusmate 或约朋友视频对坐。
2. **写好你的可验收宣告**:「这节我完成——」,具体到结束时能核对。
3. **建一个降级版协议**:找一个朋友,互为「一小时后交进度截图」的对象,零成本起步。

降低启动成本的工具讲了四篇,这一篇是反向的最后一块:**让「不启动」变贵**。一个陌生人的五十分钟,买到的其实是你自己签给自己、却终于有人见证的一纸合同——原来这颗大脑不是不守约,是从来没人跟它正经签过约。

## 参考来源

**同构强度：A 级** —— 直接文献支撑（引用 ADHD↔LLM 同构专题研究）

- [ADHD Apps: We tested 44 Apps and Here're the Best 9 in 2026](https://blog.saner.ai/best-adhd-apps/) — 证据等级：低（GRADE）
- [12 AI Personal Assistants Built for ADHD Brains (2026 Rankings)](https://www.usecarly.com/blog/best-ai-personal-assistant-adhd/) — 证据等级：低（GRADE）
- [Deficient Executive Control in Transformer Attention](https://www.biorxiv.org/content/10.1101/2025.01.22.634394v1.full.pdf) — 证据等级：低（GRADE）
- [Strong Memory, Weak Control: An Empirical Study of Executive Functioning in LLMs](https://preview.aclanthology.org/evt-to-venues/2026.eacl-long.281.pdf) — 证据等级：低（GRADE）
- [Self-Attention Limits Working Memory Capacity of Transformer-Based Models](https://arxiv.org/pdf/2409.10715) — 证据等级：低（GRADE）
- [Human-like Working Memory Interference in Large Language Models](https://arxiv.org/pdf/2604.09670) — 证据等级：低（GRADE）

---

*本文是「ADHD × AI」系列的第 59 篇，由 Devin 基于持续维护的双域研究语料（72,739 篇论文 + LLM Wiki）亲自撰写，并持续迭代更新。*
