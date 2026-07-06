---
title: "为什么用 Goblin Tools 治 ADHD 的注意力涣散，和给 agent 套 上下文工程 是一回事？"
subtitle: "Goblin Tools 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
description: "Goblin Tools 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
date: "2025-04-06"
category: "专注力管理"
categoryId: "focus"
categoryEn: "Focus Management"
tags:
  - "ADHD"
  - "AI"
  - "专注力管理"
  - "反直觉同构"
  - "注意力"
readingTime: 11
slug: "为什么用-goblin-tools-治-adhd-的注意力涣散和给-agent-套-上下文工程-是一回事"
topicId: "evolved-focus-1587"
angle: "反直觉同构"
rank: 286
score: 7.68
sourceCount: 6
toolsCited:
  - "Goblin Tools"
  - "Focusmate"
  - "RescueTime"
  - "Brain.fm"
  - "Forest"
thesis: "ADHD 大脑与 LLM 在结构上同构——都是高产但缺乏可靠执行调度层的生成核心，因此两者都需要上下文工程（harness）来稳定输出，Goblin Tools 等 ADHD 工具本质上是给大脑套上外部执行功能层，与给 agent 做上下文工程是同一套思路。"
problem: "为什么用 Goblin Tools 治 ADHD 的注意力涣散，和给 agent 套 上下文工程 是一回事？"
spine: "上下文工程"
spineKind: ""
isEvolved: true
llmGenerated: true
caseStudies:
  - "曾国藩"
  - "孔子"
  - "李芳"
---
# 为什么用 Goblin Tools 治 ADHD 的注意力涣散，和给 agent 套 上下文工程 是一回事？

> Goblin Tools 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。

你有没有过这样的体验：打开电脑准备写报告，结果半小时后发现自己刷了 20 个网页、打开 3 个文档、脑子里同时跑着 5 个念头，但报告一个字没动。这不是意志力差，是你的大脑里有个“高产但缺调度层”的生成核心——ADHD 大脑。

同样，如果你做过 agent 开发，一定遇到过：给 LLM 的上下文越长，它越容易跑偏，最后输出一堆看似相关实则无用的内容。你需要“上下文工程”——精心设计 prompt、分割上下文、加 re-grounding 机制——才能让 agent 稳定产出。

这两件事，本质上是同一个问题。

## 同构：ADHD 大脑与 LLM 是同一类“生成核心”

ADHD 大脑与 LLM 的深层同构体现在多个层面（来源：AI 与 ADHD 的专注力）：
- **生成核心与调度层**：两者都拥有强大的生成能力（ADHD 的创意发散、LLM 的文本生成），但缺乏可靠的执行调度层（ADHD 的执行功能、LLM 的上下文控制），导致输出不稳定。
- **无状态与外部记忆**：ADHD 的工作记忆缺陷与 LLM 的无状态性同构，都需要外部记忆系统（如第二大脑、向量数据库）来维持连续性。
- **上下文工程**：ADHD 易被环境带偏，LLM 易被上下文膨胀干扰，都需要主动设计“当下注意什么”的工程方案。

最新研究提供了硬证据：用经典 Stroop 冲突任务测试 Transformer 注意力，发现短上下文中表现正常，但随序列变长（认知负荷增加），模型在冲突试次上骤降到随机水平——无法抑制优势反应、无法解决认知冲突。这与 ADHD 执行功能缺陷的核心标志一一对应：注意控制不足、干扰抑制缺陷、随认知负荷增加而崩溃（来源：认知负荷）。

## 历史人物的 harness：曾国藩与孔子的“上下文工程”

曾国藩是典型的注意力不集中型 ADHD：30 岁前浮躁坐不住，天天串门喝酒看杀人，日记里天天骂自己“无恒”“浮躁”；读书慢，“他人目下二三行，余或疾读不能终一行”；一辈子严重银屑病，情绪不稳定，打败仗就跳水自杀。他的专属 harness 是“日课十二条”：黎明即起、读书不二、谨言、写日记反省等；“结硬寨打呆仗”，用最笨最稳的方法抵消自己的冲动（来源：人物案例）。

孔子同样有 ADHD 特质：身高 1 米 9，精力旺盛，周游列国 14 年坐不住；冲动爱骂人，见南子急得对天发誓，骂宰予朽木不可雕；对音乐超专注到三月不知肉味，对种地等俗事零耐心。他的 harness 是“克己复礼”——用外在的“礼”作为行为边界，每日反省，“吾日三省吾身”（来源：人物案例）。

这些 harness 与 LLM/agent 的上下文工程惊人同构：
- **日课 ↔ 定时 re-grounding**：曾国藩每日固定时间做固定事，相当于给大脑设置定时重定向指令，防止上下文漂移。
- **“礼” ↔ 系统 prompt**：孔子用“礼”作为行为边界，相当于给 agent 设定系统级约束，防止输出越界。
- **日记反省 ↔ 日志与评估**：曾国藩写日记自我反省，相当于 agent 的日志记录与自我评估机制，用于检测并纠正偏差。

## Goblin Tools：给大脑套上外部执行功能层

Goblin Tools 是一款专为 ADHD 设计的 AI 工具，其核心功能包括：
- **魔法待办（Magic ToDo）**：将模糊任务自动分解为可执行的小步骤，降低任务启动门槛。
- **调味剂（The Chef）**：根据剩余食材生成菜谱，减少决策认知负荷。
- **法官（The Judge）**：评估邮件语气，帮助避免冲动回复。

这些功能本质上是在做“上下文工程”：将大任务分割成小上下文（微任务），降低单次认知负荷；提供外部决策锚点（如菜谱），减少大脑的调度压力；增加情绪调节层（如语气评估），防止情绪失调导致的输出失控。

同样，为 LLM 做上下文工程时，我们会：
- 将长上下文分割成 chunk，每次只给 agent 一小段信息。
- 加 re-grounding prompt，定期让 agent 回顾核心目标。
- 加输出格式约束，防止 agent 跑偏。

## 工具证据：哪些工具在做什么？

- **Focusmate**：基于虚拟身体在场的在线问责服务，通过实时同伴问责提供外部结构和社会压力，弥补内在多巴胺调节不足。其核心机制是“AI-Matched Body Doubling”（来源：Focusmate）。这相当于给 agent 加了一个外部监督器，定期检查进度。
- **RescueTime**：自动化时间追踪与生产力分析工具，自动记录时间使用，揭示真实的时间去向，帮助用户识别注意力漂移（来源：RescueTime）。这相当于给 agent 加日志系统，记录每一步耗时。
- **Brain.fm**：利用 AI 生成音乐，通过神经锁相技术影响大脑处理信息的方式，帮助进入专注状态（来源：Brain.fm）。这相当于给 agent 加了一个注意力锚点，减少上下文干扰。

## 争议与局限：脚手架还是拐杖？

核心争议在于：AI 工具是“外部执行功能层”还是“拐杖”？长期使用是否会导致 ADHD 患者内在执行功能进一步退化？目前缺乏纵向研究，尚无定论（来源：矛盾与存疑）。

同样，agent 的上下文工程也存在风险：过度依赖外部 prompt 和 re-grounding，可能导致 agent 失去自主调度能力。两者都需要找到“脚手架 vs 拐杖”的平衡——脚手架是暂时的、可拆除的辅助结构，拐杖是永久依赖。

另一个争议是：超聚焦应被引导还是打断？部分 ADHD 用户反馈强行打断（如番茄钟）有效，而柔性引导可能不够强力。这对应 agent 的“中断机制”：是硬性超时打断，还是软性提醒后让 agent 自己决定？缺乏对比研究。

## 今天就能试的行动

1. **用 Goblin Tools 的 Magic ToDo 分解一个让你拖延的任务**：比如“写周报”拆成“打开文档→列出本周工作→写第一段→检查格式→发送”。每次只关注一个小步骤，降低启动阻力。
2. **设置一个外部监督器**：用 Focusmate 预约一个 25 分钟工作时段，或找一个朋友视频一起工作。这相当于给大脑加一个“实时 re-grounding”机制。
3. **记录时间流向**：用 RescueTime 或 Forest 追踪一天的时间使用，识别注意力漂移模式。这相当于给大脑加日志系统，让“时间盲”变可见。
4. **设计你的“日课”**：像曾国藩一样，每天固定时间做固定事（如早起后先做最重要的一件事）。用手机提醒或日历事件作为“定时 re-grounding”。

## 结论

ADHD 大脑与 LLM 是同构的生成核心，都需要上下文工程来稳定输出。Goblin Tools 等 ADHD 工具本质上是在给大脑套上外部执行功能层，与给 agent 做 prompt 工程、分割上下文、加 re-grounding 是同一套思路。理解这一点，你就能从“我意志力不行”的自责中解脱出来——问题不在你，在于你的大脑缺了一个调度层。而解决方案，工程师们早就知道了。

## 参考来源

- [ADHD Apps: We tested 44 Apps and Here're the Best 9 in 2026](https://blog.saner.ai/best-adhd-apps/)
- [Meta-Analysis of fMRI Studies of Disruptive Behavior Disorders](https://doi.org/10.1176/appi.ajp.2016.15081089)
- [Nonlinear Complexity Analysis of Brain fMRI Signals in Schizophrenia](https://doi.org/10.1371/journal.pone.0095146)
- [Revolutionizing ADHD Management with AI Assistants](https://neurolaunch.com/adhd-ai-assistant/)
- [Getting Started with AI for ADHD for ADHD: AI Tools... | Blue Orchid](https://www.blueorchid.world/adhd/guides/getting-started-with-ai-for-adhd)
- [An ADHD ChatGPT Guide: Helpful Prompts & ADHD Hacks - I'm Busy Being Awesome](https://imbusybeingawesome.com/chatgpt-adhd/)

---

*本文是「ADHD × AI」系列的第 286 篇，由 AI 智能体从持续维护的 LLM Wiki（全网真实情报）中取材整合生成，并持续迭代更新。*
