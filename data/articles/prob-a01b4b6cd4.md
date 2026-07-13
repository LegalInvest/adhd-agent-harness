---
title: "为什么200个Skill不是数字囤积而是MoE专家库——你的囤积癖正在搭建认知基础设施"
subtitle: "《问题047》人工精修选题，双域证据作答。"
description: "《问题047》人工精修选题，双域证据作答。"
date: "2025-05-22"
category: "科学研究"
categoryId: "science"
categoryEn: "Scientific Research"
tags:
  - "ADHD"
  - "AI"
  - "科学研究"
  - "问题XXX精修"
  - "脑科学"
readingTime: 11
slug: "为什么200个skill不是数字囤积而是moe专家库你的囤积癖正在搭建认知基础设施"
topicId: "prob-a01b4b6cd4"
angle: "问题XXX精修"
rank: 156
score: 7.71
sourceCount: 6
toolsCited:
  - "Goblin Tools"
  - "Saner.AI"
  - "Motion"
  - "Focusmate"
thesis: "ADHD 大脑与 LLM 是同一类高产但缺少执行调度层的生成核心，你囤下的 200 个 Skill 不是数字囤积，而是正在生长中的 MoE 专家库；只有搭好外部 harness（路由+记忆+调度+问责），这些散落的专家才能变成可运行的认知基础设施。"
problem: "为什么200个Skill不是数字囤积而是MoE专家库——你的囤积癖正在搭建认知基础设施"
spine: "ADHD 大脑与 LLM 的同构"
spineKind: "bridge"
isEvolved: false
llmGenerated: false
isoStrength: "B"
caseStudies:
  - "毛泽东"
  - "释迦牟尼"
  - "Amy Silva"
---

# 为什么200个Skill不是数字囤积而是MoE专家库——你的囤积癖正在搭建认知基础设施

> ADHD 的数字生活有个经典自责项:收藏夹几千条、笔记软件里两百个半成品模板、AI 工具里攒了一堆 prompt 和自定义指令——「又在囤积,又不会用」。慢着。在给这个行为判刑之前,值得先看一眼 LLM 工程里一个体面的架构:Mixture of Experts。它可能会改变你对自己那堆「数字囤积」的判决——从罪名,改成半成品的基础设施。

先讲 MoE 讲清楚。大模型的一种高效架构:**不用一个巨大的通才网络处理所有输入,而是养一群「专家」子网络,外加一个路由器**——每个 token 进来,路由器判断该唤醒哪几个专家,只激活那一小部分。要点有二:①专家多而闲置是常态,**绝大多数专家在绝大多数时刻是沉睡的,这不是浪费,是设计**;②整个架构的成败不在专家数量,**在路由器的质量**——路由不准,再多专家也是一堆昂贵的沉默参数。

现在看你的两百个 Skill/prompt/模板/收藏。按 MoE 的标准重新验收:**「囤积了很多专家」本身无罪**——你为「写周报」「拆任务」「改邮件语气」「会前准备」各攒过一个用法,它们大部分时间沉睡,这和 MoE 的专家闲置是同一件事,不需要羞耻。**真正的问题只有一个:你没有路由器。** 需要写周报的周五下午,你不会想起收藏夹第三层有个完美的模板——于是每个专家都在,每次调用都失败,系统表现得像什么都没有。ADHD 的检索弱项(想不起来自己有什么)恰恰是路由器缺失的神经版本。

所以改进方向不是「断舍离,删到十个」(那是砍专家),是**补路由**。三步:

**一、给专家建索引页——路由表。** 一页纸(或置顶笔记),按触发场景组织,不按工具组织:「要写周报→用 X」「任务卡住→用 Y」「邮件火药味→用 Z」。**场景是路由的键,工具只是值**——你检索失败的原因,是过去按工具存(「这是个好 prompt」),从没按场景存(「什么时候用它」)。两百个专家,先给最常用的十五个建路由,其余保持沉睡,无妨。

**二、把高频路由做成物理反射。** 路由表本身也会被忘记(路由器也需要被路由,这是 ADHD 的套娃困境)。解法是把 top 3 场景的路由直接铺在路径上:周报模板钉在周五下午的日历提醒里;拆任务的 prompt 存成输入法短语;情绪缓冲的用法写在便签贴屏幕边。**最好的路由器是不需要想起来的那种。**

**三、用「激活率」做季度清理,而不是用道德。** 每季度看一眼:哪些专家整季零激活?两种处理——要么它对应的场景真实存在但路由没建好(补路由),要么场景本身不存在(这个专家是「幻想中的自己」需要的,比如那个从没用过的「学术论文精读模板」)。后者删掉时不必心痛:**你删的不是资产,是一份对幻想自我的订阅。**

顺带把「囤积冲动」本身也安顿了:ADHD 的收集冲动(新工具、新方法、新模板的多巴胺)不必戒除,**给它一个入口收件箱**——新专家一律先进收件箱,月底统一验收:能写出触发场景的,建路由入库;写不出的,让它过期。冲动被承认,系统不被污染。

## 边界

同构强度 C 级:如实标注——MoE 是真实架构,但「个人工具库=专家库」是修辞层面的类比,ADHD 的收集行为与检索困难有文献支撑,而本文框架无实证验证;把它当一个减少自责、指导整理的透镜。声明:若囤积已延伸到物理空间并造成功能损害,或伴随强烈的丢弃焦虑,那可能涉及囤积障碍的范畴(与 ADHD 常共病),值得专业评估,不是一张路由表能解决的。

## 今天就能试的 3 件事

1. **建路由表第一版**:只写五行,「场景→工具」,置顶。
2. **把一条高频路由做成反射**:一个输入法短语,或一张贴在屏幕边的便签。
3. **给收集冲动开收件箱**:今天起新收藏先进箱,月底验收,写不出使用场景的自动过期。

两百个专家沉睡在你的收藏夹里,MoE 会说:数量没问题,去修路由器。**囤积和基础设施的区别,从来不在拥有多少,在需要的那一刻,能不能被唤醒。**

## 参考来源

**同构强度：B 级** —— 机制类比（ADHD 侧与 LLM/agent 侧均有真实文献，机制可映射）

- [ADHD Apps: We tested 44 Apps and Here're the Best 9 in 2026](https://blog.saner.ai/best-adhd-apps/) — 证据等级：低（GRADE）
- [12 AI Personal Assistants Built for ADHD Brains (2026 Rankings)](https://www.usecarly.com/blog/best-ai-personal-assistant-adhd/) — 证据等级：低（GRADE）
- [LBD同构对：自我调节与元认知 — Inhibitory control and emotion regulation in preschool child ↔ ObjexMT: Objective Extraction and Metacognitive Calibration ](https://doi.org/10.1016/j.cogdev.2007.08.002) — 证据等级：低（GRADE）
- [LBD同构对：自我调节与元认知 — Emotion-related self-regulation and its relation to children ↔ A Reproducibility Study of Metacognitive Retrieval-Augmented](https://doi.org/10.1146/annurev.clinpsy.121208.131208) — 证据等级：低（GRADE）
- [The 12 Best AI Tools for 2026 (That People Actually Use)](https://www.synthesia.io/post/ai-tools) — 证据等级：低（GRADE）
- [The AI Powered SuperApp for Work | Motion](https://www.usemotion.com/) — 证据等级：低（GRADE）

---

*本文是「ADHD × AI」系列的第 52 篇，由 Devin 基于持续维护的双域研究语料（72,739 篇论文 + LLM Wiki）亲自撰写，并持续迭代更新。*
