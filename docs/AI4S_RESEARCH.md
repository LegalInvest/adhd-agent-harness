# AI4S / LLM Wiki 调研与应用映射（研究过程文档）

> 最后更新：2026-07-28。本文档记录「科研自动化（AI for Science）与 LLM Wiki 领域的想法灵感」调研结论，
> 以及每条想法在本项目（ADHD 人生 Harness 研究系统）中的落地映射与实施状态。
> 任何云端 Agent 接续开发前应读本文档 + `HANDOFF.md` + `docs/METHODOLOGY.md`。

## 一、调研范围

对象：GitHub 高星项目与公开论文/产品中已验证的科研自动化机制。核心样本：

| 项目/系统 | 核心机制 | 对本项目的启发 |
|---|---|---|
| SakanaAI **AI-Scientist** (v1/v2) | 全自动闭环：想法生成 → 实验 → 写作 → 自动同行评审（reviewer agent 用评分 rubric 打回重写） | **发布前评审门**：文章在发布前必须过一遍 rubric 化审稿 |
| Stanford **STORM / Co-STORM** | 多视角提问 → 检索 → 大纲 → 成文（本项目已用 STORM questions） | 已落地（`engine/storm.py`）；可扩展 Co-STORM 的「圆桌多 agent 对话」挖 L4/L5 |
| FutureHouse **PaperQA2** | claim 级引用问答；每个论断都有可核查出处；**矛盾检测**（同一问题上文献互相打架时显式呈现） | **争议雷达**：ADHD 文献中大量结论互相矛盾（药物长期效应、脑训练、饮食干预），诚实呈现矛盾比装作有定论更可信 |
| FutureHouse **WikiCrow** | 从文献自动生成/维护概念 wiki 页（每个基因一页），持续更新 | 本项目 wiki 模式（`engine/knowledge.py` + `data/wiki/`）同源；可按脊柱概念持续维护 |
| **gpt-researcher** | planner-executor 深度研究 agent：计划 → 并行检索 → 汇总带引用报告 | 每周滚动 Automation 的「增量抓取+汇总」形态 |
| Google **AI co-scientist** (2025) | generate-debate-evolve：假设生成 → 锦标赛式两两辩论排名（Elo）→ 胜者进化 | **选题锦标赛**：L4/L5 新选题不只靠加权分，可用两两辩论淘汰赛选出真正有洞见的 |
| **SciAgents** (MIT) | 本体知识图 + 多 agent 协作生成研究假设，随机路径采样发现远距离概念连接 | 与本项目 GraphRAG + LBD 同构；可加「图上随机游走采样远端概念对」增强 LBD |
| **Scite.ai** | 引用分类：supporting / contrasting / mentioning | 参考来源不只列出处，还标注「支持/反驳」方向 |
| **Elicit / Consensus** | 结构化证据抽取（PICO、效应量、样本量）+ 证据综合 | GRADE 分级（已有）之上可抽样本量/效应方向，喂给争议雷达 |
| Living systematic review（活体综述） | 综述不是一次性的，新证据进来自动更新结论与置信度 | 滚动机制天然适配：每轮增量抓取后重跑争议雷达与 wiki 更新 |

## 二、应用映射（按价值排序）

### 已实施（本 PR）

1. **发布前评审门 `engine/review.py`**（源自 AI-Scientist 的 reviewer agent + 本项目方法论质量清单）
   - 无 API 依赖的启发式硬检查：中文正文字数、五型问题结构信号、医疗内容专业边界声明、
     未支持数字检测、类比字面等同红线、frontmatter 完整性、双目录一致。
   - 可选 LLM rubric 审稿（走 `engine/llm.py`，Kimi→DeepSeek 降级）：五型完整度/开头独特性/边界纪律打分。
   - CLI：`python -m engine.review`（全量体检，输出 `data/review_report.json`）；
     `python -m engine.review data/articles/<id>.md`（单篇）。
   - 用法约定：**每批新文章合并前必须跑一遍，FAIL 项修完才能发**。

2. **证据争议雷达 `engine/contradictions.py`**（源自 PaperQA2 矛盾检测 + Scite 引用方向 + 活体综述）
   - 在 72,739 篇语料上按主题（药物长期效应、脑训练、饮食、运动、正念、数字干预等）扫描摘要，
     用方向词极性（有效/无效/增加/降低/无差异）把研究分到「支持/反驳/中性」三桶。
   - 输出 `data/contradictions.json` + 人类可读的 `docs/CONTRADICTION_MAP.md`（争议地图）。
   - 价值：① 给写作供弹药（每个争议都是一篇「验证式问题」文章的天然选题）；② 防止文章把有争议的结论写成定论；
     ③ 滚动时增量更新 = 活体综述。

### 首轮体检结果（评审门在全量 400 篇上的发现，接续 Agent 的现成待办）

- FAIL 57 篇：55 篇涉及医疗/危机词但未检出专业边界声明、3 篇疑似类比字面等同（详见 `data/review_report.json`；
  启发式存在误报可能，需逐篇人工确认后修复）。
- WARN 335 篇：多为五型结构信号不全或字数低于 1800 目标（早期批次），可随后续批次滚动加厚。

### 待实施（按优先级，接续的 Agent 从这里继续）

3. **选题锦标赛 `engine/tournament.py`**（AI co-scientist 的 generate-debate-evolve）
   - 对 L4/L5 候选选题做两两 LLM 辩论（谁更能帮 ADHD 者自我和解/找到价值），Elo 排名，胜者保留败者淘汰。
   - 建议与 L4/L5 定向挖掘一起做：LBD 远端概念对 → 生成候选 → 锦标赛 → 胜者入池竞争 Top 400。
4. **引用方向标注**（Scite 式）：文章参考来源在 GRADE 等级之外加「支持本文观点/呈现相反证据」标签，争议雷达的数据可直接复用。
5. **GraphRAG 随机游走 LBD 增强**（SciAgents）：在 concept_graph 上采样远距离路径生成新同构假设。
6. **Co-STORM 圆桌**：多角色（ADHD 当事人/临床研究者/AI 工程师/怀疑论者）对话式挖掘 L4/L5 选题。

## 三、与北极星的关系

所有机制服务于：帮 ADHD 者获得幸福、成长、自我和解与人生价值。
- 评审门保证「每篇内容真的解决一个问题、不越医疗边界、不制造虚假确定性」；
- 争议雷达保证「诚实面对证据的不确定性」——对被伪科学和营销话术包围的 ADHD 人群，诚实本身就是稀缺价值；
- 锦标赛/圆桌用于把内容金字塔最稀薄的 L4/L5（叙事层/价值层）补厚。
