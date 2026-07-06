const fs = require("fs");
const path = require("path");

const USER_HOME = "C:\\Users\\34587";
const PROJECT_ROOT = "C:\\Users\\34587\\Desktop\\选题池\\草稿";
const OUT_DIR = path.join(PROJECT_ROOT, "docs", "done-list");
const START = new Date(2025, 4, 17, 0, 0, 0);
const END = new Date(2026, 4, 17, 23, 59, 59);

const allowedExtensions = new Set([
  ".md", ".txt", ".html", ".htm", ".csv", ".json", ".jsonl", ".yaml", ".yml", ".toml",
  ".docx", ".doc", ".xlsx", ".xls", ".pptx", ".ppt", ".pdf",
  ".py", ".ps1", ".js", ".ts", ".tsx", ".jsx", ".css", ".scss", ".sql",
  ".zip", ".png", ".jpg", ".jpeg", ".webp", ".svg"
]);

const textExtensions = new Set([
  ".md", ".txt", ".html", ".htm", ".yaml", ".yml", ".toml",
  ".py", ".ps1", ".js", ".ts", ".tsx", ".jsx", ".css", ".scss", ".sql"
]);

const excludeDirNames = new Set([
  "AppData", "Application Data", "Local Settings", "Cookies", "Cache", "cache",
  "node_modules", ".git", "__pycache__", ".venv", "venv", "env", ".cache",
  ".chromium-browser-snapshots", ".agent-browser", ".browser-use", "npm-cache",
  "telemetry", "debug", "tmp", "plugins", "cache", "file-history", "computer-use-turn-ended",
  "generated_images", "browser", "ambient-suggestions", ".vscode", ".vscode-shared", ".copilot",
  ".config", ".cc-switch", ".qoder", ".qoderwork", ".openclaw", ".multica", ".hermes"
]);

const sensitiveNamePatterns = [
  /^auth\.json$/i,
  /^config\.json$/i,
  /^settings\.json$/i,
  /^cookies?$/i,
  /^login data$/i,
  /^local state$/i,
  /token/i,
  /credential/i,
  /password/i,
  /secret/i,
  /api[_-]?key/i,
  /\.pem$/i,
  /\.p12$/i,
  /\.key$/i,
  /\.sqlite$/i,
  /\.sqlite-(wal|shm)$/i,
  /\.db$/i
];

const sensitivePathPatterns = [
  /\\\.codex\\auth\.json$/i,
  /\\\.codex\\browser\\/i,
  /\\\.codex\\sqlite\\/i,
  /\\\.codex\\logs_2\.sqlite/i,
  /\\\.codex\\state_5\.sqlite/i,
  /\\\.claude\\telemetry\\/i,
  /\\\.claude\\debug\\/i,
  /\\\.cursor\\ai-tracking\\/i,
  /\\xwechat_files\\/i,
  /\\WeChat Files\\/i,
  /\\Tencent\\WeChat\\/i,
  /\\Google\\Chrome\\User Data\\/i,
  /\\Microsoft\\Edge\\User Data\\/i
];

const doneKeywords = [
  "完成", "生成", "创建", "整理", "修复", "交付", "上线", "发布包", "报告", "索引",
  "质检", "渲染", "已入库", "已生成", "已完成", "复检", "更新", "沉淀",
  "implemented", "created", "updated", "generated", "fixed", "delivered", "completed", "success"
];

const categoryRules = [
  { name: "ADHD x AI 内容宇宙", re: /(选题池|草稿|问题\d{3}|ADHD|双A|外部前额叶|多巴胺|反应堆|认知外包|Kimi_Agent|小红书|公众号|AIGC)/i },
  { name: "urban-research 城市更新", re: /(urban-research|洞头|锦州|马鞍山|市辖区研究|县域|城市更新|深度调研|候选项目|Word报告|ppt_prompt)/i },
  { name: "法律科技 / OSINT", re: /(法律|律师|法学生|合同|诉讼|执行|尽调|OSINT|consumer|lawsuit|qcc|tyc)/i },
  { name: "Agent / Skill / 自动化", re: /(agent|skill|mcp|自动化|scripts|git-sync|workflow|harness|codex|claude|cursor|插件|工作流)/i },
  { name: "交付台 / 报告资产", re: /(交付台|delivery|report|报告|汇报|发布包|html|docx|pptx|xlsx|可交付)/i },
  { name: "AI 创业 / 内容研究", re: /(AI博主|公众号|小红书|Kimi|创业|AIGC|Agentic|制图者|资料包|洞察)/i }
];

function ensureDir(dir) {
  fs.mkdirSync(dir, { recursive: true });
}

function localDate(date) {
  const y = date.getFullYear();
  const m = String(date.getMonth() + 1).padStart(2, "0");
  const d = String(date.getDate()).padStart(2, "0");
  return `${y}-${m}-${d}`;
}

function inRange(date) {
  return date >= START && date <= END;
}

function norm(p) {
  return p.replace(/\//g, "\\");
}

function shouldSkipPath(fullPath) {
  const p = norm(fullPath);
  if (shouldSkipInternalForFileScan(p)) return true;
  if (isSensitivePathOnly(p)) return true;
  return false;
}

function isSensitivePathOnly(fullPath) {
  const p = norm(fullPath);
  if (sensitivePathPatterns.some((re) => re.test(p))) return true;
  const base = path.basename(p);
  if (sensitiveNamePatterns.some((re) => re.test(base))) return true;
  return false;
}

function shouldSkipDir(fullPath) {
  if (shouldSkipInternalForFileScan(norm(fullPath) + "\\")) return true;
  const base = path.basename(fullPath);
  if (excludeDirNames.has(base)) return true;
  if (sensitivePathPatterns.some((re) => re.test(norm(fullPath) + "\\"))) return true;
  return false;
}

function shouldSkipInternalForFileScan(fullPath) {
  const p = norm(fullPath).toLowerCase();
  const home = norm(USER_HOME).toLowerCase();
  if (p.startsWith(`${home}\\.codex\\`)) {
    return !p.startsWith(`${home}\\.codex\\memories\\rollout_summaries\\`);
  }
  if (p.startsWith(`${home}\\.claude\\`)) {
    return !(
      p.startsWith(`${home}\\.claude\\memory\\`) ||
      p.startsWith(`${home}\\.claude\\plans\\`) ||
      p.startsWith(`${home}\\.claude\\scheduled-tasks\\`) ||
      p.startsWith(`${home}\\.claude\\skills\\`) ||
      p.endsWith(`${home}\\.claude\\claude.md`)
    );
  }
  if (p.startsWith(`${home}\\.cursor\\`)) {
    return !p.startsWith(`${home}\\.cursor\\skills-cursor\\`);
  }
  return false;
}

function allowedFile(fullPath) {
  const ext = path.extname(fullPath).toLowerCase();
  if (allowedExtensions.has(ext)) return true;
  if (/\\\.claude\\projects\\.*\.jsonl$/i.test(norm(fullPath))) return true;
  if (/\\\.codex\\sessions\\.*\.jsonl$/i.test(norm(fullPath))) return true;
  if (/\\\.codex\\archived_sessions\\.*\.jsonl$/i.test(norm(fullPath))) return true;
  if (/\\\.cursor\\projects\\.*agent-transcripts\\.*\.jsonl$/i.test(norm(fullPath))) return true;
  return false;
}

function relPath(fullPath) {
  if (norm(fullPath).toLowerCase().startsWith(norm(USER_HOME).toLowerCase())) {
    return fullPath.slice(USER_HOME.length + 1);
  }
  return fullPath;
}

function classify(fullPath) {
  const hay = `${relPath(fullPath)} ${path.basename(fullPath)}`;
  for (const rule of categoryRules) {
    if (rule.re.test(hay)) return rule.name;
  }
  return "其他";
}

function redact(text) {
  if (!text) return "";
  let s = String(text);
  s = s.replace(/(sk-[A-Za-z0-9_-]{12,})/g, "[REDACTED_API_KEY]");
  s = s.replace(/(Bearer\s+)[A-Za-z0-9._-]+/gi, "$1[REDACTED]");
  s = s.replace(/([A-Za-z0-9_]*token[A-Za-z0-9_]*\s*[:=]\s*)["']?[^"',\s}]+/gi, "$1[REDACTED]");
  s = s.replace(/([A-Za-z0-9_]*password[A-Za-z0-9_]*\s*[:=]\s*)["']?[^"',\s}]+/gi, "$1[REDACTED]");
  s = s.replace(/([A-Za-z0-9_]*secret[A-Za-z0-9_]*\s*[:=]\s*)["']?[^"',\s}]+/gi, "$1[REDACTED]");
  return s.replace(/\s+/g, " ").trim().slice(0, 260);
}

function extractSnippet(fullPath, stats) {
  const ext = path.extname(fullPath).toLowerCase();
  if (!textExtensions.has(ext)) return "";
  if (stats.size > 650 * 1024) return "";
  if (shouldSkipPath(fullPath)) return "";
  try {
    const raw = fs.readFileSync(fullPath, "utf8").slice(0, 70000);
    const lines = raw.split(/\r?\n/).map((x) => x.trim()).filter(Boolean);
    const headings = [];
    for (const line of lines) {
      let m = line.match(/^#{1,3}\s+(.{2,120})$/);
      if (m) headings.push(m[1]);
      m = line.match(/<title>([^<]{2,160})<\/title>/i);
      if (m) headings.push(m[1]);
      if (headings.length >= 3) break;
    }
    if (headings.length) return redact(headings.join("；"));
    return redact(lines.slice(0, 2).join("；"));
  } catch {
    return "";
  }
}

function scoreFile(fullPath, stats) {
  let score = 1;
  const rp = relPath(fullPath);
  if (/Desktop\\(交付台|当前项目|系统|选题池|Skill开发全历程|深度调研|.*研究)/.test(rp)) score += 4;
  if (/\.(md|html|docx|pptx|xlsx|csv)$/i.test(fullPath)) score += 2;
  if (/(README|PROJECT_STATUS|NEXT_ACTIONS|报告|汇报|发布包|质检|总览|索引|问题\d{3})/i.test(fullPath)) score += 3;
  if (/docs\\(source-synthesis|topic-pools|done-list)|sources\\kimi_agent|PROJECT_STATUS|README|NEXT_ACTIONS/i.test(rp)) score += 5;
  if (/(kimi_agent|问题109-168|学习汇报|资料总览|用户意图判断|done-list|全量阅读记录)/i.test(fullPath)) score += 6;
  if (stats.size > 0) score += 1;
  return score;
}

async function walk(dir, onFile, stats) {
  let entries;
  try {
    entries = await fs.promises.readdir(dir, { withFileTypes: true });
  } catch (err) {
    stats.skippedDirs++;
    return;
  }
  for (const entry of entries) {
    const full = path.join(dir, entry.name);
    if (entry.isDirectory()) {
      if (!shouldSkipDir(full)) await walk(full, onFile, stats);
      else stats.skippedDirs++;
      continue;
    }
    if (!entry.isFile()) continue;
    if (shouldSkipPath(full)) {
      stats.skippedFiles++;
      continue;
    }
    if (!allowedFile(full)) continue;
    await onFile(full);
  }
}

function pushEvent(days, event) {
  if (!event.date) return;
  if (!days[event.date]) {
    days[event.date] = { date: event.date, fileEvents: [], chatEvents: [], categories: {} };
  }
  if (event.kind === "chat") days[event.date].chatEvents.push(event);
  else days[event.date].fileEvents.push(event);
  days[event.date].categories[event.category] = (days[event.date].categories[event.category] || 0) + 1;
}

function maybeDate(value) {
  if (!value) return null;
  if (typeof value === "number") {
    const d = new Date(value > 20000000000 ? value : value * 1000);
    if (!Number.isNaN(d.getTime())) return d;
  }
  if (typeof value === "string") {
    const d = new Date(value);
    if (!Number.isNaN(d.getTime())) return d;
  }
  return null;
}

function findDateInObject(obj) {
  if (!obj || typeof obj !== "object") return null;
  const keys = ["timestamp", "created_at", "createdAt", "time", "date", "ts", "started_at"];
  for (const key of keys) {
    if (Object.prototype.hasOwnProperty.call(obj, key)) {
      const d = maybeDate(obj[key]);
      if (d) return d;
    }
  }
  for (const value of Object.values(obj).slice(0, 20)) {
    if (value && typeof value === "object") {
      const d = findDateInObject(value);
      if (d) return d;
    }
  }
  return null;
}

function extractTextFromObject(obj, depth = 0) {
  if (!obj || depth > 5) return "";
  if (typeof obj === "string") return obj;
  if (Array.isArray(obj)) return obj.map((x) => extractTextFromObject(x, depth + 1)).filter(Boolean).join(" ");
  if (typeof obj !== "object") return "";
  const chunks = [];
  for (const key of ["summary", "title", "prompt", "message", "content", "text", "input", "output", "final", "body"]) {
    if (Object.prototype.hasOwnProperty.call(obj, key)) {
      const t = extractTextFromObject(obj[key], depth + 1);
      if (t) chunks.push(t);
    }
  }
  if (!chunks.length) {
    for (const value of Object.values(obj).slice(0, 12)) {
      const t = extractTextFromObject(value, depth + 1);
      if (t) chunks.push(t);
      if (chunks.join(" ").length > 1200) break;
    }
  }
  return chunks.join(" ");
}

function parseChatFile(fullPath, stats, days) {
  if (shouldSkipPath(fullPath)) return;
  let fileStats;
  try {
    fileStats = fs.statSync(fullPath);
  } catch {
    return;
  }
  if (!inRange(fileStats.mtime) && !inRange(fileStats.birthtime)) return;
  let raw;
  try {
    raw = fs.readFileSync(fullPath, "utf8");
  } catch {
    return;
  }
  const lines = raw.split(/\r?\n/).filter(Boolean);
  let hits = 0;
  for (const line of lines) {
    if (hits >= 18) break;
    let obj = null;
    try { obj = JSON.parse(line); } catch {}
    const d = obj ? findDateInObject(obj) : null;
    const eventDate = d && inRange(d) ? localDate(d) : localDate(fileStats.mtime);
    const text = obj ? extractTextFromObject(obj) : line;
    if (!text || !doneKeywords.some((kw) => text.toLowerCase().includes(kw.toLowerCase()))) continue;
    const safe = redact(text);
    if (!safe || safe.length < 10) continue;
    if (isChatNoise(safe)) continue;
    pushEvent(days, {
      kind: "chat",
      date: eventDate,
      category: classify(fullPath),
      source: relPath(fullPath),
      summary: safe,
      score: 3
    });
    hits++;
    stats.chatHits++;
  }
}

function isChatNoise(text) {
  return /^(thinking|session_meta|response_item|tool_call|tool_result|web search results|total \d+)/i.test(text) ||
    /AGENTS\.md instructions/i.test(text) ||
    /Filesystem sandboxing/i.test(text) ||
    /You are Codex/i.test(text) ||
    /<permissions instructions>/i.test(text) ||
    /autopilot: 自动驾驶协作模式/i.test(text) ||
    /Use for:/i.test(text) ||
    /MCP servers?/i.test(text);
}

function collectChatFiles() {
  const roots = [
    path.join(USER_HOME, ".claude", "history.jsonl"),
    path.join(USER_HOME, ".claude", "projects"),
    path.join(USER_HOME, ".codex", "sessions"),
    path.join(USER_HOME, ".codex", "archived_sessions"),
    path.join(USER_HOME, ".codex", "memories", "rollout_summaries"),
    path.join(USER_HOME, ".cursor", "projects"),
    path.join(USER_HOME, "Desktop", ".claude-sessions")
  ];
  const out = [];
  function rec(p) {
    if (isSensitivePathOnly(p)) return;
    let st;
    try { st = fs.statSync(p); } catch { return; }
    if (st.isDirectory()) {
      if (shouldSkipChatDir(p)) return;
      let entries = [];
      try { entries = fs.readdirSync(p, { withFileTypes: true }); } catch { return; }
      for (const e of entries) rec(path.join(p, e.name));
      return;
    }
    if (st.isFile() && /\.(jsonl|md|txt)$/i.test(p)) out.push(p);
  }
  for (const root of roots) rec(root);
  return Array.from(new Set(out));
}

function shouldSkipChatDir(fullPath) {
  const base = path.basename(fullPath);
  if (["telemetry", "debug", "cache", "file-history", "plugins", "tmp", "browser", "generated_images", "computer-use-turn-ended"].includes(base)) return true;
  if (sensitivePathPatterns.some((re) => re.test(norm(fullPath) + "\\"))) return true;
  return false;
}

function fileEventLabel(event) {
  const action = event.created ? "新增" : "修改";
  const snippet = event.snippet ? `：${event.snippet}` : "";
  return `${action} ${event.name}${snippet}`;
}

function makeDoneItems(day) {
  const items = [];
  const byCat = {};
  for (const ev of day.fileEvents) {
    if (!byCat[ev.category]) byCat[ev.category] = [];
    byCat[ev.category].push(ev);
  }
  for (const [cat, events] of Object.entries(byCat)) {
    events.sort((a, b) => b.score - a.score);
    const top = events.slice(0, 4).map(fileEventLabel);
    const more = events.length > top.length ? ` 等 ${events.length} 个文件` : "";
    items.push({ category: cat, text: `${cat}：${top.join("；")}${more}` });
  }
  const chats = day.chatEvents.sort((a, b) => b.score - a.score).slice(0, 4);
  for (const chat of chats) {
    items.push({ category: chat.category, text: `会话推进：${chat.summary}` });
  }
  if (!items.length) return [];
  return items.slice(0, 8);
}

function htmlEscape(s) {
  return String(s || "")
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;");
}

function monthKey(date) {
  return `${date.getFullYear()}-${String(date.getMonth() + 1).padStart(2, "0")}`;
}

function addDays(date, n) {
  const d = new Date(date);
  d.setDate(d.getDate() + n);
  return d;
}

function renderHtml(days, stats) {
  const allDates = [];
  for (let d = new Date(START); d <= END; d = addDays(d, 1)) allDates.push(new Date(d));
  const monthGroups = {};
  for (const d of allDates) {
    const key = monthKey(d);
    if (!monthGroups[key]) monthGroups[key] = [];
    monthGroups[key].push(d);
  }
  const dayValues = Object.values(days);
  const activeDays = dayValues.filter((d) => d.items && d.items.length).length;
  const emptyDays = allDates.length - activeDays;
  const topCategories = {};
  for (const day of dayValues) {
    for (const [cat, count] of Object.entries(day.categories)) topCategories[cat] = (topCategories[cat] || 0) + count;
  }
  const cats = Object.entries(topCategories).sort((a, b) => b[1] - a[1]).slice(0, 8);
  const coverageRows = Object.entries(monthGroups).map(([key, dates]) => {
    let active = 0;
    let files = 0;
    let chats = 0;
    for (const d of dates) {
      const k = localDate(d);
      const day = days[k];
      if (day && day.items && day.items.length) {
        active++;
        files += day.fileEvents.length;
        chats += day.chatEvents.length;
      }
    }
    return `<tr><td>${htmlEscape(key)}</td><td>${dates.length}</td><td>${active}</td><td>${dates.length - active}</td><td>${files}</td><td>${chats}</td></tr>`;
  }).join("");
  const monthSections = Object.entries(monthGroups).map(([key, dates]) => {
    const [y, m] = key.split("-");
    const first = dates[0];
    const offset = (first.getDay() + 6) % 7;
    const blanks = Array.from({ length: offset }, () => "<div class=\"day blank\"></div>").join("");
    const cells = dates.map((d) => {
      const k = localDate(d);
      const day = days[k] || { items: [], fileEvents: [], chatEvents: [] };
      const count = day.fileEvents.length + day.chatEvents.length;
      const items = (day.items || []).slice(0, 5).map((it) => `<li>${htmlEscape(it.text)}</li>`).join("");
      const cls = count ? "day active" : "day";
      return `<article class="${cls}" id="d-${k}">
        <div class="date"><span>${d.getDate()}</span><b>${count || ""}</b></div>
        ${items ? `<ul>${items}</ul>` : "<p class=\"empty\">无明确完成线索</p>"}
      </article>`;
    }).join("");
    return `<section class="month">
      <h2>${y}年${Number(m)}月</h2>
      <div class="weekdays"><span>一</span><span>二</span><span>三</span><span>四</span><span>五</span><span>六</span><span>日</span></div>
      <div class="calendar">${blanks}${cells}</div>
    </section>`;
  }).join("\n");

  const catHtml = cats.map(([cat, count]) => `<span>${htmlEscape(cat)}：${count}</span>`).join("");
  const css = `
body{margin:0;background:#f6f4ef;color:#202124;font-family:-apple-system,BlinkMacSystemFont,"Segoe UI","Microsoft YaHei",sans-serif;letter-spacing:0}.wrap{max-width:1440px;margin:0 auto;padding:28px 18px 80px}header{border-bottom:2px solid #d8d2c5;padding-bottom:18px;margin-bottom:20px}h1{font-size:34px;margin:0 0 10px;line-height:1.18}.sub{color:#62666c;line-height:1.7;max-width:980px}.stats{display:flex;gap:10px;flex-wrap:wrap;margin-top:16px}.stats span,.cats span{border:1px solid #d8d2c5;background:#fffdf8;border-radius:6px;padding:7px 10px;font-size:13px}.cats{display:flex;gap:8px;flex-wrap:wrap;margin:12px 0 22px}.notice{background:#fffdf8;border:1px solid #d8d2c5;border-left:5px solid #265f7c;border-radius:8px;padding:12px 14px;line-height:1.7;margin:18px 0}.warning{background:#fff7f2;border:1px solid #e4c4b8;border-left:5px solid #9a3f31;border-radius:8px;padding:12px 14px;line-height:1.7;margin:18px 0}table{border-collapse:collapse;width:100%;background:#fffdf8;border:1px solid #d8d2c5;margin:10px 0 20px}th,td{border:1px solid #d8d2c5;padding:8px 10px;text-align:left;font-size:13px}th{background:#ece7dd}.month{margin-top:28px}.month h2{font-size:23px;margin:0 0 10px}.weekdays{display:grid;grid-template-columns:repeat(7,1fr);gap:8px;margin-bottom:8px}.weekdays span{font-weight:700;color:#6b6257;text-align:center}.calendar{display:grid;grid-template-columns:repeat(7,minmax(0,1fr));gap:8px}.day{min-height:124px;background:#faf8f2;border:1px solid #ddd6c9;border-radius:8px;padding:8px;overflow:hidden}.day.active{background:#fffdf8;border-color:#c6bda9;box-shadow:0 1px 0 rgba(0,0,0,.04)}.day.blank{background:transparent;border:0}.date{display:flex;justify-content:space-between;align-items:center;margin-bottom:6px}.date span{font-weight:800}.date b{font-size:12px;color:#8a5a18}.day ul{margin:0;padding-left:17px}.day li{font-size:12px;line-height:1.45;margin:4px 0}.empty{font-size:12px;color:#aaa;margin:8px 0 0}.links a{color:#265f7c;text-decoration:none;border-bottom:1px solid rgba(38,95,124,.35)}@media(max-width:980px){.calendar,.weekdays{grid-template-columns:1fr}.day.blank,.weekdays{display:none}.day{min-height:auto}h1{font-size:28px}table{display:block;overflow-x:auto}}`;
  return `<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>过去一年 Done List 日历</title><style>${css}</style></head><body><main class="wrap">
<header><h1>过去一年 Done List 日历</h1><p class="sub">基于本机文件时间线、项目文档、Claude/Codex/Cursor 本地会话文本线索生成。它不是审计报告，而是给 ADHD 大脑看的“成就回放系统”：把已经落地的东西重新登记成可见证据。</p><div class="stats"><span>范围：${localDate(START)} 至 ${localDate(END)}</span><span>扫描文件：${stats.filesSeen}</span><span>记录文件事件：${stats.fileEvents}</span><span>会话命中：${stats.chatHits}</span><span>有本地完成证据日期：${activeDays}</span><span>无本地完成证据日期：${emptyDays}</span></div></header>
<div class="notice"><strong>安全边界：</strong>本次主动跳过 auth/token/password/secret/API key、SQLite/数据库、浏览器用户数据、微信认证/数据目录、缓存与临时目录。页面只展示脱敏后的文件名、标题和会话摘要，不输出凭据或认证内容。</div>
<div class="warning"><strong>口径说明：</strong>“无本地完成证据”不等于当天没有工作、没有思考、没有阅读或没有聊天。它只表示：在当前这台电脑、当前可读取且未被安全规则排除的数据里，没有找到足够明确的本地文件产出或可解析会话完成线索。很多真实完成项可能留在云端、手机、微信/浏览器会话、外部平台，或在拷贝/解压后丢失了原始日期。</div>
<section><h2>高频完成领域</h2><div class="cats">${catHtml}</div></section>
<section><h2>月度证据覆盖</h2><table><thead><tr><th>月份</th><th>日历天数</th><th>有本地证据</th><th>无本地证据</th><th>文件线索</th><th>会话线索</th></tr></thead><tbody>${coverageRows}</tbody></table></section>
${monthSections}
<section class="links"><h2>机器可读文件</h2><p><a href="./done-list-2025-05-17_to_2026-05-17.json">JSON 明细</a> · <a href="./done-list-2025-05-17_to_2026-05-17.csv">CSV 明细</a></p></section>
</main></body></html>`;
}

function renderCsv(days) {
  const rows = [["date", "category", "item", "file_events", "chat_events"]];
  for (const date of Object.keys(days).sort()) {
    const day = days[date];
    const items = day.items && day.items.length ? day.items : [{ category: "", text: "" }];
    for (const item of items) {
      rows.push([date, item.category || "", item.text || "", day.fileEvents.length, day.chatEvents.length]);
    }
  }
  return rows.map((row) => row.map((cell) => `"${String(cell).replace(/"/g, '""')}"`).join(",")).join("\n");
}

async function main() {
  ensureDir(OUT_DIR);
  const days = {};
  const stats = { filesSeen: 0, fileEvents: 0, chatHits: 0, skippedDirs: 0, skippedFiles: 0 };
  await walk(USER_HOME, async (fullPath) => {
    stats.filesSeen++;
    let st;
    try { st = fs.statSync(fullPath); } catch { return; }
    const eventDateObj = inRange(st.mtime) ? st.mtime : (inRange(st.birthtime) ? st.birthtime : null);
    if (!eventDateObj) return;
    const date = localDate(eventDateObj);
    const created = Math.abs(st.birthtime.getTime() - st.mtime.getTime()) < 3600 * 1000 || localDate(st.birthtime) === date;
    const ev = {
      kind: "file",
      date,
      category: classify(fullPath),
      path: relPath(fullPath),
      name: path.basename(fullPath),
      created,
      size: st.size,
      mtime: st.mtime.toISOString(),
      birthtime: st.birthtime.toISOString(),
      snippet: extractSnippet(fullPath, st),
      score: scoreFile(fullPath, st)
    };
    pushEvent(days, ev);
    stats.fileEvents++;
  }, stats);

  for (const file of collectChatFiles()) parseChatFile(file, stats, days);

  for (const day of Object.values(days)) {
    day.fileEvents.sort((a, b) => b.score - a.score || b.size - a.size);
    day.chatEvents.sort((a, b) => b.score - a.score);
    day.fileEvents = day.fileEvents.slice(0, 35);
    day.chatEvents = day.chatEvents.slice(0, 12);
    day.items = makeDoneItems(day);
  }

  const ordered = {};
  for (const date of Object.keys(days).sort()) ordered[date] = days[date];
  const base = "done-list-2025-05-17_to_2026-05-17";
  fs.writeFileSync(path.join(OUT_DIR, `${base}.json`), JSON.stringify({ generatedAt: new Date().toISOString(), start: localDate(START), end: localDate(END), stats, days: ordered }, null, 2), "utf8");
  fs.writeFileSync(path.join(OUT_DIR, `${base}.csv`), "\ufeff" + renderCsv(ordered), "utf8");
  fs.writeFileSync(path.join(OUT_DIR, `${base}.html`), renderHtml(ordered, stats), "utf8");
  console.log(JSON.stringify({ outDir: OUT_DIR, stats, html: path.join(OUT_DIR, `${base}.html`) }, null, 2));
}

main().catch((err) => {
  console.error(err && err.stack ? err.stack : err);
  process.exit(1);
});
