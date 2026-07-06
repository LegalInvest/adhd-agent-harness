#!/usr/bin/env python3
"""Build LLM-Wiki seed pages from the 400 content packs.

This script exports lightweight topic pages under `knowledge/wiki/topics/` and
source snapshots under `knowledge/raw/sources/content-packs/`. It reads content
packs but does not modify them.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import sys
import textwrap
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
PACKS_DIR = ROOT / "content-packs"
KNOWLEDGE_DIR = ROOT / "knowledge"


def read_text(path: Path, max_chars: int = 1600) -> str:
    if not path.exists():
        return ""
    text = path.read_text(encoding="utf-8", errors="replace")
    text = re.sub(r"\s+", " ", text).strip()
    return text[:max_chars]


def load_meta(meta_path: Path) -> dict[str, Any]:
    return json.loads(meta_path.read_text(encoding="utf-8"))


def ensure_dirs() -> None:
    for path in [KNOWLEDGE_DIR / "raw" / "sources" / "content-packs", KNOWLEDGE_DIR / "wiki" / "topics"]:
        path.mkdir(parents=True, exist_ok=True)


def trigger_profile(meta: dict[str, Any]) -> dict[str, str]:
    profile = meta.get("current_trigger_profile") or {}
    return {
        "category": str(profile.get("category") or ""),
        "desire": str(profile.get("desire_trigger") or ""),
        "thought": str(profile.get("thought_trigger") or ""),
        "action": str(profile.get("action_trigger") or ""),
    }


def pack_priority(meta: dict[str, Any]) -> str:
    return str(meta.get("priority") or "")


def pack_score(meta: dict[str, Any]) -> int:
    scores = meta.get("current_scores") or {}
    try:
        return int(scores.get("total") or 0)
    except (TypeError, ValueError):
        return 0


def build_pack_page(pack_dir: Path, meta: dict[str, Any]) -> str:
    pack_id = str(meta.get("id") or pack_dir.name)
    title = str(meta.get("title") or pack_id)
    number = int(meta.get("number") or re.sub(r"\D", "", pack_id))
    profile = trigger_profile(meta)
    score = pack_score(meta)
    priority = pack_priority(meta)
    body_excerpt = read_text(pack_dir / "01_正文.md")
    publish_excerpt = read_text(pack_dir / "02_发布包.md", max_chars=900)
    template_excerpt = read_text(pack_dir / "08_模板入口.md", max_chars=900)

    return textwrap.dedent(f"""
    ---
    id: {pack_id}
    number: {number}
    type: content-pack
    priority: {priority}
    score: {score}
    status: {meta.get('status', '')}
    closed_loop_ready: {str(bool(meta.get('closed_loop_ready'))).lower()}
    ---

    # {title}

    ## Pack Links

    - Source folder: `content-packs/{pack_id}/`
    - Draft: `content-packs/{pack_id}/01_正文.md`
    - Publish packet: `content-packs/{pack_id}/02_发布包.md`
    - Template entry: `content-packs/{pack_id}/08_模板入口.md`
    - Feedback sheet: `content-packs/{pack_id}/07_48小时回流表.md`

    ## Trigger Profile

    - Category: {profile['category'] or 'unknown'}
    - Desire: {profile['desire'] or '待校准'}
    - Thought: {profile['thought'] or '待校准'}
    - Action: {profile['action'] or '待校准'}

    ## Publishing State

    - Priority: {priority or 'unknown'}
    - Current score: {score}/27
    - Publication refined: {meta.get('publication_refined', False)}
    - Evidence enriched: {meta.get('evidence_enriched', False)}
    - S+ candidate: {meta.get('s_plus_candidate', False)}

    ## Draft Excerpt

    {body_excerpt or '无正文摘录。'}

    ## Publish Packet Excerpt

    {publish_excerpt or '无发布包摘录。'}

    ## Template Entry Excerpt

    {template_excerpt or '无模板入口摘录。'}
    """).strip() + "\n"


def build_source_snapshot(pack_dir: Path, meta: dict[str, Any]) -> dict[str, Any]:
    pack_id = str(meta.get("id") or pack_dir.name)
    return {
        "id": pack_id,
        "title": str(meta.get("title") or pack_id),
        "priority": pack_priority(meta),
        "score": pack_score(meta),
        "status": str(meta.get("status") or ""),
        "closed_loop_ready": bool(meta.get("closed_loop_ready")),
        "trigger_profile": trigger_profile(meta),
        "files": {
            "draft": str(pack_dir / "01_正文.md"),
            "publish_packet": str(pack_dir / "02_发布包.md"),
            "xiaohongshu": str(pack_dir / "03_小红书版.md"),
            "zhihu": str(pack_dir / "04_知乎版.md"),
            "short_video": str(pack_dir / "05_短视频口播.md"),
            "comment_question": str(pack_dir / "06_评论回流问题.md"),
            "feedback_sheet": str(pack_dir / "07_48小时回流表.md"),
            "template_entry": str(pack_dir / "08_模板入口.md"),
        },
    }


def run(args: argparse.Namespace) -> int:
    ensure_dirs()
    meta_paths = sorted(PACKS_DIR.glob("问题*/meta.json"))
    if len(meta_paths) != 400:
        raise RuntimeError(f"expected 400 packs, found {len(meta_paths)}")

    topic_entries: list[tuple[int, str, str, int, str]] = []
    snapshots: list[dict[str, Any]] = []
    for meta_path in meta_paths:
        meta = load_meta(meta_path)
        pack_dir = meta_path.parent
        pack_id = str(meta.get("id") or pack_dir.name)
        number = int(meta.get("number") or re.sub(r"\D", "", pack_id))
        title = str(meta.get("title") or pack_id)
        priority = pack_priority(meta)
        score = pack_score(meta)

        if not args.dry_run:
            (KNOWLEDGE_DIR / "wiki" / "topics" / f"{pack_id}.md").write_text(build_pack_page(pack_dir, meta), encoding="utf-8")
        snapshots.append(build_source_snapshot(pack_dir, meta))
        topic_entries.append((number, pack_id, title, score, priority))

    if not args.dry_run:
        raw_path = KNOWLEDGE_DIR / "raw" / "sources" / "content-packs" / "400-content-packs.snapshot.json"
        raw_path.write_text(json.dumps(snapshots, ensure_ascii=False, indent=2), encoding="utf-8")

        topic_index = [
            "---",
            "id: topic-index",
            "type: topic-index",
            f"updated_at: {dt.date.today().isoformat()}",
            "---",
            "",
            "# 400 Content Pack Topic Index",
            "",
            "| Pack | Priority | Score | Title |",
            "|---|---|---:|---|",
        ]
        for _, pack_id, title, score, priority in sorted(topic_entries):
            topic_index.append(f"| [[{pack_id}]] | {priority} | {score} | {title.replace('|', '/')} |")
        (KNOWLEDGE_DIR / "wiki" / "topics" / "topic-index.md").write_text("\n".join(topic_index) + "\n", encoding="utf-8")

        index_path = KNOWLEDGE_DIR / "index.md"
        previous = index_path.read_text(encoding="utf-8") if index_path.exists() else "# ADHD × AI Self-Growing Knowledge Index\n"
        if "[[topic-index]]" not in previous:
            previous = previous.rstrip() + "\n\n## Topic Map\n\n- [[topic-index]] — all 400 content packs\n"
        index_path.write_text(previous.rstrip() + "\n", encoding="utf-8")

        log_path = KNOWLEDGE_DIR / "log.md"
        old = log_path.read_text(encoding="utf-8") if log_path.exists() else "# Knowledge Operation Log\n\n"
        line = f"- {dt.datetime.now().isoformat(timespec='seconds')} build-topic-export: 400 packs\n"
        if line not in old:
            log_path.write_text(old.rstrip() + "\n" + line, encoding="utf-8")

    print(f"[llm-wiki-export] exported {len(meta_paths)} packs" + (" (dry run)" if args.dry_run else ""))
    return 0


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Export 400 content packs into LLM-Wiki seed pages.")
    parser.add_argument("--dry-run", action="store_true")
    return parser.parse_args(argv)


if __name__ == "__main__":
    raise SystemExit(run(parse_args(sys.argv[1:])))
