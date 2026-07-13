---
title: "ADHD 职场人视角：为什么「治好 ADHD 的独自做事缺乏问责、容易放弃」和「让 LLM 不跑飞」其实是同一道工程题？"
subtitle: "高风险 agent 需要 human-in-the-loop 监督——同一套 harness 思路，两边都成立。"
description: "高风险 agent 需要 human-in-the-loop 监督——同一套 harness 思路，两边都成立。"
date: "2025-05-17"
category: "社群与文化"
categoryId: "community"
categoryEn: "Community & Culture"
tags:
  - "ADHD"
  - "AI"
  - "社群与文化"
  - "人群×同构"
  - "社群"
readingTime: 10
slug: "adhd-职场人视角为什么治好-adhd-的独自做事缺乏问责容易放弃和让-llm-不跑飞其实是同一道工程题"
topicId: "prob-f4e6532bfc"
angle: "人群×同构"
rank: 79
score: 7.81
sourceCount: 6
toolsCited:
  - "Goblin Tools"
  - "Motion"
  - "Saner.AI"
thesis: "ADHD 大脑与 LLM/agent 都是「高产但缺少执行调度层」的生成核心，解决它们失控问题的关键不是改造核心，而是搭建一个轻量、外部、人在回路的 harness（脚手架），让问责与再锚定成为系统的一部分。"
problem: "ADHD 职场人视角：为什么「治好 ADHD 的独自做事缺乏问责、容易放弃」和「让 LLM 不跑飞」其实是同一道工程题？"
spine: "人在回路与身体在场"
spineKind: "llm"
isEvolved: false
llmGenerated: false
isoStrength: "B"
caseStudies:
  - "张一鸣"
  - "于东来"
  - "江静"
---

# ADHD 职场人视角：为什么「治好 ADHD 的独自做事缺乏问责、容易放弃」和「让 LLM 不跑飞」其实是同一道工程题？

> 有人盯着就能做完,没人盯着就散架——这不是软弱,是一种架构特征:你的执行回路需要外部监督信号才能闭合。agent 工程师对此毫不意外:无监督的长任务 agent,放弃和跑偏本来就是默认结局,所以他们从不裸跑。

先把现象说透。很多 ADHD 职场人有一个羞于承认的规律:开会时被分配的任务能推进,自己立项的事永远烂尾;在办公室能干活,居家办公一地鸡毛;截止日前夜效率惊人,漫长的中间地带寸步不动。共同变量只有一个:**有没有一双真实的眼睛(或一个真实的节点)在等你的产出**。没有监督信号时,任务的优先级在你的注意系统里会持续衰减,直到被任何一个更新鲜的刺激覆盖——放弃甚至不是一个决定,是一次无声的滑走。

LLM 侧的对应现象有直接工程对照:agent 跑长任务,若没有中间检查点和外部验证,目标漂移与静默失败是常态而非例外。行业解法不是「选更自觉的模型」,而是**架构化监督**:milestone 校验、进度上报、human-in-the-loop 节点、超时告警。要点:监督不是对模型的不信任侮辱,是长任务可靠性的标准配件。

把这个视角搬回职场,两件事立刻改变。

## 第一件:把「需要问责」去羞耻化

职场文化里,「需要人盯」约等于「不成熟」。但架构视角下,**问责是一种执行基础设施,和显示器、日历同级**——有人天生内置(神经典型者的自我问责回路较强),有人需要外接。外接不丢人,裸奔失败才浪费。这次归因搬家很重要,因为羞耻感恰恰是 ADHD 者不去主动搭建问责结构的原因:承认需要,才能开始设计。

## 第二件:像工程师一样设计你的监督信号

**给独立任务人造「等待方」**。凡是没人等的任务,想办法造一个等的人:主动对同事说「周三我把初稿发你看一眼」;和另一个同事结成互报对子(每天下班前互发三行:今天做了什么/明天做什么);用 body doubling(同事共处一室各干各的、或线上自习室)。机制说明:**对人承诺激活的是社会脑回路,它在 ADHD 中通常完好,甚至过敏(参见拒绝敏感)——用完好的回路,驱动损坏的回路,这是最经典的 harness 设计。**

**把长任务切出「上报节点」**。agent 的 milestone 校验翻译过来:两周的任务,别只有终点 deadline(那意味着前十二天没有任何监督信号),切成三四个中间产出,每个都有接收人和日期——哪怕接收人只是「发到自己的存档邮箱并抄送搭档」。中间节点的功能不是管理进度,是**给每一段路装上「有人在等」的信号灯**。

**给「放弃」装告警**。ADHD 的放弃是静默的:没有宣布,只是不再碰它。对策是显式化:一张「在途任务看板」,每周固定时刻扫一遍,任何一项超过 N 天无动作就触发黄灯——黄灯的处理不是自责,是三选一:重启(约一个 body doubling 时段)/降级(缩小范围)/正式关闭(写一行原因,光荣下架)。**静默失败之所以贵,是因为它从不结账;看板的作用就是强制结账。**

**远程办公的特别补丁**。居家 = 监督信号全灭的极端环境。最低配置:每天一次与真人的同步点(哪怕十五分钟站会)、上午一段线上自习室、以及把「今天的产出」在下班时发给某个人的仪式。远程自由度是留给内置问责回路的人的;外接型选手请自带信号源。

## 边界

同构强度 B 级:agent 长任务的监督架构是真实工程实践,ADHD 的外部问责有效性有行为干预方向的证据支撑(如身体在场与承诺机制的临床应用),具体协议无对照研究。注意:如果「没人盯就瘫痪」的程度已经蔓延到生活全域(吃饭、就医、账单),且伴随情绪低落,请专业评估——那可能不只是问责结构缺失。

## 今天就能试的 3 件事

1. **给手头最重要的独立任务造一个等待方**:今天就发那句「周 X 我发你初稿」。发出去,结构就生效了。
2. **找一个互报搭档**:同事或朋友,每天下班前三行互报。成本两分钟,是性价比最高的监督信号。
3. **建你的在途看板**:所有开了头的事列上去,标注最后动作日期。给超过七天的那几项,今天做三选一。

自觉是稀缺品,但问责结构是可制造品——agent 工程师从不等模型长出自觉,他们直接把监督焊进架构。你也不必等那个「更自律的自己」:造一双等你的眼睛,今天就能开工。

## 参考来源

**同构强度：B 级** —— 机制类比（ADHD 侧与 LLM/agent 侧均有真实文献，机制可映射）

- [ADHD Apps: We tested 44 Apps and Here're the Best 9 in 2026](https://blog.saner.ai/best-adhd-apps/) — 证据等级：低（GRADE）
- [12 AI Personal Assistants Built for ADHD Brains (2026 Rankings)](https://www.usecarly.com/blog/best-ai-personal-assistant-adhd/) — 证据等级：低（GRADE）
- [LBD同构对：自我调节与元认知 — Inhibitory control and emotion regulation in preschool child ↔ ObjexMT: Objective Extraction and Metacognitive Calibration ](https://doi.org/10.1016/j.cogdev.2007.08.002) — 证据等级：低（GRADE）
- [LBD同构对：自我调节与元认知 — Emotion-related self-regulation and its relation to children ↔ A Reproducibility Study of Metacognitive Retrieval-Augmented](https://doi.org/10.1146/annurev.clinpsy.121208.131208) — 证据等级：低（GRADE）
- [The 12 Best AI Tools for 2026 (That People Actually Use)](https://www.synthesia.io/post/ai-tools) — 证据等级：低（GRADE）
- [The AI Powered SuperApp for Work | Motion](https://www.usemotion.com/) — 证据等级：低（GRADE）

---

*本文是「ADHD × AI」系列的第 9 篇，由 Devin 基于持续维护的双域研究语料（72,739 篇论文 + LLM Wiki）亲自撰写，并持续迭代更新。*
