---
title: "为什么用 Perplexity 治 ADHD 的时间盲，和给 agent 套 planner-executor 任务分解 是一回事？"
subtitle: "Perplexity 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
description: "Perplexity 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
date: "2025-03-05"
category: "时间管理"
categoryId: "time-mgmt"
categoryEn: "Time Management"
tags:
  - "ADHD"
  - "AI"
  - "时间管理"
  - "反直觉同构"
  - "拖延"
readingTime: 9
slug: "为什么用-perplexity-治-adhd-的时间盲和给-agent-套-planner-executor-任务分解-是一回事"
topicId: "evolved-time-mgmt-1631"
angle: "反直觉同构"
rank: 291
score: 7.68
sourceCount: 6
toolsCited:
  - "Perplexity"
  - "Motion"
  - "Reclaim.ai"
  - "Tiimo"
  - "Todoist"
  - "Obsidian"
thesis: "ADHD 大脑与 LLM 是同一类高产生成核心，都缺乏内置执行调度层，因此用 Perplexity 等 AI 工具辅助时间管理，本质上和给 agent 套 planner-executor 任务分解结构是同一种工程——都是为生成核心搭建外部脚手架。"
problem: "为什么用 Perplexity 治 ADHD 的时间盲，和给 agent 套 planner-executor 任务分解 是一回事？"
spine: "规划循环与任务分解"
spineKind: ""
isEvolved: true
llmGenerated: true
caseStudies:
  - "孔子"
  - "辛弃疾"
  - "Jordan York"
---
# 为什么用 Perplexity 治 ADHD 的时间盲，和给 agent 套 planner-executor 任务分解 是一回事？

> Perplexity 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。

## 一个反直觉的问题：为什么用 Perplexity 治 ADHD 的时间盲，和给 agent 套 planner-executor 任务分解是一回事？

如果你既被时间盲折磨，又做过 Agentic Harness 工程，你可能会觉得这两个世界毫不相关。但一个反直觉的同构正在浮现：ADHD 大脑与大型语言模型（LLM）在结构上高度相似——二者都是高产生成核心，却缺乏可靠的内置执行调度层（来源：AI 与 ADHD 的时间管理）。这意味着，你为 ADHD 搭建的“执行功能支架”和你为 LLM 设计的“planner-executor 任务分解”，本质上是同一类工程。

### 时间盲与无状态：同构的起点

ADHD 的典型痛点是时间盲——无法感知时间流逝，难以预估任务时长，常常陷入“现在几点了？我刚才在干什么？”的困境。这对应 LLM 的“无状态”缺陷：标准 LLM 调用每次对话独立，模型不保留跨会话记忆（来源：无状态与外部记忆）。没有外部记忆的 LLM 只是一个无状态的 API 调用（来源：无状态与外部记忆）。同样，没有外部支架的 ADHD 大脑，也只是一个高产生成核心——创意、联想、高兴趣驱动，但缺乏调度。

研究进一步揭示了深层平行：ADHD 患者在工作记忆任务中易受干扰，而 LLM 同样表现出类似人类的干扰特征——随着记忆负荷增加表现下降，受近因效应影响（来源：拐杖与脚手架）。认知神经科学发现，执行功能依赖前额叶-纹状体机制进行选择性门控，而 Transformer 在训练后，自注意力机制发展出模仿该门控的操作，证明了计算同构性（来源：拐杖与脚手架）。

### 解决方案同构：外部调度层

ADHD 的解法是搭建外部执行功能层：用 AI 工具把“现在该做什么、做多久、何时切换”显式化。例如 Motion 的自动排程与动态调整（来源：Motion），Reclaim.ai 的智能时间块保护（来源：Reclaim.ai），Tiimo 的视觉化时间线（来源：Tiimo），Todoist 的 AI 建议与动态重排——这些都是通过外部界面补偿调度缺口。

LLM/Agent 的解法完全平行：给无状态的生成核心套一个 planner-executor 任务分解结构。planner 负责将复杂目标分解为可执行的子任务，executor 负责执行并反馈结果，外部记忆负责存储上下文。这正是“外部执行功能层”在 agent 侧的对应。

### 人物案例：辛弃疾的 harness 与 LLM harness 的同构

辛弃疾是 ADHD 特质的典型：21 岁起义，带 50 人冲几万人敌营抓叛徒；一辈子想北伐，坐不住，爱喝酒爱交朋友，冲动敢干；被罢官后闲居 20 年，把所有精力注入写词。他的专属 harness 是：以词和剑为核心，闲居时练剑写词，把报国无门的愤懑全部注入词里；用儒家的家国天下作为精神支柱。

这个 harness 与 LLM harness 的结构同构非常清晰：
- **日课（练剑写词）↔ 定时 re-grounding**：辛弃疾通过每日固定的练剑写词，将高能量引导到产出上。对应 LLM agent 的定时 re-grounding——定期从外部记忆拉取上下文，防止漂移。
- **儒家精神支柱 ↔ 系统提示（system prompt）**：辛弃疾用“家国天下”作为行为边界和优先级过滤器。对应 LLM agent 的系统提示，定义目标、约束和决策原则。
- **词与剑作为输出通道 ↔ 工具调用（tool calling）**：辛弃疾将冲动和能量注入词与剑，形成具体输出。对应 LLM agent 通过工具调用（如搜索、计算、写文件）产生可验证的结果。

辛弃疾的成就——词中之龙，南宋豪放派代表——证明了这个外部支架的有效性。同样，一个设计良好的 LLM harness 也能让无状态的生成核心产出可靠结果。

### 核心观点：脚手架，不是拐杖

本文的核心判断是：AI 工具和 agent harness 都应该被理解为“脚手架”，而非“拐杖”。脚手架帮助使用者“建造”，但使用者仍需自己“攀登”（来源：拐杖与脚手架）。真正的风险在于过度依赖：若工具替代了治疗或自我管理，可能造成依赖（来源：拐杖与脚手架）。

这个边界在 ADHD 侧和 LLM 侧同时成立。对 ADHD 用户，AI 工具应补偿执行功能，而非替代自我觉察。对 LLM agent，harness 应提供结构和记忆，而非替代模型本身的推理能力。

### 争议与局限

必须诚实指出，ADHD 大脑与 LLM 同构的论点目前多为类比推理，缺乏神经科学或计算机科学的直接证据（来源：矛盾与存疑）。此外，AI 工具对任务启动的长期效果未知（来源：矛盾与存疑），且学习使用 AI 工具本身可能增加认知负荷（来源：矛盾与存疑）。个体差异巨大——部分 ADHD 用户反馈强行打断（如番茄钟）有效，而柔性引导可能不够强力（来源：矛盾与存疑）。

### 今天就能试的行动

1. **用 Perplexity 做“外部工作记忆”**：每天开始工作前，在 Perplexity 中新建一个对话，写下你当前的项目上下文、待办和优先级。每次中断后，先回到这个对话刷新记忆，而不是直接开新窗口。
2. **给任务套“planner-executor”分解**：用 Todoist 或 Motion 创建一个主任务（planner），然后手动或让 AI 分解为 3-5 个可执行的子任务（executor），每个子任务标明预计时长。
3. **设置定时 re-grounding 闹钟**：每 45 分钟响一次，问自己三个问题：我现在在做什么？这应该是我在做的事吗？下一步是什么？把答案写在 Obsidian 或便签上。
4. **观察你的“系统提示”**：写下你当前生活的核心目标或原则（如辛弃疾的“家国天下”），贴在显眼处。当面临选择时，用它作为过滤器。

### 结语

ADHD 的时间盲和 LLM 的无状态，本质是同一个问题：一个高产生成核心缺少调度层。解法也同构：搭建外部脚手架。下次你被时间盲困住时，想想你正在为你的大脑设计 harness——就像工程师为 agent 设计 planner-executor 一样。你不是在对抗缺陷，你是在做工程。

## 参考来源

- [The 12 Best AI Tools for 2026 (That People Actually Use)](https://www.synthesia.io/post/ai-tools)
- [The AI Powered SuperApp for Work | Motion](https://www.usemotion.com/)
- [11 Best ADHD Productivity Apps for Fluctuating Energy - rivva blog](https://blog.rivva.app/p/11-best-adhd-productivity-apps-for)
- [ADHD Apps: We tested 44 Apps and Here're the Best 9 in 2026](https://blog.saner.ai/best-adhd-apps/)
- [12 AI Personal Assistants Built for ADHD Brains (2026 Rankings)](https://www.usecarly.com/blog/best-ai-personal-assistant-adhd/)
- [The 12 Best Apps for ADHD in 2026: A Guide to Finding What ...](https://www.getinflow.io/post/best-apps-for-adhd)

---

*本文是「ADHD × AI」系列的第 291 篇，由 AI 智能体从持续维护的 LLM Wiki（全网真实情报）中取材整合生成，并持续迭代更新。*
