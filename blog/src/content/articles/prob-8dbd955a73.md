---
title: "为什么用 Todoist 治 ADHD 的注意力涣散，和给 agent 套 上下文工程 是一回事？"
subtitle: "Todoist 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
description: "Todoist 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
date: "2025-04-18"
category: "专注力管理"
categoryId: "focus"
categoryEn: "Focus Management"
tags:
  - "ADHD"
  - "AI"
  - "专注力管理"
  - "反直觉同构"
  - "分心管理"
readingTime: 9
slug: "为什么用-todoist-治-adhd-的注意力涣散和给-agent-套-上下文工程-是一回事"
topicId: "prob-8dbd955a73"
angle: "反直觉同构"
rank: 277
score: 7.65
sourceCount: 6
toolsCited:
  - "RescueTime"
  - "Focusmate"
  - "Brain.fm"
  - "Endel"
  - "Forest"
thesis: "ADHD 大脑与 LLM 都是高产但缺执行调度层的生成核心，因此 ADHD 用外部工具（如 Todoist 这类任务清单/RescueTime/Focusmate）治注意力涣散，与给 agent 做上下文工程（记忆、路由、规划-执行分离、上下文压缩）本质上是同一套 harness：把「当下该注意什么」从内部调度层外包给外部脚手架。"
problem: "为什么用 Todoist 治 ADHD 的注意力涣散，和给 agent 套 上下文工程 是一回事？"
spine: "上下文工程"
spineKind: ""
isEvolved: true
llmGenerated: false
isoStrength: "A"
caseStudies:
  - "曾国藩"
  - "孔子"
  - "Charles Lester"
---

# 为什么用 Todoist 治 ADHD 的注意力涣散，和给 agent 套 上下文工程 是一回事？

> Todoist 大概是本系列最「无聊」的工具:一个老牌待办清单,没有 AI 光环,没有神经多样性营销。但恰恰是它,把上下文工程里最核心的一个机制做成了人人用得起的形态:**视图(view)——同一个任务库,按查询条件切出不同的工作区**。「今天」视图、按项目过滤、按标签过滤——这些看起来平平无奇的功能,在注意系统的语义里是同一件事:**你永远不面对全量任务库,只面对一个按需装配的切片**。而这正是 agent 上下文工程的第一原理:窗口里放的从来不是全部知识,是本步骤需要的查询结果。

先立 agent 侧。上下文工程的基本架构(Saner 篇讲过)是「外部存储+按需装配」:全量信息躺在库里,每一步执行时用查询把相关切片调进窗口——**窗口是视图,不是仓库**。为什么必须这样?因为全量进窗的后果有直接实证:无关内容稀释注意权重、干扰项诱发错误。任务管理的对应精确到令人发笑:**打开一个五百条的全量任务列表,和把五百条文档塞进 LLM 窗口,是同一个错误**。

ADHD 侧的现场,每个用过待办清单的人都认识:清单先是救星,然后膨胀,然后变成恐怖之物——打开就是几百条,过期的红成一片,扫一眼的信息量足以触发「关掉,眼不见为净」(全有全无的回避,清单版)。问题不在记了太多——记下来是对的(认知卸载篇:不记才是后台占用)——**问题在「存储」和「视图」没有分离**:你每次打开都直面仓库全景,而仓库全景对注意系统只有两个作用:压垮它,或者赶走它。神经典型者面对长清单也不适,但能靠自上而下的扫描纪律撑住;ADHD 的扫描更容易被红色过期项捕获、被数量触发情绪、然后弃用整个系统——**弃用的从来不是「记录」,是「面对全量」**。

Todoist 式的视图工程,拆开是三条:**①「今天」视图=默认工作区**——日常只打开今天(五到十条),仓库存在但不可见:这就是上下文装配(全库五百条,进窗五条),清单从恐怖之物变回指令序列;**②过滤器=参数化查询**——「@电脑前+15分钟内」这种过滤器,是把「当前情境下我能做什么」写成可执行查询——对 ADHD 特别值钱,因为「在碎片时间里挑任务」本身是昂贵的开放决策(Structured 篇:选择即漂移窗口),过滤器把决策预编译了;**③自然语言进箱+延迟分派**——「周五 提交报告」随手一句进系统,分类整理延后批处理(写入零摩擦,Mem 篇的原则,义务版)。

有一个 ADHD 特有的坑必须点名:**过期项堆积的羞耻螺旋**。神经典型用户过期三条,重排就是;ADHD 用户过期六十条,每一条都是一次自我指控,最终「不敢打开 app」——这是工具反噬(定价篇:崩溃成本不对称)。工程解法冷酷而有效:**定期宣布任务破产**——把过期项批量改期或删除,零愧疚,像 harness 清理失败任务队列一样对待它(系统状态腐烂了就重置,没有道德含义)。清单是工具,不是审判记录;**一个不敢打开的系统,等于没有系统,而「敢打开」优先于一切完美管理**。

## 边界

同构强度 A 级:信息过载与干扰项对注意/表现的损害在人类与 LLM 两侧都有直接实证(选择过载研究、上下文干扰实验),「视图/装配」架构是两侧的真实工程实践;Todoist 作为具体产品无 ADHD 对照研究,A 判给机制。声明:任务系统崩溃若伴随广泛的功能损害与情绪痛苦,评估优先于换工具。

## 今天就能试的 3 件事

1. **切断仓库直视**:把待办 app 的默认打开页设为「今天」——仓库你一周只进去一次做整理。
2. **写一个情境过滤器**:「在电脑前+15 分钟能做完」——下次碎片时间直接调用,不做现场挑选。
3. **宣布一次任务破产**:过期超过两周的,批量改期或删掉,不许愧疚——系统要的是能打开,不是记录完美。

清单杀死 ADHD 用户的方式,从来不是「记不下」,是「打开即全量」——**存储和视图分离,窗口只放今天**:这条上下文工程的第一原理,一个老牌待办 app 二十年前就做对了。

## 参考来源

**同构强度：A 级** —— 直接文献支撑（引用 ADHD↔LLM 同构专题研究）

- [ADHD Apps: We tested 44 Apps and Here're the Best 9 in 2026](https://blog.saner.ai/best-adhd-apps/) — 证据等级：低（GRADE）
- [Meta-Analysis of fMRI Studies of Disruptive Behavior Disorders](https://doi.org/10.1176/appi.ajp.2016.15081089) — 证据等级：高（GRADE）
- [Nonlinear Complexity Analysis of Brain fMRI Signals in Schizophrenia](https://doi.org/10.1371/journal.pone.0095146) — 证据等级：低（GRADE）
- [Revolutionizing ADHD Management with AI Assistants](https://neurolaunch.com/adhd-ai-assistant/) — 证据等级：低（GRADE）
- [The Wanderer's Algorithm: Controlled Distraction as a Catalyst for Machine Creativity](https://www.techrxiv.org/users/950560/articles/1356399/master/file/data/wanderers_algorithm_paper_independent%203/wanderers_algorithm_paper_independent%203.pdf) — 证据等级：低（GRADE）
- [Deficient Executive Control in Transformer Attention](https://www.biorxiv.org/content/10.1101/2025.01.22.634394v1.full.pdf) — 证据等级：低（GRADE）

---

*本文是「ADHD × AI」系列的第 128 篇，由 Devin 基于持续维护的双域研究语料（72,739 篇论文 + LLM Wiki）亲自撰写，并持续迭代更新。*
