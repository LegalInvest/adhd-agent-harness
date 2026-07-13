---
title: "ADHD 程序员视角：为什么「治好 ADHD 的不擅长精确、重复、状态维护类任务」和「让 LLM 不跑飞」其实是同一道工程题？"
subtitle: "agent 通过 function calling 把精确计算外包给工具——同一套 harness 思路，两边都成立。"
description: "agent 通过 function calling 把精确计算外包给工具——同一套 harness 思路，两边都成立。"
date: "2025-05-04"
category: "AI工具实战"
categoryId: "ai-tools"
categoryEn: "AI Tools in Practice"
tags:
  - "ADHD"
  - "AI"
  - "AI工具实战"
  - "人群×同构"
  - "智能助手"
readingTime: 13
slug: "adhd-程序员视角为什么治好-adhd-的不擅长精确重复状态维护类任务和让-llm-不跑飞其实是同一道工程题"
topicId: "prob-d50b27e6e3"
angle: "人群×同构"
rank: 78
score: 7.81
sourceCount: 6
toolsCited:
  - "Goblin Tools"
  - "Lex"
  - "Saner.AI"
  - "Motion"
  - "Reclaim.ai"
  - "Tiimo"
thesis: "ADHD 大脑与 LLM 都是「高产生成核心 + 缺执行调度层」的同构系统，两边的解法不是「治好它」，而是安装同一套外部 harness：把精确、重复、状态维护类任务外包给工具与仪式，用上下文约束把爆发力导入可验证的执行轨道。"
problem: "ADHD 程序员视角：为什么「治好 ADHD 的不擅长精确、重复、状态维护类任务」和「让 LLM 不跑飞」其实是同一道工程题？"
spine: "工具使用与认知卸载"
spineKind: "llm"
isEvolved: false
llmGenerated: false
isoStrength: "A"
caseStudies:
  - "孔子"
  - "苏轼"
  - "Megan Young"
---

# ADHD 程序员视角：为什么「治好 ADHD 的不擅长精确、重复、状态维护类任务」和「让 LLM 不跑飞」其实是同一道工程题？

> 程序员这个职业有个隐藏福利:它是人类历史上第一个把「精确、重复、状态维护」几乎全部自动化了的工种——前提是你肯把那些工具也用在自己的短板上,而不是只用在生产环境里。

先看 ADHD 程序员在这三类任务上的典型事故单。**精确类**:配置文件里的一个错别字查了一下午;环境变量少了个下划线;提交时漏了一个文件;改了代码忘了改文档。**重复类**:手动部署第五次时跳了一步;逐个改二十处同样的代码,改漏三处;写测试(重复感最强的活)永远欠账。**状态维护类**:三个分支并行后忘了哪个是干净的;本地环境和线上的差异说不清;「这个 bug 我半年前修过一次」但完全不记得怎么修的。

熟悉吗?这份事故单同时也是 LLM agent 的失败清单:精确操作出错、重复操作漂移、长流程状态丢失。而工程界给 agent 的答案——工具调用、幂等脚本、外部状态存储——**你的行业早就发明了人类版,而且就装在你的电脑里**:类型检查、linter、CI、自动化测试、IaC、Git。问题从来不是缺工具,是 ADHD 程序员常见的双标:给生产系统配齐了所有护栏,自己的工作流却在裸奔。

## 把行业基建对准自己的短板

**精确类:让编译器和 linter 当你的「细心」**。ADHD 程序员应该是全组最激进的静态检查拥护者:严格模式、类型标注、pre-commit hook 全开——不是因为代码洁癖,是因为**每一层自动检查,都是一份不用消耗自己注意力的精确性**。配置类错误(你的重灾区)同理:schema 校验、配置也进版本控制、启动时 fail-fast。原则:凡是机器能查的,绝不留给下班前那双疲惫的眼睛。

**重复类:第二次就自动化**。通用建议是「三次法则」(重复三次再自动化),ADHD 版应该激进到两次——因为你的重复执行可靠性衰减比常人陡:第一遍新鲜,第二遍无聊,第三遍必跳步。部署脚本化、环境 Docker 化、常用操作进 Makefile/alias。写测试这种躲不掉的重复活,用刺激注入:TDD 的红绿循环本身就是即时反馈游戏,配上覆盖率数字当记分板——**把重复任务改造成有反馈回路的游戏,是对 ADHD 神经最诚实的贿赂**。

**状态维护类:让 Git 和文档当你的海马体**。你的天然优势:这个行业的状态外置文化是现成的,照抄即可——小步提交 + 认真写 commit message(给三个月后的自己写);每个 debug 超过一小时的问题,解决后强制五行记录(现象/原因/解法/坑/关键词),进个人 wiki——**「半年前修过但不记得」的每一次,都是当年欠下五行字的利息**;分支状态用「一个 WIP + 其余必须有 issue」的纪律管住。

## 一个反直觉建议:接一点「精确类」的班

有意思的转折:LLM coding 工具成熟后,ADHD 程序员的短板结构变了。AI 能接走大量重复类(样板代码、逐处修改)和部分精确类(拼写、格式)的活——但**验证 AI 产出**这个新任务,恰恰又是精确+状态维护类的(review 生成的代码、确认它没漂移)。所以新时代的自我配置是:生成和架构你来(优势区),样板和重复交给 AI,而**给「AI 产出的验证」建清单和流程**——别用裸眼 review 生成代码,那是把旧短板换了个地方裸奔:diff 工具、测试兜底、关键路径逐行,其余抽查。

## 边界

同构强度 A 级:双侧证据都硬(LLM 的精确性与长程一致性弱点有直接研究,ADHD 的执行功能文献扎实),且软件工程工具链对这三类任务的外部化几乎是逐条工程对应。照例声明:机制不等同,类比是功能层的;另外「测试欠账」若已是团队公开矛盾,流程改造之外,和 lead 聊一次工作分配(多拿架构、少拿流水)可能是更高杠杆的一步。

## 今天就能试的 3 件事

1. **把 pre-commit hook 配到最严**:lint + 类型 + 格式,今天配齐。让机器接管你最弱的那道工序。
2. **写下你的「二次自动化」清单**:上周手动做过两次以上的操作,列出来,挑一个今天脚本化。
3. **还今天的五行债**:今天解决的最难的问题,睡前五行记录进个人 wiki。给半年后的自己发工资。

这个行业花了七十年,把精确、重复、状态维护一件件从人手里拿走,交给机器——你入行的时候,武器库就是满的。把枪口调转十五度,对准自己的工作流:生产环境值得的待遇,你也值得。

## 参考来源

**同构强度：A 级** —— 直接文献支撑（引用 ADHD↔LLM 同构专题研究）

- [ADHD Apps: We tested 44 Apps and Here're the Best 9 in 2026](https://blog.saner.ai/best-adhd-apps/) — 证据等级：低（GRADE）
- [12 AI Personal Assistants Built for ADHD Brains (2026 Rankings)](https://www.usecarly.com/blog/best-ai-personal-assistant-adhd/) — 证据等级：低（GRADE）
- [LBD同构对：奖赏与动机 — Association of attention-deficit disorder and the dopamine t ↔ Retrospex: Language Agent Meets Offline Reinforcement Learni](https://pubmed.ncbi.nlm.nih.gov/7717410) — 证据等级：低（GRADE）
- [LBD同构对：分心与走神 — Therapeutic Doses of Oral Methylphenidate Significantly Incr ↔ AutoHallusion: Automatic Generation of Hallucination Benchma](https://doi.org/10.1523/jneurosci.21-02-j0001.2001) — 证据等级：低（GRADE）
- [LBD同构对：注意调度 — Dopamine release from the locus coeruleus to the dorsal hipp ↔ Question-guided Visual Compression with Memory Feedback for ](https://doi.org/10.1073/pnas.1616515114) — 证据等级：低（GRADE）
- ["A little bit of a life raft" – Exploring the Use and Experiences of ChatGPT as a Support Tool among Adults with ADHD](https://dl.acm.org/doi/pdf/10.1145/3764687.3764713) — 证据等级：低（GRADE）

---

*本文是「ADHD × AI」系列的第 8 篇，由 Devin 基于持续维护的双域研究语料（72,739 篇论文 + LLM Wiki）亲自撰写，并持续迭代更新。*
