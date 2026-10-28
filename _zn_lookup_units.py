# -*- coding: utf-8 -*-
import re
import sys
from pathlib import Path

ROOT = Path(r"D:/中国设计史研究/04-knowledge/units")
kws = sys.argv[1].split(",")
hits = []
for p in ROOT.rglob("*.md"):
    t = p.read_text(encoding="utf-8")
    head = t.split("---", 2)[1] if t.startswith("---") else ""
    m = re.search(r"^title:\s*(.+)$", head, re.M)
    title = m.group(1).strip() if m else ""
    a = re.search(r"^aliases:\s*(.*?)(?=^\w|\Z)", head, re.M | re.S)
    aliases = a.group(1) if a else ""
    blob = title + " " + aliases
    if any(k in blob for k in kws):
        hits.append((str(p.relative_to(ROOT)).replace("\\", "/"), title))
for path, title in sorted(hits):
    print(path, "|", title)
print("count", len(hits))
