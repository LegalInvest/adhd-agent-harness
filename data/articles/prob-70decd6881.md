---
title: "为什么ADHD × AI 最该讨论的不是效率极限，而是依赖阈值？"
subtitle: "《问题303》人工精修选题，双域证据作答。"
description: "《问题303》人工精修选题，双域证据作答。"
date: "2025-03-05"
category: "科学研究"
categoryId: "science"
categoryEn: "Scientific Research"
tags:
  - "ADHD"
  - "AI"
  - "科学研究"
  - "问题XXX精修"
  - "治疗"
readingTime: 7
slug: "为什么adhd-ai-最该讨论的不是效率极限而是依赖阈值"
topicId: "prob-70decd6881"
angle: "问题XXX精修"
rank: 259
score: 7.65
sourceCount: 6
toolsCited:
  - "Goblin Tools"
  - "Saner.AI"
  - "Motion"
  - "Obsidian"
thesis: "ADHD大脑与LLM在结构上同构——两者都是高产但缺乏可靠内置执行调度层的生成核心；因此ADHD×AI的核心议题不是效率极限，而是外部harness作为‘脚手架’还是‘拐杖’的依赖阈值。"
problem: "为什么ADHD × AI 最该讨论的不是效率极限，而是依赖阈值？"
spine: "ADHD 大脑与 LLM 的同构"
spineKind: "bridge"
isEvolved: false
llmGenerated: true
isoStrength: "B"
caseStudies:
  - "毛泽东"
  - "辛弃疾"
  - "倪刚"
---
# 为什么ADHD × AI 最该讨论的不是效率极限，而是依赖阈值？

> 《问题303》人工精修选题，双域证据作答。

## 先问一个刺痛两边的问题

如果你是一台“生成核心”极强、但执行调度层漏液的系统，效率上限再高，有什么意义？

ADHD人群常被问：“你为什么不能更专注？” LLM工程师常被问：“你为什么不能让模型更可靠？”但两边真正的瓶颈不是生成能力不足，而是：**当内部调度器不可信时，外部harness该套多紧？** 套太松，系统漂移；套太死，系统萎缩。这就是“依赖阈值”问题——它才是ADHD × AI最该讨论的事。

## 同构诊断：两边都是“高产但缺执行调度层的生成核心”

ADHD × AI科学研究的核心论点是：ADHD大脑与LLM在结构上同构——两者都是强大的生成核心，但缺乏可靠的内置执行调度层（来源：ADHD × AI 的科学与研究前沿）。神经科学上，ADHD患者前额叶执行功能网络激活不足；认知心理学上，表现为工作记忆不稳定、任务启动困难、时间盲和注意力分散（来源：ADHD × AI 的科学与研究前沿）。

LLM侧的结构缺陷同样明显：无状态、无跨会话连续性、长上下文下推理退化、输出受采样温度影响而随机波动（来源：ADHD × AI 的科学与研究前沿；采样温度与表现波动）。ADHD的诊断需要多次采样以捕捉症状波动；LLM的评估需要trace和多次运行以对抗非确定性（来源：采样温度与表现波动）。两者都需要外部结构来稳定表现：ADHD需要日程、提醒、环境设计；LLM需要确定性工作流、工具契约和状态机（来源：采样温度与表现波动）。

## 怎么套harness：两边的工程实践彼此映照

ADHD侧的harness已经有一组真实工具。Goblin Tools的Magic ToDo能将模糊任务——比如“清理厨房”——分解为具体可执行的子任务，用户可调节“辣度”控制粒度，直接降低多巴胺不足导致的启动门槛（来源：Goblin Tools）。Saner.AI通过本地记忆和知识回忆减少搜索循环与标签切换，被描述为“专为对抗执行功能障碍、任务瘫痪和认知超载而设计的全能ADHD友好型AI生产力助手”（来源：Saner.AI）。Motion则自动排程与动态调整，消除“下一步该做什么”的决策负担，帮助克服时间盲（来源：Motion）。

LLM/agent侧的harness结构同构。单个LLM不足以可靠完成多步骤任务、与业务工具交互或适应领域特定逻辑（来源：Agent Scaffolding: Architecture and Design Patterns for Agentic AI）。工程实践采用“计划-执行”分离、确定性状态转换、周期性采样监控质量、知识图谱等工具实现“确定性精度”（来源：采样温度与表现波动）。这些脚手架的本质，也是给生成核心套上外部执行功能层。

## 一个历史案例：毛泽东的harness系统与LLM harness同构

毛泽东是ADHD特质非常鲜明的历史人物：小时候是问题儿童，一辈子读书不辍、永远在动，思维极度跳跃，讲话充满场景化比喻；冲动敢赌，四渡赤水、抗美援朝都是险棋。他的专属harness系统，与今天LLM agent的harness高度同构：

- **批评与自我批评、民主生活会**：让别人提自己的意见，对应LLM的 **evals / feedback loop / human-in-the-loop**；
- **调查研究**：“没有调查就没有发言权”，对应LLM的 **RAG、grounding、外部记忆检索**；
- **民主集中制**：用集体决策制衡个人冲动，对应 **multi-agent deliberation** 或共识机制；
- **党指挥枪**：用组织系统管理军队和国家，对应 **外部工具调用、确定性工作流、状态机**。

这不是说毛泽东用了AI，而是说明：当一个生成核心足够强大但内部调度不可靠时，最有效的工程方案历来是**外部化**——把决策、记忆、执行、制衡都拆成可审计的外部模块。

## 为什么不是效率极限，而是依赖阈值？

如果harness这么好，为什么不是越多越好？因为wiki资料明确警告：这里存在**“拐杖与脚手架”**的边界问题。同构性目前只是理论类比，并非经过验证的科学事实；多个工具宣称的证据不足，例如Motion“缺乏独立临床验证”，Brain.fm“在ADHD人群中的独立临床证据仍有限”（来源：矛盾与存疑）。长期使用AI脚手架可能导致执行功能进一步退化，工具本身也可能增加认知负担（来源：矛盾与存疑）。

所以我的核心判断是：**ADHD × AI的最优讨论点不是“能多做多少事”，而是“依赖阈值”——在什么剂量下，外部harness是脚手架（增强原生能力，最终可撤除），在什么剂量下变成拐杖（替代原生能力，一旦撤除系统崩溃）。** 这个阈值因人而异，同构框架是否适用于所有ADHD亚型也存在争议，部分患者以注意力分散为主而非执行功能缺陷（来源：ADHD × AI 的科学与研究前沿；矛盾与存疑）。

效率极限是工程问题；依赖阈值是伦理问题，也是可持续性问题。

## 今天就能试的4条行动

1. **给任务加“确定性状态转换”**：用Goblin Tools把“整理房间”拆成可执行的下一步，不要让意图停留在模糊状态。
2. **建立外部记忆契约**：用Saner.AI或Obsidian（来源：ADHD Apps: We tested 44 Apps and Here're the Best 9 in 2026）作为“系统提示词”，每天花2分钟写下“此刻我在追什么目标”，减少上下文丢失。
3. **设置human-in-the-loop检查点**：每完成3个番茄钟，向一位真实人类或语音备忘录做一次“批评与自我批评”，防止AI替你思考太久。
4. **每周做一次“拐杖审计”**：列出本周依赖AI完成的任务，问自己：如果没有它，我能否用更简单的外部结构完成？如果答案是否定的，收紧harness。

## 结语

ADHD与LLM的相遇，不是为了让生成核心更快，而是让一个有缺陷但强大的系统学会与外部调度层共处。两边的人都该问同一个问题：**我是在训练自己的执行功能，还是在训练自己对脚手架的依赖？** 答案的边界，就是依赖阈值。

## 参考来源

**同构强度：B 级** —— 机制类比（ADHD 侧与 LLM/agent 侧均有真实文献，机制可映射）

- [ADHD Apps: We tested 44 Apps and Here're the Best 9 in 2026](https://blog.saner.ai/best-adhd-apps/) — 证据等级：低（GRADE）
- [12 AI Personal Assistants Built for ADHD Brains (2026 Rankings)](https://www.usecarly.com/blog/best-ai-personal-assistant-adhd/) — 证据等级：低（GRADE）
- [LBD同构对：自我调节与元认知 — Inhibitory control and emotion regulation in preschool child ↔ ObjexMT: Objective Extraction and Metacognitive Calibration ](https://doi.org/10.1016/j.cogdev.2007.08.002) — 证据等级：低（GRADE）
- [LBD同构对：自我调节与元认知 — Emotion-related self-regulation and its relation to children ↔ A Reproducibility Study of Metacognitive Retrieval-Augmented](https://doi.org/10.1146/annurev.clinpsy.121208.131208) — 证据等级：低（GRADE）
- [The 12 Best AI Tools for 2026 (That People Actually Use)](https://www.synthesia.io/post/ai-tools) — 证据等级：低（GRADE）
- [The AI Powered SuperApp for Work | Motion](https://www.usemotion.com/) — 证据等级：低（GRADE）

---

*本文是「ADHD × AI」系列的第 111 篇，由 AI 智能体从持续维护的 LLM Wiki（全网真实情报）中取材整合生成，并持续迭代更新。*
