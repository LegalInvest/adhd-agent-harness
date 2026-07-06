const fs = require("fs");
const path = require("path");

const root = path.resolve(__dirname, "..");
const poolPath = path.join(root, "docs", "topic-pools", "问题221-260_Remix商业化与产品验证选题增量.md");

const existingTopics = [
  {
    number: 221,
    series: "Remix与跨域重组",
    title: "为什么 ADHD 是古希腊掌管 remix 的神？你的大脑网络不是分心，是在串台重组",
    problem: "痛点：跨域联想经常被当成分心，导致高价值连接没有被捕捉；需求：把网络串台记录成可筛选 remix 资产；待办：用 ADHD Remix 工作台记录一条高信号连接",
    product: "公众号/小红书；产品入口：ADHD Remix 工作台模板",
    priority: "S",
  },
  {
    number: 222,
    series: "商业化与多巴胺税制",
    title: "为什么 ADHD 自嗨很容易，商业化很难？你不是缺商业头脑，是缺多巴胺税制",
    problem: "痛点：新增选题和系统构想很爽，但发布、报价、回流低刺激；需求：给每次自嗨征收现实动作税；待办：每新增1个选题，完成2个旧资产动作",
    product: "公众号/模板；产品入口：自嗨/商业化时间预算表",
    priority: "S",
  },
];

const newTopics = [
  {
    number: 223,
    series: "资产治理",
    title: "为什么 ADHD 的想法库存需要折旧，而不是永远珍藏？你不是灵感富豪，是资产负债表混乱",
    problem: "痛点：每个想法都舍不得删，选题池越来越像精神仓库；需求：给灵感设置折旧、复活和核销规则；待办：把旧想法分成可发布、可模板化、冻结、删除四类",
    product: "项目系统；产品入口：想法折旧表",
    priority: "S",
  },
  {
    number: 224,
    series: "模板入口",
    title: "为什么 ADHD 的模板不是偷懒，而是把启动成本证券化？你买的不是表格，是下一次启动的坡道",
    problem: "痛点：每次从零开始都要重新攒启动能量；需求：把高频动作固化成可复用模板；待办：从135、169、221各拆出一个可复制模板",
    product: "公众号/模板包；产品入口：启动坡道模板库",
    priority: "A",
  },
  {
    number: 225,
    series: "低价产品验证",
    title: "为什么 ADHD 内容产品第一步不是课程，而是领取后能用一次的表格？完成一次，比听懂一套课更重要",
    problem: "痛点：大课制造二次羞耻，读者买了但完不成；需求：低价、低摩擦、当天可完成的小交付；待办：做一个领取后5分钟能填写的done list表格",
    product: "小红书/公众号；产品入口：9.9元轻模板",
    priority: "S",
  },
  {
    number: 226,
    series: "评论回流",
    title: "为什么 ADHD 的评论区关键词应该变成需求期货，而不是情绪烟花？反复出现的词，就是未来产品的价格信号",
    problem: "痛点：评论只被看成热闹，没有沉淀成需求趋势；需求：把高频词转成选题、模板和服务假设；待办：为135回流表增加关键词频次栏",
    product: "反馈系统；产品入口：评论关键词期货表",
    priority: "A",
  },
  {
    number: 227,
    series: "现金流验证",
    title: "为什么 ADHD 创作者需要反拖延报价单？别人愿意付钱的地方，往往是你最想逃的地方",
    problem: "痛点：最有价值的服务常常是自己最不想做的整理、拆解、跟进；需求：把逃避动作改写成可报价服务；待办：列出3个自己想逃但读者愿意托付的动作",
    product: "私域/服务；产品入口：反拖延报价单",
    priority: "S",
  },
  {
    number: 228,
    series: "Agent现实催化",
    title: "为什么 ADHD 的 Agent 不能只做助手，还要做现实催化剂？它必须把每个想法逼到一个外部动作",
    problem: "痛点：AI陪聊越顺，想法越多，但现实动作未必增加；需求：Agent每次输出都绑定发布、模板、回流或报价动作；待办：给常用Agent加一句现实动作结尾规则",
    product: "Agent工作流；产品入口：现实催化Prompt",
    priority: "S",
  },
  {
    number: 229,
    series: "知识库治理",
    title: "为什么 ADHD 的知识库越大，越需要墓地管理员？不是收藏更多，而是定期判死刑",
    problem: "痛点：资料越收越多，真正调用越来越少；需求：对沉睡资料做复活、归档、删除；待办：每周清理10条三个月未使用素材",
    product: "项目系统；产品入口：知识墓地清理SOP",
    priority: "A",
  },
  {
    number: 230,
    series: "信任与人设",
    title: "为什么 ADHD 的个人品牌需要失败现场栏目？可验证的修复，比完美教程更可信",
    problem: "痛点：完美教程和真实读者之间有距离；需求：展示失控、修复、复盘和下一次防线；待办：每周发布一次失败现场与修复动作",
    product: "公众号/小红书；产品入口：失败现场栏目模板",
    priority: "A",
  },
  {
    number: 231,
    series: "付费心理",
    title: "为什么 ADHD 的产品定价要从少自责开始，而不是提高效率？真正付费的是减轻内耗",
    problem: "痛点：效率承诺太抽象，少自责是可立即感知的收益；需求：把产品文案从提效改成减负、清债、恢复现实感；待办：重写135模板入口的价值主张",
    product: "销售文案；产品入口：少自责价值主张卡",
    priority: "S",
  },
  {
    number: 232,
    series: "平台变形",
    title: "为什么 ADHD 的小红书内容要先问能不能收藏后立刻用？平台不是阅读场，是即时工具箱",
    problem: "痛点：小红书用户收藏很多但行动很少；需求：让每篇短内容带一个可抄字段或动作；待办：把135改写成三行成就结算卡图文版",
    product: "小红书；产品入口：收藏即用卡片",
    priority: "A",
  },
  {
    number: 233,
    series: "自测入口",
    title: "为什么 ADHD 的公众号长文要有读者自测入口？没有自测，宏大框架很难变成自己",
    problem: "痛点：读者被框架击中，但不知道自己属于哪一种；需求：在长文中嵌入低门槛自测；待办：给135加一个成就盲视三问自测",
    product: "公众号；产品入口：三问自测模板",
    priority: "A",
  },
  {
    number: 234,
    series: "短视频钩子",
    title: "为什么 ADHD 的短视频前三秒必须说痛点，不要说概念？滑走发生在大脑还没认同你之前",
    problem: "痛点：概念开头太慢，短视频用户还没共鸣就划走；需求：前三秒先说具体崩溃现场；待办：把10个S级题写成痛点前三秒",
    product: "短视频；产品入口：前三秒钩子库",
    priority: "A",
  },
  {
    number: 235,
    series: "社群设计",
    title: "为什么 ADHD 的社群需要沉默成员入口？最痛的人未必最会发言",
    problem: "痛点：社群设计默认外向表达者，沉默高痛感用户被漏掉；需求：提供匿名表单、模板领取、低互动入口；待办：给读者坐标库增加匿名提交字段",
    product: "社群/私域；产品入口：沉默成员表单",
    priority: "A",
  },
  {
    number: 236,
    series: "私域验证",
    title: "为什么 ADHD 的私域不是朋友圈卖货，而是高痛感样本实验室？真正的价值是看见问题怎么复发",
    problem: "痛点：私域如果只发广告，会浪费高痛感样本；需求：把私域当作连续观察和共创场；待办：邀请20个高痛感读者测试一个模板7天",
    product: "私域/共创；产品入口：高痛感样本名单",
    priority: "A",
  },
  {
    number: 237,
    series: "产品验证",
    title: "为什么 ADHD 的产品验证要看复用率，不是看领取数？模板被第二次打开，才算活",
    problem: "痛点：领取模板很容易，真正使用和复用很难；需求：用3天、7天复用率判断产品生命力；待办：给每个模板增加二次打开记录字段",
    product: "产品验证；产品入口：模板复用率表",
    priority: "S",
  },
  {
    number: 238,
    series: "工具评测",
    title: "为什么 ADHD 的 AI 工具推荐必须写弃用理由？退出机制比种草更建立信任",
    problem: "痛点：工具种草只讲爽点，读者容易形成新依赖；需求：每次推荐都写不适合谁、何时弃用、如何导出；待办：给工具评测表增加弃用理由栏",
    product: "公众号/工具站；产品入口：弃用理由评分表",
    priority: "A",
  },
  {
    number: 239,
    series: "高压职业服务",
    title: "为什么 ADHD 的高压职业用户需要任务清债服务？他们不是缺软件，是欠债感太重",
    problem: "痛点：律师、咨询、创业者的任务背后附着人情、风险和羞耻债；需求：先清债再排序；待办：设计一次30分钟任务清债服务流程",
    product: "服务菜单；产品入口：任务清债服务",
    priority: "A",
  },
  {
    number: 240,
    series: "旧粉迁移",
    title: "为什么 ADHD 的法律旧粉迁移可以从案件压力表开始，而不是从 ADHD 科普开始？先救场，再换地图",
    problem: "痛点：旧法律粉可能不接受ADHD标签，但会接受案件压力过载；需求：用案件、客户、截止日期、风险语言桥接；待办：做一张案件压力表",
    product: "公众号/法律桥接；产品入口：案件压力表",
    priority: "A",
  },
  {
    number: 241,
    series: "Remix分级",
    title: "为什么 ADHD 的创意要分成梗、题、模板、产品四级？不分级，就会全都变成新坑",
    problem: "痛点：每个灵感都被当成项目，导致开坑过多；需求：先判断它只是梗、文章题、模板还是产品；待办：给Remix工作台增加四级判定",
    product: "模板；产品入口：创意四级分流表",
    priority: "A",
  },
  {
    number: 242,
    series: "多巴胺税制",
    title: "为什么 ADHD 需要15分钟现实税，而不是年度商业计划？现实只接受小额连续缴纳",
    problem: "痛点：年度计划太大，商业化动作太低刺激；需求：每次高能扩展后立刻交一个15分钟现实动作；待办：今天只完成一个报价、入口或回流字段",
    product: "执行系统；产品入口：15分钟现实税卡",
    priority: "S",
  },
  {
    number: 243,
    series: "成就证据",
    title: "为什么 ADHD 的 done list 应该带证据链接？没有链接的完成感，会被情绪推翻",
    problem: "痛点：低谷时大脑不相信模糊的完成记录；需求：done list绑定文件、截图、链接、评论；待办：给done list模板增加证据链接栏",
    product: "模板；产品入口：带链接done list",
    priority: "S",
  },
  {
    number: 244,
    series: "负罪感治理",
    title: "为什么 ADHD 的负罪感焚烧炉要保留灰烬？被烧掉的不是任务，而是错误责任",
    problem: "痛点：完全删除内疚会让人担心逃避责任；需求：保留被焚烧事项的判断记录；待办：给焚烧炉模板增加灰烬栏：为什么不再背它",
    product: "模板；产品入口：负罪感灰烬记录",
    priority: "A",
  },
  {
    number: 245,
    series: "今日唯一动作",
    title: "为什么 ADHD 的今日唯一动作不能完全由自己选？你会选最亮的，不一定选最该做的",
    problem: "痛点：自己选动作时容易被新鲜感劫持；需求：让Agent按现实影响、截止压力、能量状态共同排序；待办：设计今日唯一动作选择规则",
    product: "Agent模板；产品入口：唯一动作选择器",
    priority: "A",
  },
  {
    number: 246,
    series: "案例库",
    title: "为什么 ADHD 的读者案例要匿名结构化？故事不沉淀成变量，就只能感动一次",
    problem: "痛点：读者故事很有力量，但散落在评论和私信里；需求：匿名提取场景、卡点、工具、结果；待办：建立读者案例采集表",
    product: "社群/公众号；产品入口：匿名案例库",
    priority: "A",
  },
  {
    number: 247,
    series: "信任边界",
    title: "为什么 ADHD 的文章需要反对意见段落？信任不是来自全对，而是来自知道边界",
    problem: "痛点：强观点容易显得绝对化，尤其涉及ADHD机制和AI工具；需求：主动写边界、不适用人群、风险；待办：给S级文章增加反对意见段落",
    product: "写作模板；产品入口：边界声明卡",
    priority: "A",
  },
  {
    number: 248,
    series: "账号定位",
    title: "为什么 ADHD x AI 不能被做成纯效率账号？效率太窄，认知外包才是底层市场",
    problem: "痛点：效率工具账号容易同质化，也承接不了情绪、关系和身份痛点；需求：把定位升级为高方差大脑外接现实；待办：重写账号简介和置顶介绍",
    product: "账号定位；产品入口：认知外包定位文",
    priority: "A",
  },
  {
    number: 249,
    series: "低能量产品",
    title: "为什么 ADHD 的付费产品要有低能量版本？用户最需要你时，往往没有力气使用你",
    problem: "痛点：很多产品默认用户有精神、有时间、有耐心；需求：每个模板都要有30秒、5分钟、完整三档；待办：给135模板做低能量版",
    product: "模板包；产品入口：低能量三档版本",
    priority: "S",
  },
  {
    number: 250,
    series: "模板设计",
    title: "为什么 ADHD 的模板包要有空白太少原则？空白越多，启动越难",
    problem: "痛点：空白表格看似自由，实际会让ADHD卡住；需求：提供示例、选项、默认值和最小填写栏；待办：把Remix工作台改成半填充版",
    product: "模板设计；产品入口：半填充模板规范",
    priority: "A",
  },
  {
    number: 251,
    series: "失败恢复",
    title: "为什么 ADHD 的 Agent 工作流必须写失败时怎么办？正常运行不是产品，失败恢复才是",
    problem: "痛点：一旦断更、忘填、账号丢失，系统容易彻底塌；需求：每个工作流都有降级和恢复入口；待办：给135、221、222补失败恢复步骤",
    product: "Agent工作流；产品入口：失败恢复SOP",
    priority: "S",
  },
  {
    number: 252,
    series: "内容地图",
    title: "为什么 ADHD 的内容地图要按崩溃场景排序，而不是按理论分类？读者是带着火来的，不是带着目录来的",
    problem: "痛点：理论分类适合作者，不适合正在崩溃的读者；需求：按场景入口组织文章：做不动、睡不着、内疚、乱、回不来；待办：创建崩溃场景阅读地图",
    product: "网站/公众号置顶；产品入口：崩溃场景地图",
    priority: "A",
  },
  {
    number: 253,
    series: "第一批用户",
    title: "为什么 ADHD 的商业化第一批用户应来自主动托付，而不是泛粉丝？愿意交材料的人，已经越过了点赞",
    problem: "痛点：泛粉丝反馈太轻，无法验证真实付费需求；需求：识别愿意提交资料、填写模板、接受整理的人；待办：建立主动托付名单",
    product: "私域/服务；产品入口：主动托付名单",
    priority: "A",
  },
  {
    number: 254,
    series: "复购机制",
    title: "为什么 ADHD 的复购来自连续减负，而不是一次性顿悟？用户要回来的，是被持续接住的感觉",
    problem: "痛点：单篇文章让人顿悟，但顿悟很快消失；需求：用连续记录、提醒、回放和陪跑制造复用；待办：为done list设计7天连续使用机制",
    product: "模板/陪跑；产品入口：7天减负挑战",
    priority: "A",
  },
  {
    number: 255,
    series: "本地优先",
    title: "为什么 ADHD 的 AI 应用要先做本地文件夹，再做云端账号？外部前额叶不能再丢一次",
    problem: "痛点：账号、会话、平台丢失会造成认知义肢断裂；需求：所有关键状态本地可读、可迁移、可clone；待办：把模板、反馈、看板统一保存为本地Markdown",
    product: "项目系统；产品入口：本地优先Agent OS规范",
    priority: "S",
  },
  {
    number: 256,
    series: "断更保护",
    title: "为什么 ADHD 的项目管理需要停更保护机制？断更不可怕，断档才可怕",
    problem: "痛点：一旦停几天就羞耻到不敢回来；需求：保留状态、下一步、最低恢复动作；待办：给每个项目写一张断更恢复卡",
    product: "项目系统；产品入口：断更恢复卡",
    priority: "A",
  },
  {
    number: 257,
    series: "内容生命力",
    title: "为什么 ADHD 创作者的最大资产是持续被自己击中？麻木，才是内容死亡",
    problem: "痛点：写多了以后容易只剩结构，没有真正被击中的痛感；需求：定期回到个人现场、读者评论和失败记录；待办：每周选一条最刺痛评论写二轮文",
    product: "写作机制；产品入口：刺痛评论复写表",
    priority: "A",
  },
  {
    number: 258,
    series: "网站化",
    title: "为什么 ADHD 的工具站应该先做静态目录，而不是复杂后台？先让读者找到入口",
    problem: "痛点：一上来做复杂后台会消耗发布能量；需求：先用静态HTML组织文章、模板、工具、反馈入口；待办：把site目录做成最小可浏览导航",
    product: "网站；产品入口：静态工具站MVP",
    priority: "S",
  },
  {
    number: 259,
    series: "产品说明",
    title: "为什么 ADHD 的产品说明不能太完整？说明越长，启动越晚",
    problem: "痛点：详细说明会让用户读完就累；需求：说明只保留第一步、示例和完成标准；待办：把每个模板说明压缩到三行",
    product: "模板设计；产品入口：三行说明规范",
    priority: "A",
  },
  {
    number: 260,
    series: "阶段总纲",
    title: "为什么 ADHD x AI 的下一阶段不是更多文章，而是十个可复用入口？内容宇宙要开始长器官",
    problem: "痛点：继续扩文会越来越爽，但系统不一定变得更有用；需求：把高信号文章变成十个入口：模板、工具、地图、回流、服务；待办：选出十个入口并建立推进表",
    product: "项目总纲；产品入口：十入口路线图",
    priority: "S",
  },
];

function existingArticle(number) {
  const prefix = `问题${String(number).padStart(3, "0")}_`;
  return fs.readdirSync(root).find((name) => name.startsWith(prefix) && name.endsWith(".md"));
}

function sanitize(value) {
  return value
    .replace(/[<>:"/\\|?*]/g, "")
    .replace(/[，。！？、；：”“’‘（）《》【】「」]/g, "")
    .replace(/\s+/g, "")
    .slice(0, 76);
}

function splitProblem(text) {
  return {
    pain: (text.match(/痛点：([^；]+)/) || [])[1] || "痛点尚未命名",
    need: (text.match(/需求：([^；]+)/) || [])[1] || "需要压成可执行入口",
    todo: (text.match(/待办：(.+)$/) || [])[1] || "完成一个15分钟现实动作",
  };
}

function splitProduct(text) {
  const [platform, product = "最小产品入口"] = text.split("；产品入口：");
  return { platform, product };
}

function mainTitle(title) {
  return title.split("？")[0].trim() + "？";
}

function renderPool(topics) {
  const lines = [];
  lines.push("# 问题221-260 Remix、商业化与产品验证选题增量");
  lines.push("");
  lines.push("生成时间：2026-05-21");
  lines.push("");
  lines.push("这组不是继续堆症状百科，而是把 ADHD x AI 内容宇宙推向三个更硬的方向：Remix 资产化、商业化税制、产品验证。新增题必须带真实痛点、产品入口和验证动作，否则不进入本组。");
  lines.push("");
  lines.push("## 第一优先级");
  lines.push("");
  lines.push("建议优先闭环：`221`、`222`、`223`、`225`、`227`、`228`、`231`、`237`、`242`、`243`、`249`、`251`、`255`、`258`、`260`。");
  lines.push("");
  lines.push("## 选题表");
  lines.push("");
  lines.push("| 编号 | 系列 | 选题 | 真实痛点 / 需求 / 待办 | 平台与产品入口 | 优先级 |");
  lines.push("|---:|---|---|---|---|---|");
  for (const item of topics) {
    lines.push(`| ${item.number} | ${item.series} | ${item.title} | ${item.problem} | ${item.product} | ${item.priority} |`);
  }
  lines.push("");
  lines.push("## 推进规则");
  lines.push("");
  lines.push("- 每新增 1 个题，必须至少完成 2 个旧资产动作。");
  lines.push("- 每篇新正文必须自带模板、评论问题或验证动作。");
  lines.push("- 这一组的目标不是把编号推高，而是让内容宇宙长出可复用入口。");
  lines.push("");
  return lines.join("\n");
}

function renderArticle(topic) {
  const parts = splitProblem(topic.problem);
  const product = splitProduct(topic.product);
  const title = topic.title;
  const headline = mainTitle(title);
  const hook = `你可能已经见过这个问题：${parts.pain}。\n\n它看起来像一个小毛病，实际上会把 ADHD x AI 项目拖回熟悉的陷阱：想法很多，现实很少；共鸣很多，入口很少；文章很多，复用很少。\n\n所以这个题不能只写成一篇观点文。它必须同时回答三个问题：读者为什么痛，AI/Agent 能接住哪一段，最后能不能变成 ${product.product}。`;
  const isS = topic.priority === "S";
  const decision = isS
    ? "它应该进入 S 级闭环队列：正文、发布包、评论问题、模板入口、48 小时回流，一个都不能少。"
    : "它不一定要抢首发，但适合做成系统支线，给主炮题提供模板、字段、评分或恢复机制。";

  return `# 问题${String(topic.number).padStart(3, "0")}：${title}

${hook}

## 01 收敛

一句话打穿：${headline}真正问的不是“能不能再多一个好观点”，而是这个观点能不能替 ADHD 大脑减少一次现实摩擦。

ADHD 最容易把高刺激环节当成进展：想到一个新词，开一个新坑，生成一组新标题，设计一个更大的系统。可现实不会因为命名变轻。现实只会因为一个入口、一个模板、一个提交动作、一次回流记录而改变。

所以这篇的核心不是继续证明 ADHD 很特别，而是把特别的地方接到一个能使用、能验证、能复用的出口上。

## 02 穿透

这个问题有三层机制。

第一层，是痛点层。${parts.pain}。这不是情绪化抱怨，而是一个真实阻塞：它会让读者读完觉得被懂了，却仍然不知道下一步怎么做。

第二层，是系统层。${parts.need}。对 ADHD 来说，真正有价值的系统不是更复杂，而是更少决策、更少空白、更少从零开始。AI/Agent 的作用也不是陪你把想法说得更爽，而是把想法推到外部动作。

第三层，是验证层。${parts.todo}。只要没有验证动作，这个题就还停在作者脑内。只要有一个可复制入口，它才开始进入现实世界。

## 03 铁证

生活场景证据：你写完一篇文章很兴奋，但如果没有模板入口，读者只能点头；如果没有评论问题，现实不会回话；如果没有回流表，下一篇还是靠脑内感觉决定。

项目证据：这个文件夹已经有 200 多篇正文，说明“能写”不是瓶颈。真正的瓶颈是把正文变成发布包、模板、工具、表单、报价、服务和复用机制。

反事实也清楚：如果今天只新增 20 个标题，但没有一个入口被读者使用，项目会更大但更重；如果今天只让一个模板被第二次打开，项目会更小但更接近产品。

## 04 决策

你要把这个题当成产品前端，而不是内容装饰。

${decision}

判断一个题值不值得继续推进，不看它听起来多聪明，而看它能不能让读者完成以下任意一个动作：填写、复制、提交、评论、复用、托付、付费。

如果不能，它就只是漂亮标题。如果能，它就是一个未来产品的接口。

## 05 落地

今天的落地动作：${parts.todo}。

把它压成一张三行卡：

- 当前痛点：${parts.pain}
- 产品入口：${product.product}
- 15 分钟现实动作：${parts.todo}

只做这一个动作，不开新系统。做完以后再决定它进入文章、模板、服务、网站栏目，还是冻结池。

## 发布接口

- 公众号版核心标题：${headline}
- 小红书版钩子：${parts.pain}，这不是你不努力，是入口设计错了。
- 知乎回答问题：${headline}
- 短视频前三秒：ADHD 最容易被新想法骗过，现实只看你有没有留下一个入口。
- 评论区问题：你现在最想把哪一个低刺激动作交给 AI/Agent 接住？
`;
}

function writeArticle(topic) {
  if (existingArticle(topic.number)) return false;
  const fileName = `问题${String(topic.number).padStart(3, "0")}_${sanitize(topic.title.replace("？", "_"))}.md`;
  fs.writeFileSync(path.join(root, fileName), renderArticle(topic), "utf8");
  return true;
}

function main() {
  const allTopics = [...existingTopics, ...newTopics];
  fs.mkdirSync(path.dirname(poolPath), { recursive: true });
  fs.writeFileSync(poolPath, renderPool(allTopics), "utf8");
  const written = [];
  for (const topic of newTopics) {
    if (writeArticle(topic)) written.push(topic.number);
  }
  console.log(`Pool written: ${poolPath}`);
  console.log(`Generated articles: ${written.length}`);
  console.log(written.join(", "));
}

main();
