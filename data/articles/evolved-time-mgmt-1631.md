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
  - "Motion"
  - "Reclaim.ai"
  - "Tiimo"
  - "Structured"
  - "Todoist"
  - "Goblin Tools"
  - "Saner.AI"
thesis: "ADHD 大脑与 LLM 都是高产的生成核心但缺乏可靠执行调度层，因此用外部工具（如 Perplexity）缓解时间盲与给 agent 套 planner-executor harness 本质同构——都是为生成核心搭建脚手架，而非永久拐杖。"
problem: "为什么用 Perplexity 治 ADHD 的时间盲，和给 agent 套 planner-executor 任务分解 是一回事？"
spine: "规划循环与任务分解"
spineKind: ""
isEvolved: true
llmGenerated: true
---
# 为什么用 Perplexity 治 ADHD 的时间盲，和给 agent 套 planner-executor 任务分解 是一回事？

> Perplexity 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。

## 问题：ADHD 的时间盲，与 LLM 的 planner-executor 断裂，是同一个 bug

如果你是一个被时间盲折磨的 ADHD 患者，你一定熟悉这种感觉：明明知道今天有三件重要的事，但一打开电脑，大脑就像空白的文档，完全不知道从哪里开始。时间在你这里不是线性的，而是一团模糊的雾——你既无法感知它的流逝，也无法预测未来几分钟的行动代价。

如果你是一个在做 Agentic Harness 工程的工程师，你一定也熟悉这种感觉：LLM 的生成能力惊人，能写出漂亮的代码、复杂的计划，但一旦让它执行多步任务，它就会像 ADHD 患者一样——偏离轨道、忘记上下文、被无关细节吸引。你不得不给它套上 planner-executor 分解框架，用外部记忆、工具接口和验证循环来约束它。

这两个问题，表面上风马牛不相及。但当我们把 ADHD 大脑与 LLM 放在一起看，会发现惊人的同构：**两者都是高产的生成核心，但缺乏可靠的执行调度层**（来源：AI 与 ADHD 的时间管理）。ADHD 的时间盲，本质上是内在执行功能（工作记忆、时间感知、任务启动）的缺失；LLM 的 planner-executor 断裂，本质上是无状态、有限上下文窗口、缺乏持久调度能力。

而解法，也惊人地同构：**给生成核心套上一个外部 harness**。

## 答案：Perplexity 治时间盲，就是给 ADHD 大脑套 planner-executor harness

让我们拆开看。

### ADHD 一侧：外部工具作为执行调度层

ADHD 大脑的工作记忆容量有限且不稳定，导致跨会话任务难以持续（来源：无状态与外部记忆）。典型表现是：每天需要重新回忆项目上下文，否则容易偏离轨道。为此，ADHD 个体常借助“第二大脑”工具——例如基于 AI 的外部记忆系统，能存储客户历史、项目背景、质量标准和个人偏好（来源：无状态与外部记忆）。

具体到时间盲，工具如 **Tiimo** 和 **Structured** 通过视觉化时间线将时间转化为可见元素，直接应对时间盲问题（来源：Tiimo）。**Motion** 和 **Reclaim.ai** 则更进一步：它们自动根据任务、会议和截止日期创建并动态调整每日计划，消除“下一步该做什么”的决策负担（来源：Motion；Reclaim.ai）。Motion 的 AI 核心功能是自动排程与动态调整，持续评估任务优先级和截止日期，实时重建日程（来源：Motion）。Reclaim.ai 则通过创建深度工作、习惯和专注时间的智能块，自动防御会议侵占，帮助用户维持日程的稳定性（来源：Reclaim.ai）。

这些工具本质上在做同一件事：**为 ADHD 大脑提供缺失的执行调度层**。它们充当外部工作记忆，存储上下文；它们自动分解任务，降低启动门槛；它们通过视觉化或自动化，补偿时间感知缺陷。这正是“给生成核心套上 harness”的 ADHD 版本。

### LLM/harness 一侧：planner-executor 作为外部调度层

标准的 LLM 调用是无状态的：每次对话都是独立的，模型不保留跨会话的记忆（来源：无状态与外部记忆）。没有 harness 的 LLM 只是一个无状态的 API 调用（来源：无状态与外部记忆）。生产级 agent 系统通过外部记忆（如向量数据库）解决溢出问题，并组合使用会话内上下文记忆、长期检索向量库和结构化知识库（来源：无状态与外部记忆）。

Harness 工程正是设计围绕 LLM 的脚手架——包括上下文传递、工具接口、规划工件、验证循环、记忆系统和沙盒——决定代理在真实任务中的成败（来源：拐杖与脚手架）。脚手架在首次提示前组装代理，而 harness 在运行时编排工具调度、上下文管理和安全执行（来源：拐杖与脚手架）。

这里的 planner-executor 分解，与 ADHD 工具的任务分解和自动排程，结构完全一致：planner 负责制定计划（类似 Motion 的自动排程），executor 负责执行（类似用户按计划行动），而外部记忆（如向量数据库）则补偿无状态性（类似 Todoist 的智能提醒充当数字工作记忆，来源：AI 与 ADHD 的时间管理）。

### 同构对应：从概念到证据

| ADHD 侧 | LLM/harness 侧 |
|---------|----------------|
| 缺乏内在执行功能脚手架（来源：拐杖与脚手架） | LLM 固定上下文窗口，长程依赖追踪困难（来源：拐杖与脚手架） |
| 外部工具作为脚手架，外化思维，减轻工作记忆负荷（来源：拐杖与脚手架） | Harness 提供上下文、记忆、工具接口，弥补 LLM 无状态和有限窗口（来源：拐杖与脚手架） |
| 时间盲：无法感知时间流逝 | 无状态：无法感知会话历史 |
| Motion 自动排程消除决策负担 | Planner 自动分解任务给 executor |
| Tiimo 视觉化时间线 | 上下文窗口管理 |

## 核心观点：脚手架 vs 拐杖——真正的 harness 必须可撤除

同构不仅解释了为什么同一套思路两边都成立，更暴露出一个共同的危险：**过度依赖**。

ADHD 一侧，专家警告过度依赖风险：若工具替代了治疗或自我管理，可能造成依赖（来源：拐杖与脚手架）。真正的脚手架应帮助使用者“建造”，但使用者仍需自己“攀登”（来源：拐杖与脚手架）。LLM/harness 一侧，如果 harness 完全替代了 agent 的自主能力，agent 就变成了一个被动的 API 调用器，失去灵活性。

但现状是，多数工具（如 **Goblin Tools**、**Saner.AI**）设计为长期使用，未提及撤除机制（来源：矛盾与存疑）。同样，许多 agent harness 框架也没有设计“脚手架撤除”路径——它们假设 agent 永远需要外部调度。

我的观点是：**真正的 harness 应该像学习辅助轮，而不是永久拐杖**。ADHD 工具应该逐步训练用户的内在执行功能，比如随着使用时间增加，逐渐减少自动提醒的频率，或者让用户手动确认任务分解。LLM harness 也应该在 agent 表现稳定后，逐步减少外部约束，让模型学会自我规划。

这一判断目前缺乏实证支持（来源：矛盾与存疑），但逻辑上成立：如果同构成立，那么两边的“脚手架可撤除性”应该是可设计、可验证的。

## 争议与局限

必须诚实指出，ADHD 大脑与 LLM 同构命题本身是理论框架，缺乏大规模实证支持（来源：矛盾与存疑）。多数工具（如 **Structured**）的 AI 功能细节不明确，缺乏严谨的随机对照试验（来源：AI 与 ADHD 的时间管理）。多巴胺干预的有效性也存在争议（来源：矛盾与存疑）。

此外，不同 ADHD 亚型对工具的反应可能不同，现有工具多针对通用缺陷，个性化不足（来源：AI 与 ADHD 的时间管理）。

## 今天就能试的行动

1. **用 Perplexity 或 ChatGPT 做“任务分解代理”**：把你的一个模糊任务（比如“整理项目文档”）输入给 AI，要求它分解成 3-5 个可执行步骤，并给出每个步骤的预估时间。这就是在给自己套一个 planner。
2. **试用 Motion 或 Reclaim.ai 的自动排程**：设置 3 个本周任务，让 AI 自动排入日历，体验“消除决策负担”的效果。注意观察自己是否感觉更轻松。
3. **手动记录一次“时间盲”时刻**：当你发现自己不知道接下来该做什么时，用纸笔写下当前任务、下一步行动、截止时间。这相当于给大脑一个外部上下文窗口。
4. **思考你的“脚手架撤除计划”**：如果你在使用某个 ADHD 工具，问自己：如果有一天我不用它了，我的能力会退步吗？如果是，尝试每周减少一次使用，看看能否独立完成。

## 参考来源

- [AI Tools for ADHD: Boosting Productivity and Reducing Burnout](https://www.vktr.com/ai-platforms/ai-tools-for-adhd-boosting-productivity-and-reducing-burnout/)
- [6 ways AI can help you manage ADHD symptoms - Understood.org](https://www.understood.org/en/articles/adhd-ai-tools)
- [The Role of Artificial Intelligence in ADHD Diagnosis and Treatment: A New Frontier in Neurotechnology | IntechOpen](https://www.intechopen.com/online-first/1220045)
- [Artificial Intelligence Identifies Adults with ADHD Using EEG Features](https://advances.massgeneral.org/neuro/journal.aspx?id=1593)
- [AI for ADHD: Best Tools, Apps, and Strategies - Themba Tutors](https://thembatutors.com/ai-for-adhd-tools-and-apps/)
- [11 Best ADHD Productivity Apps for Fluctuating Energy - rivva blog](https://blog.rivva.app/p/11-best-adhd-productivity-apps-for)

---

*本文是「ADHD × AI」系列的第 291 篇，由 AI 智能体从持续维护的 LLM Wiki（全网真实情报）中取材整合生成，并持续迭代更新。*
