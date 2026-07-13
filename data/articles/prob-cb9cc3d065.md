---
title: "为什么用 Todoist 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用 是一回事？"
subtitle: "Todoist 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
description: "Todoist 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
date: "2025-04-20"
category: "AI工具实战"
categoryId: "ai-tools"
categoryEn: "AI Tools in Practice"
tags:
  - "ADHD"
  - "AI"
  - "AI工具实战"
  - "反直觉同构"
  - "ADHD辅助"
readingTime: 7
slug: "为什么用-todoist-治-adhd-的任务启动困难和给-agent-套-function-calling-工具调用-是一回事"
topicId: "prob-cb9cc3d065"
angle: "反直觉同构"
rank: 186
score: 7.69
sourceCount: 6
toolsCited:
  - "Todoist"
  - "Goblin Tools"
  - "Lex"
  - "Saner.AI"
  - "Motion"
  - "Reclaim.ai"
  - "ChatGPT"
  - "Claude"
thesis: "ADHD 大脑与 LLM 都是“高产生成核 + 缺执行调度层”的系统，Todoist 对人的任务启动帮助，和 function calling 对 agent 的约束，本质是同一种外部 harness：把模糊意图翻译成带参数、带时序、可验证的下一步动作。"
problem: "为什么用 Todoist 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用 是一回事？"
spine: "工具使用与认知卸载"
spineKind: ""
isEvolved: true
llmGenerated: true
isoStrength: "B"
caseStudies:
  - "孔子"
  - "孙策"
  - "Ashley Hicks"
---
# 为什么用 Todoist 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用 是一回事？

> Todoist 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。

## 任务启动困难：一个 ADHD 人，也像一个失控的 Agent

你有没有这种体验：脑子里明明想“把报告写完”，身体却从刷短视频到整理抽屉，三小时过去文档还是空白。对 ADHD 人群来说，这往往不是“懒”，而是任务启动的齿轮卡住了——目标太大、步骤太模糊、优先级太乱，执行功能层在第一步就宕机（来源：Harnessing Artificial Intelligence to Live Better with ADHD - CHADD）。

做 Agentic Harness 的工程师看了可能会会心一笑：这不就是我的 LLM 吗？你给模型一句“帮我策划一次团队outing”，它可能先写 800 字文案，再推荐三家餐厅，最后把订餐厅和发日历的 API 调用忘得一干二净。LLM 生成能力极强，却缺少稳定的跨会话状态、原生规划与注意力约束（来源：Agent Scaffolding: Architecture and Design Patterns for Agentic AI）。

两种场景表面不同，结构却惊人相似：都有一颗高速运转的“生成核心”，却缺一个可靠的“执行调度层”。

## 同构解：把“想做”翻译成“先做第一步”

ADHD 与 LLM 的同构，最具体的落点就在“任务分解与规划”。Swanson 的文献发现，ADHD 文献群（681 篇命中）与 agentic harness 文献群（2914 篇命中）都把“任务分解与规划”作为核心中间机制（来源：LBD同构对：任务分解与规划 — Attention-deficit/hyperactivity disorder is characterized by ↔ Language-conditioned world model improves policy generalizat；LBD同构对：任务分解与规划 — Safety and recommendations for TMS use in healthy subjects a ↔ AgentGen: Enhancing Planning Abilities for Large Language Model based Agent via Environment and Task Generation）。也就是说，两个领域研究的是同一个工程问题：如何把模糊目标拆成可执行的下一步。

ADHD 侧的工具直接回应这一点。Goblin Tools 的 Magic ToDo 会把“清理厨房”拆成具体子任务，还能调节“辣度”控制粒度（来源：12 AI Personal Assistants Built for ADHD Brains (2026 Rankings)）。Lex 更进一步，允许用户用“单一指令触发多步骤任务序列”，把复杂目标压缩成低启动成本的入口（来源：Best AI Tools for ADHD Productivity in 2026 (Honest Review) - Iwo Szapar）。

LLM 侧对应的就是 function calling：模型不再只是生成文本，而是输出结构化的“工具调用”——函数名、参数、顺序。它把“帮我订出差”拆成 `search_flights`、`book_hotel`、`add_calendar_event`。本质上，两边的工具都在做同一件事：把“想做”翻译成“先做第一步”，降低启动门槛。

## 外部调度层：为什么 Todoist 是人的 Function Calling

Todoist 对 ADHD 的意义，不只是“列清单”。它是一套外部执行功能层：把任务名字、截止日期、优先级、项目上下文这些内部工作记忆外化，变成可检索、可排序、可提醒的结构。ADHD 大脑的工作记忆容量不稳定，信息在任务切换中容易丢失；LLM 的上下文窗口有限，同样缺乏真正的跨会话持久状态（来源：ADHD 的 AI 工具全景）。两者都需要外部记忆系统来补位。

Saner.AI 这类工具更激进，直接提供“通用收件箱”和内部助手，从邮件、文档、日历中提取待办，并自动把大项目拆成小里程碑（来源：ADHD Apps: We tested 44 Apps and Here're the Best 9 in 2026）。这与 LLM agent 的架构几乎一一对应：外部记忆（vector store）、任务规划（planner）、工具调用（function calling）、反馈循环（reflection）。Todoist 在这里扮演的角色，就是 human agent 的 function registry：每一项任务都是一次“待执行调用”，有明确的参数和触发条件。

有趣的是，这种需求并不是现代才有。古人的 harness 系统同样结构同构。

## 历史原型：孔子与孙策的 harness

孔子的 ADHD 式特质很明显：精力旺盛、周游列国十四年坐不住、冲动骂人、对音乐超专注而对俗事零耐心，《论语》全是场景化语录而非系统著作。他的 harness 是“克己复礼”——用外在的“礼”作为行为边界，并每日反省，“吾日三省吾身”。这相当于给生成核心装了一个定期 re-grounding 的系统提示：每到一个场景，先查“礼”这个外部函数，再决定输出什么。他直到七十岁才“从心所欲不逾矩”，说明 harness 不是一次设置就永久生效，而是需要持续维护（来源：人物案例 [孔子 harness]）。

孙策的 harness 则是另一番面貌：他冲动、坐不住、身先士卒，但把行政后勤完全交给张昭、张纮等文臣，自己只负责打仗和人格魅力输出。他的系统架构是“外部调度器 + 核心生成模块”——让秘书层处理他不擅长的结构化执行，自己专注在速度上。这几乎就是现代 agent 的“planning/routing 层与工具调用分离”：一个外部 scheduler 决定调用哪些工具，核心模型只负责高价值决策（来源：人物案例 [孙策 harness]）。

## 工具不是魔法：同构的边界与风险

必须诚实地说，ADHD 大脑与 LLM 的“同构”目前更像是一种有用的结构类比，而非经过严格验证的科学事实。不同资料在表述时有时把它当既定事实，有时当假设，存在不一致（来源：全局矛盾与存疑）。同样，很多工具宣称有效，但独立临床验证有限。例如 Motion 的页面也指出“缺乏独立临床验证”，一些 ADHD 专注力工具的真实效果仍待更多研究（来源：全局矛盾与存疑）。

另一个边界是“脚手架 vs 拐杖”。外部 harness 的价值在于补位，而不是替代。如果 Todoist 清单越来越长、AI 工具本身变成新的认知负担，或者 LLM 的 function calling 链路越来越复杂却没人审查，那 harness 就从脚手架变成了拐杖。ADHD 专业人士寻找 AI 工具时的一条关键标准是“与现有工具集成，不增加认知开销”（来源：Best AI Tools for ADHD Productivity in 2026 (Honest Review) - Iwo Szapar），对 agent 工程师同样成立：每增加一个工具调用，都要问它是否真的减少了决策负担。

## 今天就能试的 4 步

1. **把一件卡住的 ADHD 任务交给 Goblin Tools**：输入模糊目标，复制它生成的第一个子任务到 Todoist，并设置具体的时间和提醒。观察“启动齿轮”是否因此咬合（来源：Harnessing Artificial Intelligence to Live Better with ADHD - CHADD）。
2. **在 Todoist 里给任务写“函数参数”**：不要只写“写报告”，而是写成“写报告：字数 1500，截止时间周五 17:00，素材在 Notion”。让外部系统替你保存上下文，减少工作记忆负担。
3. **给 LLM agent 加一个“先规划再调用”的 function**：在每次调用外部 API 之前，让模型先输出一个结构化清单（下一步动作、依赖关系、预期结果），由人类或代码确认后再执行。这就是 agent 的“三省吾身”。
4. **每周做一次 re-grounding**：对人来说，是回顾 Todoist/日历，删除过期任务、重新标优先级；对 agent 来说，是清理记忆库、校准 system prompt。两者都是防止 harness 失灵的维护动作。

## 结语

ADHD 人不是“缺想法”，而是缺把想法稳定落地的执行层；LLM 不是“没能力”，而是缺把生成结果约束到真实世界的调度层。Todoist 和 function calling，正好站在同

## 参考来源

**同构强度：B 级** —— 机制类比（ADHD 侧与 LLM/agent 侧均有真实文献，机制可映射）

- [ADHD Apps: We tested 44 Apps and Here're the Best 9 in 2026](https://blog.saner.ai/best-adhd-apps/) — 证据等级：低（GRADE）
- [12 AI Personal Assistants Built for ADHD Brains (2026 Rankings)](https://www.usecarly.com/blog/best-ai-personal-assistant-adhd/) — 证据等级：低（GRADE）
- [Agent Scaffolding: Architecture and Design Patterns for Agentic AI](https://zbrain.ai/agent-scaffolding/) — 证据等级：低（GRADE）
- [LBD同构对：任务分解与规划 — Attention-deficit/hyperactivity disorder is characterized by ↔ Language-conditioned world model improves policy generalizat](https://doi.org/10.1073/pnas.0707741104) — 证据等级：低（GRADE）
- [LBD同构对：任务分解与规划 — Safety and recommendations for TMS use in healthy subjects a ↔ AgentGen: Enhancing Planning Abilities for Large Language Mo](https://doi.org/10.1016/j.clinph.2020.10.003) — 证据等级：低（GRADE）
- [LBD同构对：任务分解与规划 — How specific are executive functioning deficits in attention ↔ AMAP Agentic Planning Technical Report](https://doi.org/10.1111/j.1469-7610.2004.00276.x) — 证据等级：低（GRADE）

---

*本文是「ADHD × AI」系列的第 66 篇，由 AI 智能体从持续维护的 LLM Wiki（全网真实情报）中取材整合生成，并持续迭代更新。*
