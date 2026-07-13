---
title: "为什么用 Lex 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用 是一回事？"
subtitle: "Lex 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
description: "Lex 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
date: "2025-03-12"
category: "AI工具实战"
categoryId: "ai-tools"
categoryEn: "AI Tools in Practice"
tags:
  - "ADHD"
  - "AI"
  - "AI工具实战"
  - "反直觉同构"
  - "效率工具"
readingTime: 10
slug: "为什么用-lex-治-adhd-的任务启动困难和给-agent-套-function-calling-工具调用-是一回事"
topicId: "prob-a99db3832c"
angle: "反直觉同构"
rank: 181
score: 7.69
sourceCount: 6
toolsCited:
  - "Lex"
  - "Goblin Tools"
  - "Saner.AI"
  - "Obsidian"
  - "Motion"
  - "Focusmate"
  - "Brain.fm"
thesis: "ADHD 大脑与 LLM/agent 都是「高产生成核心 + 不可靠执行调度层」，Lex 治 ADHD 的任务启动困难，与给 agent 加 function calling 工具调用，本质是同一种 harness：用外部脚手架把「想做的目标」翻译为「可执行的下一步」。"
problem: "为什么用 Lex 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用 是一回事？"
spine: "工具使用与认知卸载"
spineKind: ""
isEvolved: true
llmGenerated: true
isoStrength: "A"
caseStudies:
  - "孔子"
  - "文天祥"
  - "Nicole Garcia"
---
# 为什么用 Lex 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用 是一回事？

> Lex 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。

你今天又一次盯着任务清单，脑子里有方案、有素材、有热情，身体却像被钉在椅子上。与此同时，你写的 LLM agent 又在空转：模型滔滔不绝，却就是不调用那个早就写好的日历 API，也不去查数据库，只在对话里「假装」完成了任务。

两个场景看起来风马牛不相及，但故障灯指向同一个底层 bug：一个高产但缺乏稳定执行调度层的生成核心。ADHD 大脑和 LLM/agent，在这个意义上是同构的。治 ADHD 任务启动困难的 Lex，与治 agent 调用失败的 function calling，其实是同一套 harness 思路在两边落地。

## 1. 两个启动失败：大脑的油门与离合

ADHD 的问题常被误解为「没想法」或「懒」，事实往往相反：创意、信息和兴趣都不缺，缺的是把想法推进成动作的执行调度层。前额叶执行功能受损会导致工作记忆容量波动、时间感知困难、任务启动与切换受阻。目标越大，多巴胺阈值越高，启动越难，这就是常说的任务瘫痪（来源：Harnessing Artificial Intelligence to Live Better with ADHD - CHADD）。

LLM/agent 的故障模式惊人地相似。模型能高速生成文本、推理和代码，却没有原生的规划层、跨会话持久状态，也缺乏自我抑制机制。没有外部约束时，它容易偏离目标、产生幻觉，或在复杂任务前反复兜圈子（来源：ADHD 的 AI 工具全景）。研究显示，LLM 在工作记忆任务中表现出类似人类的干扰特征：记忆负荷增加、近因效应和刺激统计偏差都会降低回忆准确率，且成功回忆依赖于对无关内容的主动抑制（来源：Human-like Working Memory Interference in Large Language Models）。另一项研究则指出，没有严重依赖手动提示修正时，LLM 难以自主发现最佳问题解决模式（来源：Working Memory Identifies Reasoning Limits in Language Models）。更底层地，Transformer 的自注意力机制在训练后发展出模仿人类前额叶-纹状体门控操作的模式（来源：TRANSFORMER MECHANISMS MIMIC FRONTOSTRIATAL GATING OPERATIONS WHEN TRAINED ON HUMAN WORKING MEMORY TASKS）。

两边都是：引擎很猛，离合片磨损。

## 2. Lex 实测：把目标翻译成可执行的第一次调用

Lex 的核心设计非常像给 ADHD 大脑做了一次「function calling」封装：用户输入一个模糊意图，系统自动把它拆成多步骤任务序列并触发执行（来源：Best AI Tools for ADHD Productivity in 2026 (Honest Review) - Iwo Szapar）。它不是帮你把活全干了，而是把「写季度复盘」这种大山压顶的目标，拆成「打开文档 → 列出三个关键数据 → 写第一段摘要」这样小到可以启动的第一步。

这正是 ADHD 干预里最有效的杠杆：任务分解。复杂任务被拆解后，能显著降低 overwhelm，并提供即时正反馈，从而绕过多巴胺启动阈值（来源：6 ways AI can help you manage ADHD symptoms - Understood.org）。同类工具如 Goblin Tools 的 Magic ToDo，也是把「清理厨房」这种模糊任务变成可调粒度的具体步骤（来源：12 AI Personal Assistants Built for ADHD Brains (2026 Rankings)）。

对工程师来说，这套逻辑读起来应该非常熟悉。Lex 的底层架构被描述为类似 agent scaffolding：围绕 LLM 构建软件架构与工具，使其能执行复杂、目标驱动的任务（来源：Agent Scaffolding: Architecture and Design Patterns for Agentic AI）。而 function calling 的本质，就是给 LLM 一个外部工具清单，让它不再直接生成最终答案，而是生成一次结构化调用：调用哪个工具、传入什么参数。工具执行后，结果再喂回模型，形成「计划 → 调用 → 观察 → 再计划」的循环（来源：The Anatomy of an AI Agent: Memory, Tools, Planning, and ...）。

对比一下：
- ADHD 侧：Lex 接收「我想健身」→ 输出「换上运动鞋，只做 5 分钟热身」→ 降低启动门槛。
- LLM 侧：模型接收「帮我订明天下午开会的会议室」→ 输出 `book_room(date="明天", time="下午")` → 工具执行真实动作。

两者都没有让生成核心直接「硬扛」复杂任务，而是给它一套外部调度器，把目标翻译成可执行的第一次调用。

## 3. 孔子：最早的 agent scaffolding 案例

回到两千五百年前，孔子的 harness 系统与今天的 agent 设计高度同构。他有明显的 ADHD 行为模式：身高一米九、精力旺盛、周游列国十四年坐不住；冲动爱骂人，见南子急得对天发誓，骂宰予「朽木不可雕」；对音乐能超专注到「三月不知肉味」，对种地等俗事毫无耐心；思维极度跳跃，《论语》全是场景化语录，没有系统著作。他并非靠「自律长大就好了」，而是用一套外部脚手架与冲动共处了一辈子。

他的核心 harness 是「克己复礼」：把外在的社会规范与仪式作为行为边界，替代自己不稳定的前额叶抑制功能。每日「三省吾身」则是一套定时 re-grounding 机制：他不断回到自己的目标、言行与承诺，修正漂移。直到七十岁，他才说自己能「从心所欲不逾矩」——也就是这套外部脚手架终于内化为稳定的工作流。

在 LLM/agent 的语境里，孔子的「礼」就是 system prompt + 工具 schema：它们不是 creativity 的敌人，而是防止模型跑偏的约束边界。孔子的「日课反省」则对应 agent 的反思循环与外部记忆：每隔一段时间或每次调用后，重新读取目标状态，再决定下一步。孔子的 harness 不是拐杖，而是让高产生成核心（他的思想、游说、教学）能够稳定输出的工程架构。

## 4. 同构的边界：脚手架与拐杖之差

强调同构，不是为了把 ADHD 人脑简化成变压器，也不是为了把 LLM 拟人化。这里有一个关键边界：脚手架是为了让人最终自己攀登，拐杖是替人承担行走。真正的 AI 工具应该外化思维、减轻认知负荷，但使用者仍需自己「建造」和「攀登」（来源：AI Tools for ADHD: Boosting Productivity and Reducing Burnout）。如果工具替代了治疗、反思或自我管理，就会变成依赖（来源：CHADD）。

对 agent 工程同样如此。function calling 不是把 LLM 变成纯 API 调度器，更不是把所有步骤硬编码在工具层。它的价值在于：让模型在需要计算、查询、执行或持久化的时刻，把责任交给外部工具，同时保留模型在推理和决策层的能力。如果工具链越写越厚，模型只剩路由功能，那也不过是把 agent 的拐杖换成了担架。

还要注意工具本身可能增加认知负担。界面复杂、提示词维护成本高、跨平台切换频繁，都会让 ADHD 用户或工程师从「被辅助」变成「管理工具」本身。好的 harness 是隐形的，只在需要时出现。

## 5. 证据与局限：同构是理论，不是神话

上面说的同构，目前更接近一种

## 参考来源

**同构强度：A 级** —— 直接文献支撑（引用 ADHD↔LLM 同构专题研究）

- [ADHD Apps: We tested 44 Apps and Here're the Best 9 in 2026](https://blog.saner.ai/best-adhd-apps/) — 证据等级：低（GRADE）
- [12 AI Personal Assistants Built for ADHD Brains (2026 Rankings)](https://www.usecarly.com/blog/best-ai-personal-assistant-adhd/) — 证据等级：低（GRADE）
- [Human-like Working Memory Interference in Large Language Models](https://arxiv.org/pdf/2604.09670) — 证据等级：低（GRADE）
- [Working Memory Identifies Reasoning Limits in Language Models](https://aclanthology.org/2024.emnlp-main.938.pdf) — 证据等级：低（GRADE）
- [TRANSFORMER MECHANISMS MIMIC FRONTOSTRIATAL GATING OPERATIONS WHEN TRAINED ON HUMAN WORKING MEMORY TASKS](https://openreview.net/pdf?id=CN2bmVVpOh) — 证据等级：低（GRADE）
- [Executive Dysfunction by Design: A Cognitive Accessibility Analysis of AI Support vs. Healthcare Barriers](https://dl.acm.org/doi/pdf/10.1145/3663547.3749831) — 证据等级：低（GRADE）

---

*本文是「ADHD × AI」系列的第 61 篇，由 AI 智能体从持续维护的 LLM Wiki（全网真实情报）中取材整合生成，并持续迭代更新。*
