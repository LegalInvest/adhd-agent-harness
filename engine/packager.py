"""
发布回流闭环 —— 文章 → 发布资产包转换器

把引擎生成的 Top 400 文章（data/articles/*.md）一键转换成 publishing/content-packs/
的人工发布资产包格式（正文 / 发布包 / 小红书版 / 知乎版 / 短视频口播 / 48小时回流表），
让自动化引擎的产出直接接入既有的人工发布与数据回流工作流。

用法：
    python -m engine.packager --rank 1          # 按当前排名取文章
    python -m engine.packager --topic-id prob-xxxx
    python -m engine.packager --rank 1 --no-llm  # 只生成结构，不做平台改写
"""

import argparse
import json
import os
import re

ROOT = os.path.dirname(os.path.dirname(__file__))
ARTICLES_DIR = os.path.join(ROOT, "data", "articles")
PACKS_DIR = os.path.join(ROOT, "publishing", "content-packs")

FEEDBACK_TABLE = """# {title} —— 48小时回流记录表

| 时间点 | 阅读 | 点赞 | 收藏 | 评论 | 转发 | 备注 |
|---|---|---|---|---|---|---|
| 发布后 1h |  |  |  |  |  |  |
| 发布后 6h |  |  |  |  |  |  |
| 发布后 24h |  |  |  |  |  |  |
| 发布后 48h |  |  |  |  |  |  |

## 回流动作
- 48h 后把最终数据填入 `publishing/feedback/feedback_log.md`
- 表现显著高/低于预期时，在 meta.json 里记录假设（标题钩子？脊柱概念？平台错配？）
"""


def _parse_article(path: str) -> tuple[dict, str]:
    with open(path, "r", encoding="utf-8") as f:
        raw = f.read()
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", raw, re.S)
    if not m:
        raise ValueError(f"无法解析 frontmatter: {path}")
    fm = {}
    for line in m.group(1).splitlines():
        kv = re.match(r'^(\w+): "?(.*?)"?$', line)
        if kv:
            fm[kv.group(1)] = kv.group(2)
    return fm, m.group(2)


def _find_article(rank: int | None, topic_id: str | None) -> str:
    for fn in sorted(os.listdir(ARTICLES_DIR)):
        if not fn.endswith(".md"):
            continue
        path = os.path.join(ARTICLES_DIR, fn)
        if topic_id and fn == f"{topic_id}.md":
            return path
        if rank is not None:
            with open(path, "r", encoding="utf-8") as f:
                head = f.read(3000)
            mr = re.search(r"^rank: (\d+)$", head, re.M)
            if mr and int(mr.group(1)) == rank:
                return path
    raise FileNotFoundError(f"未找到文章 rank={rank} topic_id={topic_id}")


def _llm_adaptations(title: str, body: str, llm) -> dict:
    prompt = (
        f"以下是一篇「ADHD × Agentic Harness 同构」文章，请为多平台发布做改写。\n\n"
        f"标题：{title}\n正文：\n{body[:5000]}\n\n"
        "严格输出 JSON：\n"
        "{\n"
        '  "xiaohongshu": "小红书版（600字内，口语化，emoji 适度，带 5 个话题标签）",\n'
        '  "zhihu": "知乎版开头（以问题切入的 300 字引子 + 3 个小节标题大纲）",\n'
        '  "oral": "短视频口播稿（60-90秒，钩子开头，落到一个可执行动作）",\n'
        '  "core_judgment": "一句话核心判断（发布包用）",\n'
        '  "comment_hooks": ["3 个引导评论回流的问题", "...", "..."]\n'
        "}"
    )
    return llm.chat_json(
        [{"role": "user", "content": prompt}], temperature=0.6, max_tokens=2500
    )


def build_pack(article_path: str, use_llm: bool = True) -> str:
    fm, body = _parse_article(article_path)
    title = fm.get("title", "")
    topic_id = fm.get("topicId", os.path.basename(article_path)[:-3])
    pack_dir = os.path.join(PACKS_DIR, f"auto-{topic_id}")
    os.makedirs(pack_dir, exist_ok=True)

    ad = {}
    if use_llm:
        from engine.llm import LLMClient
        ad = _llm_adaptations(title, body, LLMClient()) or {}

    def w(name: str, content: str) -> None:
        with open(os.path.join(pack_dir, name), "w", encoding="utf-8") as f:
            f.write(content)

    w("01_正文.md", f"# {title}\n\n{body.strip()}\n")
    w(
        "02_发布包.md",
        f"# {title} 发布包\n\n## 主标题\n\n{title}\n\n"
        f"## 核心判断\n\n{ad.get('core_judgment', fm.get('thesis', ''))}\n\n"
        f"## 同构脊柱\n\n{fm.get('spine', '')}（同构强度：{fm.get('isoStrength', '未标注')} 级）\n\n"
        "## 发布提醒\n\n避免医学化断言；避免把 ADHD 浪漫化；避免把 AI 包装成万能药。"
        "重点是接口、回流和外部执行系统。\n",
    )
    if ad.get("xiaohongshu"):
        w("03_小红书版.md", f"# {title} 小红书版\n\n{ad['xiaohongshu']}\n")
    if ad.get("zhihu"):
        w("04_知乎版.md", f"# {title} 知乎版\n\n{ad['zhihu']}\n")
    if ad.get("oral"):
        w("05_短视频口播.md", f"# {title} 口播稿\n\n{ad['oral']}\n")
    hooks = ad.get("comment_hooks") or []
    if hooks:
        w("06_评论回流问题.md", f"# 评论回流问题\n\n" + "\n".join(f"- {h}" for h in hooks) + "\n")
    w("07_48小时回流表.md", FEEDBACK_TABLE.format(title=title))
    with open(os.path.join(pack_dir, "meta.json"), "w", encoding="utf-8") as f:
        json.dump(
            {
                "topic_id": topic_id,
                "title": title,
                "rank": int(fm.get("rank", 0) or 0),
                "score": float(fm.get("score", 0) or 0),
                "spine": fm.get("spine", ""),
                "iso_strength": fm.get("isoStrength", ""),
                "source": "engine-auto",
            },
            f,
            ensure_ascii=False,
            indent=2,
        )
    return pack_dir


def main() -> None:
    parser = argparse.ArgumentParser(description="文章 → 发布资产包转换")
    parser.add_argument("--rank", type=int, help="按当前排名选文章")
    parser.add_argument("--topic-id", help="按 topic id 选文章")
    parser.add_argument("--no-llm", action="store_true", help="跳过平台改写")
    args = parser.parse_args()
    if args.rank is None and not args.topic_id:
        parser.error("需要 --rank 或 --topic-id")
    path = _find_article(args.rank, args.topic_id)
    pack = build_pack(path, use_llm=not args.no_llm)
    print(f"资产包已生成: {pack}")


if __name__ == "__main__":
    main()
