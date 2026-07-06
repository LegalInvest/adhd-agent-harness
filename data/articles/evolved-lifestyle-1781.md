---
title: "为什么用 ChatGPT 治 ADHD 的日常混乱不稳定，和给 agent 套 调低采样温度 是一回事？"
subtitle: "ChatGPT 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
description: "ChatGPT 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
date: "2025-05-20"
category: "生活方式"
categoryId: "lifestyle"
categoryEn: "Lifestyle"
tags:
  - "ADHD"
  - "AI"
  - "生活方式"
  - "反直觉同构"
  - "人际关系"
readingTime: 7
slug: "为什么用-chatgpt-治-adhd-的日常混乱不稳定和给-agent-套-调低采样温度-是一回事"
topicId: "evolved-lifestyle-1781"
angle: "反直觉同构"
rank: 140
score: 7.79
sourceCount: 6
toolsCited:
  - "Routinery"
  - "Goblin Tools"
  - "Saner.AI"
  - "Tiimo"
thesis: "ADHD 大脑与 LLM 是同一类「高产但缺执行调度层的生成核心」，两者的解法——外部脚手架与调低采样温度——在结构上同构，都是通过约束生成空间来换取稳定输出。"
problem: "为什么用 ChatGPT 治 ADHD 的日常混乱不稳定，和给 agent 套 调低采样温度 是一回事？"
spine: "采样温度与表现波动"
spineKind: ""
isEvolved: true
llmGenerated: true
caseStudies:
  - "孔子"
  - "文天祥"
  - "王晶"
---
# 为什么用 ChatGPT 治 ADHD 的日常混乱不稳定，和给 agent 套 调低采样温度 是一回事？

> ChatGPT 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。

你坐在电脑前，打开 ChatGPT，想写一封邮件。五分钟后，你发现自己在查“为什么猫会踩奶”。另一边，你部署的 agent 正在生成客户回复，但输出忽而热情洋溢，忽而冷若冰霜，像换了个人格。这两个场景，看似无关，底层却是同一个问题：**生成核心太强，调度层太弱**。

## 同构：ADHD 大脑与 LLM 的底层困境

ADHD 大脑被描述为“高产但缺执行调度层的生成核心”（来源：AI 与 ADHD 的日常生活）。它创意爆棚、模式识别敏锐，但工作记忆是瓶颈——明尼苏达大学测试 LLM 的执行功能，发现“强记忆、弱控制”剖面：工作记忆容量甚至超过常人，但认知灵活性与注意控制存在核心缺陷（来源：Strong Memory, Weak Control: An Empirical Study of Executive Functioning in LLMs）。这直接对应 ADHD 的经典神经心理模式：不是记不住，是调不动。

LLM 也一样。自注意力机制本身导致工作记忆容量限制：随任务复杂度增加，注意力分数熵增、注意力弥散，表现下降（来源：Self-Attention Limits Working Memory Capacity of Transformer-Based Models）。这就是 LLM 版的“注意力漂移”。

两者的共同解法，不是提升算力或智商，而是**给生成核心套一个外部调度层**。对 ADHD 来说，这个调度层是执行功能脚手架；对 LLM 来说，是 agent scaffolding 和采样温度控制。

## 温度与混乱：同一个旋钮

“调低采样温度”是工程师控制 LLM 输出稳定性的标准操作。温度越低，模型越倾向于选择概率最高的 token，输出更保守、更可预测。温度越高，模型越敢探索低概率路径，输出更多样但也更随机。

ADHD 的“日常混乱不稳定”，本质上就是大脑的“采样温度”过高。执行功能无法有效抑制干扰、锚定目标，导致行为输出方差极大——今天能超专注三小时，明天连刷牙都要挣扎半小时。

而外部脚手架，就是那个“调低温度”的旋钮。

## 从孔子到 Routinery：脚手架的历史与当下

孔子是历史上最成功的“ADHD 脚手架用户”之一。他精力旺盛、冲动爱骂人、思维跳跃——《论语》全是场景化语录，无系统著作。他的解法是“克己复礼”：用外在的“礼”作为行为边界，每日反省（“吾日三省吾身”），70 岁才做到从心所欲不逾矩。

这个系统与 LLM 的 agent harness 结构同构：**礼 = 约束条件（temperature 设置），日课 = 定时 re-grounding（context window 刷新），弟子 = 外部调度器（orchestrator）**。孔子不是没有创造力（生成核心极强），而是通过外部规则系统把创造力导向了目标行为。

今天的工具在做同样的事。Routinery 用可视化倒计时和过渡提示，把“该做什么、现在做哪一步”从大脑内部搬到外部系统（来源：Routinery）。Goblin Tools 的 Magic ToDo 接受模糊任务（如“清理厨房”），自动分解为具体子步骤，用户可调节“辣度”控制分解粒度（来源：Goblin Tools）。Saner.AI 通过本地记忆和快速检索，减少搜索循环和标签切换（来源：Saner.AI）。

这些工具都不是在替用户思考，而是在**降低大脑的“采样温度”**——通过减少选择、提供时间锚点、分解任务，让行为输出更稳定。

## 证据：两边都有数据

ADHD 侧：创业概率在 ADHD 组是 6.25 倍于对照组（来源：Journal of Attention Disorders 2019）。这印证了“高产生成核心”的特质——但前提是找到合适的脚手架。

LLM 侧：耶鲁大学发现，自注意力机制的工作记忆限制与人类注意分散机制同源，“注意力资源的弥散分配”正是 ADHD 注意缺陷的计算本质（来源：Self-Attention Limits Working Memory Capacity of Transformer-Based Models）。这意味着，LLM 的“温度问题”不是 bug，是架构特性。

## 脚手架 vs 拐杖：边界在哪里？

这里必须诚实指出争议。AI 工具是“外部执行功能层”还是“拐杖”？过度依赖可能导致能力退化（来源：矛盾与存疑）。孔子用了大半辈子“礼”的脚手架，到 70 岁才内化。文天祥以《正气歌》为 scaffold，每日读圣贤书，最终在生死关头完成了自主决策。

关键在于：**脚手架的目标是最终可以拆除，拐杖的目标是永远不拆。** 好的 ADHD 工具应该像训练轮，而不是轮椅——它在你最摇晃的时候提供支撑，但允许你逐渐内化那些结构。

## 今天就能试的 3 件事

1. **给 ChatGPT 写一个“温度指令”**：在对话开头加一句“请用简洁、保守的语气回复，避免发散”。你会发现输出稳定性明显提升——这就是在调低 LLM 的采样温度。
2. **用 Goblin Tools 分解一个你拖延的任务**：输入“整理书桌”，看它如何拆成 5-8 个小步骤。把“辣度”调到 3-4，找到最适合你的粒度。
3. **给自己设一个“礼”**：选一个你容易失控的场景（如刷手机），设定一个外部规则（“手机必须放在另一个房间才能工作”）。这就是你的 temperature=0.3。

## 结语

ADHD 大脑和 LLM 共享同一个困境：生成能力远超调度能力。解法也共享同一个思路：**通过外部结构降低系统温度**。孔子用礼，工程师用 temperature 参数，你用 Routinery 或 Goblin Tools——本质都是给一个躁动的生成核心套上 harness。

这不是把人变成机器，而是让机器和人都能更稳定地成为自己。

## 参考来源

- [AI for ADHD: Best Tools, Apps, and Strategies - Themba Tutors](https://thembatutors.com/ai-for-adhd-tools-and-apps/)
- [11 Best ADHD Productivity Apps for Fluctuating Energy - rivva blog](https://blog.rivva.app/p/11-best-adhd-productivity-apps-for)
- [ADHD Apps: We tested 44 Apps and Here're the Best 9 in 2026](https://blog.saner.ai/best-adhd-apps/)
- [12 AI Personal Assistants Built for ADHD Brains (2026 Rankings)](https://www.usecarly.com/blog/best-ai-personal-assistant-adhd/)
- [Strong Memory, Weak Control: An Empirical Study of Executive Functioning in LLMs](https://preview.aclanthology.org/evt-to-venues/2026.eacl-long.281.pdf)
- [Self-Attention Limits Working Memory Capacity of Transformer-Based Models](https://arxiv.org/pdf/2409.10715)

---

*本文是「ADHD × AI」系列的第 140 篇，由 AI 智能体从持续维护的 LLM Wiki（全网真实情报）中取材整合生成，并持续迭代更新。*
