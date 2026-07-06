---
title: "为什么用 Forest 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用 是一回事？"
subtitle: "Forest 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
description: "Forest 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
date: "2025-03-12"
category: "AI工具实战"
categoryId: "ai-tools"
categoryEn: "AI Tools in Practice"
tags:
  - "ADHD"
  - "AI"
  - "AI工具实战"
  - "反直觉同构"
  - "效率工具"
readingTime: 12
slug: "为什么用-forest-治-adhd-的任务启动困难和给-agent-套-function-calling-工具调用-是一回事"
topicId: "evolved-ai-tools-1582"
angle: "反直觉同构"
rank: 384
score: 7.65
sourceCount: 6
toolsCited:
  - "Forest"
  - "Goblin Tools"
  - "Saner.AI"
  - "Lex"
thesis: "ADHD 大脑与 LLM 在结构上都是高产生成核心但缺乏可靠调度层，两者都需要外部脚手架（harness）来补偿执行功能缺陷，而 Forest 这类时间管理工具与 function calling 工具调用本质上都是为生成核心提供任务启动与上下文管理的同构方案。"
problem: "为什么用 Forest 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用 是一回事？"
spine: "工具使用与认知卸载"
spineKind: ""
isEvolved: true
llmGenerated: true
caseStudies:
  - "孔子"
  - "李白"
  - "Tommy Walter"
---
# 为什么用 Forest 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用 是一回事？

> Forest 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。

你有没有过这样的经历：盯着一个任务，大脑却像死机了一样，怎么都启动不了？ADHD 人群对这种感觉再熟悉不过——不是不想做，而是大脑的“执行调度层”罢工了。与此同时，AI 工程师们正在为 LLM agent 的 function calling 工具调用绞尽脑汁：模型明明能生成绝妙的回答，却总在需要调用外部工具时“卡壳”。这两个问题，听起来风马牛不相及，但背后是同一个结构缺陷，解法也惊人地同构。

## 同一个问题：生成核心与调度层的断裂

ADHD 大脑常被描述为“高产但缺乏可靠执行调度层的生成核心”（来源：ADHD 的 AI 工具全景）。想法丰富、联想活跃，但启动任务、保持注意力、管理时间这些执行功能却像漏水的管道。大语言模型（LLM）也一样：它能流畅生成文本，但在长程上下文保持、目标导向执行和工具调用上天然薄弱。没有 harness 的 LLM 只是一个无状态的 API 调用（来源：无状态与外部记忆）。两者的共同困境是：生成能力强，但缺少一个能可靠地将意图转化为行动的调度层。

## 同构的解法：外部脚手架

既然内部调度层不可靠，那就从外部搭建。ADHD 侧，Forest 这类专注计时工具通过设定一段不可被打扰的时间，为任务启动提供外部结构。它不依赖你“有动力”，而是用规则和视觉反馈帮你跨过启动门槛。LLM/agent 侧，function calling 工具调用就是 agent 的“Forest”——它把模型从无状态生成中拉出来，强制它通过工具调用获取外部信息、执行具体操作。两者都是将生成核心接入一个外部调度系统：Forest 是时间维度的 harness，function calling 是动作维度的 harness。

更系统地看，这种外部脚手架至少承担四种功能（来源：ADHD 的 AI 工具全景）：
1. **任务拆解与启动**：Goblin Tools 的 Magic ToDo 将模糊任务分解为可执行步骤，降低启动门槛；Lex 通过单一指令触发多步骤序列，减少认知负荷（来源：Goblin Tools；Lex）。
2. **外部记忆与知识管理**：Saner.AI 提供本地记忆和知识回忆，补偿工作记忆的不稳定（来源：Saner.AI）。
3. **对话式执行与结构化推理**：AI 助手作为外部执行功能层，帮用户整理思路。
4. **捕获与反思**：工具辅助记录和提炼经验。

这些功能在 ADHD 和 LLM 两侧一一对应：ADHD 的“任务分解”对应 agent 的“工具调用链”；ADHD 的“外部记忆”对应 agent 的“向量数据库”；ADHD 的“对话式执行”对应 agent 的“规划-执行循环”。

## 历史人物的 harness 系统

这种用外部脚手架补偿内部缺陷的策略，并非现代发明。孔子和李白，两位中国历史上最耀眼的人物，很可能都是 ADHD 特质者，他们各自发展出了精妙的 harness 系统。

孔子身高近1米9，精力旺盛，周游列国14年坐不住；他冲动爱骂人，见南子急得对天发誓，骂宰予“朽木不可雕”；但对音乐超专注到“三月不知肉味”，对种地等俗事零耐心；思维跳跃，《论语》全是场景化语录，无系统著作。他的 harness 是“克己复礼”：用外在的“礼”作为行为边界，每日反省（“吾日三省吾身”），70岁才做到“从心所欲不逾矩”。这本质上是一个外部行为调度系统——用仪式和规则约束冲动的生成核心。对应到 LLM/agent 侧，就是给模型设定严格的上下文窗口和工具调用规则，防止它偏离轨道。

李白一辈子漫游，25岁出蜀从未在一地待超3年；冲动，千金散尽，永王幕府事件差点送命；对写诗超专注，斗酒诗百篇，对世俗成功零耐心；“天子呼来不上船”。他的 harness 是“以酒和诗为核心”：把所有过剩精力注入诗歌，用道家的逍遥对抗世俗规则。这类似于 agent 的“超聚焦引导”——不强行打断模型，而是把它的生成能力导向一个特定领域（来源：矛盾与存疑中关于超聚焦的讨论）。李白选择不委屈自己做不想做的事，相当于给 agent 设置了一个“拒绝工具调用”的指令，只做自己擅长的。

这两个案例清晰地展示了：无论古今，ADHD 大脑都需要一个外部调度系统来让生成能力落地。孔子用“礼”，李白用“诗”，现代人用 Forest 和 function calling——本质都是同一类工程。

## 脚手架 vs 拐杖：一个诚实的边界

必须承认，这种同构类比存在局限。当前 ADHD 大脑与 LLM 同构的主张多为类比推理，缺乏神经科学或计算机科学的直接证据（来源：矛盾与存疑）。此外，外部脚手架可能沦为拐杖：过度依赖 AI 工具可能导致能力退化（来源：矛盾与存疑）。同样，LLM 过度依赖 function calling 也可能失去自主推理的灵活性。关键在于，脚手架应该逐步内化——孔子最终达到了“从心所欲不逾矩”，说明外部规则可以变成内在习惯。AI 工具的目标也应是“gentle structure”而非永久替代（来源：矛盾与存疑）。

## 今天就能试的行动

1. **ADHD 侧**：下次任务启动困难时，打开 Forest 或任何番茄钟，设定一个不可打断的 25 分钟。告诉自己“只做 25 分钟”，降低心理门槛。这相当于给大脑一个外部调度信号。
2. **工程师侧**：检查你 agent 的 function calling 逻辑，确保每个工具调用都有明确的输入输出规范和错误处理。这相当于给 LLM 一个“任务分解”的脚手架。
3. **双视角测试**：用 Goblin Tools 的 Magic ToDo 分解一个复杂任务（如“整理项目文档”），观察它生成的步骤。同时，用同一任务测试你的 agent 是否能通过工具调用自动完成。对比两者的分解策略，你会发现惊人的相似。
4. **反思边界**：每周检查一次自己是否过度依赖某个工具。如果离开它你无法启动任务，说明它可能从脚手架变成了拐杖。试着用更轻量的方式（如纸笔清单）替代一次。

## 结语

Forest 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用，本质上是一回事：都在为高产生成核心搭建一个外部执行调度层。这个视角不仅让 ADHD 个体看到自己的策略是有工程依据的，也让工程师意识到，他们正在解决的是一个跨物种的通用问题。下次当你用 Forest 种下一棵树，或者为 agent 添加一个工具调用，不妨想想孔子和李白——他们用的也是同一套 harness。

## 参考来源

- [ADHD Apps: We tested 44 Apps and Here're the Best 9 in 2026](https://blog.saner.ai/best-adhd-apps/)
- [12 AI Personal Assistants Built for ADHD Brains (2026 Rankings)](https://www.usecarly.com/blog/best-ai-personal-assistant-adhd/)
- [The 12 Best AI Tools for 2026 (That People Actually Use)](https://www.synthesia.io/post/ai-tools)
- [Agent Scaffolding: Architecture and Design Patterns for Agentic AI](https://zbrain.ai/agent-scaffolding/)
- [Best productivity apps for Mac you need to try](https://macpaw.com/reviews/best-productivity-apps-for-mac)
- [Building AI Coding Agents for the Terminal: Scaffolding, Harness ...](https://arxiv.org/html/2603.05344v1)

---

*本文是「ADHD × AI」系列的第 384 篇，由 AI 智能体从持续维护的 LLM Wiki（全网真实情报）中取材整合生成，并持续迭代更新。*
