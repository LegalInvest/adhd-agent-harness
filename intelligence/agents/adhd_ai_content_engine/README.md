# ADHD AI Content Engine — Google ADK Wrapper

This folder is a thin Google ADK entrypoint for the project-local self-growing engine.

```bash
adk run agents/adhd_ai_content_engine
adk web agents
```

Operational truth remains in the repository scripts:

```bash
python engines/self_growing_engine.py --dry-run --no-llm
python engines/build_llm_wiki_export.py
powershell.exe -NoProfile -ExecutionPolicy Bypass -File scripts/install-daily-scout.ps1 -RunNow
```

The ADK agent is intentionally lightweight. It documents and orchestrates the project rules; it does not replace the non-destructive file-based pipeline.
