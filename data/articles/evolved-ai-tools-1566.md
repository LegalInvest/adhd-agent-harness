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
  - "Saner.AI"
  - "Lex"
  - "ChatGPT"
  - "Claude"
  - "Tiimo"
thesis: "ADHD大脑与LLM在结构上同构——都是强大的生成核心但缺乏可靠的执行调度层——因此Motion等自适应规划器对ADHD任务启动困难的解法，与给agent套function calling工具调用的harness工程，本质上是同一套外部执行功能层方案。"
problem: "为什么用 Motion 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用 是一回事？"
spine: "工具使用与认知卸载"
spineKind: ""
isEvolved: true
llmGenerated: true
---
# 为什么用 Motion 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用 是一回事？

> Motion 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。

## 当任务启动变成一场拔河

你打开电脑，明明知道有个报告要写，但光标在空白文档上闪烁了十分钟，你刷了三次社交媒体、倒了一杯水、整理了一次桌面。不是不想做，是启动的瞬间像被钉在椅子上。ADHD大脑的任务启动困难，本质上不是懒惰，而是执行功能——那个负责“开始”的调度层——间歇性失灵。

另一边，工程师们正在调试一个LLM agent。你给了它一个复杂指令：“分析上季度销售数据，生成图表，写一份总结邮件。”结果agent开始胡编数字，或者卡在第一步反复列出数据源。你检查日志，发现模型在后几轮对话中“开始忘记系统提示”（来源：Building an AI Coding Agent for the Terminal: Scaffolding, Harness, Context Engineering, and Lessons Learned），目标漂移了。

这两件事，表面看毫无关系。但如果你把ADHD大脑和LLM都看作一个“高产但缺执行调度层的生成核心”，那么Motion治ADHD和function calling治agent，就是同一套思路：**给生成核心套一个外部执行功能层（harness）**。

## 同构：两个生成核心的相同困境

ADHD大脑的智力和创造力不输任何人，但执行功能（计划、组织、工作记忆、任务启动）像一条时断时续的网线。LLM同样：它能生成惊艳的文本，但一旦任务需要多步推理、工具调用、状态保持，它就会迷失在上下文的迷雾中。

这种结构同构决定了，两边的解法必须来自同一个工具箱：**外部脚手架**。ADHD患者需要工具来提供“任务分解、提醒、重锚定”；LLM agent需要harness来提供“工具接口、规划循环、指令保持”。

## Motion：ADHD侧的harness

Motion是一款自适应规划器，它能“在日程崩溃时自动重新安排”（来源：AI Tools for ADHD: Boosting Productivity and Reducing Burnout）。对于ADHD用户，传统规划器往往“一周后就失效”（来源：AI Tools for ADHD: Boosting Productivity and Reducing Burnout），因为ADHD大脑的时间盲让固定计划形同虚设。Motion的动态调整相当于一个外部调度器：它接管了“什么时候做什么”的决策，把用户从计划瘫痪中解放出来。

这就像给agent套上了function calling。Motion的调度逻辑类似于harness中的“规划循环”——它持续监控状态（任务是否完成？时间是否超支？），并重新分配资源（把未完成的任务挪到下一个可用时段）。ADHD用户不需要自己执行“重新规划”这个执行功能，Motion代劳了。

同样，Goblin Tools的Magic ToDo自动将“整理房间”分解为“捡起地板上的衣服”“擦桌子”等步骤（来源：AI Tools for Kids with ADHD: A Complete Guide to Parents...），降低了启动门槛。Lex允许用户“通过单一指令触发复杂、多步骤的任务序列”（来源：Best AI Tools for ADHD Productivity in 2026 (Honest Review) - Iwo Szapar），这相当于给ADHD大脑提供了一个“高级API”——你只需调用，底层细节由工具处理。

## Function Calling：LLM侧的Motion

在agent工程中，function calling是harness的核心组件。它让LLM不再直接输出混乱的文本，而是调用预定义的函数（如`search_database`、`send_email`），由harness负责执行和结果回传。这本质上是一种**认知卸载**：LLM只需决定“调用哪个函数”，而不用操心函数内部如何实现。

这正是Motion为ADHD做的事。Motion把“规划日程”这个复杂任务变成了一个可调用的函数：用户输入任务，Motion返回一个动态时间表。ADHD大脑无需自行执行规划算法，只需接受调度结果。

更具体地说，agent的“目标漂移”问题——模型在后几轮忘记原始指令——与ADHD的“注意力漂移”同构。Harness通过“事件驱动的系统提醒”来对抗指令消退（来源：Building an AI Coding Agent for the Terminal: Scaffolding, Harness, Context Engineering, and Lessons Learned），而ADHD工具通过“提醒和通知提供重锚定”（来源：AI for ADHD: Best Tools, Apps, and Strategies - Themba Tutors）。两者都是外部重锚定系统。

## 脚手架，不是拐杖

但这里有一个必须指出的边界：外部执行功能层应该是“脚手架”还是“拐杖”？

脚手架是临时支撑，最终可以撤除；拐杖是永久替代。当前多数ADHD工具（如Goblin Tools、Saner.AI）设计为长期使用，未提及撤除机制（来源：矛盾与存疑）。同样，agent的harness一旦去掉，LLM立刻退化。这是否意味着外部层阻碍了内在能力发展？

我的判断是：对于ADHD，外部执行功能层更像**眼镜**——它不是拐杖，而是生理缺陷的直接补偿。ADHD的执行功能缺陷是神经层面的，不是技能缺失。要求ADHD大脑“学会”自己调度，就像要求近视眼“学会”看清楚。同样，LLM的上下文窗口和注意力机制有物理上限，harness不是临时拐杖，而是架构的必然延伸。

但争议依然存在：部分研究认为过度依赖AI工具可能阻碍内在执行功能发展（来源：矛盾与存疑）。目前缺乏针对这些工具的独立随机对照试验（来源：Goblin Tools局限），效果证据主要来自用户反馈和概念对齐。我们需要更多长期研究来验证“脚手架可撤除性”是否成立。

## 今天就能试的行动

1. **用Goblin Tools的Magic ToDo分解一个你拖延了三天的小任务**（比如“整理桌面”）。观察AI分解后的步骤是否降低了启动焦虑。（来源：Goblin Tools）
2. **尝试用Lex创建一个“一键启动”的复杂任务序列**，比如“写周报”：让它自动收集邮件、生成草稿、发送预览。体验单一指令触发多步骤的认知卸载。（来源：Lex）
3. **如果你是工程师，检查你的agent harness是否有“指令保持”机制**——比如每N轮重新注入系统提示，或事件驱动的重锚定。这相当于给LLM装上Motion的“动态重新规划”。（来源：重锚定与目标漂移）
4. **同时观察自己：** 使用工具一周后，你的内在规划能力是增强了还是退化了？记录下“撤除工具”的难度。这本身就是对“脚手架vs拐杖”争议的个人实验。

## 同构的力量

ADHD大脑和LLM，一个血肉，一个硅基，却共享同一个核心困境：生成能力强，调度层弱。Motion和function calling，看似风马牛不相及，实则是同一套harness工程在不同基质上的实现。理解这个同构，ADHD用户能更清醒地选择工具——不是找“万能药”，而是找“外部调度器”；工程师能更深刻地设计agent——不是造“更聪明的模型”，而是造“更可靠的脚手架”。

这个视角也提醒我们：不要神化AI工具，也不要妖魔化依赖。工具的价值不在于替代你，而在于让你——无论是人类还是模型——把能量集中在最擅长的事上：生成。

## 参考来源

- [Best AI Tools for ADHD Productivity in 2026 (Honest Review) - Iwo Szapar](https://www.iwoszapar.com/p/best-ai-tools-adhd-productivity-2026)
- [AI Tools for ADHD: Boosting Productivity and Reducing Burnout](https://www.vktr.com/ai-platforms/ai-tools-for-adhd-boosting-productivity-and-reducing-burnout/)
- [The Best AI-Powered ADHD Productivity Tools in 2026 (That ...](https://nexasphere.io/blog/ai-adhd-productivity-tools-2026)
- [“A Cognitive Collaborator:” How Adults with ADHD Are Using ChatGPT](https://www.additudemag.com/how-to-use-chatgpt-executive-function-adhd/?srsltid=AfmBOoq-REuSO0UJC656kbLBAd5u3CDNmGeVNrZ79iouVqrFlN919a39)
- [Harnessing Artificial Intelligence to Live Better with ADHD - CHADD](https://chadd.org/attention-article/harnessing-artificial-intelligence-to-live-better-with-adhd/)
- [AI Tools for Kids with ADHD: A Complete Guide for Parents...](https://www.kidsaitools.com/en/articles/ai-tools-kids-adhd-complete-guide-2026)

---

*本文是「ADHD × AI」系列的第 182 篇，由 AI 智能体从持续维护的 LLM Wiki（全网真实情报）中取材整合生成，并持续迭代更新。*
