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
llmGenerated: true
isoStrength: "B"
caseStudies:
  - "张一鸣"
  - "于东来"
  - "江静"
---
# ADHD 职场人视角：为什么「治好 ADHD 的独自做事缺乏问责、容易放弃」和「让 LLM 不跑飞」其实是同一道工程题？

> 高风险 agent 需要 human-in-the-loop 监督——同一套 harness 思路，两边都成立。

## 1. 两个看似无关的崩溃现场

一个 ADHD 职场人打开电脑，准备独自写一份方案。三小时后，文档只开了个头，人却已经在查「明代火器」和「LLM 的 RLHF 对比」。另一个 AI 工程师把高风险任务交给 agent，设定目标后让它自主执行，结果发现它把中间步骤越走越远，生成了大量看似合理但偏离真实需求的结果。前者的问题叫「独自做事缺乏问责、容易放弃」，后者叫「高风险 agent 跑飞」。表面看，一个是神经多样性，一个是系统工程。但如果我们把它们拆成结构，会发现是同一道题：一个**高产但缺执行调度层的生成核心**，需要怎样的外部 harness，才能稳定落地？

## 2. 同构解剖：为什么两边是同一类系统

ADHD 侧的「跑飞」不是意志力问题。 wiki 资料指出，执行功能障碍是 ADHD 的核心特征之一，表现为计划、组织、时间管理、任务启动等困难，且与工作记忆、抑制控制、情绪调节互相纠缠（来源：执行功能障碍）。情绪失调在 ADHD 中也被视为核心特征，具有高强度、高积极与消极行为的特点，成人 ADHD 常表现为慢性混乱与情绪失调（来源：情绪失调；Social Functioning and Emotional Regulation in the Attention Deficit Hyperactivity Disorder Subtypes）。更关键的是，自上而下的认知功能障碍只解释了 ADHD 表型的一小部分，情绪与执行调节的缺口远大于「不够努力」（来源：Top-Down Dysregulation—From ADHD to Emotional Instability）。

LLM/agent 侧同样如此。模型能生成流畅、连贯、看似合理的输出，但缺乏稳定的执行调度层：没有真正的时间感、没有对工作记忆的持续维护、也没有对情绪波动或目标漂移的自动修正。在高风险任务中，这种缺失会导致幻觉、工具误用、目标偏离。因此工程侧的共识是：不能让它全自主跑完，必须在关键节点把人类放回回路中做校验与再锚定（来源：人在回路与身体在场）。

两边的核心都是「生成核心很强，调度层很弱」。ADHD 是神经层面的执行层低带宽；LLM 是架构层面的规划与验证层薄弱。 ADHD 需要外部执行功能层；LLM 需要外部 agent harness。二者同构。

## 3. 同一套 harness：人在回路与身体在场

ADHD 的解药不是「更努力」，而是让外部系统替大脑承担调度、记忆与问责。Goblin Tools 的 Magic ToDo 把「清理厨房」这种模糊任务切成具体可执行的子任务，还能调节分解粒度（来源：12 AI Personal Assistants Built for ADHD Brains (2026 Rankings)）。这对应 LLM 侧的任务拆解与 chain-of-thought：把复杂目标拆成可验证的小步骤。Motion 自动排程、动态调整，消除「下一步该做什么」的决策负担，帮助用户克服时间盲（来源：The Best AI-Powered ADHD Productivity Tools in 2026；11 Best ADHD Productivity Apps for Fluctuating Energy - rivva blog）。这对应 agent 的调度器与 checkpointer：持续评估优先级、依赖与截止日期，并在漂移时重新规划。Saner.AI 通过本地记忆与知识回忆减少搜索循环和标签切换（来源：Best AI Tools for ADHD Productivity in 2026），对应 LLM 的长期记忆与检索增强：让模型不必每次都从零重建上下文。

这些工具的共同点是「身体在场」的工程化替代：它们把 accountability、调度、记忆外置到系统里。而 LLM 侧的人-in-the-loop、guardrails、tool use、periodic re-grounding 做的也是同一件事：在人类不在物理现场时，仍然保留一个可回退、可校验、可问责的节点。这并不意味着 AI 能完全替代真实人际互动——它的效果存在争议，尤其是虚拟在场能否复制真实身体在场，目前仍存疑（来源：矛盾与存疑）。

## 4. 一个真实案例：张一鸣的 harness 与 agent harness 的对应

张一鸣的 ADHD 特质在资料里很典型：思维极度发散，什么新东西都要研究；理性、组织与产品导向；不爱混圈子，只接受系统与文化的管理（来源：张一鸣的 harness 自我管理系统）。他的专属 harness 包括：延迟满足感、OKR 管理系统、Context not Control、用系统和文化管公司、不搞集权、从用户需求出发而非主观判断。

这和 LLM/agent 的 harness 惊人地一一对应：

- **延迟满足感** = 长期回报与信用分配机制，防止 agent 被短期 reward hacking 带偏；
- **OKR 管理系统** = 外部目标对齐与评估器，定期 re-ground 模型行为；
- **Context not Control** = 不依赖单一中央控制者，而是把决策上下文和监督节点分布给多个反馈源，这正是 human-in-the-loop 系统的架构思想；
- **用系统和文化管公司** = 把约束写入 prompt、constitution、tool 规范，而不是靠运行时随机纠偏。

张一鸣不是「治好自己的 ADHD」，而是把自己的大脑接入了一个外部 harness。LLM 工程师要做的，本质上也是给模型接入一个类似的 harness。

## 5. 核心判断：harness 不是拐杖，但也不是万能药

我的判断是：ADHD 与 LLM 的失控，都不能靠「让核心变强」来解决，而应靠「让外部执行层可靠」来解决。 ADHD 不是缺目标，而是缺目标与行动之间的稳定调度器；LLM 不是缺知识，而是缺知识与真实世界之间的稳定校验器。因此，两边的工程重点都是脚手架：一种在需要时提供支撑、但使用者仍保有主体性的结构。

但这里必须诚实划界。第一，「ADHD 大脑与 LLM 同构」目前只是理论类比，缺乏实证基础，不应被当作科学事实推广（来源：矛盾与存疑）。第二，工具效果常被夸大：Motion 缺乏独立临床验证，Brain.fm 在 ADHD 人群中的独立临床证据也有限（来源：矛盾与存疑）。第三，任何工具都可能从「脚手架」变成「拐杖」，过度依赖反而会削弱自主执行能力；身体在场效应能否被 AI 真正替代，仍有争议（来源：矛盾与存疑）。因此，harness 的核心价值不是替代人，而是让人更清楚自己在何时需要被拉回正轨。

## 6. 今天就能试的四件事

1. **把最难启动的任务丢给 Goblin Tools**：用 Magic ToDo 把它拆成 3 个具体步骤，先只做第一步。任务分解能降低多巴胺门槛，也让 agent 侧的「任务拆解」思路反过来服务你。
2. **让 Motion 替你决定明天的顺序**：把任务、会议、截止日期输入后，让 AI 排程，减少「

## 参考来源

**同构强度：B 级** —— 机制类比（ADHD 侧与 LLM/agent 侧均有真实文献，机制可映射）

- [ADHD Apps: We tested 44 Apps and Here're the Best 9 in 2026](https://blog.saner.ai/best-adhd-apps/) — 证据等级：低（GRADE）
- [12 AI Personal Assistants Built for ADHD Brains (2026 Rankings)](https://www.usecarly.com/blog/best-ai-personal-assistant-adhd/) — 证据等级：低（GRADE）
- [LBD同构对：自我调节与元认知 — Inhibitory control and emotion regulation in preschool child ↔ ObjexMT: Objective Extraction and Metacognitive Calibration ](https://doi.org/10.1016/j.cogdev.2007.08.002) — 证据等级：低（GRADE）
- [LBD同构对：自我调节与元认知 — Emotion-related self-regulation and its relation to children ↔ A Reproducibility Study of Metacognitive Retrieval-Augmented](https://doi.org/10.1146/annurev.clinpsy.121208.131208) — 证据等级：低（GRADE）
- [The 12 Best AI Tools for 2026 (That People Actually Use)](https://www.synthesia.io/post/ai-tools) — 证据等级：低（GRADE）
- [The AI Powered SuperApp for Work | Motion](https://www.usemotion.com/) — 证据等级：低（GRADE）

---

*本文是「ADHD × AI」系列的第 9 篇，由 AI 智能体从持续维护的 LLM Wiki（全网真实情报）中取材整合生成，并持续迭代更新。*
