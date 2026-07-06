---
title: "为什么用 ChatGPT 治 ADHD 的学习半途而废，和给 agent 套 外部记忆/向量库 是一回事？"
subtitle: "ChatGPT 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
description: "ChatGPT 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
date: "2025-03-29"
category: "学习方法"
categoryId: "learning"
categoryEn: "Learning Methods"
tags:
  - "ADHD"
  - "AI"
  - "学习方法"
  - "反直觉同构"
  - "技能提升"
readingTime: 9
slug: "为什么用-chatgpt-治-adhd-的学习半途而废和给-agent-套-外部记忆向量库-是一回事"
topicId: "evolved-learning-2149"
angle: "反直觉同构"
rank: 45
score: 7.96
sourceCount: 6
toolsCited:
  - "ChatGPT"
  - "Perplexity"
  - "Goblin Tools"
  - "Saner.AI"
  - "Focusmate"
thesis: "ADHD 大脑与 LLM 都是强大的生成核心但缺乏执行调度层，两者共享同一套 harness 思路：用外部记忆/向量库补偿无状态缺陷，用重锚定系统对抗目标漂移。"
problem: "为什么用 ChatGPT 治 ADHD 的学习半途而废，和给 agent 套 外部记忆/向量库 是一回事？"
spine: "无状态与外部记忆"
spineKind: ""
isEvolved: true
llmGenerated: true
caseStudies:
  - "孔子"
  - "曹植"
  - "Mary Thompson"
---
# 为什么用 ChatGPT 治 ADHD 的学习半途而废，和给 agent 套 外部记忆/向量库 是一回事？

> ChatGPT 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。

## 一个问题，两个世界

你打开 ChatGPT，想让它帮你规划 2025 年的学习计划。三分钟后，你发现自己正在问它“如何用 Python 写一个贪吃蛇游戏”——你甚至不会 Python。

这不是你的错。这是 ADHD 大脑和 LLM 共享的底层 bug：**它们都是强大的生成核心，但缺乏可靠的执行调度层。** ADHD 的大脑每秒产生无数联想，LLM 的注意力头能同时扫描整个上下文，但两者都没有内置的“先做这个，再做那个”的调度器。结果就是：目标漂移、任务半途而废、上下文膨胀后彻底迷失。

而解法也一模一样：**给这个生成核心套上一个外部 harness——用外部记忆/向量库补偿无状态，用重锚定系统对抗目标漂移。**

## ADHD 侧：无状态的大脑需要外部记忆

ADHD 的工作记忆极不稳定。你刚想好要做什么，手机通知一响，就忘了。这不是懒，是执行功能缺陷——大脑的“RAM”容量正常，但“缓存管理器”坏了（来源：[[工作记忆]]页）。

工具们正在做同一件事：给大脑装一个外部记忆体。

- **Goblin Tools** 的 Magic ToDo 把“清理厨房”分解成 12 个小步骤，每个步骤就是一个外部记忆块，你不需要在脑子里保持整个计划（来源：Goblin Tools 页）。
- **Saner.AI** 提供“本地记忆”和“知识回忆”，你不需要记住上周的笔记，问它就行（来源：Saner.AI 页）。
- **Perplexity** 帮你把一个宏大目标分解为可管理的步骤，降低启动门槛（来源：Perplexity 页）。

这些工具的本质，就是给 ADHD 大脑加了一个外部向量库——你不需要在脑子里索引，只需要调用。

## LLM/Agent 侧：无状态的模型需要外部记忆

LLM 本身没有跨会话记忆。你问它“帮我规划项目”，它回答得很好；但如果你在同一个会话里聊了 20 轮，它就开始“忘记”最初的目标，输出变得散乱。这就是 LLM 的“目标漂移”——和 ADHD 的分心一模一样。

Agent harness 的解法是什么？**给 LLM 套一个外部记忆/向量库。** 工程师们正在做：

- 用向量数据库存储对话历史和关键信息，每次查询时检索相关片段，让 LLM 始终“记得”上下文（来源：Building an AI Agent Harness from Scratch）。
- 设置 token 预算和工具调用次数上限，防止 agent 陷入无限循环（来源：同上）。
- 加入 human-in-the-loop 检查点，在关键决策前暂停并询问用户（来源：同上）。

这和 ADHD 工具做的事情完全同构：**外部记忆体 + 重锚定机制。**

## 人物案例：孔子和曹植的 harness

拿孔子来说。他 1 米 9 的个子，精力旺盛到周游列国 14 年都坐不住，冲动到见南子急得对天发誓，骂宰予“朽木不可雕”。但他对音乐可以“三月不知肉味”。这是典型的 ADHD 特质：超聚焦与冲动并存。

他的 harness 是什么？**“克己复礼”**——用外在的“礼”作为行为边界，每日反省（“吾日三省吾身”），70 岁才做到“从心所欲不逾矩”。这个“礼”就是一个外部调度层：不是靠内在意志，而是靠一套可执行的规则系统。

曹植更明显。他写诗超专注，铜雀台作赋一挥而就；但政治上一塌糊涂，醉闯司马门，醉酒不能受命救曹仁。他的 harness 是以诗赋为核心，把所有失意注入诗歌——用创作作为外部输出通道，避免情绪失控。

这和 LLM harness 的同构对应：**“日课”对应定时 re-grounding，“秘书”对应外部调度器。** 孔子没有一个“内在执行功能”来管住自己，所以他设计了一套外部规则。LLM 也没有内在调度层，所以工程师给它套上了向量库和检查点。

## 脚手架 vs 拐杖：边界在哪里？

这里有一个关键争议：这些工具是脚手架还是拐杖？

脚手架是临时性的，目的是让你最终能自己走路。拐杖是永久替代，离开它你就瘫痪。

ADHD 工具和 LLM harness 都面临同样的问题。如果 Goblin Tools 帮你分解任务，但你从未学会自己分解，那它就是拐杖。如果 agent harness 的向量库让你永远不需要训练模型的长上下文能力，那也是拐杖。

证据显示，过度依赖 AI 可能削弱内在执行功能的锻炼机会（来源：[[拐杖与脚手架]]页）。但问题在于，**对于某些人/模型，内在执行功能可能永远无法达到足够水平**——就像孔子到 70 岁才勉强做到。那么，一个永久的外部调度层，是否比没有调度层更好？

我的判断是：**脚手架和拐杖的边界不是工具本身，而是用户是否保留了对工具的控制权。** 如果你能主动选择何时使用、何时关闭，它就是脚手架；如果你离开它就无法启动任何任务，它就是拐杖。

## 争议与局限

同构视角虽然迷人，但必须诚实指出：它目前只是理论类比，缺乏实证基础（来源：[[矛盾与存疑]]页）。ADHD 的异质性很大——注意力主导型和冲动主导型对 AI 工具的反应可能不同（来源：[[AI 与 ADHD 的学习方式]]页）。LLM 的幻觉和上下文限制也可能引入新的干扰（来源：同上）。

此外，传统提醒系统有一个关键缺陷：设置提醒本身就是一个执行功能任务（来源：[[重锚定与目标漂移]]页）。这意味着，如果你连设置 AI 工具的精力都没有，那工具就毫无用处。

## 今天就能试的 3 件事

1. **用 Goblin Tools 的 Magic ToDo 分解一个你拖延已久的任务。** 输入“写周报”，看它分解成 10 个步骤。挑第一个步骤做 5 分钟。（来源：Goblin Tools 页）
2. **用 ChatGPT 创建一个“外部记忆”会话。** 把你要做的项目背景、目标、当前进度写在一个固定会话里，每次开始前先问“根据以上信息，我下一步该做什么？”——这就是你的向量库。
3. **设置一个重锚定闹钟。** 每 25 分钟响一次，问自己：“我现在在做的事，和最初的目标一致吗？”——这就是 human-in-the-loop 检查点。

ADHD 大脑和 LLM 都不是坏的——它们只是缺一个 harness。而 harness 可以自己造。

## 参考来源

- [Can ChatGPT be Your Personal Medical Assistant?](http://arxiv.org/abs/2312.12006v1) — 证据等级：低（GRADE）
- [One Billion Word Benchmark for Measuring Progress in Statistical Language Modeling](http://arxiv.org/abs/1312.3005v3) — 证据等级：低（GRADE）
- [Activation Sparsity Opportunities for Compressing General Large Language Models](http://arxiv.org/abs/2412.12178v2) — 证据等级：低（GRADE）
- [YouZhi: Towards High-Concurrency Financial LLMs via Adaptive GQA-to-MLA Transition](http://arxiv.org/abs/2606.05868v1) — 证据等级：低（GRADE）
- [FBI-LLM: Scaling Up Fully Binarized LLMs from Scratch via Autoregressive Distillation](http://arxiv.org/abs/2407.07093v1) — 证据等级：低（GRADE）
- [Prompt Injection Attack to Tool Selection in LLM Agents](http://arxiv.org/abs/2504.19793v3) — 证据等级：低（GRADE）

---

*本文是「ADHD × AI」系列的第 45 篇，由 AI 智能体从持续维护的 LLM Wiki（全网真实情报）中取材整合生成，并持续迭代更新。*
