---
title: "为什么用 ChatGPT 治 ADHD 的注意力涣散，和给 agent 套 上下文工程 是一回事？"
subtitle: "ChatGPT 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
description: "ChatGPT 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
date: "2025-03-15"
category: "专注力管理"
categoryId: "focus"
categoryEn: "Focus Management"
tags:
  - "ADHD"
  - "AI"
  - "专注力管理"
  - "反直觉同构"
  - "心流"
readingTime: 9
slug: "为什么用-chatgpt-治-adhd-的注意力涣散和给-agent-套-上下文工程-是一回事"
topicId: "evolved-focus-2080"
angle: "反直觉同构"
rank: 17
score: 7.95
sourceCount: 6
toolsCited:
  - "ChatGPT"
  - "Focusmate"
  - "RescueTime"
  - "Brain.fm"
  - "Forest"
  - "Goblin Tools"
  - "Motion"
  - "Reclaim.ai"
thesis: "ADHD大脑与LLM/agent共享“高产但缺执行调度层的生成核心”这一结构缺陷，因此两者都需要外部上下文工程（harness）来补偿调度缺陷——用ChatGPT治注意力涣散，和给agent套上下文工程，本质上是同一套脚手架逻辑。"
problem: "为什么用 ChatGPT 治 ADHD 的注意力涣散，和给 agent 套 上下文工程 是一回事？"
spine: "上下文工程"
spineKind: ""
isEvolved: true
llmGenerated: false
caseStudies:
  - "曾国藩"
  - "苏轼"
  - "罗桂兰"
---

# 为什么用 ChatGPT 治 ADHD 的注意力涣散，和给 agent 套上下文工程是一回事？

> 上下文工程的第一课：模型的表现不取决于它有多聪明，取决于此刻窗口里装了什么。用 ChatGPT 对付注意力涣散的正确姿势，就是让它帮你管理「此刻装了什么」。

先厘清「注意力涣散」在做什么坏事。它的杀伤不是「没在想事情」——ADHD 的大脑随时都在高速想事情——而是**当前任务在意识工作区里的占比被稀释了**：你要写的文档、突然想起的水电费、刚才那条消息的措辞、周末的安排,全部挤在同一个工作区里争夺权重,谁都拿不到足够的算力。

这个描述精确对应 LLM 的上下文窗口问题：窗口里塞满无关内容时,注意力权重被稀释,与当前任务相关的 token 拿不到足够的注意力,输出质量崩塌。工程师的解法叫上下文工程,核心动作只有两个：**控制什么进窗口,和把关键信息放在权重最高的位置。**

## ChatGPT 作为你的上下文管理器

把这两个动作翻译成 ChatGPT 的用法,得到三个高杠杆场景：

**场景一：脑内清仓（控制什么占用工作区）**。涣散最重的时刻,往往是脑内积压最多的时刻。打开 ChatGPT 倾倒：「我现在脑子里同时转着这些事：……帮我分类:哪些今天必须处理、哪些可以进待办、哪些只是焦虑不需要行动。」这个动作的价值不在它的分类多准（够用即可）,在于**倾倒本身把开放回路从工作区搬到了外部**——心理学上未完成事项会持续占用认知资源（蔡加尼克效应）,写下来并获得一个处理方案,占用即释放。

**场景二：单任务上下文装配（把关键信息放进窗口）**。开始一个任务前,让 ChatGPT 帮你搭「任务上下文包」：「我接下来 45 分钟要写 X,帮我列出:目标一句话、需要的材料清单、第一步动作、以及我最可能被带偏的三个方向。」把产出贴在文档顶端。这等于给你的工作区做了一次 system prompt 注入——45 分钟内每次走神回来,读一眼顶端,即刻重锚定。

**场景三：涣散时的软着陆**。已经涣散掉了、在浏览器开了十四个标签页的时刻,别硬拽自己回去（硬拽的失败率极高,还附赠自责）。跟 ChatGPT 说：「我跑偏了,原任务是 X,我现在在看 Y。给我一句话总结 Y 值不值得存进待办,然后给我一个回到 X 的 30 秒动作。」它会把 Y 收纳掉,再递给你一个低门槛的返回台阶。**涣散的代价大头不是走神那几分钟,是回不来的那几十分钟——这个用法专门砍后者。**

## 反面清单：ChatGPT 变成涣散源的三种姿势

工具是双刃的,这三种用法会让它反过来加重涣散：把清仓对话聊成一小时的自我分析（清仓的产出是清单,不是领悟）；任务中途「顺便问它个别的」（窗口污染,正是上下文工程的头号禁忌）；用「问 ChatGPT 怎么专注」代替开始任务（元层面的努力是最高级的拖延）。统一的护栏：**给每次使用设定一个明确的输出物,拿到即关。**

## 边界

同构强度 B 级：上下文窗口与注意力稀释是真实架构特性,ADHD 的干扰易感与工作记忆占用有文献；「ChatGPT 清仓改善专注」属于机制合理的实践方法,无对照研究。涣散若伴随整体情绪低落、睡眠崩坏,先查身体和情绪层,那不是上下文问题。

## 今天就能试的 3 件事

1. **现在做一次脑内清仓**：把此刻脑子里所有开放回路倒给 ChatGPT,拿到三类清单。感受工作区变轻的瞬间。
2. **给下一个任务装配上下文包**：目标/材料/第一步/易偏方向,贴文档顶端。
3. **存一条软着陆指令**：把场景三的话术存成快捷短语,下次跑偏时直接粘贴。

注意力涣散不是工作区坏了,是工作区没有管理员。ChatGPT 当不了你的大脑,但它完全当得起那个管理员——按上下文工程的规矩用它。

## 参考来源

- [ADHD Apps: We tested 44 Apps and Here're the Best 9 in 2026](https://blog.saner.ai/best-adhd-apps/) — 证据等级：低（GRADE）
- [Meta-Analysis of fMRI Studies of Disruptive Behavior Disorders](https://doi.org/10.1176/appi.ajp.2016.15081089) — 证据等级：高（GRADE）
- [Nonlinear Complexity Analysis of Brain fMRI Signals in Schizophrenia](https://doi.org/10.1371/journal.pone.0095146) — 证据等级：低（GRADE）
- [Revolutionizing ADHD Management with AI Assistants](https://neurolaunch.com/adhd-ai-assistant/) — 证据等级：低（GRADE）
- [Agent Scaffolding: Architecture and Design Patterns for Agentic AI](https://zbrain.ai/agent-scaffolding/) — 证据等级：低（GRADE）
- [LBD同构对：任务分解与规划 — Attention-deficit/hyperactivity disorder is characterized by ↔ Language-conditioned world model improves policy generalizat](https://doi.org/10.1073/pnas.0707741104) — 证据等级：低（GRADE）

---

*本文是「ADHD × AI」系列的第 43 篇，由 Devin 基于持续维护的双域研究语料（72,739 篇论文 + LLM Wiki）亲自撰写，并持续迭代更新。*
