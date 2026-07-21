---
title: "为什么用 Inflow 治 ADHD 的注意力涣散，和给 agent 套 上下文工程 是一回事？"
subtitle: "Inflow 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
description: "Inflow 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
date: "2025-04-02"
category: "专注力管理"
categoryId: "focus"
categoryEn: "Focus Management"
tags:
  - "ADHD"
  - "AI"
  - "专注力管理"
  - "反直觉同构"
  - "专注力"
readingTime: 7
slug: "为什么用-inflow-治-adhd-的注意力涣散和给-agent-套-上下文工程-是一回事"
topicId: "prob-3cddf22016"
angle: "反直觉同构"
rank: 278
score: 7.65
sourceCount: 6
toolsCited:
  - "RescueTime"
  - "Focusmate"
  - "Brain.fm"
  - "Endel"
  - "Forest"
thesis: "ADHD 大脑与 LLM/agent 都是高产但缺乏执行调度层的生成核心，因此用外部工具管理 ADHD 的注意力涣散，与给 agent 做上下文工程，本质上是同一套 harness：主动设计「当下注意什么」，把生成优势转化为目标导向行为。"
problem: "为什么用 Inflow 治 ADHD 的注意力涣散，和给 agent 套 上下文工程 是一回事？"
spine: "上下文工程"
spineKind: ""
isEvolved: true
llmGenerated: false
isoStrength: "A"
caseStudies:
  - "曾国藩"
  - "辛弃疾"
  - "Mr. David Ramirez"
---

# 为什么用 Inflow 治 ADHD 的注意力涣散，和给 agent 套 上下文工程 是一回事？

> 这个系列讲到现在,工具都在治理「外部输入」:放什么、何时放、怎么放、谁在场。Inflow 是个异类——它是基于 CBT(认知行为疗法)框架、由临床人员参与开发的 ADHD 自助 app,主体内容是心理教育模块和练习:理解你的注意系统、识别你的思维模式、重写你对涣散的反应方式。它不管理你的任务,不过滤你的通知——**它修改的是另一层上下文:你脑子里那份常驻的、解释一切行为的自我叙事**。而这一层,恰好对应 agent 工程里权力最大的一段文本:**系统提示(system prompt)——不进入任务内容、却居于一切任务之上、改写所有输出倾向的那段常驻上下文**。

先讲 agent 侧这个层次为什么特殊。上下文窗口里的内容不平权:任务内容是流动的,系统提示是常驻的——它定义 agent「是谁」「如何解读输入」「失败时怎么反应」,同样的任务配不同的系统提示,行为可以天差地别;而且**系统提示的错误是全局性的**:任务层的错误影响一次输出,系统提示层的偏差污染所有输出。所以成熟工程对系统提示的审查最严——它是杠杆最长的一段文本。

人类的对应物,CBT 管它叫核心信念与自动思维,通俗说就是自我叙事——而 ADHD 者的这段「系统提示」,通常是几十年负面反馈写成的(反馈信用分配篇讲过:被批评却不知道错在哪一步,最终归因给「我这个人」):**「我就是懒」「我总会搞砸」「别人都能做到」**。看清楚这段叙事怎么放大涣散,是这一篇的核心:走神一次(注意系统的机械事件,本篇系列已拆过五个维度)→ 叙事介入解读:「又来了,我果然不行」→ 羞耻与焦虑升起 → 而羞耻焦虑恰恰是高唤醒的内部干扰源,直接触发下一轮捕获或逃向手机(情绪调节篇的通道) → 叙事获得新证据,更牢。**同一次走神,机械解读损失五分钟,叙事解读损失一下午**——涣散的放大器不在外部输入流里,在解释层里。

Inflow 类 CBT 工具做的,就是系统提示的重写工程,分三步,和工程师改 prompt 的流程神似:**①先让提示可见**——心理教育模块把「你的注意系统是这样工作的」讲清楚(执行功能、奖赏回路、时间盲),等于把隐式系统提示 dump 出来审查:很多用户的第一震撼是「原来这是机制,不是人品」;**②定位偏差语句**——思维记录练习(CBT 的经典技术)抓自动思维:「刚才走神时,你对自己说了什么?」——把「我果然不行」从背景常驻拖到前台检视;**③替换为准确版本**——不是替换成虚假的正能量,是替换成机制准确的描述:「我的注意系统对低刺激任务点火困难,这是特质,对策是加结构」——**好的系统提示不是夸 agent,是准确描述它的能力边界与应对策略**。

证据侧要说清:**CBT 对成人 ADHD 的疗效有多项 RCT 与荟萃分析支持**(对执行功能症状与情绪伴随问题的改善,证据等级在心理干预里相对较好),这是本篇同构 A 级的人类侧支柱;但要区分:**「CBT 有效」证据较强,「CBT app 自助版有效」证据薄得多**——数字化自助去掉了治疗师这个问责与校准环节(而问责恰恰是 ADHD 最缺的),完课率是所有自助 app 的软肋。所以定位要诚实:Inflow 这类工具是心理教育的低门槛入口与治疗的辅助,不是治疗的替代——症状显著者,正路仍是专业评估与系统治疗。

## 边界

同构强度 A 级:CBT 对成人 ADHD 的疗效有 RCT/荟萃分析,系统提示对 LLM 行为的决定性影响有直接工程实证,「常驻解释层」的同构两侧都有实体支撑;但 app 自助形态的独立疗效证据有限,A 判给机制与 CBT 本体,不判给 app 形态。声明:自助工具不替代诊断与治疗;若负面自我叙事伴随持续情绪低落,请优先专业评估。

## 今天就能试的 3 件事

1. **dump 一次你的系统提示**:下次走神后,立刻写下脑内第一句自我评论——那就是你的常驻提示原文。
2. **做一次机制翻译**:把那句话改写成机制描述(「点火困难」而非「我很懒」)——贴在屏幕边。
3. **测一次放大器**:记录本周一次走神的总代价——机械损失几分钟,叙事(羞耻/逃避)损失几分钟?

涣散的第一层是走神,第二层是你对走神说的那句话——**外部输入流治理完了,记得审查那段常驻的系统提示**:它不占屏幕,却改写你所有的输出。

## 参考来源

**同构强度：A 级** —— 直接文献支撑（引用 ADHD↔LLM 同构专题研究）

- [ADHD Apps: We tested 44 Apps and Here're the Best 9 in 2026](https://blog.saner.ai/best-adhd-apps/) — 证据等级：低（GRADE）
- [Meta-Analysis of fMRI Studies of Disruptive Behavior Disorders](https://doi.org/10.1176/appi.ajp.2016.15081089) — 证据等级：高（GRADE）
- [Nonlinear Complexity Analysis of Brain fMRI Signals in Schizophrenia](https://doi.org/10.1371/journal.pone.0095146) — 证据等级：低（GRADE）
- [Revolutionizing ADHD Management with AI Assistants](https://neurolaunch.com/adhd-ai-assistant/) — 证据等级：低（GRADE）
- [The Wanderer's Algorithm: Controlled Distraction as a Catalyst for Machine Creativity](https://www.techrxiv.org/users/950560/articles/1356399/master/file/data/wanderers_algorithm_paper_independent%203/wanderers_algorithm_paper_independent%203.pdf) — 证据等级：低（GRADE）
- [Deficient Executive Control in Transformer Attention](https://www.biorxiv.org/content/10.1101/2025.01.22.634394v1.full.pdf) — 证据等级：低（GRADE）

---

*本文是「ADHD × AI」系列的第 129 篇，由 Devin 基于持续维护的双域研究语料（72,739 篇论文 + LLM Wiki）亲自撰写，并持续迭代更新。*
