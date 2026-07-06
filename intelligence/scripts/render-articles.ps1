param(
  [string]$Root = (Split-Path -Parent $PSScriptRoot),
  [int]$EndNumber = 108
)

$ErrorActionPreference = 'Stop'

$outDir = Join-Path $Root 'delivery\rendered_articles'
if (-not (Test-Path -LiteralPath $outDir)) {
  New-Item -ItemType Directory -Path $outDir -Force | Out-Null
}

function Escape-Html {
  param([string]$Text)
  return [System.Net.WebUtility]::HtmlEncode($Text)
}

function Convert-InlineMarkdown {
  param([string]$Text)
  $encoded = Escape-Html $Text
  $encoded = $encoded -replace '\*\*(.+?)\*\*', '<strong>$1</strong>'
  $encoded = $encoded -replace '`([^`]+)`', '<code>$1</code>'
  return $encoded
}

function Convert-MarkdownToHtml {
  param([string]$Markdown)

  $lines = $Markdown -replace "`r", '' -split "`n"
  $html = New-Object System.Collections.Generic.List[string]
  $paragraph = New-Object System.Collections.Generic.List[string]
  $inUl = $false
  $inOl = $false
  $inQuote = $false

  function Flush-Paragraph {
    if ($paragraph.Count -gt 0) {
      $text = (($paragraph | ForEach-Object { $_.Trim() }) -join ' ')
      $html.Add("<p>$(Convert-InlineMarkdown $text)</p>")
      $paragraph.Clear()
    }
  }

  function Close-Lists {
    if ($inUl) { $html.Add('</ul>'); Set-Variable -Name inUl -Value $false -Scope 1 }
    if ($inOl) { $html.Add('</ol>'); Set-Variable -Name inOl -Value $false -Scope 1 }
    if ($inQuote) { $html.Add('</blockquote>'); Set-Variable -Name inQuote -Value $false -Scope 1 }
  }

  foreach ($rawLine in $lines) {
    $line = $rawLine.TrimEnd()
    if (-not $line.Trim()) {
      Flush-Paragraph
      Close-Lists
      continue
    }

    if ($line -match '^(#{1,6})\s+(.+)$') {
      Flush-Paragraph
      Close-Lists
      $level = $Matches[1].Length
      $text = Convert-InlineMarkdown $Matches[2].Trim()
      $html.Add("<h$level>$text</h$level>")
      continue
    }

    if ($line -match '^>\s*(.+)$') {
      Flush-Paragraph
      if (-not $inQuote) { $html.Add('<blockquote>'); $inQuote = $true }
      $html.Add("<p>$(Convert-InlineMarkdown $Matches[1].Trim())</p>")
      continue
    }

    if ($line -match '^\s*[-*]\s+(.+)$') {
      Flush-Paragraph
      if ($inOl) { $html.Add('</ol>'); $inOl = $false }
      if (-not $inUl) { $html.Add('<ul>'); $inUl = $true }
      $html.Add("<li>$(Convert-InlineMarkdown $Matches[1].Trim())</li>")
      continue
    }

    if ($line -match '^\s*\d+[.)]\s+(.+)$') {
      Flush-Paragraph
      if ($inUl) { $html.Add('</ul>'); $inUl = $false }
      if (-not $inOl) { $html.Add('<ol>'); $inOl = $true }
      $html.Add("<li>$(Convert-InlineMarkdown $Matches[1].Trim())</li>")
      continue
    }

    $paragraph.Add($line)
  }

  Flush-Paragraph
  Close-Lists
  return ($html -join "`n")
}

function Get-Title {
  param([string]$Text, [string]$Fallback)
  $firstLine = ($Text -split "`r?`n" | Where-Object { $_.Trim() })[0]
  if ($firstLine -match '^#\s*(.+)$') {
    return $Matches[1].Trim()
  }
  return $Fallback
}

$rendered = @()
for ($i = 1; $i -le $EndNumber; $i++) {
  $num = '{0:D3}' -f $i
  $file = Get-ChildItem -LiteralPath $Root -File -Filter "问题$num*.md" | Select-Object -First 1
  if (-not $file) { continue }

  $markdown = Get-Content -LiteralPath $file.FullName -Raw -Encoding UTF8
  $title = Get-Title -Text $markdown -Fallback $file.BaseName
  $bodyHtml = Convert-MarkdownToHtml -Markdown $markdown
  $outName = "$($file.BaseName).html"
  $outPath = Join-Path $outDir $outName
  $sourceHref = '../../' + [Uri]::EscapeDataString($file.Name)
  $indexHref = '../../indexes/问题001-108_MD总索引.html'

  $page = @"
<!doctype html>
<html lang="zh-CN">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>$(Escape-Html $title)</title>
  <style>
    :root { color-scheme: light; }
    body { margin: 0; background: #fbfbf8; color: #182026; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "PingFang SC", "Microsoft YaHei", sans-serif; line-height: 1.78; }
    .shell { max-width: 820px; margin: 0 auto; padding: 32px 22px 64px; }
    nav { display: flex; gap: 14px; flex-wrap: wrap; margin-bottom: 28px; color: #52606d; font-size: 14px; }
    nav a { color: #0b66c3; text-decoration: none; }
    nav a:hover { text-decoration: underline; }
    article { background: #fff; border: 1px solid #d9e2ec; border-radius: 8px; padding: 34px 38px; box-shadow: 0 8px 24px rgba(15, 23, 42, .04); }
    h1 { font-size: 30px; line-height: 1.32; margin: 0 0 28px; letter-spacing: 0; }
    h2 { margin-top: 34px; padding-top: 10px; font-size: 22px; border-top: 1px solid #edf2f7; }
    h3 { margin-top: 26px; font-size: 18px; }
    p { margin: 14px 0; }
    strong { color: #111827; }
    blockquote { margin: 20px 0; padding: 6px 18px; border-left: 4px solid #9fb3c8; color: #3e4c59; background: #f8fafc; }
    ul, ol { padding-left: 26px; }
    li { margin: 7px 0; }
    code { background: #f0f4f8; padding: 2px 5px; border-radius: 4px; }
    .meta { margin-top: 28px; padding-top: 18px; border-top: 1px solid #edf2f7; color: #627d98; font-size: 14px; }
    @media (max-width: 720px) {
      .shell { padding: 18px 12px 44px; }
      article { padding: 24px 18px; }
      h1 { font-size: 24px; }
    }
  </style>
</head>
<body>
  <main class="shell">
    <nav>
      <a href="$indexHref">返回总索引</a>
      <a href="$sourceHref">查看源 Markdown</a>
    </nav>
    <article>
      $bodyHtml
      <div class="meta">渲染自：$(Escape-Html $file.Name)</div>
    </article>
  </main>
</body>
</html>
"@

  $utf8NoBom = New-Object System.Text.UTF8Encoding -ArgumentList $false
  [System.IO.File]::WriteAllText($outPath, $page, $utf8NoBom)
  $rendered += [PSCustomObject]@{ Number = $num; Markdown = $file.Name; Html = $outName }
}

Write-Host "Rendered article HTML files: $($rendered.Count)"
Write-Host "Output directory: $outDir"

