---
title: "ADHD 自由职业者视角：为什么「治好 ADHD 的状态日内大幅波动、不稳定」和「让 LLM 不跑飞」其实是同一道工程题？"
subtitle: "LLM 采样温度带来输出随机性，靠结构约束稳定——同一套 harness 思路，两边都成立。"
description: "LLM 采样温度带来输出随机性，靠结构约束稳定——同一套 harness 思路，两边都成立。"
date: "2025-04-05"
category: "生活方式"
categoryId: "lifestyle"
categoryEn: "Lifestyle"
tags:
  - "ADHD"
  - "AI"
  - "生活方式"
  - "人群×同构"
  - "人际关系"
readingTime: 12
slug: "adhd-自由职业者视角为什么治好-adhd-的状态日内大幅波动不稳定和让-llm-不跑飞其实是同一道工程题"
topicId: "prob-fa0964fd2b"
angle: "人群×同构"
rank: 337
score: 7.63
sourceCount: 6
toolsCited:
  - "Routinery"
  - "Goblin Tools"
  - "Habitica"
  - "Focusmate"
  - "Saner.AI"
  - "Motion"
thesis: "ADHD 大脑与 LLM 都是「高产但缺执行调度层的生成核心」：状态波动和采样温度一样无法被「意志力/降参」根除，只能用外部 harness（脚手架、护栏、人在回路）把高方差输出约束为可靠行动。"
problem: "ADHD 自由职业者视角：为什么「治好 ADHD 的状态日内大幅波动、不稳定」和「让 LLM 不跑飞」其实是同一道工程题？"
spine: "采样温度与表现波动"
spineKind: "llm"
isEvolved: false
llmGenerated: true
isoStrength: "C"
caseStudies:
  - "孔子"
  - "毛泽东"
  - "郝小红"
---
# ADHD 自由职业者视角：为什么「治好 ADHD 的状态日内大幅波动、不稳定」和「让 LLM 不跑飞」其实是同一道工程题？

> LLM 采样温度带来输出随机性，靠结构约束稳定——同一套 harness 思路，两边都成立。

## 问题：两个看似不相干的崩溃现场

作为 ADHD 自由职业者，你大概熟悉这种日内曲线：早上思路泉涌、连写三篇草稿；午后却像被按下暂停键，连回一封邮件都要做心理建设。项目不等人，但你的状态像股票一样大幅波动。你恨自己「不稳定」，也试过靠意志力和咖啡把曲线拉平，结果往往更糟。

另一边，做 Agentic Harness 的工程师也熟悉另一种波动：LLM 温度（temperature）一高，输出就创意爆棚但不可控；温度一低，又变得死板、重复。单靠调参无法解决「不跑飞」的问题，必须靠 prompt 工程、工具调用限制、人在回路（human-in-the-loop）和护栏把随机性框住。

这两个场景，其实是同一道工程题：一个高产生成核心，缺少可靠的执行调度层，需要外部 harness 来把方差转化为可用输出。

## 同一套结构：高产生成核心 + 缺失的执行调度层

ADHD 大脑的痛点不是「笨」或「懒」，而是执行功能薄弱——计划、组织、工作记忆、冲动抑制和时间感知都靠外部补偿（来源：AI 与 ADHD 的日常生活）。工作记忆不稳定让信息在脑子里转不停，时间盲让「下午三点」变成一个模糊概念，任务启动困难则让大象一样的项目压得人动弹不得。

LLM 的痛点则来自结构：它是一个强大的生成核心，却没有内置的调度层。它不能自己决定「现在该查什么、该停、该回退」，直接输出可能偏离目标、陷入循环或产生危险行为（来源：人在回路与身体在场）。

所以两边都不适合「直接输出」。ADHD 大脑需要外部执行功能层；LLM agent 需要 scaffolding。这不仅是类比，而是一种结构同构：两者都靠外部支架来限定「此刻应关注什么」（来源：上下文工程）。

## 温度、波动与脚手架

LLM 的采样温度决定输出随机性：温度高，分布更宽，容易出惊喜也容易跑飞；温度低，分布更集中，更安全但更无趣。工程师不会让模型「自己管住自己」，而是加 prompt 约束、token 预算、工具调用次数上限、强制暂停的人工检查点（来源：Building an AI Agent Harness from Scratch: The Architecture Between LLM and Agent - DEV Community）。

ADHD 的日内波动也类似：它不是靠「决心」就能调平的参数，而是神经系统的固有方差。真正有效的策略不是消灭波动，而是给波动加结构：
- **Routinery** 用可视化倒计时和过渡提示，把「时间盲」和「任务启动难」变成可执行的步骤序列（来源：11 Best ADHD Productivity Apps for Fluctuating Energy - rivva blog；AI for ADHD: Best Tools, Apps, and Strategies - Themba Tutors）。
- **Goblin Tools** 的 Magic ToDo 能把模糊任务自动拆解成具体步骤，降低启动门槛（来源：Harnessing Artificial Intelligence to Live Better with ADHD - CHADD）。
- **Habitica** 用积分、等级、奖励提供即时多巴胺反馈，帮助坚持（来源：ADHD科技行业深度研究）。

这些工具的本质，和 LLM 的脚手架一样：不是替换生成核心，而是给生成核心加上「调度层」。

## 古人与国父的 harness：礼、批评与调查

这种 harness 思路不是新发明。孔子的 ADHD 式特质非常明显：精力旺盛、周游列国十四年、冲动爱骂人、对音乐极度专注而对其余俗事零耐心、思维跳跃，《论语》里全是场景化语录。他给自己搭的 harness 是「克己复礼」——用外在的「礼」作为行为边界，每日「三省吾身」，直到七十岁才说「从心所欲不逾矩」。这相当于给自己的大脑写了一份系统 prompt，并用每日 re-grounding 来维持。

毛泽东也有相似的特质：小时候是问题儿童、爱读闲书、一辈子读书不止、永远在动、思维跳跃、讲话充满比喻。他的 harness 是「批评与自我批评」、民主生活会、调查研究和民主集中制。用集体决策和外部反馈制衡个人冲动，用「没有调查就没有发言权」来防止目标漂移。这正对应 LLM 里的 human-in-the-loop 与外部评估器：不是让系统自己决定，而是引入外部约束来纠偏。

两个例子都说明：高方差的生成核心本身并不可怕，可怕的是没有 harness。礼、反省、调查、批评，这些都是两千年前和近代版的 scaffolding。

## 把同构落地：今天的工具箱

把这套工程思路搬到日常，可以从三个维度组合：

1. **重锚定（Re-grounding）**：ADHD 容易目标漂移，被无关刺激捕获或钻进细节（来源：重锚定与目标漂移）。AI 别针和挂绳可以转录对话、提醒会议、帮助回忆细节；但传统提醒的问题是「设置提醒本身就需要执行功能」（来源：AI Assistant for ADHD: Finally, a Productivity Tool That Requires Less...）。所以更好的方案是尽量少启动的自动化提示，比如 Routinery 的流程引导或 Focusmate 的虚拟 coworking。

2. **身体在场（Body Doubling）**：对许多 ADHD 人来说，有他人在场时任务更容易启动。Focusmate 通过虚拟视频 coworking 实现这种社会问责（来源：人在回路与身体在场）。这和 LLM 的 human-in-the-loop 一样，外部存在本身就是一个执行调度器。

3. **任务分解与多巴胺反馈**：用 Goblin Tools 把模糊任务切碎，用 Habitica 把小事变成即时奖励，弥补 ADHD 的内在动机缺陷。同时可以配合 **Saner.AI** 或 **Motion** 等动态调度工具来补全时间管理的缺口，但要注意这些工具在 ADHD 人群中的独立临床证据仍有限（来源：全局矛盾与存疑）。

## 脚手架 vs 拐杖：边界在哪里

关键争议在于：这些工具是脚手架，还是拐杖？如果外部工具只是永久替代内部功能，而不帮助用户逐步内化执行策略，就可能削弱自我调节能力（来源：拐杖与脚手架；全局矛盾与存疑）。

好的 harness 应该像训练轮：初期支撑，后期逐渐撤掉。孔子的「礼」最终变成了他内在的自律；毛泽东的民主集中制也不是为了让他放弃判断，而是让判断更稳。AI 工具最理想的用法，是把「设置提醒、拆解任务、维持专注」这些原本薄弱的执行功能，通过反复练习慢慢内化为自己的能力，而不是永远依赖通知。

## 核心判断：不是「治好波动」，而是「给波动上 harness」

回到最初的问题：为什么「治好 ADHD 的状态波动」和「让 LLM 不跑飞」是同一道题？

因为两者都不该追求「零波动」。ADHD 的高方差里包含了创造力、模式识别和风险偏好；LLM 的高温度里包含了涌现性和跨领域联想。真正要工程化的不是消除这些特性，而是建造一个可靠的外部调度层——让它该发散时发散，该收敛时收敛，该停时停。

所以，更诚实的说法不是「治愈 ADHD」，而是「设计一套适合自己的 harness」。同构性目前仍是结构与功能层面的对应，尚未被证明是生物学或计算机制上的等同（来源：全局矛盾与存疑）。但作为一个工作假设，它非常有效：它让我们把「自我管理」从道德问题转化为工程问题。

## 今天就能试的四件事

1. **写一份自己的系统 prompt**：每天早上用两分钟写下「今天最重要的三件事」和「一次重锚定时间」。不是列待办，而是给大脑设定上下文。

2. **把一个模糊任务丢进 Goblin Tools**：例如「整理发票」或「写项目提案」，让它拆解成第一步，然后立刻为第一步开一个 Focusmate 或身体在场会议。

3. **如果你在做 LLM agent，先加硬约束再加能力**：在提高模型温度或权限之前，先设置 token 上限、工具调用次数、强制暂停检查点和明确回退路径。

4. **每周做一次「批评与自我批评」**：回顾哪些外部支架真正帮助了你，哪些已经变成拐杖。目标永远是：让 harness 逐渐被内化，而不是让工具永远替你思考。

## 参考来源

**同构强度：C 级** —— 仅修辞类比（缺双域文献支撑，类比停留在修辞层面）

- [AI for ADHD: Best Tools, Apps, and Strategies - Themba Tutors](https://thembatutors.com/ai-for-adhd-tools-and-apps/) — 证据等级：低（GRADE）
- [11 Best ADHD Productivity Apps for Fluctuating Energy - rivva blog](https://blog.rivva.app/p/11-best-adhd-productivity-apps-for) — 证据等级：低（GRADE）
- [ADHD Apps: We tested 44 Apps and Here're the Best 9 in 2026](https://blog.saner.ai/best-adhd-apps/) — 证据等级：低（GRADE）
- [12 AI Personal Assistants Built for ADHD Brains (2026 Rankings)](https://www.usecarly.com/blog/best-ai-personal-assistant-adhd/) — 证据等级：低（GRADE）
- [DeepSeek - AI Assistant - Apps on Google Play](https://play.google.com/store/apps/details?id=com.deepseek.chat) — 证据等级：低（GRADE）
- [AI Assistant for ADHD: Finally, a Productivity Tool That Requires Less...](https://get-alfred.ai/blog/ai-assistant-for-adhd) — 证据等级：低（GRADE）

---

*本文是「ADHD × AI」系列的第 183 篇，由 AI 智能体从持续维护的 LLM Wiki（全网真实情报）中取材整合生成，并持续迭代更新。*
