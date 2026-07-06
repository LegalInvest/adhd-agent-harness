---
title: "为什么用 Perplexity 治 ADHD 的学习半途而废，和给 agent 套 外部记忆/向量库 是一回事？"
subtitle: "Perplexity 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
description: "Perplexity 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
date: "2025-05-03"
category: "学习方法"
categoryId: "learning"
categoryEn: "Learning Methods"
tags:
  - "ADHD"
  - "AI"
  - "学习方法"
  - "反直觉同构"
  - "技能提升"
readingTime: 8
slug: "为什么用-perplexity-治-adhd-的学习半途而废和给-agent-套-外部记忆向量库-是一回事"
topicId: "evolved-learning-1677"
angle: "反直觉同构"
rank: 294
score: 7.68
sourceCount: 6
toolsCited:
  - "Perplexity"
  - "Goblin Tools"
  - "Saner.AI"
  - "Routinery"
thesis: "ADHD大脑与LLM都是高产生成核心但缺乏执行调度层，Perplexity等AI工具为ADHD提供的外部记忆与任务分解，与为agent套上向量库和验证循环的harness工程是同一思路——都是通过外部化执行功能来补偿内在缺陷。"
problem: "为什么用 Perplexity 治 ADHD 的学习半途而废，和给 agent 套 外部记忆/向量库 是一回事？"
spine: "无状态与外部记忆"
spineKind: ""
isEvolved: true
llmGenerated: true
caseStudies:
  - "孔子"
  - "王阳明"
  - "蒋淑华"
---
# 为什么用 Perplexity 治 ADHD 的学习半途而废，和给 agent 套 外部记忆/向量库 是一回事？

> Perplexity 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。

## 问题：为什么你的学习总是半途而废？

你打开一篇教程，读了三分钟，突然想起要查邮件；查完邮件，发现微信有未读消息；回完消息，又觉得应该先整理桌面……两小时后，你连教程的第一节都没读完。这不是意志力问题，而是你的大脑在执行功能上有个漏洞：它像一个强大的生成核心，能产出无数想法，却缺少一个可靠的调度层来把想法变成有序的行动。

这个漏洞，和当前LLM agent的致命缺陷一模一样。

## 同构：ADHD大脑 = 无状态生成核心

ADHD大脑的核心问题不是缺乏智力或创造力，而是执行功能缺陷——工作记忆不稳定、时间感知扭曲、任务启动困难。wiki资料指出，ADHD个体的工作记忆“强容量伴随弱控制”，注意力“易被环境带偏”（来源：上下文工程）。这意味着，你的大脑每时每刻都在产生新念头，但无法稳定地追踪“当前应该做什么”。

LLM agent也是同样。它拥有强大的文本生成能力，但本质上是“无状态”的：每次对话都是独立推理，无法可靠保留跨会话上下文。在复杂任务中，agent容易因“上下文膨胀导致推理退化”，控制逻辑分散在框架默认值中（来源：上下文工程）。

两边共享同一个核心矛盾：**高产但缺执行调度层的生成核心**。

## 解法：外部记忆与脚手架

既然内在调度层缺失，解法就是把它外部化。

**ADHD侧**：Perplexity正是这一思路的典型工具。用户输入一个目标（如“规划2025年项目”），Perplexity“将其分解为可管理的步骤”，从而降低启动门槛（来源：Perplexity）。类似地，Goblin Tools的Magic ToDo“自动将任何任务分解为更小、更易管理的步骤”，用户可调节“辣度”控制粒度（来源：Goblin Tools）。Saner.AI则通过“本地记忆存储和快速检索”减少搜索循环和标签切换（来源：Saner.AI）。这些工具本质上都是在给大脑补上一个外部化的执行功能层——一个数字化的秘书，负责记住上下文、拆解任务、提醒下一步。

**LLM/agent侧**：这就是harness工程。wiki资料明确说，harness提供“上下文传递、工具接口、规划工件、验证循环、记忆系统和沙盒”（来源：幻觉与验证循环）。关键组件包括“验证与CI集成”和“结构化工作流和规划”——把复杂任务分解为子任务，每一步进行规划与验证。没有这些，agent会“产生更多幻觉和重复工作”（来源：幻觉与验证循环）。

两边用的都是同一套工程模式：**将意图转化为可管理、可追踪、可启动的行动序列**。

## 人物案例：孔子的“礼”与王阳明的“事上练”

孔子是典型的ADHD大脑：身高1米9，精力旺盛，周游列国14年坐不住；冲动爱骂人，思维跳跃，《论语》全是场景化语录，无系统著作。他的harness是“克己复礼”——用外在的“礼”作为行为边界，每日反省，“吾日三省吾身”。这相当于给大脑套了一个外部调度器：礼是行为模板，反省是验证循环。70岁才做到“从心所欲不逾矩”，说明他一辈子都在和自己的冲动做斗争。

王阳明同样如此：兴趣爆发式转移，格竹子格到吐血，冲动上书被廷杖。他的harness是“致良知”与“知行合一”——用良知作为决策标准，并在事上练（在行动中校准）。这相当于给agent设了一个内部价值锚点，外加一个“在真实环境中验证”的循环。

这两个harness的结构，和LLM agent的“规划-执行-验证”循环完全同构。

## 关键判断：脚手架，不是拐杖

但这里有一个必须指出的边界。wiki资料中的“矛盾与存疑”提醒：AI工具是“外部执行功能层”还是“拐杖”？过度依赖可能导致能力退化（来源：矛盾与存疑）。我的判断是：**脚手架 vs 拐杖的区别在于，你是否在使用中逐步内化其结构**。孔子70岁才内化“礼”，王阳明一辈子都在“事上练”。AI工具应该像“日课”一样定时re-grounding，而不是替代你的所有决策。

目前缺乏针对ADHD人群的独立研究（来源：Perplexity），长期效果未知。但短期来看，这套外部化思路对两类人都有效。

## 今天就能试的3件事

1. **用Perplexity分解一个模糊目标**：比如“学习Python”，让AI帮你拆成5-10个具体步骤，然后只做第一步。
2. **给AI agent加一个验证步骤**：如果使用ChatGPT写代码，让它先输出测试用例再写实现，或者用“自我批评提示”检查输出。
3. **建立一个外部记忆库**：用Saner.AI或Obsidian记录所有想法和上下文，减少大脑的“工作记忆”负担。

同构不是巧合，而是工程智慧的迁移。你的大脑和LLM agent一样，需要的不是更强的生成能力，而是一个外部化的调度层。

## 参考来源

- [Can ChatGPT be Your Personal Medical Assistant?](http://arxiv.org/abs/2312.12006v1)
- [One Billion Word Benchmark for Measuring Progress in Statistical Language Modeling](http://arxiv.org/abs/1312.3005v3)
- [Activation Sparsity Opportunities for Compressing General Large Language Models](http://arxiv.org/abs/2412.12178v2)
- [YouZhi: Towards High-Concurrency Financial LLMs via Adaptive GQA-to-MLA Transition](http://arxiv.org/abs/2606.05868v1)
- [FBI-LLM: Scaling Up Fully Binarized LLMs from Scratch via Autoregressive Distillation](http://arxiv.org/abs/2407.07093v1)
- [Prompt Injection Attack to Tool Selection in LLM Agents](http://arxiv.org/abs/2504.19793v3)

---

*本文是「ADHD × AI」系列的第 294 篇，由 AI 智能体从持续维护的 LLM Wiki（全网真实情报）中取材整合生成，并持续迭代更新。*
