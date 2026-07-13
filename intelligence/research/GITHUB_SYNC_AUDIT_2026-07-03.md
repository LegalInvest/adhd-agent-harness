# GitHub 同步审计 2026-07-03

## 总结

本次已将 C:\项目库 下发现的 6 个 Git 仓库同步到 GitHub。原远端无写权限的项目，已在 LegalInvest 账号下创建私有镜像仓库；原历史存在缺失对象的仓库，采用当前工作区快照方式推送，保证 GitHub 上有可恢复版本。

## 同步结果

| 项目 | 本地路径 | 当前分支 | 本地提交/快照 | GitHub 同步位置 | 状态 |
|---|---|---|---|---|---|
| ADHD×AI滚动池 | C:\项目库\400篇ADHD✖️AI滚动池 | main | f53b283 | https://github.com/LegalInvest/adhd-ai-creator-intelligence | 已推送，私有仓库 |
| Control-Center | C:\项目库\Control-Center | main | 0eea825，本地；5acb78d，镜像快照 | https://github.com/LegalInvest/openclaw-control-center-local-sync | 原 origin 无写权限；已推送 LegalInvest 快照镜像 |
| MiroFish | C:\项目库\MiroFish | main | ea6a43f | https://github.com/LegalInvest/mirofish-local-sync | 原 origin 无写权限；已推送 LegalInvest 镜像 |
| WeChat-Article-Exporter-Repo | C:\项目库\WeChat-Article-Exporter-Repo | master | 7e42888，本地；0356c95，镜像快照 | https://github.com/LegalInvest/wechat-article-exporter-local-sync | 原 origin 无写权限；已推送 LegalInvest 快照镜像 |
| Session-Manager | C:\项目库\Session-Manager | main | 0c94ac9 | https://github.com/LegalInvest/session-manager-local-sync | 已创建并推送私有镜像 |
| 郡县图鉴 | C:\项目库\郡县图鉴 | county-atlas-trusted-compare-checkpoints | 194ef64 | https://github.com/LegalInvest/county-atlas-local-sync | 已创建并推送私有镜像 |

## 关键风险记录

- `400篇ADHD✖️AI滚动池` 已有 `.gitignore` 排除 `.env`、`.env.*`、密钥类文件和运行缓存。
- 本次同步前对 6 个仓库做了未跟踪敏感命名扫描，未发现 `.env`、secret、token、credential、password 命名文件进入待提交列表。
- Control-Center 与 WeChat 原历史推送时远端报 `did not receive expected object`，说明旧历史对象不完整或远端解包依赖缺失；已采用 orphan 快照镜像保底同步。
- 3 个原远端返回 403：`TianyiDataScience/openclaw-control-center`、`666ghj/MiroFish`、`KKKKhazix/wechat-article-exporter`。LegalInvest 无这些仓库的写权限，不能推回原仓库，只能推 LegalInvest 私有镜像。

## 本次 ADHD×AI 人群资产更新

- 新增 `ADHDxAI创作者情报库_v3_2026-07-03.md`。
- 新增 `research/ADHDxAI_全网创作者候选池_v3_2026-07-03.csv`。
- v3 统计：203 条可行动条目，其中 179 个个人/团队账号，24 个社区入口；强确认 ADHD×AI 样本 26 个，中文待复核线索 16 个，AI 创作者交叉扫描池 137 个。
