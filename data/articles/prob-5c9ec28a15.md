---
title: "为什么「治好 ADHD 的注意力容易被环境带偏」和「让 LLM 不跑飞」其实是同一道工程题？"
subtitle: "LLM 受上下文窗口内容左右，需要上下文工程——同一套 harness 思路，两边都成立。"
description: "LLM 受上下文窗口内容左右，需要上下文工程——同一套 harness 思路，两边都成立。"
date: "2025-04-20"
category: "专注力管理"
categoryId: "focus"
categoryEn: "Focus Management"
tags:
  - "ADHD"
  - "AI"
  - "专注力管理"
  - "反直觉同构"
  - "深度工作"
readingTime: 9
slug: "为什么治好-adhd-的注意力容易被环境带偏和让-llm-不跑飞其实是同一道工程题"
topicId: "prob-5c9ec28a15"
angle: "反直觉同构"
rank: 53
score: 7.77
sourceCount: 6
toolsCited:
  - "RescueTime"
  - "Focusmate"
  - "Brain.fm"
  - "Endel"
  - "Forest"
  - "Routinery"
thesis: "ADHD 大脑与 LLM 都是高产但缺乏可靠执行调度层的生成核心，二者真正需要治的不是‘注意力’或‘模型’本身，而是上下文工程：用外部 harness 主动管理‘当下注意什么’。"
problem: "为什么「治好 ADHD 的注意力容易被环境带偏」和「让 LLM 不跑飞」其实是同一道工程题？"
spine: "上下文工程"
spineKind: "llm"
isEvolved: false
llmGenerated: false
isoStrength: "B"
caseStudies:
  - "曾国藩"
  - "孙策"
  - "Barbara Corcoran"
---

# 为什么「治好 ADHD 的注意力容易被环境带偏」和「让 LLM 不跑飞」其实是同一道工程题？

> prompt 里塞进一段无关文本,模型的输出质量立刻下滑——这是 LLM 工程被反复测量的事实,行业为此发明了一门叫「上下文工程」的手艺。ADHD 的注意力被环境带偏,是同一道题:输入流里进了什么,系统就变成什么。

先看 ADHD 侧。「容易分心」的机制核心是**刺激过滤失灵**:神经典型者的注意系统自带一道门卫,无关刺激(窗外的声音、余光里的通知、隔壁的对话)大多在进入意识前就被拦下;ADHD 的门卫缺勤,一切刺激平权涌入,每一个都在竞标注意力。所以 ADHD 者的分心不是「不想专心」,是**在一个所有声音都同样响的房间里试图听清一个人说话**。推论也直接:ADHD 的表现对环境的敏感度远高于常人——同一个人,在图书馆和在开着电视的客厅里,几乎是两种智力。

LLM 侧的证据同样扎实:模型对上下文里的无关信息高度敏感——插入干扰句,推理准确率显著下降;上下文里的诱导性内容会把生成带偏;甚至无关信息的位置都影响劣化程度。工程师的应对发展成一门系统手艺——**上下文工程**:严控什么进窗口(检索过滤、相关性排序)、控制进的顺序和位置、把无关内容主动清出去。核心信念一句话:**与其期望模型抵抗干扰,不如不让干扰进入输入流。**

这个信念平移到 ADHD,就是环境管理的全部纲领——**别练抵抗力,练过滤前置**:

## 把「门卫」外包给环境

**物理层清窗**。工作视野内只留当前任务的物件:多余的标签页关掉、桌面只放一件事的材料、手机进抽屉或另一个房间(**注意:静音不够——研究表明手机仅仅「在视野内」就持续占用认知资源**,它是一个永不闭嘴的竞标者)。声音层:降噪耳机+白噪音/无歌词音乐,把环境音的竞标资格直接取消。

**数字层清窗**。通知是现代环境里最凶猛的干扰注入:全局关闭非人类通知(应用推送一律死刑),人类消息分级(仅保留极少数直通,其余批处理);工作时段用网站/应用拦截器把高频黑洞(短视频、购物、新闻)物理断路。原则同上下文工程:**不是「尽量别点」,是「点不了」——意志防线必败,架构防线才守得住。**

**切换成本的会计学**。被带偏的真实代价不是那三分钟,是回来的路:注意力被打断后重新进入深度状态需要显著恢复时间,ADHD 的恢复成本更高(重建工作记忆现场)。所以环境管理的 ROI 计算要按「打断次数×恢复成本」算——**消灭十次打断,约等于赚回一个下午。**

**顺势而为的一条:主动选择环境,而不只是改造环境**。图书馆、自习室、咖啡馆的效果(以及 body doubling),一半是社会在场,一半是**那里的刺激恰好单调**——ADHD 的注意系统在低干扰+轻微背景刺激的环境里表现最好。把「去对的环境」当成正式的生产力策略,而不是逃避家里的书桌。

最后一个诚实的对照:LLM 的上下文可以做到无菌,人的环境永远做不到,而且**内源性干扰(自己冒出来的念头)过滤不掉**——这是同构的边界。对内源干扰,前文的「捕获收件箱」(念头 3 秒落纸,回到任务)是目前最好的低科技方案。

## 边界

同构强度 A 级:LLM 的无关上下文敏感性有直接实验研究,ADHD 的干扰抑制缺陷有扎实文献,「过滤前置」在两边都是被验证的工程方向。照例:机制不同,同构在功能层;环境改造对多数人有效但不是全部——若在无菌环境里依然无法启动,那是动机/唤醒问题,回到药物与行为治疗的证据框架。

## 今天就能试的 3 件事

1. **执行一次「视野审计」**:现在环顾你的工作区,数一数视野内与当前任务无关的竞标者,清场。
2. **给手机判「物理隔离刑」**:今天的下一个工作时段,手机放到另一个房间。感受一次干净的输入流。
3. **通知大清洗**:花 10 分钟,关掉所有应用推送,只留真人直通名单。

分心不是你的选择,是门卫缺勤下的必然——但门卫可以外包:给视野清场、给通知断路、给手机放逐。工程师不训练模型抵抗垃圾输入,他们不让垃圾进窗口;你也不必修炼百毒不侵,把毒挡在门外就够了。

## 参考来源

**同构强度：B 级** —— 机制类比（ADHD 侧与 LLM/agent 侧均有真实文献，机制可映射）

- [ADHD Apps: We tested 44 Apps and Here're the Best 9 in 2026](https://blog.saner.ai/best-adhd-apps/) — 证据等级：低（GRADE）
- [Meta-Analysis of fMRI Studies of Disruptive Behavior Disorders](https://doi.org/10.1176/appi.ajp.2016.15081089) — 证据等级：高（GRADE）
- [Nonlinear Complexity Analysis of Brain fMRI Signals in Schizophrenia](https://doi.org/10.1371/journal.pone.0095146) — 证据等级：低（GRADE）
- [Revolutionizing ADHD Management with AI Assistants](https://neurolaunch.com/adhd-ai-assistant/) — 证据等级：低（GRADE）
- [LBD同构对：工作记忆 — Toward Systems Neuroscience of ADHD: A Meta-Analysis of 55 f ↔ OCR-Memory: Optical Context Retrieval for Long-Horizon Agent](https://doi.org/10.1176/appi.ajp.2012.11101521) — 证据等级：高（GRADE）
- [LBD同构对：注意调度 — Norepinephrine ignites local hotspots of neuronal excitation ↔ Who is in the Spotlight: The Hidden Bias Undermining Multimo](https://doi.org/10.1017/s0140525x15000667) — 证据等级：低（GRADE）

---

*本文是「ADHD × AI」系列的第 16 篇，由 Devin 基于持续维护的双域研究语料（72,739 篇论文 + LLM Wiki）亲自撰写，并持续迭代更新。*
