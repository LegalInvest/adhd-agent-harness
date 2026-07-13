---
title: "为什么用 Todoist 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用 是一回事？"
subtitle: "Todoist 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
description: "Todoist 实测：同一套 harness 思路，ADHD 与 LLM 两边都成立。"
date: "2025-04-20"
category: "AI工具实战"
categoryId: "ai-tools"
categoryEn: "AI Tools in Practice"
tags:
  - "ADHD"
  - "AI"
  - "AI工具实战"
  - "反直觉同构"
  - "ADHD辅助"
readingTime: 7
slug: "为什么用-todoist-治-adhd-的任务启动困难和给-agent-套-function-calling-工具调用-是一回事"
topicId: "prob-cb9cc3d065"
angle: "反直觉同构"
rank: 186
score: 7.69
sourceCount: 6
toolsCited:
  - "Todoist"
  - "Goblin Tools"
  - "Lex"
  - "Saner.AI"
  - "Motion"
  - "Reclaim.ai"
  - "ChatGPT"
  - "Claude"
thesis: "ADHD 大脑与 LLM 都是“高产生成核 + 缺执行调度层”的系统，Todoist 对人的任务启动帮助，和 function calling 对 agent 的约束，本质是同一种外部 harness：把模糊意图翻译成带参数、带时序、可验证的下一步动作。"
problem: "为什么用 Todoist 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用 是一回事？"
spine: "工具使用与认知卸载"
spineKind: ""
isEvolved: true
llmGenerated: false
isoStrength: "B"
caseStudies:
  - "孔子"
  - "孙策"
  - "Ashley Hicks"
---

# 为什么用 Todoist 治 ADHD 的任务启动困难，和给 agent 套 function calling 工具调用 是一回事？

> function calling 系列讲过打包、递送、注册——这一篇讲注册环节的一个细节,细到只有一句话,却是整个体系的咽喉:**注册的摩擦每增加一秒,注册率就掉一截。** Todoist 在任务管理工具里活了十几年,靠的不是功能多,恰恰是把「一个念头变成一条任务」的路径压到了极限短——而这件小事,正是 ADHD 任务系统成败的第一现场。

先看工程侧的对应。工具注册在 agent 框架里的演化方向很说明问题:早期要写冗长的 JSON schema、手动挂载;后来变成一个装饰器、一行声明,框架自动提取签名生成 schema——**为什么拼命压注册成本?因为注册成本高的直接后果是「该注册的没注册」**:开发者嫌麻烦,工具就散落在框架之外,模型永远调用不到它们。注册摩擦决定注册覆盖率,覆盖率决定系统上限——这是所有插件体系的共同经验。

ADHD 侧,同一条曲线更陡峭。念头(「得给医生回电话」)的存活时间以秒计,**捕捉窗口就是念头闪现的那几秒**——窗口内完成注册,任务入库;窗口内没完成,念头被下一个刺激覆盖,任务回到「凭运气想起」的荒野。所以注册流程的每一步摩擦都是致命的:解锁手机(1 秒)→找 App(3 秒)→点新建(1 秒)→选项目(3 秒)→选日期(4 秒)→填优先级(3 秒)——**十五秒的流程,足够杀死一半的捕捉**;更糟的是几次「没记下来」的挫败后,你会放弃整个系统。ADHD 弃用任务 App 的第一大死因,不是功能不够,是注册太贵。

Todoist 的看家本领恰好是把这条路径压扁:全局快捷键/小组件一步进输入框,**自然语言解析**——打「周四下午3点 给医生回电话 #健康 p1」一行,日期、时间、项目、优先级全部自动解析入库。一次注册两三秒,窗口期内绰绰有余。按「注册摩擦」的逻辑用:

**一、把入口铺到念头出现的所有现场。** 手机小组件、电脑快捷键、语音助手转发——**注册入口和念头之间的距离,是这套系统唯一重要的性能指标**。花二十分钟把所有设备的快速添加配好,这是一次性投资,回报持续多年。

**二、捕捉时只记「动作+大概时间」,其余免谈。** 窗口期内别做任何组织决策(选项目、定优先级都是税)——**一行自然语言丢进收件箱,组织留给晚上的两分钟整理**。捕捉和组织是两个阶段,混在一起做,两个都做不好。

**三、每天一次「收件箱清空」,给注册收尾。** 收件箱是缓冲区,不是归宿——**每晚(或每早)两分钟,把收件箱条目分发:定日期的进日程,该拆的拆,垃圾删掉**。缓冲区不清,注册就只完成了一半,系统会慢慢重新失去信任。

**四、任务措辞用「下一个物理动作」。** 「处理保险的事」注册了也启动不了(它是个谜语,不是任务);「找出保单拍照发给经纪人」才是可调用的函数——**注册快是入库的事,措辞对是将来调得动的事**,两件都要。

## 边界

同构强度 B 级:注册摩擦与采纳率的关系是插件体系的真实工程经验,ADHD 的前瞻记忆脆弱与捕捉窗口有文献基础,Todoist 无 ADHD 对照研究,「自然语言注册」是功能映射。声明:任务系统解决「记住与呈现」,不解决启动的神经门槛与情绪回避——列表完美但每条都点不动的状态,请回到评估与治疗以及本系列讲协议与环境的几篇;工具是漏斗的补丁,不是引擎的替代。

## 今天就能试的 3 件事

1. **配好全设备的快速添加入口**:小组件+快捷键,二十分钟一次性投资。
2. **今天所有念头,一行自然语言进收件箱**:两三秒一条,不组织。
3. **今晚做第一次收件箱清空**:两分钟,分发或删除,一条不留。

任务系统的生死,决定于念头闪现后的那三秒——**三秒内能入库的系统活下来,十五秒的系统被遗忘杀死**。别再找功能更强的工具了,先把注册的路修到三秒以内。

## 参考来源

**同构强度：B 级** —— 机制类比（ADHD 侧与 LLM/agent 侧均有真实文献，机制可映射）

- [ADHD Apps: We tested 44 Apps and Here're the Best 9 in 2026](https://blog.saner.ai/best-adhd-apps/) — 证据等级：低（GRADE）
- [12 AI Personal Assistants Built for ADHD Brains (2026 Rankings)](https://www.usecarly.com/blog/best-ai-personal-assistant-adhd/) — 证据等级：低（GRADE）
- [Agent Scaffolding: Architecture and Design Patterns for Agentic AI](https://zbrain.ai/agent-scaffolding/) — 证据等级：低（GRADE）
- [LBD同构对：任务分解与规划 — Attention-deficit/hyperactivity disorder is characterized by ↔ Language-conditioned world model improves policy generalizat](https://doi.org/10.1073/pnas.0707741104) — 证据等级：低（GRADE）
- [LBD同构对：任务分解与规划 — Safety and recommendations for TMS use in healthy subjects a ↔ AgentGen: Enhancing Planning Abilities for Large Language Mo](https://doi.org/10.1016/j.clinph.2020.10.003) — 证据等级：低（GRADE）
- [LBD同构对：任务分解与规划 — How specific are executive functioning deficits in attention ↔ AMAP Agentic Planning Technical Report](https://doi.org/10.1111/j.1469-7610.2004.00276.x) — 证据等级：低（GRADE）

---

*本文是「ADHD × AI」系列的第 66 篇，由 Devin 基于持续维护的双域研究语料（72,739 篇论文 + LLM Wiki）亲自撰写，并持续迭代更新。*
