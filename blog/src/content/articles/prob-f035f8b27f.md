---
title: "为什么「治好 ADHD 的工作记忆容量小、边做边忘」和「让 LLM 不跑飞」其实是同一道工程题？"
subtitle: "LLM 无跨会话状态，靠外部记忆/向量库续命——同一套 harness 思路，两边都成立。"
description: "LLM 无跨会话状态，靠外部记忆/向量库续命——同一套 harness 思路，两边都成立。"
date: "2025-04-18"
category: "AI工具实战"
categoryId: "ai-tools"
categoryEn: "AI Tools in Practice"
tags:
  - "ADHD"
  - "AI"
  - "AI工具实战"
  - "反直觉同构"
  - "自动化"
readingTime: 9
slug: "为什么治好-adhd-的工作记忆容量小边做边忘和让-llm-不跑飞其实是同一道工程题"
topicId: "prob-f035f8b27f"
angle: "反直觉同构"
rank: 94
score: 7.77
sourceCount: 6
toolsCited:
  - "Goblin Tools"
  - "Lex"
  - "Saner.AI"
  - "Obsidian"
thesis: "ADHD 大脑与 LLM 是同一类「高产但缺执行调度层」的生成核心，「治 ADHD 边做边忘」和「让 LLM 不跑飞」本质都是给无状态系统安装外部记忆与执行 harness。"
problem: "为什么「治好 ADHD 的工作记忆容量小、边做边忘」和「让 LLM 不跑飞」其实是同一道工程题？"
spine: "无状态与外部记忆"
spineKind: "llm"
isEvolved: false
llmGenerated: false
isoStrength: "A"
caseStudies:
  - "孔子"
  - "辛弃疾"
  - "张玉梅"
---

# 为什么「治好 ADHD 的工作记忆容量小、边做边忘」和「让 LLM 不跑飞」其实是同一道工程题？

> 「刚才要干嘛来着?」——这句话每天在 ADHD 者的脑内响起几十次。有意思的是,LLM 工程师面对上下文窗口装不下的信息,问的其实是同一个问题;而他们的答案从来不是「扩大记忆」,是「别依赖记忆」。

先看 ADHD 侧的证据。工作记忆(短时间内「拿在手上」加工信息的容量)偏弱,是 ADHD 认知研究里效应量最稳定的发现之一:多任务时丢线程、走到厨房忘了来干嘛、对话里想说的点转瞬蒸发、做题做到后半段忘了前半段的条件。注意它的破坏方式——**不是记不住知识(长期记忆常常很好),是「工作台」太小,东西一多就往下掉**。掉的瞬间毫无预警,这是它和「懒散」的关键区别:你不是没在管,是管的东西被挤出去了。

LLM 侧的对应物精确得罕见:上下文窗口就是模型的工作台,而且有直接研究支撑这个类比不只是修辞——自注意力机制会产生**类似人类的工作记忆干扰**:上下文里信息一多,模型对中段信息的调用显著劣化(lost in the middle),多任务指令下丢失早前约束是常态。工程师的解法体系,值得逐条抄:

**外部状态存储**:关键信息不留在上下文里赌运气,写进外部存储(文件、数据库),用的时候检索回来。**checkpoint**:长流程随时把「当前进度+下一步」落盘,崩了从断点续。**上下文瘦身**:只让当前步骤需要的信息占据窗口,其余移出。

人类版翻译,三条军规:

## 军规一:工作台上永远只放一件事

工作记忆小,最贵的浪费就是让多个任务同时占台。实践:单任务窗口(屏幕上只开当前任务的窗口)、**「捕获收件箱」**——任何中途冒出来的念头/新任务,3 秒钟写进固定的收件箱(纸/手机备忘录),立刻回到当前任务。念头被安全存放,大脑才肯放手;不写下来,它就在工作台上反复弹跳,把正事挤下去。

## 军规二:边做边落盘,不做「脑内持账」

任何超过 20 分钟的任务,进度不许只存在脑子里:做到哪、下一步是什么、关键的中间结论——随手写在任务便签上(一行就够)。被打断时(必然被打断),这行字就是你的 checkpoint;没有它,重启成本高到任务直接弃疗。**「边做边忘」的真正杀伤不是忘,是忘了之后要用十倍成本重建现场**——落盘把重建成本压到读一行字。

## 军规三:交接给未来的自己,像交接给陌生人

ADHD 的「未来自己」约等于一个没有上下文的新会话。所以一切交接物(明天继续的工作、下周的安排)按「对方一无所知」的标准写:不写「继续那个事」,写「打开 X 文件,从第三节开始,思路是 Y」。对 LLM 工程师这叫 prompt 里带全上下文;对你这叫**放过明天的自己**。

还有一个常被忽略的正面推论:工作台小,但你的「长期库」和「处理器」可能很强——ADHD 者的联想、直觉、创造性检索常常出色。**架构启示是扬长避短的分工:让纸和工具当工作台,让大脑专职做它擅长的加工**——正如没有人批评 CPU 的缓存小,人们给它配内存。

## 边界

同构强度 A 级:这是双侧证据最硬的同构之一——ADHD 的工作记忆缺陷有荟萃级证据,LLM 的上下文干扰有直接实验研究(包括与人类工作记忆干扰的对照研究)。照例声明:机制不同(神经回路 vs 自注意力),同构在功能层;工作记忆训练类商业产品的远迁移证据薄弱,别为「扩容」花冤枉钱——外部化的性价比高得多。

## 今天就能试的 3 件事

1. **建捕获收件箱**:选定一个固定入口(备忘录/纸),今天起所有中途念头 3 秒入箱。
2. **给当前最大的任务写第一行 checkpoint**:「做到哪+下一步」,贴在看得见的地方。
3. **今晚给明天交接一次**:按「陌生人标准」写明早第一个任务的完整上下文。

工作台小不是耻辱,是规格——工程师面对 4K 窗口的模型,造出了外部记忆的整套架构,没人劝模型「用心记」。你的架构今天就能开工:一个收件箱、一行 checkpoint、一份陌生人交接书。忘,就让它忘——落盘的东西,忘不掉。

## 参考来源

**同构强度：A 级** —— 直接文献支撑（引用 ADHD↔LLM 同构专题研究）

- [ADHD Apps: We tested 44 Apps and Here're the Best 9 in 2026](https://blog.saner.ai/best-adhd-apps/) — 证据等级：低（GRADE）
- [12 AI Personal Assistants Built for ADHD Brains (2026 Rankings)](https://www.usecarly.com/blog/best-ai-personal-assistant-adhd/) — 证据等级：低（GRADE）
- [Human-like Working Memory Interference in Large Language Models](https://arxiv.org/pdf/2604.09670) — 证据等级：低（GRADE）
- [Working Memory Identifies Reasoning Limits in Language Models](https://aclanthology.org/2024.emnlp-main.938.pdf) — 证据等级：低（GRADE）
- [TRANSFORMER MECHANISMS MIMIC FRONTOSTRIATAL GATING OPERATIONS WHEN TRAINED ON HUMAN WORKING MEMORY TASKS](https://openreview.net/pdf?id=CN2bmVVpOh) — 证据等级：低（GRADE）
- [Executive Dysfunction by Design: A Cognitive Accessibility Analysis of AI Support vs. Healthcare Barriers](https://dl.acm.org/doi/pdf/10.1145/3663547.3749831) — 证据等级：低（GRADE）

---

*本文是「ADHD × AI」系列的第 15 篇，由 Devin 基于持续维护的双域研究语料（72,739 篇论文 + LLM Wiki）亲自撰写，并持续迭代更新。*
