---
title: "为什么用 Forest 治 ADHD 的注意力涣散，和给 agent 套 上下文工程 是一回事？"
subtitle: "Forest 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
description: "Forest 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
date: "2025-05-02"
category: "专注力管理"
categoryId: "focus"
categoryEn: "Focus Management"
tags:
  - "ADHD"
  - "AI"
  - "专注力管理"
  - "反直觉同构"
  - "专注力"
readingTime: 13
slug: "为什么用-forest-治-adhd-的注意力涣散和给-agent-套-上下文工程-是一回事"
topicId: "prob-9b0e2a0e47"
angle: "反直觉同构"
llmGenerated: false
rank: 280
score: 7.65
sourceCount: 4
toolsCited:
  - "Brain.fm"
  - "Focusmate"
  - "Endel"
  - "Forest"
problem: "为什么用 Forest 治 ADHD 的注意力涣散，和给 agent 套 上下文工程 是一回事？"
spine: "上下文工程"
spineKind: ""
isEvolved: true
---

# 为什么用 Forest 治 ADHD 的注意力涣散，和给 agent 套 上下文工程 是一回事？

> 系列里的工具大多在做「加法工程」:装配更好的内容、更好的时段、更好的信号。Forest 做的是最原始的「门禁工程」:种下一棵虚拟树,承诺 25 分钟不碰手机;中途拿起手机,树枯死。没有 AI,没有算法,机制简单到近乎幼稚——但它对准的,是上下文工程里逻辑上最优先的一层:**准入控制(admission control)。在讨论「窗口里放什么」之前,先得有能力对最强的污染源说不进来**。

先讲 agent 侧的准入层。上下文工程的完整堆栈里,过滤是第一道工序:哪些输入根本不允许进窗——恶意注入要挡、无关文档要筛、超长内容要拒;**如果准入层失守,后面的精细装配全是徒劳**(窗口已经被污染源占了)。且工程上有个清醒的认识:准入不能靠模型「自觉忽略」——指望模型对窗口内的干扰项视而不见,实测就是做不到(干扰项实验的一致结论);**必须在进窗之前物理拦截**。这个「自觉忽略不可行,只能物理拦截」的结论,请记住,它马上要在人类侧复现。

人类侧的头号污染源没有悬念:手机。它是自下而上捕获的完全体——变化性、社交信号、间歇性奖励,每一项都精准命中注意系统的捕获通道,对捕获过敏的 ADHD 更是降维打击(注意调度篇)。而多数人的对策恰恰是 agent 工程已判死刑的那条:「我就是不看它」——靠持续的自上而下抑制对抗一个为捕获而优化的设备,**每分钟都在消耗最稀缺的执行资源,且必输**(抑制资源会耗竭,手机不会累)。研究对「手机仅仅在场」的测量更狠:不碰、屏幕朝下,它的存在本身就占用工作记忆容量(brain drain 效应)——**污染不需要你打开它,它进了视野就开始计费**。

Forest 的机制,是给这个污染源上准入控制,拆开有三层:**①物理层的拦截**——种树期间打开其他 app 会杀死树:注意到没有,它不是「提醒你别玩」,是给「拿手机」这个动作接上了一个即时的、可见的代价——**从依赖抑制改为依赖机制**,正是 agent 准入层的逻辑(不指望自觉,直接拦);**②代价的具象化**——枯死的树是损失厌恶的实体化:抽象的「浪费了 25 分钟」不痛,一棵眼看着枯掉的树痛——这是给准入规则配了一个 ADHD 友好的即时反馈(奖赏时距篇:远的换成近的);**③承诺的时间盒**——25 分钟是有边界的承诺(「永远自律」不可信,「这 25 分钟」可信),到点树成,奖励闭环——顺便把专注切成了番茄式的可完成单元。

诚实的边界,三条:**其一,Forest 只挡手机这一个源**——电脑上的标签页、脑内的联想漂移,它管不着(准入层从来只是堆栈的第一层,不是全部);**其二,游戏化会衰减**——树的新奇性按新奇效应的规律折旧,几周后「枯就枯吧」的心态出现,需要轮换承诺机制(换成给真树捐款的模式、或换 app,机制轮换本身合法);**其三,它依赖「种树」这个启动动作**——最涣散的日子,你连树都不会种;所以它适合「有意愿但守不住」的日子,不适合「点火全灭」的日子(那是启动模块的战场)。

## 边界

同构定位(本文未做正式 A/B/C 分级):手机在场效应与注意捕获有直接实验文献,准入控制是 agent 工程的标准层,「物理拦截优于自觉忽略」的结论两侧一致;Forest 的 ADHD 特异性对照研究缺乏,游戏化承诺装置的长期效果证据以普通人群为主。声明:若手机使用已达强迫程度并伴随显著功能损害,值得专业讨论,门禁 app 不是成瘾干预。

## 今天就能试的 3 件事

1. **给下一个专注块上门禁**:种一棵树(或任何锁机工具),25 分钟——体验「不用自己抗」的差别。
2. **清除在场污染**:现在把手机放到另一个房间——brain drain 效应,看不见才停止计费。
3. **准备好机制轮换**:Forest 无感了就换承诺形式(捐款版/和朋友对赌)——衰减是规律,轮换是对策。

对最强的污染源,agent 工程的结论冷酷而解放:**别训练自己忽略它,拦在窗外**。一棵会枯死的树的全部智慧:把「说不」从你的意志力里,搬进机制里。

## 参考来源

- [Meta-analysis of social cognition in attention-deficit/hyperactivity disorder (ADHD): comparison with healthy controls and autistic spectrum disorder](https://doi.org/10.1017/s0033291715002573) — 证据等级：高（GRADE）
- [Impulsiveness as a timing disturbance: neurocognitive abnormalities in attention-deficit hyperactivity disorder during temporal processes and normalization with methylphenidate](https://doi.org/10.1098/rstb.2009.0014) — 证据等级：低（GRADE）
- [American Medical Society for Sports Medicine Position Statement](https://doi.org/10.1097/jsm.0b013e31827f5f93) — 证据等级：低（GRADE）
- [Artificial intelligence in ADHD: a global perspective on ...](https://pmc.ncbi.nlm.nih.gov/articles/PMC12018397/) — 证据等级：低（GRADE）

---

*本文是「ADHD × AI」系列的第 131 篇，由 Devin 基于持续维护的双域研究语料（72,739 篇论文 + LLM Wiki）亲自撰写，并持续迭代更新。*
