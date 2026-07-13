# 04 GitHub 恢复与同步交接

更新时间：2026-07-03

## 当前主项目同步状态

主项目：

- 本地：`C:\项目库\400篇ADHD✖️AI滚动池`
- GitHub：`https://github.com/LegalInvest/adhd-ai-creator-intelligence`
- 可见性：私有
- 分支：`main`
- 最新已知提交：`976161f docs: add project library GitHub sync audit`

## 已同步的项目库仓库

详见：`research/GITHUB_SYNC_AUDIT_2026-07-03.md`

已同步到 LegalInvest 的仓库：

- `https://github.com/LegalInvest/adhd-ai-creator-intelligence`
- `https://github.com/LegalInvest/openclaw-control-center-local-sync`
- `https://github.com/LegalInvest/mirofish-local-sync`
- `https://github.com/LegalInvest/wechat-article-exporter-local-sync`
- `https://github.com/LegalInvest/session-manager-local-sync`
- `https://github.com/LegalInvest/county-atlas-local-sync`

## 注意事项

部分原仓库不是 LegalInvest 名下，当前账号没有写权限：

- `TianyiDataScience/openclaw-control-center`
- `666ghj/MiroFish`
- `KKKKhazix/wechat-article-exporter`

因此这些项目保留原 `origin`，另加 `legalinvest` 镜像远端。不要误以为原仓库已经被推送。

## 快照镜像说明

`Control-Center` 和 `WeChat-Article-Exporter-Repo` 的原历史推送时出现缺失对象错误：

- `did not receive expected object`
- `remote unpack failed`

处理方式：创建 orphan 快照分支并推送到 LegalInvest 镜像仓库，保证当前工作区可恢复。旧历史仍留在本地，不要轻易清理。

## 常用命令

查看状态：

```powershell
git status --short
git remote -v
git log --oneline -5
```

提交并推送主项目：

```powershell
git add -A
git commit -m "docs: update handoff"
git push
```

确认敏感文件未入库：

```powershell
git check-ignore -v .env .env.example
git ls-files | Select-String -Pattern "^\\.env$|token|secret|credential|password"
```

## 恢复原则

- `.env`、`.env.*`、token、secret、credential、password 不入库。
- 每次大动作后写本地审计或状态文件。
- 账号/会话/远端失败时，本地项目目录是第一恢复源。
- 如果 GitHub push 失败，不要继续覆盖历史，先记录错误、当前提交、远端和分支。

