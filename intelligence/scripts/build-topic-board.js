const fs = require("fs");
const path = require("path");

const root = path.resolve(__dirname, "..");
const outDir = path.join(root, "docs", "topic-pools");
const qaCsvCandidates = [
  path.join(root, "delivery", "content_qa", "内容质检_001-220.csv"),
  path.join(root, "delivery", "content_qa", "内容质检_001-180.csv"),
  path.join(root, "delivery", "content_qa", "内容质检_001-108.csv"),
];
const qaCsvPath = qaCsvCandidates.find((file) => fs.existsSync(file)) || qaCsvCandidates[1];
const sourcePoolPath = path.join(outDir, "问题109-168_资料驱动选题增量.md");
const projectPoolPath = path.join(outDir, "问题181-220_项目治理与产品化选题增量.md");

function ensureDir(dir) {
  fs.mkdirSync(dir, { recursive: true });
}

function escapeHtml(value) {
  return String(value ?? "")
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;");
}

function escapeMdCell(value) {
  return String(value ?? "")
    .replace(/\r?\n/g, "<br>")
    .replace(/\|/g, "｜");
}

function csvEscape(value) {
  const text = String(value ?? "");
  if (/[",\n\r]/.test(text)) {
    return `"${text.replace(/"/g, '""')}"`;
  }
  return text;
}

function parseCsv(text) {
  text = text.replace(/^\uFEFF/, "");
  const rows = [];
  let row = [];
  let field = "";
  let inQuotes = false;

  for (let i = 0; i < text.length; i++) {
    const ch = text[i];
    const next = text[i + 1];

    if (inQuotes) {
      if (ch === '"' && next === '"') {
        field += '"';
        i++;
      } else if (ch === '"') {
        inQuotes = false;
      } else {
        field += ch;
      }
      continue;
    }

    if (ch === '"') {
      inQuotes = true;
    } else if (ch === ",") {
      row.push(field);
      field = "";
    } else if (ch === "\n") {
      row.push(field);
      rows.push(row);
      row = [];
      field = "";
    } else if (ch !== "\r") {
      field += ch;
    }
  }
  if (field.length || row.length) {
    row.push(field);
    rows.push(row);
  }

  const header = rows.shift() || [];
  return rows
    .filter((item) => item.some((cell) => cell.trim()))
    .map((item) => Object.fromEntries(header.map((key, index) => [key, item[index] ?? ""])));
}

function loadQaByNumber() {
  const qaRows = fs.existsSync(qaCsvPath) ? parseCsv(fs.readFileSync(qaCsvPath, "utf8")) : [];
  return new Map(qaRows.map((row) => [Number(row["选题"]), row]));
}

function firstExistingArticle(number) {
  const prefix = `问题${String(number).padStart(3, "0")}_`;
  return fs.readdirSync(root).find((name) => name.startsWith(prefix) && name.endsWith(".md"));
}

function titleFromFileName(fileName) {
  return fileName
    .replace(/^问题\d{3}_/, "")
    .replace(/\.md$/, "")
    .replace(/_/g, "｜");
}

function articleLink(fileName) {
  if (!fileName) return "";
  const base = fileName.replace(/\.md$/, "");
  const htmlName = `${base}.html`;
  const renderedPath = path.join(root, "delivery", "rendered_articles", htmlName);
  if (fs.existsSync(renderedPath)) {
    return `../../delivery/rendered_articles/${encodeURIComponent(htmlName)}`;
  }
  return `../../${encodeURIComponent(fileName)}`;
}

function priorityForExisting(number, title) {
  const s = new Set([62, 63, 64, 67, 74, 91, 92, 93, 94, 96, 97, 98]);
  const a = new Set([2, 5, 13, 16, 21, 31, 38, 47, 49, 50, 52, 58, 59, 61, 65, 66, 68, 71, 75, 77, 78, 79, 81, 82, 87]);
  if (s.has(number)) return "S";
  if (a.has(number)) return "A";
  if (number >= 99 && number <= 108) return "C";
  if (/法律|律师|法学生|实习律师/.test(title)) return "C";
  return "B";
}

function seriesForExisting(number, title) {
  if (number >= 99 && number <= 108) return "法律桥接";
  if (number >= 91 && number <= 98) return "现金流与产品化";
  if (/Agent|外部前额叶|工作流|Harness|Skill|AI/.test(title)) return "AI与外部执行系统";
  if (/多巴胺|情绪|抑郁|社交|伴侣|道歉|共情|羞耻|内疚|负罪/.test(title)) return "情绪与关系机制";
  if (/时间|睡眠|启动|拖延|待办|完成|打断|会议|截止|选择|整理|空间|仪式/.test(title)) return "执行功能机制";
  if (/投资|市场|做空|套利|现金流|变现|创业/.test(title)) return "市场与变现隐喻";
  if (/MoE|弱联系|创新|文明|过拟合|发散/.test(title)) return "高方差认知优势";
  return "ADHD基础叙事";
}

function techniqueForExisting(number, title, priority) {
  if (priority === "S") {
    if (/负罪|卸载|今日唯一动作|反馈|现金流|搭系统/.test(title)) {
      return "反常识开场 + 私人痛点场景 + 产品入口 + 评论区提问";
    }
    return "刺痛场景 + 强隐喻 + 三证据法 + 平台化结尾";
  }
  if (/哈希|蒙特卡洛|DDoS|LoRA|MoE|K线|栈指针|缓存|接口/.test(title)) {
    return "技术隐喻 + 生活场景对照 + 机制解释";
  }
  if (/律师|法学生|法律/.test(title)) {
    return "旧粉场景 + 高压职业痛点 + ADHD上游化桥接";
  }
  return "场景钩子 + 机制翻译 + 一个今天可执行动作";
}

function nextActionForExisting(number, priority, status) {
  if (number >= 99 && number <= 108) return "暂缓主线，只在旧粉迁移或高压职业专题中复用。";
  if (priority === "S") return "进入发布包：公众号长文、小红书痛点版、评论回流问题、产品入口。";
  if (priority === "A") return "做二轮编辑：补私人场景、压缩开头、加强落地动作。";
  return status === "已成稿" ? "保留为素材库，等待系列编排时再改写。" : "待补正文后再进入质检。";
}

function parsePoolTable(md) {
  const lines = md.split(/\r?\n/);
  const rows = [];
  for (const line of lines) {
    if (!line.startsWith("|")) continue;
    if (/^\|\s*-+/.test(line)) continue;
    if (/编号\s*\|/.test(line)) continue;
    const cells = line
      .slice(1, -1)
      .split("|")
      .map((cell) => cell.trim());
    if (cells.length < 6) continue;
    const num = Number(cells[0]);
    if (!Number.isFinite(num)) continue;
    rows.push({
      number: num,
      series: cells[1],
      title: cells[2],
      problem: cells[3],
      product: cells[4],
      priority: cells[5],
    });
  }
  return rows;
}

const titleUpgrades = {
  130: "为什么 ADHD 的超聚焦需要日志，而不是崇拜？你要记录它的入口、代价和坠落时间",
  133: "为什么 ADHD 的晚睡需要关机 SOP，而不是自责？你不是不睡，是系统没有收到降噪信号",
  135: "为什么 ADHD 完成一件事只爽几秒？因为你的大脑没有成就结算系统",
  153: "为什么 ADHD 不适合日更，但适合双周地图栏目？你不是流水线作者，而是周期性制图者",
};

const priorityUpgrades = {
  135: "S",
};

const problemUpgrades = {
  130: "痛点：把超聚焦当作可随时调用的超能力，结果透支、断电、反噬；需求：记录触发信号、持续时长、恢复成本；待办：建立超聚焦日志，区分值得追的信号和会掏空人的信号",
  133: "痛点：晚睡被道德化成懒和放纵；需求：用环境信号、屏幕降噪、任务封存替代训斥；待办：写一个低电量也能执行的晚间关机 SOP",
  135: "痛点：完成一件事只爽几秒，立刻被“还有好多没做”覆盖；需求：把已完成事项外部登记成安全感；待办：用 AI 每晚生成 done list 和成就回放，而不是继续追待办清单",
  153: "痛点：日更把 ADHD 的高压电容变成长期漏电；需求：有节律地制图，而不是每天挤牙膏；待办：设计双周地图栏目，平日只做短脉冲和素材回收",
};

const duplicationNotes = {
  118: "中：与099-108法律桥接重叠，但可承担旧粉迁移入口。",
  130: "高：原题与078重叠，已改为超聚焦日志和代价管理。",
  133: "中：与066睡眠相位延迟重叠，已改为晚间关机SOP。",
  135: "低：升级为成就盲视主炮题，和done list系统强相关。",
  141: "低：认知外包操作系统是新阶段总纲。",
  143: "低：可产品化为矩阵表，不是普通工具清单。",
  148: "中：承接062，但从文章升级为每日入口产品。",
  153: "中：承接094脉冲发布，升级为双周地图栏目。",
  161: "高：与099青年律师外部前额叶接近，暂缓。",
  162: "高：与100/107接近，暂缓。",
  163: "中：法律AI桥接，需从旧粉迁移角度使用。",
  164: "低：转型叙事刚需。",
  165: "中：承接064终身卸载，可面向高压职业人群。",
  166: "中：与105知识管理复杂化接近，但错题本角度可保留。",
  167: "低：旧粉迁移最强执行题。",
  168: "低：账号定位升级题。",
};

function statusForNew(number, priority) {
  if (number >= 161 && number <= 168 && ![164, 167, 168].includes(number)) return "法律桥接暂缓";
  if ([130, 133, 153].includes(number)) return "高重复已改写";
  if ([141, 143, 147, 148, 149, 150, 152].includes(number)) return "产品化续篇待写";
  if (priority === "S") return "新题待写（首发优先）";
  return "新题待写";
}

function techniqueForNew(number, series, title, priority) {
  if ([109, 111, 122, 141, 143, 148, 157, 159, 167].includes(number)) {
    return "反常识定调 + 地图式结构 + 产品入口 + 评论区需求采集";
  }
  if (series.includes("科学机制")) return "刺痛场景 + 机制命名 + 科学解释 + 自测动作";
  if (series.includes("AI内容生态")) return "行业观察 + 反模板判断 + 平台策略 + 案例拆解";
  if (series.includes("发布回流")) return "发布现场 + 数据回流 + SOP拆解 + 下一篇生成";
  if (series.includes("旧粉迁移")) return "旧粉真实处境 + 上游化解释 + 不道歉转型 + 当下救援动作";
  if (title.includes("制图")) return "身份宣言 + 地形图隐喻 + 读者坐标 + 栏目化";
  return priority === "S" ? "强钩子 + 机制翻译 + 产品化落点" : "生活场景 + 机制解释 + 小动作";
}

function nextActionForNew(number, status, priority) {
  if (status === "法律桥接暂缓") return "不抢主线；等旧法律粉迁移节点再写。";
  if (number === 135) return "优先成稿，并把 done list 日历作为证据和产品入口。";
  if (priority === "S") return "优先写正文，再直接做首发包和评论区问题。";
  if (status === "高重复已改写") return "按新角度写，避免复述旧题；正文开头必须说明与旧题的区别。";
  if (status.includes("产品化")) return "先写小红书痛点版，再补公众号框架版和模板入口。";
  return "进入待写池；等同系列首发验证后决定是否扩写。";
}

function duplicationForProjectTopic(number, series) {
  if ([181, 183, 184, 187, 191, 193, 196, 201, 207, 215, 220].includes(number)) {
    return "低：项目治理/产品化主线，负责把内容资产推向发布、回流和产品入口。";
  }
  if (series.includes("旧粉迁移")) return "中：与法律桥接题相关，但承担旧粉迁移和高压职业转译。";
  if (series.includes("选题治理")) return "低：治理题，约束无限扩题，避免把供料误判成推进。";
  return "低：系统层增量，补足发布、模板、证据、节律或现金流闭环。";
}

function techniqueForProjectTopic(series, priority) {
  if (priority === "S") return "系统判断开场 + 痛点场景 + 闭环拆解 + 产品入口 + 评论问题";
  if (series.includes("工具评测")) return "工具爽感反转 + 反噬场景 + 评分维度 + 退出条件";
  if (series.includes("旧粉迁移")) return "高压职业现场 + 认知负荷转译 + 旧粉救场入口";
  if (series.includes("现金流验证")) return "反馈信号分级 + 托付证据 + 人工服务验证";
  if (series.includes("选题治理")) return "反扩题判断 + 冻结/删除规则 + 看板化动作";
  if (series.includes("发布节律")) return "能量潮汐隐喻 + 双周节律 + 低能任务菜单";
  return "项目治理视角 + 三层机制 + 最小模板/入口落点";
}

function nextActionForProjectTopic(number, priority, product) {
  if (number === 181) return "做成发布包生成器模板，并优先服务 135 首发。";
  if (number === 183) return "建立评论需求库字段：共鸣、求助、模板、付费线索。";
  if (number === 184) return "为 135/169/148 各补一个可复制小模板。";
  if (number === 187) return "挑 10 个 S 级题建立正文-发布-回流-模板推进卡。";
  if (number === 193) return "生成 ADHD x AI 工具反噬评分表，作为固定栏目。";
  if (number === 201) return "把 091 做成今日唯一动作卡，作为第一个入口产品。";
  if (number === 215 || number === 220) return "作为账号/项目总纲，进入置顶文和路线图候选。";
  if (priority === "S") return `进入首发包或产品化冲刺，优先验证 ${product}。`;
  return "作为系统支线，等待首发回流后做二轮编辑和模板化。";
}

const extraTopics = [
  {
    number: 169,
    series: "成就盲视与回放系统",
    title: "为什么 ADHD 需要 done list，而不是更多待办？你的大脑缺的不是任务，是已完成证据",
    problem: "痛点：每天只看见没做完的事，做完的事立刻消失；需求：把完成线索变成可回看的证据库；待办：每日自动记录3条完成、1条推进、1条外部反馈",
    product: "小红书/公众号；产品入口：AI done list 日报",
    priority: "S",
  },
  {
    number: 170,
    series: "成就盲视与回放系统",
    title: "为什么 ADHD 的自尊需要证据墙？不是鸡血鼓励，而是可复查的完成记录",
    problem: "痛点：情绪低谷时会全盘否认过去一年；需求：建立能对抗低谷叙事的证据墙；待办：把完成日期、文件、截图、反馈做成月度墙",
    product: "公众号；产品入口：成就证据墙模板",
    priority: "A",
  },
  {
    number: 171,
    series: "成就盲视与回放系统",
    title: "为什么 ADHD 的复盘不能只问哪里没做好？你需要先让大脑看见已经做成了什么",
    problem: "痛点：复盘一开始就变成审判大会；需求：先结算完成，再讨论改进；待办：复盘模板第一栏固定写已完成资产",
    product: "小红书；产品入口：低羞耻复盘模板",
    priority: "A",
  },
  {
    number: 172,
    series: "成就盲视与回放系统",
    title: "为什么 ADHD 需要成就回放，而不是年终总结？年终总结太远，回放要按周发生",
    problem: "痛点：一年很长，但成就感的半衰期只有几秒；需求：缩短结算周期；待办：每周生成一次已完成时间线和下周唯一动作",
    product: "公众号/Newsletter；产品入口：AI周报模板",
    priority: "A",
  },
  {
    number: 173,
    series: "成就盲视与回放系统",
    title: "为什么 ADHD 的完成感需要外部见证？一个人偷偷做成，很快会被大脑删档",
    problem: "痛点：独自完成没有回声，成就感难以固化；需求：用社群、评论、同伴或Agent做见证；待办：每周公开一个小完成，而不是公开宏大计划",
    product: "小红书/社群；产品入口：完成见证群",
    priority: "A",
  },
  {
    number: 174,
    series: "成就盲视与回放系统",
    title: "为什么 ADHD 的文件夹也应该会夸你？项目状态页不是文档，是外部自尊系统",
    problem: "痛点：文件很多但用户感受不到自己真的推进了；需求：让项目状态页自动呈现已交付、已验证、下一步；待办：每个项目都保留一个状态台",
    product: "公众号；产品入口：项目状态台模板",
    priority: "A",
  },
  {
    number: 175,
    series: "反馈回流与现金流",
    title: "为什么 ADHD 的内容选题要问“谁会因此行动”？只让人点头的文章还没开始赚钱",
    problem: "痛点：共鸣很多但没有购买、咨询、投稿或评论；需求：每篇文章绑定一个行动信号；待办：为选题增加评论问题、模板下载、咨询入口之一",
    product: "公众号；产品入口：选题行动信号表",
    priority: "S",
  },
  {
    number: 176,
    series: "反馈回流与现金流",
    title: "为什么 ADHD 的爆款不一定值钱？真正值钱的是能暴露付费痛点的评论",
    problem: "痛点：被点赞数带偏，忽视能转产品的语言；需求：区分情绪共鸣和付费需求；待办：评论按共鸣、求助、模板需求、咨询线索四类标注",
    product: "公众号/小红书；产品入口：评论需求分类表",
    priority: "S",
  },
  {
    number: 177,
    series: "反馈回流与现金流",
    title: "为什么 ADHD 创作者要少写观点，多写入口？入口才会把读者带到下一步",
    problem: "痛点：观点很强但用户读完不知道做什么；需求：每篇有一个低摩擦入口；待办：结尾固定给一个可回复、可下载、可自测的入口",
    product: "全平台；产品入口：文章入口清单",
    priority: "A",
  },
  {
    number: 178,
    series: "旧粉迁移升级",
    title: "为什么旧法律粉丝不是要被说服，而是要被重新命名？他们的问题一直是认知负荷过载",
    problem: "痛点：旧粉不一定认同 ADHD 标签，却长期受高压任务和情绪后果折磨；需求：用认知负荷语言桥接，而不是强行科普ADHD；待办：写一篇高压职业认知负荷自测",
    product: "公众号；产品入口：高压职业认知负荷自测",
    priority: "A",
  },
  {
    number: 179,
    series: "旧粉迁移升级",
    title: "为什么从法律人成长到 ADHD x AI，不是逃离专业，而是看见了更底层的问题",
    problem: "痛点：转型容易被理解为放弃旧积累；需求：把法律经历解释成高压认知系统样本；待办：写一篇账号转型说明，不道歉，只给新地图",
    product: "公众号；产品入口：账号置顶文",
    priority: "A",
  },
  {
    number: 180,
    series: "内容宇宙治理",
    title: "为什么这个选题池不该再追求数量？下一阶段要让每个 S 级题目长出正文、发布包和产品入口",
    problem: "痛点：选题越多越爽，但发布和回流跟不上；需求：用分级治理替代无限扩题；待办：每周只推进1个S级题的正文、分发、回流和模板",
    product: "项目系统；产品入口：S级选题推进看板",
    priority: "S",
  },
];

function buildExistingTopics() {
  const qaByNumber = loadQaByNumber();
  const topics = [];

  for (let number = 1; number <= 108; number++) {
    const fileName = firstExistingArticle(number);
    const qa = qaByNumber.get(number) || {};
    const title = qa["题目"] || (fileName ? titleFromFileName(fileName) : "待补标题");
    const status = fileName ? "已成稿" : "待补正文";
    const priority = priorityForExisting(number, title);
    const series = seriesForExisting(number, title);
    topics.push({
      number,
      title,
      status: number >= 99 && number <= 108 ? "已成稿（法律桥接降级）" : status,
      series,
      priority,
      duplication: number >= 99 && number <= 108 ? "中：与当前主线有距离，只做桥接资产。" : "低：已有正文，可按系列编辑复用。",
      technique: techniqueForExisting(number, title, priority),
      problem: qa["解决的问题"] || "痛点/需求/待办待复核。",
      product: fileName ? "正文已渲染；可进入平台发布包。" : "需先补本地正文。",
      next: nextActionForExisting(number, priority, status),
      link: articleLink(fileName),
    });
  }
  return topics;
}

function buildNewTopics() {
  const sourceRows = fs.existsSync(sourcePoolPath) ? parsePoolTable(fs.readFileSync(sourcePoolPath, "utf8")) : [];
  const projectRows = fs.existsSync(projectPoolPath) ? parsePoolTable(fs.readFileSync(projectPoolPath, "utf8")) : [];
  const qaByNumber = loadQaByNumber();
  const topics = sourceRows.map((row) => {
    const title = titleUpgrades[row.number] || row.title;
    const problem = problemUpgrades[row.number] || row.problem;
    const priority = priorityUpgrades[row.number] || row.priority;
    const fileName = firstExistingArticle(row.number);
    const qa = qaByNumber.get(row.number) || {};
    const hasDraft = Boolean(fileName);
    const status = hasDraft ? (row.number >= 161 && row.number <= 168 ? "已成稿（法律桥接）" : "已成稿") : statusForNew(row.number, priority);
    return {
      number: row.number,
      title: hasDraft ? (qa["题目"] || title) : title,
      status,
      series: row.series,
      priority,
      duplication: duplicationNotes[row.number] || "低：资料驱动增量，和001-108没有直接同义复述。",
      technique: techniqueForNew(row.number, row.series, title, priority),
      problem: hasDraft ? (qa["解决的问题"] || problem) : problem,
      product: hasDraft ? "正文已渲染；可进入平台发布包。" : row.product,
      next: hasDraft ? (priority === "S" ? "进入发布包：公众号长文、小红书痛点版、评论回流问题、产品入口。" : "做二轮编辑：补私人场景、压缩开头、加强落地动作。") : nextActionForNew(row.number, status, priority),
      link: hasDraft ? articleLink(fileName) : "",
    };
  });

  const extras = extraTopics.map((row) => ({
    ...row,
    title: firstExistingArticle(row.number) ? ((qaByNumber.get(row.number) || {})["题目"] || row.title) : row.title,
    status: firstExistingArticle(row.number) ? "已成稿" : (row.priority === "S" ? "新增强题待写（首发优先）" : "新增强题待写"),
    duplication: row.number === 180 ? "低：治理题，约束选题膨胀。" : "低：从成就盲视和真实回流切入，是当前对话新信号。",
    technique: row.priority === "S"
      ? "刺痛原句开场 + 机制命名 + 产品入口 + 读者行动问题"
      : "个人场景 + 机制翻译 + 模板化落点",
    problem: firstExistingArticle(row.number) ? ((qaByNumber.get(row.number) || {})["解决的问题"] || row.problem) : row.problem,
    product: firstExistingArticle(row.number) ? "正文已渲染；可进入平台发布包。" : row.product,
    next: firstExistingArticle(row.number) ? (row.priority === "S" ? "进入发布包：公众号长文、小红书痛点版、评论回流问题、产品入口。" : "做二轮编辑：补私人场景、压缩开头、加强落地动作。") : (row.priority === "S"
      ? "优先写正文，直接接发布包或模板入口。"
      : "作为S级题的支线，等待首发反馈后扩写。"),
    link: firstExistingArticle(row.number) ? articleLink(firstExistingArticle(row.number)) : "",
  }));

  const projectTopics = projectRows.map((row) => {
    const fileName = firstExistingArticle(row.number);
    const qa = qaByNumber.get(row.number) || {};
    const hasDraft = Boolean(fileName);
    return {
      number: row.number,
      title: hasDraft ? (qa["题目"] || row.title) : row.title,
      status: hasDraft ? "已成稿" : (row.priority === "S" ? "项目治理待写（首发优先）" : "项目治理待写"),
      series: row.series,
      priority: row.priority,
      duplication: duplicationForProjectTopic(row.number, row.series),
      technique: techniqueForProjectTopic(row.series, row.priority),
      problem: hasDraft ? (qa["解决的问题"] || row.problem) : row.problem,
      product: hasDraft ? `正文已渲染；产品入口：${row.product}` : row.product,
      next: hasDraft ? nextActionForProjectTopic(row.number, row.priority, row.product) : "先补正文，再进入质检与发布包队列。",
      link: hasDraft ? articleLink(fileName) : "",
    };
  });

  return [...topics, ...extras, ...projectTopics];
}

function renderMarkdown(topics, generatedAt) {
  const summaryByStatus = groupCount(topics, "status");
  const summaryByPriority = groupCount(topics, "priority");
  const completed = topics.filter((item) => item.status.includes("已成稿")).length;
  const pending = topics.length - completed;
  const sTopics = topics.filter((item) => item.priority === "S");

  const lines = [];
  lines.push("# ADHD x AI 选题升级看板 001-220");
  lines.push("");
  lines.push(`生成时间：${generatedAt}`);
  lines.push("");
  lines.push("## 一句话判断");
  lines.push("");
  lines.push("现在不是继续堆标题的阶段，而是把 S 级题目变成“正文 -> 发布包 -> 评论回流 -> 产品入口”的闭环。001-220 已经形成完整内容资产，181-220 负责把文章库升级成发布包系统、评论需求库、模板入口、工具评测、旧粉迁移和认知外包 OS 路线图。");
  lines.push("");
  lines.push("## 总览");
  lines.push("");
  lines.push(`- 总选题：${topics.length} 个（001-220）`);
  lines.push(`- 已有本地正文：${completed} 个（001-220）`);
  lines.push(`- 待写/待验证：${pending} 个`);
  lines.push(`- S 级优先：${sTopics.length} 个`);
  lines.push(`- 状态分布：${summaryByStatus}`);
  lines.push(`- 优先级分布：${summaryByPriority}`);
  lines.push("");
  lines.push("## 最高优先级队列");
  lines.push("");
  lines.push("| 编号 | 题目 | 为什么优先 | 下一步 |");
  lines.push("|---:|---|---|---|");
  for (const item of sTopics) {
    lines.push(`| ${item.numberLabel} | ${escapeMdCell(item.title)} | ${escapeMdCell(item.problem)} | ${escapeMdCell(item.next)} |`);
  }
  lines.push("");
  lines.push("## 全量看板");
  lines.push("");
  lines.push("| 编号 | 状态 | 优先级 | 系列 | 题目 | 重复风险/改写判断 | 写作技法 | 真实痛点/需求/待办 | 产品/平台入口 | 下一步动作 | 正文 |");
  lines.push("|---:|---|---|---|---|---|---|---|---|---|---|");
  for (const item of topics) {
    const link = item.link ? `[打开](${item.link})` : "待写";
    lines.push(`| ${item.numberLabel} | ${escapeMdCell(item.status)} | ${item.priority} | ${escapeMdCell(item.series)} | ${escapeMdCell(item.title)} | ${escapeMdCell(item.duplication)} | ${escapeMdCell(item.technique)} | ${escapeMdCell(item.problem)} | ${escapeMdCell(item.product)} | ${escapeMdCell(item.next)} | ${link} |`);
  }
  lines.push("");
  lines.push("## 写作技法库");
  lines.push("");
  lines.push("- 反常识开场：先推翻读者熟悉的道德解释，比如“不是懒，是时间盲视”。");
  lines.push("- 私人刺痛场景：从具体崩溃瞬间开场，不从抽象概念开场。");
  lines.push("- 机制命名：给痛苦一个可传播的新名字，如成就盲视、负罪感焚烧炉、认知外包 OS。");
  lines.push("- 技术隐喻：把 ADHD 体验翻译成 DDoS、哈希表、蒙特卡洛、缓存、路由器，但必须落回生活。");
  lines.push("- 三证据法：生活场景、个人观察、理论/类比各给一个证据。");
  lines.push("- 产品化落点：每篇至少接一个模板、清单、SOP、入口或反馈问题。");
  lines.push("- 评论区提问：不要问“你是不是这样”，要问“你最想外包哪一个痛点/你愿意交给 AI 处理什么”。");
  lines.push("");
  lines.push("## 当前编辑原则");
  lines.push("");
  lines.push("1. 不再无目的扩题；只新增能接正文、回流或产品入口的题。");
  lines.push("2. 109-168 中重复题不删除，改写角度后保留，避免丢失素材资产。");
  lines.push("3. 099-108 和 161-168 法律线暂缓，但保留为旧粉迁移桥。");
  lines.push("4. 下一步最建议做 135 发布包：正文已经够多，真实回流比继续扩题更重要。");
  lines.push("5. 181、183、184、187、201 是当前最小闭环：发布包、评论回流、模板入口、S级推进、今日唯一动作。");
  lines.push("");
  return lines.join("\n");
}

function renderExtraTopicMarkdown(generatedAt) {
  const lines = [];
  lines.push("# 问题169-180 成就盲视与回流选题增量");
  lines.push("");
  lines.push(`生成时间：${generatedAt}`);
  lines.push("");
  lines.push("这组不是为了继续凑数量，而是把当前最真实的新信号接住：完成一件事只爽几秒，随后立刻被“还有好多没做”覆盖。这里的核心产品方向是 done list、证据墙、成就回放、评论需求分类和 S 级选题推进。");
  lines.push("");
  lines.push("| 编号 | 系列 | 选题 | 真实痛点 / 需求 / 待办 | 平台与产品入口 | 优先级 |");
  lines.push("|---:|---|---|---|---|---|");
  for (const item of extraTopics) {
    lines.push(`| ${item.number} | ${escapeMdCell(item.series)} | ${escapeMdCell(item.title)} | ${escapeMdCell(item.problem)} | ${escapeMdCell(item.product)} | ${item.priority} |`);
  }
  lines.push("");
  lines.push("## 写作建议");
  lines.push("");
  lines.push("1. 先写 `169`，因为它最直接承接用户的 done list 焦虑。");
  lines.push("2. `175`、`176` 不只是内容题，而是发布后 48 小时回流系统的规则。");
  lines.push("3. `180` 是选题治理题，提醒后续 Agent 不要把无限扩题伪装成推进。");
  lines.push("");
  return lines.join("\n");
}

function renderExtraTopicHtml(generatedAt) {
  const rows = extraTopics.map((item) => `<tr class="priority-${escapeHtml(item.priority)}">
    <td>${item.number}</td>
    <td>${escapeHtml(item.series)}</td>
    <td class="title">${escapeHtml(item.title)}</td>
    <td>${escapeHtml(item.problem)}</td>
    <td>${escapeHtml(item.product)}</td>
    <td class="priority">${escapeHtml(item.priority)}</td>
  </tr>`).join("\n");
  return `<!doctype html>
<html lang="zh-CN">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>问题169-180 成就盲视与回流选题增量</title>
  <style>
    body { margin:0; background:#f6f6f2; color:#1f2933; font-family:-apple-system,BlinkMacSystemFont,"Segoe UI","Microsoft YaHei",sans-serif; }
    main { max-width:1280px; margin:0 auto; padding:32px 24px 72px; }
    h1 { font-size:30px; margin:0 0 12px; }
    p, li { line-height:1.7; }
    table { width:100%; border-collapse:collapse; background:#fff; border:1px solid #ddd8cc; margin-top:18px; }
    th, td { border:1px solid #e4dfd4; padding:10px; vertical-align:top; line-height:1.55; }
    th { background:#ede9df; text-align:left; }
    tr:nth-child(even) td { background:#fbfaf6; }
    td:first-child { font-weight:800; white-space:nowrap; }
    .title { font-weight:700; }
    .priority { font-weight:800; text-align:center; color:#7a2e0e; }
    .note { background:#eef7f5; border:1px solid #c7ddd8; padding:14px 16px; border-radius:8px; margin:18px 0; }
  </style>
</head>
<body>
  <main>
    <h1>问题169-180 成就盲视与回流选题增量</h1>
    <p>生成时间：${escapeHtml(generatedAt)}</p>
    <div class="note">这组不是为了继续凑数量，而是把当前最真实的新信号接住：完成一件事只爽几秒，随后立刻被“还有好多没做”覆盖。</div>
    <table>
      <thead><tr><th>编号</th><th>系列</th><th>选题</th><th>真实痛点 / 需求 / 待办</th><th>平台与产品入口</th><th>优先级</th></tr></thead>
      <tbody>${rows}</tbody>
    </table>
    <h2>写作建议</h2>
    <ol>
      <li>先写 169，因为它最直接承接用户的 done list 焦虑。</li>
      <li>175、176 不只是内容题，而是发布后 48 小时回流系统的规则。</li>
      <li>180 是选题治理题，提醒后续 Agent 不要把无限扩题伪装成推进。</li>
    </ol>
  </main>
</body>
</html>`;
}

function renderHtml(topics, generatedAt) {
  const summary = {
    total: topics.length,
    completed: topics.filter((item) => item.status.includes("已成稿")).length,
    pending: topics.filter((item) => !item.status.includes("已成稿")).length,
    s: topics.filter((item) => item.priority === "S").length,
  };
  const statusChips = Object.entries(groupCountObject(topics, "status"))
    .map(([key, count]) => `<span class="chip">${escapeHtml(key)}：${count}</span>`)
    .join("");
  const priorityChips = Object.entries(groupCountObject(topics, "priority"))
    .map(([key, count]) => `<span class="chip priority-${escapeHtml(key)}">${escapeHtml(key)}：${count}</span>`)
    .join("");

  const rows = topics.map((item) => {
    const link = item.link ? `<a href="${escapeHtml(item.link)}">打开</a>` : `<span class="muted">待写</span>`;
    return `<tr class="priority-${escapeHtml(item.priority)}">
      <td class="num">${item.numberLabel}</td>
      <td>${escapeHtml(item.status)}</td>
      <td class="priority">${escapeHtml(item.priority)}</td>
      <td>${escapeHtml(item.series)}</td>
      <td class="title">${escapeHtml(item.title)}</td>
      <td>${escapeHtml(item.duplication)}</td>
      <td>${escapeHtml(item.technique)}</td>
      <td>${escapeHtml(item.problem)}</td>
      <td>${escapeHtml(item.product)}</td>
      <td>${escapeHtml(item.next)}</td>
      <td>${link}</td>
    </tr>`;
  }).join("\n");

  const sRows = topics.filter((item) => item.priority === "S").map((item) => {
    return `<tr>
      <td class="num">${item.numberLabel}</td>
      <td class="title">${escapeHtml(item.title)}</td>
      <td>${escapeHtml(item.problem)}</td>
      <td>${escapeHtml(item.next)}</td>
    </tr>`;
  }).join("\n");

  return `<!doctype html>
<html lang="zh-CN">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>ADHD x AI 选题升级看板 001-220</title>
  <style>
    :root { --bg:#f6f6f2; --ink:#1f2933; --muted:#667085; --line:#ddd8cc; --paper:#fffefa; --accent:#11615c; --s:#7a2e0e; --a:#6a4a00; --b:#475467; --c:#667085; }
    * { box-sizing: border-box; }
    body { margin:0; background:var(--bg); color:var(--ink); font-family:-apple-system,BlinkMacSystemFont,"Segoe UI","Microsoft YaHei",sans-serif; }
    header { padding:30px 28px 22px; border-bottom:1px solid var(--line); background:#fffefa; position:sticky; top:0; z-index:5; }
    h1 { margin:0 0 8px; font-size:28px; line-height:1.2; letter-spacing:0; }
    h2 { margin:30px 0 12px; font-size:20px; }
    p { line-height:1.72; margin:8px 0; }
    .wrap { max-width:1500px; margin:0 auto; padding:0 22px 64px; }
    .meta { color:var(--muted); }
    .summary { display:grid; grid-template-columns:repeat(4,minmax(120px,1fr)); gap:12px; margin:18px 0; }
    .card { background:var(--paper); border:1px solid var(--line); border-radius:8px; padding:14px; }
    .card b { display:block; font-size:26px; margin-bottom:4px; }
    .chips { display:flex; flex-wrap:wrap; gap:8px; margin:10px 0 0; }
    .chip { border:1px solid var(--line); background:#fff; border-radius:999px; padding:5px 10px; font-size:13px; color:#344054; }
    table { width:100%; border-collapse:collapse; background:#fff; border:1px solid var(--line); table-layout:fixed; }
    th, td { border:1px solid #e4dfd4; padding:9px 10px; vertical-align:top; word-break:break-word; line-height:1.55; }
    th { background:#ede9df; text-align:left; position:sticky; top:108px; z-index:4; }
    tbody tr:nth-child(even) td { background:#fbfaf6; }
    .num { width:64px; font-weight:800; white-space:nowrap; }
    .priority { width:52px; font-weight:800; text-align:center; }
    .title { font-weight:700; }
    .muted { color:var(--muted); }
    .priority-S .priority { color:var(--s); }
    .priority-A .priority { color:var(--a); }
    .priority-C { color:var(--c); }
    a { color:#0b66c3; text-decoration:none; font-weight:700; }
    a:hover { text-decoration:underline; }
    .note { background:#eef7f5; border:1px solid #c7ddd8; padding:14px 16px; border-radius:8px; margin:18px 0 24px; }
    .tools { display:grid; grid-template-columns:repeat(2,minmax(240px,1fr)); gap:12px; }
    .tools li { margin:6px 0; line-height:1.55; }
    @media (max-width:900px) {
      header { position:static; }
      th { position:static; }
      .summary, .tools { grid-template-columns:1fr; }
      table { font-size:13px; }
      th, td { padding:7px; }
    }
  </style>
</head>
<body>
  <header>
    <div class="wrap">
      <h1>ADHD x AI 选题升级看板 001-220</h1>
      <p class="meta">生成时间：${escapeHtml(generatedAt)}。这个看板用于判断写什么、怎么写、先发布什么、如何接产品和反馈。</p>
      <div class="chips">${statusChips}</div>
      <div class="chips">${priorityChips}</div>
    </div>
  </header>
  <main class="wrap">
    <section class="summary">
      <div class="card"><b>${summary.total}</b><span>总选题</span></div>
      <div class="card"><b>${summary.completed}</b><span>已有本地正文</span></div>
      <div class="card"><b>${summary.pending}</b><span>待写/待验证</span></div>
      <div class="card"><b>${summary.s}</b><span>S 级优先题</span></div>
    </section>
    <section class="note">
      <b>判断：</b> 001-220 已经完成本地正文和质检。现在不是继续堆标题，而是把 S 级题目变成“正文 -> 发布包 -> 评论回流 -> 产品入口”的闭环；181-220 是项目治理和产品化层。
    </section>
    <h2>S 级优先队列</h2>
    <table>
      <thead><tr><th>编号</th><th>题目</th><th>真实痛点/需求/待办</th><th>下一步</th></tr></thead>
      <tbody>${sRows}</tbody>
    </table>
    <h2>全量看板</h2>
    <table>
      <thead>
        <tr>
          <th>编号</th><th>状态</th><th>优先级</th><th>系列</th><th>题目</th><th>重复风险/改写判断</th><th>写作技法</th><th>真实痛点/需求/待办</th><th>产品/平台入口</th><th>下一步动作</th><th>正文</th>
        </tr>
      </thead>
      <tbody>${rows}</tbody>
    </table>
    <h2>写作技法库</h2>
    <ul class="tools">
      <li><b>反常识开场：</b>先推翻熟悉的道德解释，比如“不是懒，是时间盲视”。</li>
      <li><b>私人刺痛场景：</b>从一个具体崩溃瞬间开场，不从抽象概念开场。</li>
      <li><b>机制命名：</b>给痛苦一个可传播的新名字，如成就盲视、负罪感焚烧炉、认知外包 OS。</li>
      <li><b>技术隐喻：</b>用 DDoS、哈希表、蒙特卡洛、缓存、路由器解释，但必须落回生活。</li>
      <li><b>三证据法：</b>生活场景、个人观察、理论/类比各给一个证据。</li>
      <li><b>产品化落点：</b>每篇至少接一个模板、清单、SOP、入口或反馈问题。</li>
      <li><b>评论区提问：</b>不要问“你是不是这样”，要问“你最想外包哪一个痛点”。</li>
      <li><b>平台变形：</b>公众号讲框架证据，小红书讲痛点步骤，短视频讲前三秒刺痛。</li>
    </ul>
  </main>
</body>
</html>`;
}

function groupCountObject(items, key) {
  return items.reduce((acc, item) => {
    acc[item[key]] = (acc[item[key]] || 0) + 1;
    return acc;
  }, {});
}

function groupCount(items, key) {
  return Object.entries(groupCountObject(items, key))
    .map(([name, count]) => `${name} ${count}`)
    .join("；");
}

function renderCsv(topics) {
  const header = ["编号", "状态", "优先级", "系列", "题目", "重复风险/改写判断", "写作技法", "真实痛点/需求/待办", "产品/平台入口", "下一步动作", "正文链接"];
  const lines = [header.map(csvEscape).join(",")];
  for (const item of topics) {
    lines.push([
      item.numberLabel,
      item.status,
      item.priority,
      item.series,
      item.title,
      item.duplication,
      item.technique,
      item.problem,
      item.product,
      item.next,
      item.link,
    ].map(csvEscape).join(","));
  }
  return lines.join("\n");
}

function main() {
  ensureDir(outDir);
  const generatedAt = new Intl.DateTimeFormat("zh-CN", {
    timeZone: "Asia/Shanghai",
    year: "numeric",
    month: "2-digit",
    day: "2-digit",
    hour: "2-digit",
    minute: "2-digit",
    second: "2-digit",
    hour12: false,
  }).format(new Date()).replaceAll("/", "-");
  const topics = [...buildExistingTopics(), ...buildNewTopics()]
    .sort((a, b) => a.number - b.number)
    .map((item) => ({ ...item, numberLabel: String(item.number).padStart(3, "0") }));

  const mdPath = path.join(outDir, "ADHDxAI_选题升级看板_001-220.md");
  const htmlPath = path.join(outDir, "ADHDxAI_选题升级看板_001-220.html");
  const csvPath = path.join(outDir, "ADHDxAI_选题升级看板_001-220.csv");
  const extraMdPath = path.join(outDir, "问题169-180_成就盲视与回流选题增量.md");
  const extraHtmlPath = path.join(outDir, "问题169-180_成就盲视与回流选题增量.html");
  fs.writeFileSync(mdPath, renderMarkdown(topics, generatedAt), "utf8");
  fs.writeFileSync(htmlPath, renderHtml(topics, generatedAt), "utf8");
  fs.writeFileSync(csvPath, renderCsv(topics), "utf8");
  fs.writeFileSync(extraMdPath, renderExtraTopicMarkdown(generatedAt), "utf8");
  fs.writeFileSync(extraHtmlPath, renderExtraTopicHtml(generatedAt), "utf8");

  const statusSummary = groupCount(topics, "status");
  const prioritySummary = groupCount(topics, "priority");
  console.log("Topic board generated:");
  console.log(`  ${mdPath}`);
  console.log(`  ${htmlPath}`);
  console.log(`  ${csvPath}`);
  console.log(`  ${extraMdPath}`);
  console.log(`  ${extraHtmlPath}`);
  console.log(`Status: ${statusSummary}`);
  console.log(`Priority: ${prioritySummary}`);
}

main();
