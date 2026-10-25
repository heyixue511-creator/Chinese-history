# -*- coding: utf-8 -*-
"""Generate 8 event KUs for the Li Lixin 2011 event batch."""
import sys
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).parent))
from _tmp_lilixin_events_items import ITEMS_LLX

OUT = Path("04-knowledge/units/events")
BOOK = "中国设计艺术史论"
DOC = "2011-lilixin-zhongguo-sheji-yishu-shilun"
SRC = "03基础书籍-md文档/中国设计艺术史论_李立新_2011_人民出版社.md"

DIM_LABEL = {
    "A": "设计史观与史学方法",
    "B": "造物、工艺与生产技术",
    "C": "视觉传达与文字设计",
    "D": "商业、制度与设计教育",
    "E": "现代性与跨文化互动",
}

TEMPLATE = """---
title: "{title}（{en}）"
name_en: "{en}"
type: event
sub_type: {sub}
date: "{date}"
date_note: "{date_note}"
location: "{loc}"
participants: "{part}"
cause: "{cause}"
result: "{result}"
source_basis: "{basis}"
tags:
{tags}
sources:
  - citation: "李立新, *{book}* (北京: 人民出版社, 2011), {span}."
    location: "{span}"
    evidence_ref:
      doc_id: {doc}
      source_file: {src}
      chapter_id: null
      chunk_id: null
created: 2026-10-25
updated: 2026-10-25
confidence: medium
consensus: tentative
source_count: 1
last_verified: 2026-10-25
review_due: 2027-04-25
version: 1
evidence_status: source_backed
primary_domain: chinese-design-history
primary_dimension: {dim}
{sec_fm}hierarchy_scope_note: "{scope}"
---

## 描述

{desc}

## 核心内容

{bullets}

## 在层级体系中的位置

- primary_domain: chinese-design-history
- primary_dimension: {dim}
{sec_md}- primary_theme: 未建立；Theme 尚未 materialize
- topic_memberships: 无；Topic 尚未 materialize
- role_in_theme: 未定
- scope_note: {scope}

## 相关知识元

{related}

## 验证状态

- 证据状态: source_backed（来源内复读）
- 验证层级: 未评定；consensus 为 tentative，按字段契约不填 L1–L7
- 验证平台: 未使用外部平台
- 匹配质量: {match}
- 验证日期: 2026-10-25
- 证据范围: 仅前六册 Markdown 文本；未做来源外核对

## 参考文献

1. 李立新. *{book}*. 北京: 人民出版社, 2011.
"""


def check(path: Path, item: dict) -> None:
    text = path.read_text(encoding="utf-8")
    assert text.startswith("---\n"), path
    data = yaml.safe_load(text.split("---\n", 2)[1])
    assert data["type"] == "event", path
    assert data["sub_type"] == item["sub"], path
    assert data["evidence_status"] == "source_backed", path
    assert data["primary_dimension"] == item["dim"], path
    assert data["sources"][0]["evidence_ref"]["doc_id"] == DOC, path
    if item["sec"]:
        assert data["secondary_dimensions"] == item["sec"], path
    for section in ["## 描述", "## 核心内容", "## 在层级体系中的位置", "## 相关知识元", "## 验证状态", "## 参考文献"]:
        assert section in text, (path, section)


slugs = [i["slug"] for i in ITEMS_LLX]
assert len(slugs) == len(set(slugs)), "duplicate slugs"
assert len(ITEMS_LLX) == 8, len(ITEMS_LLX)
written = 0
for item in ITEMS_LLX:
    tags = "\n".join(f"  - {t}" for t in item["tags"])
    bullets = "\n".join(item["bullets"])
    if item["sec"]:
        sec_fm = "secondary_dimensions:\n" + "\n".join(f"  - {s}" for s in item["sec"]) + "\n"
        sec_md = "- secondary_dimensions: " + "、".join(
            f"{s}（{DIM_LABEL[s]}）" for s in item["sec"]
        ) + "\n"
    else:
        sec_fm = ""
        sec_md = ""
    text = TEMPLATE.format(
        title=item["title"], en=item["en"], sub=item["sub"], date=item["date"],
        date_note=item["date_note"], loc=item["loc"], part=item["part"],
        cause=item["cause"], result=item["result"], basis=item["basis"],
        tags=tags, book=BOOK, span=item["span"], doc=DOC, src=SRC,
        dim=item["dim"], sec_fm=sec_fm, sec_md=sec_md, scope=item["scope"],
        desc=item["desc"], bullets=bullets, related=item["related"],
        match=item["match"],
    )
    path = OUT / f"{item['slug']}.md"
    if path.exists():
        raise SystemExit(f"exists: {path}")
    path.write_bytes(text.encode("utf-8"))
    check(path, item)
    written += 1

print("written", written)
