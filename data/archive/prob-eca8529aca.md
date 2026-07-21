---
title: "ADHD 程序员视角：为什么「治好 ADHD 的独自做事缺乏问责、容易放弃」和「让 LLM 不跑飞」其实是同一道工程题？"
subtitle: "高风险 agent 需要 human-in-the-loop 监督——同一套 harness 思路，两边都成立。"
description: "高风险 agent 需要 human-in-the-loop 监督——同一套 harness 思路，两边都成立。"
date: "2025-04-22"
category: "社群与文化"
categoryId: "community"
categoryEn: "Community & Culture"
tags:
  - "ADHD"
  - "AI"
  - "社群与文化"
  - "人群×同构"
  - "社群"
readingTime: 9
slug: "adhd-程序员视角为什么治好-adhd-的独自做事缺乏问责容易放弃和让-llm-不跑飞其实是同一道工程题"
topicId: "prob-eca8529aca"
angle: "人群×同构"
rank: 344
score: 7.63
sourceCount: 6
toolsCited:
  - "ChatGPT"
  - "Goblin Tools"
  - "Motion"
  - "Reclaim.ai"
  - "Tiimo"
  - "Saner.AI"
  - "Focusmate"
thesis: "ADHD 大脑与高风险 LLM/agent 都是「高产但缺乏执行调度层」的生成核心，治愈前者与控制后者其实共用同一套工程思路：在外部建立一个持续 re-grounding、问责在环（human-in-the-loop/body presence）的 harness，让生成能力有方向、有边界、有回滚。"
problem: "ADHD 程序员视角：为什么「治好 ADHD 的独自做事缺乏问责、容易放弃」和「让 LLM 不跑飞」其实是同一道工程题？"
spine: "人在回路与身体在场"
spineKind: "llm"
isEvolved: false
llmGenerated: false
isoStrength: "B"
caseStudies:
  - "张一鸣"
  - "彭玉麟"
  - "尹涛"
---

# ADHD 程序员视角：为什么「治好 ADHD 的独自做事缺乏问责、容易放弃」和「让 LLM 不跑飞」其实是同一道工程题？

> ADHD 程序员的职业生涯里藏着一个几乎没人点破的分野:**在团队里你可能是靠谱甚至出色的工程师,而你的个人项目坟场里埋着三十个写了 20% 的 repo**。同一个人、同一双手、同样的技术栈——差别只有一个变量:团队工程自带全套问责基础设施(code review、standup、sprint、CI 红灯、有人等你的接口),个人项目一样都没有。**你在公司不是「更自律」,是运行在一个问责密度极高的运行时里**;side project 的死亡率不反映你的能力,反映的是裸跑。好消息是:那套基础设施你天天在用、门儿清,而且几乎全部可以低成本地移植到个人项目上。

逐件移植。**其一,standup 移植为公开 build**。团队 standup 的本质是「固定频率向具体的人宣告进度」;个人版:build in public——在社交平台/开发者社区开一条项目线程,每天(或每周)发一条真实进展:截图、commit 链接、卡住的问题——**关注者的存在把静默弃坑变成了可见的失踪**;嫌太吵就退一档:找两三个也在做 side project 的朋友建个小群,互发进度,效力相同。**其二,code review 移植为同行互审**。没人 review 的代码,质量滑坡从「反正没人看」开始(自由职业篇讲过这个动机失血);和朋友互为对方项目的 reviewer:每两周互看一次 PR 或架构——**对方的一句具体反馈,同时完成质量校验和「有人在看我的工作」的强化**。**其三,CI 移植为不可协商的红绿灯**。个人项目最容易烂掉的是纪律性工序(测试/lint/构建)——没有流水线拦着,「先跳过测试」三次之后项目就进入不可维护态,而不可维护态是弃坑的头号技术诱因(回坑成本超过兴趣余额,无状态篇的死法);第一天就配好 GitHub Actions:**红灯不合并,对自己也一样**——机器问责的妙处是它免疫你的借口,也免收羞耻税(闹钟不会失望,家长篇讲过)。**其四,sprint 移植为公开的里程碑**。「做一个笔记应用」是无限期的雾;切成两周一个的 milestone 并公开(发在项目 README 或群里):「v0.1:能存能搜,2 月 15 日」——**日期一旦公开,它就从愿望变成了承诺**(承诺机制),而两周的粒度恰好卡在 ADHD 兴趣半衰期之内。

还有一个程序员特有的反模式要专门拆:**用「重构/换框架」体面地弃坑**。个人项目推进到无聊的中段(CRUD、边界处理、文档),突然觉得「架构不行,得用 Rust 重写」——**这不是技术判断,是新鲜感耗尽后的合法化逃跑**(研究生篇的「我在读文献」,程序员版):重写让你回到项目最快乐的 0→1 阶段,同时杀死已有的 60%。防御规则:**重写决策也要过人在回路**——发给你的 reviewer 朋友:「我想用 X 重写,理由是 Y」——对方只需要问一句「现在的架构具体挡住了哪个 feature?」——答不上来,就回去写 CRUD。这正是验证循环篇的原理:生成核心(你的兴奋)不能自证决策,外部采样才有校验力。

边界:build in public 对部分人有社交焦虑成本,小群互报是完全等效的低配版,别让「公开」的门槛挡住「问责」的落地;个人项目的意义不全在完成——**纯玩具、纯学习的 repo 弃了就弃了,豁免区合法**(Todoist 篇);需要装问责的,只是那些你真心想让它活到 v1.0 的项目——先分清哪个是哪个,再决定给谁装回路。

## 边界

同构强度 B 级:同伴问责与承诺机制有行为研究方向,standup/review/CI 是软件工程实体,「团队运行时 vs 裸跑」的结构对应完整;移植方案为实践翻译,无对照研究。声明:side project 的完成与否不定义工程师价值;长期动力问题请关注整体状态。

## 今天就能试的 3 件事

1. **给最想活下来的 side project 建一条进度线程**:群里或社区,今天发第一条(现状+下一个里程碑+日期)。
2. **第一天配 CI**:哪怕项目只有一个文件——红灯不合并的规矩,从 commit #1 立起来。
3. **立重写审查制**:下次「想换框架重写」的冲动,先发给一个朋友,让他问你那个问题——「现在的架构具体挡住了什么?」

公司里的你和 side project 里的你,是同一个工程师,**跑在两个问责密度天差地别的运行时上**。standup、review、CI、sprint——那套你熟到骨子里的基础设施,搬三件回家,坟场就能少埋几个 repo。

## 参考来源

**同构强度：B 级** —— 机制类比（ADHD 侧与 LLM/agent 侧均有真实文献，机制可映射）

- [ADHD Apps: We tested 44 Apps and Here're the Best 9 in 2026](https://blog.saner.ai/best-adhd-apps/) — 证据等级：低（GRADE）
- [12 AI Personal Assistants Built for ADHD Brains (2026 Rankings)](https://www.usecarly.com/blog/best-ai-personal-assistant-adhd/) — 证据等级：低（GRADE）
- [LBD同构对：自我调节与元认知 — Inhibitory control and emotion regulation in preschool child ↔ ObjexMT: Objective Extraction and Metacognitive Calibration ](https://doi.org/10.1016/j.cogdev.2007.08.002) — 证据等级：低（GRADE）
- [LBD同构对：自我调节与元认知 — Emotion-related self-regulation and its relation to children ↔ A Reproducibility Study of Metacognitive Retrieval-Augmented](https://doi.org/10.1146/annurev.clinpsy.121208.131208) — 证据等级：低（GRADE）
- [The 12 Best AI Tools for 2026 (That People Actually Use)](https://www.synthesia.io/post/ai-tools) — 证据等级：低（GRADE）
- [The AI Powered SuperApp for Work | Motion](https://www.usemotion.com/) — 证据等级：低（GRADE）

---

*本文是「ADHD × AI」系列的第 190 篇，由 Devin 基于持续维护的双域研究语料（72,739 篇论文 + LLM Wiki）亲自撰写，并持续迭代更新。*
