---
title: "为什么用 Lex 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用 是一回事？"
subtitle: "Lex 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
description: "Lex 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
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
readingTime: 10
slug: "为什么用-lex-治-adhd-的任务启动困难和给-agent-套-function-calling-工具调用-是一回事"
topicId: "evolved-ai-tools-1572"
angle: "反直觉同构"
rank: 376
score: 7.65
sourceCount: 6
toolsCited:
  - "Lex"
  - "Goblin Tools"
  - "Saner.AI"
  - "Focusmate"
  - "ChatGPT"
thesis: "ADHD大脑与LLM是同一类高产生成核心但缺调度层的系统，两者的解法——外部执行功能层或function calling工具调用——在结构上同构，Lex正是这一同构的工程实现。"
problem: "为什么用 Lex 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用 是一回事？"
spine: "工具使用与认知卸载"
spineKind: ""
isEvolved: true
llmGenerated: true
caseStudies:
  - "孔子"
  - "徐渭徐文长"
  - "Patrick Tapia"
---
# 为什么用 Lex 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用 是一回事？

> Lex 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。

你坐在电脑前，盯着“写周报”三个字，手指悬在键盘上，却怎么也按不下去。大脑里有一千个想法在冲撞，但没有一个能变成第一个动作。这不是懒，这是ADHD的任务启动困难——一个高产生成核心，却缺少一个能把想法变成行动的调度层。

另一边，你正在调试一个LLM agent。它明明能写出漂亮的回答，但当你让它“帮我订机票并整理行程”时，它要么忘记查询航班，要么把日期搞错。你不得不给它套上function calling工具调用，把“订机票”拆成“搜索航班→选择→支付→生成行程”的步骤链。

这两件事，本质上是同一个问题。

## 同构：高产生成核心 vs 缺失的调度层

ADHD大脑常被描述为一个高产的生成核心——想法丰富、联想活跃，但缺少稳定、可靠的调度层来筛选、组织、启动和坚持任务（来源：ADHD 的 AI 工具全景）。LLM同样具备强大的生成能力，却在长程上下文、目标保持与执行调度上存在天然缺陷。因此，“AI帮ADHD”的实质与“给LLM套harness”是同一类工程：用外部脚手架把生成能力约束到目标轨道上。

这种脚手架在ADHD侧被称为“外部执行功能层”，在LLM侧则对应agent scaffolding——围绕大语言模型构建软件架构和工具，使其能够执行复杂、目标驱动的任务（来源：Lex工具页）。Lex正是这一思路的产物：它允许用户通过单一指令触发复杂、多步骤的任务序列，底层架构类似于agent scaffolding（来源：Lex工具页）。

## 历史中的harness：孔子与徐渭的脚手架

孔子身高1米9，精力旺盛，周游列国14年坐不住；冲动爱骂人，见南子急得对天发誓，骂宰予“朽木不可雕”；对音乐超专注到三月不知肉味，对种地等俗事零耐心；思维跳跃，《论语》全是场景化语录，无系统著作。他的专属harness是“克己复礼”——用外在的“礼”作为行为边界，每日反省，“吾日三省吾身”。70岁才做到“从心所欲不逾矩”，一辈子和自己的冲动做斗争。

徐渭徐文长，诗书画戏军全能，胡宗宪平倭寇主要谋士；执行功能极差，8次举人不中；情绪失调，杀妻、9次自杀；兴趣爆发式转移，什么都学什么都会。他的harness是以书画为核心，把所有痛苦和精力注入艺术创作；用军事谋略帮助胡宗宪抗倭，把超专注用在打仗上。

这两套harness，本质上和Lex或function calling一样：用外部结构来约束和引导一个高产生成核心。孔子的“日课”对应agent的定时re-grounding，徐渭的“秘书/幕僚”对应外部调度器。没有这些脚手架，天才也会被自己的冲动和分心淹没。

## Lex如何实现同构

Lex的核心功能是“单一指令触发多步骤任务序列”（来源：Lex工具页）。对ADHD用户来说，这意味着“写周报”这个指令背后，Lex会自动拆解为“打开上周邮件→提取关键事件→按模板生成草稿→设置提醒”等步骤，降低启动时的认知负荷。对agent工程师来说，这相当于在LLM外面套了一层function calling harness，把“写周报”这个模糊意图转化为可执行的工具调用链。

这并非孤例。Goblin Tools的Magic ToDo功能也能将复杂任务分解为可管理的小步骤，用户可调节“辣度”控制分解粒度（来源：Goblin Tools工具页）。Saner.AI则通过知识回忆和本地记忆补偿ADHD的工作记忆不稳定（来源：Saner.AI工具页）。这些工具的共同点都是：把ADHD大脑的高产生成核心接入一个可维护的执行调度系统。

## 但脚手架不是拐杖

这里必须诚实指出争议：AI工具是“外部执行功能层”还是“拐杖”？过度依赖可能导致能力退化（来源：矛盾与存疑）。孔子用了大半辈子才做到“从心所欲”，徐渭一生都在挣扎——脚手架并不保证永远不需要它。同样，给agent套function calling，如果prompt写得足够好，也许有一天agent能自我调度，但今天还不行。

另一个局限是：ADHD大脑与LLM同构的论点多为类比推理，缺乏神经科学或计算机科学的直接证据（来源：矛盾与存疑）。它目前是一个有用的理论框架，但不应被当作定论。

## 今天就能试的行动

1. **用Lex的“单一指令”启动一个你拖了一周的任务**：比如“整理桌面”，让Lex帮你拆成“清空垃圾桶→归类文件→擦拭桌面→拍照记录”。
2. **如果你是工程师，试着把你常用的agent prompt改成一个function calling schema**：把“帮我写邮件”拆成“收件人→主题→正文→语气检查→发送”的步骤。
3. **模仿孔子的“日省”**：每天结束时，用ChatGPT或Saner.AI回顾今天完成了什么，没完成什么，问自己“我的调度层今天工作了吗？”
4. **找一个身体加倍伙伴**：用Focusmate或找朋友一起工作，利用身体在场效应降低启动门槛（来源：身体在场效应页）。

ADHD大脑和LLM都像一辆引擎强大但方向盘失灵的赛车。Lex和function calling就是那个外挂的方向盘——不是要修好引擎，而是让我们能开得更远。

## 参考来源

- [ADHD Apps: We tested 44 Apps and Here're the Best 9 in 2026](https://blog.saner.ai/best-adhd-apps/)
- [12 AI Personal Assistants Built for ADHD Brains (2026 Rankings)](https://www.usecarly.com/blog/best-ai-personal-assistant-adhd/)
- [The 12 Best AI Tools for 2026 (That People Actually Use)](https://www.synthesia.io/post/ai-tools)
- [Agent Scaffolding: Architecture and Design Patterns for Agentic AI](https://zbrain.ai/agent-scaffolding/)
- [Best productivity apps for Mac you need to try](https://macpaw.com/reviews/best-productivity-apps-for-mac)
- [Building AI Coding Agents for the Terminal: Scaffolding, Harness ...](https://arxiv.org/html/2603.05344v1)

---

*本文是「ADHD × AI」系列的第 376 篇，由 AI 智能体从持续维护的 LLM Wiki（全网真实情报）中取材整合生成，并持续迭代更新。*
