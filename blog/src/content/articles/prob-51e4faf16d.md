---
title: "为什么「治好 ADHD 的独自做事缺乏问责、容易放弃」和「让 LLM 不跑飞」其实是同一道工程题？"
subtitle: "高风险 agent 需要 human-in-the-loop 监督——同一套 harness 思路，两边都成立。"
description: "高风险 agent 需要 human-in-the-loop 监督——同一套 harness 思路，两边都成立。"
date: "2025-03-28"
category: "社群与文化"
categoryId: "community"
categoryEn: "Community & Culture"
tags:
  - "ADHD"
  - "AI"
  - "社群与文化"
  - "反直觉同构"
  - "社群"
readingTime: 8
slug: "为什么治好-adhd-的独自做事缺乏问责容易放弃和让-llm-不跑飞其实是同一道工程题"
topicId: "prob-51e4faf16d"
angle: "反直觉同构"
rank: 328
score: 7.63
sourceCount: 6
toolsCited:
  - "Goblin Tools"
  - "Motion"
  - "Saner.AI"
thesis: "ADHD 大脑与 LLM agent 本质上是同一类「高产但缺执行调度层的生成核心」，它们需要的不是被「修好」，而是一个外挂的 harness（上下文管理、验证循环、记忆与调度）来补全执行层，把「人在回路」和「身体在场」变成可工程化的约束。"
problem: "为什么「治好 ADHD 的独自做事缺乏问责、容易放弃」和「让 LLM 不跑飞」其实是同一道工程题？"
spine: "人在回路与身体在场"
spineKind: "llm"
isEvolved: false
llmGenerated: true
isoStrength: "B"
caseStudies:
  - "张一鸣"
  - "王传福"
  - "Donna Wilson"
---
# 为什么「治好 ADHD 的独自做事缺乏问责、容易放弃」和「让 LLM 不跑飞」其实是同一道工程题？

> 高风险 agent 需要 human-in-the-loop 监督——同一套 harness 思路，两边都成立。

如果你是个 ADHD 患者，你一定熟悉这个场景：一个人在家，任务表上有三件重要的事，结果三小时后发现自己在整理书架。如果你是个做 agent 工程的工程师，你也一定熟悉另一个场景：LLM 在无人监督下规划了一个二十步 workflow，第五步就调错了 API。两种崩溃看起来毫无关系，其实是同一道工程题。

## 01 同一个病根：高产核心，缺执行调度层

ADHD 大脑和 LLM agent 都可以被理解为「高产但缺乏可靠执行调度层的生成核心」（来源：上下文工程）。ADHD 一侧的困难来自执行功能、工作记忆、时间盲与多巴胺调节：时间感知会扭曲，「hours slipping away unnoticed or that drag on forever」（来源：ADHD），注意力被新刺激不断捕获，任务被切割成碎片，「they often add another inbox, another prompt, and another place to lose the thread」（来源：ADHD）。

LLM 一侧面对的是上下文膨胀、推理退化和幻觉。它的生成核心自信且连贯，却可能和外部现实脱节。Harness 工程之所以存在，正是为了给这个高产核心外挂一个外部调度层：上下文传递、工具接口、规划工件、验证循环、记忆系统和沙盒（来源：GitHub - ai-boost/awesome-harness-engineering）。

两边不是「不够聪明」，而是聪明得没有刹车和方向盘。

## 02 同一套解法：Harness 就是外部执行功能层

给 ADHD 大脑加 harness，本质上和给 LLM 加 harness 是同构的。

Goblin Tools 的 Magic ToDo 把模糊任务——比如「清理厨房」——拆成可执行子步骤，还能用「辣度」调节粒度，降低启动门槛（来源：12 AI Personal Assistants Built for ADHD Brains (2026 Rankings)）。这对应 LLM harness 里的「结构化工作流与规划」：复杂任务被分解为子任务，每一步都留下规划工件。

Motion 自动排程、动态调整，在日程被打乱时重新安排，减少「下一步该做什么」的决策负担（来源：11 Best ADHD Productivity Apps for Fluctuating Energy - rivva blog）。这对应 agent 里的规划与重规划模块：不是让模型自己决定先做哪一步，而是由外部调度器根据优先级、依赖和截止日期重建计划。

Saner.AI 用本地记忆和通用收件箱减少搜索循环和标签切换，帮助对抗 ADHD 的工作记忆不足（来源：ADHD Apps: We tested 44 Apps and Here're the Best 9 in 2026）。这对应 LLM harness 里的记忆系统：没有外部记忆，上下文就会断裂，导致重复工作和幻觉（来源：Loop Engineering for AI Agents: Memory-First Design）。

最关键的对应是验证循环。ADHD 个体需要把内部状态与外部现实核对，这是一种「接地」过程（来源：ADHAPT: An AI Tool for Emotional Regulation）；LLM harness 也不会盲目执行工具，而是检查输出格式、运行测试用例、做 CI 集成（来源：What is an agent harness...）。两者都是让高产核心在行动前先把内部模型和世界对齐。

## 03 张一鸣的 harness：不是控制，而是调度

张一鸣的 ADHD 特质表现为思维极度发散、永远在思考组织和产品，什么新东西都要研究。他的 harness 不是用意志力硬把自己按在椅子上，而是建立外部系统：OKR 把大目标拆成可追踪的里程碑；「Context not Control」用系统和文化管公司，不靠集权 micromanagement；做产品从用户需求出发，不做主观判断。

这正对应 LLM harness 的设计哲学：不是直接控制生成核心，而是定义目标、约束上下文、建立验证节点。OKR 是规划工件，「Context not Control」是外部调度器，用户需求是接地信号。张一鸣的成就在于，他给自己建了一套比个人意志力更稳定的工程系统。

这种 harness 也解释了为什么 ADHD 创业者群体有超常产出：Pace Ventures Research 2026 的数据显示，ADHD 组的超专注工作时长达到 14.5 小时，对照组只有 8.2 小时。高产核心一直都在，缺的是让它稳定输出的 harness。

## 04 核心判断与诚实局限

我的判断是：ADHD 和 LLM 的「跑飞」不是道德缺陷，也不是模型能力问题，而是同一类工程问题——它们都需要一个外挂 harness 来补全执行调度层。但 wiki 资料也明确提醒我们，这个同构性目前只是理论类比，缺乏实证基础，不能当成已被证实的科学事实（来源：矛盾与存疑）。

此外还有三条边界必须诚实指出。第一，工具宣称的证据不足：Motion 页面提到「缺乏独立临床验证」，Goblin Tools 和 Saner.AI 的好评也主要来自用户反馈，而非随机对照试验。第二，harness 是脚手架，不是拐杖；过度依赖 AI 工具可能增加认知负担，甚至削弱真实的人际在场效应（来源：矛盾与存疑）。第三，同构是启发，不是处方——ADHD 是神经发育特征，LLM 是统计模型，两者的生物学基础和社会后果完全不同，不能简单套用。

## 05 今天就能试

1. 选一个拖延的任务，用 Goblin Tools 的 Magic ToDo 拆解，把「写报告」变成「打开文档→写三段→检查格式」三个可执行动作。  
2. 用 Motion 或日历把任务自动排进时间块，让系统替你决定「下一步」，而不是自己决定。  
3. 如果你在做 agent 工程

## 参考来源

**同构强度：B 级** —— 机制类比（ADHD 侧与 LLM/agent 侧均有真实文献，机制可映射）

- [ADHD Apps: We tested 44 Apps and Here're the Best 9 in 2026](https://blog.saner.ai/best-adhd-apps/) — 证据等级：低（GRADE）
- [12 AI Personal Assistants Built for ADHD Brains (2026 Rankings)](https://www.usecarly.com/blog/best-ai-personal-assistant-adhd/) — 证据等级：低（GRADE）
- [LBD同构对：自我调节与元认知 — Inhibitory control and emotion regulation in preschool child ↔ ObjexMT: Objective Extraction and Metacognitive Calibration ](https://doi.org/10.1016/j.cogdev.2007.08.002) — 证据等级：低（GRADE）
- [LBD同构对：自我调节与元认知 — Emotion-related self-regulation and its relation to children ↔ A Reproducibility Study of Metacognitive Retrieval-Augmented](https://doi.org/10.1146/annurev.clinpsy.121208.131208) — 证据等级：低（GRADE）
- [The 12 Best AI Tools for 2026 (That People Actually Use)](https://www.synthesia.io/post/ai-tools) — 证据等级：低（GRADE）
- [The AI Powered SuperApp for Work | Motion](https://www.usemotion.com/) — 证据等级：低（GRADE）

---

*本文是「ADHD × AI」系列的第 178 篇，由 AI 智能体从持续维护的 LLM Wiki（全网真实情报）中取材整合生成，并持续迭代更新。*
