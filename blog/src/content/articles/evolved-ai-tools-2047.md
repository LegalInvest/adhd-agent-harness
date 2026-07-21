---
title: "为什么用 Goblin Tools 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用 是一回事？"
subtitle: "Goblin Tools 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
description: "Goblin Tools 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
date: "2025-05-19"
category: "AI工具实战"
categoryId: "ai-tools"
categoryEn: "AI Tools in Practice"
tags:
  - "ADHD"
  - "AI"
  - "AI工具实战"
  - "反直觉同构"
  - "智能助手"
readingTime: 14
slug: "为什么用-goblin-tools-治-adhd-的任务启动困难和给-agent-套-function-calling-工具调用-是一回事"
topicId: "evolved-ai-tools-2047"
angle: "反直觉同构"
rank: 281
score: 7.45
sourceCount: 6
toolsCited:
  - "Goblin Tools"
  - "Lex"
  - "Saner.AI"
  - "Focusmate"
  - "ChatGPT"
thesis: "ADHD大脑与LLM都是高产但缺执行调度层的生成核心，Goblin Tools的任务分解和function calling工具调用本质相同——通过外部harness补偿内部执行功能缺陷。"
problem: "为什么用 Goblin Tools 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用 是一回事？"
spine: "工具使用与认知卸载"
spineKind: ""
isEvolved: true
llmGenerated: false
caseStudies:
  - "孔子"
  - "文天祥"
  - "王雪"
---

# 为什么用 Goblin Tools 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用是一回事？

> LLM 不擅长算术,工程师没有硬练它,而是接了个计算器——识别短板,注册工具,调用了事。ADHD 不擅长「把任务变成第一步」,Goblin Tools 干的就是计算器的活:把「拆解」这个特定认知操作,做成一个可以一键调用的外部函数。想通这层,你对这个小工具的用法会完全不同。

先把「任务启动困难」拆到机件级。启动一个任务,大脑要在幕后完成一串操作:把模糊目标翻译成具体动作→选出第一步→评估成本→压制竞争刺激→点火。ADHD 卡的高频位置是第一环:**「收拾房间」在脑中始终是一团没有把手的雾**,翻译器过载,后面全部堵死。外人看到的是「拖延」,内部实况是「编译失败」。关键的诊断:这不是全局性的能力缺失——同一个人给朋友拆解任务头头是道,给自己的任务就是拆不动(自己的任务捆着焦虑和自我评价,把本就吃紧的翻译器压垮了)。**局部的、可预测的、特定操作的失灵——这正是 function calling 要解决的问题形状。**

LLM 的算术就是这个形状:整体能力强,单项操作系统性不可靠。工程答案的精髓在于「不纠正,只旁路」:**模型的职责从「做算术」收缩为「识别出这是算术→调用计算器」**。Magic ToDo 之于任务启动,是完全同构的旁路:你的职责从「拆解任务」收缩为「识别出我卡在拆解→打开工具输入任务」——后者对 ADHD 是可执行的,前者常常不是。

## 把它用成真正的 function calling,三条纪律

**一、写清触发条件(function signature)。** 好的工具调用有明确的触发判据。给自己立一条:**「对着任务发呆超过 5 分钟=调用」**——不是「实在不行了再用」(那时自责已经烧掉半天),也不是「所有任务都用」(过度调用见下)。识别触发条件这件事本身,几周后会变成你的元认知肌肉:「哦,我现在卡的是拆解,不是执行。」

**二、调用完立即消费返回值。** 计算器返回结果,模型立即用它继续生成——没有哪个系统调用完工具就把结果晾着。Magic ToDo 返回子任务列表后,**立即执行第一条**(拆到 5 分钟内粒度),这是整个调用的兑现时刻。拆完不做,等于调用了计算器然后不看结果。

**三、只在短板处调用。** function calling 的边界纪律:工具接管系统性短板,不接管核心职责。你的短板是「把雾变成把手」;**「哪些任务值得做」「做成什么样算好」仍是本体的职责**——让工具替你拆解「怎么收拾房间」可以,让「今天该收拾房间还是该写简历」这类价值排序也交给工具的推荐顺序,就越界了。

## 用错的姿势速查

**过度调用**:刷牙都要拆——调用有成本(打开、输入、读输出),熟练任务直接跑本体;判据:手已经知道怎么动的,不调用。**调用后不执行**:拆解列表越攒越多,变成新的焦虑源——记住 3 任务上限,拆一个做一个。**用调用逃避识别**:从不问「我到底卡在哪」,一律扔工具——有些卡点不是拆解(是情绪、是睡眠、是这任务本来就不该做),错误的调用签名会让真正的问题一直漏诊。

## 边界

同构强度 B 级:function calling 是真实工程机制,ADHD 的任务翻译/启动困难有执行功能文献支撑,Goblin Tools 无独立对照研究,「触发条件」等纪律是本文的操作化建议。声明:启动困难若在完美拆解后依然普遍存在,或伴随持续情绪低落,请专业评估——工具旁路得了拆解,旁路不了抑郁;药物对启动的改善有证据,工具是配合项。

## 今天就能试的 3 件事

1. **写下你的调用签名**:「发呆超过 5 分钟→打开 Magic ToDo」,贴在桌上。
2. **今天完成一次完整调用**:卡住→输入→拆到 5 分钟粒度→立即做第一条。
3. **记录一次「不该调用」**:哪个任务其实不卡拆解?识别它,直接动手——分辨力和工具同样重要。

给模型接计算器的那批工程师,从没想过要「治好」模型的算术——他们只是承认短板、注册工具、设好触发。对自己的启动困难,同样的姿势就够了:不搏斗,不羞耻,一键调用,立即执行。雾变成把手,把手就在那,握住它。

## 参考来源

- [ADHD Apps: We tested 44 Apps and Here're the Best 9 in 2026](https://blog.saner.ai/best-adhd-apps/) — 证据等级：低（GRADE）
- [12 AI Personal Assistants Built for ADHD Brains (2026 Rankings)](https://www.usecarly.com/blog/best-ai-personal-assistant-adhd/) — 证据等级：低（GRADE）
- [Using an AI Assistant to Manage ADHD: A Practical Guide](https://www.lobsterfarm.ai/guides/ai-for-adhd/) — 证据等级：低（GRADE）
- [10 Killer ChatGPT Prompts For Organizing Your ADHD Brain](https://www.adhdflowstate.com/best-chatgpt-prompts-for-adhd/) — 证据等级：低（GRADE）
- [ADHD Task Managers That Work: Top AI Tools 2025](https://www.sentisight.ai/ai-neurodivergent-productivity-adhd-friendly/) — 证据等级：低（GRADE）
- [¡Hacia una IA neurodivergente! (迈向神经多样性AI)](https://ddd.uab.cat/pub/uabdivulga/uabdivulga_a2026m1/uabdivulga_a2026m1a4iSPA.pdf) — 证据等级：低（GRADE）

---

*本文是「ADHD × AI」系列的第 209 篇，由 Devin 基于持续维护的双域研究语料（72,739 篇论文 + LLM Wiki）亲自撰写，并持续迭代更新。*
