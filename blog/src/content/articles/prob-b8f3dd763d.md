---
title: "用 ChatGPT 给 ADHD 补上幻觉与验证循环，真的能像 agent 那样工作吗？"
subtitle: "把 ChatGPT 当作 ADHD 的外部执行层来实测：它补的是哪一块短板？"
description: "把 ChatGPT 当作 ADHD 的外部执行层来实测：它补的是哪一块短板？"
date: "2025-05-16"
category: "科学研究"
categoryId: "science"
categoryEn: "Scientific Research"
tags:
  - "ADHD"
  - "AI"
  - "科学研究"
  - "工具×同构"
  - "研究"
readingTime: 13
slug: "用-chatgpt-给-adhd-补上幻觉与验证循环真的能像-agent-那样工作吗"
topicId: "prob-b8f3dd763d"
angle: "工具×同构"
rank: 210
score: 7.51
sourceCount: 5
toolsCited:
  - "Goblin Tools"
  - "Saner.AI"
  - "Motion"
  - "Tiimo"
problem: "用 ChatGPT 给 ADHD 补上幻觉与验证循环，真的能像 agent 那样工作吗？"
spine: "幻觉与验证循环"
spineKind: "llm"
isEvolved: false
llmGenerated: false
---

# 用 ChatGPT 给 ADHD 补上幻觉与验证循环，真的能像 agent 那样工作吗？

> 读完一篇讲 agent 架构的文章,她兴奋地给自己设计了一套「人肉 agent 系统」:每个任务前让 ChatGPT 做计划验证,执行中让它做步骤检查,完成后让它做结果复盘——完美复刻 plan-verify-execute-review 循环。第一周,系统运转如论文般优美。第三周,系统只剩下一个环节还活着:任务前的计划验证——因为那个环节有新鲜感。执行中检查?她根本想不起来。事后复盘?任务做完的那一刻她的注意力已经在三公里外。她盯着自己烂尾的「架构图」苦笑:**agent 的循环之所以能转,是因为有代码在转它——而我这里,谁来转我?**

收敛:上一篇回答了「该不该用」(脚手架 vs 拐杖),这一篇回答工程可行性——**人肉复刻 agent 验证循环,断点到底在哪?哪些环节人真的能跑,哪些必须换成别的东西?**

## 穿透:循环的每一环都能跑,唯独「循环」本身跑不了

把 agent 验证循环拆开看,人肉复刻的断点立刻显形。agent 的循环里有四种东西:**计划(plan)、验证(verify)、执行(execute)、复盘(review)**——这四个环节 ChatGPT 都能辅助人完成,单环质量甚至不差。但 agent 还有第五种东西,藏在代码里、不出现在架构图上:**调用器(the loop itself)**——是它保证「执行完必然触发复盘」「验证完必然进入执行」。**agent 从不需要「记得」进入下一环,而人肉系统里,每一次环节转换都依赖前瞻记忆——恰好是 ADHD 最深的坑。**她的系统不是设计错了,是把「循环会自己转」当成了免费的默认,而那恰恰是最贵的组件。

所以正确的问题不是「怎么更自律地转循环」,是**「用什么替代代码来当调用器」**。可用的替代品按可靠性排序:①**日历/闹钟(时间触发)**——复盘不靠「做完后记得」,靠每天固定的 17:30 闹钟(「今天做完的事,过一遍」);②**物理锚点(空间触发)**——执行中检查绑定到已有习惯上(每次起身倒水=顺手看一眼「我还在原任务上吗」);③**他人(社会触发)**——每周和一个伙伴互相问一次「上周的循环转了几圈」;④最后才是意志力——它只配当兜底,不配当架构。

第二个断点同样致命:**环节的成本不对称。**对 agent,四环成本相同;对 ADHD,计划环有新鲜感红利(所以她的系统只有这环活着),执行中检查要打断心流(高成本),复盘发生在多巴胺已经离场的时刻(最高成本)。工程含义:**人肉系统必须按人的成本曲线降级设计**——复盘从「深度总结」降到「三个勾选框」(完成了吗/卡在哪/明天第一步),执行检查从「每小时」降到「每次自然中断时」。**循环能转的秘诀不是环节精美,是每一环便宜到状态最差的那天也跑得动。**

利益视角:「人人都能是自己的 agent」是效率内容的新叙事,它卖的是架构图的美感;没人告诉你 agent 架构图里最重要的组件是不可见的——因为承认这一点,课程就不好卖了。

## 验证

改造后的系统四周可测:调用器全部外置(闹钟+锚点+伙伴)、环节全部降级(勾选框级),跟踪「循环完整转过的次数」——不是环节质量,是圈数。圈数才是系统活着的证据。可证伪:若外置调用器+降级环节后圈数依然为零,问题不在架构而在任务本身(全是回避型任务)或状态层(睡眠/情绪先崩了)——先修地基,循环是地基之上的东西。

## 决策

做什么:承认「循环本身」是需要采购的组件,用时间/空间/社会触发器把它焊死;所有环节按「最差状态可运行」标准降级;每周只看一个指标:圈数。

不做什么:不要照抄 agent 架构图搭人肉系统(你不是在跑代码,你在跑一个有成本曲线的神经系统);不要在系统烂尾时升级它的复杂度(烂尾的原因几乎永远是太贵,不是太简陋)。

先做什么:给「复盘」设一个每天固定时间的闹钟,内容降到三个勾选框——今天 17:30,转你的第一圈。

## 边界

「验证循环↔人肉流程」为 B 级架构类比,且本文的核心恰恰是指出类比的断点(调用器不可复刻);前瞻记忆困难有 ADHD 文献支持(本文未做正式 A/B/C 分级)。若连最简系统也持续无法启动且伴随显著痛苦,请考虑专业评估——有时候该修的不是流程,是流程下面的人的状态。

## 今天就能试的 3 件事

1. 给你现有的(或烂尾的)自我管理系统做一次「调用器审计」:每个环节转换,靠什么触发?凡是答案为「靠我记得」的,今天换成闹钟或锚点。
2. 把复盘降级为三个勾选框,设 17:30 闹钟——圈数从今天开始计。
3. 招募一个「循环伙伴」:每周日互发一条消息,只问一句——这周转了几圈?

本文服务于人生 Harness 金字塔的**执行层**:agent 和你的差距从来不在智能,在那行看不见的 while True——你造不出它,但你可以用闹钟、门把手和一个朋友,把它一段一段焊出来。

## 参考来源

- [Large Language Models as simulative agents for neurodivergent adult psychometric profiles](https://www.arxiv.org/pdf/2601.15319) — 证据等级：低（GRADE）
- [Algorithmic Classification of Psychiatric Disorder-Related Spontaneous Communication Using LLM Embeddings](https://pubmed.ncbi.nlm.nih.gov/40605829/) — 证据等级：低（GRADE）
- ["A little bit of a life raft" – Exploring the Use and Experiences of ChatGPT as a Support Tool among Adults with ADHD](https://dl.acm.org/doi/pdf/10.1145/3764687.3764713) — 证据等级：低（GRADE）
- [Comorbidity of LD and ADHD](https://doi.org/10.1177/0022219412464351) — 证据等级：低（GRADE）
- [YOUNG ADULTS WITH ATTENTION DEFICIT HYPERACTIVITY DISORDER: SUBTYPE DIFFERENCES IN COMORBIDITY, EDUCATIONAL, AND CLINICAL HISTORY](https://doi.org/10.1097/00005053-200203000-00003) — 证据等级：低（GRADE）

---

*本文是「ADHD × AI」系列的第 74 篇，由 Devin 基于持续维护的双域研究语料（72,739 篇论文 + LLM Wiki）亲自撰写，并持续迭代更新。*
