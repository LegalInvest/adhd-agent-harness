---
title: "为什么用 Claude 治 ADHD 的不知哪些方法有用，和给 agent 套 human-in-the-loop 监督 是一回事？"
subtitle: "Claude 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
description: "Claude 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
date: "2025-05-02"
category: "亲子教育"
categoryId: "parenting"
categoryEn: "Parenting & Education"
tags:
  - "ADHD"
  - "AI"
  - "亲子教育"
  - "反直觉同构"
readingTime: 11
slug: "为什么用-claude-治-adhd-的不知哪些方法有用和给-agent-套-human-in-the-loop-监督-是一回事"
topicId: "evolved-parenting-1759"
angle: "反直觉同构"
rank: 206
score: 7.71
sourceCount: 6
toolsCited:
  - "Goblin Tools"
  - "Saner.AI"
  - "Motion"
thesis: "ADHD 大脑与 LLM agent 本质上是同构的：两者都是高产生成核心但缺乏可靠执行调度层，因此有效的解决方案——对 ADHD 是外部脚手架，对 LLM 是 human-in-the-loop harness——在结构上完全对应，且都面临‘拐杖 vs 脚手架’的边界争议。"
problem: "为什么用 Claude 治 ADHD 的不知哪些方法有用，和给 agent 套 human-in-the-loop 监督 是一回事？"
spine: "人在回路与身体在场"
spineKind: ""
isEvolved: true
llmGenerated: true
caseStudies:
  - "张謇"
  - "孔子"
  - "Denise Stanley"
---
# 为什么用 Claude 治 ADHD 的不知哪些方法有用，和给 agent 套 human-in-the-loop 监督 是一回事？

> Claude 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。

你打开 Claude，想让它帮你制定一个每日计划。你输入“帮我安排今天的工作”，它立刻输出一个漂亮的清单。但第二天，你发现它忘了你的截止日期，把重要会议排到了午餐时间。你叹了口气，觉得 AI 还是“不够懂你”。

与此同时，你作为 ADHD 患者，每天也在经历类似的事：你的大脑像一台创意永动机，但执行功能——任务启动、时间管理、抑制冲动——总是掉链子。你试过无数方法：番茄钟、待办清单、身体在场，但总觉得“不知哪些方法有用”。

这两个问题，其实是同一个问题。

## 同构的困境：高产但不可靠的生成核心

ADHD 大脑与 LLM 共享一个核心特征：生成能力极强，但缺乏可靠的执行调度层。ADHD 个体在发散思维、创意、多任务并行上表现突出，但执行功能（任务启动、持续专注、抑制冲动）薄弱，导致“高产但不可靠”（来源：人在回路与身体在场）。LLM 同样如此：它能生成流畅的文本、代码、计划，但直接输出可能偏离目标、陷入循环或产生危险行为（来源：人在回路与身体在场）。

这意味着，对于 ADHD 和 LLM，解决方案不是“更强的生成能力”，而是“更好的外部调度”。

## 外部调度层：从 Goblin Tools 到 Agent Harness

ADHD 一侧的典型工具是 Goblin Tools 的 Magic ToDo：它将模糊任务（如“清理厨房”）分解为具体、可执行的子步骤，用户可调节“辣度”控制粒度（来源：Goblin Tools）。这降低了启动门槛，提供了即时反馈。Saner.AI 则通过增强知识回忆，减少搜索循环和标签切换（来源：Saner.AI）。Motion 更进一步，自动根据任务、会议和截止日期创建并动态调整每日计划，消除“下一步该做什么”的决策负担（来源：Motion）。

这些工具构成一个外部执行功能层：它们补偿了 ADHD 内在的执行功能缺陷，但有一个关键缺陷——传统提醒系统要求你主动设置提醒，而这本身就是一个执行功能任务（来源：重锚定与目标漂移）。

LLM/agent 一侧的对应方案是 agent harness（脚手架）。Harness 通过 human-in-the-loop 监督提供外部调度：设置护栏（token 预算、工具调用次数上限）、加入人工检查点（暂停并询问后再执行）（来源：人在回路与身体在场）。其核心是“形式化规划与护栏，使代理输出真正有用且正确”（来源：人在回路与身体在场）。

## 历史人物的 Harness：张謇与孔子

张謇（清末状元实业家）是 ADHD 特质的典型：41 岁中状元后辞官不做实业，冲动敢干，一生创办 20 多家企业、300 多所学校。他的专属 harness 是“父教育母实业”——用实业和教育救国，每天写日记反省，严格管理企业。这对应 LLM harness 中的“日课↔定时 re-grounding”和“秘书↔外部调度器”。

孔子同样如此：精力旺盛，周游列国 14 年，冲动爱骂人，思维跳跃，《论语》全是场景化语录。他的 harness 是“克己复礼”——用外在的“礼”作为行为边界，每日反省。70 岁才做到从心所欲不逾矩，一辈子和自己的冲动做斗争。

他们的 harness 系统与 LLM agent harness 同构：都是通过外部规则和检查点来约束和引导一个强大的生成核心。

## 脚手架 vs 拐杖：争议与边界

但这里有一个关键争议：AI 工具是“外部执行功能层”还是“拐杖”？过度依赖可能导致能力退化（来源：矛盾与存疑）。同样，LLM harness 如果过度约束，会扼杀模型的创造性；如果约束不足，又会导致输出失控。

我的判断是：脚手架与拐杖的边界在于**是否促进能力内化**。张謇的日课和孔子的“礼”最终内化为习惯；而单纯的提醒工具如果永远不减少使用频率，就可能成为拐杖。LLM harness 的设计也应如此：检查点应逐步减少频率，让模型学会自我校验。

## 今天就能试的行动

1. **用 Goblin Tools 分解一个你拖延的任务**：输入“写周报”，调节辣度到 3，执行第一步“打开文档”。
2. **给 Claude 设置一个“人工检查点”**：在关键步骤前要求它输出“确认继续？”，避免它直接执行。
3. **模仿张謇的日课**：每天固定时间向 AI 报告进度（来源：人在回路与身体在场），作为外部 accountability。
4. **反思你的工具是脚手架还是拐杖**：如果离开它你完全无法启动任务，尝试逐步减少使用频率。

ADHD 大脑和 LLM agent 的困境，本质上是同一个设计问题：如何让一个强大的生成核心变得可靠？答案不是压制生成，而是构建外部调度层。这个层可以是 Goblin Tools、Motion，也可以是 agent harness。关键在于，它必须是一个**可内化的脚手架**，而非永久的拐杖。

## 参考来源

- [ADHD Apps: We tested 44 Apps and Here're the Best 9 in 2026](https://blog.saner.ai/best-adhd-apps/)
- [12 AI Personal Assistants Built for ADHD Brains (2026 Rankings)](https://www.usecarly.com/blog/best-ai-personal-assistant-adhd/)
- [The 12 Best AI Tools for 2026 (That People Actually Use)](https://www.synthesia.io/post/ai-tools)
- [The AI Powered SuperApp for Work | Motion](https://www.usemotion.com/)
- [DeepSeek - AI Assistant - Apps on Google Play](https://play.google.com/store/apps/details?id=com.deepseek.chat)
- [AI Assistant for ADHD: Finally, a Productivity Tool That Requires Less...](https://get-alfred.ai/blog/ai-assistant-for-adhd)

---

*本文是「ADHD × AI」系列的第 206 篇，由 AI 智能体从持续维护的 LLM Wiki（全网真实情报）中取材整合生成，并持续迭代更新。*
