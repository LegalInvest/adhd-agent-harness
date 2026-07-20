# ADHD × AI 内容宇宙（自动化引擎 + 人工发布资产）

> **北极星**：深入研究 ADHD，找到「人生 Harness 系统」的方法论，助力 ADHD 者获得幸福、成长与人生价值。
> 内容宪法见 [docs/METHODOLOGY.md](docs/METHODOLOGY.md)（人生 Harness 五层金字塔 / 文章解剖 / 证据与同构规则 / N-of-1 协议库 / 质量清单）。

一个**研究驱动**的 ADHD × AI 主题内容引擎：用 AI 智能体全网检索最新情报，
萃取真实事实/工具/研究，按证据强度评分，用最新发现进化替换低质选题，
最终生成 400 篇可溯源、有据可查的文章并发布到博客。

同时承载《问题XXX》系列的**人工发布资产**（由 adhd-ai-creator-intelligence 仓库合并而来）：
- `publishing/content-packs/` — 400 个闭环发布资产包（正文/发布包/小红书/知乎/短视频口播/48h回流表）
- `intelligence/` — 一手研究资产（创作者情报库/考古报告/策略报告/研究数据），已接入引擎语料层
- 人工精修的 400 个选题标题已并入问题池（engine/curated_topics.py），与自动候选同台滚动竞争

## 项目架构

```
ABCoding/
├── engine/              # Python 研究驱动内容引擎
│   ├── research.py      # 全网情报检索 (DuckDuckGo + trafilatura)
│   ├── knowledge.py     # 知识萃取：真实工具/研究发现/统计/策略
│   ├── categories.py    # 11大分类候选选题库
│   ├── scorer.py        # 证据驱动多维度评分
│   ├── evolution.py     # 研究驱动进化：用最新发现替换低分选题
│   ├── generator.py     # 事实驱动文章生成器（带来源引用）
│   └── pipeline.py      # 主流程编排
├── data/
│   ├── scraped_knowledge.json  # 全网抓取的真实研究内容
│   ├── knowledge_base.json     # 萃取的结构化知识库
│   ├── topics.json      # 选题池
│   ├── rankings.json    # 当前排名 + 进化历史
│   └── articles/        # 生成的 Markdown 文章
├── publishing/          # 人工发布资产（content-packs 400 包 / indexes / templates / delivery / feedback）
├── intelligence/        # 一手研究资产（research / root-assets / docs / sources / archive）
├── blog/                # Astro 博客网站
│   ├── src/
│   │   ├── content/     # 文章内容 (MDX)
│   │   ├── layouts/     # 页面布局
│   │   ├── pages/       # 路由页面
│   │   └── components/  # UI 组件
│   └── public/          # 静态资源
└── requirements.txt
```

## 核心机制（研究驱动情报闭环）

```
全网检索(research) → 知识萃取(knowledge) → 证据评分(scorer)
  → 研究驱动进化(evolution) → 事实文章生成(generator)
```

### 1. 全网情报检索 research.py
用 DuckDuckGo 搜索（35 条中英文查询矩阵）+ trafilatura 深度抓取，
获取数十篇真实研究论文与社区实践，带缓存与增量合并。

### 2. 知识萃取 knowledge.py
从抓取内容中萃取结构化知识：真实 AI 工具、研究发现（带来源）、
统计数据、可操作策略、核心概念，并提供按主题检索的接口。

### 3. 证据驱动评分 scorer.py
每个选题从 6 个维度评分 (1-10)，其中**证据强度权重最高**：
- **证据强度**: 知识库中支撑该选题的真实研究/统计/工具数量（权重 0.25）
- **SEO潜力**: 真实高搜索量关键词覆盖
- **跨平台吸引力**: 适配微信、知乎、小红书、Twitter、Medium
- **实用价值**: 可操作性
- **情感共鸣**: 读者连接感
- **分享潜力**: 病毒传播可能性

### 4. 研究驱动进化 evolution.py
- 用知识库中发现的**真实工具**生成全新选题候选
- 每一代用更有证据支撑的最新发现替换得分最低的选题
- 多轮迭代：好的留下，差的被最新情报替换

### 5. 事实文章生成 generator.py
不再空洞模板填充，而是把真实工具、研究发现、统计、策略
编织进每篇文章，并在文末附上**可点击的原始来源链接**。

### 6. 博客网站
- **框架**: Astro (最快的内容优先框架)
- **样式**: Tailwind CSS
- **特性**: 深色/浅色模式、分类筛选、搜索、SEO 优化、RSS

## 快速开始

```bash
# 安装 Python 依赖
pip install -r requirements.txt

# 运行内容引擎生成 400 篇文章
python -m engine.pipeline

# 安装博客依赖
cd blog && npm install

# 启动开发服务器
npm run dev
```

## 部署

```bash
cd blog && npm run build
# 输出在 blog/dist/ 目录，可部署到 Vercel/Netlify/Cloudflare Pages
```
