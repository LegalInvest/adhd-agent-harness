param(
  [string]$Root = (Split-Path -Parent $PSScriptRoot),
  [int]$EndNumber = 0
)

$ErrorActionPreference = 'Stop'

$indexDir = Join-Path $Root 'indexes'
if (-not (Test-Path -LiteralPath $indexDir)) {
  New-Item -ItemType Directory -Path $indexDir | Out-Null
}

$titleMap = @{
  14 = '为什么 ADHD 最懂 LLM 的幻觉？'
  15 = '为什么 ADHD 和 LLM 都需要 Harness？'
  16 = '为什么从“我想做”到“Agent 帮我做了”是 ADHD 的救赎？'
  17 = '为什么 ADHD 的情绪风暴和 LLM 的温度参数是同构的？'
  18 = '为什么 ADHD 的身体不安分遇到 AI 反而成了优势？'
  19 = '为什么 80% 的成人 ADHD 从未被诊断？'
  20 = '为什么 ADHD 在聚会上是焦点，回家却想死？'
  21 = '为什么 Agent 正在成为 ADHD 新的多巴胺来源？'
  22 = '为什么 ADHD 是应试教育的最极端受害者？'
  23 = '为什么 ADHD 在职场中总是聊起来聪明做起来糊涂？'
  24 = '为什么 ADHD 的能量在冬天消失却在春天爆发？'
  25 = '为什么 ADHD 是文明的隐藏引擎？'
  26 = '为什么不是 ADHD 像 AI，而是 AI 像 ADHD？'
  27 = '为什么 ADHD 是你的大脑在拒绝过拟合？'
  28 = '为什么 ADHD 与弱联系是你最大的创新资产？'
  29 = '为什么 ADHD 创始人将在 AI 时代统治世界？'
  30 = '如果 2028 年 AI 比 ADHD 更会发散，我们还剩什么？'
  31 = '为什么你的大脑就是 MoE？'
  76 = '为什么 ADHD 的“心算困难”是大脑把工作记忆让位给了发散网络？'
  77 = '为什么 ADHD 的“完成恐惧”比拖延更深一层？'
  78 = '为什么 ADHD 的“超聚焦”是高浓度的多巴胺极化，不是意志力胜利？'
  79 = '为什么 ADHD 的“被打断后回不来”是栈指针丢失，不是性格脆弱？'
  80 = '为什么 ADHD 的“过度共情”是镜像神经元的无门控泄洪？'
  81 = '为什么 ADHD 的“决策疲劳”在下午三点比午饭前更可预测？'
  82 = '为什么 ADHD 需要“任务的物理化身”（实体便签/小道具）才能真正记得？'
  83 = '为什么 ADHD 的“反复确认”不是焦虑，是工作记忆校验和？'
  84 = '为什么 ADHD 的“读不完非虚构书”恰恰是因为太懂这本书的核心？'
  85 = '为什么 ADHD 的“反复重启项目”是迭代而不是循环？'
  86 = '为什么 ADHD 的“会议中突然走神”是大脑在帮你识别真正的关键句？'
  87 = '为什么 ADHD 的“截止日期前才动”是延迟最大化期望效用的理性策略？'
  88 = '为什么 ADHD 的“反复刷同一个信息流”是低成本的多巴胺取暖？'
  89 = '为什么 ADHD 的“无法决定吃什么”是选择维度过载，不是优柔寡断？'
  90 = '为什么 ADHD 的“工作时听书做菜同时进行”是有意的认知节流？'
  99 = '为什么青年律师最需要的不是自律，而是一个外部前额叶？'
  100 = '为什么法学生写不出论文，不是因为懒，而是启动系统坏了？'
  101 = '为什么实习律师最容易死在“我先整理一下资料”？'
  102 = '为什么律师的微信已读不回，本质是决策瘫痪？'
  103 = '为什么法律人最该训练的不是专注力，而是切换力？'
  104 = '为什么青年律师的焦虑，其实是大脑在做风险尽调？'
  105 = '为什么法律人的知识管理越做越复杂，反而越不产出？'
  106 = '为什么 AI Agent 是青年律师从助理到主理人的认知外骨骼？'
  107 = '为什么法学生需要“今日唯一动作”，而不是一张完美学习计划？'
  108 = '为什么律师成长最危险的不是不会学，而是不会卸载？'
}

function Get-ArticleTitle {
  param([System.IO.FileInfo]$File)

  $firstLine = Get-Content -LiteralPath $File.FullName -Encoding UTF8 -TotalCount 1
  if ($firstLine -match '^#\s*问题\d{3}[：:]\s*(.+)$') {
    return $Matches[1].Trim()
  }
  if ($firstLine -match '^#\s*(.+)$') {
    return $Matches[1].Trim()
  }
  if ($File.BaseName -match '^问题\d{3}_(.+)$') {
    return ($Matches[1] -replace '_', '｜').Trim()
  }
  return $File.BaseName
}

function Get-Status {
  param(
    [int]$Number,
    [bool]$HasFile
  )

  if ($HasFile) {
    return '已有正文'
  }
  if (($Number -ge 14 -and $Number -le 31)) {
    return '历史待核验/待补正文'
  }
  if (($Number -ge 76 -and $Number -le 90)) {
    return '待写'
  }
  if (($Number -ge 99 -and $Number -le 100)) {
    return '法律桥接降级'
  }
  return '待补正文'
}

function Escape-Html {
  param([string]$Text)
  return [System.Net.WebUtility]::HtmlEncode($Text)
}

$articleFiles = @{}
Get-ChildItem -LiteralPath $Root -File -Filter '问题*.md' | ForEach-Object {
  if ($_.Name -match '^问题(?<num>\d{3})_.+\.md$') {
    $articleFiles[[int]$Matches['num']] = $_
  }
}

$generatedAt = Get-Date -Format 'yyyy-MM-dd HH:mm:ss'
if ($EndNumber -gt 0) {
  $endNumber = $EndNumber
} elseif ($articleFiles.Count -gt 0) {
  $endNumber = ($articleFiles.Keys | Measure-Object -Maximum).Maximum
} else {
  $endNumber = 108
}
$endLabel = '{0:D3}' -f $endNumber
$md = New-Object System.Collections.Generic.List[string]
$htmlRows = New-Object System.Collections.Generic.List[string]

$md.Add("# ADHD x AI 问题001-$endLabel MD总索引")
$md.Add('')
$md.Add("生成时间：$generatedAt")
$md.Add('')
$md.Add('说明：正文链接使用相对路径，仓库移动或 clone 后仍可打开。')
$md.Add('')
$md.Add('| 编号 | 标题 | 状态 | 正文链接 |')
$md.Add('|---|---|---|---|')

for ($i = 1; $i -le $endNumber; $i++) {
  $num = '{0:D3}' -f $i
  $file = $null
  if ($articleFiles.ContainsKey($i)) {
    $file = $articleFiles[$i]
  }

  if ($file) {
    $title = Get-ArticleTitle -File $file
  } elseif ($titleMap.ContainsKey($i)) {
    $title = $titleMap[$i]
  } else {
    $title = '待补标题'
  }

  $status = Get-Status -Number $i -HasFile ([bool]$file)
  if ($file) {
    $renderedName = "$($file.BaseName).html"
    $renderedRel = "delivery/rendered_articles/$renderedName"
    $renderedPath = Join-Path $Root $renderedRel
    if (Test-Path -LiteralPath $renderedPath) {
      $mdLink = "[打开正文](../$renderedRel)"
      $href = '../delivery/rendered_articles/' + [Uri]::EscapeDataString($renderedName)
    } else {
      $mdLink = "[打开正文](../$($file.Name))"
      $href = '../' + [Uri]::EscapeDataString($file.Name)
    }
    $htmlLink = "<a href=`"$href`">打开正文</a>"
  } else {
    $mdLink = '未生成'
    $htmlLink = '未生成'
  }

  $md.Add("| $num | $title | $status | $mdLink |")
  $htmlRows.Add("<tr><td>$num</td><td>$(Escape-Html $title)</td><td>$(Escape-Html $status)</td><td>$htmlLink</td></tr>")
}

$html = @"
<!doctype html>
<html lang="zh-CN">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>ADHD x AI 问题001-$endLabel MD总索引</title>
  <style>
    body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; margin: 32px; color: #1f2933; background: #fbfbf8; }
    h1 { font-size: 28px; margin-bottom: 8px; }
    p { color: #52606d; }
    table { width: 100%; border-collapse: collapse; background: white; }
    th, td { border: 1px solid #d9e2ec; padding: 8px 10px; vertical-align: top; }
    th { background: #f0f4f8; text-align: left; }
    tr:nth-child(even) { background: #f8fafc; }
    a { color: #0b66c3; text-decoration: none; }
    a:hover { text-decoration: underline; }
  </style>
</head>
<body>
  <h1>ADHD x AI 问题001-$endLabel MD总索引</h1>
  <p>生成时间：$(Escape-Html $generatedAt)。链接为相对路径，适合本地打开或仓库 clone 后使用。</p>
  <table>
    <thead>
      <tr><th>编号</th><th>标题</th><th>状态</th><th>正文链接</th></tr>
    </thead>
    <tbody>
      $($htmlRows -join "`n      ")
    </tbody>
  </table>
</body>
</html>
"@

$utf8NoBom = New-Object System.Text.UTF8Encoding -ArgumentList $false
$mdFileName = "问题001-$endLabel`_MD总索引.md"
$htmlFileName = "问题001-$endLabel`_MD总索引.html"
[System.IO.File]::WriteAllLines((Join-Path $indexDir $mdFileName), $md, $utf8NoBom)
[System.IO.File]::WriteAllText((Join-Path $indexDir $htmlFileName), $html, $utf8NoBom)

Write-Host "Index updated:"
Write-Host "  indexes/$mdFileName"
Write-Host "  indexes/$htmlFileName"


