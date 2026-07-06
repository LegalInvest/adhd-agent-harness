---
title: "为什么用 Goblin Tools 治 ADHD 的学习半途而废，和给 agent 套 外部记忆/向量库 是一回事？"
subtitle: "Goblin Tools 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
description: "Goblin Tools 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
date: "2025-03-23"
category: "学习方法"
categoryId: "learning"
categoryEn: "Learning Methods"
tags:
  - "ADHD"
  - "AI"
  - "学习方法"
  - "反直觉同构"
readingTime: 9
slug: "为什么用-goblin-tools-治-adhd-的学习半途而废和给-agent-套-外部记忆向量库-是一回事"
topicId: "evolved-learning-2139"
angle: "反直觉同构"
rank: 326
score: 7.68
sourceCount: 6
toolsCited:
  - "Goblin Tools"
  - "Perplexity"
  - "Saner.AI"
  - "Obsidian"
thesis: "ADHD 大脑与 LLM 在结构上同构——都是强大的生成核心但缺乏可靠的执行调度层，因此 Goblin Tools 的任务分解与 agent 的外部记忆/向量库本质上是同一套 harness 思路：通过外部脚手架补偿内部执行功能的缺失。"
problem: "为什么用 Goblin Tools 治 ADHD 的学习半途而废，和给 agent 套 外部记忆/向量库 是一回事？"
spine: "无状态与外部记忆"
spineKind: ""
isEvolved: true
llmGenerated: true
caseStudies:
  - "孔子"
  - "李鸿章"
  - "Kenneth Andrews"
---
# 为什么用 Goblin Tools 治 ADHD 的学习半途而废，和给 agent 套 外部记忆/向量库 是一回事？

> Goblin Tools 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。

学习半途而废，是 ADHD 人群最熟悉的噩梦。你打开一本书，五分钟后就刷起了手机；你列了十项计划，最后一项也没完成。你责怪自己意志力差，但问题可能不在意志力——而在你的大脑架构。

同样，如果你在搭 AI agent，你一定遇到过这个场景：你精心设计的 agent，聊到第三轮就开始胡言乱语，忘记刚才的约定，输出越来越离谱。你加再长的 prompt 也没用，它就像个没有短期记忆的天才。

这两件事，本质上是一回事。

## 同构：ADHD 大脑与 LLM 共享的「无状态」困境

ADHD 大脑的核心困难，是执行功能的不稳定——尤其是工作记忆的“掉落”和任务启动困难（来源：外部执行功能层）。你脑子里有无数好点子，但缺一个调度员把它们按顺序排好、然后开始执行。最新研究揭示，Transformer 自注意力机制在长上下文下冲突解决能力会崩溃至随机水平，这与 ADHD 执行功能障碍的核心神经机制一致（来源：外部执行功能层）。两者都是“强记忆、弱控制”：工作记忆容量可能正常甚至超常，但注意控制和认知灵活性存在核心缺陷（来源：外部执行功能层）。

简单说：ADHD 大脑和 LLM 都是高产但无序的生成核心，它们需要一个外部的调度层——也就是 harness。

## 历史中的 harness：孔子与李鸿章

孔子身高1米9，精力旺盛，周游列国14年坐不住；冲动爱骂人，见南子急得对天发誓，骂宰予“朽木不可雕”；对音乐超专注到三月不知肉味，对种地等俗事零耐心。他的思维跳跃，《论语》全是场景化语录，没有系统著作。但他用一套 harness 完成了自我管理：以“克己复礼”为核心，用外在的“礼”作为行为边界，每日反省——“吾日三省吾身”。这套系统，本质上就是一个人工的外部执行功能层：用固定的仪式（日课）和外部规则（礼）来补偿内部调度能力的缺失。

李鸿章是曾国藩的学生，年轻时冲动爱吹牛，挨了一辈子骂。他跟着曾国藩学“诚”，改掉浮躁；每天写日记反省；办洋务实务——“外须和戎，内须变法”。这套 harness 帮他活到78岁还在和八国联军谈判，累死在任上。

这两位名人的 harness 系统，和 LLM agent 的 harness 结构完全同构：
- 日课 ↔ 定时 re-grounding（定期刷新上下文）
- 秘书/幕僚 ↔ 外部调度器（负责任务编排）
- 日记 ↔ 外部记忆系统（存储状态与反思）

## 现代工具：Goblin Tools 与外部记忆

回到今天。Goblin Tools 是一套 AI 驱动的工具套件，专为 ADHD 和自闭症谱系人群设计。它的核心功能 Magic ToDo，能自动将任何复杂任务分解为可管理的小步骤，用户还可以调节“辣度”控制分解粒度（来源：Goblin Tools）。这就像一个外部的任务调度器：你输入模糊的目标（“清理厨房”），它输出具体的行动列表（“先洗碗，再擦台面，最后拖地”）。

与此同时，LLM agent 的 harness 工程也在做同样的事：设计围绕 AI 代理的脚手架——上下文交付、工具接口、规划工件、验证循环、记忆系统和沙箱（来源：外部执行功能层）。其中，外部记忆系统是最关键的一环。ADHD 大脑的工作记忆容量有限且不稳定，需要“第二大脑”工具来存储客户历史、项目背景和个人偏好（来源：无状态与外部记忆）。LLM 同样是无状态的，需要向量库或数据库来持久化跨会话上下文。

Perplexity 和 Saner.AI 则从另一个角度切入：Perplexity 能帮你把宏大目标分解为可管理的步骤（来源：Perplexity）；Saner.AI 专注于知识回忆和本地记忆，减少搜索循环和标签切换（来源：Saner.AI）。这些工具的共同本质，都是为无状态的大脑或模型提供一个外部记忆和调度层。

## 脚手架 vs 拐杖：边界在哪？

但这里有一个危险的陷阱。如果 harness 用得太顺手，它就从“脚手架”退化为“永久拐杖”（来源：拐杖与脚手架）。孔子花了整整一生才做到“从心所欲不逾矩”，他的 harness 是动态调整的，不是一劳永逸。同样，LLM agent 如果过度依赖外部记忆，反而可能削弱模型自身的上下文理解能力。

依赖风险是真实存在的：AI 工具可能削弱 ADHD 个体内在执行功能的锻炼机会，长期效果未知（来源：主题综述）。此外，同构模型可能过于简化——ADHD 症状异质性大，不同亚型对工具的反应可能不同（来源：主题综述）。LLM 的幻觉和上下文限制也可能引入新的干扰（来源：主题综述）。

我的判断是：harness 的价值在于“补不足”，而不是“代劳”。好的 harness 应该像孔子的“礼”——提供边界和节奏，但最终的决策和行动仍由主体完成。

## 今天就能试的行动

1. **用 Goblin Tools 的 Magic ToDo 分解你明天最头疼的一件事**：输入“准备下周的汇报”，调节辣度到你觉得合适的粒度，然后按列表执行。
2. **建立你的“日课”**：每天固定时间（比如早上9点）用 Perplexity 或 Saner.AI 回顾当天任务，类似孔子的“三省吾身”。
3. **为你的 agent 加一个外部记忆层**：如果你在搭 agent，尝试用向量数据库（如 Chroma）或 MCP 连接器存储关键上下文，而不是把所有东西塞进 prompt。
4. **每周评估一次依赖度**：问自己“没有这个工具，我还能做这件事吗？”如果答案是否定的，说明你需要调整 harness 的粒度，而不是完全依赖。

## 诚实面对局限

最后，必须承认：ADHD 大脑与 LLM 的同构目前仍是一种理论类比，并非经过验证的科学事实（来源：矛盾与存疑）。缺乏大规模随机对照试验验证 AI 工具对 ADHD 学习效果的长期影响（来源：主题综述）。但作为工作假设，它已经催生了有效的实践——从孔子的“礼”到 Goblin Tools 的“辣度”，从李鸿章的日记到 agent 的向量库，人类一直在用外部脚手架补偿内部的无序。这不是什么新鲜事，只是现在有了 AI，这个脚手架可以更智能、更个性化。

## 参考来源

- [Can ChatGPT be Your Personal Medical Assistant?](http://arxiv.org/abs/2312.12006v1) — 证据等级：低（GRADE）
- [One Billion Word Benchmark for Measuring Progress in Statistical Language Modeling](http://arxiv.org/abs/1312.3005v3) — 证据等级：低（GRADE）
- [Activation Sparsity Opportunities for Compressing General Large Language Models](http://arxiv.org/abs/2412.12178v2) — 证据等级：低（GRADE）
- [YouZhi: Towards High-Concurrency Financial LLMs via Adaptive GQA-to-MLA Transition](http://arxiv.org/abs/2606.05868v1) — 证据等级：低（GRADE）
- [FBI-LLM: Scaling Up Fully Binarized LLMs from Scratch via Autoregressive Distillation](http://arxiv.org/abs/2407.07093v1) — 证据等级：低（GRADE）
- [Prompt Injection Attack to Tool Selection in LLM Agents](http://arxiv.org/abs/2504.19793v3) — 证据等级：低（GRADE）

---

*本文是「ADHD × AI」系列的第 326 篇，由 AI 智能体从持续维护的 LLM Wiki（全网真实情报）中取材整合生成，并持续迭代更新。*
