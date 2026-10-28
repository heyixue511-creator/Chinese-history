# -*- coding: utf-8 -*-
"""Dump review-relevant parts of KU files: selected frontmatter keys + 3 sections."""
import io
import re
import sys
from pathlib import Path

ROOT = Path(r"D:/中国设计史研究")
files = [x.strip() for x in (ROOT / sys.argv[1]).read_text(encoding="utf-8").splitlines() if x.strip()]
KEYS = ("title:", "sub_type:", "aliases:", "aliases", "year:", "creator:", "location:",
        "dimensions:", "collection:", "format:", "confidence:", "term_original:",
        "term_zh:", "title_original:", "title_zh:", "occupation:", "author:",
        "publication_year:", "edition:", "secondary_dimensions:")
SECT = ("## 描述", "## 核心内容", "## 在层级体系中的位置", "## 相关知识元", "## 验证状态")
for f in files:
    p = ROOT / f
    if not p.exists():
        print(f"\n===== {f} ===== MISSING\n")
        continue
    text = p.read_text(encoding="utf-8").replace("\r\n", "\n")
    parts = text.split("\n---\n", 1)
    fm = parts[0]
    body = parts[1] if len(parts) > 1 else ""
    print(f"\n===== {f} =====")
    for line in fm.split("\n"):
        s = line.rstrip()
        if any(s.lstrip().startswith(k) for k in KEYS):
            print("  " + s)
    # sections
    chunks = re.split(r"(?m)^## ", body)
    for c in chunks:
        head = c.split("\n", 1)[0].strip()
        if ("## " + head) in SECT or head in [x[3:] for x in SECT]:
            print("## " + c.rstrip())
    print()
