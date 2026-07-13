# Git Sync for ADHD AI Drafts

这套脚本把当前文件夹自动同步到 Git 仓库。最后你只需要填 3 个小内容：

1. Git 仓库地址，例如 `https://github.com/YOUR_NAME/YOUR_REPO.git`
2. 提交用户名
3. 提交邮箱

## 首次使用

先登录 GitHub：

```powershell
gh auth login
```

然后生成配置并初始化：

```powershell
.\setup-git-sync.ps1 -RemoteUrl "https://github.com/YOUR_NAME/YOUR_REPO.git" -UserName "YOUR_NAME" -UserEmail "YOUR_EMAIL@example.com"
```

如果不确定还缺什么，运行：

```powershell
.\check-git-sync.ps1
```

## 手动同步

```powershell
.\git-sync.ps1 -Message "sync: update ADHD AI drafts"
```

## 自动监听同步

```powershell
.\watch-git-sync.ps1
```

它会监听当前文件夹变化，默认等待 60 秒后自动提交并推送。

## 自测

```powershell
.\test-git-sync.ps1
```

这个测试会在 `.git-sync-fixture` 中创建一个本地模拟远程仓库，不访问 GitHub，用来验证初始化、提交、推送和状态文件。

如果测试夹具没有自动清理，可以运行：

```powershell
.\clean-git-sync-test.ps1
```

`.git-sync-fixture` 已经被忽略，不会上传。

## 真正投入使用前的最小清单

- GitHub 登录完成：`gh auth login`
- 已有一个 GitHub 仓库地址
- 运行过 `setup-git-sync.ps1`
- 运行过 `git-sync.ps1` 并看到 `Synced commit ...`

## 状态文件

同步后会生成：

```text
.git-sync/latest.json
```

里面记录最后一次同步时间、commit、branch 和 remote。

为了避免 Windows 桌面权限和沙盒用户冲突，Git 元数据会放在：

```text
.git-sync/repo.git
```

这不会被上传，也不会污染你的草稿文件夹。
