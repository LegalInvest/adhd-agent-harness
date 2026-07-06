# AGENT_BRIEF

## 2026-07-03 handoff entry

如果你是新接手的 Agent，先读根目录 `HANDOFF_FOR_NEXT_AGENT.md`，再读 `handoff/00_README_NEXT_AGENT.md` 到 `handoff/05_DEVELOPMENT_TASKS_FOR_NEXT_AGENT.md`。这些文件是最新交接包，优先级高于本文件中较早的阶段性说明。

## Project one-liner

这是《问题XXX》ADHD × AI 内容与产品化项目：目标是把高方差大脑的真实痛感、AI/Agent 外部执行系统、正文资产、发布包、评论回流和模板入口，组织成 400 个可持续发布、可网站化、可产品化的闭环资产包。

## Current structure

- `content-packs/问题001` 到 `content-packs/问题400`：当前主工作区，每个编号一个闭环资产包。
- 每个资产包固定 9 个文件：`01_正文.md`、`02_发布包.md`、`03_小红书版.md`、`04_知乎版.md`、`05_短视频口播.md`、`06_评论回流问题.md`、`07_48小时回流表.md`、`08_模板入口.md`、`meta.json`。
- `indexes/400闭环资产总索引.md`：400 包总状态。
- `indexes/400缺口清单.md`：正文缺口，当前为 0。
- `indexes/400发布排期表.md`：按 S/A/B/D 优先级排列的发布与回流队列。
- `archive/loose-files-before-cleanup/root-drafts/`：已迁移的根目录旧正文。
- `archive/cleanup-2026-06-03-generator-attempts/`：已归档的旧生成器、bat 和日志。
- `docs/topic-pools/`：历史选题池与新增编号来源。
- `docs/templates/`、`docs/workflows/`、`delivery/`、`feedback/`：旧资产与辅助工作区，后续应按需并入包内。

## Core files to read first

1. `PROJECT_STATUS.md`
2. `README.md`
3. `docs/400闭环资产包最终目录规范.md`
4. `docs/400闭环资产包补齐执行队列.md`
5. `indexes/400闭环资产总索引.md`
6. `indexes/400缺口清单.md`
7. `indexes/400发布排期表.md`

## Do not touch

未经用户明确同意，不要：

- 永久删除任何文件。
- 删除 `sources/` 原始资料。
- 删除或覆盖 `delivery/` 既有渲染与质检输出。
- 清理 `archive/legacy/` 历史资产。
- 把已归档的根目录旧正文再搬回根目录作为主入口。
- 用待填 `07_48小时回流表.md` 冒充真实发布反馈。

## Safe-to-edit areas

可以安全编辑或新增：

- `content-packs/问题NNN/` 内的 9 个标准资产文件。
- `meta.json` 的状态字段。
- `indexes/400闭环资产总索引.md`。
- `indexes/400缺口清单.md`。
- `indexes/400发布排期表.md`。
- `PROJECT_STATUS.md`、`PROJECT_AUDIT.md`、`AGENT_BRIEF.md`。
- `docs/400闭环资产包最终目录规范.md`、`docs/400闭环资产包补齐执行队列.md`。

## Self-growing rule

总量锁定 400。新素材、新选题、新研究不得直接扩成 401；必须先进入 `research-inbox/`，再按痛感强度、ADHD × AI 交叉度、证据强度、产品化潜力、回流潜力评分。强候选只能替换弱题，替换必须归档旧包并记录到 `research-inbox/replacement-log.md`。

每日自动采集任务：`adhd-ai-daily-scout`，每天 08:05 运行，用于联网检索 ADHD × AI / Agentic AI 新材料并沉淀 evidence cards、replacement candidates 和 S+ upgrade board。

## Next single action

下一步唯一动作：进入“真实欲望校准”工作流。先不要继续按 27/27 点火分发布；优先审计并重写高风险失真选题，尤其是 `ai_interface`、`attention`、`org`、`money`、`self` 中复用类型模板的题。每次重写都要先问：读者最想扔掉哪种痛？哪些痛点希望被 AI/Agent/外部系统直接接走？

## If continuing development, start here

硬规则先执行：

- 默认不以“新增选题数”衡量进度，只以“已闭环资产包数”和“真实回流数”衡量进度。
- 一个闭环资产包必须同时具备正文、发布包、小红书版、知乎版、短视频口播、评论回流问题、48 小时回流表、模板入口和同步后的 `meta.json`。
- 每次真实发布后，都更新 `07_48小时回流表.md` 与三个 400 索引。
- 每次想开新题前，先发布并回流一个旧包。
- 风格必须是严肃随笔，不要营销号。
- ADHD × AI / Agentic AI 交叉点必须清楚。
- ADHD 真实欲望优先于理论正确：先承认免痛、代偿、外包、自动恢复的欲望，再谈风险、兜底和验收。
- Agentic AI 题不要默认“害怕委托”。高痛感 ADHD 读者更可能想把启动、排序、记忆、催办、沟通、收尾、复盘全部交出去；真正的问题是系统是否可信、可验收、失败可恢复。

## Quality baseline

400 篇正文已完成质量审计与批量补强。自动审计结果：400/400 达到基础质量线，最低分 85，平均分 89.2。接手时优先参考 `docs/400正文质量审计与升级报告.md`。

## Ignition rewrite baseline

400 篇正文已完成结构性“点火改写”升级。每个 `content-packs/问题NNN/01_正文.md` 顶部都有 `点火改写：所欲、所思、所行`、`点火开场：发布版第一屏`、`三维度电流评分表`。`meta.json` 已写入 `ignition_rewritten=true` 与 `current_scores`。

重要校正：当前点火分只能说明结构完成，不能等同于真实欲望命中。此前大量触动内容由类型模板生成，尤其 `ai_interface` 容易把“巴不得所有痛点外包出去”的 ADHD 真实欲望误写成“害怕委托/保留判断权”；`attention` 容易把“想让系统替我挡掉注意力掠夺”误写成“我要夺回注意力”；`money/org/self` 也有创业者视角、组织咨询语和泛共鸣过强的问题。后续发布前必须先做“真实欲望校准”。

点火指数倒序总表：`indexes/400点火指数倒序总表.md`。真实欲望审计表：`indexes/400真实欲望失真审计表.md`。真实欲望校准后电流倒序总表：`indexes/400真实欲望校准后电流倒序总表.md`。接手时如果用户要“最强/最先发/倒序”，优先看真实欲望校准后总表，不要只看旧分数。
