---
title: "为什么用 Routinery 治 ADHD 的不知哪些方法有用，和给 agent 套 human-in-the-loop 监督 是一回事？"
subtitle: "Routinery 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
description: "Routinery 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
date: "2025-04-27"
category: "亲子教育"
categoryId: "parenting"
categoryEn: "Parenting & Education"
tags:
  - "ADHD"
  - "AI"
  - "亲子教育"
  - "反直觉同构"
readingTime: 14
slug: "为什么用-routinery-治-adhd-的不知哪些方法有用和给-agent-套-human-in-the-loop-监督-是一回事"
topicId: "prob-daf54837e7"
angle: "反直觉同构"
rank: 376
score: 7.62
sourceCount: 6
toolsCited:
  - "Goblin Tools"
  - "Motion"
  - "Saner.AI"
thesis: "ADHD 大脑与 LLM/agent 都是‘高产但缺执行调度层’的生成核心，用 Routinery（可重复流程脚手架）治疗 ADHD 的‘不知哪些方法有用’，与给 agent 加 human-in-the-loop 监督本质上是同一套 harness：外部化调度、在回路中重新接地、把脚手架而非拐杖嵌入日常。"
problem: "为什么用 Routinery 治 ADHD 的不知哪些方法有用，和给 agent 套 human-in-the-loop 监督 是一回事？"
spine: "人在回路与身体在场"
spineKind: ""
isEvolved: true
llmGenerated: false
isoStrength: "B"
caseStudies:
  - "张謇"
  - "苏轼"
  - "米萍"
---

# 为什么用 Routinery 治 ADHD 的不知哪些方法有用，和给 agent 套 human-in-the-loop 监督 是一回事？

> Routinery 做的事非常朴素:把一段例程(晨间/睡前/收工)拆成带时长的步骤序列,执行时逐步倒计时、逐步打勾——像给生活装了一个流程引擎。对 ADHD,它瞄准的是一个被低估的痛点:**例程明明是最该自动化的东西,却每天都要靠现场决策来驱动**——「刷牙之后干嘛来着?」「还要不要拉伸?」——神经典型的人靠习惯的自动挡开过这段路,而 ADHD 的习惯形成机制偏弱(奖赏回路的延迟折扣让「重复 66 天成习惯」的经典路径格外艰难),于是每个早晨都是一次手动挡的重新起步。Routinery 的方案是**把「习惯」这个内部自动化,替换成「流程引擎」这个外部自动化**——序列写好,执行时只需跟随。逻辑漂亮。但三个月后的灵魂拷问照例到来:**为什么我建了七个精美例程,现在一个都没在跑?**是例程设计错了、工具不适合、还是「用 app 跑例程」这个模式对我根本不成立?——工具自己给不了答案,**能给答案的是一个装了监督回路的人**:这正是 agent 工程对一切自动化流程的态度——**流程引擎负责执行,人负责观测流程的真实运行数据并持续修编排**。

用工程语言重述 Routinery 的架构位置,监督点就自然浮现了。它本质上是一个**工作流编排器(workflow orchestrator)**:预定义步骤序列+每步超时+完成确认。工程上,编排器上线后最常见的三种死法,恰好就是 ADHD 用户的三种弃用剧本:**死法一:触发失败**——工作流写好了,但没有任何事件去启动它(你忘了打开 app,或通知响了但被划掉)——**编排器再完美,没有触发器就是死代码**;**死法二:步骤超编**——把理想主义塞进序列(晨间例程 14 步 45 分钟),真实执行到第 4 步就崩,崩两次后整个流程被回避(全或无的机制:跑不完=失败=不如不跑);**死法三:静态腐化**——生活变了(换季/换工作/孩子放假),例程没变,越来越不合身,摩擦累积到弃用——**没有版本迭代的工作流,注定腐化**。三种死法,三个监督旋钮。

逐个修。**修触发:把例程锚到既有事件上**。app 通知是最弱的触发器(ADHD 对通知的耐受性衰减极快);强触发是**事件锚+物理布景**:「咖啡机按下=打开 Routinery 晨间流程」(把手机支架装在咖啡机旁,物理路径替你按播放键)——**触发器的强度不看提醒多响,看它在不在你必经的路径上**。**修超编:用完成率倒推步骤数**。监督指标就一个:**过去两周每个例程的完整跑通率**;低于七成,不是你不行,是流程超编——砍步骤,砍到「最烂的日子也跑得完」的长度(晨间保底版可能只有 3 步 8 分钟)——**宁要每天都跑的 3 步,不要每周跑一次的 14 步**:因为例程的价值在「无决策的稳定性」,稳定性来自次数不来自步数;状态好的日子想多做?做完保底版随意加,加的部分不进流程(把弹性放在流程外,刚性留在流程内)。**修腐化:月度重编排**。每月一次十分钟,对着数据修订:哪一步经常被跳过(跳过≠偷懒,是这一步和你的真实生活有摩擦——删掉或换位置)、哪个时段的例程整体死了(换季了,时间锚失效了,重锚)——**例程是版本化的软件,不是刻在石头上的戒律**;顺带把弃用的羞耻也修了:一个例程死了,不是「我又坚持不下来」,是 v1.3 该升 v1.4 了。

边界:例程引擎管的是「已决定要做的重复性序列」,它不负责决定什么值得重复,更不触碰情绪、动机与核心症状的底层;对例程的执着若走向僵化(变动一步就全天崩溃),对 ADHD 是新的脆弱性而不是结构——**流程为人服务,人不为流程殉道**;显著功能损害请正式评估。工具的订阅去留,让「保底版例程的两周跑通率」这个数字投票——它比任何应用商店评分都懂你。

## 边界

同构强度 B 级:习惯形成与延迟奖赏的困难有 ADHD 研究方向,工作流编排与触发器/版本迭代是工程实体,「例程=外部自动化流程」的结构对应清晰;修法为实践翻译,无对照研究。声明:Routinery 未被证实为 ADHD 治疗手段,本文不构成产品疗效背书;显著功能损害请专业评估。

## 今天就能试的 3 件事

1. **把最重要的例程砍到保底版**:3–5 步、最烂日子也跑得完的长度——先保次数,再谈内容。
2. **给它换一个物理触发器**:锚到必经事件上(咖啡机/进门/关电脑),配上物理布景——别再指望通知。
3. **日历约下月的重编排**:十分钟,按跳过率修订步骤——例程是软件,该有版本号。

七个精美例程的坟场,埋的不是你的意志力,**是三个没修的工程 bug:触发、超编、腐化**。锚事件、砍步骤、月迭代——编排器管执行,你管编排:这才是人和流程引擎的正确分工。

## 参考来源

**同构强度：B 级** —— 机制类比（ADHD 侧与 LLM/agent 侧均有真实文献，机制可映射）

- [ADHD Apps: We tested 44 Apps and Here're the Best 9 in 2026](https://blog.saner.ai/best-adhd-apps/) — 证据等级：低（GRADE）
- [12 AI Personal Assistants Built for ADHD Brains (2026 Rankings)](https://www.usecarly.com/blog/best-ai-personal-assistant-adhd/) — 证据等级：低（GRADE）
- [LBD同构对：自我调节与元认知 — Inhibitory control and emotion regulation in preschool child ↔ ObjexMT: Objective Extraction and Metacognitive Calibration ](https://doi.org/10.1016/j.cogdev.2007.08.002) — 证据等级：低（GRADE）
- [LBD同构对：自我调节与元认知 — Emotion-related self-regulation and its relation to children ↔ A Reproducibility Study of Metacognitive Retrieval-Augmented](https://doi.org/10.1146/annurev.clinpsy.121208.131208) — 证据等级：低（GRADE）
- [The 12 Best AI Tools for 2026 (That People Actually Use)](https://www.synthesia.io/post/ai-tools) — 证据等级：低（GRADE）
- [The AI Powered SuperApp for Work | Motion](https://www.usemotion.com/) — 证据等级：低（GRADE）

---

*本文是「ADHD × AI」系列的第 217 篇，由 Devin 基于持续维护的双域研究语料（72,739 篇论文 + LLM Wiki）亲自撰写，并持续迭代更新。*
