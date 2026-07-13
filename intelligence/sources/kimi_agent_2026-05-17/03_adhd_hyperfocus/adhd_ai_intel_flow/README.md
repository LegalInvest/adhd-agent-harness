# 🧠 ADHD×AI 情报自动流 (ADHD×AI Intelligence Flow)

> 为 ADHD 博主设计的自动化情报收集、分析和内容生成系统。
> 不是你的另一个待办工具——是你研究 ADHD×AI 交叉领域的**外部认知伙伴**。

---

## 系统架构

```
┌─────────────────────────────────────────────────────────┐
│                    ADHD×AI 情报自动流                      │
├─────────────┬─────────────┬─────────────┬───────────────┤
│  数据捕获层  │  智能处理层  │  思考生成层  │   内容输出层   │
├─────────────┼─────────────┼─────────────┼───────────────┤
│ • arXiv论文  │ • 自动分类   │ • 知识连接   │ • 每日简报    │
│ • Reddit社区 │ • 重要性评分 │ • 趋势检测   │ • 社交动态    │
│ • PubMed    │ • 中文摘要   │ • 矛盾发现   │ • 深度选题    │
│ • 新闻源    │ • 关键洞察   │             │ • 周报汇总    │
│ • 政策审批   │             │             │               │
└─────────────┴─────────────┴─────────────┴───────────────┘
```

## 核心设计理念

这个系统不是"又一个生产力工具"。它是为 ADHD 大脑的**结构性需求**设计的：

1. **不需要启动** — 自动运行，你只需要看结果
2. **反向提问** — 不只是收集信息，而是生成洞察
3. **对话即输入** — 你说/写，AI 处理一切
4. **复利知识图谱** — 今天的每条情报自动连接过去的研究

## 快速开始

### 1. 安装依赖

```bash
pip install pyyaml requests
```

### 2. 运行测试（使用模拟数据）

```bash
python run.py --test
```

这会展示系统的完整能力：收集 → 分类 → 评分 → 分析 → 生成多格式输出。

### 3. 运行实际收集

```bash
# 每日情报收集
python run.py --daily

# 查看输出
cat output/daily/brief_YYYYMMDD.md       # 每日简报
cat output/daily/social_YYYYMMDD.md      # 社交动态稿
cat output/drafts/triggers_YYYYMMDD.md   # 深度选题提醒
```

## 配置文件 (`config/config.yaml`)

### 数据源开关

```yaml
data_sources:
  arxiv:
    enabled: true        # 开关
    keywords:            # 自定义关键词
      - "ADHD"
      - "attention deficit"
      - "digital phenotyping"
    max_results: 20      # 每次最多收集
    days_back: 7         # 收集最近N天

  reddit:
    enabled: true
    subreddits:          # 自定义社区
      - "ADHD"
      - "adhd_science"
      - "ADHD_Programmers"
    min_score: 50        # 最低点赞数过滤
```

### 输出格式

```yaml
output:
  formats:
    daily_brief:         # 每日简报 (Markdown)
      enabled: true
    social_posts:        # 社交媒体动态稿
      enabled: true
      platforms:         # 适配不同平台
        - "twitter"
        - "zhihu"
        - "xiaohongshu"
    deep_draft:          # 深度选题触发器
      enabled: true
      trigger_threshold: 8.0  # 重要性>8时触发
```

## 输出格式说明

### 📄 每日简报 (`output/daily/brief_YYYYMMDD.md`)

按分类组织的情报汇总，每条包含：
- 标题 + 重要性评分
- 中文摘要
- 关键洞察
- 与已有知识库的连接
- 原文链接

### 📱 社交媒体动态稿 (`output/daily/social_YYYYMMDD.md`)

预格式化的社交媒体内容：
```
【ADHD×AI情报流】

论文标题/讨论主题

💡 一句话洞察

来源: arXiv
链接
```

直接复制粘贴即可发布到 Twitter/知乎/小红书。

### 🚨 深度选题触发器 (`output/drafts/triggers_YYYYMMDD.md`)

当情报重要性 > 8.0 时自动生成，包含：
- 选题标题 + 评分
- 为什么重要
- 建议的四个分析角度（事实/意义/知识连接/行动影响）

**这就是你的存稿选题池。**

## 定时运行

### 使用 cron (Linux/Mac)

```bash
# 编辑 crontab
crontab -e

# 每天早上8点运行
crontab -e
0 8 * * * cd /path/to/adhd_ai_intel_flow && python run.py --daily
```

### 使用 GitHub Actions (免费云端运行)

创建 `.github/workflows/daily-intel.yml`：

```yaml
name: Daily ADHD×AI Intel
on:
  schedule:
    - cron: '0 8 * * *'  # 每天UTC 8点
  workflow_dispatch:       # 也支持手动触发

jobs:
  collect:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
        with:
          python-version: '3.10'
      - run: pip install pyyaml requests
      - run: python run.py --daily
      - uses: actions/upload-artifact@v3
        with:
          name: daily-intel
          path: output/daily/
```

## 进阶：接入 LLM 增强分析

当前系统使用**规则驱动**的分析（零成本）。要启用 LLM 增强：

### 1. 配置 LLM API

在 `config/config.yaml` 中：

```yaml
processing:
  llm:
    provider: "anthropic"
    model: "claude-sonnet-4-20250514"
    # 添加 API key 到环境变量
```

### 2. 设置环境变量

```bash
export ANTHROPIC_API_KEY="sk-ant-..."
```

### 3. LLM 增强后的能力

- **更精准的中文摘要**（而非模板化输出）
- **更深层的洞察生成**（连接你已有的研究知识）
- **自动发现矛盾信号**（新论文与已有结论的矛盾）
- **个性化的存稿建议**（基于你的写作风格和受众）

## 项目结构

```
adhd_ai_intel_flow/
├── config/
│   └── config.yaml              # 配置文件
├── collectors/
│   ├── __init__.py
│   ├── base.py                  # 收集器基类
│   ├── arxiv.py                 # arXiv论文收集
│   └── reddit.py                # Reddit社区收集
├── processors/
│   ├── __init__.py
│   └── intelligence_processor.py # 智能处理器
├── output/
│   ├── daily/                   # 每日输出
│   ├── weekly/                  # 周报输出
│   └── drafts/                  # 深度选题
├── vault/                       # 知识库（连接已有研究）
├── run.py                       # 主运行脚本
└── README.md                    # 本文件
```

## 你是 ADHD 博主，这个系统为你解决什么？

| 你的痛苦 | 系统的解决方案 |
|---------|--------------|
| "信息太多，不知道看什么" | 自动过滤+重要性评分，只看>6分的内容 |
| "看到了好东西，但忘了记录" | 自动捕获+归档+连接，永不遗忘 |
| "想写但不知道写什么选题" | 深度选题触发器自动推荐 |
| "写了但不知道怎么发" | 自动生成多平台社交动态稿 |
| "想保持更新但总是拖延启动" | 定时自动运行，你只需要看结果 |
| "研究成果散落在各处" | vault/ 目录统一存储，AI自动连接 |

## 下一步迭代

- [ ] 接入 PubMed 医学文献源
- [ ] 接入 Google News 新闻源
- [ ] 接入 Twitter/X 实时讨论
- [ ] LLM 增强分析模块
- [ ] 知识图谱可视化
- [ ] 趋势自动检测
- [ ] 多语言输出（中英文切换）
- [ ] Discord/Telegram 推送

---

> **核心哲学**: 这个系统不替代你的思考——它让你终于能**看见**自己思考的全貌。
>
> 就像 Wes Kennedy 说的："Stop looking for an app. Start looking for a collaborator."
