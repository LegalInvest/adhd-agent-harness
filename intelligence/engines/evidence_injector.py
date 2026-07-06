#!/usr/bin/env python3
"""Evidence-to-pack injection engine.

Reads evidence cards with LLM analysis and injects upgrade notes into the
matching content packs. Never overwrites existing pack text — only appends
an `## 🧠 自生长引擎：证据升级建议` section at the end of 01_正文.md.

Also ranks packs by weakness and flags the most promising replacement targets.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import sys
from pathlib import Path
from collections import defaultdict

ROOT = Path(__file__).resolve().parents[1]
PACKS_DIR = ROOT / "content-packs"
EVIDENCE_DIR = ROOT / "knowledge" / "wiki" / "evidence"


class io:
    @staticmethod
    def ok(s: str) -> str:
        return f"[OK] {s}"

    @staticmethod
    def warn(s: str) -> str:
        return f"[WARN] {s}"

    @staticmethod
    def info(s: str) -> str:
        return f"[INFO] {s}"


def read_frontmatter(lines: list[str]) -> dict[str, str]:
    fm: dict[str, str] = {}
    for line in lines:
        line = line.strip()
        if ":" in line:
            k, v = line.split(":", 1)
            fm[k.strip()] = v.strip().strip('"')
    return fm


def load_evidence() -> list[dict]:
    """Parse all evidence cards from knowledge/wiki/evidence/."""
    evidence: list[dict] = []
    for f in sorted(EVIDENCE_DIR.glob("*.md")):
        text = f.read_text(encoding="utf-8")
        # Split frontmatter
        parts = text.split("---")
        fm = read_frontmatter(parts[1].strip().split("\n")) if len(parts) >= 3 else {}
        # Extract angle
        angle_match = re.search(r"## ADHD × AI Angle\n\n(.+?)(?:\n##|\n---|\Z)", text, re.DOTALL)
        angle = angle_match.group(1).strip() if angle_match else ""
        pack_ids = re.findall(r"\[\[(问题\d+)\]\]", text)
        url_match = re.search(r"- URL: (.+)", text)
        url = url_match.group(1).strip() if url_match else ""
        score = int(fm.get("score", 0))
        evidence.append({
            "id": fm.get("id", f.stem),
            "source": fm.get("source", ""),
            "score": score,
            "angle": angle,
            "url": url,
            "related_packs": pack_ids,
            "path": str(f),
        })
    return evidence


def load_pack_meta(pack_id: str) -> dict | None:
    meta_path = PACKS_DIR / pack_id / "meta.json"
    if not meta_path.exists():
        return None
    return json.loads(meta_path.read_text(encoding="utf-8"))


def inject_evidence_into_pack(pack_id: str, evidence_items: list[dict]) -> bool:
    """Append upgrade suggestions to 01_正文.md without modifying existing content."""
    draft_path = PACKS_DIR / pack_id / "01_正文.md"
    if not draft_path.exists():
        return False

    existing_text = draft_path.read_text(encoding="utf-8")
    marker = "## 🧠 自生长引擎：证据升级建议"
    header = marker + f"\n\n> 自动注入时间：{dt.datetime.now().strftime('%Y-%m-%d %H:%M')}\n> 来源：自生长引擎 LLM 分析\n"

    # Remove old injection block to start fresh
    if marker in existing_text:
        existing_text = existing_text.split(marker)[0].rstrip()

    notes = []
    for ev in evidence_items:
        if ev["angle"] and "LLM call failed" not in ev["angle"] and "No LLM note" not in ev["angle"]:
            notes.append(f"- 📄 [{ev['source']}]({ev['url']}) — {ev['angle']}")
    if not notes:
        return False

    new_block = header + "\n" + "\n".join(notes)
    draft_path.write_text(existing_text.rstrip() + "\n\n" + new_block + "\n", encoding="utf-8")
    return True


def rank_weak_packs(evidence: list[dict], min_score: int = 18) -> list[tuple[str, int, int, int]]:
    """Rank packs by (low current score, high evidence count) for replacement targeting."""
    pack_stats: dict[str, tuple[int, int, list[str]]] = defaultdict(lambda: (0, 0, []))

    for ev in evidence:
        for pid in ev["related_packs"]:
            evidence_count, _, sources = pack_stats[pid]
            pack_stats[pid] = (evidence_count + 1, 0, sources + [ev["source"]])

    # Load current scores
    ranked: list[tuple[str, int, int, int]] = []
    for pid, (ev_count, _, sources) in pack_stats.items():
        meta = load_pack_meta(pid)
        if not meta:
            continue
        current_score = int(meta.get("current_scores", {}).get("total", 0))
        priority = str(meta.get("priority", "D"))
        # Lower score + higher evidence = better replacement target
        ranked.append((pid, current_score, ev_count, priority))

    # Sort: low score first, within same score high evidence count first
    ranked.sort(key=lambda x: (x[1], -x[2]))
    return [(pid, score, ev, pri) for pid, score, ev, pri in ranked if score <= min_score]


def generate_weak_pack_report(weak_packs: list[tuple[str, int, int, int]], limit: int = 20) -> str:
    lines = [
        "# 弱题候选报告",
        f"\n> 生成时间：{dt.datetime.now().strftime('%Y-%m-%d %H:%M')}",
        f"> 策略：低分+高证据流入 = 优先考虑升级或替换",
        f"> 阈值：电流总分 ≤ 18 的内容包",
        "",
        "| 排名 | 包ID | 当前分 | 证据数 | 优先级 | 建议动作 |",
        "|---|---:|---:|---:|---:|---|",
    ]
    for rank, (pid, score, ev_count, priority) in enumerate(weak_packs[:limit], 1):
        if ev_count >= 5 and score < 15:
            action = "🔴 高优先级替换候选"
        elif ev_count >= 3:
            action = "🟡 证据强化优先"
        else:
            action = "🟢 观察"
        lines.append(f"| {rank} | {pid} | {score} | {ev_count} | {priority} | {action} |")

    lines.extend([
        "",
        "## 替换流程",
        "",
        "1. 人工确认替换目标和替换候选（新证据 vs 旧弱题）",
        "2. 备份旧包：`archive/topic-replacements/YYYY-MM-DD/{pack_id}/`",
        "3. 用新题重写 9 个资产文件",
        "4. 更新 `meta.json` → 旧编号保留，标题/标签/来源替换",
        "5. 更新 `indexes/400闭环资产总索引.md` 和 `research-inbox/replacement-log.md`",
    ])
    return "\n".join(lines)


def run(args: argparse.Namespace) -> int:
    evidence = load_evidence()
    real_evidence = [e for e in evidence if e["angle"] and "LLM call failed" not in e["angle"]]

    if not real_evidence:
        print("No evidence cards with LLM analysis found. Run self_growing_engine.py first.")
        return 1

    pack_evidence: dict[str, list[dict]] = defaultdict(list)
    for ev in real_evidence:
        for pid in ev["related_packs"]:
            pack_evidence[pid].append(ev)

    if not args.no_inject:
        injected = 0
        for pid, evs in pack_evidence.items():
            if inject_evidence_into_pack(pid, evs[:3]):
                injected += 1
                if not args.quiet:
                    print(f"  [OK] {pid} <- {len(evs[:3])} evidence notes")
        print(f"\n[OK] Injected evidence into {injected} packs.")

    # Generate weak pack report
    weak = rank_weak_packs(evidence, min_score=args.max_score)
    report = generate_weak_pack_report(weak, limit=args.top_n)
    report_path = ROOT / "research-inbox" / "weak-pack-replacement-report.md"
    report_path.write_text(report, encoding="utf-8")
    print(f"[INFO] Weak pack report: {report_path}")
    print(f"  {len(weak)} packs below score {args.max_score}, top {min(args.top_n, len(weak))} listed.")

    # Write pack-level evidence summary
    summary_lines = ["# 包级证据摘要", f"\n> 生成时间：{dt.datetime.now().strftime('%Y-%m-%d %H:%M')}", ""]
    for pid, evs in sorted(pack_evidence.items(), key=lambda x: -len(x[1])):
        meta = load_pack_meta(pid)
        score = int(meta.get("current_scores", {}).get("total", 0)) if meta else 0
        summary_lines.append(f"## {pid} (当前分:{score}/27, 证据:{len(evs)}条)")
        for ev in sorted(evs, key=lambda x: -x["score"])[:3]:
            summary_lines.append(f"- [{ev['score']}/25] {ev['source']}: {ev['angle'][:120]}")
        summary_lines.append("")
    (ROOT / "research-inbox" / "pack-evidence-summary.md").write_text("\n".join(summary_lines), encoding="utf-8")

    return 0


def parse_args(argv: list[str]) -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Inject evidence into content packs and rank weak ones.")
    p.add_argument("--no-inject", action="store_true", help="Skip actual file injection, only report")
    p.add_argument("--max-score", type=int, default=18, help="Max current score for weak pack consideration")
    p.add_argument("--top-n", type=int, default=20, help="Top N weak packs to list")
    p.add_argument("--quiet", action="store_true")
    return p.parse_args(argv)


if __name__ == "__main__":
    raise SystemExit(run(parse_args(sys.argv[1:])))
