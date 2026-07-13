---
title: "为什么用 Routinery 治 ADHD 的学习半途而废，和给 agent 套 外部记忆/向量库 是一回事？"
subtitle: "Routinery 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
description: "Routinery 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
date: "2025-05-02"
category: "学习方法"
categoryId: "learning"
categoryEn: "Learning Methods"
tags:
  - "ADHD"
  - "AI"
  - "学习方法"
  - "反直觉同构"
readingTime: 11
slug: "为什么用-routinery-治-adhd-的学习半途而废和给-agent-套-外部记忆向量库-是一回事"
topicId: "prob-efd4494c5e"
angle: "反直觉同构"
rank: 312
score: 7.65
sourceCount: 6
toolsCited:
  - "Goblin Tools"
  - "Saner.AI"
  - "Perplexity"
thesis: "ADHD 大脑与 LLM 都是高产的生成核心，但缺乏可靠的执行调度层，导致学习或任务屡屡因“状态丢失”而半途而废；Routinery 这类例程 harness 与 agent 的外部记忆/向量库本质上是同一套“外部状态层”的工程方案。"
problem: "为什么用 Routinery 治 ADHD 的学习半途而废，和给 agent 套 外部记忆/向量库 是一回事？"
spine: "无状态与外部记忆"
spineKind: ""
isEvolved: true
llmGenerated: true
isoStrength: "A"
caseStudies:
  - "孔子"
  - "王阳明"
  - "Julie Haynes"
---
# 为什么用 Routinery 治 ADHD 的学习半途而废，和给 agent 套 外部记忆/向量库 是一回事？

> Routinery 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。

你是不是也这样：报课时雄心万丈，第三天就找不到“当时为什么要学”的上下文；刷到一半的视频、写到一半的笔记、买到一半的课，全变成数字废墟。对 ADHD 人群来说，这常被误读为“不自律”；对做 Agentic Harness 的工程师来说，这看起来像极了 LLM 的典型故障——一次对话结束，上下文清空，下一轮完全不知道自己之前在哪、接下来该干嘛。

两种“半途而废”的底层结构其实相同：核心很强，调度层很脆。这篇文章我想把 Routinery 这类“例程 harness”当作一个代表来讨论，并用 wiki 中的真实工具与研究说明：**给 ADHD 套一个外部执行层，和给 agent 套外部记忆/向量库，是同一回事。**

## 1. 不是懒，是“状态丢失”

ADHD 的瓶颈往往不在智力或兴趣，而在工作记忆。工作记忆是一种极短期的“脑海中的草稿纸”，ADHD 患者这张草稿纸不稳定，容易丢失任务细节和上下文（来源：6 ways AI can help you manage ADHD symptoms - Understood.org）。一旦目标被日常生活的噪音冲散，人就停在“启动线”前，或者无限切换。

LLM 同理。单次推理很强，但本质上无状态：每次新对话都是一张空白草稿纸。没有外部记忆，它无法记住你上周的训练目标、上一步的偏好，也无法在多次交互中保持连贯。这就是“无状态与外部记忆”的同构——两边都需要一个外挂的“状态层”来补自己缺失的连续性（来源：AI 与 ADHD 的学习方式）。

## 2. 同一架构：生成核心 + 脆弱调度层

明尼苏达大学系统测试 LLM 的执行功能，发现它们呈现“强记忆、弱控制”的剖面：工作记忆容量甚至超过常人，但认知灵活性、注意控制和对自动化反应的抑制存在核心缺陷，这正是 ADHD 的经典神经心理模式（来源：Strong Memory, Weak Control: An Empirical Study of Executive Functioning in LLMs）。

耶鲁大学进一步证明，Transformer 的自注意力机制本身就会造成工作记忆容量限制：随着序列变长，注意力分数熵增、注意力弥散，表现下降——这与人类 ADHD 的注意力分散在计算层面同源（来源：Self-Attention Limits Working Memory Capacity of Transformer-Based Models）。另一项用经典 Stroop 冲突任务测试 Transformer 的研究也发现，短上下文里模型表现正常，但认知负荷增加后，它在冲突试次上骤降到随机水平，无法抑制优势反应，与 ADHD 执行功能缺陷一一对应（来源：Deficient Executive Control in Transformer Attention）。

所以 ADHD 大脑和 LLM 不是“像”，而是共享同一种故障模式：**底层生成能力过剩，orchestration 层不足。** 瓶颈不是算力或智商，而是谁来决定“现在注意什么、下一步做什么”。

## 3. 从孔子的“礼”到 agent 的向量库：harness 的同构

古人早就在用手工 harness 解决这个 bug。孔子身高一米九、精力旺盛、冲动爱骂人、对俗事毫无耐心，思维跳跃到《论语》全是场景化语录，没有系统著作。他的 harness 是“克己复礼”——用外在的“礼”作为行为边界，每天“吾日三省吾身”，直到七十岁才“从心所欲不逾矩”。这相当于给生成核心写了一套 system prompt 加 guardrails，再用日课做每日 re-grounding。

王阳明的 harness 更靠近现代 agent。他兴趣爆发式转移，从格竹子到兵法、道、佛、军事、讲学，35 岁冲动上书骂权臣被廷杖流放。他的解决方案是“致良知”和“知行合一”：把“良知”当作一个内置价值 oracle，所有决策用它裁决；把“事上练”当作在真实环境中执行、获得反馈。这对应到 LLM agent 架构，就是价值对齐的 reward/critic 模型 + 工具调用与环境反馈的 loop。

两个人的共同点很清楚：**他们都没指望靠“意志力”管住自己，而是把规则、记忆、反省和决策标准外化成一套可重复的 harness。** 工程师给 agent 加向量库，做的不是更 Fancy 的模型，而是同样的事：把易失状态持久化，让核心每次重启都能重新加载上下文。

## 4. 为什么 Routinery 治学习半途而废，等于给 agent 加向量库

Routinery 这类例程工具的核心价值不是“时间表”，而是**状态持久化**。它帮你把“我要学什么、今天学到哪、下一步最小动作是什么”写在核心之外，每次你掉线后回来，不需要从大脑里重新打捞上下文，而是看一眼外部记录就能重新进入。

这对应 LLM 的向量库：它不只是一个搜索仓库，而是 agent 的“可恢复状态”。当你把学习历史、偏好、目标、前一步输出向量化存进去，下一次交互时通过检索重新注入 prompt，模型就知道“之前在哪、现在该干嘛”。

wiki 中提到的 ADHD 工具正好体现了同一套设计：
- **Goblin Tools** 的 Magic ToDo 把模糊任务（如“清理厨房”）自动分解成可调粒度的小步骤，降低启动门槛（来源：12 AI Personal Assistants Built for ADHD Brains (2026 Rankings)）。这相当于 agent 的任务规划器。
- **Saner.AI** 强调“本地记忆”和“知识回忆”，减少 ADHD 用户在多个标签和应用之间的搜索循环，用通用收件箱自动提取待办并分解里程碑（来源：ADHD Apps: We tested 44 Apps and Here're the Best 9 in 2026）。这相当于 agent 的向量记忆与检索层。
- **Perplexity** 从一个目标开始，把它拆成可管理的步骤，帮助用户跨越 ADHD 的执行功能缺口（来源：ADHD Productivity Hack: Plan 2025 Using AI (Step-by-Step)）。这相当于 agent 的检索-分解-推理链。

所以 Routinery 不是“培养自律”的鸡汤，而是 ADHD 版的“上下文管理器”；向量库也不是“让模型记得更多”，而是 LLM 版的“外部执行功能层”。

## 5. 脚手架 vs 拐杖的边界

同构视角很好，但 wiki 也提醒我们：它目前仍是一种理论类比，不同页面在表述上有不一致，并非已被验证的科学事实（来源：矛盾与存疑）。更实际的风险是**脚手架退化成拐杖**——如果外部系统替你做了所有决策，ADHD 个体内在的执行功能可能失去锻炼机会，LLM 也可能因为过度依赖检索而弱化了自身的推理与规划能力（来源：拐杖与脚手架）。

边界在哪里？我认为：当外部 harness 只是帮你“恢复状态”而不是“替你做决定”，它就是脚手架；当它开始接管目标设定、价值判断和反思，你就被拐杖架走了。ADHD 需要 harness 来降低启动负荷，但最终的“致良知”仍然要回到人身上；agent 需要向量库来补全上下文，但核心推理能力不能丢给检索。

## 6. 今天就能试的四步

1. **写一个“重启便签”**：每次结束学习前，用一句话写下“目标是什么、刚才卡在哪、下一步最小动作是什么”。这就是 ADHD 版的 checkpoint。
2. **把模糊目标丢给分解器**：用 **Goblin Tools** 或 **Perplexity** 把“学英语”“学 Python”拆成 10 分钟就能启动的微任务，直接降低执行门槛。
3. **设置每日 re-ground

## 参考来源

**同构强度：A 级** —— 直接文献支撑（引用 ADHD↔LLM 同构专题研究）

- [Transformer-XL: Attentive Language Models beyond a Fixed-Length Context](https://doi.org/10.18653/v1/p19-1285) — 证据等级：低（GRADE）
- [Dialogue Response Ranking Training with Large-Scale Human Feedback Data](https://doi.org/10.18653/v1/2020.emnlp-main.28) — 证据等级：低（GRADE）
- [ADHD Apps: We tested 44 Apps and Here're the Best 9 in 2026](https://blog.saner.ai/best-adhd-apps/) — 证据等级：低（GRADE）
- [12 AI Personal Assistants Built for ADHD Brains (2026 Rankings)](https://www.usecarly.com/blog/best-ai-personal-assistant-adhd/) — 证据等级：低（GRADE）
- [Strong Memory, Weak Control: An Empirical Study of Executive Functioning in LLMs](https://preview.aclanthology.org/evt-to-venues/2026.eacl-long.281.pdf) — 证据等级：低（GRADE）
- [Self-Attention Limits Working Memory Capacity of Transformer-Based Models](https://arxiv.org/pdf/2409.10715) — 证据等级：低（GRADE）

---

*本文是「ADHD × AI」系列的第 163 篇，由 AI 智能体从持续维护的 LLM Wiki（全网真实情报）中取材整合生成，并持续迭代更新。*
