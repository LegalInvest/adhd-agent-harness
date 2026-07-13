# Scripts

本目录放可复跑脚本，目标是让仓库状态靠文件系统事实更新，而不是靠记忆。

## update-index.ps1

刷新 Markdown 与 HTML 索引：

```powershell
.\scripts\update-index.ps1 -EndNumber 260
```

输出：

- `indexes/问题001-260_MD总索引.md`
- `indexes/问题001-260_MD总索引.html`

不传 `-EndNumber` 时，脚本会自动扫描根目录 `问题*.md` 的最大编号。索引会优先把“打开正文”链接指向 `delivery/rendered_articles/` 下的渲染 HTML。

## render-articles.ps1

把根目录 `问题*.md` 渲染成可直接浏览的 HTML 正文页：

```powershell
.\scripts\render-articles.ps1 -EndNumber 260
```

输出目录：

- `delivery/rendered_articles/`

## audit-content.ps1

刷新正文内容质检表：

```powershell
.\scripts\audit-content.ps1 -EndNumber 260
```

输出：

- `delivery/content_qa/内容质检_001-260.csv`
- `delivery/content_qa/内容质检_001-260.html`

质检字段：

- 选题
- 题目
- 字数
- 3 个核心观点
- 解决的问题
- 质量评分
- 质量状态
- 质检备注
- 正文链接

## build-topic-board.js

刷新 001-220 的选题升级看板：

```powershell
node .\scripts\build-topic-board.js
```

输出：

- `docs/topic-pools/ADHDxAI_选题升级看板_001-220.md`
- `docs/topic-pools/ADHDxAI_选题升级看板_001-220.html`
- `docs/topic-pools/ADHDxAI_选题升级看板_001-220.csv`

脚本会合并 `001-108` 基础正文、`109-168` 资料驱动选题、`169-180` 成就盲视/回流增量、`181-220` 项目治理/产品化增量，并生成状态、优先级、重复风险、写作技法、真实痛点、产品入口和下一步动作。

## generate-missing-articles-110-179.js

一次性补稿脚本，已用于 2026-05-20 补齐 `109-180` 中剩余正文。后续原则上不应再优先运行它，而应进入发布包、真实回流和产品化验证。

## generate-articles-181-220.js

一次性补稿脚本，已用于 2026-05-20 补齐 `181-220` 项目治理与产品化层正文。后续原则上不应再优先运行它；如果要正式发布其中的 S 级题，应该做二轮编辑和发布包，而不是重新批量生成。

## generate-articles-223-260.js

一次性补稿脚本，已用于 2026-05-21 补齐 `223-260` Remix、商业化与产品验证层正文，并生成 `docs/topic-pools/问题221-260_Remix商业化与产品验证选题增量.md`。后续原则上不应再优先运行它；下一步应推进十个可复用入口和真实回流。
