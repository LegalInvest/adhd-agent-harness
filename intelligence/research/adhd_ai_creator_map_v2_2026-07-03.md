# ADHD x AI / Vibe Coding 创作者情报库 v2

更新日期：2026-07-03

## 0. 口径先说清楚

用户原始愿望是“全网搜集 ADHD x AI / vibe coding 博主，尤其小红书”。这个题不能用“全网所有”做绝对承诺，因为小红书、抖音、Instagram、Threads、X 等平台都不是完整开放索引；不少内容只在 App 内可见，搜索引擎只能看到转载页、播客 shownotes、第三方资料页、App Store 文案和少量社媒 OCR。

所以本项目采用三层口径：

1. **强确认 ADHD x AI / vibe coding 创作者**：账号/本人明确 ADHD，同时内容明确 AI、Claude、ChatGPT、Cursor、OpenClaw、vibe coding、AI 工具或 AI 产品。
2. **高价值线索**：ADHD 明确，且有 AI/产品/开发/效率工具邻近证据，但还需要站内核验。
3. **扩展雷达**：AI/vibe 明确但 ADHD 未确认，或 ADHD 明确但 AI 未确认，用于后续交叉检索。

当前统计：

| 口径 | 数量 | 说明 |
|---|---:|---|
| 强确认 ADHD x AI / vibe coding 创作者/账号/团队 | 26 | 可点名，有公开证据链 |
| 中文/小红书/播客高价值线索 | 16 | 包括小红书、B站、小宇宙、公众号、App 创始人 |
| ADHD 明确但 AI 未确认 | 12 | 用于后续站内核验 |
| AI/vibe 明确但 ADHD 未确认 | 8 | 用于反向核验 |
| 公开可点名总样本 | 62 | 包括强确认、高价值线索和扩展雷达 |

> 注意：这不是“全网 ADHD 博主总数”。更准确地说，这是截至本轮公开网页索引能稳定点名、能写入情报库的样本数。

## 1. 这版比上一版好在哪里

### 亮点

- 从“少量名单”升级为“分层情报库”：强确认、线索、待核验分开，避免把弱证据混进强名单。
- 补上中文播客和小宇宙渠道：小红书内容经常通过小宇宙 shownotes、Apple Podcasts、搜狐/新浪/SMZDM 转载被搜索引擎捕捉。
- 增加“产品团队型创作者”：Dopamind、ADHD Pal、Codot 这类不是传统博主，但它们围绕 ADHD x AI 做产品、内容和社区，应该纳入项目。
- 增加“英文 AI 工作流作者”：Claude Code、Obsidian、second brain、vibe coding 方向的 ADHD 创作者明显增加。
- 增加工具验证：本地安装并测试 `redbook`、`xhs-cli`，明确站内搜索卡在小红书登录态。

### 不足

- 没有小红书登录 cookie，无法完成小红书 App 内全量检索。
- TikTok、Instagram、Threads 搜索结果噪声很高，很多只是 hashtag 帖，不一定是稳定博主。
- “ADHD 博主”本身定义模糊：有人是确诊经验号，有人是 ADHD 友好工具号，有人只是偶尔发 ADHD 标签。
- 第三方转载会丢失原始小红书笔记链接、粉丝数和发布时间，只能作为中等强度证据。
- 部分英文结果来自 LinkedIn/Instagram/Threads，公开索引能看到摘要，但不一定能长期访问全文。

## 2. 强确认 ADHD x AI / Vibe Coding 创作者

| # | 名称 | 平台 | 类型 | 证据摘要 | 可信度 |
|---:|---|---|---|---|---|
| 1 | AI金三啊 | 小红书 / 微博转载 / SMZDM | 中文 AI 博主 | 发过 ADHD prompt、ADHD AI 工具、Obsidian + Claude Code；新浪转载标注“AI博主” | 高 |
| 2 | ADHD执行力实验室 / 张程 | 小红书 / B站 / YouTube / 小宇宙 / 公众号 | 中文 ADHD 教练 + 前 ML 工程师 | 播客资料写明小红书/B站/油管同名；内容覆盖 ChatGPT、Claude、Cursor、Suno、AI 作曲、AI 学习工具 | 高 |
| 3 | 明天的我也是ADHD / 小明 | 小红书 / 小宇宙客座 | 中文小红书博主 | 小宇宙《再读一遍》明确称“小红书博主 @明天的我也是ADHD”，一起聊 OpenClaw/ClawdBot、飞书/Telegram AI 数字中枢 | 高 |
| 4 | Dopamind / Philo | 官网 / Blog / 小红书入口 | ADHD AI 产品创作者 | 官网称 AI focus companion designed for ADHD users；中文页写创始人 Philo 通过 AI 打造 ADHD 第二大脑；博客写 Vibe Working | 高 |
| 5 | 独立开发者Junga / 数码测评员Junga | 小红书 / 搜狐号 / App | ADHD 独立开发者 | 关联 ADHD Pal；搜狐文章称国内 ADHD 独立开发者 Junga，小红书开发；产品含 AI 规划、想法冰箱 | 中高 |
| 6 | ADHD Founders: Jesse J. Anderson, Marie Ng, Sharon Pope | Podcast / 社媒 | ADHD founder 社群 | Episode 63 “Vibe Coding for Fun and Profit”，讨论 Claude、ChatGPT、AI agents | 高 |
| 7 | Zack Proser | Blog / developer | 英文开发者 | 自述 ADHD，把 voice-first vibe coding 与 ADHD flow/chaos 连接 | 高 |
| 8 | Mohamed Amgad Khater | Blog / developer | 英文开发者 | 文章 “Vibe Coding My Way Out of ADHD”，用 Claude Code + Obsidian 做 ADHD-friendly assistant | 高 |
| 9 | Lo Zarantonello | Medium / Level Up Coding | 英文开发者作者 | 文章 “ADHD Brains Were Built for Vibe Coding”，提 Claude、Codex、Cursor | 中高 |
| 10 | Famer / My Space | Personal blog | 英文技术作者 | 写 “AI-native = ADHD-native”，自述 ADHD，讨论 AI-native coding agents | 中高 |
| 11 | Ryan Tolmia | YouTube | ADHD + AI 内容创作者 | 主题包括 AI tools for ADHD creators、ChatGPT + ADHD、Claude Projects | 中高 |
| 12 | Sonya Barlow | Blog / LinkedIn | 神经多样性 CEO / 内容创作者 | 写 neurodivergent CEO 使用 AI 工具，提 ChatGPT 帮助 ADHD brain | 中高 |
| 13 | Philip Lakin | LinkedIn | 讨论节点 / 创作者 | 发帖 “Claude Code + my ADHD ... 100k tokens of vibe coding”，高互动 | 中 |
| 14 | 散心二意 | 小宇宙 / 小红书嘉宾 | 中文 ADHD 播客 | EP3 “ADHD如何利用AI工具？”；嘉宾 Cassie 做 AI/计算思维，C君做图像处理 AI；含小红书账号 KKK_Cassie啊、橘女士 | 中高 |
| 15 | Cassie / KKK_Cassie啊 | 小红书 / 小宇宙 | ADHD x AI 教育科技嘉宾 | 《散心二意》EP3 嘉宾，教育科技方向博士，研究 AI 和计算思维培养 | 中高 |
| 16 | C君 / 橘女士 | 小红书 / 小宇宙 | AI 从业者嘉宾 | 《散心二意》EP3 嘉宾，曾在日本硬件制造商做图像处理 AI | 中 |
| 17 | Line Hjartarson | Medium | 英文 AI second brain 作者 | “The vault that thinks like me” 写 Obsidian + Claude Code，并明确 ADHD piece matters | 中高 |
| 18 | Olena Mytruk | Substack | Claude Code 工作流作者 | 写 Claude Code 是 ADHD-friendly AI assistant，自己大部分工作都在 Claude Code 中完成 | 中高 |
| 19 | Naomi Carrigan | Blog | AI assistant / wellbeing 作者 | “Hikari” 个人 AI assistant powered by Claude Code，用于管理 ADHD、工作和健康 | 中高 |
| 20 | Jenna Redfield | Substack | ADHD business / ChatGPT 作者 | “How I Use ChatGPT to Manage My ADHD Life & Business” | 中 |
| 21 | Christy Lingo / The ADHD Mompreneur | Podcast / Blog | ADHD entrepreneur 内容创作者 | “How to Use ChatGPT for ADHD Moms / ADHD ChatGPT Prompts for Life and Business” | 中 |
| 22 | Melissa Hale | LinkedIn | ADHD + AI 系列作者 | “Me Oh My, ADHD & AI” 系列，Claude + email/calendar/Notion | 中 |
| 23 | Wendy Breakstone | Threads | ADHD vibe coding creator | Threads 帖 “Adventures in vibe-coding (ADHD edition)” | 中 |
| 24 | Jonathan Acuna | Threads | ADHD entrepreneur + Claude Code | Threads 帖面向 ADHD entrepreneurs，Claude Code / VS Code / Terminal AI assistant | 中 |
| 25 | Amanda White | Instagram | neurodivergent vibe coding 传播者 | Instagram 摘要称 “Vibe coding ... neurodivergent space ... change everything” | 中低 |
| 26 | Matt Upham | Instagram | ADHD life OS / Claude Code | Instagram 摘要称 building ultimate ADHD life operating system with Claude Code、Codex、Cursor | 中低 |

## 3. 中文 / 小红书高价值线索

| # | 名称 | 平台 | 为什么值得继续追 | 状态 |
|---:|---|---|---|---|
| 1 | Vivi的ADHD日记 | 小红书 / B站 / Threads OCR | 用户点名；小红书 ADHD 账号影响力高；B站有同名空间；Threads OCR 捕捉到其小红书内容 | ADHD 高，AI 待核验 |
| 2 | 大号A娃 / adhd_diary | 小红书 | ADHD 账号，公开资料显示在开发 A 人备考小程序 | AI/开发邻近 |
| 3 | 玩AI的阿麦 | 小红书 | SMZDM 聚合页出现“保姆级教程！ADHD的AI生活助理训练指南” | AI 明确，原帖待开 |
| 4 | code A / Bingo Time | 产品 / 社媒 | ADHD 产品 + GPT-4o / Claude Code 开发线索 | 原始页面待二次核验 |
| 5 | Una | 小红书相关创业者 | 媒体报道其通过小红书验证 ADHD focus app 需求 | 账号待定位 |
| 6 | Codot | App Store / 小红书链接 | AI 语音助手，文案明确“ADHD 跟忙翻天的脑袋必备”，可保存小红书链接 | 产品型线索 |
| 7 | ADHD Pal | App Store / 搜狐 / 小红书 | AI 任务规划、想法冰箱，面向中国 ADHD 学生群体 | 产品型线索 |
| 8 | NoFeed / 菠萝的胃 | App Store / 小红书 / 即刻 | 反信息流搜索工具，描述注意力保护，作者小红书/即刻同名 | ADHD 邻近 |
| 9 | 念念念念喔 | 小红书 / 新周刊转载 | 曾因确诊 ADHD 分享在小红书引发讨论 | ADHD 高，AI 未确认 |
| 10 | 二的三次方播客 | 小红书 / 抖音 / B站 / Apple Podcasts | ADHD 福音主题，shownotes 含“让豆包给提示词开聊” | AI 邻近 |
| 11 | 中年管理者日常 | 小红书 / 公众号 / 小宇宙 | 《再读一遍》主播账号，OpenClaw/AI 数字中枢内容 | AI 高，ADHD 来自嘉宾 |
| 12 | 启师傅 / 启师傅AI客厅 | 小宇宙 / 即刻 | AI 独立开发者，产品“了然清单”定位适合 P 人和 ADHD | AI 高，ADHD 产品邻近 |
| 13 | 陈哥_David | 小宇宙 / 即刻 | AI 开发 App、Cursor、小红书推广案例；与 ADHD 友好待办产品同场 | AI 高，ADHD 邻近 |
| 14 | 静静 / 专注豆 | 小宇宙 / 小红书 | ADHD 解压玩具创业者，小红书爆款；虽“反 AI”，但可作为 ADHD 需求市场参照 | ADHD 市场线索 |
| 15 | 小马的懵圈频道 | 小红书 / 播客 | ADHD 经验类内容，节目评论提 ChatGPT 情绪理解 | ADHD 高，AI 弱 |
| 16 | 枕侠 / 狩江 | 小宇宙 / 小红书相关 | 国内第一档 ADHD 中文播客《散心二意》主播 | ADHD 高，AI 经 EP3 关联 |

## 4. ADHD 明确但 AI / Vibe Coding 未确认

| 名称 | 平台 | 备注 |
|---|---|---|
| ADHD幸福指南 | 小红书 | ADHD 社群/内容账号 |
| ADHD自救指南 | 小红书 | ADHD 经验账号 |
| 梨子最大 | 小红书 | ADHD 标签命中 |
| Nagi真的很文静 | 小红书 | ADHD / MBTI 个人账号线索 |
| 小荘的ADHD日记 | 小红书 | ADHD 日记类账号 |
| ADHDer / Lucie_1997 | 小红书 | ADHD + 心理/运动方向 |
| How to ADHD / Jessica McCabe | YouTube | 大型 ADHD 内容创作者 |
| Jarvis Johnson | YouTube / Podcast | ADHD + 前软件工程师背景 |
| 正经叭叭相关主播 | 小宇宙 / 小红书 / B站 | 拖延主题强，AI 只是弱提及 |
| 多此一问 / Problem Makers | 小宇宙 | 女性 ADHD、注意力系统 |
| 躁春天 | 小宇宙 | 残障时间/非线性时间，与 ADHD 议题邻近 |
| 双响屁 | 小宇宙 | 自我说明书、注意力机制相关 |

## 5. AI / Vibe 明确但 ADHD 未确认

| 名称 | 平台 | 备注 |
|---|---|---|
| 茶与风铃 / Tresa143 | 小红书 | Vibe Coding 玩家，大厂全栈工程师 |
| 瑞哥那 / topbusiness101 / @ZhiZhouHuang | 小红书 / X | AI 产品、vibe coding |
| 小盖AI | 小红书 | AI 账号影响力高 |
| 兮兮的AI实战笔记 | 小红书 | AI 工具/实战 |
| 摸鱼的AI笔记 | 小红书 | AI 工具账号 |
| 话仙桃 | 小宇宙 | ChatGPT 使用法，非 ADHD 主线 |
| 从零开始用AI | 小宇宙 | AI 创业/小红书案例，部分 ADHD 市场案例 |
| AI Native Developer / 悠一 | 小宇宙 | AI Native / 黑客松，非 ADHD 主线 |

## 6. 工具与采集状态

本地已安装：

- `@lucasygu/redbook@0.8.0`
- `xhs-cli@1.4.2`

验证结果：

| 工具 | 测试 | 结果 |
|---|---|---|
| redbook | `redbook search "ADHD AI" --json` | 失败：需要小红书登录 cookie；当前 Chrome 无可读取 `a1` cookie |
| xhs-cli | `xhs search "ADHD AI" --json` | 失败：当前 npm 版本没有 `search` 子命令，文档与实际命令不一致 |

可继续推进的站内方案：

1. 用户先在 Chrome 登录 `xiaohongshu.com`，再重试 `redbook search`。
2. 或手动提供小红书 cookie string，仅用于只读搜索。
3. 或改用真实浏览器自动化 skill / MCP，但仍需要登录态。

## 7. 100 次优化记录：每 10 次保留一次

这里不是泄露内部思考链，而是保留可审计的项目优化记录。

### 1-10：定义边界

- 从“全网所有 ADHD 博主”改成三个可执行口径：强确认、线索、扩展雷达。
- 明确“小红书站内全量”需要登录态，否则只能公开索引。
- 把“博主”扩展为“创作者/账号/播客/产品团队”，因为 ADHD x AI 很多是产品型内容。

### 11-20：修正质量标准

- 不再把单个 hashtag 直接算作博主。
- 引入证据等级：高 / 中高 / 中 / 中低。
- 对 Threads、Instagram 结果降权处理，因为公开摘要短、稳定性差。

### 21-30：补中文播客渠道

- 增加小宇宙、Apple Podcasts 检索。
- 新增《散心二意》EP3、“ADHD执行力实验室”、“再读一遍 x 明天的我也是ADHD”。
- 发现中文 ADHD x AI 讨论大量藏在 shownotes，而不是网页文章。

### 31-40：补小红书间接证据

- 用新浪、搜狐、SMZDM、虎嗅、腾讯新闻、豆瓣等转载页反查小红书内容。
- 加固 AI金三啊证据链。
- 找到 Vivi 的 B站同名空间和 Threads OCR 线索。

### 41-50：补产品团队

- 新增 Dopamind / Philo、ADHD Pal / Junga、Codot、NoFeed 等。
- 将“产品型账号”独立标注，避免和传统博主混淆。
- 把“ADHD 用户需求 + AI 产品 + 内容传播”作为独立观察类。

### 51-60：补英文 Claude Code / Obsidian 流派

- 新增 Mohamed Amgad Khater、Line Hjartarson、Olena Mytruk、Naomi Carrigan。
- 发现 “Claude Code + Obsidian + ADHD second brain” 是稳定子主题。
- 将 vibe coding 与 second brain 分开记录，但都归入 AI 工作流。

### 61-70：补英文创作者经济流派

- 新增 Ryan Tolmia、Jenna Redfield、Christy Lingo、Sonya Barlow。
- 识别 “ADHD entrepreneur / mompreneur / creator + ChatGPT prompts” 子主题。
- 对 YouTube/Podcast 结果按标题和频道定位判断，不只看单条视频。

### 71-80：补社交媒体弱信号

- 新增 Philip Lakin、Wendy Breakstone、Jonathan Acuna、Amanda White、Matt Upham。
- Threads/Instagram 只作为中低到中等级别，除非有明确账号与持续内容。
- 识别“ADHD + Claude Code / Codex / Cursor life OS”正在变成 2026 新热词。

### 81-90：重构报告结构

- 旧版乱码问题修复，重写为 UTF-8 中文。
- 增加计数表、亮点、不足、工具状态。
- 把“证据摘要”写进表格，减少用户来回点链接的负担。

### 91-100：产品化输出

- 最终输出从“名单”升级为“情报库”。
- 保留下一步采集方案：登录态、cookie、真实浏览器自动化。
- 输出可用于后续项目管理的分类：强确认、中文线索、ADHD-only、AI-only。

## 8. 下一步采集关键词

小红书 / 中文：

- `ADHD AI`
- `ADHD AI工具`
- `ADHD prompt`
- `ADHD 提示词`
- `ADHD Claude Code`
- `ADHD Cursor`
- `ADHD Obsidian`
- `ADHD OpenClaw`
- `ADHD ClawdBot`
- `ADHD vibe coding`
- `ADHD 独立开发者`
- `ADHD 小程序`
- `ADHD AI生活助理`
- `Vivi ADHD AI`
- `明天的我也是ADHD`
- `AI金三啊 ADHD`
- `玩AI的阿麦 ADHD`
- `Dopamind 小红书`
- `ADHD Pal Junga`

英文：

- `"ADHD" "Claude Code"`
- `"ADHD" "vibe coding"`
- `"ADHD" "Codex" "Cursor"`
- `"ADHD" "Obsidian" "Claude"`
- `"ADHD" "AI assistant" "second brain"`
- `"ADHD entrepreneur" "ChatGPT"`
- `"ADHD mom" "ChatGPT prompts"`
- `"neurodivergent" "vibe coding"`
- `"ADHD" "life operating system" "AI"`

## 9. 主要来源

- AI金三啊：`https://www.sina.cn/news/detail/5277783259351236.html`
- AI金三啊 Obsidian + Claude Code：`https://www.sina.cn/news/detail/5277370541934380.html`
- ADHD执行力实验室 Apple Podcasts：`https://podcasts.apple.com/us/podcast/adhd%E6%89%A7%E8%A1%8C%E5%8A%9B%E5%AE%9E%E9%AA%8C%E5%AE%A4/id1831144368`
- ADHD执行力实验室 小宇宙：`https://www.xiaoyuzhoufm.com/podcast/68917f6c3785854f3ede832c`
- 再读一遍 x 明天的我也是ADHD：`https://www.xiaoyuzhoufm.com/episode/6983f66170aae7e967a60fca`
- 散心二意 EP3：`https://www.xiaoyuzhoufm.com/episode/646e2a8f1672628240f7facd`
- Dopamind 官网：`https://dopamind.app/`
- Dopamind 中文页：`https://dopamind.app/zh`
- Dopamind 创始人博客：`https://dopamind.app/blog/why-i-built-dopamind`
- ADHD Pal / Junga 搜狐测评：`https://www.sohu.com/a/996479039_122663794`
- Junga 搜狐主页：`https://mp.sohu.com/profile?xpt=ZWY0MGNjODktNTVmMi00N2JhLTkzNDUtNmYxMGFjNGRiMTdh`
- Vivi B站空间：`https://space.bilibili.com/3546779964410027/`
- Lo Zarantonello / Level Up Coding：`https://levelup.gitconnected.com/adhd-brains-were-built-for-vibe-coding-a824c68863a0`
- Mohamed Amgad Khater：`https://amgad.io/posts/building-ai-assistant-productivity-claude-obsidian/`
- Philip Lakin LinkedIn：`https://www.linkedin.com/posts/philip-lakin_claude-code-my-adhd-turned-a-5-min-task-activity-7448186264048144384-a2LE`
- Line Hjartarson：`https://byaline.medium.com/the-vault-that-thinks-like-me-159aecaab6e5`
- Olena Mytruk：`https://olenamytruk.substack.com/p/claude-code-command-ai-memory`
- Naomi Carrigan：`https://blog.nhcarrigan.com/post/ai-assistant-for-work-and-wellbeing`
- Jenna Redfield：`https://jennaredfield.substack.com/p/how-i-use-chatgpt-to-manage-my-adhd`
- The ADHD Mompreneur：`https://www.theadhdmompreneur.com/podcast/adhd-and-chatgpt`
- Codot App Store：`https://apps.apple.com/us/app/codot-ai%E8%AA%9E%E9%9F%B3%E5%8A%A9%E7%90%86-%E5%B9%AB%E4%BD%A0%E8%A8%98%E4%BD%8F%E4%B8%80%E5%88%87-%E6%89%93%E7%90%86%E7%94%9F%E6%B4%BB%E8%88%87%E5%B7%A5%E4%BD%9C/id6743443746`
- 虎嗅 / 新周刊 ADHD 小红书报道：`https://www.huxiu.com/article/803201.html`
- Yahoo / 端传媒转载 ADHD 小红书规模线索：`https://tw.news.yahoo.com/%E5%8E%BB%E5%85%92%E7%A7%91%E9%96%80%E8%A8%BA%E7%A2%BA%E8%A8%BA-%E5%A4%9A%E5%8B%95%E7%97%87-%E5%BE%8C-%E4%B8%AD%E5%9C%8Bz%E4%B8%96%E4%BB%A3%E6%8A%8Aadhd%E7%94%A8%E4%BD%9C%E4%BA%86%E6%B5%81%E8%A1%8C%E7%A4%BE%E4%BA%A4%E6%A8%99%E7%B1%A4-034538702.html`
