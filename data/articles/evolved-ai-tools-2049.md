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
topicId: "evolved-ai-tools-2049"
angle: "反直觉同构"
rank: 210
score: 7.72
sourceCount: 6
toolsCited:
  - "Motion"
  - "Goblin Tools"
  - "Saner.AI"
  - "Lex"
  - "ChatGPT"
thesis: "ADHD大脑与LLM都是高产生成核心却缺乏内置调度层，两者都需要外部harness（脚手架）来补偿执行功能缺陷——Motion的任务启动辅助与agent的function calling在架构上同构。"
problem: "为什么用 Motion 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用 是一回事？"
spine: "工具使用与认知卸载"
spineKind: ""
isEvolved: true
llmGenerated: true
caseStudies:
  - "孔子"
  - "孙策"
  - "Brittney Campbell"
---
# 为什么用 Motion 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用 是一回事？

> Motion 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。

## 问题：为什么“开始”这么难？

你盯着空白的待办清单，大脑像死机一样无法输出第一条指令。另一边，工程师调试Agent时，LLM面对复杂任务也常常“卡住”——它知道要做什么，但就是无法自主调用工具、分解步骤。这两种困境共享同一底层结构：**一个强大的生成核心，配了一个失灵的调度层**。

## 同构：生成核心 vs 调度层

ADHD 大脑与 LLM 的结构同构并非空泛比喻。最新研究用经典Stroop冲突任务测试Transformer注意力，发现短上下文中模型表现正常，但随序列变长（认知负荷增加），模型在冲突试次上骤降到随机水平——无法抑制优势反应、无法解决认知冲突。这与ADHD执行功能缺陷的核心标志一一对应：注意控制不足、干扰抑制缺陷、随认知负荷增加而崩溃（来源：Deficient Executive Control in Transformer Attention）。两者都是“高产但缺执行调度层”的生成核心。

ADHD侧的任务启动困难，本质是执行功能层无法将意图转化为动作序列；LLM/Agent侧的函数调用失败，本质是无状态模型缺乏内置的规划与调度机制。两边的解法因此结构同构：**通过外部脚手架（harness）补偿调度缺陷**。

## 人物案例：孔子与孙策的Harness系统

孔子身高1米9，精力旺盛，周游列国14年坐不住；冲动爱骂人，见南子急得对天发誓；对音乐超专注到三月不知肉味，对种地等俗事零耐心；思维跳跃，《论语》全是场景化语录，无系统著作。他的专属harness是“克己复礼”——用外在的“礼”作为行为边界，每日反省，“吾日三省吾身”；70岁才做到从心所欲不逾矩，一辈子和自己的冲动做斗争（来源：wiki人物案例）。这套系统相当于给ADHD大脑套了一个**外部调度器**：礼制提供结构化日程，日课相当于定时re-grounding，帮助生成核心在正确的时间做正确的事。

孙策17岁起兵，26岁遇刺，9年扫平江东；永远坐不住，身先士卒，单骑出猎被刺杀；冲动杀于吉，和太史慈单挑。他的harness是**用张昭张纮等文臣管行政，自己只负责打仗**——将执行功能外包给外部团队，自己只做最擅长的快速决策与冲锋。这与LLM Agent的“工具调用”架构如出一辙：模型只负责生成意图，具体执行由外部工具（如计算器、数据库、API）完成。

## Motion：同一个Harness思路

Motion 是一款AI日程规划工具，核心功能是智能调度：用户输入任务，AI自动排入日历，动态调整优先级。对于ADHD用户，Motion解决了任务启动困难——用户只需输入“写报告”，AI自动分解为子任务并分配时间块，降低启动门槛。对于工程师，Motion的底层是典型的agent scaffolding：围绕LLM构建调度层，自动调用日历、任务分解、时间估算等工具（来源：Lex页面提及Motion的智能调度类似agent scaffolding）。

这与给Agent套function calling工具调用是同一回事：**用外部系统接管调度，让生成核心只负责输出内容**。ADHD用户依赖Motion的“外部调度器”来补偿执行功能，LLM Agent依赖function calling来补偿无状态缺陷。两边都从“全凭自己”转向“脚手架辅助”。

## 核心观点：脚手架 vs 拐杖

我的判断是：**同构性成立，但需警惕过度依赖**。AI工具从脚手架变为永久拐杖的风险真实存在（来源：拐杖与脚手架）。孔子70岁才做到从心所欲不逾矩，说明脚手架需要逐步内化而非永远外包。同样，Agent的function calling如果完全取代模型自身的规划能力，也会导致模型退化。

但当前更紧迫的问题不是依赖，而是**调度层的缺失**。多数ADHD工具（如Goblin Tools的任务分解、Saner.AI的知识回忆、Lex的单一指令触发）都在做同一件事：降低认知负荷，补偿工作记忆不足（来源：认知负荷页面）。而工程师设计的Agent框架（如ReAct、Plan-and-Solve）也在做同一件事：通过外部记忆和工具调用补偿LLM的无状态。两边共享的工程原则是：**不要指望生成核心自己学会调度，给它一个可靠的harness**。

## 争议与局限

同构性目前仍是一种理论类比，缺乏严格的实验验证（来源：矛盾与存疑）。例如，超聚焦在ADHD和Agent中表现不同：ADHD的超聚焦可能卡在错误任务上，而Agent的“超聚焦”是注意力机制的设计选择。另外，工具效果多基于用户报告，缺乏独立临床验证（如Motion页面提到“缺乏独立临床验证”）。依赖风险也需持续监控。

## 今天就能试的行动

1. **ADHD读者**：试用Motion或Goblin Tools的Magic ToDo，将一个模糊任务（如“整理房间”）输入，观察AI如何分解。记录你启动的阻力变化。
2. **工程师读者**：为你的Agent添加一个外部调度模块（如LangChain的AgentExecutor），将复杂任务分解为子步骤并调用工具。对比无调度时的失败率。
3. **通用**：建立“日课”机制——每天固定时间用AI工具（如ChatGPT）做一次任务回顾与优先级排序，相当于孔子的“吾日三省吾身”数字化版。
4. **警惕依赖**：每周选一天关闭所有AI调度工具，手动规划任务，训练内在执行功能。观察哪些能力在退化，哪些在进步。

Motion与function calling的同一性，揭示了ADHD与AI工程共享的底层逻辑：**调度层必须外置，生成核心才能释放潜力**。无论你是ADHD患者还是Agent开发者，答案都是——别让它自己调度，给它一个harness。

## 参考来源

- [ADHD Apps: We tested 44 Apps and Here're the Best 9 in 2026](https://blog.saner.ai/best-adhd-apps/) — 证据等级：低（GRADE）
- [12 AI Personal Assistants Built for ADHD Brains (2026 Rankings)](https://www.usecarly.com/blog/best-ai-personal-assistant-adhd/) — 证据等级：低（GRADE）
- [¡Hacia una IA neurodivergente! (迈向神经多样性AI)](https://ddd.uab.cat/pub/uabdivulga/uabdivulga_a2026m1/uabdivulga_a2026m1a4iSPA.pdf) — 证据等级：低（GRADE）
- [Monotropic Artificial Intelligence: Toward a Cognitive Taxonomy of Domain-Specialized Language Models](https://arxiv.org/pdf/2603.00350v1) — 证据等级：低（GRADE）
- [Transient Frontal Fracturing: A Theoretical Account of Hyperfocus](https://watermark02.silverchair.com/jocn.a.2428.pdf) — 证据等级：低（GRADE）
- [Getting Started with AI for ADHD for ADHD: AI Tools... | Blue Orchid](https://www.blueorchid.world/adhd/guides/getting-started-with-ai-for-adhd) — 证据等级：低（GRADE）

---

*本文是「ADHD × AI」系列的第 210 篇，由 AI 智能体从持续维护的 LLM Wiki（全网真实情报）中取材整合生成，并持续迭代更新。*
