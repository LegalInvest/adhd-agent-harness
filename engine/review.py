"""
发布前评审门（AI-Scientist reviewer agent 思路的本地化实现）。

对文章做 rubric 化质量检查，分两层：
- 硬检查（无 API 依赖）：字数、五型问题结构、医疗边界声明、未支持数字、
  类比字面等同红线、frontmatter 完整性、双目录一致。
- 软审稿（可选，走 engine.llm，Kimi→DeepSeek 降级）：五型完整度评分与改进建议。

CLI：
  python -m engine.review                       # 全量体检 -> data/review_report.json
  python -m engine.review data/articles/x.md    # 单篇
  python -m engine.review --llm data/articles/x.md  # 附加 LLM rubric 审稿
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ARTICLES_DIR = Path("data/articles")
BLOG_DIR = Path("blog/src/content/articles")
REPORT_PATH = Path("data/review_report.json")

MIN_CN_CHARS = 1000
TARGET_CN_CHARS = 1800

_MEDICAL_TERMS = [
    "药物", "用药", "哌甲酯", "安非他明", "阿托西汀", "停药", "剂量",
    "诊断", "自伤", "自杀", "危机", "抑郁", "死亡率", "副作用", "戒断",
]
_BOUNDARY_MARKERS = [
    "医生", "医师", "专业", "精神科", "心理咨询", "就医", "临床医生", "处方",
]
_LITERAL_EQUATION_PATTERNS = [
    r"就是[一个]*\s*(?:Transformer|KV\s*cache|LLM|大模型)",
    r"(?:工作记忆|前额叶|大脑)\s*(?:就是|等于|=)\s*(?:KV\s*cache|上下文窗口|显存)",
]
_FIVE_STEP_SIGNALS = {
    "收敛": ["只回答", "只解决", "本文只", "锁定", "这篇只"],
    "验证": ["反例", "证伪", "自测", "N-of-1", "n-of-1", "验证"],
    "决策": ["不做", "先做", "不要做", "别做", "优先做"],
    "落地": ["今天", "第一步", "最小动作", "当天", "现在就"],
}


def _split(md: str) -> tuple[str, str]:
    """返回 (frontmatter, body)。"""
    m = re.match(r"\A---\n(.*?)\n---\n(.*)\Z", md, re.DOTALL)
    return (m.group(1), m.group(2)) if m else ("", md)


def _cn_count(text: str) -> int:
    return len(re.findall(r"[\u4e00-\u9fff]", text))


def review_article(path: Path) -> dict:
    md = path.read_text(encoding="utf-8")
    fm, body = _split(md)
    body_main = body.split("## 参考来源")[0]
    issues: list[str] = []
    warnings: list[str] = []

    n = _cn_count(body_main)
    if n < MIN_CN_CHARS:
        issues.append(f"正文中文字符 {n} < {MIN_CN_CHARS}")
    elif n < TARGET_CN_CHARS:
        warnings.append(f"正文中文字符 {n}，低于目标 {TARGET_CN_CHARS}")

    for field in ("title", "slug", "rank", "score"):
        if not re.search(rf"^{field}\s*:", fm, re.MULTILINE):
            issues.append(f"frontmatter 缺少 {field}")
    if not re.search(r"^llmGenerated\s*:", fm, re.MULTILINE):
        warnings.append("frontmatter 缺少 llmGenerated 标记")

    if any(t in body_main for t in _MEDICAL_TERMS):
        if not any(b in body_main for b in _BOUNDARY_MARKERS):
            issues.append("涉及医疗/危机内容但缺少专业支持边界声明")

    for pat in _LITERAL_EQUATION_PATTERNS:
        for m in re.finditer(pat, body_main, re.IGNORECASE):
            ctx = body_main[max(0, m.start() - 40): m.end() + 40]
            # 引用他人错误说法并否定的语境不算违规
            if any(k in ctx for k in ("不是", "并非", "错的", "错误", "「", "修辞", "排除")):
                continue
            issues.append(f"疑似类比字面等同红线：/{pat}/")
            break

    missing_steps = [k for k, sigs in _FIVE_STEP_SIGNALS.items()
                     if not any(s in body_main for s in sigs)]
    if missing_steps:
        warnings.append(f"五型问题结构信号缺失：{'、'.join(missing_steps)}")

    pct = re.findall(r"(\d{1,3}(?:\.\d+)?)\s*%", body_main)
    if pct and "## 参考来源" not in body:
        warnings.append(f"正文含 {len(pct)} 个百分比数字但无参考来源区块")

    twin = BLOG_DIR / path.name
    if twin.exists():
        if twin.read_bytes() != path.read_bytes():
            issues.append("data/articles 与 blog/src/content/articles 不一致")
    else:
        issues.append("blog/src/content/articles 缺少同名文件")

    return {
        "file": str(path),
        "cn_chars": n,
        "issues": issues,
        "warnings": warnings,
        "status": "FAIL" if issues else ("WARN" if warnings else "PASS"),
    }


def llm_review(path: Path) -> dict:
    """可选：LLM rubric 审稿（AI-Scientist 式）。"""
    from engine.llm import get_client

    md = path.read_text(encoding="utf-8")
    prompt = (
        "你是严格的内容审稿人。按以下 rubric 给这篇 ADHD×AI 文章打分（各 1-10）并给出最重要的一条改进建议：\n"
        "1. single_question：是否只回答一个明确问题；\n"
        "2. five_steps：收敛→穿透→验证→决策→落地五步是否完整；\n"
        "3. opening：开头失败现场是否具体独特（非模板）；\n"
        "4. boundary：同构类比边界与医疗边界是否守住；\n"
        "5. actionable：当天可执行最小动作是否真实可做。\n"
        '输出 JSON：{"scores": {...}, "suggestion": "..."}\n\n' + md[:6000]
    )
    return get_client().chat_json([{"role": "user", "content": prompt}])


def main() -> None:
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    use_llm = "--llm" in sys.argv
    paths = [Path(a) for a in args] if args else sorted(ARTICLES_DIR.glob("*.md"))

    results = [review_article(p) for p in paths]
    fails = [r for r in results if r["status"] == "FAIL"]
    warns = [r for r in results if r["status"] == "WARN"]

    if use_llm:
        for r, p in zip(results, paths):
            try:
                r["llm_review"] = llm_review(p)
            except Exception as e:  # noqa: BLE001
                r["llm_review_error"] = str(e)

    REPORT_PATH.write_text(
        json.dumps({"total": len(results), "fail": len(fails), "warn": len(warns),
                    "results": results}, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    print(f"reviewed {len(results)} | FAIL {len(fails)} | WARN {len(warns)} | report -> {REPORT_PATH}")
    for r in fails:
        print(f"FAIL {r['file']}: {'; '.join(r['issues'])}")


if __name__ == "__main__":
    main()
