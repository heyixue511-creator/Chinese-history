# -*- coding: utf-8 -*-
"""Generate Li Lixin 2011 batch-LL2a (第一章 造物起源与体系形成) KU files."""
import importlib.util
import json
import sys
from pathlib import Path

ROOT = Path(r"D:/中国设计史研究")
sys.path.insert(0, str(ROOT))
UNIT = ROOT / "04-knowledge/units"
DIMS = {
    "A": "设计史观与史学方法",
    "B": "造物、工艺与生产技术",
    "C": "视觉传达与文字设计",
    "D": "商业、制度与设计教育",
    "E": "现代性与跨文化互动",
}
DOC = "2011-lilixin-zhongguo-sheji-yishu-shilun"
SRC = "03基础书籍-md文档/中国设计艺术史论_李立新_2011_人民出版社.md"
LI_REF = "李立新. *中国设计艺术史论*. 北京: 人民出版社, 2011."
PARTS = ("_zn_ll2a_e1.py", "_zn_ll2a_e2.py", "_zn_ll2a_e3.py")


def load(path):
    spec = importlib.util.spec_from_file_location(Path(path).stem, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def tags_block(tags):
    return "tags:\n" + "".join(f"  - {t}\n" for t in tags)


def aliases_block(aliases):
    if not aliases:
        return "aliases: []\n"
    return "aliases:\n" + "".join(f"  - {a}\n" for a in aliases)


def source_block(e):
    lines = e["lines"]
    out = (
        "sources:\n"
        f'  - citation: "李立新, *中国设计艺术史论* (北京: 人民出版社, 2011), {lines}."\n'
        f'    location: "{lines}"\n'
        "    evidence_ref:\n"
        f"      doc_id: {DOC}\n"
        f"      source_file: {SRC}\n"
        "      chapter_id: null\n"
        "      chunk_id: null\n"
    )
    for x in e.get("extra", []):
        out += (
            f'  - citation: "{x["citation"]}"\n'
            f'    location: "{x["location"]}"\n'
            "    evidence_ref:\n"
            f"      doc_id: {x['doc_id']}\n"
            f"      source_file: {x['source_file']}\n"
            "      chapter_id: null\n"
            "      chunk_id: null\n"
        )
    return out


def tail_block(e):
    out = (
        "created: 2026-10-27\n"
        "updated: 2026-10-27\n"
        f"confidence: {e['conf']}\n"
        "consensus: tentative\n"
        f"source_count: {1 + len(e.get('extra', []))}\n"
        "last_verified: 2026-10-27\n"
        "review_due: 2027-04-27\n"
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
    out += f"name_en: {e['en']}\n"
    out += f"type: {t}\n"
    out += f"sub_type: {e['sub']}\n"
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
    out += source_block(e)
    out += tail_block(e)
    out += "---\n\n"
    return out


def body(e):
    n = 1 + len(e.get("extra", []))
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
    out += f"- 证据状态: source_backed（{n} 册来源内复读）\n"
    out += "- 验证层级: 未评定；consensus 为 tentative，按字段契约不填 L1–L7\n"
    out += "- 验证平台: 未使用外部平台\n"
    out += f"- 匹配质量: {e['quality']}\n"
    out += "- 验证日期: 2026-10-27\n"
    scope = f"仅李立新 2011 册 Markdown 文本 {e['lines'].replace(', ', '、')}"
    for x in e.get("extra", []):
        scope += f"，以及 {x['citation'].split(',')[0]} {x['location']}"
    out += f"- 证据范围: {scope}；未做来源外核对\n\n"
    out += "## 参考文献\n\n"
    out += f"1. {LI_REF}\n"
    for i, x in enumerate(e.get("extra", []), start=2):
        out += f"{i}. {x['ref']}\n"
    return out


def main():
    only = set(sys.argv[1:]) or None
    entries = []
    for part in PARTS:
        entries += load(ROOT / part).E
    seen = set()
    written = 0
    for e in entries:
        if e["slug"] in seen:
            raise SystemExit("duplicate slug " + e["slug"])
        seen.add(e["slug"])
        if only is not None and e["slug"] not in only:
            continue
        p = UNIT / e["dir"] / (e["slug"] + ".md")
        if p.exists() and only is None:
            raise SystemExit("exists " + str(p))
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(frontmatter(e) + body(e), encoding="utf-8", newline="\n")
        written += 1
    print(json.dumps({"entries": len(entries), "written": written}, ensure_ascii=False))


if __name__ == "__main__":
    main()
