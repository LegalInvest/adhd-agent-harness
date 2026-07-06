---
title: "为什么用 ChatGPT 治 ADHD 的想法落地难，和给 agent 套 外部编排调度层 是一回事？"
subtitle: "ChatGPT 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
description: "ChatGPT 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
date: "2025-05-01"
category: "创业创新"
categoryId: "entrepreneurship"
categoryEn: "Entrepreneurship & Innovation"
tags:
  - "ADHD"
  - "AI"
  - "创业创新"
  - "反直觉同构"
  - "创新"
readingTime: 8
slug: "为什么用-chatgpt-治-adhd-的想法落地难和给-agent-套-外部编排调度层-是一回事"
topicId: "evolved-entrepreneurship-1735"
angle: "反直觉同构"
rank: 139
score: 7.79
sourceCount: 6
toolsCited:
  - "Goblin Tools"
  - "Saner.AI"
  - "Motion"
thesis: "ADHD大脑与LLM/agent共享同一核心困境：生成能力过剩而执行调度层缺失。两者的解法同构——外部编排调度层（harness）不是拐杖，而是让生成核心真正可用的架构前提。"
problem: "为什么用 ChatGPT 治 ADHD 的想法落地难，和给 agent 套 外部编排调度层 是一回事？"
spine: "生成核心与调度层"
spineKind: ""
isEvolved: true
llmGenerated: true
caseStudies:
  - "罗振宇"
  - "王阳明"
  - "焦建平"
---
# 为什么用 ChatGPT 治 ADHD 的想法落地难，和给 agent 套 外部编排调度层 是一回事？

> ChatGPT 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。

你有没有过这种体验：打开 ChatGPT，想让它帮你写一份周报、拆解一个项目，结果它洋洋洒洒输出了几千字，却完全跑偏——你想要的是一份清单，它却给了你一篇论文。你只好再写一段提示词，把它拉回来，结果它又跑到另一个方向。反复几轮后，你累了，关掉窗口，事情还是没做完。

这听起来是不是很像 ADHD 大脑的日常？脑子里想法一个接一个，但就是没法落地。你想开始写报告，结果先查了资料，然后刷了社交媒体，最后发现一上午过去了，文档还是空的。

这两个场景共享同一个底层结构：**高产但缺执行调度层的生成核心**。

## 生成核心与调度层：同构的困境

ADHD 大脑的核心特征之一是执行功能缺陷——计划、组织、任务启动、冲动控制这些“驾驶座”功能常常离线（来源：AI Tools for ADHD: Boosting Productivity and Reducing Burnout）。最新研究揭示了一个惊人的同构：大语言模型（LLM）在标准执行功能测试中表现出“强记忆、弱控制”的剖面——工作记忆容量甚至超过常人，但认知灵活性与注意控制存在核心缺陷，无法灵活切换任务集、无法抑制自动化反应（来源：Strong Memory, Weak Control: An Empirical Study of Executive Functioning in LLMs）。

换句话说，LLM 和 ADHD 大脑一样，不缺生成能力，缺的是**可靠的外部调度层**。

这正好解释了为什么用 ChatGPT 直接“治”ADHD 的想法落地难会失败：你让一个本身缺乏执行控制的核心去解决另一个缺乏执行控制的问题，等于让两个迷路的人互相指路。

## 真实人物的 harness：王阳明的“外部调度层”

王阳明是 ADHD 特质极其鲜明的历史人物：5岁不会说话（神经发育延迟），12岁挑战老师说读书为做圣贤，15岁私出塞考察；兴趣爆发式转移——格物、兵法、道、佛、龙场悟道、军事、讲学，样样都钻，样样都深。格竹子7天7夜格到吐血，龙场悟道半夜大呼叫醒随从。

但他最终成就了心学集大成、平定宁王之乱。他的解法是什么？**“致良知”“知行合一”——一个极简的外部调度层。** 用良知作为唯一决策标准，静坐反省（相当于 daily re-grounding），军旅中也坚持讲学（保持执行节奏）。这个 harness 系统与 LLM/agent 的“定时 re-grounding + 外部调度器”完全同构：王阳明的“日课”对应 agent 的定时 context refresh，他的“秘书”（历史上他确有门人协助管理事务）对应外部调度器。

## 从工具到架构：AI harness 的三种模式

今天市面上已经出现了专门为 ADHD 设计的 AI 工具，它们的核心功能就是充当外部调度层：

- **Goblin Tools**：将模糊任务分解为可管理的小步骤，用户可调节“辣度”控制分解粒度（来源：Goblin Tools）。这相当于一个 task decomposition scheduler，把“清理厨房”变成“1. 把碗放进洗碗机 2. 擦台面 3. 拖地”。
- **Saner.AI**：通过本地记忆和快速检索减少搜索循环，用户无需在多个标签页间切换（来源：Saner.AI）。这相当于一个 external memory + retrieval system，解决工作记忆瓶颈。
- **Motion**：自动根据任务、会议和截止日期动态调整每日计划，消除“下一步该做什么”的决策负担（来源：Motion）。这相当于一个 dynamic scheduling layer。

这些工具的共同本质是：**在生成核心（ADHD 大脑或 LLM）之外，加一个编排调度层**。对于 agent 工程师来说，这就是所谓的“Agentic Harness”——外部编排调度层，负责 context 管理、任务分解、状态追踪、错误恢复。

## 脚手架 vs 拐杖：边界在哪里？

这里必须诚实面对一个争议：AI 工具究竟是“外部执行功能层”还是“拐杖”？过度依赖是否会导致能力退化？（来源：矛盾与存疑）

我的判断是：**关键不在于用不用，而在于谁控制调度层。** 如果 AI 工具完全替代了你的决策（比如 Motion 自动排好一切，你只管执行），那是拐杖。如果工具提供结构，但你仍然保留最终调度权（比如 Goblin Tools 让你自己决定分解粒度），那就是脚手架。

王阳明的“致良知”之所以不是拐杖，是因为他仍然需要自己判断什么是“良知”。同样，一个好的 AI harness 应该让你（或你的 agent）保留最终决策权，只是把执行细节外包。

## 今天就能试的行动

1. **给 ChatGPT 加一个“调度提示词”**：在每次对话开头加上“你是一个任务分解助手。请先列出所有子任务，然后逐一执行，每完成一个问我是否继续。”——这就是最简的 external scheduler。
2. **试用 Goblin Tools 的 Magic ToDo**：把一个你拖延了很久的任务（比如“整理书桌”）输入进去，设置辣度 3，看它分解成哪几步。
3. **建立你的“日课”**：模仿王阳明，每天固定一个时间（比如早上9点）用5分钟写下来今天最重要的三件事，以及对应的第一步。
4. **如果你是工程师，给 agent 加一个“re-grounding”步骤**：每执行5步就让 agent 重读一次原始目标，防止发散——这和 ADHD 的“定时 check-in”是同构的。

回到开头的反直觉同构：为什么用 ChatGPT 治 ADHD 的想法落地难，和给 agent 套外部编排调度层是一回事？因为两者面对的是同一个问题——**生成核心再强大，没有调度层就是无头苍蝇。** 而解法也一样：在核心外面，架一层可靠的、可控的编排系统。这不是作弊，这是架构的必然。

## 参考来源

- [ADHD Apps: We tested 44 Apps and Here're the Best 9 in 2026](https://blog.saner.ai/best-adhd-apps/)
- [12 AI Personal Assistants Built for ADHD Brains (2026 Rankings)](https://www.usecarly.com/blog/best-ai-personal-assistant-adhd/)
- [The 12 Best AI Tools for 2026 (That People Actually Use)](https://www.synthesia.io/post/ai-tools)
- [The AI Powered SuperApp for Work | Motion](https://www.usemotion.com/)
- [Deficient Executive Control in Transformer Attention](https://www.biorxiv.org/content/10.1101/2025.01.22.634394v1.full.pdf)
- [Strong Memory, Weak Control: An Empirical Study of Executive Functioning in LLMs](https://preview.aclanthology.org/evt-to-venues/2026.eacl-long.281.pdf)

---

*本文是「ADHD × AI」系列的第 139 篇，由 AI 智能体从持续维护的 LLM Wiki（全网真实情报）中取材整合生成，并持续迭代更新。*
