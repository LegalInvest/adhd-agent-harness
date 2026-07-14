# ADHD × AI 内容引擎 & 博客系统

一个**研究驱动**的 ADHD × AI 主题内容引擎：用 AI 智能体全网检索最新情报，
萃取真实事实/工具/研究，按证据强度评分，用最新发现进化替换低质选题，
最终生成 400 篇可溯源、有据可查的文章并发布到博客。

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
# 建议使用 Python 3.10+ 和 Node.js 20+

# 安装 Python 依赖
pip install -r requirements.txt

# 运行内容引擎生成 400 篇文章
python -m engine.pipeline

# 安装博客依赖
cd blog && npm install

# 启动开发服务器
npm run dev
```

内容引擎会访问公开网络并更新 `data/` 下的研究、选题和文章产物。首次全量执行前建议先提交当前数据快照；只做静态验收时无需运行完整 400 篇管线。

## 密钥与配置

当前代码不需要 API Key、Token 或登录凭据。研究模块通过公开搜索与网页抓取获取资料，因此需要正常网络连接，并应遵守来源站点的访问规则。

## 最小验收

```bash
# Python 源码静态验收，不触发网络抓取
python -m compileall engine

# 博客生产构建
cd blog
npm install
npm run build
```

`npm run build` 成功后，静态交付物位于 `blog/dist/`。完整内容管线验收再单独执行 `python -m engine.pipeline`，并检查 `data/` 与博客文章是否同步更新。

## 部署

```bash
cd blog && npm run build
# 输出在 blog/dist/ 目录，可部署到 Vercel/Netlify/Cloudflare Pages
```
