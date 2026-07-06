@echo off
setlocal
pushd "%~dp0"
echo Running ASCII-safe 400 content pack generator...
echo Project root: %CD%
echo.
powershell.exe -NoProfile -ExecutionPolicy Bypass -File ".\src\build_400_content_packs_ascii.ps1" > ".\build_400_content_packs_ascii.log" 2>&1
echo.
echo ===== Generator log =====
type ".\build_400_content_packs_ascii.log"
echo.
echo ===== Quick check =====
powershell.exe -NoProfile -ExecutionPolicy Bypass -Command "$root=Join-Path (Get-Location) 'content-packs'; if(Test-Path $root){ 'Pack dirs: ' + ((Get-ChildItem $root -Directory -Filter '*001' -ErrorAction SilentlyContinue).Count + (Get-ChildItem $root -Directory -Filter '*002' -ErrorAction SilentlyContinue).Count); 'All pack dirs: ' + ((Get-ChildItem $root -Directory -ErrorAction SilentlyContinue).Count); 'Meta files: ' + ((Get-ChildItem $root -Recurse -File -Filter 'meta.json' -ErrorAction SilentlyContinue).Count); 'Draft files: ' + ((Get-ChildItem $root -Recurse -File -Filter '01_*.md' -ErrorAction SilentlyContinue).Count) } else { 'content-packs missing' }"
echo.
echo Done. Tell Claude the Generator log and Quick check counts.
popd
pause
