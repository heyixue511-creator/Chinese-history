# -*- coding: utf-8 -*-
"""Generate chapter 10 batch-Q KU files from authored entry specs."""
import importlib.util
import json
from pathlib import Path

ROOT = Path(r"D:/中国设计史研究")
UNIT = ROOT / "04-knowledge/units"
DIMS = {
    "A": "设计史观与史学方法",
    "B": "造物、工艺与生产技术",
    "C": "视觉传达与文字设计",
    "D": "商业、制度与设计教育",
    "E": "现代性与跨文化互动",
}
DOC = "2009-zhaonong-zhongguo-yishu-shejishi"
SRC = "03基础书籍-md文档/中国艺术设计史_赵农_2009_高等教育出版社.md"


def load(path):
    spec = importlib.util.spec_from_file_location(Path(path).stem, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.E


def tags_block(tags):
    return "tags:\n" + "".join(f"  - {t}\n" for t in tags)


def aliases_block(aliases):
    if not aliases:
        return "aliases: []\n"
    return "aliases:\n" + "".join(f"  - {a}\n" for a in aliases)


def source_block(lines):
    return (
        "sources:\n"
        f'  - citation: "赵农, *中国艺术设计史* (北京: 高等教育出版社, 2009), {lines}."\n'
        f'    location: "{lines}"\n'
        "    evidence_ref:\n"
        f"      doc_id: {DOC}\n"
        f"      source_file: {SRC}\n"
        "      chapter_id: null\n"
        "      chunk_id: null\n"
    )


def tail_block(e):
    out = (
        "created: 2026-10-26\n"
        "updated: 2026-10-26\n"
        f"confidence: {e['conf']}\n"
        "consensus: tentative\n"
        "source_count: 1\n"
        "last_verified: 2026-10-26\n"
        "review_due: 2027-04-26\n"
        "version: 1\n"
        "evidence_status: source_backed\n"
        "primary_domain: chinese-design-history\n"
        f"primary_dimension: {e['dim']}\n"
    )
    if e.get("sec"):
        out += "secondary_dimensions:\n" + "".join(f"  - {d}\n" for d in e["sec"])
    else:
        out += "secondary_dimensions:\n"
    out += f"hierarchy_scope_note: \"{e['scope']}\"\n"
    return out


def frontmatter(e):
    t = e["type"]
    out = "---\n"
    if t in ("term", "work", "person"):
        out += f"title: {e['title']}（{e['en']}）\n"
    elif t == "publication":
        out += f"title: 《{e['plain']}》（{e['en']}）\n"
    elif t == "place":
        out += f"title: {e['title']}（{e['en']}）\n"
    out += f"name_en: {e['en']}\n"
    out += f"type: {t}\n"
    out += f"sub_type: {e['sub']}\n"
    if t == "place":
        out += f"modern_name: {e['modern_name']}\n"
        out += "historical_names:\n" + "".join(f"  - {h}\n" for h in e["hist"])
        out += f"administrative_context: {e['admin']}\n"
        out += f"spatial_scope: {e['space']}\n"
    if t in ("term", "work", "publication"):
        out += f"title_original: {e['plain']}\n"
        out += "title_original_language: zh\n"
        out += f"title_zh: {e['plain']}\n"
    if t == "term":
        out += f"term_original: {e['plain']}\n"
        out += f"term_zh: {e['plain']}\n"
        out += "academic_translation_status: provisional\n"
    elif t == "person":
        out += f"name_original: {e['plain']}\n"
        out += "language_original: zh\n"
        out += f"name_zh: {e['plain']}\n"
        out += "translation_status: provisional\n"
    out += f"translation_note: {e['tn']}\n"
    meta = e.get("meta", {})
    for k, v in meta.items():
        out += f"{k}: {v}\n"
    out += tags_block(e["tags"])
    out += aliases_block(e.get("aliases", []))
    out += source_block(e["lines"])
    out += tail_block(e)
    out += "---\n\n"
    return out


def body(e):
    out = "## 描述\n\n" + e["desc"].strip() + "\n\n"
    out += "## 核心内容\n\n"
    for p in e["points"]:
        out += "- " + p.strip() + "\n"
    out += "\n## 在层级体系中的位置\n\n"
    out += "- primary_domain: chinese-design-history\n"
    out += f"- primary_dimension: {e['dim']}（{DIMS[e['dim']]}）\n"
    if e.get("sec"):
        out += "- secondary_dimensions: " + "、".join(f"{d}（{DIMS[d]}）" for d in e["sec"]) + "\n"
    else:
        out += "- secondary_dimensions: 无\n"
    out += "- primary_theme: 未建立；Theme 尚未 materialize\n"
    out += "- topic_memberships: 无；Topic 尚未 materialize\n"
    out += "- role_in_theme: 未定\n"
    out += f"- scope_note: {e['scope']}\n\n"
    out += "## 相关知识元\n\n" + e["rel"].strip() + "\n\n"
    out += "## 验证状态\n\n"
    out += "- 证据状态: source_backed（赵农 2009 册内复读）\n"
    out += "- 验证层级: 未评定；consensus 为 tentative，按字段契约不填 L1–L7\n"
    out += "- 验证平台: 未使用外部平台\n"
    out += f"- 匹配质量: {e['quality']}\n"
    out += "- 验证日期: 2026-10-26\n"
    out += f"- 证据范围: 仅赵农 2009 册 Markdown 文本 {e['lines'].replace(', ', '、')}；未做来源外核对\n\n"
    out += "## 参考文献\n\n"
    out += "1. 赵农. *中国艺术设计史*. 北京: 高等教育出版社, 2009.\n"
    return out


def main():
    entries = []
    for part in ("_zn_ch10_e10.py", "_zn_ch10_e11.py"):
        entries += load(ROOT / part)
    seen = set()
    for e in entries:
        if e["slug"] in seen:
            raise SystemExit("duplicate slug " + e["slug"])
        seen.add(e["slug"])
        p = UNIT / e["dir"] / (e["slug"] + ".md")
        if p.exists():
            raise SystemExit("exists " + str(p))
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(frontmatter(e) + body(e), encoding="utf-8", newline="\n")
    print(json.dumps({"written": len(entries)}, ensure_ascii=False))


if __name__ == "__main__":
    main()
