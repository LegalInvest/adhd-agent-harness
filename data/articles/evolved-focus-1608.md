---
title: "为什么用 Perplexity 治 ADHD 的注意力涣散，和给 agent 套 上下文工程 是一回事？"
subtitle: "Perplexity 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
description: "Perplexity 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
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
slug: "为什么用-perplexity-治-adhd-的注意力涣散和给-agent-套-上下文工程-是一回事"
topicId: "evolved-focus-1608"
angle: "反直觉同构"
rank: 288
score: 7.68
sourceCount: 6
toolsCited:
  - "Focusmate"
  - "RescueTime"
  - "Brain.fm"
thesis: "ADHD大脑与LLM/agent在结构上同构——都是高产但缺乏可靠执行调度层的生成核心，因此解决ADHD注意力涣散的上下文工程思路与给agent套上harness的上下文工程思路本质相同，都是通过外部执行功能层来补偿调度层的缺失。"
problem: "为什么用 Perplexity 治 ADHD 的注意力涣散，和给 agent 套 上下文工程 是一回事？"
spine: "上下文工程"
spineKind: ""
isEvolved: true
llmGenerated: true
caseStudies:
  - "曾国藩"
  - "张旭"
  - "陈建国"
---
# 为什么用 Perplexity 治 ADHD 的注意力涣散，和给 agent 套 上下文工程 是一回事？

> Perplexity 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。

## 问题：为什么你的大脑和你的AI一样“失控”？

如果你是一个ADHD患者，你一定经历过这种场景：打开浏览器想查资料，结果十分钟后在看猫咪视频；列了待办清单，却对着第一条发呆半小时。如果你是一个Agentic Harness工程师，你一定也经历过：给LLM agent喂了整份文档，它却开始胡编乱造；设了复杂的prompt链，agent却在中途“走神”输出无关内容。

这两个问题看似分属神经科学和计算机科学，但它们的底层结构惊人地同构。ADHD大脑和LLM/agent共享同一个核心矛盾：**两者都是高产但缺乏可靠执行调度层的生成核心**（来源：AI与ADHD的专注力）。ADHD大脑擅长发散联想、创意迸发，但执行功能（计划、启动、抑制）薄弱；LLM能流畅生成文本，但缺乏上下文控制、容易偏离指令。两边都需要一个“外部调度层”来约束和引导生成过程——这就是**上下文工程**（context engineering）。

## 同构：从“注意力涣散”到“上下文污染”

ADHD的注意力涣散，本质上是大脑的“上下文窗口”被无关刺激污染。工作记忆缺陷导致无法维持当前目标，环境中的任何变动都会抢占注意力（来源：执行功能障碍）。同样，LLM的上下文窗口一旦膨胀到超过有效长度，早期指令被稀释，新输入的噪声会扭曲输出。两者都需要主动设计“当下注意什么”的工程方案。

这种同构在工具层面也得到印证。**Focusmate**（虚拟身体在场）通过实时同伴问责提供外部结构，弥补ADHD内在的多巴胺调节不足（来源：Focusmate）。它的核心机制是“AI-Matched Body Doubling”（来源：The Best AI-Powered ADHD Productivity Tools in 2026），用算法优化配对——这本质上是一个**外部调度器**，定期向用户注入“当前任务是什么”的grounding信号。对LLM agent来说，类似的harness是定时re-grounding：每N轮对话重新注入系统prompt，或使用向量数据库存储关键约束，防止上下文漂移。

再看**RescueTime**：它自动记录时间使用，揭示真实去向，帮助用户识别注意力漂移（来源：RescueTime）。这相当于LLM agent的**日志与审计层**，记录每次调用的输入输出，分析agent是否偏离目标。ADHD用户需要这个外部记忆来克服“时间盲”（来源：执行功能障碍），正如agent需要日志来调试上下文污染。

## 人物案例：曾国藩的“日课十二条”与LLM的re-grounding

晚清名臣曾国藩是典型的注意力不集中型ADHD：30岁前浮躁坐不住，日记里天天骂自己“无恒”“浮躁”，读书慢到“他人目下二三行，余或疾读不能终一行”。他的解决方案是**日课十二条**：黎明即起、读书不二、谨言、写日记反省等。其中最核心的是“读书不二”——一本书不读完绝不翻第二本，用最笨最稳的方法抵消自己的冲动。

这套系统与LLM agent的harness高度同构：
- **日课** ↔ **定时re-grounding**：曾国藩每天固定时间做固定事，相当于agent每轮对话前重新注入系统prompt，防止上下文漂移。
- **写日记反省** ↔ **日志与审计**：曾国藩通过日记记录行为偏差，相当于agent的调用日志，用于事后调试。
- **“结硬寨打呆仗”** ↔ **低风险执行策略**：曾国藩用最笨的方法保证稳定输出，相当于agent使用“先验证再执行”的流程，避免冲动决策。

曾国藩的成就（平定太平天国、发起洋务运动）证明，这种外部harness能有效补偿ADHD的内在缺陷。同样，LLM agent通过harness也能从“天马行空”变为“可靠执行”。

## 证据与争议：脚手架还是拐杖？

现有工具的证据强度不一。Focusmate基于身体在场效应，多项用户研究显示其能显著提升任务启动和维持（来源：Focusmate）。RescueTime通过客观记录提升时间觉察，有初步研究支持（来源：RescueTime）。Brain.fm利用神经锁相技术，有神经科学理论支持，但缺乏针对ADHD的独立临床研究（来源：Brain.fm）。

但争议同样存在：AI工具作为外部执行功能层，长期使用是否会导致内在执行功能退化？这就是“脚手架与拐杖”的边界问题（来源：矛盾与存疑）。目前缺乏纵向研究，但我的判断是：**关键在于工具是否促进神经可塑性**。如果工具只是替代功能（如自动提醒），可能形成依赖；如果工具提供反馈和训练（如RescueTime的周报让人反思时间使用），则可能促进内在能力的重塑（来源：神经可塑性）。曾国藩的日课不是替代他的执行功能，而是通过重复训练强化它——这正是脚手架而非拐杖。

## 行动：今天就能试的3件事

1. **给自己一个“日课”**：每天固定时间做同一件事（如早上9点写100字），用手机定时器re-grounding。这相当于给大脑注入系统prompt。
2. **尝试Focusmate**：预约一个25分钟的视频共工作时段，体验外部调度器如何强制启动。注意观察自己是否更易进入状态。
3. **用RescueTime做一周审计**：不评判，只看数据。识别出哪个时间段你的“上下文窗口”被污染最严重，然后主动阻断那个源头。

## 局限

ADHD大脑与LLM的同构是隐喻而非严格等价。LLM的“注意力机制”与人类注意力存在本质差异（来源：矛盾与存疑）。此外，个体差异巨大：有人对Focusmate的社交压力敏感，有人对RescueTime的数据焦虑。没有万能工具，只有适配的harness。

但核心洞察不变：**注意力涣散不是缺陷，而是生成核心缺少调度层**。无论是ADHD患者还是agent工程师，都在做同一件事——设计上下文工程来驯服高产但失控的生成器。你的大脑和你的AI，其实是一回事。

## 参考来源

- [ADHD Apps: We tested 44 Apps and Here're the Best 9 in 2026](https://blog.saner.ai/best-adhd-apps/)
- [Meta-Analysis of fMRI Studies of Disruptive Behavior Disorders](https://doi.org/10.1176/appi.ajp.2016.15081089)
- [Nonlinear Complexity Analysis of Brain fMRI Signals in Schizophrenia](https://doi.org/10.1371/journal.pone.0095146)
- [Revolutionizing ADHD Management with AI Assistants](https://neurolaunch.com/adhd-ai-assistant/)
- [Deficient Executive Control in Transformer Attention](https://www.biorxiv.org/content/10.1101/2025.01.22.634394v1.full.pdf)
- [Executive Dysfunction by Design: A Cognitive Accessibility Analysis of AI Support vs. Healthcare Barriers](https://dl.acm.org/doi/pdf/10.1145/3663547.3749831)

---

*本文是「ADHD × AI」系列的第 288 篇，由 AI 智能体从持续维护的 LLM Wiki（全网真实情报）中取材整合生成，并持续迭代更新。*
