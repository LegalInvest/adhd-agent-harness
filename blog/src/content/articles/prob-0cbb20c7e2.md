---
title: "如果ADHD大脑是缺调度层的LLM，那么我能否设计一个类似ReAct或Plan-and-Execute的外部编排系统，为ADHD用户提供实时任务分解与提醒？这比现有ADHD管理工具有何优势？"
subtitle: "构建外部调度层辅助ADHD执行功能"
description: "构建外部调度层辅助ADHD执行功能"
date: "2025-04-07"
category: "科学研究"
categoryId: "science"
categoryEn: "Scientific Research"
tags:
  - "ADHD"
  - "AI"
  - "科学研究"
  - "STORM视角轮"
  - "脑科学"
readingTime: 14
slug: "如果adhd大脑是缺调度层的llm那么我能否设计一个类似react或plan-and"
topicId: "prob-0cbb20c7e2"
angle: "STORM视角轮"
rank: 168
score: 7.55
sourceCount: 4
toolsCited:
  - "Goblin Tools"
  - "Saner.AI"
  - "Motion"
  - "Tiimo"
problem: "如果ADHD大脑是缺调度层的LLM，那么我能否设计一个类似ReAct或Plan-and-Execute的外部编排系统，为ADHD用户提供实时任务分解与提醒？这比现有ADHD管理工具有何优势？"
spine: "ADHD 大脑与 LLM 的同构"
spineKind: "bridge"
isEvolved: false
llmGenerated: false
---

# 如果ADHD大脑是缺调度层的LLM，那么我能否设计一个类似ReAct或Plan-and-Execute的外部编排系统，为ADHD用户提供实时的任务规划与自我监控？

> 作为一个会写代码的 ADHD 患者,他做过最讽刺的事,是在自己人生一团乱麻的那个月,给公司交付了一套漂亮的 agent 编排系统:规划器拆任务、执行器带工具、反思器盯偏差、状态机管一切。上线那晚他盯着架构图突然愣住:这套东西的每一个组件,都是他自己没有的。那个念头自然得可怕——**既然我能给模型写编排层,为什么不能给自己写一个?**

收敛:这是本站最工程化的一个问题,值得给出工程化的答案。本文只回答——**把 ReAct / Plan-and-Execute 模式移植成「人的编排系统」,哪些组件能直接搬,哪些必须改造,最小可行版本长什么样?**

## 穿透:逐组件移植评估

把两种经典模式拆开对照。**Plan-and-Execute**:规划器先生成全计划,执行器逐步跑,失败再重规划——移植到人身上的陷阱前面的文章讲过(全景任务树会变成拖延道具),但它的核心洞见能搬:**规划和执行由不同组件负责**,人版的翻译是「规划时段与执行时段分离」:早上 10 分钟只做规划(AI 辅助拆解今天的 3 项),白天只执行,不许在执行中途重开规划(那是 ADHD 最爱的逃生门)。

**ReAct** 的循环是 Thought→Action→Observation:每步行动前显式写一行推理,行动后显式记录观察。移植价值极高,因为它恰好补上 ADHD 的两个断点:行动前的「我现在要做什么、为什么」(对抗自动驾驶式漂移)和行动后的「刚才发生了什么」(对抗做完即忘)。人版实现可以低技术到一张纸:干活前写一行「现在:__,因为__」,干完写一行结果。**这个仪式的本质是把内隐的执行流显式化——LLM 需要它,是因为不写出来就没有推理;ADHD 需要它,是因为不写出来就没有监控。**

必须改造的部分,三处:①**监控频率**——agent 每步都反思,人会被反思仪式压垮,人版要稀疏化(只在启动、切换、卡住三个时机触发);②**奖励接口**——agent 不需要动机,人需要:每个 Observation 后追加一个微小的完成确认(划掉、打勾、对人汇报),给多巴胺系统发工资;③**强制力**——代码里的循环自动执行,人的循环会被跳过,所以人版必须借外部触发器(闹钟、身边人、body doubling)来驱动循环,而不是靠记得。

风险直说:自建系统本身是高刺激项目,「搭系统」可能变成最高级的拖延——判据是系统上线速度:两周还没跑起来的自我编排系统,已经变成玩具了。

## 验证

最小可行版本(MVP)一周可验证:一张纸或一个便签软件,三条规则——①早上 10 分钟规划,产出今天 3 项(AI 可辅助);②每项启动时写一行 Thought,结束写一行 Observation;③下午设一个闹钟触发「中途反思」:我还在计划上吗?一周后数据说话:实际完成项数 vs 前一周基线。可证伪:若完成数无变化但你感到负担加重,说明监控开销超过了收益,砍掉一半仪式再试;若你三天就忘了整个系统,问题在触发器缺失,先修外部提醒,再谈编排。

## 决策

做什么:从纸质 MVP 起步,存活两周后再考虑升级为 AI 实时版(让 ChatGPT 当规划器+反思器,你只当执行器);升级时保留「人有最终启动权」——编排系统提议,你签发。

不做什么:不要一上来就写代码搭完整系统(先用纸验证协议本身);不要给系统加超过三条规则——ADHD 系统的死因排行第一永远是维护成本。

先做什么:明早的 10 分钟规划,今晚先把纸和笔放在早餐位上——给第一个循环装好触发器。

## 边界

「ReAct/Plan-and-Execute↔自我编排」是计算层的架构类比(本文未做正式 A/B/C 分级);外部结构化支持对 ADHD 有行为干预层面的证据,但本文的 MVP 协议是实践设计而非验证过的干预。自建系统不替代诊断与治疗;若执行困难严重损害生活,请与专业人员讨论完整的治疗方案。

## 今天就能试的 3 件事

1. 今晚把纸笔放在早餐位——明早 10 分钟,写下今天的 3 项。
2. 给下午 3 点设一个循环闹钟,标签就叫「我还在计划上吗?」
3. 今天完成任何一项后,写你的第一行 Observation:「做了__,结果__」——系统从这一行开始存在。

本文服务于人生 Harness 金字塔的**执行层**:你给模型写过的每一个组件,都是你欠自己的那一个——从一张纸开始,把它还上。

## 参考来源

- [Brain Connectivity Breakthrough Sheds New Light on ADHD](https://neurosciencenews.com/brain-connectivity-adhd-25751/) — 证据等级：中（GRADE）
- [Landmark finding that showed brains of kids with ADHD mature later ...](https://www.livescience.com/health/neuroscience/landmark-finding-that-showed-brains-of-kids-with-adhd-mature-later-was-actually-a-mirage-in-the-data-new-research-finds) — 证据等级：中（GRADE）
- [Can You See ADHD on a Brain Scan? What Brain Imaging Reveals](https://int.livhospital.com/can-you-see-adhd-on-a-brain-scan-what-brain-imaging-reveals/) — 证据等级：低（GRADE）
- [Frontiers | Can biomarkers be used to diagnose attention deficit...](https://www.frontiersin.org/journals/psychiatry/articles/10.3389/fpsyt.2023.1026616/full) — 证据等级：低（GRADE）

---

*本文是「ADHD × AI」系列的第 39 篇，由 Devin 基于持续维护的双域研究语料（72,739 篇论文 + LLM Wiki）亲自撰写，并持续迭代更新。*
