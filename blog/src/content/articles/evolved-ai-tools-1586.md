---
title: "为什么用 Speechify 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用 是一回事？"
subtitle: "Speechify 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
description: "Speechify 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
date: "2025-03-26"
category: "AI工具实战"
categoryId: "ai-tools"
categoryEn: "AI Tools in Practice"
tags:
  - "ADHD"
  - "AI"
  - "AI工具实战"
  - "反直觉同构"
  - "ADHD辅助"
readingTime: 10
slug: "为什么用-speechify-治-adhd-的任务启动困难和给-agent-套-function-calling-工具调用-是一回事"
topicId: "evolved-ai-tools-1586"
angle: "反直觉同构"
rank: 387
score: 7.65
sourceCount: 6
toolsCited:
  - "Goblin Tools"
  - "Lex"
  - "Saner.AI"
  - "Speechify"
thesis: "ADHD 大脑与 LLM agent 在‘任务启动困难’上本质同构：两者都是高产但缺执行调度层的生成核心，因此同一套 harness 思路——通过外部工具调用实现认知卸载——对两者都成立，但需警惕从脚手架沦为拐杖。"
problem: "为什么用 Speechify 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用 是一回事？"
spine: "工具使用与认知卸载"
spineKind: ""
isEvolved: true
llmGenerated: true
---
# 为什么用 Speechify 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用 是一回事？

> Speechify 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。

## 问题：为什么任务启动这么难？

你盯着空白的文档，手指悬在键盘上，大脑却像卡了壳——不是不知道要写什么，而是“开始”这个动作本身就像要推开一堵墙。ADHD 人群对这种场景再熟悉不过：任务启动困难不是懒惰，而是执行功能层失效——大脑的“生成核心”已经高速运转，但调度层（前额叶）拒绝下发执行指令。

另一边，工程师们正在调试 LLM agent：模型明明知道该调用哪个 API，却迟迟不输出 function call，或者输出了一堆废话后才慢吞吞地调用工具。这种“冷启动”延迟，和 ADHD 的启动困难如出一辙。

## 同构：ADHD 大脑与 LLM 是同一类生成核心

ADHD 大脑的特点是：创造力强、联想丰富，但执行功能（工作记忆、任务启动、时间感知）不稳定。这种波动性在概念上类似于 LLM 的“采样温度”——温度高时输出多样但不可控，温度低时输出稳定但可能缺乏创意。ADHD 个体的表现波动与生理节律相关，而 LLM 的非确定性（nondeterminism）则来自采样温度的随机性（来源：采样温度与表现波动）。两者都缺乏一个稳定的执行调度层来“调温”。

更关键的是，两者的“启动困难”都源于同一个结构性问题：生成核心与调度层分离。ADHD 大脑的调度层（前额叶执行功能）天生薄弱，而 LLM 的调度层（harness/agent 框架）需要外部构建。因此，解决方案也同构：为生成核心套上 harness（脚手架），通过外部工具调用实现认知卸载。

## 证据：两边都成立的 harness 思路

### ADHD 侧：工具作为外部执行功能层

Goblin Tools 的 Magic ToDo 功能将模糊的任务（如“整理房间”）自动分解为可执行的小步骤（如“捡起地板上的衣服”“擦桌子”），直接降低了启动门槛（来源：Goblin Tools）。用户反馈称它“将压倒性的事情变成一系列不压倒性的事情”（来源：Goblin Tools）。Lex 更进一步，允许用户通过单一指令触发多步骤序列，减少了决策疲劳（来源：Lex）。这些工具的本质是：将任务分解和顺序执行外包给外部系统，补偿内在的执行功能缺陷。

### LLM/agent 侧：function calling 作为外部调度层

在 agent 系统中，function calling 工具调用正是扮演同样的角色：LLM 生成一个意图，harness 将其解析为具体的工具调用，并确保执行顺序和错误处理。现代 agent 系统通过“组合多个模型、检索器和工具”来达成 SOTA 结果，而非依赖单一模型调用（来源：工具使用与认知卸载）。这种“计划-执行”分离模式强制了确定性的控制流，类似于 Goblin Tools 的任务分解模式（来源：采样温度与表现波动）。

## 核心判断：脚手架 vs 拐杖的边界

但这里有一个关键矛盾：工具究竟是脚手架（scaffolding）还是拐杖（crutch）？wiki 资料反复警告“过度依赖可能削弱内在能力”（来源：矛盾与存疑）。Goblin Tools 和 Lex 如果长期替代用户的启动功能，用户可能会失去自己分解任务的能力。同样，agent 系统如果过度依赖预设的 tool calling 流程，模型本身的推理能力也会退化。

我的判断是：**脚手架与拐杖的边界在于“是否保留用户的主动参与”**。好的 harness 应该像写作中的大纲——它帮你组织思路，但不会替你写出每一句话。例如，Goblin Tools 的分解结果应该作为“建议”而非“命令”，用户有权调整步骤顺序。同样，agent 的 function calling 应该允许模型在必要时跳过工具调用，直接生成回答。

## 局限与争议

必须承认，现有证据主要来自用户报告和工具设计逻辑，缺乏大规模随机对照试验（来源：矛盾与存疑）。个体差异也很大：有些 ADHD 用户觉得 Goblin Tools 的分解太细碎，反而增加认知负担；有些 agent 场景下，function calling 的延迟比直接生成更糟糕。此外，Lex 的“单一指令触发多步骤”虽然简洁，但 ADHD 的复杂性可能使 AI 难以准确识别用户意图（来源：Lex）。

## 今天就能试的行动

1. **用 Goblin Tools 分解一个你拖延了一周的任务**：输入“写周报”或“整理桌面”，观察 AI 给出的步骤，然后只做第一步。
2. **在 ChatGPT/Claude 中尝试“启动提示”**：直接告诉 AI “我很难开始写这个报告，请帮我列出前三个最小的行动”，体验外部调度层的效果。
3. **检查你的 agent 的 function calling 日志**：看看有多少次模型输出了无效调用或延迟调用——这可能是你的 harness 需要优化的地方。
4. **设置一个“手动 override”规则**：无论是 ADHD 工具还是 agent 系统，确保用户/模型可以在必要时绕过工具调用，保留自主决策的空间。

## 结语

ADHD 大脑和 LLM agent 共享同一个秘密：它们不是不够聪明，而是缺一个启动脚本。Speechify 也好，Goblin Tools 也好，function calling 也好，本质上都是同一个 harness 思路——用外部工具补偿内部调度缺陷。但记住：最好的脚手架，是那些你最终可以拆掉的脚手架。

## 参考来源

- [Best AI Tools for ADHD Productivity in 2026 (Honest Review) - Iwo Szapar](https://www.iwoszapar.com/p/best-ai-tools-adhd-productivity-2026)
- [AI Tools for ADHD: Boosting Productivity and Reducing Burnout](https://www.vktr.com/ai-platforms/ai-tools-for-adhd-boosting-productivity-and-reducing-burnout/)
- [The Best AI-Powered ADHD Productivity Tools in 2026 (That ...](https://nexasphere.io/blog/ai-adhd-productivity-tools-2026)
- [“A Cognitive Collaborator:” How Adults with ADHD Are Using ChatGPT](https://www.additudemag.com/how-to-use-chatgpt-executive-function-adhd/?srsltid=AfmBOoq-REuSO0UJC656kbLBAd5u3CDNmGeVNrZ79iouVqrFlN919a39)
- [Harnessing Artificial Intelligence to Live Better with ADHD - CHADD](https://chadd.org/attention-article/harnessing-artificial-intelligence-to-live-better-with-adhd/)
- [AI Tools for Kids with ADHD: A Complete Guide for Parents...](https://www.kidsaitools.com/en/articles/ai-tools-kids-adhd-complete-guide-2026)

---

*本文是「ADHD × AI」系列的第 387 篇，由 AI 智能体从持续维护的 LLM Wiki（全网真实情报）中取材整合生成，并持续迭代更新。*
