# -*- coding: utf-8 -*-
import json
from collections import Counter
from pathlib import Path

ROOT = Path(r"D:/中国设计史研究")
ROWS = json.loads((ROOT / "_zn_cl4b_rows.json").read_text(encoding="utf-8"))
link = Counter()
dist = Counter()
for r in ROWS:
    for p in r["supported_by"]:
        link[p.split("/")[2]] += 1
    for p in set(r["supported_by"]):
        dist[p.split("/")[2]] += 1
print("links_by_type", dict(sorted(link.items())))
gdist = Counter(p.split("/")[2] for p in {p for r in ROWS for p in r["supported_by"]})
print("global_distinct_by_type", dict(sorted(gdist.items())))
print("distinct_paths", len({p for r in ROWS for p in r["supported_by"]}))
print("no_support", [r["claim_id"] for r in ROWS if not r["supported_by"]])
