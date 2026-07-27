# HANDOFF — 交接文档（给任何接手的人或 AI Agent）

> **最后更新：2026-07-27**
> 如果你是新接手的云端 Agent 或者不记得上下文的项目所有者：**从这份文档开始读，然后读 `docs/METHODOLOGY.md`（项目宪法）和 `README.md`。**

## 0. 项目所有者须知

项目所有者是 ADHD 人士，可能不记得之前的开发历史。任何 Agent 接手时必须：
1. 主动、完整、简明地汇报项目现状，不要假设对方记得任何上下文；
2. 所有成果必须落到 GitHub（不能只留在本地或会话里）；
3. 每次工作结束前更新本文档的「当前状态」和「下一步」。

## 1. 这个项目是什么（北极星）

**深入研究 ADHD，找到「人生 Harness 系统」的方法论，助力 ADHD 者获得幸福、成长、自我和解，找到人生价值。**

- 不是单纯的博客/SEO 站/工具评测站。论文数据库、评分器、博客、发布资产都是手段，终点是人。
- 人生 Harness 五层金字塔：状态层（供电）→ 执行层（外部执行功能）→ 关系层（社会性基础设施）→ 叙事层（自我和解）→ 价值层（人生方向）。
- 每篇内容只解决一个问题，正文按五型问题推进：收敛 → 穿透 → 验证 → 决策 → 落地。
- 完整规范：**`docs/METHODOLOGY.md`**（必读）。

## 2. 当前状态（截至 2026-07-27）

- **全站 400 篇文章均为亲笔重写版**（llmGenerated: false），按五型问题骨架，每篇约 1800–2500 字。
- 研究资产：72,739 篇双域论文语料、13 个同构脊柱概念、LBD/突发概念/GRADE/STORM/GraphRAG 五件套、100 历史案例、442 画像、publishing/ 发布资产包、intelligence/ 研究资产。
- 评分引擎（`engine/scorer.py`）：8 维加权（证据 0.22 / 同构 0.20 / SEO 0.12 / 跨平台 0.11 / 实用 0.11 / attention 0.10 / 情感 0.07 / 分享 0.07）+ 成长 marker 加权 + 标题模板族去同质化惩罚。
- 留存机制：全量选题池（~2400+ 条）永不删除；Top 400 是发布切片；下架文章正文归档 `data/archive/`，重新上榜自动复用；每轮变动记录在 `data/rolling_log.json`。
- LLM 供应商：Kimi（配额已耗尽）→ DeepSeek fallback（`engine/llm.py`）。**新晋文章优先由 Agent 亲笔写，DeepSeek 只作兜底。**

## 3. 部署（push 即自动更新，无需手动操作）

push 到 main 后 `.github/workflows/deploy.yml` 自动执行：
1. **GitHub Pages**：https://legalinvest.github.io/adhd-agent-harness/
2. **阿里云服务器**：https://legalbot.top/adhd/ （rsync 到 121.40.230.101 的 /opt/apps/static/adhd/，凭据在仓库 Secrets：ALIYUN_SSH_KEY/HOST/USER）

⚠️ 服务器上 /opt/apps/static/adhd 归 CI 管，手动改动会被下次部署覆盖。

## 4. 相关仓库全景

| 仓库 | 用途 | 部署 |
|---|---|---|
| **adhd-agent-harness**（本仓库） | 核心项目 | GitHub Pages + legalbot.top/adhd/ |
| jinzhou-logistics-hub-intel | 锦州物流枢纽情报系统 | legalbot.top/jinzhou/（push 自动部署，源目录 `02_工作资料_WORKING/`） |
| shuangying-ai-investment-platform-demo | 双盈智慧招商平台 Demo | legalbot.top/shuangying/（push 自动部署） |
| industrial-park-investment-ecosystem | 产业园区招商生态研究院 | legalbot.top/park/（push 自动部署） |
| investment-financing-pm-ecosystem | 投融资项目管理生态研究院 | legalbot.top/invest/（push 自动部署） |
| shuangjianghu-ai-toolbox-demo | 双江湖AI百宝箱演示 | legalbot.top/toolbox/（push 自动部署） |

以上 5 个静态站与本仓库共用同一把专用部署密钥（各仓库 Secrets 已配置）。`srv-*` 仓库是另一台服务器（43.142.31.198）的备份镜像，`*-local-sync` 是本地工作区镜像，均不是部署源。

## 5. 下一步（待项目所有者选择，三选一或组合）

1. **L4/L5 定向选题挖掘**：自我和解 / 亲密关系 / ADHD 优势与职业设计 / 人生价值——内容金字塔上层最稀薄，用 LBD + STORM + GraphRAG 定向挖掘新选题。
2. **启用每周自动滚动 Automation**：增量抓新论文 → 重排 → 只生成新晋选题 → 更新台账 → PR → 自动部署。
3. **开始发布并接回流数据**：用 `python -m engine.packager --rank N` 出发布资产包（公众号/小红书/知乎/口播稿），发布后把真实阅读/点赞/转发数据回流校准评分权重。

## 6. 常用命令

```bash
# 博客构建（Node 22）
cd blog && npm ci --legacy-peer-deps && npm run build

# 引擎语法检查
python3 -m compileall -q engine

# 发布资产包
python -m engine.packager --rank 1

# 增量滚动（需 LLM API key 环境变量）
python -m engine.pipeline
```

## 7. 关键文件索引

- `docs/METHODOLOGY.md` — 项目宪法（北极星、五层金字塔、五型问题、证据规则、安全边界、质量清单）
- `engine/` — 评分/生成/滚动引擎；`engine/scorer.py` 排名逻辑；`engine/pipeline.py` 增量滚动主流程
- `data/articles/` 与 `blog/src/content/articles/` — 正式文章（两目录必须 byte-identical）
- `data/archive/` — 下架文章正文归档；`data/rolling_log.json` — 每轮上/下榜台账
- `publishing/` — 发布资产包；`intelligence/` — 研究资产
- `.github/workflows/deploy.yml` — 双部署 workflow
