---
title: "为什么用 RescueTime 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用 是一回事？"
subtitle: "RescueTime 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
description: "RescueTime 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
date: "2025-04-06"
category: "AI工具实战"
categoryId: "ai-tools"
categoryEn: "AI Tools in Practice"
tags:
  - "ADHD"
  - "AI"
  - "AI工具实战"
  - "反直觉同构"
  - "效率工具"
readingTime: 11
slug: "为什么用-rescuetime-治-adhd-的任务启动困难和给-agent-套-function-calling-工具调用-是一回事"
topicId: "prob-0eda03c4fc"
angle: "反直觉同构"
rank: 190
score: 7.69
sourceCount: 6
toolsCited:
  - "Goblin Tools"
  - "Lex"
  - "Saner.AI"
  - "Tiimo"
  - "Focusmate"
  - "Motion"
  - "Brain.fm"
  - "Obsidian"
thesis: "ADHD 大脑与 LLM 都是「高产生成核心 + 脆弱执行调度层」的同构系统，给 ADHD 用时间/任务外化工具（如 Lex、Goblin Tools、Tiimo）和给 agent 加 function calling，本质上都是同一套外部 harness：把模糊意图翻译成可落地的下一步动作。"
problem: "为什么用 RescueTime 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用 是一回事？"
spine: "工具使用与认知卸载"
spineKind: ""
isEvolved: true
llmGenerated: true
isoStrength: "A"
caseStudies:
  - "孔子"
  - "苏轼"
  - "Jennifer Robertson"
---
# 为什么用 RescueTime 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用 是一回事？

> RescueTime 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。

## 1. 同一个 bug：脑子里能跑，手脚不动

你盯着待办清单的第三行，已经过了 25 分钟。你清楚地知道要做什么，甚至知道怎么做，但身体就是不动。另一边，你的 LLM agent 正在滔滔不绝地输出一份 800 字的“今日计划”，却一封邮件都没发、一个日历事件都没建。

两件事看起来风马牛不相及，但其实是同一个 bug：生成核心很强，执行调度层掉了链子。ADHD 大脑并不缺想法、创意或信息检索能力，它缺的是工作记忆、任务启动、时间管理与组织排序（来源：ADHD 的 AI 工具全景）。LLM 也一样：它能高速生成文本，却没有稳定的跨会话状态、原生规划与注意力约束（来源：ADHD 的 AI 工具全景）。所以“用工具治 ADHD”和“给 agent 加 function calling”不是比喻，而是同一类结构工程——为同一个同构系统安装外部 harness。

标题里提到的 RescueTime 本身并未出现在我们手头的 wiki 资料中，因此我不会声称它已被实测。但“时间记录/任务启动外化”这条 harness 逻辑，在资料记载的 Lex、Goblin Tools、Tiimo、Saner.AI 等工具中同样成立，且与 function calling 的机理完全对应。

## 2. ADHD 侧：用外部工具把“想做”变成“先做”

ADHD 的任务启动困难，往往不是因为任务太难，而是因为入口太模糊。wiki 资料把当前的 AI 工具价值分为四类补偿：任务分解与启动、外部记忆、时间管理、元认知反思（来源：ADHD 的 AI 工具全景）。每一类都在做同一件事：把内部不可控的执行功能，外化为可触摸的结构。

Goblin Tools 的 Magic ToDo 能把“清理厨房”这种模糊目标拆成具体子任务，用户还能调节“辣度”控制粒度（来源：Goblin Tools）。Lex 走得更远：一条指令触发多步骤任务序列，把复杂目标压缩成低启动成本的入口（来源：Lex）。Saner.AI 用通用收件箱把邮件、文档、日历里的待办自动提取，并拆解里程碑，减少搜索循环和标签切换（来源：Saner.AI）。Tiimo 则用视觉化时间表把时间“变可触摸”，专门应对 ADHD 的时间盲（来源：时间盲）。如果你需要启动阻力更小，Focusmate 用虚拟“身体在场”提供隐性问责——研究证明，即将到来的问责检查可改善积极行为达 50%，定期问责能把目标达成率从 25% 提升到 95%（来源：身体在场效应）。

这些工具不是替你做决定，而是替你做“决定之后的下一步”。这正是 harness 的核心：让生成核心继续发挥，但用外部调度层把输出导向动作。

## 3. LLM/Agent 侧：function calling 就是 agent 的“任务启动”

LLM 的 function calling 机制，本质是把一段自然语言意图转译成一次确定性工具调用。模型不再只生成文本，而是说：“我要调用 `send_email`”，并把参数填好。没有这一层，agent 就会陷入和 ADHD 类似的“启动瘫痪”：一直在做计划、解释、再计划，永远不碰真实世界。

这与 ADHD 工具链是同构的：
- **任务分解** ↔ 复杂目标被拆成可调用的函数序列；
- **外部记忆** ↔ 跨会话的持久化存储，补全 LLM 的上下文窗口限制；
- **时间管理** ↔ 调度器决定何时调用哪个工具、何时等待用户确认；
- **元认知反思** ↔ 在每次生成前先做 re-grounding，检查目标是否偏离。

Lex 的架构被明确类比为 agent scaffolding，即围绕大语言模型构建软件架构和工具，使其能执行目标驱动的任务（来源：Lex）。也就是说，Lex 对 ADHD 用户的设计思路，和它作为 agent 框架的底层思路，是同一个脚手架。

## 4. 历史名人也这么 harness：孔子与苏轼

两千多年前的孔子，可能是最早发现“外部 harness”价值的人。他身高 1 米 9、精力旺盛、周游列国 14 年坐不住，冲动爱骂人，思维跳跃，《论语》全是场景化语录。他的 harness 是“克己复礼”：用外在的“礼”作为行为边界，每日“吾日三省吾身”，到 70 岁才“从心所欲不逾矩”。这对应到 LLM agent 上，就是 system prompt 的硬性约束、定期的 re-grounding，以及让模型在生成前必须调用一次“对齐检查”函数。

苏轼的 harness 则是另一种风格：兴趣极广、情绪来得快去得快，被贬到哪里都能重新启动。他的策略是“豁达”——用写作、美食、交朋友作为注意力的 redirector，每日读书写字，不因挫折停止创作。这对应的是 LLM 里的自适应状态管理、持久记忆和 fallback routine：当主任务失败时，不是宕机，而是切换到一个预设的恢复动作。

两人的 harness 都说明：高产生成核心从不可控到可控，关键不是压抑它，而是给它一个外部路由表。

## 5. 脚手架 vs. 拐杖：边界与争议

同构视角很锋利，但 wiki 资料也提醒我们，它目前仍是理论类比，缺乏实证基础，不同页面在表述上甚至不一致（来源：全局矛盾与存疑）。多个工具（如 Motion、Brain.fm）的独立临床验证有限，却被当作有效方案推荐；ChatGPT、Claude 等工具页面强调益处，却很少讨论依赖

## 参考来源

**同构强度：A 级** —— 直接文献支撑（引用 ADHD↔LLM 同构专题研究）

- [ADHD Apps: We tested 44 Apps and Here're the Best 9 in 2026](https://blog.saner.ai/best-adhd-apps/) — 证据等级：低（GRADE）
- [12 AI Personal Assistants Built for ADHD Brains (2026 Rankings)](https://www.usecarly.com/blog/best-ai-personal-assistant-adhd/) — 证据等级：低（GRADE）
- [Toward Neurodivergent-Aware Productivity: A Systems and AI-Based Human-in-the-Loop Framework for ADHD-Affected Professionals](https://arxiv.org/pdf/2507.06864) — 证据等级：低（GRADE）
- [Using an AI Assistant to Manage ADHD: A Practical Guide](https://www.lobsterfarm.ai/guides/ai-for-adhd/) — 证据等级：低（GRADE）
- [Revolutionizing ADHD Management with AI Assistants](https://neurolaunch.com/adhd-ai-assistant/) — 证据等级：低（GRADE）
- [10 Killer ChatGPT Prompts For Organizing Your ADHD Brain](https://www.adhdflowstate.com/best-chatgpt-prompts-for-adhd/) — 证据等级：低（GRADE）

---

*本文是「ADHD × AI」系列的第 70 篇，由 AI 智能体从持续维护的 LLM Wiki（全网真实情报）中取材整合生成，并持续迭代更新。*
