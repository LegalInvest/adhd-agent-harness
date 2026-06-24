# ADHD × AI 内容引擎 & 博客系统

一个自动化的 ADHD × AI 主题内容生成、评分、晋升和发布系统。

## 项目架构

```
ABCoding/
├── engine/              # Python 内容引擎
│   ├── categories.py    # 10大分类 × 40选题 = 400篇
│   ├── scorer.py        # 多维度评分系统
│   ├── evolution.py     # 晋升/淘汰进化机制
│   ├── generator.py     # 文章内容生成器
│   └── pipeline.py      # 主流程编排
├── data/
│   ├── topics.json      # 选题池
│   ├── rankings.json    # 当前排名
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

## 核心机制

### 1. 选题生成
覆盖 10 大核心分类，每个分类 40 个精选选题：
- AI工具实战、专注力管理、时间管理、情绪调节、学习方法
- 职场发展、创业创新、亲子教育、科学研究、生活方式

### 2. 多维度评分
每个选题从 6 个维度评分 (1-10)：
- **SEO潜力**: 关键词搜索量、竞争度
- **跨平台吸引力**: 适配微信、知乎、小红书、Twitter、Medium
- **独特性**: 角度新颖度
- **实用价值**: 可操作性
- **情感共鸣**: 读者连接感
- **分享潜力**: 病毒传播可能性

### 3. 进化晋升机制
- 候选池 > 400 篇选题
- 多维度加权评分排序
- 保留 Top 400
- 新选题替换末位选题
- 多轮迭代优化

### 4. 博客网站
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
