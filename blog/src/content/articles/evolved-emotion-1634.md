---
title: "为什么用 Saner.AI 治 ADHD 的情绪失调，和给 agent 套 会褪去的脚手架 是一回事？"
subtitle: "Saner.AI 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
description: "Saner.AI 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
date: "2025-05-17"
category: "情绪调节"
categoryId: "emotion"
categoryEn: "Emotional Regulation"
tags:
  - "ADHD"
  - "AI"
  - "情绪调节"
  - "反直觉同构"
  - "情绪管理"
readingTime: 8
slug: "为什么用-sanerai-治-adhd-的情绪失调和给-agent-套-会褪去的脚手架-是一回事"
topicId: "evolved-emotion-1634"
angle: "反直觉同构"
rank: 388
score: 7.65
sourceCount: 6
toolsCited:
  - "Saner.AI"
  - "Inflow"
  - "Goblin Tools"
  - "Motion"
  - "Tiimo"
thesis: "ADHD的情绪失调与LLM的上下文失控本质是同一类问题——生成核心缺乏可靠的执行调度层；Saner.AI等工具通过外部记忆和任务分解为ADHD提供临时脚手架，正如harness工程为agent提供会褪去的执行框架，两者同构于“补偿而非替代”的哲学。"
problem: "为什么用 Saner.AI 治 ADHD 的情绪失调，和给 agent 套 会褪去的脚手架 是一回事？"
spine: "拐杖与脚手架"
spineKind: ""
isEvolved: true
llmGenerated: true
---
# 为什么用 Saner.AI 治 ADHD 的情绪失调，和给 agent 套 会褪去的脚手架 是一回事？

> Saner.AI 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。

## 问题：情绪失调不是“心理问题”，而是调度层崩溃

ADHD的情绪失调常被误解为“情绪管理能力差”。但神经科学告诉我们，根源在执行功能缺陷：工作记忆容量有限，情绪信息无法被有效加工；时间盲导致对情绪持续时间的误判；任务启动困难加剧挫败感，形成情绪漩涡（来源：AI与ADHD的情绪调节）。

同样，LLM agent在长上下文或复杂任务中出现的“幻觉”和“逻辑断裂”，也不是模型本身能力不足，而是上下文工程和工具调度层失效——生成核心（LLM）与执行层（harness）脱节。

**核心观点**：ADHD大脑和LLM都是“高产但缺执行调度层的生成核心”。情绪失调与LLM的上下文失控是同构问题。解决方案不是“修复核心”，而是设计会褪去的脚手架——临时接管调度，让核心流畅运作，同时逐步放手。

## 同构解法：Saner.AI 与 harness 工程

Saner.AI 的核心功能是“知识回忆和本地记忆”，减少搜索循环和标签切换（来源：Saner.AI）。对ADHD而言，工作记忆不足导致频繁切换任务、丢失信息，情绪随之波动。Saner.AI 作为外部记忆层，让用户无需“记住”就能找回信息，降低了认知负荷，从而稳定情绪。

在LLM侧，harness工程通过工具调用、上下文管理和规划循环，为agent提供类似的外部记忆和调度层。例如，Goblin Tools 的 Magic ToDo 将“整理房间”分解为可执行步骤（来源：Goblin Tools），对应agent的“多步推理+工具调用”模式。Motion 和 Tiimo 的动态规划（来源：规划循环与任务分解）则对应agent的实时重规划。

**证据**：
- ADHD侧：Inflow 通过训练工作记忆改善认知控制，其靶点（背外侧前额叶皮层）与工作记忆表现正相关（来源：Inflow）。但直接针对Saner.AI的随机对照试验缺乏，效果主要来自用户报告（来源：矛盾与存疑）。
- LLM侧：Harness工程被定义为“设计脚手架——上下文传递、工具接口、规划工件、验证”（来源：规划循环与任务分解）。现代agent系统通过组合多个模型和工具达成SOTA，而非依赖单一模型（来源：工具使用与认知卸载）。

**同构对应**：ADHD将不擅长的精确状态外包给外部工具，对应LLM agent通过function calling将复杂任务拆解为工具调用。两者都依赖外部系统补偿内部执行功能的不足。

## 脚手架 vs 拐杖：边界在哪里？

关键区分在于“补偿”还是“替代”。脚手架会褪去，拐杖则永久依赖。

- 脚手架：Saner.AI 提供记忆检索，但用户仍需主动使用；Goblin Tools 分解任务，但用户仍需执行步骤。工具设计应注重“agent UX”——简单、无认知开销，不增加额外负担（来源：工具使用与认知卸载）。
- 拐杖：过度依赖AI可能削弱内在时间感知能力（来源：矛盾与存疑）。例如，长期使用自动规划工具可能导致用户丧失手动规划能力。

**争议**：现有证据多来自用户报告，缺乏大规模对照实验。且个体差异大——注意缺陷型与多动冲动型对工具反应不同（来源：矛盾与存疑）。工具设计者声称是脚手架，但实际使用中可能沦为拐杖。

## 今天就能试的行动

1. **用Saner.AI记录情绪触发点**：每次情绪波动时，语音输入到Saner.AI，利用其本地记忆功能快速检索之前类似场景，识别模式。这类似agent的上下文工程——主动设计注意焦点。
2. **用Goblin Tools分解一个让你焦虑的任务**：输入模糊任务（如“准备会议”），观察AI输出步骤。对比自己手动分解的差异，体会“外部调度层”如何降低启动焦虑。
3. **设置工具使用时限**：例如，使用Motion规划一天后，第二天尝试手动调整计划。刻意练习脱离工具，避免依赖。
4. **评估工具的“认知开销”**：如果某个工具让你花更多时间学习或切换，果断放弃——好的脚手架应无缝嵌入日常流程（来源：工具使用与认知卸载）。

## 局限与诚实

- 证据不足：Saner.AI、Goblin Tools等工具缺乏独立RCT，效果主要基于用户反馈（来源：矛盾与存疑）。
- 多巴胺干预争议：基于多巴胺的奖励系统可能强化成瘾行为（来源：AI与ADHD的情绪调节）。
- 长期效果未知：神经可塑性变化缺乏追踪（来源：AI与ADHD的情绪调节）。

但同构视角的价值在于：它揭示了问题本质不是“情绪管理”或“模型能力”，而是调度层设计。无论是ADHD还是LLM，解决方案都是——设计会褪去的脚手架，让生成核心自由奔跑。

## 参考来源

- [Dynamic causal brain circuits during working memory and their functional controllability](https://doi.org/10.1038/s41467-021-23509-x)
- [Best AI Tools for ADHD Productivity in 2026 (Honest Review) - Iwo Szapar](https://www.iwoszapar.com/p/best-ai-tools-adhd-productivity-2026)
- [AI Tools for ADHD: Boosting Productivity and Reducing Burnout](https://www.vktr.com/ai-platforms/ai-tools-for-adhd-boosting-productivity-and-reducing-burnout/)
- [The Best AI-Powered ADHD Productivity Tools in 2026 (That ...](https://nexasphere.io/blog/ai-adhd-productivity-tools-2026)
- [“A Cognitive Collaborator:” How Adults with ADHD Are Using ChatGPT](https://www.additudemag.com/how-to-use-chatgpt-executive-function-adhd/?srsltid=AfmBOoq-REuSO0UJC656kbLBAd5u3CDNmGeVNrZ79iouVqrFlN919a39)
- [Harnessing Artificial Intelligence to Live Better with ADHD - CHADD](https://chadd.org/attention-article/harnessing-artificial-intelligence-to-live-better-with-adhd/)

---

*本文是「ADHD × AI」系列的第 388 篇，由 AI 智能体从持续维护的 LLM Wiki（全网真实情报）中取材整合生成，并持续迭代更新。*
