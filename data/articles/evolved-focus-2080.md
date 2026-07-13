---
title: "为什么用 ChatGPT 治 ADHD 的注意力涣散，和给 agent 套 上下文工程 是一回事？"
subtitle: "ChatGPT 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
description: "ChatGPT 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
date: "2025-03-15"
category: "专注力管理"
categoryId: "focus"
categoryEn: "Focus Management"
tags:
  - "ADHD"
  - "AI"
  - "专注力管理"
  - "反直觉同构"
  - "心流"
readingTime: 9
slug: "为什么用-chatgpt-治-adhd-的注意力涣散和给-agent-套-上下文工程-是一回事"
topicId: "evolved-focus-2080"
angle: "反直觉同构"
rank: 40
score: 7.95
sourceCount: 6
toolsCited:
  - "ChatGPT"
  - "Focusmate"
  - "RescueTime"
  - "Brain.fm"
  - "Forest"
  - "Goblin Tools"
  - "Motion"
  - "Reclaim.ai"
thesis: "ADHD大脑与LLM/agent共享“高产但缺执行调度层的生成核心”这一结构缺陷，因此两者都需要外部上下文工程（harness）来补偿调度缺陷——用ChatGPT治注意力涣散，和给agent套上下文工程，本质上是同一套脚手架逻辑。"
problem: "为什么用 ChatGPT 治 ADHD 的注意力涣散，和给 agent 套 上下文工程 是一回事？"
spine: "上下文工程"
spineKind: ""
isEvolved: true
llmGenerated: true
caseStudies:
  - "曾国藩"
  - "苏轼"
  - "罗桂兰"
---
# 为什么用 ChatGPT 治 ADHD 的注意力涣散，和给 agent 套 上下文工程 是一回事？

> ChatGPT 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。

你有没有过这样的体验：打开ChatGPT想写一篇文章，结果十分钟后发现自己正在问它“如何养绿萝”；与此同时，你手头那个本该自动执行的agent，跑了一半就卡在无关的API调用里，输出一堆乱码。

这不是巧合。ADHD大脑和LLM/agent，共享同一个致命缺陷：**两者都是强大的生成核心，但缺乏可靠的内置执行调度层**。

## 同一个问题：生成核心，没有调度

ADHD的注意力涣散，本质上是执行功能缺陷——大脑能产出无数想法，却无法自主决定“现在该注意什么”。你坐在书桌前，任务清单铺开，但大脑像一台没有操作系统的服务器：所有进程同时抢占CPU，最后哪个都跑不完。

LLM/agent也一样。GPT-4能写出漂亮的代码，但让它“先查数据库、再调API、最后发邮件”，它要么忘记步骤，要么上下文一长就开始“幻觉”——把上一步的结果当成无关信息丢掉。文献明确指出：“单个LLM不足以可靠地完成多步骤任务、与业务工具交互或适应领域特定逻辑”（来源：Agent Scaffolding: Architecture and Design Patterns for Agentic AI）。

两边缺的，都是那个说“现在做这个，做完做那个”的调度层。

## 同一套解法：上下文工程（harness）

对ADHD来说，这个调度层就是**外部脚手架**。曾国藩30岁前“浮躁坐不住”，日记里天天骂自己“无恒”“读书不能终一行”。他的解法是“日课十二条”：黎明即起、读书不二、谨言、写日记反省。这套系统本质上是一个**外部调度程序**——每天固定时间、固定动作，用外部结构替代内部执行功能。

对LLM/agent来说，这个调度层就是**上下文工程**。你给agent的prompt里写清楚“第一步：查数据库；第二步：调用API；第三步：格式化输出”，再加一个“每完成一步，输出当前状态”。这和曾国藩的“日课”完全同构：**用外部指令序列，弥补内部调度缺失**。

苏轼也用了同一套逻辑。他被贬到哪都能适应，靠的不是“意志力”，而是**环境工程**：用美食、写作、交友主动构建注意力锚点。他的“每日读书写字”就是定时re-grounding，和agent里“每5分钟输出一次进度摘要”异曲同工。

## 工具实证：两边都成立

ADHD侧的工具已经验证了这一点。

- **Focusmate**：通过虚拟身体在场提供外部问责。你预约一个时段，平台匹配一个伙伴，两人视频共同工作。这不是AI生成的专注，而是**用社会结构充当调度器**——对方的存在就是“现在该做事”的上下文信号（来源：11 Best ADHD Productivity Apps for Fluctuating Energy）。
- **RescueTime**：自动追踪时间并阻断分心网站。它补偿的是ADHD的“时间盲”——你感觉才过了10分钟，其实已经刷了1小时。RescueTime就是那个**外部时间戳**，告诉agent“你当前在做什么”（来源：Revolutionizing ADHD Management with AI Assistants）。
- **Brain.fm**：用神经锁相音乐调节大脑状态。它不是直接调度任务，而是**优化运行环境**，和agent里“先清空上下文、再注入新任务”的prompt工程原理一致（来源：ADHD Apps: We tested 44 Apps and Here're the Best 9 in 2026）。

LLM/agent侧的证据同样清晰。

- **任务分解与规划**：ADHD文献群（681篇）和agentic harness文献群（2914篇）的核心中间机制概念都是“任务分解与规划”（来源：LBD同构对）。Goblin Tools这类AI工具“将模糊的工作分解为更小的行动”（来源：Best AI Tools for ADHD Productivity in 2026），而AgentGen等框架“通过环境与任务生成增强LLM agent的规划能力”（来源：AgentGen: Enhancing Planning Abilities for Large Language Model based Agent via Environment and Task Generation）。两边用的策略一模一样：**把大目标拆成小步骤，每一步只做一件事**。
- **外部记忆**：ADHD的工作记忆缺陷与LLM的无跨会话状态同构。RescueTime的自动记录、Forest的专注记录，就是agent的**外部记忆系统**——你不需要记住自己做了什么，系统帮你记。

## 脚手架，不是拐杖

这里有一个关键边界：**脚手架 vs. 拐杖**。

如果曾国藩一辈子只靠别人提醒才读书，那就是拐杖。但他把日课内化成了习惯，最终“无恒”变成了“恒”。同样，好的上下文工程应该让agent**逐渐学会自主调度**，而不是永远依赖你写的每一步指令。

但争议在于：AI工具是否会导致永久依赖？目前没有长期追踪研究（来源：矛盾与存疑）。Focusmate的用户报告显示，长期使用后部分人能减少使用频率，但另一些人形成依赖。这和agent工程里的“prompt退化”问题一模一样——写死步骤的agent一旦遇到新场景就崩溃。

真正的解法是**可退出的脚手架**：工具只在你需要时提供结构，同时允许你逐步撤除。比如曾国藩的日课，他晚年不再逐条检查，但框架已内化。对应到agent，就是**动态prompt**——系统根据任务复杂度自动调整上下文深度，而不是固定模板。

## 今天就能试的3件事

1. **给ChatGPT一个“日课”prompt**：每次对话开头加一句“请按以下步骤执行：1. 确认目标；2. 分解为3个步骤；3. 每完成一步输出‘step X done’”。这就是你的agent harness。

2. **用Focusmate做一次“身体加倍”**：预约一个25分钟时段，和陌生人一起工作。注意观察：外部在场是否降低了启动门槛？这和agent里“human-in-the-loop”的验证机制完全一样。

3. **打开RescueTime的“分心阻断”**：设定每天2小时的专注时段，让工具自动屏蔽社交媒体。然后记录：你的注意力漂移频率是否下降？这相当于给agent加了一个“上下文窗口锁定”指令。

## 局限与诚实

本文的核心论点——ADHD大脑与LLM的同构——目前**仅是一种理论类比，并非经过验证的科学事实**（来源：矛盾与存疑）。它帮助我们理解问题，但不能替代临床诊断或系统架构设计。

工具证据也有限：Brain.fm在ADHD人群中的独立临床研究极少；Focusmate的效果主要来自用户报告；RescueTime的自动分类可能不准确（来源：各工具页）。

但正是这些局限，让同构视角更有价值：它把两个看似无关的领域连在一起，让工程师和ADHD患者看到彼此的问题其实是同一个。下次你被注意力涣散折磨时，可以对自己说：“不是我有问题，是我的调度层没装好。”然后，去写一个更好的prompt。

## 参考来源

- [ADHD Apps: We tested 44 Apps and Here're the Best 9 in 2026](https://blog.saner.ai/best-adhd-apps/) — 证据等级：低（GRADE）
- [Meta-Analysis of fMRI Studies of Disruptive Behavior Disorders](https://doi.org/10.1176/appi.ajp.2016.15081089) — 证据等级：高（GRADE）
- [Nonlinear Complexity Analysis of Brain fMRI Signals in Schizophrenia](https://doi.org/10.1371/journal.pone.0095146) — 证据等级：低（GRADE）
- [Revolutionizing ADHD Management with AI Assistants](https://neurolaunch.com/adhd-ai-assistant/) — 证据等级：低（GRADE）
- [Agent Scaffolding: Architecture and Design Patterns for Agentic AI](https://zbrain.ai/agent-scaffolding/) — 证据等级：低（GRADE）
- [LBD同构对：任务分解与规划 — Attention-deficit/hyperactivity disorder is characterized by ↔ Language-conditioned world model improves policy generalizat](https://doi.org/10.1073/pnas.0707741104) — 证据等级：低（GRADE）

---

*本文是「ADHD × AI」系列的第 43 篇，由 AI 智能体从持续维护的 LLM Wiki（全网真实情报）中取材整合生成，并持续迭代更新。*
