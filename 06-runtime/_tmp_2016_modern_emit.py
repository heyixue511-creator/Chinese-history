# -*- coding: utf-8 -*-
"""Generate 33 event KUs for the 2016 modern design chronology batch."""
import sys
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).parent))
from _tmp_2016_modern_items_a import ITEMS_A
from _tmp_2016_modern_items_b import ITEMS_B
from _tmp_2016_modern_items_c import ITEMS_C

OUT = Path("04-knowledge/units/events")
BOOK = "中国艺术设计史（升级版）"
DOC = "2016-xiayanjing-zhongguo-yishu-shejishi-upgrade"
SRC = "03基础书籍-md文档/中国艺术设计史（升级版）_夏燕靖_2016_上海人民美术出版社.md"

ITEMS = ITEMS_A + ITEMS_B + ITEMS_C

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
  - citation: "夏燕靖, *{book}* (上海: 上海人民美术出版社, 2016), {span}."
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
hierarchy_scope_note: "{scope}"
---

## 描述

{desc}

## 核心内容

{bullets}

## 在层级体系中的位置

- primary_domain: chinese-design-history
- primary_dimension: {dim}
- primary_theme: 未建立；Theme 尚未 materialize
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

1. 夏燕靖. *{book}*. 上海: 上海人民美术出版社, 2016.
"""


def check(path: Path) -> None:
    text = path.read_text(encoding="utf-8")
    assert text.startswith("---\n"), path
    fm = text.split("---\n", 2)[1]
    data = yaml.safe_load(fm)
    assert data["type"] == "event", path
    assert data["evidence_status"] == "source_backed", path
    for section in ["## 描述", "## 核心内容", "## 在层级体系中的位置", "## 相关知识元", "## 验证状态", "## 参考文献"]:
        assert section in text, (path, section)


slugs = [i["slug"] for i in ITEMS]
assert len(slugs) == len(set(slugs)), "duplicate slugs"
written = 0
for item in ITEMS:
    tags = "\n".join(f"  - {t}" for t in item["tags"])
    bullets = "\n".join(f"- {b}" for b in item["bullets"])
    text = TEMPLATE.format(
        title=item["title"], en=item["en"], sub=item["sub"], date=item["date"],
        date_note=item["date_note"], loc=item["loc"], part=item["part"],
        cause=item["cause"], result=item["result"], basis=item["basis"],
        tags=tags, book=BOOK, span=item["span"], doc=DOC, src=SRC,
        dim=item["dim"], scope=item["scope"], desc=item["desc"],
        bullets=bullets, related=item["related"], match=item["match"],
    )
    path = OUT / f"{item['slug']}.md"
    if path.exists():
        raise SystemExit(f"exists: {path}")
    path.write_bytes(text.encode("utf-8"))
    check(path)
    written += 1

print("written", written)
