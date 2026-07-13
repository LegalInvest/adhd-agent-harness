# Workflow: Write Missing Draft

适用场景：某个编号有标题但没有本地正文。

## 步骤

1. 在 `PROJECT_STATUS.md` 或 `indexes/问题001-108_MD总索引.md` 找到待写编号。
2. 用 `templates/article_template.md` 生成正文结构。
3. 文件名使用：

```text
问题NNN_主标题_副标题.md
```

4. 正文必须包含：

- 一个具体生活场景
- 一个反常识判断
- 一个机制解释
- 至少三个铁证或例子
- 一个可执行动作

5. 写完运行：

```powershell
.\scripts\update-index.ps1
```

6. 更新 `PROJECT_STATUS.md` 和 `NEXT_ACTIONS.md`。

## 优先补写顺序

1. `076-090`
2. `014-031`
3. `012`
