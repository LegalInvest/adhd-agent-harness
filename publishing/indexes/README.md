# Indexes

本目录存放项目索引。

当前主要索引：

- `问题001-260_MD总索引.md`
- `问题001-260_MD总索引.html`

历史索引 `001-100`、`001-108` 保留作阶段快照，不再作为当前状态依据。

刷新方式：

```powershell
.\scripts\update-index.ps1 -EndNumber 220
```

当前最新口径建议使用：

```powershell
.\scripts\update-index.ps1 -EndNumber 260
```

不传 `-EndNumber` 时，脚本会自动扫描根目录 `问题*.md` 的最大编号。

索引使用相对路径，仓库移动或 clone 后仍可打开正文文件。

如果已运行 `.\scripts\render-articles.ps1 -EndNumber 260`，索引里的“打开正文”会优先跳转到 `delivery/rendered_articles/` 下的渲染 HTML，而不是 Markdown 源文件。
