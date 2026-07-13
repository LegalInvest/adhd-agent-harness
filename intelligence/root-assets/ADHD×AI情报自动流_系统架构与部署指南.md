# ADHD×AI 情报自动流系统 —— 架构设计与部署指南

> **版本**: v1.0
> **日期**: 2026-05-08
> **定位**: ADHD内容创业者的"第二大脑"——自动化情报采集、分析、生成流水线

---

## 🧠 系统定位

**你不是在"看信息"，你是在运营一个情报机构。**

这个系统是你的"分布式大脑"——它每天自动追踪30位核心ADHD×AI博主的动态，用你设计的评分算法判断价值，生成适合你发布的各平台内容草稿，让你把有限的时间从"信息收集"转移到"创作和判断"。

---

## 🏗️ 系统架构图

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                        ADHD×AI 情报自动流系统架构                              │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐ │
│  │  数据采集层  │ → │  内容分析层  │ → │  洞察生成层  │ → │  发布准备层  │ │
│  │ Collection  │    │  Analysis   │    │   Insight   │    │  Publish    │ │
│  └─────────────┘    └─────────────┘    └─────────────┘    └─────────────┘ │
│         │                  │                  │                  │         │
│         ▼                  ▼                  ▼                  ▼         │
│  ┌───────────────────────────────────────────────────────────────────────┐ │
│  │                        ADHD友好工作流编排层                              │ │
│  │                   (15分钟Hyperfocus窗口设计)                             │ │
│  └───────────────────────────────────────────────────────────────────────┘ │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 📊 数据采集层 (Collection Engine)

### 监控目标 (30位核心博主)

| 平台 | 数量 | S级优先级 | 采集方式 |
|------|------|----------|---------|
| **Twitter/X** | 8 | 2人(@karpathy, @ylecun) | Twitter API v2 |
| **RSS订阅** | 4 | 2个(The Rundown, One Useful Thing) | feedparser |
| **微信公众号** | 6 | 1个(数字生命卡兹克) | wechat-spider/第三方 |
| **B站** | 3 | 0 | bilibili-api |
| **YouTube** | 3 | 1个(Two Minute Papers) | youtube-data-api |
| **Substack** | 3 | 0 | RSS直连 |
| **大厂员工** | 7 | 2人 | 多平台聚合 |

### 采集频率设计 (ADHD友好)

```
S级博主: 每30分钟检查一次 (Burst模式可能随时发生)
A级博主: 每2小时检查一次
B级博主: 每6小时检查一次
RSS源:   每1小时拉取一次

每日总采集量上限: 50条 (防止信息过载)
```

### 技术实现

```python
# Twitter API采集 (真实部署时需要)
import tweepy

class TwitterCollector:
    def __init__(self, bearer_token: str):
        self.client = tweepy.Client(bearer_token=bearer_token)
    
    def fetch_recent_tweets(self, handle: str, max_results: int = 10) -> List[RawItem]:
        user = self.client.get_user(username=handle)
        tweets = self.client.get_users_tweets(
            id=user.data.id,
            max_results=max_results,
            tweet_fields=["created_at", "public_metrics", "context_annotations"]
        )
        # 转换为RawItem...
```

---

## 🔬 内容分析层 (Analysis Engine)

### 核心算法: ADHD×AI相关性评分

```
重要性分数 = ADHD相关度×0.4 + AI主题度×0.4 + 情绪加成 + 博主优先级加成 + 互动数据加成

ADHD相关度: 0-1 (基于关键词匹配)
AI主题度:   0-1 (基于关键词匹配)
情绪加成:   0-0.25 (urgent/controversial/excited/trending)
博主优先级: 0-0.20 (S级0.20, A级0.10, B级0.05)
互动加成:   0-0.10 (基于点赞/转发数)
```

### 关键词词典

**ADHD关键词** (覆盖症状、优势、名人、生活方式):
- 核心症状: adhd, hyperfocus, dopamine, procrastination, impulsivity
- 优势相关: creativity, neurodiversity, neurodivergent
- 职场创业: founder, startup, burnout, productivity, workflow
- 科技名人: karpathy, elon, musk, sam altman, LeCun

**AI关键词** (覆盖技术、产品、公司、概念):
- 核心概念: ai, llm, gpt, chatgpt, claude, agent, agi
- 公司: openai, deepmind, anthropic, nvidia
- 产品: deepseek, sora, midjourney, stable diffusion
- 概念: vibe coding, english is the hottest

### 情绪检测引擎

| 情绪类型 | 触发词 | 加成 |
|---------|--------|------|
| **urgent** | breaking, leaked, exposed, 突发, 震惊 | +0.25 |
| **controversial** | wrong, vs, debate, 反驳, 骂战 | +0.20 |
| **excited** | amazing, incredible, 炸裂, wow | +0.15 |
| **trending** | viral, 热门, 热搜, 爆火 | +0.15 |
| **neutral** | 无 | +0.05 |

---

## 💡 洞察生成层 (Insight Generator)

### 自动摘要生成

- 基于关键词权重提取关键句
- 优先选择包含ADHD/AI核心概念的句子
- 限制200字符以内，适合快速浏览

### 趋势概念提取

- 跨所有内容统计概念出现频率
- 识别当日最热AI产品/概念
- 输出Top 5趋势概念

### 选题推荐引擎

基于以下信号生成推荐选题:
1. 当日最热趋势概念 → "{概念}对ADHD大脑的影响"
2. 高优先级内容摘要 → "从ADHD视角解读: {摘要}"
3. 固定栏目:
   - "今日AI圈ADHD含量最高的3个动态"
   - "ADHD创始人如何用AI工具管理信息过载"
   - "为什么Twitter是ADHD人群的天然栖息地？"

---

## 📱 发布准备层 (Publish Prep)

### 跨平台内容变形模板

| 平台 | 格式 | 长度 | 最佳发布时间 | 标题公式 |
|------|------|------|------------|---------|
| **Twitter/X** | 短推/Thread | <280字 | 22:00-24:00 | 🔥 {博主}刚发了关于{概念} |
| **公众号** | 长文 | 1500-3000字 | 6:00-8:00 或 22:00-24:00 | {博主}最新观点：{概念}——ADHD视角解读 |
| **小红书** | 图文笔记 | <1000字 | 12:00-13:00 或 19:00-20:00 | 🔥 {博主}又输出了！ADHD人看{概念} |
| **B站** | 短视频 | 30-60秒 | 18:00-22:00 | 3秒钩子→15秒核心→5秒ADHD视角→5秒互动 |
| **即刻** | 短动态 | <500字 | 随时 | {概念} + 个人ADHD体验 |
| **知乎** | 问答/文章 | 2000-5000字 | 20:00-22:00 | 为什么ADHD人群更适合{概念}？ |

---

## ⏱️ ADHD友好工作流设计

### 核心原则

```
1. 15分钟原则: 每次系统运行不超过15分钟 (ADHD hyperfocus窗口)
2. 即时反馈原则: 每步操作后立即显示结果 (多巴胺驱动)
3. 信息节食原则: 每天最多50条，只看最重要的
4. 一鱼多吃原则: 一次采集，多平台输出
5. 决策分离原则: 机器做筛选，人做创作
```

### 每日工作流程

```
06:00  系统自动运行第一轮 (早间简报生成)
       → 输出: Markdown简报 + 3个推荐选题

12:00  系统自动运行第二轮 (午间更新)
       → 输出: 新增高优先级动态

18:00  系统自动运行第三轮 (晚间汇总)
       → 输出: 完整日报 + 各平台内容草稿

21:00  你的15分钟创作窗口
       → 查看系统推荐的选题
       → 选择1-2个最有感觉的
       → 用系统生成的草稿作为起点
       → 加入你的ADHD视角和个人体验
       → 发布到主平台

22:00  系统变形分发
       → 同一内容变形到各平台
       → 设置定时发布
```

---

## 🛠️ 部署指南

### 第一步: 环境准备

```bash
# 创建项目目录
mkdir ~/adhd-ai-flow
cd ~/adhd-ai-flow

# 创建Python虚拟环境
python3 -m venv venv
source venv/bin/activate

# 安装依赖
pip install tweepy feedparser requests schedule python-dotenv
```

### 第二步: 配置文件 (.env)

```bash
# Twitter API v2 (developer.twitter.com申请)
TWITTER_BEARER_TOKEN=your_bearer_token_here

# 可选: YouTube Data API
YOUTUBE_API_KEY=your_youtube_api_key

# 系统设置
MAX_DAILY_ITEMS=50
MIN_IMPORTANCE=0.45
LOG_LEVEL=INFO
```

### 第三步: 定时任务设置 (cron)

```bash
# 编辑crontab
crontab -e

# 添加以下行 (每30分钟运行一次)
*/30 * * * * cd ~/adhd-ai-flow && source venv/bin/activate && python3 main.py --mode collect >> logs/collect.log 2>&1

# 每天21:00生成日报
0 21 * * * cd ~/adhd-ai-flow && source venv/bin/activate && python3 main.py --mode digest >> logs/digest.log 2>&1
```

### 第四步: 运行测试

```bash
# 模拟模式运行 (无需API key)
python3 adhd_ai_intelligence_flow.py

# 真实模式运行 (需要配置API key)
python3 adhd_ai_intelligence_flow.py --mode=production
```

---

## 📈 系统进化路线图

### v1.0 (当前)
- ✅ 基础采集引擎 (Twitter + RSS)
- ✅ ADHD×AI评分算法
- ✅ 每日摘要生成
- ✅ 跨平台内容变形

### v1.1 (下一步)
- 🔲 接入微信公众号爬虫
- 🔲 接入B站API
- 🔲 情感分析升级 (使用transformers模型)
- 🔲 概念提取升级 (使用NER模型)

### v1.2 (进阶)
- 🔲 历史趋势分析 (某话题7天/30天热度曲线)
- 🔲 博主影响力网络图 (谁影响谁)
- 🔲 自动发现新博主 (基于转发链)
- 🔲 LLM辅助摘要生成 (GPT-4/Claude)

### v2.0 (终极)
- 🔲 全自动发布 (接入各平台API自动发布)
- 🔲 A/B测试 (不同标题/发布时间的效果对比)
- 🔲 互动监控 (追踪发布后互动数据)
- 🔲 反馈学习 (根据历史表现调整评分算法)

---

## 🎯 给ADHD用户的特别提醒

### 这个系统为什么适合你

1. **它替你做了你最讨厌的事**: 信息收集和筛选 (ADHD最不擅长的)
2. **它放大你最擅长的事**: 创作、联想、表达 (ADHD最擅长的)
3. **它匹配你的注意力模式**: 15分钟一轮，即时反馈
4. **它理解你的大脑**: ADHD相关度评分，优先推送与你相关的内容

### 防burnout设置

```python
# 在配置中添加
MAX_DAILY_ITEMS = 30  # 从50降到30，如果你感觉过载
SKIP_WEEKENDS = True  # 周末不采集，强制休息
NOTIFICATION_COOLDOWN = 3600  # 同一博主1小时内只通知一次
```

### 多巴胺触发器设计

```
系统输出使用emoji和颜色编码:
🔥 urgent (红色) → 立即行动!
🟡 analyze (黄色) → 值得思考
🟢 share (绿色) → 简单转发
⚪ ignore (灰色) → 跳过

每轮运行后显示:
✅ 今日已采集 X 条
🔥 发现 Y 条高价值
💡 推荐 Z 个选题
📊 你的今日ADHD指数: XX%
```

---

## 💾 文件清单

| 文件 | 说明 |
|------|------|
| `adhd_ai_intelligence_flow.py` | 主系统代码 (532行，可直接运行) |
| `.env` | 环境变量配置 (API key等) |
| `adhd_ai_flow_data.json` | 历史数据存储 |
| `logs/` | 运行日志 |

---

## 🚀 现在就开始

```bash
# 1. 复制代码到本地
cp adhd_ai_intelligence_flow.py ~/adhd-ai-flow/

# 2. 运行模拟模式测试
python3 adhd_ai_intelligence_flow.py

# 3. 申请Twitter API key (developer.twitter.com)
# 4. 配置.env文件
# 5. 设置cron定时任务
# 6. 每天查看你的情报简报!
```

---

> **"这个系统不是你的老板，它是你的员工。它24小时不间断地工作，只为让你每天早上醒来时，看到一份已经整理好的、只属于你的、关于ADHD×AI世界的情报简报。你的任务只有一个：用你ADHD独有的视角，把这些情报变成爆款内容。"**
