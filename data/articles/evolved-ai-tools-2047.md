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
rank: 139
score: 7.75
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
llmGenerated: true
caseStudies:
  - "孔子"
  - "文天祥"
  - "王雪"
---
# 为什么用 Goblin Tools 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用 是一回事？

> Goblin Tools 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。

## 问题：为什么启动一件事这么难？

你盯着“写周报”三个字，大脑一片空白。不是不会写，而是那个“开始”的按钮像是被焊死在远处。ADHD人群对这种“任务启动困难”再熟悉不过——执行功能缺陷让大脑的生成能力与调度能力严重脱节（来源：ADHD 大脑与 LLM 的同构）。

与此同时，工程师们正在为LLM agent头疼：模型能写诗、能编程，但让它“帮我预订明天的航班并整理行程”，它要么胡编乱造，要么卡在第一步。于是大家给它套上function calling——把“预订航班”拆成`search_flights`、`book_ticket`、`add_to_calendar`等可调用的工具函数。

这两件事，本质上是同一类问题。

## 同构：生成核心 vs 调度层

ADHD大脑与LLM在结构上惊人相似：两者都是强大的生成核心，但缺乏可靠的内置执行调度层（来源：生成核心与调度层）。ADHD的工作记忆不稳定、时间感知模糊（时间盲）、容易在无关细节上超聚焦六小时（来源：超聚焦）；LLM则无状态、缺乏持久记忆、上下文窗口有限。两边都需要外部脚手架（harness）来补偿——对ADHD是任务分解、身体加倍、外部记忆；对LLM是function calling、工具调用、记忆系统。

Goblin Tools的Magic ToDo就是ADHD版的function calling。你输入“清理厨房”，它自动分解为“1. 把碗放进洗碗机；2. 擦拭台面；3. 拖地”——这就是把模糊意图转化为可执行的原子步骤，和agent把“预订航班”拆成多个API调用一模一样（来源：Goblin Tools）。用户可调节“辣度”控制粒度，相当于调整function的颗粒度。

同样，Lex通过“单一指令触发多步骤任务”降低启动门槛（来源：Lex），其底层架构类似于agent scaffolding——围绕大语言模型构建软件架构和工具，使其能执行复杂目标驱动任务（来源：Agent Scaffolding）。Saner.AI则用本地记忆减少搜索循环（来源：Saner.AI），对应agent的外部记忆系统。

## 人物案例：孔子的harness系统

孔子是典型的ADHD大脑：身高1米9，精力旺盛，周游列国14年坐不住；冲动爱骂人，见南子急得对天发誓，骂宰予“朽木不可雕”；音乐超专注到“三月不知肉味”，对种地零耐心；思维跳跃，《论语》全是场景化语录，无系统著作。他的专属harness是“克己复礼”——用外在的“礼”作为行为边界，每日反省，“吾日三省吾身”。70岁才做到“从心所欲不逾矩”，一辈子和自己的冲动做斗争。

这个harness与LLM/agent的function calling同构：“礼”就是预定义的工具函数（如“见长辈要鞠躬”“吃饭不能吧唧嘴”），每日反省相当于定时re-grounding（类似agent的定期状态检查），而“从心所欲不逾矩”则是经过长期训练后，外部规则内化为自动流程——就像agent经过微调后，function calling变得流畅自然。孔子的成就（儒家学派创始人）证明，即使生成核心有缺陷，只要harness设计得当，依然可以产出伟大成果。

## 脚手架 vs 拐杖：争议与边界

同构类比虽有力，但需诚实指出局限。目前“ADHD大脑与LLM同构”仍是一种理论类比，缺乏实证基础（来源：矛盾与存疑）。工具宣称的效果多基于用户报告，缺乏严格临床验证（来源：矛盾与存疑）。更重要的是依赖风险：Goblin Tools从脚手架变成永久拐杖，用户可能再也无法手动分解任务（来源：拐杖与脚手架）。同样，agent过度依赖function calling也会丧失自主推理能力。

身体在场效应（Body Doubling）是另一个例子。Focusmate通过AI匹配虚拟伙伴提升专注度（来源：身体在场效应），但AI是否能替代真实人际互动存在争议（来源：矛盾与存疑）。多巴胺检测技术（通过视网膜检测）尚处早期，不应作为成熟功能宣传（来源：矛盾与存疑）。

## 核心观点：harness不是削弱，而是解放

我的判断是：好的harness不会削弱核心能力，而是释放生成潜力。孔子如果没有“礼”的约束，可能只是一个暴躁的流浪教师；LLM如果没有function calling，只是一个会写诗但订不了机票的聊天机器人。关键区别在于：脚手架是临时的、可调节的（如Goblin Tools的辣度控制），而拐杖是永久的、不可移除的。ADHD用户应定期尝试“无工具”执行小任务，保持核心肌群不萎缩；工程师应设计可退化的agent，在工具不可用时仍能推理。

## 今天就能试的4件事

1. **用Goblin Tools分解一个你拖延的任务**：输入“整理书桌”或“写邮件”，调节辣度到你觉得“可以开始”的程度。对比手动分解，感受认知负荷的差异（来源：Goblin Tools）。
2. **为你的LLM agent设计一个最小function calling**：选一个日常任务（如“查天气并提醒我带伞”），拆成2-3个函数，观察执行流畅度提升。
3. **尝试一次虚拟身体加倍**：用Focusmate或和朋友视频连线，各自做各自的事，感受社会在场感对启动的帮助（来源：Focusmate）。
4. **设置一个“无工具日”**：每周选一天，不用任何AI助手手动完成任务，记录自己的执行功能状态，警惕依赖。

同构不是巧合，而是工程与生物在进化压力下的共同答案。当ADHD大脑和LLM都学会借用外部脚手架，它们才真正开始行动。

## 参考来源

- [ADHD Apps: We tested 44 Apps and Here're the Best 9 in 2026](https://blog.saner.ai/best-adhd-apps/) — 证据等级：低（GRADE）
- [12 AI Personal Assistants Built for ADHD Brains (2026 Rankings)](https://www.usecarly.com/blog/best-ai-personal-assistant-adhd/) — 证据等级：低（GRADE）
- [Using an AI Assistant to Manage ADHD: A Practical Guide](https://www.lobsterfarm.ai/guides/ai-for-adhd/) — 证据等级：低（GRADE）
- [10 Killer ChatGPT Prompts For Organizing Your ADHD Brain](https://www.adhdflowstate.com/best-chatgpt-prompts-for-adhd/) — 证据等级：低（GRADE）
- [ADHD Task Managers That Work: Top AI Tools 2025](https://www.sentisight.ai/ai-neurodivergent-productivity-adhd-friendly/) — 证据等级：低（GRADE）
- [¡Hacia una IA neurodivergente! (迈向神经多样性AI)](https://ddd.uab.cat/pub/uabdivulga/uabdivulga_a2026m1/uabdivulga_a2026m1a4iSPA.pdf) — 证据等级：低（GRADE）

---

*本文是「ADHD × AI」系列的第 209 篇，由 AI 智能体从持续维护的 LLM Wiki（全网真实情报）中取材整合生成，并持续迭代更新。*
