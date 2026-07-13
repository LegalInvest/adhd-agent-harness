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
llmGenerated: true
isoStrength: "B"
caseStudies:
  - "张一鸣"
  - "彭玉麟"
  - "尹涛"
---
# ADHD 程序员视角：为什么「治好 ADHD 的独自做事缺乏问责、容易放弃」和「让 LLM 不跑飞」其实是同一道工程题？

> 高风险 agent 需要 human-in-the-loop 监督——同一套 harness 思路，两边都成立。

你坐在桌前，屏幕上是明明不难的任务，却像被一层透明胶裹住。手指悬在键盘上，大脑在十几个念头之间跳转，时间一到，又放弃了。同一个下午，你写的 agent 在 sandbox 里越跑越远：它生成、调用、再生成，目标明明还在 README 里，输出却开始编造 API、覆盖文件、甚至向外部服务发送请求。你盯着两个屏幕，感到一种奇怪的同构——人和模型，都在「高产」这件事上失控了。

这不是意志力问题，也不是单纯的对齐问题。它是一种更底层的工程故障：生成核心很猛，但执行调度层太薄。

## 01 同一类故障：高产核心缺执行调度层

ADHD 侧的痛点是教科书级的。多巴胺系统失衡让行动动机难以点燃，工作记忆容量有限使任务步骤无法在脑中清晰展开，时间盲让「再做五分钟」变成三小时，拒绝敏感性焦虑（RSD）又在启动前加上一层情绪过滤（来源：任务启动）。而超聚焦一旦启动，可能让人在错误的事情上沉没数小时却浑然不觉（来源：超聚焦）。

但一个耐人寻味的现象是：越来越多 ADHD 成年人自发把 ChatGPT 当成「执行功能外挂」，用来补任务启动、组织、表达的缺口（来源："A little bit of a life raft" – Exploring the Use and Experiences of ChatGPT as a Support Tool among Adults with ADHD）。这暗示了一个关键架构：ADHD 大脑需要一个外部的执行功能层，否则内部生成核心就会空转。

LLM/agent 的侧写几乎一致。LLM 是极强的生成器，但它没有持续的目标锚定、没有稳定的记忆、没有时间感知、没有情绪后果。高风险 agent 一旦进入工具调用循环，就可能出现目标漂移、幻觉累积、行动不可撤销。工程上的标准答案就是 human-in-the-loop：关键节点必须有人类确认、回滚和重新定向。这与 ADHD 侧「身体在场效应」——他人在场或物理环境线索能降低启动阻力——是同一种结构（来源：人在回路与身体在场）。

## 02 同构的解法：外部执行功能层 / Agent Harness

ADHD 的 harness 已经可以用现有 AI 工具拼出来。Goblin Tools 的 Magic ToDo 把模糊任务切成可执行的微步骤，本质是把「任务启动瘫痪」用粒度化解（来源：ADHD Task Managers That Work: Top AI Tools 2025；Harnessing Artificial Intelligence to Live Better with ADHD - CHADD）。Motion 和 Reclaim.ai 自动排程，减少「下一步该做什么」的决策消耗（来源：11 Best ADHD Productivity Apps for Fluctuating Energy - rivva blog；The AI Powered SuperApp for Work | Motion）。Tiimo 把时间可视化，对抗时间盲（来源：任务启动）。Saner.AI 做本地记忆和知识回忆，减少标签切换和搜索循环（来源：ADHD Apps: We tested 44 Apps and Here're the Best 9 in 2026）。这些工具不是替代大脑，而是给大脑加了一层外部调度器。

在 agent 侧，这套结构对应的是：目标重述（re-grounding）、状态机、工具调用前的权限 gate、输出验证器、人类审批点。ADHD 的「身体在场」就是 agent 的 human-in-the-loop；ADHD 的自动排程就是 agent 的 orchestration 层；ADHD 的知识回忆就是 agent 的可检索记忆与长期上下文。两边的本质都是：给生成核心加上一个「不怕它跑，但得让它在跑道上跑」的 harness。

## 03 人物案例：harness 不是性格，是系统

张一鸣的特质高度吻合 ADHD 行为画像：思维极度发散，对新鲜事物有强烈的好奇，不爱社交而沉迷组织和产品系统。他的 harness 不是「更自律」，而是搭建系统：OKR 管理、Context not Control、用数据和文化而非个人意志驱动公司，以及「延迟满足感」（来源：张一鸣 harness）。

把它映射到 agent 工程：OKR 是外部目标调度器；Context not Control 是分布式约束而非微观控制；数据驱动产品则是持续的真实反馈，防止系统凭主观漂移。张一鸣没有「管住」自己的发散，而是给发散装了一个轨道。

彭玉麟的 harness 更古老，但结构同样清晰：性格刚直、冲动、容易杀伐决断，却能带兵十几年。他的方式是「每天画梅花」磨练心性，以严格军纪约束行为，以「不要官、不要钱、不要命」的「三不要」原则给自己设硬边界（来源：彭玉麟 harness）。

对应到 LLM/agent：画梅花是定期的 re-grounding 仪式；严格军纪是 safety policy 与约束规则；「三不要」是 agent 的权限白名单——有些事无论多强的生成冲动，都不允许做。

这两个人说明：harness 不是把生成核心压小，而是让它在边界内释放。

## 04 核心判断：人在回路与身体在场不是「锦上添花」

我的判断是：ADHD 的「独自做事缺乏问责、容易放弃」和 LLM 的「跑飞」是同一道题，因为两边都需要一个外部、可感知、可追责的闭环。AI 工具可以承担一部分调度，但无法完全替代真实的人际问责和身体在场（来源：矛盾与存疑）。Focusmate 等虚拟共作工具尝试用视频身体在场来替代，但效果仍有争议，不能被默认为等价。

同样，agent 工程里的 human-in-the-loop 也不是为了让人类「管每一步」，而是作为最终锚点：当生成核心的内部一致性无法自证时，必须有一个人类状态来终止、确认或重启。少了这一层，再强的 planner 也会变成高级自嗨。

## 05 局限与争议：同构是启发，不是定律

必须诚实指出，这套同构目前更像理论类比，而非已验证的神经科学或计算机科学事实（来源：矛盾与存疑）。ADHD 工具大多缺乏独立临床验证，厂商宣称的「提升效率」不能等同于治疗证据（来源：矛盾与存疑）。而 LLM 与 ADHD 大脑在生物基础、情绪动机、身体经验上差异巨大，不能简单把一方的解法搬到另一方。此外，「超聚焦」本身的定义在学界尚无统一共识（来源：超聚焦），把 AI 注意力机制直接借鉴 ADHD 超聚焦也还为时过早。

更关键的是「脚手架 vs 拐杖」的边界：工具应当降低启动阻力并让人逐渐内化能力，而不是无限替代执行功能。如果 AI 日程安排让你更不会自己安排，那就是拐杖，不是脚手架（来源：矛盾与存疑）。

## 06 今天就能试的四件事

1. **选一件卡住的任务，用 Goblin Tools 的 Magic ToDo 切到第一步**：把「写文档」切成「打开文件、写一句标题、写一个段落」，降低启动阈值（来源：ADHD Task Managers That Work: Top AI Tools 2025）。
2. **给自己加一个真实或视频问责在场**：找一个同伴、Focusmate 或一段共作时间，让身体在场先于意志力启动（来源：身体在场效应；矛盾与存疑）。
3. **如果你是工程师，给高风险 agent 加三个硬 gate**：任何外部 API 调用、文件写入、不可逆操作前，必须显式等待人类确认，并保留回滚状态。
4. **每周做一次「脚手架检查」**：问问自己，这个工具是让我更敢开始，还是让我更不依赖自己？如果是后者，缩小它的使用范围，增加主动步骤。

生成不是问题，没有 harness 的生成才是问题。无论是 ADHD 的大脑还是今天的 LLM，真正要修的都不是「变得更听话」，而是在外部搭一个足够坚固的调度、问责与回滚系统。答案不是治愈生成核心，而是给它的力量装上方向盘和刹车。

## 参考来源

**同构强度：B 级** —— 机制类比（ADHD 侧与 LLM/agent 侧均有真实文献，机制可映射）

- [ADHD Apps: We tested 44 Apps and Here're the Best 9 in 2026](https://blog.saner.ai/best-adhd-apps/) — 证据等级：低（GRADE）
- [12 AI Personal Assistants Built for ADHD Brains (2026 Rankings)](https://www.usecarly.com/blog/best-ai-personal-assistant-adhd/) — 证据等级：低（GRADE）
- [LBD同构对：自我调节与元认知 — Inhibitory control and emotion regulation in preschool child ↔ ObjexMT: Objective Extraction and Metacognitive Calibration ](https://doi.org/10.1016/j.cogdev.2007.08.002) — 证据等级：低（GRADE）
- [LBD同构对：自我调节与元认知 — Emotion-related self-regulation and its relation to children ↔ A Reproducibility Study of Metacognitive Retrieval-Augmented](https://doi.org/10.1146/annurev.clinpsy.121208.131208) — 证据等级：低（GRADE）
- [The 12 Best AI Tools for 2026 (That People Actually Use)](https://www.synthesia.io/post/ai-tools) — 证据等级：低（GRADE）
- [The AI Powered SuperApp for Work | Motion](https://www.usemotion.com/) — 证据等级：低（GRADE）

---

*本文是「ADHD × AI」系列的第 190 篇，由 AI 智能体从持续维护的 LLM Wiki（全网真实情报）中取材整合生成，并持续迭代更新。*
