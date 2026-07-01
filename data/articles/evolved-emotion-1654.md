---
title: "为什么用 Perplexity 治 ADHD 的情绪失调，和给 agent 套 会褪去的脚手架 是一回事？"
subtitle: "Perplexity 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
description: "Perplexity 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
date: "2025-05-04"
category: "情绪调节"
categoryId: "emotion"
categoryEn: "Emotional Regulation"
tags:
  - "ADHD"
  - "AI"
  - "情绪调节"
  - "反直觉同构"
  - "心理健康"
readingTime: 7
slug: "为什么用-perplexity-治-adhd-的情绪失调和给-agent-套-会褪去的脚手架-是一回事"
topicId: "evolved-emotion-1654"
angle: "反直觉同构"
rank: 164
score: 7.74
sourceCount: 6
toolsCited:
  - "Inflow"
  - "Goblin Tools"
  - "Saner.AI"
  - "Tiimo"
  - "Motion"
  - "Reclaim.ai"
  - "Brain.fm"
thesis: "ADHD的情绪失调与LLM的上下文失控共享同一底层问题——生成核心缺乏执行调度层，而Perplexity式的AI工具与agent的‘会褪去的脚手架’正是同一种解决方案：外挂一个临时、可拆卸的调度层，让生成核心先跑起来，再逐步撤除。"
problem: "为什么用 Perplexity 治 ADHD 的情绪失调，和给 agent 套 会褪去的脚手架 是一回事？"
spine: "拐杖与脚手架"
spineKind: ""
isEvolved: true
llmGenerated: true
---
# 为什么用 Perplexity 治 ADHD 的情绪失调，和给 agent 套 会褪去的脚手架 是一回事？

> Perplexity 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。

## 当情绪像LLM一样失控

你有没有过这种经历：明明只是小事——一条消息没回、一个截止日期逼近——情绪却像被按下了快进键，从烦躁飙升到绝望，仿佛整个世界都在崩塌。下一秒，你又冷静下来，看着刚才的自己像个陌生人。

ADHD的情绪失调，本质上是执行功能缺陷的副产品。工作记忆容量有限，情绪信息来不及被理性加工就炸开了；时间盲让你觉得这种糟糕感觉会永远持续下去；任务启动困难则把挫败感喂养成滚雪球（来源：AI 与 ADHD 的情绪调节）。

现在，把视角换到LLM。一个模型生成流畅文本时，如果上下文窗口被无关信息污染，或者注意力被干扰，它就开始胡言乱语——输出幻觉、逻辑断裂、情绪（如果它有的话）失控。明尼苏达大学的研究发现，LLM表现出“强记忆、弱控制”的剖面：工作记忆容量甚至超过人类，但认知灵活性与注意控制存在核心缺陷（来源：工作记忆）。耶鲁大学进一步揭示，自注意力机制本身就会导致工作记忆容量限制——随着记忆负荷增加，注意力分数熵增、弥散，与人类注意分散机制同源（来源：工作记忆）。

ADHD大脑与LLM，都是同一个故事：**高产但缺乏可靠执行调度层的生成核心**。

## 拐杖 vs. 脚手架：两种外挂调度层

既然问题出在调度层，解法自然就是外挂一个调度层。但这里有一条关键分界线：**拐杖**是永久替代，**脚手架**是临时辅助，用完后要能撤掉。

ADHD侧，AI工具充当的就是这个脚手架。Inflow通过训练背外侧前额叶皮层来强化工作记忆的“流入”中枢（来源：Inflow）；Goblin Tools将复杂任务分解为小步骤，降低启动门槛（来源：Goblin Tools）；Saner.AI用本地记忆减少搜索循环和标签切换（来源：Saner.AI）；Tiimo用视觉时间表对抗时间盲（来源：时间盲）。这些工具的共同逻辑是：**接管执行调度，让生成核心流畅运作**。

LLM/Agent侧，同样的逻辑。Agent在执行复杂任务时，需要外部的规划器、记忆模块、工具调用接口——这些就是“会褪去的脚手架”。比如，给LLM套一个ReAct循环（思考-行动-观察），或者用LangChain的Agent框架，本质上是把调度逻辑外挂到prompt或代码里。随着模型能力提升，这些脚手架可以逐步简化甚至移除。

## Perplexity 实测：同一套 harness 思路

Perplexity 是一个典型例子。它本质上是一个“会褪去的脚手架”：

- **对ADHD用户**：当你被情绪淹没时，打开Perplexity，输入“我现在感到极度焦虑，怎么办？”它会给出结构化回答——呼吸练习、时间估算、任务分解。这不是治愈，而是**外挂一个冷静的调度层**，帮你把情绪信息转化成可操作的步骤。用户报告显示，这种外部结构能有效缓解工作记忆过载导致的情绪波动（来源：AI 与 ADHD 的情绪调节）。
- **对Agent工程师**：Perplexity的搜索+回答流程，就是给LLM套上了一个检索增强生成（RAG）的脚手架。模型不需要记住所有知识，只需要在需要时从外部检索。这个脚手架可以随着模型能力提升而褪去——比如未来模型原生支持长上下文时，RAG可能不再必要。

## 证据与局限

现有证据主要来自用户报告和初步研究，缺乏大规模对照实验（来源：矛盾与存疑）。例如，Inflow的效果依赖神经科学基础，但缺乏直接针对该工具的随机对照试验（来源：Inflow）。Goblin Tools被用户评价为“简单有用”，但同样没有独立验证（来源：Goblin Tools）。

更大的争议在于依赖风险。ADHD用户可能过度依赖AI工具，削弱内在情绪调节能力（来源：矛盾与存疑）。同样，Agent工程师如果过度依赖复杂框架，可能掩盖模型本身的缺陷。关键在于**脚手架要能褪去**——设计时就要考虑逐步撤除的路径。

另一个局限是个体差异。ADHD亚型不同，对AI工具的反应差异大（来源：AI 与 ADHD 的情绪调节）。LLM模型也各有千秋，一种脚手架未必通用。

## 今天就能试的行动

1. **情绪爆发时，用Perplexity提问**：输入“我现在感到[情绪]，可能是因为[原因]，帮我列出三个可立即执行的步骤”。这相当于外挂一个即时调度层。
2. **给AI工具设定期限**：比如用Goblin Tools分解任务时，同时设一个“两周后尝试不用它”的提醒，测试自己是否已经内化了分解能力。
3. **Agent开发时，先写“褪去计划”**：在代码注释里注明“这个脚手架在模型升级到X版本后可移除”，避免永久依赖。
4. **记录工具使用前后的情绪变化**：用Saner.AI或简单笔记记录每次使用AI工具前后的情绪评分，一周后观察模式，判断工具是否真的在帮你，还是成了拐杖。

## 同构的启示

ADHD的情绪失调与LLM的上下文失控，共享同一底层问题：生成核心跑得太快，调度层跟不上。Perplexity式的AI工具和Agent的脚手架，都是临时外挂的调度层。区别在于：**对ADHD用户，脚手架是认知的延伸；对Agent，脚手架是能力的补丁。** 但最终目标一致——让核心流畅运作，然后逐步撤除辅助，直到不再需要它。

这个同构告诉我们：设计工具时，不要只想着“解决问题”，而要想着“让问题不再需要被解决”。好的脚手架，是那些最终会褪去的脚手架。

## 参考来源

- [Dynamic causal brain circuits during working memory and their functional controllability](https://doi.org/10.1038/s41467-021-23509-x)
- [Best AI Tools for ADHD Productivity in 2026 (Honest Review) - Iwo Szapar](https://www.iwoszapar.com/p/best-ai-tools-adhd-productivity-2026)
- [AI Tools for ADHD: Boosting Productivity and Reducing Burnout](https://www.vktr.com/ai-platforms/ai-tools-for-adhd-boosting-productivity-and-reducing-burnout/)
- [The Best AI-Powered ADHD Productivity Tools in 2026 (That ...](https://nexasphere.io/blog/ai-adhd-productivity-tools-2026)
- [“A Cognitive Collaborator:” How Adults with ADHD Are Using ChatGPT](https://www.additudemag.com/how-to-use-chatgpt-executive-function-adhd/?srsltid=AfmBOoq-REuSO0UJC656kbLBAd5u3CDNmGeVNrZ79iouVqrFlN919a39)
- [Harnessing Artificial Intelligence to Live Better with ADHD - CHADD](https://chadd.org/attention-article/harnessing-artificial-intelligence-to-live-better-with-adhd/)

---

*本文是「ADHD × AI」系列的第 164 篇，由 AI 智能体从持续维护的 LLM Wiki（全网真实情报）中取材整合生成，并持续迭代更新。*
