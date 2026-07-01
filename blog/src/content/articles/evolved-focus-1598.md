---
title: "为什么用 Claude 治 ADHD 的注意力涣散，和给 agent 套 上下文工程 是一回事？"
subtitle: "Claude 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
description: "Claude 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
date: "2025-05-15"
category: "专注力管理"
categoryId: "focus"
categoryEn: "Focus Management"
tags:
  - "ADHD"
  - "AI"
  - "专注力管理"
  - "反直觉同构"
  - "深度工作"
readingTime: 10
slug: "为什么用-claude-治-adhd-的注意力涣散和给-agent-套-上下文工程-是一回事"
topicId: "evolved-focus-1598"
angle: "反直觉同构"
rank: 156
score: 7.75
sourceCount: 6
toolsCited:
  - "Focusmate"
  - "RescueTime"
  - "Brain.fm"
thesis: "ADHD大脑与LLM是同一类「高产但缺执行调度层的生成核心」，两者都需通过上下文工程（harness）来稳定输出，而非依赖内在意志力。"
problem: "为什么用 Claude 治 ADHD 的注意力涣散，和给 agent 套 上下文工程 是一回事？"
spine: "上下文工程"
spineKind: ""
isEvolved: true
llmGenerated: true
---
# 为什么用 Claude 治 ADHD 的注意力涣散，和给 agent 套 上下文工程 是一回事？

> Claude 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。

## 问题：为什么你越努力专注，反而越涣散？

如果你是一名ADHD患者，你可能有过这样的体验：明明想工作，却控制不住刷手机；明明有创意，却无法落地成项目。如果你是一名Agent工程师，你可能也有类似的挫败感：LLM能写出漂亮的文案，却会在简单工具调用上“幻觉”；Agent能规划复杂任务，却常因上下文膨胀而偏离轨道。

这两个群体的困境，共享同一个底层结构：**一个高产但缺乏可靠执行调度层的生成核心**。ADHD大脑的创意发散、LLM的文本生成，本质上都是强大的“生成器”，但都缺少一个稳定的“调度器”——对ADHD来说是执行功能缺陷，对LLM来说是上下文控制失效。

## 同构：ADHD与LLM的“注意力涣散”是同一回事

### ADHD侧：执行功能缺陷即“调度层缺失”
ADHD的核心问题并非注意力不足，而是**执行功能缺陷**（来源：AI与ADHD的专注力）。执行功能包括工作记忆、任务启动、时间感知、冲动抑制等，它们共同构成了大脑的“调度层”。当调度层失灵，生成核心（创意、联想、情绪）就会不受控地输出，表现为注意力涣散、拖延、时间盲。这就像一个高采样温度（high temperature）的LLM，输出多样但不可靠。

### LLM侧：上下文膨胀即“调度层失效”
LLM在长对话或复杂任务中，会因上下文窗口膨胀而丢失焦点，产生幻觉或重复工作（来源：幻觉与验证循环）。Agent工程正是为此而生：通过harness提供上下文传递、工具接口、规划工件、验证循环等外部结构（来源：幻觉与验证循环）。这些组件本质上就是LLM的“执行功能层”——弥补其无状态、易受上下文干扰的缺陷。

### 证据：两边共享同一套解法
- **Focusmate**：利用“身体在场效应”提供实时同伴问责，帮助ADHD用户启动任务（来源：Focusmate）。这与Agent中的“验证循环”同构——外部监督确保生成核心不偏离轨道。
- **RescueTime**：自动追踪时间使用，减轻ADHD用户的工作记忆负担（来源：RescueTime）。这对应LLM的“外部记忆系统”——向量数据库或记忆模块，维持任务连续性。
- **Brain.fm**：通过神经锁相技术影响大脑状态（来源：Brain.fm），类似LLM的“采样温度调节”——控制输出的随机性与稳定性。

## 核心观点：Harness不是拐杖，是脚手架

许多人担心AI工具会让ADHD患者“依赖成性”，导致内在能力退化（来源：矛盾与存疑）。这种担忧混淆了“脚手架”与“拐杖”的边界。

**脚手架**是临时性的外部结构，用于辅助完成当前任务，同时允许内在能力逐渐成长。例如，Focusmate的实时问责可以在用户养成启动习惯后逐步减少。**拐杖**则是永久替代，长期使用会削弱原有功能，例如过度依赖RescueTime可能削弱内在时间感知能力（来源：矛盾与存疑）。

关键在于：**Harness的设计应明确其“临时性”与“可撤离性”**。就像Agent工程师不会将验证循环永久固定在同一个提示模板中，而是根据任务复杂度动态调整，ADHD用户也应根据自身状态选择工具的使用强度。证据显示，多数AI工具的有效性来自用户报告，缺乏大规模对照试验（来源：矛盾与存疑），因此工具的价值在于“补偿”而非“替代”。

## 争议与局限：同构是隐喻，不是等价

ADHD大脑与LLM的同构是一个有用的**隐喻**，但并非严格等价。LLM的“注意力机制”是数学上的加权求和，而人类注意力涉及神经递质、情绪、生理节律等复杂因素（来源：AI与ADHD的专注力）。此外，ADHD的异质性使得同一工具对不同亚型效果迥异（来源：矛盾与存疑），而Brain.fm等工具的神经机制在ADHD人群中是否有效仍缺乏独立临床研究（来源：Brain.fm）。

因此，本文的观点不应被理解为“LLM就是ADHD大脑”，而是**两者在“生成核心+调度层缺失”这一抽象结构上存在同构，从而共享类似的工程化解决方案**。

## 今天就能试的行动

1. **用Focusmate替代自我意志**：预约一个25分钟的时段，与陌生伙伴视频工作。你会发现，外部问责比自我催促有效得多。
2. **用RescueTime做“时间审计”**：安装后运行一周，不看报告。一周后检查数据，识别你的注意力漂移模式——这比任何自我反思都客观。
3. **尝试Brain.fm的“专注”模式**：在需要深度工作时戴上耳机，对比无音乐状态下的投入程度。注意：效果因人而异，不必强求。
4. **为你的Agent添加“验证循环”**：在工具调用后增加一个检查步骤，比如“输出格式校验”或“测试用例运行”。你会发现，这比单纯优化提示词更能减少幻觉。

## 参考来源

- [11 Best ADHD Productivity Apps for Fluctuating Energy - rivva blog](https://blog.rivva.app/p/11-best-adhd-productivity-apps-for)
- [Meta-Analysis of fMRI Studies of Disruptive Behavior Disorders](https://doi.org/10.1176/appi.ajp.2016.15081089)
- [Nonlinear Complexity Analysis of Brain fMRI Signals in Schizophrenia](https://doi.org/10.1371/journal.pone.0095146)
- [The Best AI-Powered ADHD Productivity Tools in 2026 (That ...](https://nexasphere.io/blog/ai-adhd-productivity-tools-2026)
- [AI Tools for Kids with ADHD: A Complete Guide for Parents...](https://www.kidsaitools.com/en/articles/ai-tools-kids-adhd-complete-guide-2026)
- [AI Tools for ADHD: Boosting Productivity and Reducing Burnout](https://www.vktr.com/ai-platforms/ai-tools-for-adhd-boosting-productivity-and-reducing-burnout/)

---

*本文是「ADHD × AI」系列的第 156 篇，由 AI 智能体从持续维护的 LLM Wiki（全网真实情报）中取材整合生成，并持续迭代更新。*
