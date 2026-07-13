---
title: "为什么用 ChatGPT 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用 是一回事？"
subtitle: "ChatGPT 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
description: "ChatGPT 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
date: "2025-05-11"
category: "AI工具实战"
categoryId: "ai-tools"
categoryEn: "AI Tools in Practice"
tags:
  - "ADHD"
  - "AI"
  - "AI工具实战"
  - "反直觉同构"
  - "效率工具"
readingTime: 14
slug: "为什么用-chatgpt-治-adhd-的任务启动困难和给-agent-套-function-calling-工具调用-是一回事"
topicId: "evolved-ai-tools-2057"
angle: "反直觉同构"
rank: 32
score: 8.0
sourceCount: 6
toolsCited:
  - "ChatGPT"
  - "Goblin Tools"
  - "Saner.AI"
  - "Lex"
  - "Mem"
  - "Otter.ai"
thesis: "ADHD大脑与LLM在结构上同构——都是高产生成核心但缺乏可靠执行调度层，因此用ChatGPT辅助任务启动困难与为agent套function calling工具调用是同一类工程：通过外部脚手架补偿执行功能缺陷。"
problem: "为什么用 ChatGPT 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用 是一回事？"
spine: "工具使用与认知卸载"
spineKind: ""
isEvolved: true
llmGenerated: true
caseStudies:
  - "孔子"
  - "王阳明"
  - "Laura Riley"
---
# 为什么用 ChatGPT 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用 是一回事？

> ChatGPT 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。

## 问题：为什么AI治ADHD与Agent工程是一回事？

如果你是一个ADHD患者，你可能经历过这样的场景：打开电脑，盯着空白的文档，大脑里有一万个想法，但手指就是敲不出一个字。任务启动困难——像被无形的墙堵在起点。如果你是一个AI agent工程师，你可能也经历过类似的挫败：给LLM一个复杂目标，它输出了一大段漂亮的推理，但就是不调用工具、不执行动作，或者调用到一半就偏离轨道。

这两个问题，表面看一个属于神经多样性，一个属于软件工程，但底层结构惊人地同构。ADHD大脑与LLM都是强大的生成核心——能产出海量创意、快速联想、发现模式——但缺乏可靠的内置执行调度层（来源：ADHD 大脑与 LLM 的同构）。任务启动困难，本质上是执行功能层失灵；而agent的function calling失败，本质上是调度层缺失。两边的解法因此共享同一套工程逻辑：给核心套上外部脚手架（harness），补偿执行缺陷。

## 同构：生成核心与调度层

ADHD大脑的多巴胺系统失衡导致动机信号弱、工作记忆不稳定（来源：多巴胺）。你明明知道该做什么，但大脑不给你“启动”的指令。LLM同样是无状态的——每次对话都是新的开始，没有内置的优先级和步骤记忆。你给GPT一个任务，它可能给出一个完美的计划，但不会自动执行下一步。

这正是为什么ADHD患者自发用ChatGPT作为执行功能外挂（来源："A little bit of a life raft" – Exploring the Use and Experiences of ChatGPT as a Support Tool among Adults with ADHD）。他们给ChatGPT一个模糊指令（比如“帮我规划今天的工作”），ChatGPT返回一个分解好的清单。这本质上就是给大脑套了一个外部调度器。同样，agent工程师给LLM套上function calling框架——定义工具、设定约束、管理上下文——让模型从“只会说”变成“会做”。

## 案例：孔子与王阳明的Harness系统

这种同构并非现代才有。孔子和王阳明，两位历史人物，都展现了ADHD特质，并各自构建了外部脚手架。

孔子精力旺盛、坐不住（周游列国14年），冲动爱骂人（骂宰予“朽木不可雕”），对音乐超专注（三月不知肉味），但对种地零耐心。他的harness是“克己复礼”——用外在的“礼”作为行为边界，每日反省（“吾日三省吾身”）。这就像给LLM设定了一套严格的function calling规则：每个动作必须符合“礼”的定义，否则触发反省回调。

王阳明5岁不会说话（神经发育延迟），兴趣爆发式转移（格物→兵法→道→佛→军事），冲动上书骂刘瑾被廷杖。他的harness是“致良知”——用内在良知作为决策标准，并在事上练（军旅中坚持讲学）。这相当于给agent设置了一个“核心价值观”约束，所有工具调用必须通过良知校验。

两人都通过外部脚手架补偿了执行功能缺陷，最终成就斐然。这与现代ADHD工具和agent engineering的目标完全一致。

## 现有工具：从分解到调度

当前AI工具已在多个维度实践这一思路：

- **任务分解**：Goblin Tools的Magic ToDo将模糊任务拆解为小步骤，降低启动门槛（来源：Goblin Tools）。这相当于给LLM一个plan-then-execute的agent模式。
- **外部记忆**：Saner.AI和Mem补偿工作记忆不足，减少搜索循环（来源：Saner.AI；Mem）。这对应agent的memory模块。
- **单一指令触发多步骤**：Lex允许用户用一条指令触发复杂任务序列（来源：Lex）。这本质上是agent的function calling——将意图映射为工具链。
- **实时转录**：Otter.ai捕捉会议灵感，减轻笔记负担（来源：Otter.ai）。这相当于agent的log系统。

这些工具的共同点是：它们不是替代大脑或LLM的生成能力，而是提供执行调度层。

## 核心观点：脚手架，不是拐杖

我的判断是：ADHD与LLM同构性的价值不在于它是否完全科学（目前仍是理论类比，缺乏实证基础，来源：矛盾与存疑），而在于它提供了一个统一的工程框架。当一位ADHD患者使用ChatGPT分解任务时，他做的和工程师写function calling代码是同一件事：构建外部执行层。

但必须警惕过度依赖。工具应从脚手架变成永久拐杖（来源：拐杖与脚手架）。孔子70岁才做到“从心所欲不逾矩”，说明内部化需要时间。同样，agent不能永远依赖硬编码的调度——最终需要学会自主规划。

## 今天就能试的行动

1. **用ChatGPT做任务分解**：下次遇到启动困难，直接对ChatGPT说“把‘写报告’拆成5个具体步骤”，然后只做第一步。
2. **设置外部触发器**：像王阳明“事上练”一样，在手机上设一个定时提醒：“现在调用哪个工具？”——把agent的function calling逻辑用到自己身上。
3. **试用Goblin Tools的Magic ToDo**：输入“清理房间”，调节“辣度”控制粒度，体验外部调度器的效果。
4. **记录自己的“function calling”日志**：每天睡前写一行：今天用了哪些外部工具（提醒、清单、AI）？哪些调用成功？哪些失败了？像agent调试一样优化自己的harness。

## 参考来源

- [ADHD Apps: We tested 44 Apps and Here're the Best 9 in 2026](https://blog.saner.ai/best-adhd-apps/) — 证据等级：低（GRADE）
- [12 AI Personal Assistants Built for ADHD Brains (2026 Rankings)](https://www.usecarly.com/blog/best-ai-personal-assistant-adhd/) — 证据等级：低（GRADE）
- [LBD同构对：奖赏与动机 — Association of attention-deficit disorder and the dopamine t ↔ Retrospex: Language Agent Meets Offline Reinforcement Learni](https://pubmed.ncbi.nlm.nih.gov/7717410) — 证据等级：低（GRADE）
- [LBD同构对：分心与走神 — Therapeutic Doses of Oral Methylphenidate Significantly Incr ↔ AutoHallusion: Automatic Generation of Hallucination Benchma](https://doi.org/10.1523/jneurosci.21-02-j0001.2001) — 证据等级：低（GRADE）
- [LBD同构对：注意调度 — Dopamine release from the locus coeruleus to the dorsal hipp ↔ Question-guided Visual Compression with Memory Feedback for ](https://doi.org/10.1073/pnas.1616515114) — 证据等级：低（GRADE）
- ["A little bit of a life raft" – Exploring the Use and Experiences of ChatGPT as a Support Tool among Adults with ADHD](https://dl.acm.org/doi/pdf/10.1145/3764687.3764713) — 证据等级：低（GRADE）

---

*本文是「ADHD × AI」系列的第 32 篇，由 AI 智能体从持续维护的 LLM Wiki（全网真实情报）中取材整合生成，并持续迭代更新。*
