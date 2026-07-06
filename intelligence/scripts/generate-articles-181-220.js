const fs = require("fs");
const path = require("path");

const root = path.resolve(__dirname, "..");
const sourcePath = path.join(root, "docs", "topic-pools", "问题181-220_项目治理与产品化选题增量.md");

function parsePoolTable(markdown) {
  const rows = [];
  for (const line of markdown.split(/\r?\n/)) {
    if (!line.startsWith("|")) continue;
    if (/^\|\s*-+/.test(line)) continue;
    if (/编号\s*\|/.test(line)) continue;
    const cells = line
      .slice(1, -1)
      .split("|")
      .map((cell) => cell.trim());
    if (cells.length < 6) continue;
    const number = Number(cells[0]);
    if (!Number.isFinite(number)) continue;
    rows.push({
      number,
      series: cells[1],
      title: cells[2],
      problem: cells[3],
      product: cells[4],
      priority: cells[5],
    });
  }
  return rows.filter((row) => row.number >= 181 && row.number <= 220);
}

function splitProblem(text) {
  const pain = (text.match(/痛点：([^；]+)/) || [])[1] || "痛点还没有被清楚命名";
  const need = (text.match(/需求：([^；]+)/) || [])[1] || "需要把它压成一个可执行系统";
  const todo = (text.match(/待办：(.+)$/) || [])[1] || "今天先写出一个最小动作";
  return { pain, need, todo };
}

function splitProduct(text) {
  const [platformPart, productPart] = text.split("；产品入口：");
  return {
    platform: platformPart || "公众号/小红书",
    product: productPart || text || "最小模板入口",
  };
}

function splitTitle(title) {
  const [main, ...rest] = title.split("？");
  const subtitle = rest.join("？").trim();
  return {
    main: main.trim() + (title.includes("？") ? "？" : ""),
    subtitle,
  };
}

function sanitizeFilePart(value) {
  return value
    .replace(/[<>:"/\\|?*]/g, "")
    .replace(/[，。！？、；：”“’‘（）《》【】「」]/g, "")
    .replace(/\s+/g, "")
    .replace(/x/g, "x")
    .slice(0, 68);
}

function existingArticle(number) {
  const prefix = `问题${String(number).padStart(3, "0")}_`;
  return fs.readdirSync(root).find((name) => name.startsWith(prefix) && name.endsWith(".md"));
}

const profiles = {
  发布包系统: {
    axes: ["任务结束错觉", "平台语境转换", "发布后回流责任"],
    identity: "发布包不是附属品，而是正文接入现实世界的接口层。",
    evidence: "同一篇长文，在公众号里需要框架，在小红书里需要痛点步骤，在评论区里需要一个能让读者开口的问题。",
  },
  评论回流: {
    axes: ["情绪信号被浪费", "需求语言未编码", "反馈没有回写进选题池"],
    identity: "评论不是热闹，评论是读者把未命名需求递到你手里。",
    evidence: "真正有价值的评论通常不是夸你写得好，而是说自己卡在哪里、试过什么、愿意交给谁处理。",
  },
  模板入口: {
    axes: ["共鸣后的行动断崖", "复制成本决定转化", "模板让外部前额叶落地"],
    identity: "模板是文章最小的产品形态，也是读者第一次把你带回现实的方式。",
    evidence: "ADHD 读者读完一篇文章最需要的不是再懂一点，而是立刻少背一点。",
  },
  内容治理: {
    axes: ["新选题多巴胺", "优先级稀释", "冻结权比扩张权更重要"],
    identity: "内容治理不是压制灵感，而是给高方差系统装调度器。",
    evidence: "越是选题多的项目，越需要敢于暂停、冻结和排序。",
  },
  S级推进: {
    axes: ["最高势能浪费", "闭环缺口", "产品入口缺席"],
    identity: "S 级题不是写完就结束，而是必须被榨成发布包、评论问题和产品入口。",
    evidence: "一个真正的主炮题，至少应该在四个地方出现：正文、平台、评论区、模板。",
  },
  反模板化: {
    axes: ["AI 顺滑化", "痛感位置被磨平", "私人证据消失"],
    identity: "ADHD 文章的价值不在正确，而在它能不能保留真实带电的位置。",
    evidence: "最能击中人的段落，往往不是概念解释，而是作者承认自己也在那里摔过。",
  },
  证据系统: {
    axes: ["科学证据太远", "生活证据太散", "产品证据没有沉淀"],
    identity: "证据系统要同时让读者相信、让作者复用、让产品可验证。",
    evidence: "论文证明机制，生活证明真实，产品证明这件事可以被改变。",
  },
  读者坐标: {
    axes: ["共鸣过度聚集", "卡点没有坐标", "社群缺少沉淀结构"],
    identity: "社群真正要建的不是聊天池，而是一张读者困境地图。",
    evidence: "一句我也是只能证明共鸣，一个具体卡点才能生成产品。",
  },
  工具评测: {
    axes: ["初始爽感误导", "整理欲反噬", "断电模式缺席"],
    identity: "ADHD x AI 工具测评要先问怎么救人，也要问什么时候会害人。",
    evidence: "一个工具刚用时越爽，越要检查它会不会制造新依赖、新沉迷和新羞耻。",
  },
  旧粉迁移: {
    axes: ["标签接受门槛", "高压职业样本", "旧经验上游化"],
    identity: "旧粉迁移不是解释你为什么转型，而是先解决他们当下的认知负荷。",
    evidence: "法律人不一定认同 ADHD 标签，但他们一定懂任务、风险、客户和截止日期同时排队的崩溃。",
  },
  产品入口: {
    axes: ["宏大愿望过载", "最小交付缺失", "可复用模板不足"],
    identity: "ADHD 产品的第一形态不该是大系统，而是一个当天就能减负的小入口。",
    evidence: "读者第一次愿意使用你的东西，往往不是因为它宏大，而是因为它今天就能少背一点。",
  },
  内容资产: {
    axes: ["文章仓库化", "入口路径缺失", "二次变形没有记录"],
    identity: "内容资产不是文章数量，而是读者能否从正确入口找到正确工具。",
    evidence: "一百篇文章如果没有地图，对新读者就是一百扇不知道通向哪里的门。",
  },
  现金流验证: {
    axes: ["点赞信号失真", "托付信号稀缺", "人工服务先于自动化"],
    identity: "现金流验证要先听见真实托付，而不是被泛流量哄高兴。",
    evidence: "有人愿意把资料发给你、把问题交给你、把钱付给你，比一百个赞更接近产品需求。",
  },
  发布节律: {
    axes: ["日更幻觉", "能量潮汐", "低能任务菜单"],
    identity: "ADHD 创作者需要节律，不需要每天把自己当稳定工厂。",
    evidence: "高能周适合写作冲刺，低能周适合搬运证据、整理评论和复用旧资产。",
  },
  研究供料: {
    axes: ["资料沉睡", "证据复用困难", "矿脉没有开采流程"],
    identity: "研究资料不是仓库，而是下一批选题、证据和产品判断的矿脉。",
    evidence: "一份好报告至少应该被拆成选题、案例、证据、图表和行动建议。",
  },
  人设与信任: {
    axes: ["完美人设失真", "失控记录缺席", "同行感比导师感更重要"],
    identity: "ADHD 创作者的信任来自可验证的修复过程，不来自完美姿态。",
    evidence: "读者不一定需要你站在山顶教他自律，他更需要看见你也在修系统。",
  },
  账号定位: {
    axes: ["标签容易被模仿", "底层主线未提炼", "旧资产没有统一解释"],
    identity: "账号护城河不是 ADHD 或 AI 两个词，而是高方差大脑如何外接现实。",
    evidence: "法律、投资、Agent、ADHD 和内容系统其实都在回答同一个问题：判断如何接入执行。",
  },
  选题治理: {
    axes: ["扩题伪装推进", "删除权缺失", "产品入口断裂"],
    identity: "选题治理的关键不是继续长大，而是让系统敢排序、敢暂停、敢删除。",
    evidence: "一个不能删除、不能冻结、不能降级的选题池，很快会变成新的认知负债。",
  },
  项目总纲: {
    axes: ["文章库误判", "反馈系统缺席", "认知外包 OS 尚未成型"],
    identity: "这个项目真正要开发的不是文章库，而是一套 ADHD x AI 的认知外包操作系统。",
    evidence: "文章是训练数据，模板是接口，反馈是传感器，社群是坐标库，Agent 是外部执行层。",
  },
};

const comments = {
  181: "你最常卡在发布包里的哪一步：标题、小红书、评论问题，还是模板入口？",
  183: "你最希望评论区被整理成哪一种需求库：共鸣、求助、模板，还是付费线索？",
  184: "你读完文章后最想直接复制哪一种小模板？",
  187: "你最想先看哪个 S 级题目跑完整个闭环？",
  191: "如果建读者坐标库，你愿意先留下哪个卡点坐标？",
  193: "你用过哪个 AI 工具一开始很爽，后来开始反噬？",
  196: "你在法律或高压职业里最重的认知负荷是什么？",
  201: "如果今天只能保留一个动作，你最该保留哪一个？",
  207: "你有没有愿意交给别人整理、但一直没人接住的资料？",
  215: "你觉得自己的高方差大脑最难接入现实的地方是什么？",
  220: "如果把这个项目做成认知外包 OS，你最想先拥有哪个模块？",
};

function firstSentence(text) {
  return text.split(/[。；]/)[0].trim();
}

function makeHook(topic, parts, productInfo) {
  const { number, series } = topic;
  const pain = parts.pain;
  const product = productInfo.product;
  const openings = {
    发布包系统: `你有没有这种体验：正文终于写完了，人也已经空了。可真正要发出去的时候，标题、小红书版本、配图说明、评论区问题、转发文案，又像五个新任务一起站起来。`,
    评论回流: `你发完文章，看见一串“我也是”，会短暂开心一下。然后它们就沉进评论区，变成一堆没有被命名、没有被分类、也没有被回收的真实需求。`,
    模板入口: `读者被你击中了，但他关掉页面以后，生活并不会自动变轻。ADHD 最怕的就是这种共鸣后的坠落：心里懂了，手上还是没有入口。`,
    内容治理: `选题池越大，越像一个漂亮但危险的仓库。每个标题都在发光，每个方向都像机会，最后真正被推到现实里的反而变少。`,
    S级推进: `一个 S 级选题最可惜的死法，不是没人喜欢，而是它只被写成了一篇文章。明明能长成模板、服务、评论库和产品入口，却停在正文里睡觉。`,
    反模板化: `AI 最会把文章改得顺。顺到没有毛刺，没有羞耻，没有失败现场，也没有那个让读者突然沉默的痛点。`,
    证据系统: `很多 ADHD 文章有两种死法：一种是只讲论文，像科普；一种是只讲感觉，像玄学。真正能让人相信的，是三层证据同时在场。`,
    读者坐标: `社群最容易一开始很热闹，后来变成情绪水池。大家都说我也是，但没人知道每个人到底卡在哪一步。`,
    工具评测: `AI 工具最危险的地方，往往不是它不好用，而是它太好用了。刚开始像外骨骼，过一阵可能变成新的整理欲、新依赖和新债务。`,
    旧粉迁移: `旧法律粉丝不一定会立刻接受 ADHD 这个词。但他们一定懂另一种东西：脑子里同时排着案件、客户、风险、截止日期和自我怀疑。`,
    产品入口: `ADHD 用户不缺宏大愿望。缺的是今天打开系统以后，第一步到底是什么，能不能小到不会吓退自己。`,
    内容资产: `当文章超过一百篇，编号就不再是读者路径了。你知道每篇在哪里，新读者只会看到一座没有入口标识的仓库。`,
    现金流验证: `点赞很好，但点赞太轻了。真正让项目往现金流靠近的，不是别人说你写得好，而是有人愿意把自己的资料、问题和时间交给你。`,
    发布节律: `ADHD 创作者最容易被日更神话伤到。高能量时像反应堆，低能量时连打开后台都费劲，却还逼自己每天像工厂一样稳定。`,
    研究供料: `资料包最危险的归宿，是安静地躺在 sources 文件夹里。它明明是矿脉，却被当成仓库。`,
    人设与信任: `完美人设对 ADHD 读者不一定有吸引力，甚至会让人想逃。因为他们太熟悉失控，太不相信一套从不崩溃的成功学。`,
    账号定位: `ADHD 和 AI 都是容易被复制的标签。真正复制不了的，是你如何把法律、投资、内容、Agent 和自己的失控经验，压成同一张地图。`,
    选题治理: `220 个选题以后，最危险的动作不是停下来，而是继续扩。因为继续扩太舒服了，舒服到像是在推进。`,
    项目总纲: `如果这个项目最后只是一堆文章，它会很可惜。因为这 220 个问题真正训练出来的，不是写作能力，而是一套外接现实的认知系统。`,
  };

  const base = openings[series] || `你可能已经知道这个问题存在：${pain}。但知道问题和能把问题接到现实，是两回事。`;
  const second = priorityLine(topic.priority, number, product);
  return `${base}\n\n${second}\n\n这篇要处理的不是一个单点技巧，而是一个更底层的项目判断：${pain}。真正的需求是：${parts.need}。\n\n如果它不能被压成 ${product}，它就还只是一个观点；只有变成入口，它才开始替 ADHD 大脑减负。`;
}

function priorityLine(priority, number, product) {
  if (priority === "S") {
    return `这类题必须进入首发队列，因为它直接连接 ${product}，不是只负责让读者点头。`;
  }
  if (priority === "A") {
    return `这类题适合做成系列支柱：它不一定是第一发主炮，但会决定整个系统能不能稳定复用。`;
  }
  return `这类题可以不抢首发，但它决定系统有没有清理、复用和降级能力。`;
}

function buildArticle(topic) {
  const title = splitTitle(topic.title);
  const parts = splitProblem(topic.problem);
  const productInfo = splitProduct(topic.product);
  const profile = profiles[topic.series] || profiles["产品入口"];
  const hook = makeHook(topic, parts, productInfo);
  const axes = profile.axes;
  const comment = comments[topic.number] || `你现在最想把哪一个环节交给 AI 或 Agent 接住？`;
  const coreQuestion = title.main.replace(/^为什么/, "").replace(/？$/, "");
  const xhsHook = firstSentence(parts.pain).replace(/^把|^建立|^做/, "");
  const zhihuQuestion = `为什么${coreQuestion}？`;
  const shortVideo = `别再把${firstSentence(parts.pain)}当成小问题，它其实是系统入口断了。`;

  return `# 问题${String(topic.number).padStart(3, "0")}：${topic.title}

${hook}

## 01 收敛

一句话打穿：${profile.identity}

这件事最容易被误解成一个写作技巧、运营技巧或效率技巧。但在 ADHD x AI 的内容宇宙里，它本质上是外部前额叶的接口设计。

ADHD 大脑不是没有想法，也不是没有表达欲。它真正容易断线的地方，是从“我懂了”到“我做了”，从“我写完了”到“我发出去了”，从“有人共鸣”到“我知道下一步该做什么”。

所以这篇文章要反复强调一个判断：不要只把内容当内容，要把内容当成一段可执行系统。文章负责命名痛苦，模板负责降低启动成本，评论负责带回现实信号，Agent 负责把这些信号整理成下一轮动作。

## 02 穿透

这个问题背后至少有三层机制。

第一层，是${axes[0]}。ADHD 最容易在这里出现错觉：只要想清楚、写出来、收藏好，就好像事情已经推进了。但现实不会因为你命名了痛苦就自动改变，它需要一个具体入口。

第二层，是${axes[1]}。同一个观点，如果没有被翻译成平台语言、模板语言、评论语言或产品语言，它就会停在作者自己的脑子里。读者会被击中，但击中之后没有台阶。

第三层，是${axes[2]}。真正成熟的内容系统，必须能让每一次输出带回一点现实数据：谁被击中，谁愿意留言，谁需要模板，谁愿意把资料交出来，谁的问题可以变成下一篇文章。

这就是为什么 ${title.main} 不是一个孤立问题。它是在问：你的内容有没有从“表达系统”升级成“执行系统”。

## 03 铁证

生活场景证据：${profile.evidence}

个人观察也很直接：很多高发散创作者不是死在没有灵感，而是死在灵感没有被接线。一个标题出来很爽，一篇正文写完也很爽，但没有发布包、没有模板、没有评论回收，爽感就会停在脑内。

项目证据更硬：当一个选题同时拥有正文、渲染 HTML、发布版本、评论问题、产品入口和反馈记录时，它才从“文章”变成“资产”。否则它只是一个写得不错的孤岛。

反事实也成立：如果你每次只多做一个很小的接口，比如在文末附一个模板、在评论区问一个卡点、在反馈表里记录一个需求，这个项目三个月以后会完全不同。你得到的不是更多文章，而是一张读者需求地图。

## 04 决策

你要停止把“写完”当成终点。

对 ADHD 作者来说，写完只是第一阶段结算。真正决定价值的，是这篇文章能不能进入下一层：能不能被拆成小红书，能不能引出评论，能不能变成模板，能不能让读者把一个真实任务托付给你。

${parts.need}。这句话不是运营口号，而是系统设计原则。

如果一个选题没有痛点，它就冻结；如果一个选题没有产品入口，它就降级；如果一个选题没有评论问题，它就暂时不要首发。这样做不是保守，而是防止高发散系统把“又想到了一个好题”误判成推进。

## 05 落地

今天的落地动作：${parts.todo}。

把它压成一个三行卡片：

- 当前痛点：${parts.pain}
- 今天只做：${parts.todo}
- 交给 AI/Agent：把这一步改写成一个可复制、可记录、可回流的最小入口

不要试图一次做完整个系统。ADHD 最需要的是小到能开始、大到能改变现实的接口。今天只要把这个题从观点往入口推进一步，就已经不是自嗨。

如果接 Agent，就给它一个固定命令：读取这篇文章，生成一个发布包、一个评论问题、一个模板入口、一个反馈记录字段。它不需要夸你，它只需要把内容推过现实边界。

## 发布接口

- 公众号版核心标题：${title.main}${title.subtitle ? title.subtitle : ""}
- 小红书版钩子：${xhsHook}，这不是小问题，是系统入口断了。
- 知乎回答问题：${zhihuQuestion}
- 短视频前三秒：${shortVideo}
- 评论区问题：${comment}
`;
}

function main() {
  if (!fs.existsSync(sourcePath)) {
    throw new Error(`Source not found: ${sourcePath}`);
  }
  const topics = parsePoolTable(fs.readFileSync(sourcePath, "utf8"));
  const written = [];
  const skipped = [];
  for (const topic of topics) {
    const existing = existingArticle(topic.number);
    if (existing) {
      skipped.push(existing);
      continue;
    }
    const title = splitTitle(topic.title);
    const filePart = sanitizeFilePart(`${title.main}_${title.subtitle || ""}`);
    const fileName = `问题${String(topic.number).padStart(3, "0")}_${filePart}.md`;
    const filePath = path.join(root, fileName);
    fs.writeFileSync(filePath, buildArticle(topic), "utf8");
    written.push(fileName);
  }
  console.log(`Generated articles: ${written.length}`);
  for (const name of written) console.log(`  ${name}`);
  if (skipped.length) {
    console.log(`Skipped existing: ${skipped.length}`);
  }
}

main();
