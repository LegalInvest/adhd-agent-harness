#!/usr/bin/env python3
"""Self-growing engine for the ADHD × AI 400-pack content pool.

The engine is intentionally non-destructive. It collects and scores new
materials, writes evidence cards and upgrade/replacement candidates, and exports
LLM-Wiki-compatible knowledge files. Evidence injection into content packs is
handled by `evidence_injector.py` which runs as step 2 in the daily pipeline.
"""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import os
import re
import sys
import textwrap
import urllib.error
import urllib.request
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

try:
    import feedparser  # type: ignore
except ImportError:  # pragma: no cover - surfaced in main preflight
    feedparser = None

ROOT = Path(__file__).resolve().parents[1]
CONFIG_PATH = ROOT / "config" / "self_growing_engine.config.json"
PACKS_DIR = ROOT / "content-packs"
RESEARCH_INBOX = ROOT / "research-inbox"
KNOWLEDGE_DIR = ROOT / "knowledge"
LOGS_DIR = ROOT / "logs"

ADHD_TERMS = {
    "adhd", "executive", "function", "attention", "focus", "dopamine",
    "procrastination", "neurodiversity", "neurodivergent", "accommodation",
    "disability", "burnout", "impulsivity", "hyperfocus", "working memory",
    "执行", "注意", "专注", "多巴胺", "拖延", "神经多样性", "合理便利",
}

AI_TERMS = {
    "ai", "agent", "agentic", "llm", "claude", "gemini", "chatgpt", "openai",
    "anthropic", "google", "algorithm", "automation", "workflow", "cognitive offloading",
    "diagnosis", "hiring", "digital therapeutic", "人工智能", "大模型", "智能体", "算法",
}

PRODUCT_TERMS = {
    "template", "checklist", "workflow", "agent", "tool", "dashboard", "tracker",
    "prompt", "form", "system", "表", "清单", "模板", "工具", "工作流", "看板", "提示词",
}

URL_RE = re.compile(r"https?://\S+", re.IGNORECASE)
TOKEN_RE = re.compile(r"[A-Za-z0-9_\-一-鿿]{2,}")


@dataclass(frozen=True)
class PackMeta:
    pack_id: str
    number: int
    title: str
    priority: str
    score_total: int
    path: Path
    keywords: set[str] = field(default_factory=set)


@dataclass
class EvidenceItem:
    id: str
    title: str
    url: str
    source: str
    source_type: str
    reliability: str
    summary: str
    published_at: str
    collected_at: str
    related_pack_ids: list[str]
    dimensions: dict[str, int]
    total_score: int
    recommended_action: str
    llm_note: str = ""

    def to_json(self) -> dict[str, Any]:
        return {
            "id": self.id,
            "title": self.title,
            "url": self.url,
            "source": self.source,
            "source_type": self.source_type,
            "reliability": self.reliability,
            "summary": self.summary,
            "published_at": self.published_at,
            "collected_at": self.collected_at,
            "related_pack_ids": self.related_pack_ids,
            "dimensions": self.dimensions,
            "total_score": self.total_score,
            "recommended_action": self.recommended_action,
            "llm_note": self.llm_note,
        }


def load_config() -> dict[str, Any]:
    if not CONFIG_PATH.exists():
        raise FileNotFoundError(f"missing config: {CONFIG_PATH}")
    return json.loads(CONFIG_PATH.read_text(encoding="utf-8"))


def load_dotenv(path: Path) -> None:
    # The shell environment may have a stale or unreachable ANTHROPIC_BASE_URL
    # (e.g. an overseas proxy). Allow a local .env to override these keys.
    _FORCE_OVERRIDE = {"ANTHROPIC_BASE_URL", "ANTHROPIC_API_KEY", "LLM_ANTHROPIC_MODEL"}
    if not path.exists():
        return
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        if not key:
            continue
        if key not in os.environ or key in _FORCE_OVERRIDE:
            os.environ[key] = value


def slug_id(text: str, length: int = 12) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()[:length]


def today_string() -> str:
    return dt.date.today().isoformat()


def ensure_dirs() -> None:
    for path in [RESEARCH_INBOX / "daily-scout", KNOWLEDGE_DIR / "raw" / "sources", KNOWLEDGE_DIR / "wiki" / "daily", KNOWLEDGE_DIR / "wiki" / "evidence", KNOWLEDGE_DIR / "wiki" / "topics", LOGS_DIR]:
        path.mkdir(parents=True, exist_ok=True)


def tokenize(text: str) -> set[str]:
    return {m.group(0).lower() for m in TOKEN_RE.finditer(text)}


def load_pack_metas() -> list[PackMeta]:
    packs: list[PackMeta] = []
    for meta_path in sorted(PACKS_DIR.glob("问题*/meta.json")):
        try:
            meta = json.loads(meta_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            raise ValueError(f"invalid meta json: {meta_path}: {exc}") from exc
        pack_id = str(meta.get("id") or meta_path.parent.name)
        number = int(meta.get("number") or re.sub(r"\D", "", pack_id))
        title = str(meta.get("title") or pack_id)
        priority = str(meta.get("priority") or "")
        scores = meta.get("current_scores") or {}
        score_total = int(scores.get("total") or 0)
        trigger = meta.get("current_trigger_profile") or {}
        keyword_text = " ".join([
            title,
            priority,
            str(trigger.get("category") or ""),
            str(trigger.get("desire_trigger") or ""),
            str(trigger.get("thought_trigger") or ""),
            str(trigger.get("action_trigger") or ""),
        ])
        packs.append(PackMeta(pack_id, number, title, priority, score_total, meta_path.parent, tokenize(keyword_text)))
    if len(packs) != 400:
        raise RuntimeError(f"expected 400 content packs, found {len(packs)} under {PACKS_DIR}")
    return packs


def reliability_score(value: str) -> int:
    value = value.upper().strip()
    if value.startswith("A"):
        return 5
    if value.startswith("B"):
        return 4
    if value.startswith("C"):
        return 3
    return 2


def score_item(title: str, summary: str, source_type: str, reliability: str) -> dict[str, int]:
    text = f"{title} {summary}".lower()
    tokens = tokenize(text)
    adhd_hits = len(tokens & ADHD_TERMS) + sum(1 for term in ADHD_TERMS if " " in term and term in text)
    ai_hits = len(tokens & AI_TERMS) + sum(1 for term in AI_TERMS if " " in term and term in text)
    product_hits = len(tokens & PRODUCT_TERMS) + sum(1 for term in PRODUCT_TERMS if " " in term and term in text)

    pain = min(5, 1 + adhd_hits)
    intersection = min(5, 1 + min(adhd_hits, 2) + min(ai_hits, 2))
    evidence = min(5, reliability_score(reliability) + (1 if source_type in {"paper", "policy", "public_health_data", "medical_boundary", "organization_case"} else 0))
    product = min(5, 1 + product_hits + (1 if "agent" in text or "workflow" in text or "模板" in text else 0))
    feedback = min(5, 1 + min(adhd_hits + product_hits, 4))
    return {
        "pain_intensity": pain,
        "adhd_ai_intersection": intersection,
        "evidence_strength": evidence,
        "product_entry_potential": product,
        "feedback_potential": feedback,
    }


def classify_action(total_score: int, config: dict[str, Any]) -> str:
    daily = config["daily_scout"]
    if total_score >= int(daily["min_s_plus_candidate_score"]):
        return "S+-upgrade candidate"
    if total_score >= int(daily["min_replacement_candidate_score"]):
        return "replacement-or-S-upgrade candidate"
    if total_score >= int(daily["min_evidence_score"]):
        return "evidence enrich"
    return "archive only"


def match_related_packs(title: str, summary: str, packs: list[PackMeta], explicit_ids: list[str] | None = None) -> list[str]:
    if explicit_ids:
        return explicit_ids[:8]
    tokens = tokenize(f"{title} {summary}")
    scored: list[tuple[int, PackMeta]] = []
    for pack in packs:
        overlap = len(tokens & pack.keywords)
        if overlap:
            scored.append((overlap, pack))
    scored.sort(key=lambda x: (x[0], x[1].score_total, x[1].priority), reverse=True)
    return [pack.pack_id for _, pack in scored[:8]]


def normalize_url(url: str) -> str:
    return url.strip().rstrip(")].,，。")


def collect_curated(config: dict[str, Any], packs: list[PackMeta], run_date: str) -> list[EvidenceItem]:
    items: list[EvidenceItem] = []
    for source in config.get("curated_sources", []):
        title = str(source["title"])
        url = normalize_url(str(source["url"]))
        summary = str(source.get("summary") or "")
        dimensions = score_item(title, summary, str(source.get("source_type") or "reference"), str(source.get("reliability") or "B"))
        total = sum(dimensions.values())
        related = match_related_packs(title, summary, packs, [str(x) for x in source.get("related_pack_ids", [])])
        items.append(EvidenceItem(
            id=f"src_{slug_id(url)}",
            title=title,
            url=url,
            source=str(source.get("source") or "curated"),
            source_type=str(source.get("source_type") or "reference"),
            reliability=str(source.get("reliability") or "B"),
            summary=summary,
            published_at="",
            collected_at=run_date,
            related_pack_ids=related,
            dimensions=dimensions,
            total_score=total,
            recommended_action=classify_action(total, config),
        ))
    return items


def entry_value(entry: Any, key: str, default: str = "") -> str:
    value = getattr(entry, key, default)
    if value is None:
        return default
    return str(value)


def collect_rss(config: dict[str, Any], packs: list[PackMeta], run_date: str, limit: int) -> list[EvidenceItem]:
    if feedparser is None:
        raise RuntimeError("feedparser is required. Install with: pip install feedparser")
    items: list[EvidenceItem] = []
    for source in config.get("rss_sources", []):
        if len(items) >= limit:
            break
        url = str(source["url"])
        try:
            feed = feedparser.parse(url)
        except Exception as exc:  # feedparser can raise network/parser errors
            print(f"[warn] RSS parse failed: {source.get('name')}: {exc}", file=sys.stderr)
            continue
        for entry in feed.entries[: max(3, limit // max(1, len(config.get("rss_sources", []))))]:
            title = entry_value(entry, "title").strip()
            link = normalize_url(entry_value(entry, "link"))
            summary = re.sub(r"<[^>]+>", " ", entry_value(entry, "summary") or entry_value(entry, "description"))
            summary = re.sub(r"\s+", " ", summary).strip()[:800]
            if not title or not link:
                continue
            dimensions = score_item(title, summary, str(source.get("source_type") or "rss"), str(source.get("reliability") or "B"))
            total = sum(dimensions.values())
            related = match_related_packs(title, summary, packs)
            if total < 8 and not related:
                continue
            items.append(EvidenceItem(
                id=f"rss_{slug_id(link)}",
                title=title[:220],
                url=link,
                source=str(source.get("name") or "RSS"),
                source_type=str(source.get("source_type") or "rss"),
                reliability=str(source.get("reliability") or "B"),
                summary=summary[:800],
                published_at=entry_value(entry, "published") or entry_value(entry, "updated"),
                collected_at=run_date,
                related_pack_ids=related,
                dimensions=dimensions,
                total_score=total,
                recommended_action=classify_action(total, config),
            ))
            if len(items) >= limit:
                break
    return items


def collect_manual_inputs(config: dict[str, Any], packs: list[PackMeta], run_date: str) -> list[EvidenceItem]:
    manual_path = RESEARCH_INBOX / "manual-input.json"
    if not manual_path.exists():
        manual_path.write_text("[]\n", encoding="utf-8")
        return []
    data = json.loads(manual_path.read_text(encoding="utf-8"))
    if not isinstance(data, list):
        raise ValueError(f"manual input must be a JSON array: {manual_path}")
    items: list[EvidenceItem] = []
    for row in data:
        if not isinstance(row, dict):
            raise ValueError("each manual input item must be an object")
        title = str(row.get("title") or "").strip()
        url = normalize_url(str(row.get("url") or ""))
        summary = str(row.get("summary") or "").strip()
        if not title or not url:
            raise ValueError("manual input items require title and url")
        dimensions = score_item(title, summary, str(row.get("source_type") or "manual"), str(row.get("reliability") or "B"))
        total = sum(dimensions.values())
        related = match_related_packs(title, summary, packs, [str(x) for x in row.get("related_pack_ids", [])])
        items.append(EvidenceItem(
            id=f"manual_{slug_id(url + title)}",
            title=title,
            url=url,
            source=str(row.get("source") or "manual"),
            source_type=str(row.get("source_type") or "manual"),
            reliability=str(row.get("reliability") or "B"),
            summary=summary,
            published_at=str(row.get("published_at") or ""),
            collected_at=run_date,
            related_pack_ids=related,
            dimensions=dimensions,
            total_score=total,
            recommended_action=classify_action(total, config),
        ))
    if items:
        backup = RESEARCH_INBOX / f"manual-input-processed-{run_date}.json"
        backup.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
        manual_path.write_text("[]\n", encoding="utf-8")
    return items


def call_llm_if_configured(items: list[EvidenceItem], config: dict[str, Any]) -> None:
    """Annotate items with optional LLM analysis.

    The engine remains useful without API keys. If credentials are present, it
    asks the model only for a short judgment note and adjusted dimension hints;
    raw source facts remain preserved separately.
    """
    if not items:
        return
    provider = ""
    if os.environ.get("ANTHROPIC_API_KEY"):
        provider = "anthropic"
    elif os.environ.get("GOOGLE_API_KEY"):
        provider = "google"
    if not provider:
        for item in items:
            item.llm_note = "LLM not configured; scored by local rules."
        return

    # Batch items through LLM at 12 items per call to stay within token limits
    # while covering the full collected set.
    batch_size = 12
    for batch_start in range(0, len(items), batch_size):
        batch = items[batch_start : batch_start + batch_size]
        payload_items = [
            {
                "id": item.id,
                "title": item.title,
                "summary": item.summary[:400],
                "score": item.total_score,
                "related_pack_ids": item.related_pack_ids[:5],
            }
            for item in batch
        ]
        prompt = (
            "You are auditing ADHD × AI content evidence for a Chinese content system. "
            "For each item, return one short Chinese note on how it can upgrade a content pack. "
            "Do not invent facts beyond title/summary. JSON object id->note only.\n\n"
            + json.dumps(payload_items, ensure_ascii=False)
        )
        try:
            notes = call_llm_json(provider, prompt, config)
        except Exception as exc:
            for item in batch:
                item.llm_note = f"LLM call failed; local score kept. Error: {type(exc).__name__}"
            continue
        if not isinstance(notes, dict):
            for item in batch:
                item.llm_note = "LLM returned non-object; local score kept."
            continue
        for item in batch:
            note = notes.get(item.id)
            item.llm_note = str(note)[:500] if note else "No LLM note returned for this item."


def call_llm_json(provider: str, prompt: str, config: dict[str, Any]) -> Any:
    if provider == "anthropic":
        # Allow local proxy routers (e.g. anyrouter or litellm) running at
        # ANTHROPIC_BASE_URL. When that env is set the engine calls it instead
        # of the vanilla api.anthropic.com endpoint. Auth tokens are expected to
        # be handled by the proxy itself; we still send the X-Api-Key header so
        # that proxy implementations that forward it upstream work too.
        api_key = os.environ.get("ANTHROPIC_API_KEY") or os.environ.get("ANTHROPIC_AUTH_TOKEN") or "proxy-managed"
        base_url = os.environ.get("ANTHROPIC_BASE_URL", "https://api.anthropic.com").rstrip("/")
        model = config["llm"].get("anthropic_model", "claude-sonnet-4-6")
        body = {
            "model": model,
            "max_tokens": 4000,
            "messages": [{"role": "user", "content": prompt}],
        }
        req = urllib.request.Request(
            f"{base_url}/v1/messages",
            data=json.dumps(body).encode("utf-8"),
            headers={
                "content-type": "application/json",
                "x-api-key": api_key,
                "anthropic-version": "2023-06-01",
            },
            method="POST",
        )
        with urllib.request.urlopen(req, timeout=60) as resp:
            data = json.loads(resp.read().decode("utf-8"))
        # Handle extended-thinking content blocks (type=thinking + thinking field)
        # as well as standard text blocks.
        content_blocks = data["content"]
        full_text = ""
        for block in content_blocks:
            full_text += block.get("text") or block.get("thinking") or ""
        if not full_text:
            raise ValueError(f"No text/thinking found in response content blocks: {json.dumps([{k:v for k,v in b.items() if k!='signature'} for b in content_blocks[:2]])[:300]}")
        return parse_json_from_text(full_text)

    if provider == "google":
        from google import genai  # type: ignore

        client = genai.Client(api_key=os.environ["GOOGLE_API_KEY"])
        model = config["llm"].get("google_model", "gemini-2.5-flash")
        resp = client.models.generate_content(model=model, contents=prompt)
        return parse_json_from_text(resp.text or "{}")

    raise ValueError(f"unsupported provider: {provider}")


def parse_json_from_text(text: str) -> Any:
    text = text.strip()
    if text.startswith("```"):
        text = re.sub(r"^```(?:json)?\s*", "", text)
        text = re.sub(r"\s*```$", "", text)
    # Find the *last* balanced JSON object, because some extended-thinking
    # models emit reasoning then repeat the same JSON.
    # Also accept the first complete object if no repeated one is found.
    candidates = []
    depth = 0
    start = -1
    for i, ch in enumerate(text):
        if ch == "{":
            if depth == 0:
                start = i
            depth += 1
        elif ch == "}":
            depth -= 1
            if depth == 0 and start >= 0:
                candidates.append(text[start : i + 1])
                start = -1
    if not candidates:
        raise ValueError(f"No complete JSON object found in: {text[:800]}")
    # Return the last (usually the cleanest, post-reasoning) object
    return json.loads(candidates[-1])


def dedupe_items(items: list[EvidenceItem]) -> list[EvidenceItem]:
    seen: set[str] = set()
    out: list[EvidenceItem] = []
    for item in items:
        key = item.url.lower()
        if key in seen:
            continue
        seen.add(key)
        out.append(item)
    return out


def existing_text(path: Path) -> str:
    return path.read_text(encoding="utf-8") if path.exists() else ""


def append_once(path: Path, block: str, marker: str) -> None:
    text = existing_text(path)
    if marker in text:
        return
    prefix = "" if text.endswith("\n") or not text else "\n"
    path.write_text(text + prefix + block.rstrip() + "\n", encoding="utf-8")


def format_daily_scout(run_date: str, items: list[EvidenceItem], config: dict[str, Any]) -> str:
    lines = [
        "# ADHD x AI / Agentic AI Daily Scout",
        "",
        f"日期：{run_date}",
        "",
        "## 查询组",
        "",
    ]
    for query in config.get("queries", []):
        lines.append(f"- {query}")
    lines.extend(["", "## 本日有效来源", ""])
    if not items:
        lines.append("本日没有采集到达到入库阈值的新来源。")
    for idx, item in enumerate(sorted(items, key=lambda x: x.total_score, reverse=True), 1):
        packs = "、".join(item.related_pack_ids[:8]) or "待人工匹配"
        lines.extend([
            f"### {idx}. {item.title}",
            "",
            f"- URL: {item.url}",
            f"- 来源：{item.source}",
            f"- 类型：{item.source_type}",
            f"- 可信度：{item.reliability}",
            f"- 总分：{item.total_score}/25",
            f"- 建议动作：{item.recommended_action}",
            f"- 可升级包：{packs}",
            "",
            f"核心沉淀：{item.summary or '待人工摘录。'}",
            "",
            f"LLM/本地判断：{item.llm_note}",
            "",
        ])
    return "\n".join(lines).rstrip() + "\n"


def write_source_ledger(items: list[EvidenceItem]) -> None:
    path = RESEARCH_INBOX / "source-ledger.md"
    if not path.exists():
        path.write_text("# Source Ledger\n\n| Date | Source | Title | URL | Reliability | Related packs | Action |\n|---|---|---|---|---|---|---|\n", encoding="utf-8")
    text = path.read_text(encoding="utf-8")
    additions = []
    for item in items:
        if item.url in text:
            continue
        packs = ", ".join(item.related_pack_ids[:8])
        additions.append(f"| {item.collected_at} | {item.source} | {item.title.replace('|', '/')} | {item.url} | {item.reliability} | {packs} | {item.recommended_action} |")
    if additions:
        path.write_text(text.rstrip() + "\n" + "\n".join(additions) + "\n", encoding="utf-8")


def write_evidence_cards(items: list[EvidenceItem]) -> None:
    path = RESEARCH_INBOX / "evidence-cards.md"
    if not path.exists():
        path.write_text("# Evidence Cards\n\n每张 evidence card 只记录一个可复用证据，不混写多个观点。\n", encoding="utf-8")
    blocks = []
    text = path.read_text(encoding="utf-8")
    for item in items:
        marker = f"Evidence Card {item.id}"
        if marker in text:
            continue
        packs = ", ".join(item.related_pack_ids[:8]) or "待人工匹配"
        dims = ", ".join(f"{k}={v}" for k, v in item.dimensions.items())
        blocks.append(textwrap.dedent(f"""
        ### {marker}

        - Date: {item.collected_at}
        - Source: {item.source}
        - URL: {item.url}
        - Evidence type: {item.source_type}
        - Claim supported: {item.summary or '待人工摘录'}
        - ADHD × AI angle: {item.llm_note or '待人工判断'}
        - Reliability: {item.reliability}
        - Related packs: {packs}
        - Score: {item.total_score}/25 ({dims})
        - Possible action: {item.recommended_action}
        """).strip())
    if blocks:
        path.write_text(text.rstrip() + "\n\n" + "\n\n".join(blocks) + "\n", encoding="utf-8")


def write_replacement_candidates(items: list[EvidenceItem], config: dict[str, Any]) -> None:
    threshold = int(config["daily_scout"]["min_replacement_candidate_score"])
    candidates = [item for item in items if item.total_score >= threshold]
    path = RESEARCH_INBOX / "replacement-candidates.md"
    if not path.exists():
        path.write_text("# Replacement Candidates\n\n| Candidate | Score | Evidence | Replace Target | Reason | Status |\n|---|---:|---|---|---|---|\n", encoding="utf-8")
    text = path.read_text(encoding="utf-8")
    rows = []
    for item in candidates:
        if item.id in text or item.url in text:
            continue
        target = "暂不自动替换，先补强 " + ("/".join(item.related_pack_ids[:4]) if item.related_pack_ids else "待人工匹配包")
        reason = (item.summary or item.llm_note or "新证据强于普通泛观点，需要人工判断承载包。")[:120].replace("|", "/")
        rows.append(f"| {item.collected_at}: {item.title.replace('|', '/')} <!-- {item.id} --> | {item.total_score} | {item.source} + {item.reliability} | {target} | {reason} | {item.recommended_action} |")
    if rows:
        path.write_text(text.rstrip() + "\n" + "\n".join(rows) + "\n", encoding="utf-8")


def write_upgrade_board_notes(items: list[EvidenceItem], run_date: str) -> None:
    strong = [item for item in items if item.total_score >= 14 and item.related_pack_ids]
    if not strong:
        return
    path = RESEARCH_INBOX / "s-plus-upgrade-board.md"
    if not path.exists():
        path.write_text("# S+ Upgrade Board\n\n", encoding="utf-8")
    marker = f"## {run_date} Scout Upgrade Notes"
    if marker in path.read_text(encoding="utf-8"):
        return
    lines = [marker, "", "| Evidence | Score | Related packs | Next action |", "|---|---:|---|---|"]
    for item in sorted(strong, key=lambda x: x.total_score, reverse=True)[:12]:
        lines.append(f"| {item.title.replace('|', '/')} | {item.total_score} | {', '.join(item.related_pack_ids[:6])} | {item.recommended_action} |")
    append_once(path, "\n".join(lines), marker)


def wiki_link(name: str) -> str:
    return f"[[{name}]]"


def write_llm_wiki_exports(items: list[EvidenceItem], run_date: str) -> None:
    raw_path = KNOWLEDGE_DIR / "raw" / "sources" / f"{run_date}-scout.json"
    raw_path.write_text(json.dumps([item.to_json() for item in items], ensure_ascii=False, indent=2), encoding="utf-8")

    daily_path = KNOWLEDGE_DIR / "wiki" / "daily" / f"{run_date}.md"
    daily_lines = ["---", f"date: {run_date}", "type: daily-scout", "---", "", f"# Daily Scout {run_date}", ""]
    for item in sorted(items, key=lambda x: x.total_score, reverse=True):
        daily_lines.append(f"- {wiki_link(item.id)} — {item.title} ({item.total_score}/25)")
    daily_path.write_text("\n".join(daily_lines).rstrip() + "\n", encoding="utf-8")

    for item in items:
        evidence_path = KNOWLEDGE_DIR / "wiki" / "evidence" / f"{item.id}.md"
        related_links = " ".join(wiki_link(pid) for pid in item.related_pack_ids[:8])
        lines = [
            "---",
            f"id: {item.id}",
            "type: evidence-card",
            f"source: {json.dumps(item.source, ensure_ascii=False)}",
            f"source_type: {item.source_type}",
            f"reliability: {item.reliability}",
            f"score: {item.total_score}",
            f"collected_at: {item.collected_at}",
            "---",
            "",
            f"# {item.title}",
            "",
            f"- URL: {item.url}",
            f"- Related packs: {related_links or '待人工匹配'}",
            f"- Recommended action: {item.recommended_action}",
            "",
            "## Claim Supported",
            "",
            item.summary or "待人工摘录。",
            "",
            "## ADHD × AI Angle",
            "",
            item.llm_note or "待人工判断。",
            "",
            "## Dimension Scores",
            "",
            json.dumps(item.dimensions, ensure_ascii=False, indent=2),
            "",
        ]
        evidence_path.write_text("\n".join(lines), encoding="utf-8")

    update_knowledge_index(run_date, items)


def update_knowledge_index(run_date: str, items: list[EvidenceItem]) -> None:
    schema_path = KNOWLEDGE_DIR / "schema.md"
    if not schema_path.exists():
        schema_path.write_text("""# ADHD × AI LLM-Wiki Schema

This local knowledge export follows the LLM-Wiki pattern:

- `raw/sources/`: immutable source snapshots produced by daily scout runs.
- `wiki/daily/`: daily scout digest pages.
- `wiki/evidence/`: one evidence card per reusable source.
- `wiki/topics/`: one seed page per content pack, generated separately.
- `index.md`: navigation entry point.
- `log.md`: chronological operation log.

The content engine is non-destructive. Evidence can recommend upgrades or
replacements, but actual content-pack replacement requires explicit human approval
and an archive entry under `archive/topic-replacements/`.
""")

    index_path = KNOWLEDGE_DIR / "index.md"
    evidence_lines = [f"- [[{item.id}]] — {item.title} ({item.total_score}/25)" for item in sorted(items, key=lambda x: x.total_score, reverse=True)[:20]]
    index_path.write_text(f"""# ADHD × AI Self-Growing Knowledge Index

## Current Entrypoints

- [[{run_date}]] — latest daily scout
- [[topic-index]] — 400 content pack seed pages
- `schema.md` — local LLM-Wiki schema
- `log.md` — operation log

## Latest Evidence Cards

{chr(10).join(evidence_lines) if evidence_lines else '- No evidence cards in latest run.'}
""")

    log_path = KNOWLEDGE_DIR / "log.md"
    log_line = f"- {dt.datetime.now().isoformat(timespec='seconds')} daily-scout {run_date}: {len(items)} items\n"
    old = log_path.read_text(encoding="utf-8") if log_path.exists() else "# Knowledge Operation Log\n\n"
    if log_line not in old:
        log_path.write_text(old.rstrip() + "\n" + log_line, encoding="utf-8")


def write_run_outputs(items: list[EvidenceItem], config: dict[str, Any], run_date: str, dry_run: bool) -> None:
    if dry_run:
        print(format_daily_scout(run_date, items, config))
        return
    ensure_dirs()
    daily_path = RESEARCH_INBOX / "daily-scout" / f"{run_date}.md"
    daily_path.write_text(format_daily_scout(run_date, items, config), encoding="utf-8")
    write_source_ledger(items)
    write_evidence_cards(items)
    write_replacement_candidates(items, config)
    write_upgrade_board_notes(items, run_date)
    write_llm_wiki_exports(items, run_date)


def run(args: argparse.Namespace) -> int:
    load_dotenv(ROOT / ".env")
    config = load_config()
    run_date = args.date or today_string()
    ensure_dirs()
    packs = load_pack_metas()

    limit = args.limit or int(config["daily_scout"]["max_items_per_run"])
    items: list[EvidenceItem] = []
    items.extend(collect_curated(config, packs, run_date))
    items.extend(collect_manual_inputs(config, packs, run_date))
    try:
        items.extend(collect_rss(config, packs, run_date, limit=max(0, limit - len(items))))
    except (RuntimeError, urllib.error.URLError) as exc:
        print(f"[warn] RSS collection degraded: {exc}", file=sys.stderr)

    items = dedupe_items(items)
    items.sort(key=lambda x: x.total_score, reverse=True)
    if len(items) > limit:
        items = items[:limit]
    if not args.no_llm:
        call_llm_if_configured(items, config)
    write_run_outputs(items, config, run_date, args.dry_run)
    print(f"[self-growing-engine] {run_date}: wrote {len(items)} evidence items" + (" (dry run)" if args.dry_run else ""))
    return 0


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run the ADHD × AI self-growing daily scout.")
    parser.add_argument("--date", help="Run date YYYY-MM-DD. Defaults to today.")
    parser.add_argument("--limit", type=int, default=0, help="Maximum evidence items to keep.")
    parser.add_argument("--dry-run", action="store_true", help="Print outputs without writing files.")
    parser.add_argument("--no-llm", action="store_true", help="Disable optional live LLM annotation even if API keys exist.")
    return parser.parse_args(argv)


if __name__ == "__main__":
    raise SystemExit(run(parse_args(sys.argv[1:])))
