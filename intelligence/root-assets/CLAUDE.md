# 400篇ADHD✖️AI滚动池 — 内容生产流水线

> Type: content-production | Status: active | Size: 5,724 items, 48 MB
> Last updated: 2026-06-25

## What This Is

ADHD × AI 主题的 400 篇长文内容滚动生产流水线。包含选题库、大纲模板、AI 生成脚本、发布排期、数据分析、自生长采集引擎和可视化系统。产出目标为公众号和知乎平台。

2026-06-25 升级：新增自生长引擎 `engines/self_growing_engine.py`（每日采集+评分+证据卡+替换候选），LLM-Wiki 知识库导出 `engines/build_llm_wiki_export.py`，Google ADK 入口，A2A Agent Card，以及 Windows 定时任务 `adhd-ai-daily-scout`（每天 08:05 运行）。详细部署说明见 `docs/SELF_GROWING_ENGINE_DEPLOYMENT.md`。

## Contents

| Category | Key Items |
|---|---|
| 选题与规划 | `ADHDxAI选题总台_2026-05-12.md`, `所有选题问句标题_持续更新.md`, `plan*.md`, `ROADMAP.md` |
| 内容生产 | `adhd_ai_intelligence_flow.py`, `adhd_ai_intelligence_system.py`, `变电器工作流_v1.0_多接口输出系统.md` |
| 自生长引擎 (NEW) | `engines/self_growing_engine.py` (每日采集+评分), `engines/build_llm_wiki_export.py` (知识库导出), `scripts/run-daily-scout.ps1`, `scripts/install-daily-scout.ps1` |
| 外部集成 (NEW) | Google ADK (`agents/adhd_ai_content_engine/agent.py`), A2A Agent Card (`.well-known/agent-card.json`), LLM-Wiki skill (`.agents/skills/llm-wiki/`) |
| 报告产出 | 全球AI博主情报蒸馏作战手册、双A博主深度洞见、ADHD全史终极考古报告、ADHDAIGC双A博主深层洞见 等 DOCX/MD |
| 可视化 | 8 张 PNG 分析图 (topic_evolution, sentiment_cycle, originality_analysis 等) |
| 发布管理 | `ADHDxAI_091-098_连续发布作战表_2026-05-12.md`, `ADHDxAI_问题001-100_MD总索引_2026-05-16.html` |
| 数据看板 | `400选题正文评分阅卷面板.html`, `指挥中心.html` |
| Git 同步 | `git-sync.ps1`, `git-sync.config.example.json` |
| 研究资料 | `research/` 目录, `content-packs/`, `sources/`, `research-inbox/` |
| 交付产物 | `delivery/`, `archive/`, `feedback/` |

## How to Use

```bash
# 自生长引擎 — 每日采集（已安装 Windows 定时任务 adhd-ai-daily-scout）
python engines/self_growing_engine.py --no-llm       # 本地评分
python engines/self_growing_engine.py --dry-run       # 预览不写文件
python engines/self_growing_engine.py                 # 启用 LLM 分析（需 API key）

# LLM-Wiki 知识库导出
python engines/build_llm_wiki_export.py

# Google ADK agent 入口
adk run agents/adhd_ai_content_engine

# 内容生产管线 (Python)
python adhd_ai_intelligence_flow.py
python adhd_ai_intelligence_system.py

# Git 同步 (PowerShell)
.\git-sync.ps1

# 每日任务管理
powershell.exe -NoProfile -ExecutionPolicy Bypass -File .\scripts\install-daily-scout.ps1   # 安装/更新定时任务
Get-ScheduledTask -TaskName adhd-ai-daily-scout                                               # 查看任务状态

# 查看选题总台和阅卷面板 (浏览器打开 HTML)
```

## Key Entry Documents

- `PROJECT_STATUS.md` — 当前项目状态
- `PROJECT_AUDIT.md` — 审计记录
- `ROADMAP.md` — 路线图
- `NEXT_ACTIONS.md` — 下一步行动
- `CONTENT_PIPELINE.md` — 内容管线说明
- `CONTRIBUTING.md` — 贡献指南
- `README.md` — 项目总览
- `docs/SELF_GROWING_ENGINE_DEPLOYMENT.md` — **自生长引擎部署说明 (NEW)**

## Research

- `research/2026-06-24_ADHD×AI_深度研究报告.md` — deep-research 产出：AI 诊断/数字疗法/LLM 辅助/可穿戴监测 4 维度，31 源 → 149 声明 → 25 对抗验证 → 4 条存活

## Related Projects

| Relationship | Project | How |
|---|---|---|
| Publishing target | 知乎问题自动发布器 (`C:\项目库\知乎问题自动发布器\`) | 知乎内容发布 |
| Publishing target | WeChat-Article-Exporter-Repo | 公众号文章导出参考 |
| Research tool | deep-research skill | 深度研究报告生成 |
