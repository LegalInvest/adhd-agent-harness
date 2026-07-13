param(
  [string]$Root = (Split-Path -Parent $PSScriptRoot),
  [int]$EndNumber = 108
)

$ErrorActionPreference = 'Stop'

$outDir = Join-Path $Root 'delivery\content_qa'
if (-not (Test-Path -LiteralPath $outDir)) {
  New-Item -ItemType Directory -Path $outDir -Force | Out-Null
}

function Escape-Html {
  param([string]$Text)
  return [System.Net.WebUtility]::HtmlEncode($Text)
}

function Normalize-Text {
  param([string]$Text)
  $text = $Text -replace "`r", "`n"
  $text = $text -replace '```[\s\S]*?```', ''
  $text = $text -replace '(?m)^#.*$', ''
  $text = $text -replace '(?m)^\s*[-*]\s+', ''
  $text = $text -replace '\*\*', ''
  $text = $text -replace '\[(.*?)\]\(.*?\)', '$1'
  $text = $text -replace '\s+', ' '
  return $text.Trim()
}

function Get-Title {
  param([string]$Text, [string]$Fallback)
  $firstLine = ($Text -split "`r?`n" | Where-Object { $_.Trim() })[0]
  if ($firstLine -match '^#\s*问题\d{3}[：:]\s*(.+)$') {
    return $Matches[1].Trim()
  }
  if ($Fallback -match '^问题\d{3}_(.+)$') {
    return (($Matches[1] -replace '_', '｜') -replace '\.md$', '').Trim()
  }
  return $Fallback
}

function Split-Sentences {
  param([string]$Text)
  $normalized = Normalize-Text -Text $Text
  $items = $normalized -split '(?<=[。！？!?])'
  return @($items | ForEach-Object { $_.Trim() } | Where-Object { $_.Length -ge 18 })
}

function Shorten-Text {
  param(
    [string]$Text,
    [int]$MaxLength = 62
  )
  $value = ($Text -replace '\s+', ' ').Trim()
  $value = $value -replace '^[0-9一二三四五六七八九十]+[、\.\s]+', ''
  if ($value.Length -gt $MaxLength) {
    return $value.Substring(0, $MaxLength) + '...'
  }
  return $value
}

function Select-IssueSentence {
  param(
    [string[]]$Sentences,
    [string[]]$Patterns,
    [string[]]$Exclude = @()
  )
  foreach ($pattern in $Patterns) {
    foreach ($sentence in $Sentences) {
      $blocked = $false
      foreach ($excludePattern in $Exclude) {
        if ($sentence -match $excludePattern) {
          $blocked = $true
          break
        }
      }
      if (-not $blocked -and $sentence -match $pattern) {
        return (Shorten-Text -Text $sentence)
      }
    }
  }
  foreach ($sentence in $Sentences) {
    if ($sentence -notmatch '今天的落地动作|发布接口|Done|Next') {
      return (Shorten-Text -Text $sentence)
    }
  }
  return ''
}

function Get-ActionTask {
  param([string]$Text)
  $normalized = $Text -replace "`r", "`n"
  $markerIndex = $normalized.IndexOf('今天的落地动作')
  if ($markerIndex -ge 0) {
    $block = $normalized.Substring($markerIndex)
    $lines = @($block -split "`n" | ForEach-Object { $_.Trim() } | Where-Object {
      $_ -and
      $_ -notmatch '^#' -and
      $_ -notmatch '^今天的落地动作' -and
      $_ -notmatch '^发布接口' -and
      $_ -notmatch '^格式[:：]?$' -and
      $_ -notmatch '^例如[:：]?$' -and
      $_ -notmatch '^Done' -and
      $_ -notmatch '^Next'
    })
    $actionLines = @()
    foreach ($line in $lines) {
      if ($line -match '___|：|写|建立|运行|选择|先|把|问|列|做|记录|设置|格式|只') {
        $clean = ($line -replace '\*\*', '') -replace '\s+', ' '
        $actionLines += $clean
      }
      if ($actionLines.Count -ge 3) { break }
    }
    if ($actionLines.Count -gt 0) {
      return (Shorten-Text -Text ($actionLines -join '；') -MaxLength 92)
    }
  }

  $sentences = Split-Sentences -Text $Text
  $todoPatterns = @('今天.*动作', '写下', '建立', '运行', '选择', '先做', '拿.*写', '只问', '列.*清单', '记录', '设置', 'Decide')
  return (Select-IssueSentence -Sentences $sentences -Patterns $todoPatterns -Exclude @('不是.*而是'))
}

function Get-Problem {
  param(
    [string]$Text,
    [string]$Title
  )
  $sentences = Split-Sentences -Text $Text
  $contentSentences = @($sentences | Where-Object {
    $_ -and
    $_ -notmatch '^\s*#' -and
    $_ -notmatch [regex]::Escape($Title) -and
    $_ -notmatch '发布接口|Done|Next'
  })

  $painPatterns = @(
    '你有没有',
    '你是不是',
    '你明明',
    '最痛苦',
    '最容易',
    '经常',
    '卡住',
    '崩',
    '不敢',
    '忘',
    '拖',
    '焦虑',
    '内疚',
    '羞耻',
    '已读不回',
    '写不出',
    '启动不了',
    '无法',
    '反复'
  )
  $needPatterns = @(
    '真正.*需要',
    '真正.*要',
    '需要的是',
    '需要.*机制',
    '需要.*系统',
    '缺的不是',
    '缺的是',
    '问题不是',
    '问题不在',
    '关键',
    '所以.*需要',
    '解决方式',
    '你需要',
    '把.*翻译',
    '变成.*清单',
    '转成.*动作',
    '不是.*而是'
  )

  $pain = Select-IssueSentence -Sentences $contentSentences -Patterns $painPatterns -Exclude @('今天的落地动作')
  $need = Select-IssueSentence -Sentences $contentSentences -Patterns $needPatterns -Exclude @([regex]::Escape($pain), '今天的落地动作')
  $todo = Get-ActionTask -Text $Text

  if (-not $pain) { $pain = '痛点待人工复核：正文未抽取到清晰场景' }
  if (-not $need) { $need = '需求待人工复核：需补出明确机制或产品需求' }
  if (-not $todo) { $todo = '待办待人工复核：需补一个可执行动作' }

  return "痛点：$pain；需求：$need；待办：$todo"
}

function Pick-CorePoints {
  param([string]$Text)
  $sentences = Split-Sentences -Text $Text
  $preferred = @()
  $patterns = @('不是.*而是', '真正', '核心', '关键', '所以', '需要', '问题是', '第一', '第二', '第三', 'Agent', '外部')
  foreach ($pattern in $patterns) {
    foreach ($sentence in $sentences) {
      if ($sentence -match $pattern -and -not ($preferred -contains $sentence)) {
        $preferred += $sentence
      }
      if ($preferred.Count -ge 3) { break }
    }
    if ($preferred.Count -ge 3) { break }
  }
  foreach ($sentence in $sentences) {
    if ($preferred.Count -ge 3) { break }
    if (-not ($preferred -contains $sentence)) {
      $preferred += $sentence
    }
  }
  $points = @()
  for ($i = 0; $i -lt 3; $i++) {
    if ($i -lt $preferred.Count) {
      $point = $preferred[$i] -replace '\s+', ' '
      if ($point.Length -gt 72) {
        $point = $point.Substring(0, 72) + '...'
      }
      $points += $point
    } else {
      $points += ''
    }
  }
  return $points
}

function Get-Quality {
  param(
    [int]$CharCount,
    [int]$SectionCount,
    [int]$CoreCount,
    [string]$Problem
  )
  $score = 0
  if ($CharCount -ge 800) { $score += 2 }
  if ($CharCount -ge 1200) { $score += 1 }
  if ($SectionCount -ge 4 -or $CharCount -ge 1500) { $score += 1 }
  if ($CoreCount -ge 3) { $score += 2 }
  if ($Problem.Trim().Length -gt 0) { $score += 1 }

  if ($score -ge 6) { return @('通过', $score, '') }
  if ($score -ge 5) { return @('需增强', $score, '短稿或结构略薄，建议补充场景、铁证或落地动作。') }
  return @('需重写', $score, '正文无法稳定支撑 3 个核心观点或篇幅/结构不足。')
}

$rows = New-Object System.Collections.Generic.List[object]

for ($i = 1; $i -le $EndNumber; $i++) {
  $num = '{0:D3}' -f $i
  $file = Get-ChildItem -LiteralPath $Root -File -Filter "问题$num*.md" | Select-Object -First 1
  if (-not $file) {
    $rows.Add([PSCustomObject]@{
      '选题' = $num
      '题目' = '未生成'
      '字数' = 0
      '3个核心观点' = ''
      '解决的问题' = '痛点：未找到正文；需求：补齐本地正文；待办：生成 Markdown 正文并复跑质检'
      '质量评分' = 0
      '质量状态' = '需重写'
      '质检备注' = '未找到正文文件'
      '正文链接' = ''
    })
    continue
  }

  $text = Get-Content -LiteralPath $file.FullName -Raw -Encoding UTF8
  $title = Get-Title -Text $text -Fallback $file.Name
  $charCount = (($text -replace '\s', '')).Length
  $sectionCount = ([regex]::Matches($text, '(?m)^\s*(#{2,3}\s*)?(0[1-9]|[一二三四五六七八九十]+)[、\.\s]')).Count
  $points = Pick-CorePoints -Text $text
  $coreCount = @($points | Where-Object { $_.Trim().Length -gt 0 }).Count
  $problem = Get-Problem -Text $text -Title $title
  $quality = Get-Quality -CharCount $charCount -SectionCount $sectionCount -CoreCount $coreCount -Problem $problem

  $renderedName = "$($file.BaseName).html"
  $renderedPath = Join-Path $Root "delivery\rendered_articles\$renderedName"
  if (Test-Path -LiteralPath $renderedPath) {
    $articleLink = "../rendered_articles/$renderedName"
  } else {
    $articleLink = "../$($file.Name)"
  }

  $rows.Add([PSCustomObject]@{
    '选题' = $num
    '题目' = $title
    '字数' = $charCount
    '3个核心观点' = (($points | ForEach-Object { $_.Trim() }) -join ' | ')
    '解决的问题' = $problem
    '质量评分' = $quality[1]
    '质量状态' = $quality[0]
    '质检备注' = $quality[2]
    '正文链接' = $articleLink
  })
}

$csvPath = Join-Path $outDir "内容质检_001-$('{0:D3}' -f $EndNumber).csv"
$htmlPath = Join-Path $outDir "内容质检_001-$('{0:D3}' -f $EndNumber).html"

$rows | Export-Csv -LiteralPath $csvPath -NoTypeInformation -Encoding UTF8

$generatedAt = Get-Date -Format 'yyyy-MM-dd HH:mm:ss'
$htmlRows = $rows | ForEach-Object {
  $statusClass = switch ($_.质量状态) {
    '通过' { 'pass' }
    '需增强' { 'warn' }
    default { 'fail' }
  }
  $link = if ($_.正文链接) { "<a href=`"$(Escape-Html $_.正文链接)`">打开正文</a>" } else { '' }
  "<tr class=`"$statusClass`"><td>$($_.选题)</td><td>$(Escape-Html $_.题目)</td><td>$($_.字数)</td><td>$(Escape-Html $_.'3个核心观点')</td><td>$(Escape-Html $_.解决的问题)</td><td>$($_.质量评分)</td><td>$($_.质量状态)</td><td>$(Escape-Html $_.质检备注)</td><td>$link</td></tr>"
}

$html = @"
<!doctype html>
<html lang="zh-CN">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>内容质检 001-$('{0:D3}' -f $EndNumber)</title>
  <style>
    body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; margin: 28px; background: #fbfbf8; color: #1f2933; }
    h1 { margin-bottom: 4px; }
    .meta { color: #52606d; margin-bottom: 20px; }
    table { width: 100%; border-collapse: collapse; background: white; table-layout: fixed; }
    th, td { border: 1px solid #d9e2ec; padding: 8px; vertical-align: top; word-break: break-word; }
    th { background: #f0f4f8; text-align: left; position: sticky; top: 0; }
    tr.pass { background: #f7fff8; }
    tr.warn { background: #fffaf0; }
    tr.fail { background: #fff5f5; }
    td:nth-child(1) { width: 54px; }
    td:nth-child(3) { width: 70px; text-align: right; }
    td:nth-child(6) { width: 72px; font-weight: 700; }
    td:nth-child(8) { width: 82px; }
    a { color: #0b66c3; text-decoration: none; }
    a:hover { text-decoration: underline; }
  </style>
</head>
<body>
  <h1>内容质检 001-$('{0:D3}' -f $EndNumber)</h1>
  <p class="meta">生成时间：$(Escape-Html $generatedAt)。质量评分满分 7 分；质检标准：字数、结构、3 个核心观点可提取性、解决问题清晰度。</p>
  <table>
    <thead>
      <tr><th>选题</th><th>题目</th><th>字数</th><th>3个核心观点</th><th>解决的问题</th><th>质量评分</th><th>质量状态</th><th>质检备注</th><th>正文</th></tr>
    </thead>
    <tbody>
      $($htmlRows -join "`n      ")
    </tbody>
  </table>
</body>
</html>
"@

$utf8NoBom = New-Object System.Text.UTF8Encoding -ArgumentList $false
[System.IO.File]::WriteAllText($htmlPath, $html, $utf8NoBom)

$summary = $rows | Group-Object -Property '质量状态' | ForEach-Object { "$($_.Name): $($_.Count)" }
Write-Host "Content QA generated:"
Write-Host "  $csvPath"
Write-Host "  $htmlPath"
Write-Host ($summary -join '; ')


