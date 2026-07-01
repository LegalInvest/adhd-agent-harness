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
  - "Focusmate"
  - "Brain.fm"
thesis: "ADHD大脑与LLM agent共享同一困境：生成核心强大但执行调度层缺失，因此两者的解法——人在回路的脚手架——在结构上完全同构。"
problem: "为什么用 Claude 治 ADHD 的不知哪些方法有用，和给 agent 套 human-in-the-loop 监督 是一回事？"
spine: "人在回路与身体在场"
spineKind: ""
isEvolved: true
llmGenerated: true
---
# 为什么用 Claude 治 ADHD 的不知哪些方法有用，和给 agent 套 human-in-the-loop 监督 是一回事？

> Claude 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。

## 问题：为什么“不知哪些方法有用”成了ADHD与AI agent的共同死穴？

ADHD人群最熟悉的挫败感，不是“做不到”，而是“不知道哪个方法有用”。今天试了番茄钟，明天觉得Goblin Tools不错，后天又切换到Motion——然后所有工具都在两周后吃灰。这种“方法流浪”的根源，不是工具不好，而是大脑缺少一个**可靠的执行调度层**。

同样的困境正在LLM agent上重演。开发者发现，即使是最强的模型（Claude、GPT-4），在长程任务中也会“开始忘记系统提示”（来源：Building an AI Coding Agent for the Terminal），行为逐渐漂移。工程师们拼命给agent套上human-in-the-loop监督、护栏、检查点——而这套东西，和ADHD群体需要的“外部脚手架”在结构上**一模一样**。

## 同构脊柱：高产但缺执行调度层的生成核心

### ADHD侧：生成核心过剩，执行功能不足

ADHD大脑的生成核心（发散思维、创意、多任务并行）产出极高，但执行功能（任务启动、持续专注、抑制冲动）薄弱，导致“高产但不可靠”（来源：人在回路与身体在场）。当大脑无法自动调度注意力时，外部工具就不得不扮演调度员的角色：Goblin Tools将“整理房间”分解成“捡起地板上的衣服”“擦桌子”等小步骤（来源：Goblin Tools），降低启动门槛；Motion自动排程并动态调整，消除“下一步该做什么”的决策负担（来源：Motion）；Saner.AI通过知识回忆减少搜索循环（来源：Saner.AI）。这些工具本质上都在做同一件事：**提供一个外部执行层**，对抗目标漂移。

### LLM/agent侧：生成核心强大，但指令消退

LLM本身是强大的生成核心，但缺乏可靠的执行调度层。在长程交互中，模型会因“指令消退”而偏离初始目标（来源：重锚定与目标漂移）。Agent harness通过事件驱动的系统提醒、token预算、工具调用次数上限和人工检查点来对抗这种漂移（来源：人在回路与身体在场）。Harness的核心是“形式化规划与护栏，使代理输出真正有用且正确”（来源：人在回路与身体在场）。模型本身强大，可靠性来自架构+护栏（来源：人在回路与身体在场）。

### 同构的解法：人在回路与身体在场

ADHD侧最有效的策略之一是身体在场效应：有另一个人在场时，执行功能障碍被绕过（来源：人在回路与身体在场）。Focusmate通过AI匹配虚拟身体搭档提供外部问责（来源：人在回路与身体在场）。LLM侧则对应human-in-the-loop监督：在关键决策点暂停并询问人类（来源：人在回路与身体在场）。两者都是**引入一个外部监督者**，弥补内在调度层的缺失。

## 脚手架 vs 拐杖：同构解法的边界

这里必须诚实指出一个争议：外部执行层如果设计不当，会从“脚手架”变成“拐杖”。多个wiki页面警告“过度依赖可能削弱内在能力”（来源：矛盾与存疑）。例如，Brain.fm的ADHD效果缺乏独立临床研究（来源：矛盾与存疑）；Goblin Tools的证据主要来自用户评价，缺乏随机对照试验（来源：Goblin Tools）。同一个harness，如果剥夺了人类的主动判断，就变成了拐杖；如果保留人类在回路中的决策权，才是真正的脚手架。

## 核心观点：ADHD与LLM agent的解法是同一类工程

我的判断是：**ADHD大脑与LLM agent是同一类“高产但缺执行调度层的生成核心”，两边的解法（harness/脚手架）结构同构。** 这意味着，如果你是一个正在为ADHD方法流浪而痛苦的人，你可以用agent harness的思维来设计自己的外部系统：不是寻找一个万能工具，而是搭建一个包含**重锚定、人在回路、护栏**的脚手架。如果你是一个在给agent做harness的工程师，你可以从ADHD群体的策略中学到更人性化的监督节奏——比如身体在场效应对应的“轻量级检查点”，而不是每次都在关键步骤打断用户。

## 今天就能试的行动

1. **用Goblin Tools的Magic ToDo分解一个让你拖延的任务**，观察分解后启动门槛的变化。如果觉得好用，记录下“分解到什么粒度最有效”——这就是你的“任务分解护栏”。
2. **在Claude或ChatGPT中设置一个“检查点提示”**：每次对话超过5轮后，自动要求AI总结当前进度并询问“是否继续”。这模拟了agent harness中的人工检查点。
3. **尝试一次Focusmate或类似的身体搭档**，体验“外部监督者”如何绕过执行功能屏障。记录下被监督时与独自工作时效率的差异。
4. **警惕拐杖化**：任何工具使用两周后，问自己“如果明天这个工具消失，我还能完成同样的任务吗？”如果答案是否定的，说明你需要调整脚手架的设计，而不是依赖工具本身。

## 参考来源

- [Best AI Tools for ADHD Productivity in 2026 (Honest Review) - Iwo Szapar](https://www.iwoszapar.com/p/best-ai-tools-adhd-productivity-2026)
- [AI Tools for ADHD: Boosting Productivity and Reducing Burnout](https://www.vktr.com/ai-platforms/ai-tools-for-adhd-boosting-productivity-and-reducing-burnout/)
- [The Best AI-Powered ADHD Productivity Tools in 2026 (That ...](https://nexasphere.io/blog/ai-adhd-productivity-tools-2026)
- [“A Cognitive Collaborator:” How Adults with ADHD Are Using ChatGPT](https://www.additudemag.com/how-to-use-chatgpt-executive-function-adhd/?srsltid=AfmBOoq-REuSO0UJC656kbLBAd5u3CDNmGeVNrZ79iouVqrFlN919a39)
- [Harnessing Artificial Intelligence to Live Better with ADHD - CHADD](https://chadd.org/attention-article/harnessing-artificial-intelligence-to-live-better-with-adhd/)
- [AI Tools for Kids with ADHD: A Complete Guide for Parents...](https://www.kidsaitools.com/en/articles/ai-tools-kids-adhd-complete-guide-2026)

---

*本文是「ADHD × AI」系列的第 206 篇，由 AI 智能体从持续维护的 LLM Wiki（全网真实情报）中取材整合生成，并持续迭代更新。*
