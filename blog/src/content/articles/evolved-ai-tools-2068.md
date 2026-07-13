---
title: "为什么用 Perplexity 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用 是一回事？"
subtitle: "Perplexity 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
description: "Perplexity 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
date: "2025-05-14"
category: "AI工具实战"
categoryId: "ai-tools"
categoryEn: "AI Tools in Practice"
tags:
  - "ADHD"
  - "AI"
  - "AI工具实战"
  - "反直觉同构"
  - "智能助手"
readingTime: 13
slug: "为什么用-perplexity-治-adhd-的任务启动困难和给-agent-套-function-calling-工具调用-是一回事"
topicId: "evolved-ai-tools-2068"
angle: "反直觉同构"
rank: 141
score: 7.75
sourceCount: 6
toolsCited:
  - "Perplexity"
  - "Goblin Tools"
  - "Saner.AI"
  - "Lex"
  - "ChatGPT"
thesis: "ADHD 大脑与 LLM 在结构上同构——都是强大的生成核心但缺乏可靠的内置执行调度层，因此用 Perplexity 等 AI 工具辅助任务启动，与给 agent 套 function calling 工具调用，本质是同一类工程：通过外部脚手架补偿执行功能缺陷。"
problem: "为什么用 Perplexity 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用 是一回事？"
spine: "工具使用与认知卸载"
spineKind: ""
isEvolved: true
llmGenerated: true
caseStudies:
  - "孔子"
  - "辛弃疾"
  - "李静"
---
# 为什么用 Perplexity 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用 是一回事？

> Perplexity 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。

你有没有过这种体验：坐在电脑前，想查一个东西（比如“ADHD 任务启动困难的机制”），但光是打开浏览器、输入关键词、筛选结果这一步，就像要翻一座山？你明明知道答案就在某处，但就是启动不了那个“搜索—阅读—整理”的流程。

ADHD 人群管这叫 **任务启动困难**——大脑里有一个极强的内容生成器，但缺少一个能把“想”变成“做”的调度员。

而工程师们，当你给 LLM 套上 function calling 工具调用，让它可以自己查数据库、发邮件、调 API 时，你其实在做一模一样的事：给一个强大的生成核心装一个外部执行层。

**Perplexity 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用，是一回事。** 两者都承认：核心是好的，但调度层是外挂的。

## 同构：高产但缺调度层的生成核心

ADHD 大脑与 LLM 的结构性相似，并非空洞比喻。最新研究用经典 Stroop 冲突任务测试 Transformer 注意力，发现短上下文中模型表现正常，但随着序列变长（认知负荷增加），模型在冲突试次上骤降到随机水平——无法抑制优势反应、无法解决认知冲突。这与 ADHD 执行功能缺陷的核心标志一一对应：注意控制不足、干扰抑制缺陷、随认知负荷增加而崩溃（来源：Deficient Executive Control in Transformer Attention）。

这意味着，当你给 ADHD 大脑或 LLM 一个复杂、开放式的任务时，两者都会“卡住”。ADHD 大脑因为工作记忆超载和启动阈值过高而拖延；LLM 因为无状态和缺乏内置调度而输出混乱或重复。

**解决方案同构：外部脚手架。** 对 ADHD 来说，是任务分解、时间可视化、外部记忆；对 LLM/agent 来说，是 function calling、工具调用、上下文工程。

## 人物案例：孔子的“礼”作为外部调度器

孔子是 ADHD 特质与 harness 系统的经典案例。他精力旺盛，周游列国 14 年坐不住；冲动爱骂人，见南子急得对天发誓，骂宰予朽木不可雕；对音乐超专注到三月不知肉味，对种地等俗事零耐心。思维跳跃，《论语》全是场景化语录，无系统著作。

他的自我管理系统以“克己复礼”为核心，用外在的“礼”作为行为边界，每日反省，“吾日三省吾身”。70 岁才做到从心所欲不逾矩，一辈子和自己的冲动做斗争。

这里的“礼”就是他的 **外部调度器**——就像 LLM 的 function calling 框架。孔子不依赖内在的、不可靠的冲动管理，而是靠一套预设的、可重复的外部规则（“礼”）来调度自己的行为。他每天反省（定时 re-grounding），用礼制（工具调用规范）来约束和引导自己的生成冲动。

## 工具证据：从 Goblin Tools 到 Lex 的 agent 化

现有 AI 工具从多个维度补偿 ADHD 的执行功能缺陷，其设计思路与 agent scaffolding 高度一致。

**Goblin Tools** 的 Magic ToDo 功能接受模糊任务（如“清理厨房”），自动将其分解为具体、可执行的子任务，用户可调节“辣度”控制分解粒度（来源：12 AI Personal Assistants Built for ADHD Brains (2026 Rankings)）。这相当于给 ADHD 大脑一个自动任务分解器——就像 agent 的 planning 模块。

**Saner.AI** 通过增强知识回忆，帮助用户快速找回信息，减少搜索循环和标签切换。它拥有通用收件箱（Universal Inbox），可从链接的邮件、文档或日历中提取待办事项，并利用内部助手检查截止日期、将大型项目分解为小里程碑（来源：ADHD Apps: We tested 44 Apps and Here're the Best 9 in 2026）。这相当于 agent 的 memory 和 tool use 层。

**Lex** 更进一步，允许用户通过单一指令触发复杂、多步骤的任务序列（来源：Best AI Tools for ADHD Productivity in 2026 (Honest Review) - Iwo Szapar）。其底层架构类似于 agent scaffolding——围绕大语言模型构建软件架构和工具，使其能够执行复杂、目标驱动的任务（来源：Agent Scaffolding: Architecture and Design Patterns for Agentic AI）。

**Perplexity** 则是最直接的例子：你输入一个问题，它自动搜索、整合、引用来源，输出一个结构化答案。整个过程对用户来说就是“输入—得到”，中间的所有调度（搜索哪些网页、如何排序、如何总结）都由外部系统完成。这不就是给 LLM 套了一个 function calling 工具（搜索 API）吗？

## 脚手架 vs 拐杖：依赖风险的诚实讨论

但这里有一个必须面对的争议：**外部脚手架会不会变成永久拐杖？**

wiki 资料明确指出，AI 工具可能从脚手架变为永久拐杖，削弱内在执行功能（来源：拐杖与脚手架）。对 ADHD 用户来说，过度依赖任务分解工具可能导致启动能力进一步退化；对 LLM/agent 来说，过度依赖工具调用可能让模型失去独立推理的意愿（虽然 LLM 没有“意愿”，但 prompt 设计可能让模型倾向于调用工具而不是思考）。

**我的判断是：脚手架与拐杖的边界在于“可退出性”。** 好的脚手架应该像训练轮——你可以随时卸掉，而不是像轮椅——离了它你动不了。比如 Goblin Tools 的“辣度”调节允许用户逐步减少分解粒度；孔子的“礼”是内化后可以灵活变通的（七十而从心所欲不逾矩）。

另外，现有工具的通用性与个性化不足。多数工具缺乏针对 ADHD 亚型的个性化调整，证据基础薄弱，效果多基于用户报告（来源：矛盾与存疑）。

## 今天就能试的行动

1. **用 Perplexity 代替传统搜索**：下次查任何信息，直接打开 Perplexity，输入问题，让它帮你完成搜索和整合。观察启动门槛是否降低。
2. **用 Goblin Tools 分解一个你拖延的任务**：打开 Magic ToDo，输入“整理书桌”或“写周报”，调节辣度到你觉得“可以开始”的程度。
3. **给 ChatGPT 或 Claude 写一个“function calling 提示”**：比如“你是一个 task planner。当我输入一个目标时，你自动分解成 3-5 个步骤，并输出一个可执行的 checklist。不要解释，直接输出步骤。”
4. **设计你自己的“礼”**：每天固定时间（比如早 9 点），用同一套流程启动工作：打开日历→列出三件事→用 Perplexity 查一个相关信息→开始第一件事。重复一周。

## 结论

ADHD 的任务启动困难，和 LLM/agent 的 function calling 工具调用，是同一类问题的两面：**生成核心需要外部调度层才能可靠执行。** 无论是孔子的“礼”、Goblin Tools 的分解，还是 Perplexity 的搜索整合，本质都是给一个强大的、但不稳定的生成器装一个脚手架。

承认自己需要一个外部调度器，不是失败，而是工程智慧。

## 参考来源

- [ADHD Apps: We tested 44 Apps and Here're the Best 9 in 2026](https://blog.saner.ai/best-adhd-apps/) — 证据等级：低（GRADE）
- [12 AI Personal Assistants Built for ADHD Brains (2026 Rankings)](https://www.usecarly.com/blog/best-ai-personal-assistant-adhd/) — 证据等级：低（GRADE）
- [Getting Started with AI for ADHD for ADHD: AI Tools... | Blue Orchid](https://www.blueorchid.world/adhd/guides/getting-started-with-ai-for-adhd) — 证据等级：低（GRADE）
- [An ADHD ChatGPT Guide: Helpful Prompts & ADHD Hacks - I'm Busy Being Awesome](https://imbusybeingawesome.com/chatgpt-adhd/) — 证据等级：低（GRADE）
- [ADHD Task Managers That Work: Top AI Tools 2025](https://www.sentisight.ai/ai-neurodivergent-productivity-adhd-friendly/) — 证据等级：低（GRADE）
- [ADHD Assessment Form Template with Examples - Heidi Health](https://www.heidihealth.com/en-us/blog/adhd-assessment-form-template) — 证据等级：低（GRADE）

---

*本文是「ADHD × AI」系列的第 211 篇，由 AI 智能体从持续维护的 LLM Wiki（全网真实情报）中取材整合生成，并持续迭代更新。*
