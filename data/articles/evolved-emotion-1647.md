---
title: "为什么用 Routinery 治 ADHD 的情绪失调，和给 agent 套 会褪去的脚手架 是一回事？"
subtitle: "Routinery 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
description: "Routinery 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
date: "2025-05-10"
category: "情绪调节"
categoryId: "emotion"
categoryEn: "Emotional Regulation"
tags:
  - "ADHD"
  - "AI"
  - "情绪调节"
  - "反直觉同构"
  - "自我接纳"
readingTime: 7
slug: "为什么用-routinery-治-adhd-的情绪失调和给-agent-套-会褪去的脚手架-是一回事"
topicId: "evolved-emotion-1647"
angle: "反直觉同构"
rank: 398
score: 7.65
sourceCount: 6
toolsCited:
  - "Routinery"
  - "Inflow"
  - "Goblin Tools"
  - "Saner.AI"
  - "Motion"
  - "Tiimo"
thesis: "ADHD 的情绪失调与 LLM 的上下文失控共享同一底层缺陷：高产但缺乏可靠执行调度层的生成核心。Routinery 通过结构化重复（外部执行层）补偿 ADHD 的调度缺陷，而 agent 的“会褪去的脚手架”通过临时约束补偿 LLM 的上下文漂移——两者本质都是给生成核心套上可渐撤的 harness，而非永久拐杖。"
problem: "为什么用 Routinery 治 ADHD 的情绪失调，和给 agent 套 会褪去的脚手架 是一回事？"
spine: "拐杖与脚手架"
spineKind: ""
isEvolved: true
llmGenerated: true
---
# 为什么用 Routinery 治 ADHD 的情绪失调，和给 agent 套 会褪去的脚手架 是一回事？

> Routinery 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。

## 问题：情绪怎么就成了那个“失控的 agent”？

如果你有 ADHD，你一定经历过这种时刻：明明只是被一句评论刺到，情绪却像脱缰的 agent 一样横冲直撞，理性提示“冷静”完全无效。你事后分析，发现触发点很小，但当时的你就像被一个没有上下文约束的 LLM 劫持——输出完全偏离轨道。

如果你在做 agentic harness 工程，你也一定见过这种场面：一个精心设计的 agent 在简单任务上表现完美，但一旦上下文窗口被污染或指令模糊，它就开始“幻觉”——生成看似合理但完全脱离目标的输出。

这两件事，在结构上是同一件事。ADHD 大脑与 LLM 是同一类“高产但缺执行调度层的生成核心”（来源：ADHD 大脑与 LLM 的同构）。情绪失调，就是 ADHD 大脑的“上下文失控”——当工作记忆过载或注意力被干扰时，情绪反应如同 LLM 的幻觉，脱离理性轨道（来源：AI 与 ADHD 的情绪调节）。而解法，也共享同一套逻辑：给生成核心套上一个会褪去的脚手架。

## 同构：Routinery 与“会褪去的脚手架”

Routinery 是一款基于结构化重复的 ADHD 辅助工具。它的核心机制是：把每天必须完成的任务（如起床、刷牙、吃药）编排成固定序列，通过重复执行降低启动阻力。对 ADHD 用户来说，Routinery 就像一个外部执行调度器——它接管了“什么时候做什么”的决策，让大脑的生成核心（创造力、冲动、情绪）有了可预测的轨道。

这恰恰是 agentic harness 工程中“会褪去的脚手架”的镜像。在 LLM agent 开发中，常需要给模型套上临时约束：固定输出格式、限定上下文窗口、提供 few-shot 示例。这些约束不是永久的——一旦 agent 学会在目标范围内稳定输出，脚手架就可以逐步撤掉。Routinery 的“重复序列”也是同样的逻辑：它不是让你永远依赖它，而是通过重复训练，让大脑的内隐记忆逐渐接管（来源：拐杖与脚手架）。

但关键在于：脚手架 vs 拐杖的边界在哪里？Wiki 资料明确指出，过度依赖 AI 工具可能削弱内在情绪调节能力（来源：矛盾与存疑）。Routinery 如果被用成“没有它我就无法启动”的拐杖，那就违背了脚手架的设计初衷。真正的脚手架，应该在能力增长后自然褪去——就像训练 agent 时，最终目标是让它在无约束下也能稳定输出。

## 证据：两边的真实案例

**ADHD 侧**：Inflow 通过训练工作记忆来改善执行功能，其神经科学依据是背外侧前额叶皮层作为因果流入中枢（来源：Inflow）。但用户报告显示，效果因人而异（来源：矛盾与存疑）。Goblin Tools 的 Magic ToDo 功能将复杂任务分解为小步骤，降低启动门槛（来源：Goblin Tools）。用户反馈称“它把压倒性的事情变成一系列不压倒性的事情”（来源：Goblin Tools）。Saner.AI 通过知识回忆减少搜索循环（来源：Saner.AI），这直接针对 ADHD 的工作记忆缺陷——但同样缺乏独立 RCT（来源：矛盾与存疑）。

**LLM/agent 侧**：在 agent 工程中，会褪去的脚手架通常表现为：初期提供 strict schema 和 step-by-step 提示，后期逐步放宽。例如，一个用于客户支持的 agent，最初被约束为“只能回答预设 FAQ”，随着训练数据积累，约束被替换为“参考知识库后自由回答”。这与 ADHD 工具的逻辑完全平行：Routinery 提供固定序列（约束），Motion 和 Tiimo 通过 AI 自动规划日程（动态约束），但最终目标都是让用户/agent 内化调度能力。

## 核心判断：脚手架必须包含“褪去机制”

我在这里提出一个鲜明的观点：**任何声称帮助 ADHD 的工具，如果缺乏“渐撤计划”，本质上都是拐杖。** 现有的 ADHD 工具，包括 Routinery、Inflow、Goblin Tools，都强调“补偿”而非“训练”。Wiki 资料也承认，AI 工具作为外部执行功能层的有效性证据不足（来源：矛盾与存疑），且存在依赖风险。这让我怀疑：这些工具是否真的在构建脚手架？还是只是在卖拐杖？

一个合格的脚手架，应该内置“褪去机制”：比如 Routinery 可以设置“每执行 30 天后减少一次提示”；Inflow 可以在工作记忆提升后自动降低训练强度。但目前的工具几乎都没有这个功能。这或许是因为，商业上“永久依赖”比“成功褪去”更有利可图——但这对用户是不负责任的。

## 局限与争议

必须诚实指出：本文的同构论证主要基于概念类比，而非严格的神经科学或工程研究。ADHD 的情绪失调与 LLM 的上下文失控在生物学机制上完全不同，只是功能层面相似。另外，ADHD 亚型不同（注意缺陷型 vs. 多动冲动型）对工具的反应差异大（来源：矛盾与存疑），而 agent 的“上下文失控”也有技术原因（如 token 限制、注意力机制缺陷）。这些差异意味着，同构不能简单映射为“同一个解决方案”。

## 今天就能试的行动

1. **测试你的“脚手架褪去阈值”**：如果你在用 Routinery，尝试每周减少一次序列中的提示步骤，观察自己的启动能力是否仍然稳定。记录下“褪去”后表现不变的那一天——那就是你的脚手架该撤掉的时刻。
2. **给 agent 设置“约束衰减”实验**：如果你在开发 agent，在测试阶段加入“约束逐步放宽”的脚本。例如，前 10 次交互提供 5 个示例，后 10 次只提供 2 个，观察输出质量变化。这能帮你找到“最小必要约束”。
3. **用 Goblin Tools 分解一个情绪触发任务**：下次情绪波动时，用 Magic ToDo 把“冷静下来”分解为具体步骤（如“深呼吸 3 次”“喝一口水”“写下三个事实”）。这种外部脚手架能打断情绪失控的循环（来源：Goblin Tools）。
4. **建立“情绪日志”作为外部记忆**：利用 Saner.AI 的知识回忆功能，记录每次情绪失调的触发模式和持续时间（来源：Saner.AI）。这相当于给 ADHD 大脑增加了一个“上下文缓存”——就像 agent 的 memory 模块，防止下次被同样的 trigger 劫持。

## 结语

Routinery 治 ADHD 的情绪失调，和给 agent 套会褪去的脚手架，本质都是同一个工程问题：如何让一个强大的生成核心在缺乏可靠调度层时，通过外部约束稳定输出，并最终内化这些约束。但请记住：真正的脚手架，最终是要拆掉的。如果你发现自己或你的 agent 离开了工具就崩溃，那说明你还没有完成“褪去”这一步。而这一步，恰恰是工程中最容易被忽略，也最重要的环节。

## 参考来源

- [Dynamic causal brain circuits during working memory and their functional controllability](https://doi.org/10.1038/s41467-021-23509-x)
- [Best AI Tools for ADHD Productivity in 2026 (Honest Review) - Iwo Szapar](https://www.iwoszapar.com/p/best-ai-tools-adhd-productivity-2026)
- [AI Tools for ADHD: Boosting Productivity and Reducing Burnout](https://www.vktr.com/ai-platforms/ai-tools-for-adhd-boosting-productivity-and-reducing-burnout/)
- [The Best AI-Powered ADHD Productivity Tools in 2026 (That ...](https://nexasphere.io/blog/ai-adhd-productivity-tools-2026)
- [“A Cognitive Collaborator:” How Adults with ADHD Are Using ChatGPT](https://www.additudemag.com/how-to-use-chatgpt-executive-function-adhd/?srsltid=AfmBOoq-REuSO0UJC656kbLBAd5u3CDNmGeVNrZ79iouVqrFlN919a39)
- [Harnessing Artificial Intelligence to Live Better with ADHD - CHADD](https://chadd.org/attention-article/harnessing-artificial-intelligence-to-live-better-with-adhd/)

---

*本文是「ADHD × AI」系列的第 398 篇，由 AI 智能体从持续维护的 LLM Wiki（全网真实情报）中取材整合生成，并持续迭代更新。*
