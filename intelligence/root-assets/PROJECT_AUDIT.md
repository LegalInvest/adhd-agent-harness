# PROJECT_AUDIT

审计时间：2026-05-22

## What was scanned

本轮按 `folder-to-project` 对 `C:\Users\34587\Desktop\选题池\草稿` 做“深度整理但不破坏正文路径”的复扫。

扫描覆盖：

- 根目录 `问题*.md` 正文资产
- 项目入口：`README.md`、`PROJECT_STATUS.md`、`PROJECT_AUDIT.md`、`AGENT_BRIEF.md`
- 交付区：`delivery/`
- 研究资料：`sources/`
- 归档区：`archive/legacy/`
- 模板与看板：`docs/templates/`、`docs/topic-pools/`
- 网站预留：`site/README.md`
- 根目录压缩包：`ADHD选题合集.zip`

## Classification result

| 项目角色 | 当前路径 | 说明 |
|---|---|---|
| Active content | 根目录 `问题*.md` | 正文主资产（当前口径到 001-262） |
| Master index | `indexes/`、主索引文件 | 总索引与导航入口 |
| Topic pools | `docs/topic-pools/` | 选题池、增量池、看板 |
| Templates | `docs/templates/` | 发布包与产品化模板 |
| Sources | `sources/` | 原始研究资料与中间产物 |
| Outputs/delivery | `delivery/`、`outputs/` | 渲染 HTML、质检、发布包 |
| Archive/legacy | `archive/legacy/` | 历史版本与旧草稿 |
| Website readiness | `site/README.md`、`docs/publishing-plan.md` | 站点信息架构与发布计划 |
| Quarantine candidate | `ADHD选题合集.zip` | 需确认是否为历史打包产物 |

## Files moved / renamed / archived

本轮未做破坏性移动或删除。

原因：当前正文、索引、渲染、质检之间存在大量隐式引用，先保持稳定结构，再逐轮做安全迁移。

## Files updated in this run

- `PROJECT_AUDIT.md`（本文件）
- `AGENT_BRIEF.md`（下一步动作与目录口径同步）

## Files left untouched and why

- 根目录 `问题*.md`：保留原路径，防止断链。
- `delivery/`：保留现有交付与质检。
- `sources/`：保留原始证据与中间研究文件。
- `archive/legacy/`：保留历史资产，不二次清理。

## Unclear files / future review

- `ADHD选题合集.zip`：建议确认用途后放入 `archive/legacy/packages/`。
- `docs/topic-pools/ADHDxAI_选题升级看板_001-220.html`：与 001-262 口径不一致，需升级。

## Suggested future cleanup

1. 建立 `archive/legacy/packages/`，归档历史 zip（先确认用途）。
2. 生成 `data/articles-001-262.json` 与 `data/topic-board-001-262.csv`。
3. 升级全量看板到 001-262 口径。
4. 保持“每新增 1 选题，完成 2 个旧资产闭环动作”。

## Safety note

本轮未永久删除任何文件。