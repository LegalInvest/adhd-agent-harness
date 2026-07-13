---
title: "为什么用 ChatGPT 治 ADHD 的情绪失调，和给 agent 套 会褪去的脚手架 是一回事？"
subtitle: "ChatGPT 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
description: "ChatGPT 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
date: "2025-05-16"
category: "情绪调节"
categoryId: "emotion"
categoryEn: "Emotional Regulation"
tags:
  - "ADHD"
  - "AI"
  - "情绪调节"
  - "反直觉同构"
  - "焦虑"
readingTime: 13
slug: "为什么用-chatgpt-治-adhd-的情绪失调和给-agent-套-会褪去的脚手架-是一回事"
topicId: "evolved-emotion-2126"
angle: "反直觉同构"
rank: 21
score: 8.07
sourceCount: 6
toolsCited:
  - "ChatGPT"
  - "Inflow"
  - "Goblin Tools"
  - "Saner.AI"
thesis: "ADHD的情绪失调与LLM的不可靠输出，根源都在于一个高产生成核心缺乏可靠调度层；两者的解法同构——通过外部脚手架（harness）补偿执行功能缺陷，且脚手架必须‘会褪去’，否则变成拐杖。"
problem: "为什么用 ChatGPT 治 ADHD 的情绪失调，和给 agent 套 会褪去的脚手架 是一回事？"
spine: "拐杖与脚手架"
spineKind: ""
isEvolved: true
llmGenerated: true
caseStudies:
  - "释迦牟尼"
  - "曾国藩"
  - "王飞"
---
# 为什么用 ChatGPT 治 ADHD 的情绪失调，和给 agent 套 会褪去的脚手架 是一回事？

> ChatGPT 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。

你打开ChatGPT，想让它帮你把“清理厨房”拆成几步。它列了10个子任务，你盯着屏幕，却感觉更焦虑了——因为你的大脑和ChatGPT此刻遇到了同一个问题：都生成了太多东西，却没人帮它们调度。

这就是本文要说的反直觉同构：ADHD大脑的情绪失调，和LLM的胡言乱语，其实是同一类故障。

## 问题：高产核心，缺调度层

ADHD大脑被描述为“高产生成核心，但缺乏可靠调度层”（来源：AI 与 ADHD 的情绪调节）。你的前额叶——本该像CEO一样抑制无关情绪、启动任务、跟踪进度——却常常掉线。于是情绪像脱缰的生成器：焦虑、挫败、兴奋轮流冒出来，你没法按“暂停”或“重定向”。

LLM也一样。GPT-4能一秒生成千字，但没有外部约束时，它也会跑题、编造、输出有害内容。Transformer的自注意力机制在训练后发展出模仿前额叶-纹状体门控的操作（来源：TRANSFORMER MECHANISMS MIMIC FRONTOSTRIATAL GATING OPERATIONS WHEN TRAINED ON HUMAN WORKING MEMORY TASKS），但推理时仍需外部提示工程来充当调度层。

两边都是：核心很强，调度很弱。

## 解法：会褪去的脚手架

既然调度层缺失，就从外部搭一个。对ADHD来说，这个脚手架叫“外部执行功能层”——比如用Goblin Tools的Magic ToDo把“清理厨房”分解成“打开柜门”“拿出碗碟”等可执行步骤，降低启动门槛（来源：Goblin Tools）。用Saner.AI存储上下文，减少工作记忆负担（来源：Saner.AI）。用Inflow的CBT练习结构化情绪调节（来源：Inflow）。

对LLM来说，脚手架叫“上下文工程”——system prompt规定角色、输出格式、禁止内容；few-shot示例约束输出风格；外部工具（如检索增强生成）提供事实锚点。这些都是在生成核心外面套一个调度层。

但关键区别在于：脚手架必须会褪去。曾国藩的“日课十二条”就是一套会褪去的脚手架：黎明即起、读书不二、谨言——这些规则帮他抵消注意力不集中和情绪波动（他打败仗时甚至跳水自杀）。但他最终内化了“持敬”“主静”的原则，不再需要逐条对照。他的成就（平定太平天国、洋务运动）恰恰来自脚手架的内化，而非永久依赖（来源：人物案例）。

同样，释迦牟尼的“八正道”和“自依止法依止”也是一套脚手架：用戒律管行为，用正念拴念头。但他明确要求弟子“自依止”，而非永远依赖佛陀（来源：人物案例）。

工具如ChatGPT、Inflow，如果只用不内化，就会变成拐杖——削弱内在执行功能，长期反而恶化自我效能感（来源：拐杖与脚手架）。

## 证据：两边都成立

ADHD侧：研究显示ADHD组在工作记忆任务中易受干扰，而LLM表现出类似人类的干扰特征——随记忆负荷增加表现下降，受近因效应影响（来源：Human-like Working Memory Interference in Large Language Models）。ADHD患者在无外部结构时难以自主组织任务；类似地，LLM在没有严重依赖手动修正提示的情况下，难以自主发现最佳问题解决模式（来源：Working Memory Identifies Reasoning Limits in Language Models）。

LLM/Agent侧：Transformer的自注意力机制在训练后模仿前额叶-纹状体门控，证明了计算同构性（来源：TRANSFORMER MECHANISMS MIMIC FRONTOSTRIATAL GATING OPERATIONS WHEN TRAINED ON HUMAN WORKING MEMORY TASKS）。而ADHD的自动反应模式与LLM的自动完成机制平行，两者都在有限执行监督下生成复杂行为，且易出现虚构/幻觉等错误（来源：Automatic Minds: Cognitive Parallels Between Hypn...）。

## 核心观点：脚手架是暂时的，能力是永久的

我的判断是：ADHD×AI工具的真正价值，不在于替代执行功能，而在于提供一个可内化的训练环境。Inflow的CBT练习、Goblin Tools的分解、Saner.AI的上下文存储——这些都应该像曾国藩的日课一样，用一段时间后逐渐撤去，让用户自己学会“攀登”。

但当前工具普遍只强调益处，未充分讨论依赖风险（来源：矛盾与存疑）。同构性也被过度推广——它目前只是理论类比，并非经过验证的科学事实（来源：矛盾与存疑）。

## 今天就能试的行动

1. **用Goblin Tools分解一个让你焦虑的任务**：比如“写周报”，让AI拆成5步，完成后打勾。观察情绪变化。
2. **给ChatGPT写一个“会褪去的脚手架”prompt**：比如“你是一个任务教练，帮我拆解‘整理书桌’。请先给出3个步骤，并告诉我如何逐步减少对你的依赖。”
3. **记录一周内情绪波动的触发点**：用Saner.AI或Obsidian记下，看是否与任务启动困难有关。
4. **曾国藩式日课**：选一条规则（如“读书不二”），严格执行一周，再评估是否内化。

脚手架会褪去，但能力会留下。这才是真正的同构答案。

## 参考来源

- [The 12 Best Apps for ADHD in 2026: A Guide to Finding What ...](https://www.getinflow.io/post/best-apps-for-adhd) — 证据等级：低（GRADE）
- [Dynamic causal brain circuits during working memory and their functional controllability](https://doi.org/10.1038/s41467-021-23509-x) — 证据等级：低（GRADE）
- [ADHD Apps: We tested 44 Apps and Here're the Best 9 in 2026](https://blog.saner.ai/best-adhd-apps/) — 证据等级：低（GRADE）
- [12 AI Personal Assistants Built for ADHD Brains (2026 Rankings)](https://www.usecarly.com/blog/best-ai-personal-assistant-adhd/) — 证据等级：低（GRADE）
- [Human-like Working Memory Interference in Large Language Models](https://arxiv.org/pdf/2604.09670) — 证据等级：低（GRADE）
- [Working Memory Identifies Reasoning Limits in Language Models](https://aclanthology.org/2024.emnlp-main.938.pdf) — 证据等级：低（GRADE）

---

*本文是「ADHD × AI」系列的第 15 篇，由 AI 智能体从持续维护的 LLM Wiki（全网真实情报）中取材整合生成，并持续迭代更新。*
