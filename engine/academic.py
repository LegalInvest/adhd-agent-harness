"""
学术大规模检索（双域语料）

从开放学术数据库批量抓取「ADHD（神经/心理）」与「Agentic Harness（LLM/agent 工程）」
两域的论文摘要，目标两域各数万篇，构成同构论证的真实证据底座。

数据源（均免费、无需 key）：
  - OpenAlex   : 2.5 亿+ 文献，cursor 分页，两域主力
  - arXiv      : cs.AI / cs.CL / cs.LG，harness 工程
  - Europe PMC : 生物医学 / 神经科学，ADHD 主力

每条记录统一为：
  {id, title, abstract, year, venue, doi, url, cited_by, source, domain, query}
"""

from __future__ import annotations

import json
import os
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")
ACADEMIC_FILE = os.path.join(DATA_DIR, "academic_corpus.json")

# 礼貌联系邮箱（OpenAlex polite pool），可被环境变量覆盖
MAILTO = os.environ.get("OPENALEX_MAILTO", "research@abcoding.dev")
USER_AGENT = f"ABCoding-ResearchBot/1.0 (mailto:{MAILTO})"


# ───────────────────────── 检索词 ─────────────────────────

ADHD_QUERIES = [
    "ADHD attention deficit hyperactivity disorder",
    "ADHD executive function deficit",
    "ADHD working memory",
    "ADHD dopamine reward prediction",
    "ADHD time perception time blindness",
    "ADHD emotional dysregulation",
    "ADHD inhibition impulsivity self-control",
    "ADHD default mode network",
    "ADHD prefrontal cortex cognitive control",
    "ADHD digital intervention app",
    "ADHD cognitive training",
    "ADHD self-regulation strategies",
    "ADHD task initiation procrastination",
    "ADHD external scaffolding support",
    "ADHD assistive technology",
    "ADHD hyperfocus attention",
    "ADHD adults workplace productivity",
    "ADHD children academic intervention",
    "ADHD machine learning diagnosis EEG",
    "ADHD neurofeedback treatment",
    "ADHD reward feedback delay discounting",
    "ADHD credit assignment causal learning",
    "ADHD cognitive load working memory capacity",
    "ADHD reinforcement learning behavior",
    "ADHD goal setting motivation feedback",
    "ADHD error monitoring performance feedback",
    "ADHD delay aversion reward timing",
    "ADHD metacognition self-monitoring",
]

HARNESS_QUERIES = [
    "large language model agent",
    "LLM tool use function calling",
    "retrieval augmented generation",
    "LLM hallucination mitigation",
    "LLM agent memory architecture",
    "context window management long context",
    "chain of thought reasoning LLM",
    "self-consistency self-critique LLM",
    "LLM planning task decomposition",
    "human in the loop LLM oversight",
    "agent orchestration framework",
    "LLM reasoning reliability verification",
    "prompt engineering instruction following",
    "LLM temperature sampling decoding",
    "autonomous agent scaffolding",
    "LLM grounding external knowledge",
    "agentic workflow planner executor",
    "language model alignment guardrails",
    "vector database semantic memory agent",
    "LLM goal drift long horizon task",
    "multi-agent system coordination LLM",
    "reflection self-improvement language model agent",
    "in-context learning few-shot prompting",
    "reinforcement learning human feedback RLHF",
    "code generation programming agent",
    "ReAct reasoning acting language model",
    "memory augmented neural network",
    "knowledge grounding factuality language model",
    "tool augmented language model API",
    "long-term memory conversational agent",
    "cognitive architecture artificial agent",
    "working memory artificial neural network",
    "episodic memory AI agent",
    "external memory transformer",
    "agent benchmark evaluation reasoning",
    "instruction tuning fine-tuning language model",
    "scratchpad intermediate reasoning steps",
    "self-reflection error correction LLM",
    "task planning robot language model",
    "credit assignment reinforcement learning agent",
    "reward shaping sparse reward agent",
    "process reward model step-level feedback",
    "cognitive load context length degradation LLM",
    "delayed reward long horizon credit assignment",
    "feedback loop self-improving agent",
    "agent evaluation reward hacking alignment",
    "temporal credit assignment sequence learning",
]

ARXIV_QUERIES = [
    "large language model agent",
    "tool use function calling LLM",
    "retrieval augmented generation",
    "hallucination language model",
    "agent memory long context",
    "chain of thought reasoning",
    "self critique verification LLM",
    "task decomposition planning agent",
    "human in the loop language model",
    "autonomous agent orchestration",
    "multi-agent collaboration language model",
    "in-context learning few-shot",
    "reinforcement learning human feedback",
    "code generation agent programming",
    "ReAct reasoning acting",
    "memory augmented neural network",
    "knowledge grounding factuality",
    "instruction tuning fine-tuning",
    "self-reflection error correction",
    "long-horizon planning agent",
    "context window extension",
    "prompt engineering optimization",
    "tree of thoughts search reasoning",
    "agent benchmark evaluation",
    "embodied agent language instruction",
    "scratchpad working memory transformer",
    "external memory retrieval transformer",
    "LLM reasoning reliability faithfulness",
    "cognitive architecture agent",
    "vector store semantic retrieval",
    "guardrails safety alignment LLM",
    "decoding sampling temperature generation",
    "world model planning agent",
    "self-consistency majority voting reasoning",
    "graph of thoughts reasoning",
    "credit assignment reinforcement learning",
    "reward shaping sparse reward",
    "process reward model step verification",
    "reward hacking specification gaming",
    "temporal credit assignment",
    "long horizon agent reward",
]


# ───────────────────────── HTTP ─────────────────────────


def _get(url: str, timeout: int = 30, retries: int = 5) -> bytes:
    """带指数退避的 GET：遇到 429/5xx 自动退避重试，尊重 Retry-After。"""
    delay = 2.0
    last_err: Exception | None = None
    for attempt in range(retries):
        req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
        try:
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                return resp.read()
        except urllib.error.HTTPError as e:
            last_err = e
            if e.code in (429, 500, 502, 503, 504):
                ra = e.headers.get("Retry-After") if e.headers else None
                wait = float(ra) if (ra and ra.isdigit()) else delay
                time.sleep(min(wait, 30.0))
                delay = min(delay * 2, 30.0)
                continue
            raise
        except (urllib.error.URLError, TimeoutError) as e:
            last_err = e
            time.sleep(delay)
            delay = min(delay * 2, 30.0)
    if last_err:
        raise last_err
    raise RuntimeError("unreachable")


def _get_json(url: str, timeout: int = 30) -> dict:
    return json.loads(_get(url, timeout).decode("utf-8", "replace"))


# ───────────────────────── OpenAlex ─────────────────────────


def _reconstruct_abstract(inv_index: dict | None) -> str:
    """OpenAlex 用 abstract_inverted_index 存摘要，需还原成正文。"""
    if not inv_index:
        return ""
    positions: list[tuple[int, str]] = []
    for word, idxs in inv_index.items():
        for i in idxs:
            positions.append((i, word))
    positions.sort()
    return " ".join(w for _, w in positions)


OPENALEX_SELECT = ",".join([
    "id", "title", "abstract_inverted_index", "publication_year",
    "cited_by_count", "primary_location", "doi", "language",
])


def harvest_openalex(query: str, domain: str, max_records: int = 1000,
                     verbose: bool = False) -> list[dict]:
    """用 cursor 分页从 OpenAlex 抓取一个检索词的论文（含摘要、英文）。"""
    out: list[dict] = []
    cursor = "*"
    per_page = 200
    while len(out) < max_records and cursor:
        params = {
            "search": query,
            "per-page": str(per_page),
            "cursor": cursor,
            "select": OPENALEX_SELECT,
            "filter": "has_abstract:true,language:en",
            "mailto": MAILTO,
        }
        url = "https://api.openalex.org/works?" + urllib.parse.urlencode(params)
        try:
            data = _get_json(url)
        except Exception as e:
            if verbose:
                print(f"   [openalex] {query[:30]} 失败：{e}")
            break
        results = data.get("results", [])
        cursor = data.get("meta", {}).get("next_cursor")
        if not results:
            break
        for r in results:
            abstract = _reconstruct_abstract(r.get("abstract_inverted_index"))
            if len(abstract) < 80:
                continue
            loc = r.get("primary_location") or {}
            src = loc.get("source") or {}
            out.append({
                "id": r.get("id", ""),
                "title": (r.get("title") or "").strip(),
                "abstract": abstract,
                "year": r.get("publication_year"),
                "venue": (src.get("display_name") or "").strip(),
                "doi": r.get("doi", "") or "",
                "url": (loc.get("landing_page_url") or r.get("doi") or r.get("id") or ""),
                "cited_by": r.get("cited_by_count", 0),
                "source": "openalex",
                "domain": domain,
                "query": query,
            })
            if len(out) >= max_records:
                break
        time.sleep(0.5)
    return out


# ───────────────────────── arXiv ─────────────────────────

ARXIV_NS = {"atom": "http://www.w3.org/2005/Atom"}


def harvest_arxiv(query: str, domain: str = "harness", max_records: int = 600,
                  verbose: bool = False) -> list[dict]:
    """arXiv API 分页抓取（每页 100，含摘要）。"""
    out: list[dict] = []
    step = 100
    for start in range(0, max_records, step):
        params = {
            "search_query": f"all:{query}",
            "start": str(start),
            "max_results": str(step),
            "sortBy": "relevance",
            "sortOrder": "descending",
        }
        url = "https://export.arxiv.org/api/query?" + urllib.parse.urlencode(params)
        try:
            raw = _get(url)
        except Exception as e:
            if verbose:
                print(f"   [arxiv] {query[:30]} 失败：{e}")
            break
        try:
            root = ET.fromstring(raw)
        except ET.ParseError:
            break
        entries = root.findall("atom:entry", ARXIV_NS)
        if not entries:
            break
        for e in entries:
            title = (e.findtext("atom:title", "", ARXIV_NS) or "").strip().replace("\n", " ")
            summary = (e.findtext("atom:summary", "", ARXIV_NS) or "").strip().replace("\n", " ")
            link = e.findtext("atom:id", "", ARXIV_NS) or ""
            published = e.findtext("atom:published", "", ARXIV_NS) or ""
            year = published[:4] if published else None
            if len(summary) < 80:
                continue
            out.append({
                "id": link,
                "title": title,
                "abstract": summary,
                "year": int(year) if year and year.isdigit() else None,
                "venue": "arXiv",
                "doi": "",
                "url": link,
                "cited_by": 0,
                "source": "arxiv",
                "domain": domain,
                "query": query,
            })
        time.sleep(3.0)  # arXiv 要求请求间隔
    return out


# ───────────────────────── Europe PMC ─────────────────────────


def harvest_europepmc(query: str, domain: str = "adhd", max_records: int = 1000,
                      verbose: bool = False) -> list[dict]:
    """Europe PMC 分页抓取（cursorMark，含摘要）。"""
    out: list[dict] = []
    cursor = "*"
    page_size = 100
    while len(out) < max_records and cursor:
        params = {
            "query": f"{query} AND HAS_ABSTRACT:Y",
            "format": "json",
            "pageSize": str(page_size),
            "cursorMark": cursor,
            "resultType": "core",
        }
        url = ("https://www.ebi.ac.uk/europepmc/webservices/rest/search?"
               + urllib.parse.urlencode(params))
        try:
            data = _get_json(url)
        except Exception as e:
            if verbose:
                print(f"   [europepmc] {query[:30]} 失败：{e}")
            break
        results = data.get("resultList", {}).get("result", [])
        next_cursor = data.get("nextCursorMark")
        if not results or next_cursor == cursor:
            break
        cursor = next_cursor
        for r in results:
            abstract = (r.get("abstractText") or "").strip()
            if len(abstract) < 80:
                continue
            doi = r.get("doi", "") or ""
            pmid = r.get("pmid", "") or r.get("id", "")
            out.append({
                "id": f"epmc:{pmid}",
                "title": (r.get("title") or "").strip(),
                "abstract": abstract,
                "year": int(r["pubYear"]) if str(r.get("pubYear", "")).isdigit() else None,
                "venue": (r.get("journalTitle") or "").strip(),
                "doi": doi,
                "url": (f"https://doi.org/{doi}" if doi
                        else f"https://europepmc.org/abstract/MED/{pmid}"),
                "cited_by": r.get("citedByCount", 0),
                "source": "europepmc",
                "domain": domain,
                "query": query,
            })
            if len(out) >= max_records:
                break
        time.sleep(0.2)
    return out


# ───────────────────────── 编排 ─────────────────────────


def _dedupe(records: list[dict]) -> list[dict]:
    seen: set[str] = set()
    out = []
    for r in records:
        key = (r.get("doi") or "").lower() or (r.get("title") or "").lower().strip()
        if not key or key in seen:
            continue
        seen.add(key)
        out.append(r)
    return out


def harvest_all(
    per_query_openalex: int = 1000,
    per_query_arxiv: int = 400,
    per_query_europepmc: int = 800,
    save_every: bool = True,
    verbose: bool = True,
) -> list[dict]:
    """抓取双域大规模学术语料并落盘（增量保存，可中断续跑）。"""
    os.makedirs(DATA_DIR, exist_ok=True)
    records = load_academic()
    have_keys = {
        (r.get("doi") or "").lower() or (r.get("title") or "").lower().strip()
        for r in records
    }

    def absorb(new: list[dict]):
        added = 0
        for r in new:
            key = (r.get("doi") or "").lower() or (r.get("title") or "").lower().strip()
            if key and key not in have_keys:
                have_keys.add(key)
                records.append(r)
                added += 1
        return added

    def flush():
        if save_every:
            save_academic(records)

    # ADHD 域：OpenAlex + Europe PMC
    for q in ADHD_QUERIES:
        a = harvest_openalex(q, "adhd", per_query_openalex, verbose)
        n1 = absorb(a)
        b = harvest_europepmc(q, "adhd", per_query_europepmc, verbose)
        n2 = absorb(b)
        if verbose:
            print(f"[ADHD] {q[:40]:40s} +OpenAlex {n1:4d} +EPMC {n2:4d}  共 {len(records)}")
        flush()

    # Harness 域：OpenAlex + arXiv
    for q in HARNESS_QUERIES:
        a = harvest_openalex(q, "harness", per_query_openalex, verbose)
        n1 = absorb(a)
        if verbose:
            print(f"[HARN] {q[:40]:40s} +OpenAlex {n1:4d}  共 {len(records)}")
        flush()

    for q in ARXIV_QUERIES:
        a = harvest_arxiv(q, "harness", per_query_arxiv, verbose)
        n = absorb(a)
        if verbose:
            print(f"[HARN/arxiv] {q[:34]:34s} +{n:4d}  共 {len(records)}")
        flush()

    save_academic(records)
    return records


def topup_openalex(queries: list[str], domain: str, per_query: int = 1500,
                   verbose: bool = True) -> list[dict]:
    """针对某一域，用 OpenAlex 补齐语料（增量、去重、落盘）。"""
    os.makedirs(DATA_DIR, exist_ok=True)
    records = load_academic()
    have_keys = {
        (r.get("doi") or "").lower() or (r.get("title") or "").lower().strip()
        for r in records
    }
    for q in queries:
        added = 0
        for r in harvest_openalex(q, domain, per_query, verbose):
            key = (r.get("doi") or "").lower() or (r.get("title") or "").lower().strip()
            if key and key not in have_keys:
                have_keys.add(key)
                records.append(r)
                added += 1
        if verbose:
            print(f"[topup {domain}] {q[:42]:42s} +{added:4d}  共 {len(records)}")
        save_academic(records)
    return records


def save_academic(records: list[dict], filename: str = ACADEMIC_FILE) -> None:
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(records, f, ensure_ascii=False)


def load_academic(filename: str = ACADEMIC_FILE) -> list[dict]:
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as f:
            return json.load(f)
    return []


def as_articles(records: list[dict] | None = None, domain: str | None = None,
                limit: int | None = None, min_chars: int = 120) -> list[dict]:
    """把学术记录映射成「文章」结构（content=abstract），供知识萃取 / wiki 取材。

    按引用量降序，优先取高影响力论文。limit 为每次返回上限。
    """
    records = records if records is not None else load_academic()
    if domain:
        records = [r for r in records if r.get("domain") == domain]
    records = [r for r in records if len(r.get("abstract", "")) >= min_chars]
    records = sorted(records, key=lambda r: r.get("cited_by", 0) or 0, reverse=True)
    if limit:
        records = records[:limit]
    out = []
    for r in records:
        title = r.get("title", "")
        abstract = r.get("abstract", "")
        venue = r.get("venue", "")
        out.append({
            "title": title,
            "content": f"{title}. {abstract}",
            "content_length": len(abstract),
            "url": r.get("url", ""),
            "source_title": venue,
            "domain": r.get("domain", ""),
            "year": r.get("year"),
            "is_academic": True,
        })
    return out


def stats(records: list[dict] | None = None) -> dict:
    records = records if records is not None else load_academic()
    from collections import Counter
    return {
        "total": len(records),
        "by_domain": dict(Counter(r.get("domain") for r in records)),
        "by_source": dict(Counter(r.get("source") for r in records)),
    }


if __name__ == "__main__":
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--openalex", type=int, default=1000)
    ap.add_argument("--arxiv", type=int, default=400)
    ap.add_argument("--europepmc", type=int, default=800)
    ap.add_argument("--stats", action="store_true")
    ap.add_argument("--topup-harness", action="store_true")
    ap.add_argument("--topup-adhd", action="store_true")
    ap.add_argument("--topup-arxiv", action="store_true")
    args = ap.parse_args()
    if args.stats:
        print(json.dumps(stats(), ensure_ascii=False, indent=2))
    elif args.topup_arxiv:
        # arXiv 深抓 harness 域（摘要质量高、无 OpenAlex 限流问题）
        records = load_academic()
        have = {(r.get("doi") or "").lower() or (r.get("title") or "").lower().strip()
                for r in records}
        for q in ARXIV_QUERIES:
            added = 0
            for r in harvest_arxiv(q, "harness", args.arxiv, verbose=True):
                key = (r.get("doi") or "").lower() or (r.get("title") or "").lower().strip()
                if key and key not in have:
                    have.add(key); records.append(r); added += 1
            print(f"[topup arxiv] {q[:40]:40s} +{added:4d}  共 {len(records)}")
            save_academic(records)
        print(json.dumps(stats(records), ensure_ascii=False, indent=2))
    elif args.topup_harness:
        topup_openalex(HARNESS_QUERIES, "harness", per_query=args.openalex)
        print(json.dumps(stats(), ensure_ascii=False, indent=2))
    elif args.topup_adhd:
        topup_openalex(ADHD_QUERIES, "adhd", per_query=args.openalex)
        print(json.dumps(stats(), ensure_ascii=False, indent=2))
    else:
        harvest_all(args.openalex, args.arxiv, args.europepmc)
        print(json.dumps(stats(), ensure_ascii=False, indent=2))
