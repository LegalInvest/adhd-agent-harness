# Workflow: Git Sync

本仓库已有 Git 同步脚本：

- `setup-git-sync.ps1`
- `git-sync.ps1`
- `watch-git-sync.ps1`
- `check-git-sync.ps1`
- `test-git-sync.ps1`
- `README_git_sync.md`

## 首次配置

作者需要提供三个小内容：

- GitHub 仓库地址
- 提交用户名
- 提交邮箱

配置命令示例：

```powershell
.\setup-git-sync.ps1 -RemoteUrl "https://github.com/YOUR_NAME/YOUR_REPO.git" -UserName "YOUR_NAME" -UserEmail "YOUR_EMAIL@example.com"
```

## 检查

```powershell
.\check-git-sync.ps1
```

## 手动同步

```powershell
.\git-sync.ps1 -Message "sync: update ADHD AI drafts"
```

## 安全边界

上传前确认 `.gitignore` 正常排除了：

- `.env`
- token、secret、credential、password
- `.claude/`
- `.codex/`
- `.agents/`
- `.git-sync/`
- 浏览器登录数据

不要在未确认远程仓库可见性时公开推送。

