# 自生长内容引擎部署说明

更新时间：2026-06-25

## 一句话判断

本项目现在拥有一个可运行的“自生长运行层”：每天采集 ADHD × AI / Agentic AI 新素材，写入 `research-inbox/`，生成 evidence cards、替换候选、S+ 升级提示，并同步导出到 LLM-Wiki 风格知识库。它默认**不自动替换正文**，避免把 400 个内容包静默污染。

## 已接入的外部机制

| 外部项目 / 标准 | 本项目采用方式 |
|---|---|
| LLM-Wiki / Karpathy LLM Wiki pattern | 建立 `knowledge/raw/sources` + `knowledge/wiki` + `knowledge/index.md` + `knowledge/log.md`，让 400 包和每日证据可导入 LLM-Wiki 桌面 App |
| nashsu/llm_wiki desktop | 已安装 Windows 桌面应用；项目内也安装了 `.agents/skills/llm-wiki` skill |
| Google ADK 2.x | 已安装 `google-adk`；新增 `agents/adhd_ai_content_engine/agent.py` 作为轻量 ADK 入口 |
| Google / Linux Foundation A2A Agent Card | 新增 `.well-known/agent-card.json`，描述本内容引擎的能力、技能和本地接口 |
| A2A SDK | 已安装 `a2a-sdk`，后续可把本地 CLI 升级成 A2A server |

## 新增文件

| 文件 | 作用 |
|---|---|
| `config/self_growing_engine.config.json` | 采集源、评分阈值、LLM 模型、LLM-Wiki 导出路径 |
| `engines/self_growing_engine.py` | 每日采集 + 评分 + evidence cards + 候选记录主引擎 |
| `engines/build_llm_wiki_export.py` | 把 400 个 content packs 导出为 LLM-Wiki seed pages |
| `scripts/run-daily-scout.ps1` | Windows 定时任务实际调用的 runner，写日志到 `logs/` |
| `scripts/install-daily-scout.ps1` | 安装 Windows Task Scheduler 任务 `adhd-ai-daily-scout` |
| `.well-known/agent-card.json` | A2A Agent Card / agent discovery 描述文件 |
| `agents/adhd_ai_content_engine/agent.py` | Google ADK 入口 agent |
| `knowledge/` | LLM-Wiki 风格知识库导出目录 |

## 日常运行

### 手动试跑，不写文件

```bash
python engines/self_growing_engine.py --dry-run --no-llm
```

### 手动运行并写入 research-inbox / knowledge

```bash
python engines/self_growing_engine.py --no-llm
```

如果配置了 API Key，可以去掉 `--no-llm`，引擎会自动尝试：

1. `ANTHROPIC_API_KEY` → Anthropic API
2. `GOOGLE_API_KEY` → Gemini / Google GenAI
3. 都没有 → 本地规则评分

### 重建 LLM-Wiki seed pages

```bash
python engines/build_llm_wiki_export.py
```

输出：

- `knowledge/wiki/topics/问题001.md` 到 `问题400.md`
- `knowledge/wiki/topics/topic-index.md`
- `knowledge/raw/sources/content-packs/400-content-packs.snapshot.json`

## 当前运行策略（2026-07-15）

原 `adhd-ai-daily-scout` 计划任务已退役。历史任务从未完整成功，且旧 runner 会在无人审核时调用 evidence injector 改写内容包注入区块。

当前 runner 已改成**只采集、只生成审核报告、不写 `content-packs/`**。默认使用人工入口：

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File .\scripts\run-daily-scout.ps1 -NoLlm
```

该入口仍会联网采集并更新 `research-inbox/`、`knowledge/` 和 `logs/`；`-NoLlm` 可避免 API 调用与费用。运行后必须检查：

```powershell
git status --short -- content-packs
```

结果应为空。只有人工审核证据后，才允许单独运行 `evidence_injector.py` 的写入模式。

## 重新启用每日任务（默认禁止）

安装器现在要求显式传入 `-EnableUnattended`，避免误恢复已退役的自动化：

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File .\scripts\install-daily-scout.ps1 -EnableUnattended
```

仅当 API 成本、网络超时和输出审核机制都重新验收后才应使用。默认每天 08:05；如需安装后立即运行：

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File .\scripts\install-daily-scout.ps1 -EnableUnattended -RunNow
```

查看任务：

```powershell
Get-ScheduledTask -TaskName adhd-ai-daily-scout
```

日志：

```text
logs/daily-scout-YYYY-MM-DD_HHMMSS.log
```

## LLM-Wiki 使用方式

LLM-Wiki 桌面应用已安装在：

```text
C:\Users\34587\AppData\Local\LLM Wiki\llm-wiki.exe
```

桌面快捷方式：

```text
C:\Users\34587\Desktop\LLM Wiki.lnk
```

推荐操作：

1. 打开 LLM Wiki。
2. 新建项目，源目录选择本项目的 `knowledge/` 或 `knowledge/raw/sources/`。
3. 在 LLM Wiki 设置里启用 API Server。
4. 如需 Claude Code 查询该知识库，生成 token 并设置 `LLM_WIKI_API_TOKEN`。

已安装 skill：

```text
.agents/skills/llm-wiki/
```

## 非破坏性边界

引擎会写入：

- `research-inbox/daily-scout/YYYY-MM-DD.md`
- `research-inbox/source-ledger.md`
- `research-inbox/evidence-cards.md`
- `research-inbox/replacement-candidates.md`
- `research-inbox/s-plus-upgrade-board.md`
- `knowledge/**`
- `logs/**`

引擎不会自动修改：

- `content-packs/问题NNN/01_正文.md`
- `content-packs/问题NNN/meta.json`
- `indexes/400*.md`
- `feedback/` 真实回流表

真正替换旧题必须另走人工确认流程：备份旧包到 `archive/topic-replacements/YYYY-MM-DD/问题NNN/`，重写 9 个资产文件，更新 `meta.json`、索引和 `replacement-log.md`。

## 评分口径

每条新素材按 5 个维度打分，每项 1-5：

1. 痛感强度
2. ADHD × AI 交叉度
3. 证据强度
4. 产品化入口潜力
5. 回流潜力

阈值：

| 分数 | 处理 |
|---:|---|
| 14+ | evidence enrich |
| 22+ | replacement-or-S-upgrade candidate |
| 25 | S+ upgrade candidate |

## 当前仍需人工完成

1. 配置真实 API Key：`ANTHROPIC_API_KEY` 或 `GOOGLE_API_KEY`。
2. 打开 LLM-Wiki 桌面 App 并导入 `knowledge/`。
3. 发布至少 5-10 篇 S/A 级文章，回填真实 48 小时数据。
4. 根据真实回流决定是否执行第一次替换。

## 外部参考

- [nashsu/llm_wiki](https://github.com/nashsu/llm_wiki)
- [nashsu/llm_wiki_skill](https://github.com/nashsu/llm_wiki_skill)
- [google/adk-python](https://github.com/google/adk-python)
- [a2aproject/A2A](https://github.com/a2aproject/A2A)
- [Agent Discovery / Agent Card 说明](https://deepwiki.com/google/A2A/1.2-agent-discovery)
