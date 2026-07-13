---
title: "ADHD 学生视角：为什么「治好 ADHD 的工作记忆容量小、边做边忘」和「让 LLM 不跑飞」其实是同一道工程题？"
subtitle: "LLM 无跨会话状态，靠外部记忆/向量库续命——同一套 harness 思路，两边都成立。"
description: "LLM 无跨会话状态，靠外部记忆/向量库续命——同一套 harness 思路，两边都成立。"
date: "2025-04-23"
category: "AI工具实战"
categoryId: "ai-tools"
categoryEn: "AI Tools in Practice"
tags:
  - "ADHD"
  - "AI"
  - "AI工具实战"
  - "人群×同构"
  - "自动化"
readingTime: 12
slug: "adhd-学生视角为什么治好-adhd-的工作记忆容量小边做边忘和让-llm-不跑飞其实是同一道工程题"
topicId: "prob-f472b0a5d0"
angle: "人群×同构"
rank: 99
score: 7.77
sourceCount: 6
toolsCited:
  - "Goblin Tools"
  - "Lex"
  - "Saner.AI"
  - "Motion"
  - "Reclaim.ai"
thesis: "ADHD 大脑与 LLM 都是「高产生成核心 + 不可靠执行调度层」，二者的问题不是去「修好内部」，而是外接同一套 harness：用外部记忆、任务分解与上下文约束把跑飞的生成核心重新锚定。"
problem: "ADHD 学生视角：为什么「治好 ADHD 的工作记忆容量小、边做边忘」和「让 LLM 不跑飞」其实是同一道工程题？"
spine: "无状态与外部记忆"
spineKind: "llm"
isEvolved: false
llmGenerated: true
isoStrength: "B"
caseStudies:
  - "孔子"
  - "辛弃疾"
  - "余林"
---
# ADHD 学生视角：为什么「治好 ADHD 的工作记忆容量小、边做边忘」和「让 LLM 不跑飞」其实是同一道工程题？

> LLM 无跨会话状态，靠外部记忆/向量库续命——同一套 harness 思路，两边都成立。

你写论文写到一半，脑子里突然闪过一个更棒的选题，于是切过去查文献；半小时后回头，已经忘了刚才要补哪一段。这不是懒，是你的工作记忆在「边做边忘」。你的 LLM agent 也一样：上一轮对话里它刚答应你要按 A→B→C 执行，新会话一开始，它又开始自由发挥，甚至把目标都忘了。LLM 没有跨会话状态，只能靠外部记忆/向量库续命（来源：ADHD 的 AI 工具全景）。

两个看似无关的崩溃——ADHD 的「边做边忘」和 LLM 的「会话漂移」——其实是同一道工程题。

## 一、两个「跑飞」的系统：为什么同构

ADHD 大脑并不缺想法。它的问题在于，前额叶执行功能受损导致计划、抑制、维持目标的能力不稳定，工作记忆容量小，注意力容易被新鲜刺激拉走（来源：ADHD 的 AI 工具全景）。LLM 也不缺生成能力，但它没有内置调度层，上下文窗口有限，更不具备真正的跨会话持久状态，因而在多轮任务中容易偏离目标或产生幻觉（来源：ADHD 的 AI 工具全景）。

这种同构至少体现在三点：第一，都缺少可靠的执行调度层；第二，内部状态（工作记忆/上下文）都脆弱易失；第三，注意力/输出都容易漂移。因此，给 ADHD 设计执行功能支架和给 LLM 设计 agent harness，是同一类结构工程：用外部脚手架替代缺失的调度层，用结构换可控性（来源：ADHD 的 AI 工具全景）。

## 二、Harness 不是治疗，而是外接执行层

对 ADHD 来说，AI 工具的价值不是「代替大脑」，而是成为**外部执行功能层**（来源：ADHD 的 AI 工具全景）。对 LLM 来说，单独一个模型不足以可靠完成多步骤任务，需要围绕它构建软件架构和工具，也就是 agent scaffolding（来源：工具使用与认知卸载）。两边的核心操作都是**上下文工程**：主动限定「此刻应关注什么」。

具体工具的功能惊人地对应：

- **任务分解与启动**：Goblin Tools 的 Magic ToDo 能把「清理厨房」这种模糊目标拆成可执行的子任务，还能调节粒度；Lex 则允许用单一指令触发多步骤任务序列，降低启动门槛（来源：Goblin Tools；Lex）。
- **外部记忆与信息捕获**：Saner.AI 通过本地记忆和语义搜索，把「搜索循环」和标签切换外化为可检索的结构，让工作记忆从大脑里卸载到系统里（来源：Saner.AI）。
- **动态规划与时间调度**：Motion、Reclaim.ai 等自适应工具能根据日程动态调整优先级，对应 LLM agent 里的规划循环与重调度（来源：规划循环与任务分解）。

这些工具共同回答一个问题：当内部调度层不可靠时，如何让外部结构接管「记住、排序、启动、检查」的闭环。

## 三、孔子的「礼」与 LLM 的 system prompt

这种 harness 思路并非今天才有。孔子很可能就是一个典型的 ADHD 式大脑：精力旺盛、周游列国十四年坐不住、冲动爱骂人、对音乐能超专注到「三月不知肉味」、对种地等俗事毫无耐心，《论语》全是场景化语录，没有系统著作（来源：人物案例）。他的 harness 是「克己复礼」——用外在的「礼」作为行为边界，用「吾日三省吾身」做每日反省，直到七十岁才「从心所欲不逾矩」。

这正是一套古代的执行功能支架：
- **「礼」** 对应 LLM 的 system prompt 与输出约束，划定什么能做、什么不能碰；
- **「日三省吾身」** 对应 agent 的定时 re-grounding，让系统周期性地回顾目标、纠正漂移；
- **终身的自我斗争** 则说明，harness 不是一次性治愈，而是持续维护。

辛弃疾则是另一个例子：他把坐不住、冲动、无处安放的能量，外化为「词与剑」两个固定出口，用家国理想作为精神支柱，把报国之愤注入词作（来源：人物案例）。对 LLM 来说，这相当于给它限定领域工具和输出格式，让高产生成核心有明确通道，而不是在开放空间里乱跑。

## 四、脚手架 vs. 拐杖：边界与诚实的局限

必须承认，这种同构是一种**理论类比**，目前缺乏实证基础，不能把它当作既定科学事实（来源：矛盾与存疑）。同时，很多工具宣称的效果证据不足：例如 Motion 缺乏独立临床验证，Brain.fm 在 ADHD 人群中的独立证据也有限（来源：矛盾与存疑）。

更重要的是「脚手架」与「拐杖」的边界。工具应该与现有流程无缝集成、不增加认知开销，否则工具本身会变成新的负担（来源：工具使用与认知卸载）。对 ADHD 来说，如果 every app 都需要复杂配置，那就违背了 harness 的本意；对 LLM agent 来说，如果外部记忆检索不准确，反而会把错误上下文喂回模型，加剧漂移。依赖风险两边都存在：一旦脚手架倒塌，系统会比原来更失控。

所以我的判断是：**harness 的有效性不取决于工具多高级，而取决于它是否形成了可维护的闭环——捕获、结构、回顾、迭代。** 它不是治愈，而是把不可控的生成核心接入一个可检查的外部系统。

## 五、今天就能试的四步

1. **给自己写一个 system prompt**：每天开始工作或学习前，用三句话写下当前目标、约束和下一步动作。ADHD 大脑需要外部 re-grounding，就像 LLM 需要每轮先读一遍系统提示。
2. **用单一工具完成「捕获→分解」**：试着把一件让你卡住的事丢进 Goblin Tools 或 Lex，把模糊压力变成第一条可执行的子任务。重点是先动起来，而不是规划完美（来源：Goblin Tools；Lex）。
3. **给 LLM agent 加最简外部记忆**：一个向量库 + 每轮会话开始时把「目标、已做、待做」摘要塞回上下文，就能显著减少跑飞。这是 ADHD 工作记忆外化的工程版本。
4. **每周做一次 harness 复盘**：不是复盘「我又失败了」，而是复盘「这套外部结构在哪失效了」。脚手架需要持续校准，孔子七十岁才做到不逾矩，我们有理由对自己宽容一点。

 ADHD 学生和 LLM 工程师面对的，其实是同一个问题：一个生成能力极强、但内部调度不可靠的核心，该如何被外部结构稳住。答案不是修好它，而是为它设计一套可维护的 harness。

## 参考来源

**同构强度：B 级** —— 机制类比（ADHD 侧与 LLM/agent 侧均有真实文献，机制可映射）

- [ADHD Apps: We tested 44 Apps and Here're the Best 9 in 2026](https://blog.saner.ai/best-adhd-apps/) — 证据等级：低（GRADE）
- [12 AI Personal Assistants Built for ADHD Brains (2026 Rankings)](https://www.usecarly.com/blog/best-ai-personal-assistant-adhd/) — 证据等级：低（GRADE）
- [Agent Scaffolding: Architecture and Design Patterns for Agentic AI](https://zbrain.ai/agent-scaffolding/) — 证据等级：低（GRADE）
- [LBD同构对：任务分解与规划 — Attention-deficit/hyperactivity disorder is characterized by ↔ Language-conditioned world model improves policy generalizat](https://doi.org/10.1073/pnas.0707741104) — 证据等级：低（GRADE）
- [LBD同构对：任务分解与规划 — Safety and recommendations for TMS use in healthy subjects a ↔ AgentGen: Enhancing Planning Abilities for Large Language Mo](https://doi.org/10.1016/j.clinph.2020.10.003) — 证据等级：低（GRADE）
- [LBD同构对：任务分解与规划 — How specific are executive functioning deficits in attention ↔ AMAP Agentic Planning Technical Report](https://doi.org/10.1111/j.1469-7610.2004.00276.x) — 证据等级：低（GRADE）

---

*本文是「ADHD × AI」系列的第 20 篇，由 AI 智能体从持续维护的 LLM Wiki（全网真实情报）中取材整合生成，并持续迭代更新。*
