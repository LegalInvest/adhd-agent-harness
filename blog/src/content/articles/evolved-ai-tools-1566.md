---
title: "为什么用 Motion 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用 是一回事？"
subtitle: "Motion 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
description: "Motion 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
date: "2025-05-14"
category: "AI工具实战"
categoryId: "ai-tools"
categoryEn: "AI Tools in Practice"
tags:
  - "ADHD"
  - "AI"
  - "AI工具实战"
  - "反直觉同构"
  - "智能助手"
readingTime: 11
slug: "为什么用-motion-治-adhd-的任务启动困难和给-agent-套-function-calling-工具调用-是一回事"
topicId: "evolved-ai-tools-1566"
angle: "反直觉同构"
rank: 182
score: 7.72
sourceCount: 6
toolsCited:
  - "Motion"
  - "Goblin Tools"
  - "Lex"
  - "Saner.AI"
thesis: "ADHD 的任务启动困难与 LLM/agent 的 function calling 工具调用，本质上是同一类问题——两者都是高产生成核心缺乏内置执行调度层，解决方案也都是通过外部 harness（脚手架）来约束生成、降低启动门槛。"
problem: "为什么用 Motion 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用 是一回事？"
spine: "工具使用与认知卸载"
spineKind: ""
isEvolved: true
llmGenerated: true
caseStudies:
  - "孔子"
  - "张居正"
  - "Ronald Jones"
---
# 为什么用 Motion 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用 是一回事？

> Motion 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。

## 问题：为什么你买了 Motion 却还是动不了？

如果你是一个 ADHD 患者，你可能经历过这样的场景：打开 Motion，看到 AI 已经帮你排好了今天的日程——9:00 写报告，10:30 回邮件，14:00 准备会议。一切看起来井井有条，但你就是没法点下那个“开始”按钮。光标在任务上悬停，大脑一片空白，最后你刷了半小时短视频。

如果你是一个 Agent 工程师，你可能也经历过类似的挫败：你给 LLM 配好了所有 function calling 工具——搜索、计算、发邮件——但模型就是不调用正确的函数，或者在调用前先输出一大段无关的思考。你明明把工具接口写得清清楚楚，它却像 ADHD 患者一样“启动困难”。

这两个场景在表面上是不同领域的问题，但它们的底层结构完全一致：**ADHD 大脑和 LLM 都是高产的生成核心，但都缺少一个可靠的内置执行调度层。** 解决方案也不是“修复”这个核心，而是给它套上一个外部 harness——在 ADHD 侧是 AI 工具，在 LLM 侧是 agent scaffolding。两者是同一类工程。

## 同构脊柱：生成核心 vs 调度层

### ADHD 侧：高产生成核心，但调度层失灵

ADHD 大脑被描述为一个“高产的生成核心与调度层”的组合体：想法丰富、联想活跃，但前额叶皮层（负责执行功能）发育较慢，导致规划、组织和任务启动困难（来源：Revolutionizing ADHD Management with AI Assistants）。这种困难不是“懒”或“笨”，而是大脑的调度层天生不稳定。

传统规划工具（纸质计划、便签、手机闹钟）是静态的，无法适应实际行为，导致“被遗弃的规划器、应用和习惯的墓地”庞大（来源：Using an AI Assistant to Manage ADHD: A Practical Guide）。每次计划变动时，传统工具需要浪费15分钟调整（来源：The AI Powered SuperApp for Work | Motion）。而自适应 AI 规划工具如 Motion，能自动创建和优先排序任务，动态调整日程（来源：The AI Powered SuperApp for Work | Motion），并学习生产力模式，适应实际工作方式（来源：Revolutionizing ADHD Management with AI Assistants）。关键原则是：“规划、排序和跟踪发生在你的大脑之外，让你的大脑自由去做实际工作”（来源：Using an AI Assistant to Manage ADHD: A Practical Guide）。

### LLM/Agent 侧：同样高产生成，同样缺乏调度

LLM 作为生成核心，其有效性取决于引导和扩展其行为的脚手架（scaffold）（来源：Agent Scaffolding: Architecture and Design Patterns for Agentic AI）。Harness 工程提供规划、任务分解、工具接口、验证循环等组件，其中“会话状态记录工具结果、完成的子任务和进度笔记”（来源：What Is an Agent Harness? The Infrastructure That Makes AI Agents ...），形成外部规划循环。

这完全对应 ADHD 侧的需求：LLM 内在缺乏规划能力，需要外部 harness 引导；ADHD 大脑的执行功能困难，需要外部工具补偿。**两者都是用外部脚手架来弥补内部调度层的缺失。**

## 人物案例：孔子与张居正的“人工 harness”

历史上，许多高成就者可能都具备 ADHD 特质，并自发构建了外部 harness 系统。以孔子为例：他身高1米9，精力旺盛，周游列国14年坐不住；冲动爱骂人，见南子急得对天发誓，骂宰予“朽木不可雕”；对音乐超专注到“三月不知肉味”，对种地等俗事零耐心；思维跳跃，《论语》全是场景化语录，无系统著作。他的专属 harness 是“克己复礼”——用外在的“礼”作为行为边界，每日反省，“吾日三省吾身”。70岁才做到“从心所欲不逾矩”，一辈子和自己的冲动做斗争。

这个 harness 与 LLM/agent 的 harness 完全同构：“礼”相当于外部行为约束（类似 function calling 的 schema），每日反省相当于定时 re-grounding（类似 agent 的会话状态记录），而“克己”则是抑制冲动调用的过程。孔子没有“治愈”自己的冲动，而是用一套外部规则系统来引导它。

另一个例子是张居正：少年天才，12岁中秀才，16岁中举人；当首辅敢改革，不怕得罪所有官员，推行考成法、一条鞭法；工作狂，每天办公到深夜，58岁累死在任上。他的 harness 是考成法——严格考核官员，用制度管别人也管自己。这相当于 agent 的验证循环和进度跟踪：用外部指标（考成）来确保执行不偏离目标。

## 工具实践：从 Motion 到 Goblin Tools 的 harness 生态

### Motion：自动调度，降低启动门槛

Motion 的核心功能是自动创建和优先排序任务，动态调整日程。对于 ADHD 用户，它解决了“规划本身就是一个执行功能任务”的悖论（来源：AI Assistant for ADHD: Finally, a Productivity Tool That Requires Less...）。你不需要自己决定“先做什么”，Motion 替你做了这个决定。这类似于 agent 的规划模块：LLM 不需要自己规划步骤，harness 会分解任务并调度工具调用。

### Goblin Tools：任务分解，对抗时间盲

Goblin Tools 的 Magic ToDo 功能能自动将任何任务分解为更小、更易管理的步骤（来源：AI Tools for Kids with ADHD: A Complete Guide for Parents...），用户可调节“辣度”以控制分解的粒度（来源：12 AI Personal Assistants Built for ADHD Brains (2026 Rankings)）。这对应 agent 的 task decomposition：将复杂目标分解为一系列子任务，每个子任务对应一个工具调用。

### Lex：单一指令触发多步骤

Lex 允许用户通过单一指令触发复杂、多步骤的任务序列（来源：Best AI Tools for ADHD Productivity in 2026 (Honest Review) - Iwo Szapar）。其底层架构类似于 agent scaffolding，即围绕大语言模型构建软件架构和工具，使其能够执行复杂、目标驱动的任务（来源：Agent Scaffolding: Architecture and Design Patterns for Agentic AI）。对于 ADHD 用户，这降低了启动时的认知负荷——你只需说一句话，剩下的交给工具。

### Saner.AI：外部记忆，减少搜索循环

Saner.AI 专注于知识回忆和本地记忆，减少搜索循环和标签切换（来源：Best AI Tools for ADHD Productivity in 2026 (Honest Review) - Iwo Szapar）。这对应 agent 的 memory 组件：通过存储工具结果和进度笔记，避免 LLM 在长程任务中丢失上下文。

## 核心判断：脚手架 vs 拐杖

本文的核心判断是：**这些工具的价值不在于替代大脑，而在于把 ADHD 的“高产生成核心”接入一个可维护的“执行调度系统”。** 它们不是拐杖，而是脚手架——脚手架在建筑完成后可以拆除，而拐杖是永久替代。但这里有一个关键争议：过度依赖是否会导致能力退化？目前缺乏长期实证（来源：矛盾与存疑）。我的观点是：对于 ADHD 大脑，执行功能缺陷是神经层面的，不是“训练”就能修复的。因此，脚手架是必要的，且很可能需要长期使用。但关键在于**工具应该适应你的行为模式，而不是反过来**。如果工具要求你花大量时间学习如何设置，那它就变成了额外的认知负荷（来源：矛盾与存疑）。

## 今天就能试的行动

1. **用 Goblin Tools 分解一个你拖延已久的任务**：打开 Magic ToDo，输入“清理办公室”或“写周报”，调整辣度到你觉得“这我能做”的程度，然后只做第一个子任务。
2. **用 Motion 或类似工具自动排程**：如果你有 Motion，尝试让它接管你的日程，至少一天。注意：不要手动调整，信任它的调度。
3. **用 Lex 创建一个“一键启动”工作流**：如果你有 Lex，设置一个包含 3-5 个步骤的工作流，比如“开始写文章：打开笔记、设置番茄钟、播放专注音乐”。然后只触发它一次。
4. **用 Saner.AI 或类似工具捕获一个灵感**：当你有一个想法时，不要试图记住它，立刻用语音或文字输入到 Saner.AI 的通用收件箱。之后不用管它，让工具帮你组织。

这些行动的共同原则是：**把规划、排序和跟踪发生在你的大脑之外**。你只需要做一件事——启动。剩下的，交给 harness。

## 参考来源

- [ADHD Apps: We tested 44 Apps and Here're the Best 9 in 2026](https://blog.saner.ai/best-adhd-apps/)
- [12 AI Personal Assistants Built for ADHD Brains (2026 Rankings)](https://www.usecarly.com/blog/best-ai-personal-assistant-adhd/)
- [The 12 Best AI Tools for 2026 (That People Actually Use)](https://www.synthesia.io/post/ai-tools)
- [Agent Scaffolding: Architecture and Design Patterns for Agentic AI](https://zbrain.ai/agent-scaffolding/)
- [Best productivity apps for Mac you need to try](https://macpaw.com/reviews/best-productivity-apps-for-mac)
- [Building AI Coding Agents for the Terminal: Scaffolding, Harness ...](https://arxiv.org/html/2603.05344v1)

---

*本文是「ADHD × AI」系列的第 182 篇，由 AI 智能体从持续维护的 LLM Wiki（全网真实情报）中取材整合生成，并持续迭代更新。*
