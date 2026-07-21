---
title: "为什么用 Goblin Tools 治 ADHD 的想理解自己的大脑，和给 agent 套 生成核心 + 缺失的执行层 是一回事？"
subtitle: "Goblin Tools 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
description: "Goblin Tools 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
date: "2025-03-21"
category: "科学研究"
categoryId: "science"
categoryEn: "Scientific Research"
tags:
  - "ADHD"
  - "AI"
  - "科学研究"
  - "反直觉同构"
  - "诊断"
readingTime: 9
slug: "为什么用-goblin-tools-治-adhd-的想理解自己的大脑和给-agent-套-生成核心-缺失的执行层-是一回事"
topicId: "prob-ac8a7da23e"
angle: "反直觉同构"
rank: 250
score: 7.67
sourceCount: 6
toolsCited:
  - "Goblin Tools"
  - "Saner.AI"
  - "Motion"
  - "ReAct"
  - "Chain-of-Thought"
thesis: "ADHD 大脑与 LLM 都是‘高产但缺少内置执行调度层的生成核心’，Goblin Tools 与 agent scaffolding 本质上是同一套外部 harness：把模糊意图拆成可执行步骤、把上下文外置、让下一步行动显而易见。"
problem: "为什么用 Goblin Tools 治 ADHD 的想理解自己的大脑，和给 agent 套 生成核心 + 缺失的执行层 是一回事？"
spine: "ADHD 大脑与 LLM 的同构"
spineKind: ""
isEvolved: true
llmGenerated: false
isoStrength: "B"
caseStudies:
  - "毛泽东"
  - "张瑞敏"
  - "倪刚"
---

# 为什么用 Goblin Tools 治 ADHD 的想理解自己的大脑，和给 agent 套 生成核心 + 缺失的执行层 是一回事？

> 「我想理解我的大脑到底怎么回事」——这个需求听起来该去读神经科学,但对很多 ADHD 者,最深的理解时刻反而发生在一个不起眼的工具里。用 Goblin Tools 的人常报告同一种顿悟:把「收拾房间」输进去,看它拆成八个具体步骤,每一步自己明明都会做——**「原来我不是不会做,我是不会拆」**。这一刻你摸到的,正是理解 ADHD 大脑最有用的那个模型:**生成核心完好甚至过剩,缺的是执行层**——而这恰好也是整个 agent 工程的出发点:LLM 会想不会办,所以给它外接执行层。

先把模型说清,因为它反直觉。直觉模型是「ADHD=脑子不好使」,笼统而伤人;而神经心理证据画出的图景精细得多:ADHD 的生成侧——联想、发散、创意、语言流畅性——常常完好甚至占优;**受损的是执行侧:把意图翻译成有序动作的那一层**(启动、排序、抑制、工作记忆维持)。有研究者用「强记忆、弱控制」概括类似的分离模式,而对 Transformer 的测试发现了同款:生成能力惊人,但冲突抑制和多步执行会系统性崩坏——**「聪明」和「能执行」在两种系统里都是可分离的两层**。Goblin Tools 的顿悟之所以珍贵,是因为它让你**亲手摸到了这条分界线**:AI 补的是拆解(执行层的第一道工序),补上之后你立刻能跑——证明生成核心和动作能力都在,断的只是中间那道翻译工序。

用这个模型重新审视自己,有三个具体收益:

**收益一:自责的靶子换了,而且换对了。** 「我连房间都收拾不了」是对整个人格的判决;「我的任务拆解工序缺失」是对一个组件的诊断——**前者只能羞耻,后者可以采购**(Goblin 就是采购来的拆解组件)。这不是安慰性的语言游戏:靶子换对了,解法空间才会打开——你不会给「人格缺陷」找工具,但会给「组件缺失」找。

**收益二:失败日志变成了诊断数据。** 有了双层模型,每次卡壳都可以问一个诊断问题:**卡在生成层还是执行层?**「不知道该做什么」是生成层(少见);「知道做什么但启动不了」是执行层的启动工序;「做着做着漂走了」是执行层的目标维持工序;「几件事不知道先后」是排序工序。**用 Goblin 当探针**:把卡住的任务扔进去——如果看到拆解结果就能动,断点在拆解;如果拆完还是动不了,断点在启动(那要换启动类工具,如共工或两分钟法)。工程师调试系统就是这么定位故障层的。

**收益三:对「聪明却混乱」这个终生谜题的和解。** 很多 ADHD 者一生被同一句话追着打:「你这么聪明,为什么这点小事做不好?」——双层模型给出了第一个不含道德指控的答案:**因为「聪明」住在生成层,「小事」死在执行层,两层本来就不通信**。这句话值得写下来给身边的人看:它把一个羞耻谜题,变成了一个架构事实。

当然,模型是模型,要防止用过头:大脑不是真的分两层的软件(见边界),而且「执行层外包」不等于「执行层可以永久无人值守」——Goblin 拆解之后,采纳、修改、执行、复盘仍是你的活(human-in-the-loop 那一篇讲过监督位)。**模型的正确用途是导航,不是免责。**

## 边界

同构强度 B 级:ADHD 执行功能与生成/创造能力的分离有神经心理文献支撑,Transformer 生成与执行控制的分离有直接实证(Deficient Executive Control 等),两者的对应是功能层面的同构;但大脑并无字面意义的「两层架构」,「生成核心/执行层」是有用的工程隐喻而非解剖事实。声明:自我理解不替代专业评估——这个模型帮你组织经验,确诊与治疗方案请走临床路径;若「理解自己」的探索长期伴随强烈的哀伤或愤怒(为被误解的岁月),那些情绪值得专业陪伴,不必独自消化。

## 今天就能试的 3 件事

1. **做一次探针实验**:把卡了最久的任务扔进 Goblin——拆完能动,断点在拆解;不能动,断点在启动。
2. **建一页「断点日志」**:本周每次卡壳,记一个词:拆解/启动/维持/排序——一周后看你的高频断层。
3. **把那句话写下来**:「聪明住在生成层,小事死在执行层」——下次被问「你这么聪明为什么」,你有答案了。

理解大脑不必从教科书开始——**从一个工具补上缺口的瞬间开始:缺口在哪,架构就在哪**。你不是坏掉的整体,你是一台生成核心过剩、等着配执行层的机器,而执行层,是可以搭的。

## 参考来源

**同构强度：B 级** —— 机制类比（ADHD 侧与 LLM/agent 侧均有真实文献，机制可映射）

- [ADHD Apps: We tested 44 Apps and Here're the Best 9 in 2026](https://blog.saner.ai/best-adhd-apps/) — 证据等级：低（GRADE）
- [12 AI Personal Assistants Built for ADHD Brains (2026 Rankings)](https://www.usecarly.com/blog/best-ai-personal-assistant-adhd/) — 证据等级：低（GRADE）
- [LBD同构对：自我调节与元认知 — Inhibitory control and emotion regulation in preschool child ↔ ObjexMT: Objective Extraction and Metacognitive Calibration ](https://doi.org/10.1016/j.cogdev.2007.08.002) — 证据等级：低（GRADE）
- [LBD同构对：自我调节与元认知 — Emotion-related self-regulation and its relation to children ↔ A Reproducibility Study of Metacognitive Retrieval-Augmented](https://doi.org/10.1146/annurev.clinpsy.121208.131208) — 证据等级：低（GRADE）
- [The 12 Best AI Tools for 2026 (That People Actually Use)](https://www.synthesia.io/post/ai-tools) — 证据等级：低（GRADE）
- [The AI Powered SuperApp for Work | Motion](https://www.usemotion.com/) — 证据等级：低（GRADE）

---

*本文是「ADHD × AI」系列的第 103 篇，由 Devin 基于持续维护的双域研究语料（72,739 篇论文 + LLM Wiki）亲自撰写，并持续迭代更新。*
