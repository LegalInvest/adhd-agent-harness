# ab-coding · 项目目标卡

> 本卡由 leader 流程于 2026-07-29 生成，是本项目唯一目标文档；接手的 agent 先读本卡。

## 为什么干（一句意图＋干完世界什么样）

用 AI 智能体全网检索 ADHD × AI 主题的真实研究、工具和统计，按证据强度评分、迭代进化选题，自动产出 400 篇带来源引用的中文文章并发到 Astro 博客。干完之后：一个内容可溯源、静态可部署的「ADHD × AI」中文内容站上线就绪，读者每篇文章末尾都能点回原始研究出处。

## 现状（2026-07-29 实测）

- **GitHub 仓**：origin = `https://github.com/LegalInvest/ab-coding.git`。
- **技术栈**：Python 内容引擎（`engine/` 8 个模块，依赖 jieba / ddgs / trafilatura，见 `requirements.txt`，README 建议 Python 3.10+）＋ Astro 5 + Tailwind CSS 3 静态博客（`blog/`，README 建议 Node.js 20+）。
- **体量**：git 跟踪 834 个文件，其中 Markdown 401 个（含 400 篇文章）；磁盘约 15MB（不含 .git 与 node_modules）。`data/articles/` 400 篇已生成，已同步进 `blog/src/content/articles/`（400 个），`blog/dist/articles/` 也有 400 个构建产物页。
- **最近提交**：2026-07-14 `f8b63e4f fix: restore reproducible Astro blog build`，全仓共 6 个提交，当前分支 `codex/runtime-readiness-20260714`，工作区干净。最后一次活动在 15 天前，核心目标（400 篇）已达成。
- **怎么跑**（README 写的命令都与文件对得上）：
  - 静态验收 `python -m compileall engine` —— **2026-07-29 已实测通过**。
  - 博客构建 `cd blog && npm install && npm run build` —— **未实测重跑**；但 `blog/node_modules/` 与 `blog/dist/` 已存在且 dist 内含 400 篇文章页，说明上次构建成功过。
  - 完整管线 `python -m engine.pipeline` —— **未实测**（会联网抓取并重写 `data/` 与文章产物）。
  - 开发预览 `cd blog && npm run dev` —— 未实测。
- 无嵌套 git 仓、无 vendor 克隆。项目不需要任何 API Key（README 明示），仅需正常网络。

## 下一步（维护模式）

核心目标已完工，进入维护模式，只做巡检与按需保鲜：

1. **Python 静态巡检**：在仓库根目录执行 `python -m compileall engine -q && echo OK` —— 输出 `OK` 即通过。
2. **博客构建巡检**：`cd blog && npm run build && ls dist/articles | wc -l` —— 构建成功且输出 `400` 即通过。
3. **（可选）内容保鲜**：`python -m engine.pipeline` 重跑「检索→萃取→评分→进化→生成」闭环；验收 = 命令正常退出且 `git status` 的变更只落在 `data/` 与 `blog/src/content/articles/` 内。

## 禁区

- **不许 push** 到任何远程。特别注意：仓里存在一个「名字本身就是 URL」的异常远程，指向 `LegalInvest/adhd-agent-harness.git`，那不是本仓，处理它之前先问领导。
- `data/` 下全部 JSON 与 `data/articles/`：管线产物和知识库，手工改动会被下次管线覆盖。
- `blog/node_modules/`、`blog/dist/`、`blog/.astro/`：依赖与构建产物，不进 git，不手工编辑。
- 不引入、不创建任何密钥/`.env` 文件（项目当前设计为零密钥）。
- 不删现有分支（`desktop-b`、`devin/1782301812-adhd-ai-content-system`、`adhd-authority/main`）。

## 我替领导拍的板

- 400 篇文章目标已达成，定性为维护模式，不主动扩量、不重写引擎。
- 主语言按引擎代码定为 Python；博客是 Astro 静态站，产物以 `blog/dist/` 为准。
- 文章正文质量（措辞、来源时效）不在本卡验收范围内，发现问题另开任务。
- 本卡判断锚定 2026-07-29：`compileall` 为当日实测，npm build 与完整管线以现有产物为证、标注未实测。
