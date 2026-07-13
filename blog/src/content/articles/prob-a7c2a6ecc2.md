---
title: "ADHD 职场人视角：为什么「治好 ADHD 的有想法有能力，却卡在执行与落地」和「让 LLM 不跑飞」其实是同一道工程题？"
subtitle: "LLM 智力强但需要外部编排才能完成长任务——同一套 harness 思路，两边都成立。"
description: "LLM 智力强但需要外部编排才能完成长任务——同一套 harness 思路，两边都成立。"
date: "2025-04-04"
category: "职场发展"
categoryId: "career"
categoryEn: "Career Development"
tags:
  - "ADHD"
  - "AI"
  - "职场发展"
  - "人群×同构"
  - "领导力"
readingTime: 11
slug: "adhd-职场人视角为什么治好-adhd-的有想法有能力却卡在执行与落地和让-llm-不跑飞其实是同一道工程题"
topicId: "prob-a7c2a6ecc2"
angle: "人群×同构"
rank: 81
score: 7.81
sourceCount: 6
toolsCited:
  - "Goblin Tools"
  - "Saner.AI"
  - "Motion"
thesis: "ADHD 大脑与 LLM 是同一类「高产却缺执行调度层」的生成核心，因此两边的解法不是「训练核心自己变强」，而是为它构建可拆可调的外部 harness；职场 ADHD 人群与 Agentic 工程师面对的其实是同一道工程题。"
problem: "ADHD 职场人视角：为什么「治好 ADHD 的有想法有能力，却卡在执行与落地」和「让 LLM 不跑飞」其实是同一道工程题？"
spine: "生成核心与调度层"
spineKind: "bridge"
isEvolved: false
llmGenerated: false
isoStrength: "B"
caseStudies:
  - "屠呦呦"
  - "胡林翼"
  - "Jack Snow"
---

# ADHD 职场人视角：为什么「治好 ADHD 的有想法有能力，却卡在执行与落地」和「让 LLM 不跑飞」其实是同一道工程题？

> 「有想法有能力,就是落不了地」——这句绩效评语的残忍之处在于,它听起来像性格缺陷,实际上描述的是一个精确的架构事实:生成核心在线,调度层缺席。而调度层,恰好是四种组件里最容易外置的一种。

先给这个职场画像存证。会议上你的点子最多、质量还高;方案的框架你半小时能搭出别人两天的水平;同事遇到难题爱找你聊,聊完总有突破。但年底盘点,你的「落地清单」薄得难堪:想法送给了别人执行(他们升了职),自己立项的事卡在 30%,承诺的迭代拖成了传说。**输入端是全组最富的,输出端是全组最穷的**——这种贫富差在绩效体系里没有科目,最后只能记成「不够踏实」。

架构诊断:想法→落地之间隔着一条流水线(拆解成步骤→排进日程→启动第一步→跨天续接→收尾交付),这条流水线的每一站都是执行功能的岗位,而 ADHD 的执行功能全线缺员。LLM 的对应画像有直接研究:生成与推理惊艳,但让裸模型自主完成多步任务,计划维持与执行控制是系统性弱项——**没有人因此说「这模型不踏实」,工程师直接给它配了编排调度层**(planner 拆解、queue 排程、executor 分发、checkpoint 续接)。

职场人版的调度层,逐站配齐:

## 流水线五站,每站一个外置件

**拆解站**:想法出现的当天,趁热让 ChatGPT 拆:「把这个想法拆成第一周就能做的三步,每步两小时内。」注意时机——**拆解必须发生在兴奋期内**,ADHD 的想法热度有半衰期,过了窗口连拆解都懒得做。拆解的产出直接进下一站,不许停留在「回头再说」。

**排程站**:拆出的步骤立刻进日历,占据具体时段(不是 to-do list——清单是愿望,日历才是调度)。给每个想法级项目每周固定预留一块「落地时段」,雷打不动,像对待会议一样。

**启动站**:到点启动是最疼的一环,配双保险:5 分钟合同(只承诺做 5 分钟,启动阻力最小化)+ body doubling(和同事约定同时段各干各的)。

**续接站**:跨天/跨周的断点续接,靠「下一步便签」——每次停工前 60 秒写下「下次从哪句开始」,下次启动时读它,而不是靠重新回忆(重新回忆的成本高到足以劝退整个项目)。

**交付站**:给每个项目造一个等待方(「周五发你初稿」),把终点从「自我满意」改成「有人在等」——ADHD 的收尾涣散,大半是因为终点信号太弱。

## 关键的职场策略:让落地率先在小事上翻身

常见错误是拿最宏大的想法练手(热情最高,流水线负载也最重,失败率最高,失败又加固「我就是落不了地」的自我叙事)。正确顺序反过来:**挑一个两周能见结果的小想法,用全套流水线把它完整送到终点**——这一次完整闭环的价值不在产出本身,在两个副产品:你的自我叙事第一次有了反例;你的流水线各站被实测调通。然后逐级加载更大的想法。工程师不会用最难的任务调试新架构,你也别。

还有一个分配策略:**接受「想法与执行的比例永远失衡」,主动经营它**。你天生的产能就是想法多于执行位,与其让多余的想法烂在心里发酵成焦虑,不如建一个「想法停车场」(一页文档,想法进场即登记,每月挑一个进流水线,其余大方送人或搁置)。把「送出去的想法」记账——年底述职时,「我的提议被 X 个团队落地」同样是硬产出,前提是你说得出来。

## 边界

同构强度 B 级:planner/executor 架构是真实 agent 工程,ADHD 的「意图-执行落差」有执行功能文献支撑,流水线协议属机制映射的实践,无对照研究。注意:如果卡点集中在「启动前的恐惧」而非「启动的惰性」(怕做不完美所以不开始),那一半是完美主义议题,值得单独处理——调度层治不了审美洁癖。

## 今天就能试的 3 件事

1. **建想法停车场**:一页文档,把脑子里所有「回头要做」的想法全部登记。今天先清空缓存。
2. **挑一个两周级小想法,今天走完前两站**:趁热拆解 + 排进日历。只挑小的。
3. **给这个小项目预约一个等待方**:「两周后的周五发你看」——今天就把这句话发出去。

「有想法没执行」从来不是你的完整档案——完整版是:生成核心超配,调度层未安装。前者是天赋,后者是采购清单。按站配齐,让年底的落地清单,第一次配得上你会议上的样子。

## 参考来源

**同构强度：B 级** —— 机制类比（ADHD 侧与 LLM/agent 侧均有真实文献，机制可映射）

- [ADHD Apps: We tested 44 Apps and Here're the Best 9 in 2026](https://blog.saner.ai/best-adhd-apps/) — 证据等级：低（GRADE）
- [12 AI Personal Assistants Built for ADHD Brains (2026 Rankings)](https://www.usecarly.com/blog/best-ai-personal-assistant-adhd/) — 证据等级：低（GRADE）
- [LBD同构对：自我调节与元认知 — Inhibitory control and emotion regulation in preschool child ↔ ObjexMT: Objective Extraction and Metacognitive Calibration ](https://doi.org/10.1016/j.cogdev.2007.08.002) — 证据等级：低（GRADE）
- [LBD同构对：自我调节与元认知 — Emotion-related self-regulation and its relation to children ↔ A Reproducibility Study of Metacognitive Retrieval-Augmented](https://doi.org/10.1146/annurev.clinpsy.121208.131208) — 证据等级：低（GRADE）
- [The 12 Best AI Tools for 2026 (That People Actually Use)](https://www.synthesia.io/post/ai-tools) — 证据等级：低（GRADE）
- [The AI Powered SuperApp for Work | Motion](https://www.usemotion.com/) — 证据等级：低（GRADE）

---

*本文是「ADHD × AI」系列的第 11 篇，由 Devin 基于持续维护的双域研究语料（72,739 篇论文 + LLM Wiki）亲自撰写，并持续迭代更新。*
