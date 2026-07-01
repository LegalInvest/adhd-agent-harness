# ADHD 大脑与 LLM 的同构

## ADHD 一侧

ADHD大脑的核心特征是高产但无序的生成能力，同时缺乏可靠的执行调度层。执行功能（如工作记忆、任务启动、时间管理）常出现故障，导致“想法很多，行动困难”。因此，ADHD个体需要外部工具来“减少决策、保留上下文、让下一步行动显而易见”（来源：Best AI Tools for ADHD Productivity in 2026 (Honest Review) - Iwo Szapar）。例如，AI助手被用来“在自身工作记忆丢失时携带上下文”（来源同上），并充当“AI第二大脑”来记住项目上下文（来源同上）。

## LLM/harness 一侧

LLM本身是强大的生成核心，但缺乏可靠的内置调度与执行控制。因此，在构建AI agent时，需要“agent harness”——即“包裹LLM或AI agent的软件基础设施，处理模型本身之外的一切”（来源：What is an agent harness in the context of large-language models?）。这种架构常采用“复合AI系统”（来源：Building AI Coding Agents for the Terminal: Scaffolding, Harness, Context Engineering, and Lessons Learned），通过“每个工作流可绑定不同LLM”的架构（来源同上）来分配任务，并依赖“模型连接器”等组件（来源：Worker Agents | Harness Developer Hub）来管理外部工具和上下文。

## 同构对应

| ADHD大脑 | LLM + Harness |
|----------|---------------|
| 高产但缺乏执行调度层的生成核心 | 高生成能力但需外部调度的LLM |
| 工作记忆易丢失上下文 | LLM无状态，需外部记忆管理 |
| 需要AI助手减少决策、保留上下文 | Harness负责上下文工程和决策路由 |
| 外部工具（如Goblin Tools）作为执行功能支架 | Harness中的模型连接器、工具调用等 |
| 多巴胺驱动任务启动困难 | 缺乏内在奖励机制，需外部提示 |

## 工程启示（可迁移的做法）

1. **上下文保护**：ADHD工具应像harness一样主动保存和恢复上下文，避免工作记忆丢失。
2. **决策减负**：设计明确的下一步行动提示，类似harness中的工作流编排。
3. **外部记忆**：利用“AI第二大脑”等工具作为外部工作记忆，对应harness中的上下文存储。
4. **模块化架构**：为不同任务绑定不同工具/策略，类似per-workflow LLM绑定。

## 类比的边界与反例

> ⚠️ 矛盾：ADHD大脑的“生成核心”包含情感、多巴胺等生物因素，而LLM无情感；ADHD的执行功能缺陷是神经性的，而harness是人为设计的软件。类比在生物与工程之间失效。

此外，ADHD个体可能需要个性化适应，而harness通常追求通用性。

## 来源

- Best AI Tools for ADHD Productivity in 2026 (Honest Review) - Iwo Szapar
- Building AI Coding Agents for the Terminal: Scaffolding, Harness, Context Engineering, and Lessons Learned
- Worker Agents | Harness Developer Hub
- What is an agent harness in the context of large-language models? | Parallel Web Systems
