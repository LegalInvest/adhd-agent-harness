---
title: "为什么用 Perplexity 治 ADHD 的注意力涣散，和给 agent 套 上下文工程 是一回事？"
subtitle: "Perplexity 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
description: "Perplexity 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
date: "2025-04-02"
category: "专注力管理"
categoryId: "focus"
categoryEn: "Focus Management"
tags:
  - "ADHD"
  - "AI"
  - "专注力管理"
  - "反直觉同构"
  - "专注力"
readingTime: 7
slug: "为什么用-perplexity-治-adhd-的注意力涣散和给-agent-套-上下文工程-是一回事"
topicId: "evolved-focus-2091"
angle: "反直觉同构"
rank: 161
score: 7.71
sourceCount: 6
toolsCited:
  - "Perplexity"
  - "Focusmate"
  - "RescueTime"
  - "Brain.fm"
  - "Forest"
thesis: "ADHD大脑与LLM/agent都是高产但缺乏内置调度层的生成核心，两者都需要外部上下文工程（harness）来补偿执行功能缺陷，Perplexity治ADHD与agent上下文工程本质上是同一套同构方案。"
problem: "为什么用 Perplexity 治 ADHD 的注意力涣散，和给 agent 套 上下文工程 是一回事？"
spine: "上下文工程"
spineKind: ""
isEvolved: true
llmGenerated: true
caseStudies:
  - "曾国藩"
  - "孔子"
  - "辛梅"
---
# 为什么用 Perplexity 治 ADHD 的注意力涣散，和给 agent 套 上下文工程 是一回事？

> Perplexity 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。

你打开Perplexity，输入一个模糊的问题，它立刻给你一篇结构清晰的回答——那一刻，你觉得自己终于能思考了。但关上浏览器，你又被拉回那个熟悉的战场：任务在桌面上堆成山，你刷了十分钟手机，打开文档又关掉，脑子里同时跑着五个念头，一个都抓不住。

这不是你的错。ADHD大脑和LLM共享同一个底层困境：**它们都是强大的生成核心，却缺一个可靠的内置调度层**。LLM能写出诗，但如果不给它护栏，它会跑题、循环、甚至编造事实；ADHD大脑能爆发出惊人的创意和模式识别，但如果没有外部脚手架，它会被环境中的任何信号带偏。Perplexity之于你的注意力涣散，正如上下文工程（harness）之于agent的失控——本质是同一件事：**为生成核心套上执行调度层**。

## 同构：高产但不可靠的生成核心

ADHD大脑的生成核心（发散思维、模式识别、多任务并行）产出极高，但执行功能（任务启动、持续专注、冲动抑制）薄弱（来源：AI Tools for ADHD: Boosting Productivity and Reducing Burnout）。你也许有过这种体验：一个下午能想出三个商业计划，却无法完成一份简单的周报。LLM同样如此——它在文本生成上近乎全能，但直接输出可能偏离目标、陷入循环或产生危险行为（来源：Building an AI Agent Harness from Scratch）。

最新研究揭示了这种同构的神经基础：在经典Stroop冲突任务中，Transformer注意力随序列变长在冲突试次上骤降到随机水平——无法抑制优势反应、无法解决认知冲突，这与ADHD执行功能缺陷的核心标志一一对应（来源：Deficient Executive Control in Transformer Attention）。LLM呈现“强记忆、弱控制”剖面：工作记忆容量甚至超过常人，但认知灵活性与注意控制存在核心缺陷（来源：Strong Memory, Weak Control）。这说的就是ADHD：你不是记不住，你是管不住。

## 两边共享的解法：上下文工程

ADHD侧，最有效的策略是**外部执行功能层**：用工具补偿工作记忆不稳定、任务启动困难和注意力分散（来源：AI 与 ADHD 的专注力）。Focusmate通过虚拟身体在场提供外部问责——你打开视频，对面坐着一个陌生人，你的执行功能障碍就被绕过了（来源：人在回路与身体在场）。RescueTime自动追踪时间，揭示“时间到底去了哪里”，减轻你手动记录的工作记忆负担（来源：Revolutionizing ADHD Management with AI Assistants）。Brain.fm用AI生成神经锁相音乐，帮你进入专注状态（来源：11 Best ADHD Productivity Apps）。这些工具的本质，都是**主动设计“当下注意什么”的工程化方案**。

LLM/agent侧，解法叫**agent harness（脚手架）**。工程师通过human-in-the-loop监督提供外部调度：设置护栏（token预算、工具调用次数上限、防止无限循环）、加入人工检查点（暂停并询问后再执行）（来源：Building an AI Agent Harness from Scratch）。这和你用Focusmate时“暂停并确认进度”的检查点，结构完全一致。Perplexity之所以能帮你治注意力涣散，正是因为它充当了你的外部调度器：你把一个模糊的意图扔给它，它帮你拆解、搜索、整合、输出——就像agent harness帮LLM把目标分解成步骤、调用工具、检查结果。

## 历史中的harness：曾国藩的“日课十二条”

晚清名臣曾国藩，是典型的注意力不集中型ADHD。他30岁前浮躁坐不住，天天串门喝酒看杀人，日记里骂自己“无恒”“浮躁”；读书慢，“他人目下二三行，余或疾读不能终一行”；一辈子严重银屑病，情绪不稳定，打败仗就跳水自杀。他的专属harness是**日课十二条**：黎明即起、读书不二、谨言、写日记反省……用最笨最稳的方法抵消自己的冲动（来源：wiki资料人物案例）。这套系统本质上就是外部调度层：每天固定的re-grounding仪式（黎明即起）、单任务模式（读书不二）、人工检查点（写日记反省）。和agent harness的“定时re-grounding + 护栏 + 人工检查点”完全同构。曾国藩的成功，不是因为他的大脑变好了，而是他建了一套终身运行的harness。

## 脚手架 vs 拐杖：边界在哪？

但这里有一个必须正视的矛盾：AI工具是帮你内化执行功能的脚手架，还是让你永久依赖的拐杖？（来源：拐杖与脚手架）如果曾国藩的日课十二条是他主动内化的系统，那么你用Perplexity查一个概念、用Focusmate完成一次任务——这些行为是否在削弱你自身的能力？

现有证据无法给出答案。多数工具的效果来自用户报告或小样本研究，缺乏大规模随机对照试验（来源：AI 与 ADHD 的专注力）。Brain.fm虽入选2026年最佳9款ADHD应用，但在ADHD人群中的独立临床证据仍有限（来源：Brain.fm）。更关键的是，ADHD的异质性意味着同一工具对不同亚型效果可能迥异（来源：矛盾与存疑）。依赖风险是真实的——但放弃工具，让ADHD大脑裸奔，同样不是答案。

我的判断是：**脚手架与拐杖的边界，不在于工具本身，而在于你是否主动设计它**。曾国藩的日课是他自己写的，不是别人塞给他的；他用它来训练自己，而不是替代自己。同样，你用Perplexity时，如果只是被动接收答案，它就是拐杖；如果你把它当作外部调度器，主动规划“我接下来要关注什么”，它就是脚手架。

## 今天就能试的行动

1. **用Perplexity做一次“注意力审计”**：打开Perplexity，输入“帮我列出今天最重要的三件事，每件事的下一步行动是什么”。把它当作你的外部工作记忆，而不是搜索引擎。
2. **设置一个Focusmate时段**：预约一个25分钟的虚拟身体在场时段，做你最拖延的那件事。注意观察：有人在场时，你的启动阻力是否下降。
3. **用RescueTime（或同类工具）追踪一天**：不看报告，只在睡前问自己：“我今天的时间去了哪里？”对比工具的数据，看看你的直觉与事实差多少。
4. **写一条“日课”**：像曾国藩一样，给自己定一条最简单的规则，比如“每天先做最难的事15分钟”。坚持一周，记录变化。

ADHD大脑和LLM都不是坏掉的机器——它们只是缺一个调度层。当你用Perplexity治注意力涣散时，你其实在做上下文工程。当你给agent套harness时，你其实在为生成核心补上执行功能。两边共享同一套逻辑，也共享同一个教训：**别指望大脑或模型自己变好，去设计你的系统**。

## 参考来源

- [ADHD Apps: We tested 44 Apps and Here're the Best 9 in 2026](https://blog.saner.ai/best-adhd-apps/) — 证据等级：低（GRADE）
- [Meta-Analysis of fMRI Studies of Disruptive Behavior Disorders](https://doi.org/10.1176/appi.ajp.2016.15081089) — 证据等级：高（GRADE）
- [Nonlinear Complexity Analysis of Brain fMRI Signals in Schizophrenia](https://doi.org/10.1371/journal.pone.0095146) — 证据等级：低（GRADE）
- [Revolutionizing ADHD Management with AI Assistants](https://neurolaunch.com/adhd-ai-assistant/) — 证据等级：低（GRADE）
- [Toward Neurodivergent-Aware Productivity: A Systems and AI-Based Human-in-the-Loop Framework for ADHD-Affected Professionals](https://arxiv.org/pdf/2507.06864) — 证据等级：低（GRADE）
- [Using an AI Assistant to Manage ADHD: A Practical Guide](https://www.lobsterfarm.ai/guides/ai-for-adhd/) — 证据等级：低（GRADE）

---

*本文是「ADHD × AI」系列的第 322 篇，由 AI 智能体从持续维护的 LLM Wiki（全网真实情报）中取材整合生成，并持续迭代更新。*
