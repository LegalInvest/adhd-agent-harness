---
title: "ADHD 程序员视角：为什么「治好 ADHD 的有想法有能力，却卡在执行与落地」和「让 LLM 不跑飞」其实是同一道工程题？"
subtitle: "LLM 智力强但需要外部编排才能完成长任务——同一套 harness 思路，两边都成立。"
description: "LLM 智力强但需要外部编排才能完成长任务——同一套 harness 思路，两边都成立。"
date: "2025-05-08"
category: "职场发展"
categoryId: "career"
categoryEn: "Career Development"
tags:
  - "ADHD"
  - "AI"
  - "职场发展"
  - "人群×同构"
  - "远程工作"
readingTime: 11
slug: "adhd-程序员视角为什么治好-adhd-的有想法有能力却卡在执行与落地和让-llm-不跑飞其实是同一道工程题"
topicId: "prob-ac7473ecc7"
angle: "人群×同构"
rank: 353
score: 7.63
sourceCount: 6
toolsCited:
  - "Goblin Tools"
  - "Motion"
  - "Saner.AI"
thesis: "ADHD 大脑与 LLM 都是「生成核心强、调度层弱」的系统：有想法有能力却卡在执行落地，与 LLM 智力强但长任务跑飞，本质上是同一道工程题——给高产却缺稳定执行调度的生成核心，装配可拆可调的外部 harness（脚手架）。"
problem: "ADHD 程序员视角：为什么「治好 ADHD 的有想法有能力，却卡在执行与落地」和「让 LLM 不跑飞」其实是同一道工程题？"
spine: "生成核心与调度层"
spineKind: "bridge"
isEvolved: false
llmGenerated: false
isoStrength: "B"
caseStudies:
  - "屠呦呦"
  - "胡林翼"
  - "Tommy Walter"
---

# ADHD 程序员视角：为什么「治好 ADHD 的有想法有能力，却卡在执行与落地」和「让 LLM 不跑飞」其实是同一道工程题？

> ADHD 程序员的「有想法有能力却卡在落地」,有一个行业专属的高清版本:**你能在会议上十分钟设计出让架构师点头的方案,却让一个五行的 PR 挂在「待自测」状态两星期**。技术能力毋庸置疑(难 bug 常常是你修的),但工程产出的完整闭环——设计、实现、测试、文档、上线、收尾——你的贡献分布严重左偏:**闭环的前 30%(有趣的设计与攻坚)你是团队最强,后 70%(枯燥的收尾)你是团队瓶颈**。这条曲线的架构解释,本系列的读者已经会抢答了:生成核心负责前 30%,调度层负责后 70%——**而「后 70% 的枯燥工程」恰恰是软件业招人时说的「工程素养」:它考的从来不是聪明,是调度**。

程序员场景的好消息是双重的:你的行业不但有最完备的外置调度工具链(前一篇问责版讲过 CI/review/standup 的移植),还发明了一个专门对付「想法→落地」缺口的武器,值得单独展开:**把「完成的定义」(Definition of Done)代码化**。ADHD 的「做完了」有弹性:「功能写完了」(没测)、「基本能跑」(没处理边界)、「回头补文档」(永不)——弹性的完成定义,让后 70% 有了无限的豁免空间;工程的对策是把 DoD 从主观判断变成机器判据:**测试覆盖的门禁、lint 的强制、PR 模板里的 checklist(文档?回滚方案?监控?)——「完成」由流水线裁决,不由你今天的感觉裁决**;给自己的个人项目也装同一套(问责篇讲过),你会发现一个反直觉的解放:**当「什么算完」不再需要你决定,收尾阶段最大的启动闸(每一步都要自我谈判)直接消失了**——机器裁决不但更严,而且更省意志力。

另外三个程序员专属的落地组件。**①「设计文档先行」是你的想法海关**。兴奋的新方案直接开写代码,是 ADHD 程序员想法过剩的典型泄洪口(三天后热情耗尽,留下一个半成品分支);规矩:任何超过一天的工作,先写一页设计(问题/方案/不做什么)——**写不满一页的兴奋,说明它还是情绪不是方案**(三重门的工程版);写完发给一个同事看——外部采样,防的是超专注状态下的隧道视野。**②拆 PR 是拆任务的物理执行**。大 PR 是 ADHD 程序员的沼泽:改动越攒越大、越大越不敢提交、越不敢提交越攒——最后「重写吧」(体面弃坑);纪律:**PR 以「一次 review 能看完」为上限**——小 PR 不只是团队礼仪,它是把「落地」切成叶子任务的物理机制:每个小 PR 都是一次真实的完成、一次 CI 的校验、一次「进度存档」(未提交的分支=未序列化的状态,程序员篇的落盘原则)。**③给「收尾债」设固定偿还时段**。文档、测试补齐、TODO 清理——这些永远排不进兴趣队列的债,不要指望「有空就补」(那个时段不存在);每周固定一个低状态时段(状态篇的任务匹配:收尾恰好是低状态友好任务)设为「还债时间」,列表化逐条清——**债务有了固定的还款日,才不会复利成「这模块没法维护了」**。

最后一个身份层面的和解:行业文化崇拜「10x 工程师」,而你可能真的在某些时刻是 10x(超专注攻坚时)——但**长期看,团队信任的是「1x 但每天都是 1x」的交付曲线**;这不是要你放弃爆发力,是要你认清:**爆发力是天赋,交付曲线是架构**——DoD、小 PR、还债时段,这些不是把你变平庸的枷锁,是让你的 10x 时刻真正落进主干分支的管道。

## 边界

同构强度 B 级:执行功能与任务完成的分离有研究基础,DoD/CI/小 PR 是软件工程实体,「前 30% 与后 70%」的结构对应清晰;个人策略为实践翻译,无对照研究。声明:职业倦怠与长期自我评价问题请关注心理健康;团队流程的调整请结合具体工程文化。

## 今天就能试的 3 件事

1. **给个人项目装 DoD**:写一个 PR checklist(测试/文档/回滚),让「什么算完」从此机器说了算。
2. **量一下你的 PR**:最近五个 PR 的大小——超过「一次 review 看得完」的,下次拆。
3. **设本周的还债时段**:挑一个低状态时段,清三条 TODO 或补一页文档——给收尾债一个固定还款日。

会议室里十分钟的天才方案,和挂了两周的五行 PR,**是同一颗大脑的两个组件在各自为政**。前 30% 的光芒不需要你操心,把后 70% 交给 DoD、小 PR 和还款日——落地,从来就该是管道的事。

## 参考来源

**同构强度：B 级** —— 机制类比（ADHD 侧与 LLM/agent 侧均有真实文献，机制可映射）

- [ADHD Apps: We tested 44 Apps and Here're the Best 9 in 2026](https://blog.saner.ai/best-adhd-apps/) — 证据等级：低（GRADE）
- [12 AI Personal Assistants Built for ADHD Brains (2026 Rankings)](https://www.usecarly.com/blog/best-ai-personal-assistant-adhd/) — 证据等级：低（GRADE）
- [LBD同构对：自我调节与元认知 — Inhibitory control and emotion regulation in preschool child ↔ ObjexMT: Objective Extraction and Metacognitive Calibration ](https://doi.org/10.1016/j.cogdev.2007.08.002) — 证据等级：低（GRADE）
- [LBD同构对：自我调节与元认知 — Emotion-related self-regulation and its relation to children ↔ A Reproducibility Study of Metacognitive Retrieval-Augmented](https://doi.org/10.1146/annurev.clinpsy.121208.131208) — 证据等级：低（GRADE）
- [The 12 Best AI Tools for 2026 (That People Actually Use)](https://www.synthesia.io/post/ai-tools) — 证据等级：低（GRADE）
- [The AI Powered SuperApp for Work | Motion](https://www.usemotion.com/) — 证据等级：低（GRADE）

---

*本文是「ADHD × AI」系列的第 195 篇，由 Devin 基于持续维护的双域研究语料（72,739 篇论文 + LLM Wiki）亲自撰写，并持续迭代更新。*
