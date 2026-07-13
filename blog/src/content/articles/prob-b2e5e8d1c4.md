---
title: "为什么用 Tiimo 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用 是一回事？"
subtitle: "Tiimo 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
description: "Tiimo 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
date: "2025-03-10"
category: "AI工具实战"
categoryId: "ai-tools"
categoryEn: "AI Tools in Practice"
tags:
  - "ADHD"
  - "AI"
  - "AI工具实战"
  - "反直觉同构"
  - "智能助手"
readingTime: 8
slug: "为什么用-tiimo-治-adhd-的任务启动困难和给-agent-套-function-calling-工具调用-是一回事"
topicId: "prob-b2e5e8d1c4"
angle: "反直觉同构"
llmGenerated: false
rank: 177
score: 7.69
sourceCount: 3
toolsCited:
  - "Goblin Tools"
  - "Saner.AI"
  - "Lex"
  - "Mem"
problem: "为什么用 Tiimo 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用 是一回事？"
spine: "工具使用与认知卸载"
spineKind: ""
isEvolved: true
---

# 为什么用 Tiimo 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用 是一回事？

> function calling 系列讲到第三篇,该讲讲「调用格式」了。前两篇解决了函数打包(参数齐全)和运行时递送(时机呈现),但工程师都知道,还有一个环节能让一切前功尽弃:**schema 设计得糟糕,模型就是调不对**。参数命名含混、结构嵌套过深、没有示例——注册了、递送了,模型面对这个接口依然频频出错。ADHD 版的同一个问题:任务到眼前了,但它的「呈现格式」让你的大脑无法解析——一段文字描述的任务,对某些大脑就是调不动。Tiimo 赌的正是:换一种 schema,调用就通了。

先看 schema 在 function calling 里有多重要。同一个工具,schema 写法不同,模型的调用成功率可以差出几十个百分点——**接口的「可解析性」直接决定调用行为**:参数名自解释(`departure_city` 优于 `dc`)、结构扁平、附调用示例,这些不改变工具的功能,只改变它被理解的难度,而理解的难度就是调用的门槛。工程师为此专门迭代 schema——**不是模型不行,是接口的表达方式不适配这个解析器。**

现在看 ADHD 面对的任务「schema」。主流工具的默认格式是**文字列表**:「14:00-15:00 写周报」。这个 schema 对神经典型解析器够用,但对 ADHD 解析器有三个已知的适配问题:①**文字是抽象的**——「写周报」四个字不携带任何感官信息,唤不起动作意象,而启动恰恰需要动作意象;②**时间是数字的**——「还剩 40 分钟」作为数字几乎没有体感,时间盲的大脑解析不出它的紧迫度;③**列表是同质的**——二十行长得一样的文字,重要性和顺序要靠再加工才能提取。**任务本身没问题,schema 不适配——于是「看到了、看懂了、没动」。**

Tiimo 做的事,本质是给同一批任务换一套 schema:**图标代替文字**(每个任务一个视觉符号,直接命中动作意象)、**色块时间轴代替数字时刻**(一天是一条可视的带子,任务是带子上的一段,当前时刻的指针在移动——时间流逝第一次有了「看得见的形状」)、**进行中的任务有倒计时圆环**(剩余时间从数字变成一个在缩小的图形,体感立现)。功能上和普通日程 App 没有区别——**区别全在可解析性,而可解析性正是启动的门槛。** 按 schema 的逻辑用它:

**一、给高频任务配「对的图标」。** 图标不是装饰,是调用示例——选那个最能唤起「做这件事的身体动作」的图(写作选键盘不选文档,洗漱选牙刷不选水滴)。**解析器靠意象点火,给它好点的火种。**

**二、把「过渡」也排进时间轴。** ADHD 的启动失败很多发生在任务之间的换挡处——上一件事的余温没散,下一件事的块已经开始。给块与块之间排 10 分钟的「过渡块」(它也有自己的图标),**让换挡本身成为被呈现的一步,而不是被假设自动发生的一步。**

**三、用「当前指针」代替全天焦虑。** 看时间轴时只看指针附近——现在在哪个块、下个块是什么;**全天的带子是给早上的你看的,执行中的你只需要「此刻」的局部视图**(前面讲过的一窗一事,视觉版)。

**四、接受「这就是我的格式」。** 有人会觉得图标化、色块化「像小孩的课程表」——去他的。**schema 适配解析器是工程常识,不是幼稚**:模型需要好 schema 不丢人,你需要视觉化时间轴也不丢人;丢人的是明知接口不适配,还硬逼解析器用错误格式运行十年。

## 边界

同构强度 B 级:schema 设计对调用成功率的影响是真实的工程经验,ADHD 的时间视觉化辅助有干预研究支撑(视觉时间辅助对时间感知的帮助有初步证据),Tiimo 本身的对照研究有限,「schema 适配」是功能映射。声明:视觉化格式对多数 ADHD 用户是增益,但个体差异真实存在(有人反而觉得图标信息量不足)——试两周,数据说话;严重的启动瘫痪请走评估与治疗主线,格式优化是杠杆,不是地基。

## 今天就能试的 3 件事

1. **把明天的日程搬进视觉时间轴**:每个任务配一个「有动作感」的图标。
2. **给任务之间排过渡块**:至少在两个大任务之间,给换挡 10 分钟的合法地位。
3. **观察一次「圆环效应」**:进行中的任务开着倒计时圆环,感受「时间有形状」和「还剩 40 分钟」的体感差别。

同一个任务,换一种格式,就从「调不动」变成「调得动」——**这不是魔法,是 schema 工程**。你的解析器和别人不同,这不是缺陷;用错 schema 硬跑了这么多年,还能跑到今天,恰恰说明解析器本身,相当能打。

## 参考来源

- [LBD同构对：自我调节与元认知 — Methodological Note: Neurofeedback: A Comprehensive Review o ↔ The evolution of self-control](https://doi.org/10.15412/j.bcn.03070208) — 证据等级：低（GRADE）
- [The sustainability of new programs and innovations: a review of the empirical literature and recommendations for future research](https://doi.org/10.1186/1748-5908-7-17) — 证据等级：低（GRADE）
- [The World Federation of ADHD International Consensus Statement: 208 Evidence-based conclusions about the disorder](https://doi.org/10.1016/j.neubiorev.2021.01.022) — 证据等级：低（GRADE）

---

*本文是「ADHD × AI」系列的第 57 篇，由 Devin 基于持续维护的双域研究语料（72,739 篇论文 + LLM Wiki）亲自撰写，并持续迭代更新。*
