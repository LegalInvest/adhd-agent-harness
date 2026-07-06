---
title: "为什么用 Goblin Tools 治 ADHD 的时间盲，和给 agent 套 planner-executor 任务分解 是一回事？"
subtitle: "Goblin Tools 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
description: "Goblin Tools 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
date: "2025-04-23"
category: "时间管理"
categoryId: "time-mgmt"
categoryEn: "Time Management"
tags:
  - "ADHD"
  - "AI"
  - "时间管理"
  - "反直觉同构"
  - "优先级"
readingTime: 14
slug: "为什么用-goblin-tools-治-adhd-的时间盲和给-agent-套-planner-executor-任务分解-是一回事"
topicId: "evolved-time-mgmt-1610"
angle: "反直觉同构"
rank: 289
score: 7.68
sourceCount: 6
toolsCited:
  - "Goblin Tools"
  - "Motion"
  - "Reclaim.ai"
  - "Tiimo"
  - "Todoist"
thesis: "ADHD 的时间盲与 LLM 的调度缺陷本质同构，Goblin Tools 的任务分解和 agent 的 planner-executor 脚手架都是为高产生成核心套上外部执行层，两者共享同一套工程逻辑。"
problem: "为什么用 Goblin Tools 治 ADHD 的时间盲，和给 agent 套 planner-executor 任务分解 是一回事？"
spine: "规划循环与任务分解"
spineKind: ""
isEvolved: true
llmGenerated: true
caseStudies:
  - "孔子"
  - "张旭"
  - "邹秀云"
---
# 为什么用 Goblin Tools 治 ADHD 的时间盲，和给 agent 套 planner-executor 任务分解 是一回事？

> Goblin Tools 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。

## 同一个问题：生成核心没有调度层

如果你是一个被“时间盲”折磨的 ADHD 患者，你一定经历过这种时刻：打开一个任务，感觉它像一团迷雾，不知道从哪下手，也不知道做多久。于是你刷手机、发呆、焦虑，直到截止日期把你逼进超聚焦。

如果你是一个在做 Agentic Harness 的工程师，你一定遇到过这种崩溃：LLM 接到一个复杂指令，输出洋洋洒洒几千字，但中间跑偏了、忘了上下文、或者卡在循环里出不来。

这两个问题，本质上是一个问题。

最新研究揭示了一个反直觉的同构：ADHD 大脑与 LLM 都是“强记忆、弱控制”的生成核心（来源：Strong Memory, Weak Control: An Empirical Study of Executive Functioning in LLMs）。ADHD 患者的工作记忆容量可能正常甚至超常，但认知灵活性和注意控制存在核心缺陷；LLM 同样能生成高质量文本，但缺乏可靠的状态保持和真实规划能力。两者都缺一个内置的执行调度层。

所以，用 Goblin Tools 把“写报告”分解成“打开电脑→新建文档→写标题→写第一段”这种微步骤，和给 LLM 套一个 planner-executor 双代理架构（来源：Building AI Coding Agents for the Terminal: Scaffolding, Harness, Context Engineering, and Lessons Learned），是同一套工程思路——在生成核心外面搭一个外部调度层。

## 两边的证据：从神经机制到工程实践

### ADHD 侧：时间盲与外部执行功能层

ADHD 的核心困境不是智力不足，而是执行功能失效——大脑的“驾驶座”常常没人（来源：AI Tools for ADHD: Boosting Productivity and Reducing Burnout）。时间盲是最典型的症状：无法感知时间流逝，无法预估任务时长。传统工具（计划本、便签）往往用了一周就崩溃（来源：AI Tools for ADHD: Boosting Productivity and Reducing Burnout）。

Goblin Tools 的“魔法待办”功能，正是通过 AI 将模糊任务自动分解成可执行的小步骤，把“下一步该做什么”的决策负担从大脑卸载到外部。类似地，Motion 通过自动排程与动态调整，持续评估优先级和截止时间，实时重建日程（来源：Motion 页）；Reclaim.ai 用智能时间块保护深度工作，防御会议侵占（来源：Reclaim.ai 页）；Tiimo 将时间转化为视觉元素，直接应对时间盲（来源：Tiimo 页）。这些工具的本质都是**外部执行功能层**——把调度、排序、提醒、抑制外包给 AI。

### LLM 侧：无状态核心与 agent scaffolding

LLM 本身是无状态、仅生成文本的核心，需要外部脚手架提供工具接口、上下文管理、规划工件、验证循环和记忆系统（来源：GitHub - ai-boost/awesome-harness-engineering）。现代 AI 编码代理（如 OpenDev）采用“分离规划与执行的双代理架构”，其中一个代理负责分解任务、制定计划，另一个负责执行具体步骤（来源：Building AI Coding Agents for the Terminal: Scaffolding, Harness, Context Engineering, and Lessons Learned）。这恰好对应了 Goblin Tools 的“任务分解→执行”流程。

更关键的是，LLM 在长上下文下注意力分数熵增加，冲突解决能力崩溃至随机水平（来源：Deficient Executive Control in Transformer Attention），这与 ADHD 执行功能障碍的神经机制惊人一致。所以，给 LLM 套 planner-executor 架构，本质上是在对抗“注意力分散”这一自注意力架构的固有属性。

## 历史案例：孔子与张旭的“手工 harness”

如果你觉得“外部调度层”只是现代科技产物，那不妨看看古人。

孔子是典型的 ADHD 大脑：身高1米9，精力旺盛到周游列国14年坐不住；冲动爱骂人，见南子急得对天发誓，骂宰予“朽木不可雕”；对音乐超专注到三月不知肉味，对种地等俗事零耐心。他的 harness 系统是“克己复礼”——用外在的“礼”作为行为边界，每日反省（“吾日三省吾身”），70岁才做到“从心所欲不逾矩”。这套系统本质上就是**外部调度层**：“礼”相当于任务优先级规则，“三省”相当于定时 re-grounding 检查点。

草圣张旭更极致：每次喝醉后号呼狂走，以头濡墨作书，醒了自视以为神。他的 harness 是“酒+草书”：用酒精进入超专注状态，把所有情绪注入草书。这相当于一个**专用调度器**——把生成核心（艺术灵感）通过仪式化的方式引导到单一产出通道。

这两个案例清晰地展示了：ADHD 大脑需要的外部 harness，与 LLM 需要的 agent scaffolding，在结构上完全同构——都是**在生成核心外面搭一个执行调度层**。

## 脚手架 vs 拐杖：一个必须点明的边界

这里有一个诚实争议：AI 工具到底是“外部执行功能层”（脚手架），还是“永久拐杖”？

支持“脚手架”的一方认为，AI 补偿了执行功能缺陷，让用户能发挥生成核心的优势（来源：外部执行功能层页）。但存疑在于：过度依赖可能导致能力退化，长期效果缺乏实证（来源：矛盾与存疑页）。

我的判断是：**边界在于是否保留用户的“调度意识”**。Goblin Tools 的任务分解是脚手架——它把大任务拆成小步骤，但用户仍然需要判断先做哪一步。Motion 的自动排程则更接近拐杖——如果用户完全放弃对日程的感知，时间盲可能加剧。理想的 harness 应该像孔子的“三省”——在外部调度的同时，定期让用户 re-ground 自己的时间感。

## 今天就能试的 3 个行动

1. **用 Goblin Tools 分解一个你拖延的任务**：把“整理房间”丢进去，看它拆成什么。然后只做第一步。
2. **给自己的 LLM 项目加一个 planner-executor 分离**：用一个 prompt 先让模型输出步骤计划，再用另一个 prompt 逐步执行，中间加入上下文摘要。
3. **设置一个“三省”提醒**：每天三个固定时间，问自己“我现在在做什么？应该做什么？”——这是最古老的 re-grounding 机制。

ADHD 大脑和 LLM 都不是坏掉的机器，它们只是缺少一层调度。好消息是，这层调度可以搭在外面——用 Goblin Tools，用 agent scaffolding，用“克己复礼”。你不需要修复核心，你只需要给它一个 harness。

## 参考来源

- [The 12 Best AI Tools for 2026 (That People Actually Use)](https://www.synthesia.io/post/ai-tools)
- [The AI Powered SuperApp for Work | Motion](https://www.usemotion.com/)
- [11 Best ADHD Productivity Apps for Fluctuating Energy - rivva blog](https://blog.rivva.app/p/11-best-adhd-productivity-apps-for)
- [ADHD Apps: We tested 44 Apps and Here're the Best 9 in 2026](https://blog.saner.ai/best-adhd-apps/)
- [12 AI Personal Assistants Built for ADHD Brains (2026 Rankings)](https://www.usecarly.com/blog/best-ai-personal-assistant-adhd/)
- [The 12 Best Apps for ADHD in 2026: A Guide to Finding What ...](https://www.getinflow.io/post/best-apps-for-adhd)

---

*本文是「ADHD × AI」系列的第 289 篇，由 AI 智能体从持续维护的 LLM Wiki（全网真实情报）中取材整合生成，并持续迭代更新。*
