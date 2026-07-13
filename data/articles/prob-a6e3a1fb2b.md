---
title: "ADHD 程序员视角：为什么「治好 ADHD 的怕过度依赖工具、又怕没有支撑就崩」和「让 LLM 不跑飞」其实是同一道工程题？"
subtitle: "harness 应是会褪去的脚手架，而非永久拐杖——同一套 harness 思路，两边都成立。"
description: "harness 应是会褪去的脚手架，而非永久拐杖——同一套 harness 思路，两边都成立。"
date: "2025-03-08"
category: "情绪调节"
categoryId: "emotion"
categoryEn: "Emotional Regulation"
tags:
  - "ADHD"
  - "AI"
  - "情绪调节"
  - "人群×同构"
  - "情绪管理"
readingTime: 10
slug: "adhd-程序员视角为什么治好-adhd-的怕过度依赖工具又怕没有支撑就崩和让-llm-不跑飞其实是同一道工程题"
topicId: "prob-a6e3a1fb2b"
angle: "人群×同构"
rank: 249
score: 7.67
sourceCount: 6
toolsCited:
  - "Inflow"
  - "Goblin Tools"
  - "Saner.AI"
  - "Motion"
  - "Brain.fm"
thesis: "ADHD 大脑与 LLM/agent 都是高产但缺乏可靠执行调度层的生成核心，两边的「依赖恐惧」与「跑飞恐惧」本质同一道题：harness 不是永久拐杖，而是可随能力增长逐步褪去的脚手架，核心目标是让外部调度层最终被内化为自身的执行功能。"
problem: "ADHD 程序员视角：为什么「治好 ADHD 的怕过度依赖工具、又怕没有支撑就崩」和「让 LLM 不跑飞」其实是同一道工程题？"
spine: "拐杖与脚手架"
spineKind: "bridge"
isEvolved: false
llmGenerated: false
isoStrength: "A"
caseStudies:
  - "释迦牟尼"
  - "于谦"
  - "雷英"
---

# ADHD 程序员视角：为什么「治好 ADHD 的怕过度依赖工具、又怕没有支撑就崩」和「让 LLM 不跑飞」其实是同一道工程题？

> 这道工程题对程序员有一层其他职业没有的讽刺:**你白天的工作,就是给一个「聪明但不可靠」的系统搭 harness**——重试、超时、护栏、监控、回滚,你给 LLM agent 配这些的时候毫无道德挣扎,不会说「这模型要学会自律」;**但下班后面对自己的启动困难和注意涣散,你换了一套语言:「我就是废」「我该更自觉」**。同一个人,对机器用工程学,对自己用道德学。这一篇的任务只有一个:把你已经会的那套工程学,原样用回自己身上。

先建立映射表,每一项你都熟:**目标漂移**——agent 跑长任务会偏离初始目标,解法是定期重注入 system prompt;你写代码两小时后从重构漂到「顺便升级依赖」再漂到读 HN,解法同款:任务卡贴在屏幕边,每小时读一次。**上下文污染**——无关内容进窗会稀释注意力,解法是窗口隔离;你的八个标签页和三个聊天窗口同理,解法:当前任务一个窗口组,其余最小化。**无限循环**——agent 会在失败的路径上反复重试,harness 用循环计数器强制跳出;你在一个 bug 上死磕四小时不肯求助,同款:**卡壳 45 分钟即触发协议(换路径/求助/记录后跳过)**——你给 agent 设的 max_retries,凭什么自己没有?**冷启动成本**——服务冷启动贵,所以工程上尽量保温;你的任务启动贵,所以尽量不完全冷却:**下班前给明天的自己留一个「热入口」**——写到一半的函数留个失败的测试,明早从「让测试变绿」进入,启动成本砍掉大半(这是老程序员的土办法,Hemingway 也用:停在写得出的地方)。

映射表建完,回到那个核心拧巴——「靠这些撑着,算真本事吗?」用你自己的行话回答:**你评估一个生产系统,看的是 SLO,不是「裸奖跑分」**。没有监控和重试的服务再优雅,可用性三个九都到不了,你不会上线它;同理,「我+我的 harness」能稳定交付,这就是全部需要证明的事。**Agent 领域已经默认「模型+脚手架」才是评估单位,你对自己却还在坚持裸模型主义**——这是你知识库里已有答案、只是没做跨域调用的问题。

程序员版还有两个独有的坑,顺手标掉:**坑一:把搭 harness 本身变成拖延**。工具链、dotfiles、任务管理系统的无限调优——这是 240 篇「准备行为」的程序员豪华版:**配置不产生 reward,commit 才产生**;给自己的系统也要设「配置预算」(每周调优不超过一小时,超了就是在装修拖延开火)。**坑二:hyperfocus 的双刃性**。程序员是少数能把 ADHD 的超聚焦直接变现的职业(一夜写完一个模块的传说),但超聚焦不受控:它选题不由你(经常锁死在有趣但不重要的支线),且透支后崩两天。工程处理:**不压制,加护栏**——进入超聚焦前放一个闹钟(三小时强制水面呼吸:喝水、看一眼任务卡确认没漂移),把它从「不可控的爆发」驯化成「有监控的高性能模式」。

## 边界

同构强度 A 级:LLM 的目标漂移、上下文稀释、执行控制随长度崩坏均有直接实证研究(含与 ADHD 执行缺陷显式对标的工作),harness 各组件是工程标准实践;「hyperfocus」的机制研究尚不充分,相关建议属实践总结。声明:长期靠 deadline 恐慌和熬夜爆发交付、且伴随情绪耗竭的模式,值得临床评估而不只是流程优化;工程类比不覆盖药物决策——那是你和医生的 code review,不是自己 merge。

## 今天就能试的 3 件事

1. **给自己写 max_retries**:卡壳 45 分钟触发协议——换路/求助/记录跳过,今天生效。
2. **下班前留热入口**:留一个失败的测试或写一半的注释,明早从那里点火。
3. **设配置预算**:本周调工具链的时间封顶一小时——超出的冲动,记进「准备行为」账。

你给每个不可靠的系统都配了监控、重试和回滚,唯独对自己要求裸奔零故障——**把白天的工程学带回家:你不是有缺陷的程序员,你是一个还没给自己上生产级 harness 的系统**。SLO 达标即可,裸跑分不用交。

## 参考来源

**同构强度：A 级** —— 直接文献支撑（引用 ADHD↔LLM 同构专题研究）

- [The 12 Best Apps for ADHD in 2026: A Guide to Finding What ...](https://www.getinflow.io/post/best-apps-for-adhd) — 证据等级：低（GRADE）
- [Dynamic causal brain circuits during working memory and their functional controllability](https://doi.org/10.1038/s41467-021-23509-x) — 证据等级：低（GRADE）
- [ADHD Apps: We tested 44 Apps and Here're the Best 9 in 2026](https://blog.saner.ai/best-adhd-apps/) — 证据等级：低（GRADE）
- [12 AI Personal Assistants Built for ADHD Brains (2026 Rankings)](https://www.usecarly.com/blog/best-ai-personal-assistant-adhd/) — 证据等级：低（GRADE）
- [Deficient Executive Control in Transformer Attention](https://www.biorxiv.org/content/10.1101/2025.01.22.634394v1.full.pdf) — 证据等级：低（GRADE）
- [Executive Dysfunction by Design: A Cognitive Accessibility Analysis of AI Support vs. Healthcare Barriers](https://dl.acm.org/doi/pdf/10.1145/3663547.3749831) — 证据等级：低（GRADE）

---

*本文是「ADHD × AI」系列的第 102 篇，由 Devin 基于持续维护的双域研究语料（72,739 篇论文 + LLM Wiki）亲自撰写，并持续迭代更新。*
