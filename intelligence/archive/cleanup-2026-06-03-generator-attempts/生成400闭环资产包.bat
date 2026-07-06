@echo off
setlocal
cd /d "%~dp0"
echo Running 400 content pack generator...
echo Project root: %CD%
echo.
powershell.exe -NoProfile -ExecutionPolicy Bypass -File "%~dp0src\build_400_content_packs.ps1" 1> "%~dp0生成400闭环资产包.log" 2>&1
echo.
echo ===== Generator log =====
type "%~dp0生成400闭环资产包.log"
echo.
echo ===== Quick check =====
powershell.exe -NoProfile -ExecutionPolicy Bypass -Command "$root='%~dp0content-packs'; if(Test-Path $root){ 'Pack dirs: ' + ((Get-ChildItem $root -Directory -Filter '问题*' -ErrorAction SilentlyContinue).Count); 'Meta files: ' + ((Get-ChildItem $root -Recurse -File -Filter 'meta.json' -ErrorAction SilentlyContinue).Count); 'Draft files: ' + ((Get-ChildItem $root -Recurse -File -Filter '01_正文.md' -ErrorAction SilentlyContinue).Count) } else { 'content-packs missing' }"
echo.
echo Done. Keep this window open and tell Claude if Pack dirs is 400.
pause
