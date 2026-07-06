# Workflow: Update Indexes

适用场景：新增、改名、删除或补全任何 `问题*.md` 正文后。

## 命令

```powershell
.\scripts\update-index.ps1
```

## 输出

- `indexes/问题001-108_MD总索引.md`
- `indexes/问题001-108_MD总索引.html`

## 检查

确认新增编号显示为“已有正文”，并且链接可打开。

## 内容质检

新增或重写正文后，继续运行：

```powershell
.\scripts\audit-content.ps1
```

确认 `delivery/content_qa/内容质检_001-108.html` 中没有“需重写”。
