---
title: "ADHD 创业者视角：为什么「治好 ADHD 的被批评却不知道错在哪一步，反馈延迟就失去动力」和「让 LLM 不跑飞」其实是同一道工程题？"
subtitle: "agent 拿到 episode 末尾的标量 reward，却不知该强化哪个动作（credit assignment）——同一套 harness 思路，两边都成立。"
description: "agent 拿到 episode 末尾的标量 reward，却不知该强化哪个动作（credit assignment）——同一套 harness 思路，两边都成立。"
date: "2025-03-17"
category: "科学研究"
categoryId: "science"
categoryEn: "Scientific Research"
tags:
  - "ADHD"
  - "AI"
  - "科学研究"
  - "人群×同构"
  - "研究"
readingTime: 7
slug: "adhd-创业者视角为什么治好-adhd-的被批评却不知道错在哪一步反馈延迟就失去动力和让-llm-不跑飞其实是同一道工程题"
topicId: "prob-a4427fb8d6"
angle: "人群×同构"
rank: 84
score: 7.81
sourceCount: 6
toolsCited:
  - "Goblin Tools"
  - "Motion"
  - "Saner.AI"
thesis: "ADHD 大脑与 LLM/agent 都是强大的生成核心配脆弱的内置调度层，所以「被批评却不知错在哪一步」和「episode 末尾的标量 reward 不知如何强化动作」是同一个反馈信用分配问题；解法不是继续生产更聪明的生成器，而是外挂一个会拆分步骤、即时授信、允许人在回路的 harness。"
problem: "ADHD 创业者视角：为什么「治好 ADHD 的被批评却不知道错在哪一步，反馈延迟就失去动力」和「让 LLM 不跑飞」其实是同一道工程题？"
spine: "反馈信用分配"
spineKind: "bridge"
isEvolved: false
llmGenerated: true
isoStrength: "B"
caseStudies:
  - "毛泽东"
  - "孔子"
  - "徐刚"
---
# ADHD 创业者视角：为什么「治好 ADHD 的被批评却不知道错在哪一步，反馈延迟就失去动力」和「让 LLM 不跑飞」其实是同一道工程题？

> agent 拿到 episode 末尾的标量 reward，却不知该强化哪个动作（credit assignment）——同一套 harness 思路，两边都成立。

## 两种崩溃：一句批评 vs. 一个标量 reward

先想象两个画面。

画面 A：一位 ADHD 创业者刚把方案发出去，老板回了一句“不行，重写”。他知道结果不好，却不知道哪一步错了——是开头定位、中间数据，还是最后结论？反馈没有拆到动作级，多巴胺机器立刻熄火。研究显示，ADHD 创业者的创业概率是对照组的 6.25 倍（来源：Journal of Attention Disorders 2019），但高创造力的另一面，是他们对“结果反馈”极其敏感，对“步骤反馈”极其饥渴。

画面 B：一位做 Agentic Harness 的工程师看着 agent 跑完一个 episode，最后收到一个标量 reward：0.3。他不知道哪一步该被强化——是检索工具调用早了？还是 chain-of-thought 里某一步推导错了？这叫 credit assignment 问题，RL 经典困境。

两个画面共享同一个结构：系统都靠一个强大的生成核心输出复杂行为，但反馈信号来得太晚、太粗、太末端。大脑和 agent 都需要把 reward 拆到动作链路上，否则要么掉动力，要么跑飞。

## 同构病根：强大的生成核心，缺一个调度层

ADHD 的大脑不是不聪明，而是“驾驶座常常没人”。fMRI 研究显示，前额叶执行功能网络激活不足（来源：ADHD × AI 的科学与研究前沿）。最新认知剖面进一步把它描述为“强记忆、弱控制”（来源：生成核心与调度层）：信息在、灵感在，但自上而下的控制、排序、门控不在线。

LLM 如出一辙。它可以生成连贯长文本、写代码、做推理，但单独运行时没有稳定的执行调度层。OpenDev 等现代 AI 编码代理的做法，是用“工作负载专用模型路由、分离规划与执行的双代理架构、惰性工具发现、自适应上下文压缩”来补上这个缺口（来源：生成核心与调度层）。本质上，这叫 agent scaffolding：一个由提示、记忆、代码、工具和编排逻辑组成的模块化框架，把 LLM 这颗生成核心套进能用的 harness 里（来源：生成核心与调度层）。

所以两边是同一类架构：高产但缺执行调度层。ADHD 的“时间盲”“任务启动难”“工作记忆不稳”，与 LLM 的“上下文膨胀”“推理退化”“任务切换崩”是同一个调度层失效的两种表现（来源：ADHD × AI 的科学与研究前沿）。

## 从 Harness 名人看：毛泽东与孔子的“外部执行系统”

真实历史中，高能量、高发散的头脑往往靠外部 harness 才不出轨。毛泽东和孔子都高度符合 ADHD 的行为模式，也都给自己搭了严密的执行系统。

毛泽东小时候是“问题儿童”，和父亲吵架、爱读闲书、坐不住；成年后永远在动，行军路上带书，思维极度跳跃，讲话全是场景化比喻；决策又极敢赌，四渡赤水、抗美援朝都是险棋（来源：案例素材）。他的 harness 是：调查研究（没有调查就没有发言权）、民主集中制（用集体决策制衡冲动）、批评与自我批评（让别人给自己提意见）、党指挥枪（用组织系统管理军队）。这些分别对应 agent 的 grounding 工具调用、外部仲裁器、human-in-the-loop 反馈和分层编排逻辑。他不是靠“更努力克制”成功，而是把决策和执行外包给一个可追责的结构。

孔子身高一米九，精力旺盛，周游列国十四年，冲动到见南子要对天发誓、骂宰予“朽木不可雕”；但他对音乐又能超专注到“三月不知肉味”，对种地俗事零耐心（来源：案例素材）。他的 harness 是“礼”：用外在行为规范作为边界，每日“吾日三省吾身”，七十岁才“从心所欲不逾矩”。这对应 LLM 的 prompt 约束、guardrails 和 episode replay：先用外部规则把行为空间切小，再用高频反省做 reward shaping，最终把约束内化为生成器的习惯。

两个人的共性在于： harness 不是“让自己变乖”，而是把信用分配拆到日常动作上——每一步都有人、有规则、有反馈。

## 把 credit 拆到每一步：今天可用的工具

好消息是，这一 harness 思路已经产品化。ADHD 侧和 LLM 侧的解法结构

## 参考来源

**同构强度：B 级** —— 机制类比（ADHD 侧与 LLM/agent 侧均有真实文献，机制可映射）

- [ADHD Apps: We tested 44 Apps and Here're the Best 9 in 2026](https://blog.saner.ai/best-adhd-apps/) — 证据等级：低（GRADE）
- [12 AI Personal Assistants Built for ADHD Brains (2026 Rankings)](https://www.usecarly.com/blog/best-ai-personal-assistant-adhd/) — 证据等级：低（GRADE）
- [LBD同构对：自我调节与元认知 — Inhibitory control and emotion regulation in preschool child ↔ ObjexMT: Objective Extraction and Metacognitive Calibration ](https://doi.org/10.1016/j.cogdev.2007.08.002) — 证据等级：低（GRADE）
- [LBD同构对：自我调节与元认知 — Emotion-related self-regulation and its relation to children ↔ A Reproducibility Study of Metacognitive Retrieval-Augmented](https://doi.org/10.1146/annurev.clinpsy.121208.131208) — 证据等级：低（GRADE）
- [The 12 Best AI Tools for 2026 (That People Actually Use)](https://www.synthesia.io/post/ai-tools) — 证据等级：低（GRADE）
- [The AI Powered SuperApp for Work | Motion](https://www.usemotion.com/) — 证据等级：低（GRADE）

---

*本文是「ADHD × AI」系列的第 14 篇，由 AI 智能体从持续维护的 LLM Wiki（全网真实情报）中取材整合生成，并持续迭代更新。*
