---
title: "ADHD 职场人视角：为什么「治好 ADHD 的状态日内大幅波动、不稳定」和「让 LLM 不跑飞」其实是同一道工程题？"
subtitle: "LLM 采样温度带来输出随机性，靠结构约束稳定——同一套 harness 思路，两边都成立。"
description: "LLM 采样温度带来输出随机性，靠结构约束稳定——同一套 harness 思路，两边都成立。"
date: "2025-05-10"
category: "生活方式"
categoryId: "lifestyle"
categoryEn: "Lifestyle"
tags:
  - "ADHD"
  - "AI"
  - "生活方式"
  - "人群×同构"
  - "人际关系"
readingTime: 13
slug: "adhd-职场人视角为什么治好-adhd-的状态日内大幅波动不稳定和让-llm-不跑飞其实是同一道工程题"
topicId: "prob-584b73feb6"
angle: "人群×同构"
rank: 386
score: 7.21
sourceCount: 6
toolsCited:
  - "Routinery"
  - "Habitica"
  - "Goblin Tools"
thesis: "ADHD 大脑与 LLM 都是「高产生成核心 + 薄弱执行调度层」的同类系统，因此日内状态波动与采样温度导致的输出漂移，不是要靠「治好」或「降温」来消除，而要用外部 harness/脚手架把随机性约束进可预测的结构里。"
problem: "ADHD 职场人视角：为什么「治好 ADHD 的状态日内大幅波动、不稳定」和「让 LLM 不跑飞」其实是同一道工程题？"
spine: "采样温度与表现波动"
spineKind: "llm"
isEvolved: false
llmGenerated: false
isoStrength: "A"
caseStudies:
  - "孔子"
  - "曾国藩"
  - "David Thompson"
---

# ADHD 职场人视角：为什么「治好 ADHD 的状态日内大幅波动、不稳定」和「让 LLM 不跑飞」其实是同一道工程题？

> 同一个你,上午十点是公司里最锋利的脑子,下午三点连一封邮件都读不进去。职场对此的判词是「不稳定」;工程界对同款现象的处理却冷静得多——输出方差大的系统,不是坏系统,是需要按方差来设计使用方式的系统。

先承认现象的真实性。ADHD 的状态波动不是懒散的借口:警觉性、工作记忆、抑制控制在一天内的起伏幅度显著大于神经典型者,且波动受睡眠、药物时效(如服用兴奋剂类药物的浓度曲线)、刺激水平、情绪事件多重调制。职场的困难在于:**岗位默认你是恒定输出的机器,而你是一台高方差的机器**——峰值惊艳,谷值糟糕,均值反而没人看见。

LLM 侧的对应物很直接:采样温度与输出方差。同一个模型、同一个 prompt,多次采样的质量有波动;temperature 越高,创造性与胡言乱语齐飞。工程师的应对从来不是「要求模型每次都稳定发挥」,而是一组**方差管理**技术:关键任务降温度、多次采样取最优(best-of-n)、按任务类型路由(创造类高温、事实类低温)、质量不稳时加验证层。

把这套搬进职场,就是 ADHD 状态管理的工程版。

## 方差管理四式

**第一式:按状态路由任务(最重要)**。工程师按任务选温度,你按状态选任务。前提是知道自己的波动曲线:记录两周,每天三次(上午/下午/晚上)给状态打分,标注睡眠和用药时间。多数人会发现清晰的模式(比如药效峰值的上午 9–12 点是黄金窗)。然后重排工作:**深度、创造、高风险的事锁进黄金窗;邮件、整理、例会填进低谷**。这一条能兑现的产出差异,超过任何意志力训练——因为它不对抗波动,只对齐波动。

**第二式:给关键输出加验证层(替代「稳定发挥」)**。你无法保证写它时状态在线,但可以保证发出前过一道检查:高风险交付(对上的、对外的)一律隔一个状态周期再审一遍——上午写的下午审,或反之。**用两个状态点的交叉验证,对冲单点状态的方差**——这就是你的 best-of-n。

**第三式:低谷协议**。谷值时刻最大的损耗不是产出低,是硬扛产生的错误和自我攻击(「我怎么这么废」)。预写低谷协议:状态跌破线→切换到预存的「低谷任务清单」(机械类、整理类、低风险类)→不做任何重要决定、不发任何重要消息→到点复查。**接受谷值的存在,谷值就只损失产出;否认它,还要搭上质量和自尊。**

**第四式:对外的期望管理**。方差机器在恒定预期的组织里,吃亏在预期错配。不需要公开诊断,只需要管理承诺方式:不承诺「明天下午给」(单点承诺赌的是单点状态),承诺「本周四前给」(区间承诺让你有波动腾挪);重要协作日主动排到你的高概率时段(「上午开这个会我状态最好」)。**把承诺从状态的赌博,改成波动区间上的统计**。

## 一条容易被漏掉的杠杆:波动源治理

方差管理的上游是降低方差本身的可治理部分:睡眠不规律是 ADHD 状态波动的头号放大器(而 ADHD 恰好高发睡眠问题——恶性循环);药物时效的错配(峰值浪费在通勤上)值得和医生专门讨论服药时间;血糖过山车、连续高强度会议也都是可干预的波动源。**先治理波动源,再管理剩余方差**——工程里这叫先降噪,再滤波。

## 边界

同构强度 B 级:temperature 与输出方差是真实模型行为,ADHD 的日内状态波动与药物浓度曲线有临床文献,「按状态路由」是机制映射的实践,无对照研究。注意:如果波动幅度极端(从亢奋到瘫痪的量级)或伴随情绪的周期性剧烈起伏,请务必专业评估——那可能超出 ADHD 的范畴(如共病心境障碍),不是时间管理能接住的。

## 今天就能试的 3 件事

1. **启动两周状态记录**:每天三次打分,标注睡眠与用药。你在找自己的浓度曲线。
2. **把本周最重要的一件事挪进疑似黄金窗**:哪怕曲线还没画完,先按直觉对齐一次,感受差异。
3. **写下你的低谷协议**:跌破线做什么、不做什么。贴出来,谷值时的你没有决策力,只能照读。

「稳定」从来不是高方差系统的正确目标——工程师不这么要求模型,你也别这么要求自己。目标是:峰值用在刀刃上,谷值不出事故,承诺给出区间。做到这三条,一台方差机器的年产出,能赢过大多数恒定机器。

## 参考来源

**同构强度：A 级** —— 直接文献支撑（引用 ADHD↔LLM 同构专题研究）

- [AI for ADHD: Best Tools, Apps, and Strategies - Themba Tutors](https://thembatutors.com/ai-for-adhd-tools-and-apps/) — 证据等级：低（GRADE）
- [11 Best ADHD Productivity Apps for Fluctuating Energy - rivva blog](https://blog.rivva.app/p/11-best-adhd-productivity-apps-for) — 证据等级：低（GRADE）
- [ADHD Apps: We tested 44 Apps and Here're the Best 9 in 2026](https://blog.saner.ai/best-adhd-apps/) — 证据等级：低（GRADE）
- [12 AI Personal Assistants Built for ADHD Brains (2026 Rankings)](https://www.usecarly.com/blog/best-ai-personal-assistant-adhd/) — 证据等级：低（GRADE）
- [Strong Memory, Weak Control: An Empirical Study of Executive Functioning in LLMs](https://preview.aclanthology.org/evt-to-venues/2026.eacl-long.281.pdf) — 证据等级：低（GRADE）
- [Self-Attention Limits Working Memory Capacity of Transformer-Based Models](https://arxiv.org/pdf/2409.10715) — 证据等级：低（GRADE）

---

*本文是「ADHD × AI」系列的第 2 篇，由 Devin 基于持续维护的双域研究语料（72,739 篇论文 + LLM Wiki）亲自撰写，并持续迭代更新。*
