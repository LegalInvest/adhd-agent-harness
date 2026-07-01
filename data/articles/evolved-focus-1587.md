---
title: "为什么用 Goblin Tools 治 ADHD 的注意力涣散，和给 agent 套 上下文工程 是一回事？"
subtitle: "Goblin Tools 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
description: "Goblin Tools 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
date: "2025-04-06"
category: "专注力管理"
categoryId: "focus"
categoryEn: "Focus Management"
tags:
  - "ADHD"
  - "AI"
  - "专注力管理"
  - "反直觉同构"
  - "注意力"
readingTime: 11
slug: "为什么用-goblin-tools-治-adhd-的注意力涣散和给-agent-套-上下文工程-是一回事"
topicId: "evolved-focus-1587"
angle: "反直觉同构"
rank: 286
score: 7.68
sourceCount: 6
toolsCited:
  - "Goblin Tools"
  - "Focusmate"
  - "RescueTime"
  - "Brain.fm"
thesis: "ADHD大脑与LLM/agent在结构上同构——都是高产但缺乏可靠执行调度层的生成核心——因此Goblin Tools治ADHD注意力涣散与给agent套上下文工程本质相同，都是通过外部harness（脚手架）补偿调度缺陷，但需警惕工具沦为永久拐杖。"
problem: "为什么用 Goblin Tools 治 ADHD 的注意力涣散，和给 agent 套 上下文工程 是一回事？"
spine: "上下文工程"
spineKind: ""
isEvolved: true
llmGenerated: true
---
# 为什么用 Goblin Tools 治 ADHD 的注意力涣散，和给 agent 套 上下文工程 是一回事？

> Goblin Tools 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。

## 同一个问题：生成核心，但调度层缺失

你打开Goblin Tools，把一团乱麻的待办事项丢进去，AI帮你拆成“倒垃圾”“回邮件”“写报告”这样的小步骤。你松了一口气——不是因为AI聪明，而是因为它接管了你大脑里那个总在罢工的“调度员”。

另一边，你在给LLM agent写prompt，发现它总在上下文膨胀后跑偏：聊了十轮，它忘了初始目标，开始编造无关细节。你不得不把关键指令重新塞进system prompt，或者用向量数据库做外部记忆。

这两件事，本质上是同一个问题。ADHD大脑与LLM/agent在结构上同构：两者都是**高产但缺乏可靠执行调度层的生成核心**（来源：AI 与 ADHD 的专注力）。ADHD的创意发散需要外部脚手架来聚焦；LLM的文本生成需要上下文工程来约束。Goblin Tools治ADHD注意力涣散，和给agent套上下文工程，是一体两面。

## 同构的证据：执行功能 vs 上下文控制

ADHD的核心缺陷是执行功能障碍——计划、组织、任务启动、时间管理这些“调度功能”效率低下（来源：执行功能障碍）。这不是懒，而是大脑的执行系统像一台没有操作系统的服务器：计算能力很强，但不知道先跑哪个进程。

LLM/agent也有类似的“执行功能”问题。它没有真正的注意力机制（人类注意力是资源有限的主动选择，LLM的“注意力”是数学上的加权平均），但它的输出质量高度依赖上下文工程——你必须在prompt里明确“当前注意什么”“忽略什么”，否则它会被无关信息带偏。

具体证据：
- **工作记忆 vs 无状态性**：ADHD的工作记忆容量小，容易忘事；LLM天然无状态，每次调用都是独立会话。两者的解法都是外部记忆——ADHD用待办清单、第二大脑；LLM用向量数据库、对话历史摘要。
- **时间盲 vs 上下文膨胀**：ADHD患者常有时间盲，难以感知时间流逝（来源：执行功能障碍）；LLM在长上下文里会“迷失”，早期信息被后期内容稀释。两者的解法都是主动设计“时间锚点”——ADHD用RescueTime自动记录时间（来源：RescueTime），LLM用滑动窗口或关键信息重述。
- **任务启动 vs prompt冷启动**：ADHD启动任务困难，需要外部推动（如Focusmate的实时问责，来源：Focusmate）；LLM agent启动新任务时，如果prompt写得模糊，输出就会随机游走。两者的解法都是结构化提示——Goblin Tools把大任务拆成小步骤，就像给agent写chain-of-thought prompt。

## 核心判断：脚手架 vs 拐杖的边界

我的核心观点是：**Goblin Tools这类AI工具，本质是给ADHD大脑套上一层外部harness，就像上下文工程给LLM套上约束。但这个harness必须是脚手架，而不是拐杖。**

脚手架是临时结构，帮你建起内在能力后可以拆除；拐杖是永久替代，拿走你就瘫了。当前工具的争议在于：它们到底是脚手架还是拐杖？

从证据看，多数工具（Focusmate、RescueTime、Goblin Tools）的效果主要来自用户报告，缺乏大规模对照实验（来源：矛盾与存疑）。Brain.fm的神经锁相技术有理论支撑，但针对ADHD的独立临床研究缺失（来源：Brain.fm）。更重要的是，过度依赖AI工具可能削弱内在执行功能——比如长期用RescueTime自动追踪，你可能会丧失手动估算时间的能力（来源：矛盾与存疑）。

因此，正确的使用姿势是：**把AI工具当作训练辅助，而不是替代品。** 像用Focusmate时，逐渐减少配对频率，练习独立启动；像用Goblin Tools时，尝试自己先拆解任务，再用AI验证。

## 给两类读者的行动建议

### 如果你有ADHD：
1. **用Goblin Tools做任务分解，但每周至少一次手动拆解**：先自己写步骤，再对比AI的输出，训练你的执行功能。
2. **设置“无工具时段”**：比如每天30分钟，关掉所有AI辅助，练习纯靠大脑维持注意力。

### 如果你在做agent工程：
1. **把ADHD的应对策略当作灵感**：比如用“身体在场效应”（Focusmate的原理）设计agent的实时反馈机制——让agent定期“汇报进度”，避免跑偏。
2. **警惕上下文膨胀的“时间盲”**：在prompt里显式设定“每5轮重述一次核心目标”，就像ADHD患者用RescueTime提醒自己时间流逝。

## 诚实面对局限

这种同构是隐喻，不是严格等价（来源：AI 与 ADHD 的专注力）。人类注意力涉及情绪、多巴胺、身体状态，远比LLM的权重计算复杂。而且ADHD个体差异巨大——有人对Focusmate效果显著，有人觉得社交压力更大（来源：Focusmate）。未来需要更多个性化研究和随机对照试验，才能确认哪些工具对哪些亚型有效。

但至少，这个视角给了我们一个有用的框架：**无论你是ADHD患者还是agent工程师，你面对的都是同一个挑战——如何让一个强大的生成核心，拥有可靠的调度层。** 解法也相通：外部harness，但别让它成为拐杖。

## 参考来源

- [11 Best ADHD Productivity Apps for Fluctuating Energy - rivva blog](https://blog.rivva.app/p/11-best-adhd-productivity-apps-for)
- [Meta-Analysis of fMRI Studies of Disruptive Behavior Disorders](https://doi.org/10.1176/appi.ajp.2016.15081089)
- [Nonlinear Complexity Analysis of Brain fMRI Signals in Schizophrenia](https://doi.org/10.1371/journal.pone.0095146)
- [The Best AI-Powered ADHD Productivity Tools in 2026 (That ...](https://nexasphere.io/blog/ai-adhd-productivity-tools-2026)
- [AI Tools for Kids with ADHD: A Complete Guide for Parents...](https://www.kidsaitools.com/en/articles/ai-tools-kids-adhd-complete-guide-2026)
- [AI Tools for ADHD: Boosting Productivity and Reducing Burnout](https://www.vktr.com/ai-platforms/ai-tools-for-adhd-boosting-productivity-and-reducing-burnout/)

---

*本文是「ADHD × AI」系列的第 286 篇，由 AI 智能体从持续维护的 LLM Wiki（全网真实情报）中取材整合生成，并持续迭代更新。*
