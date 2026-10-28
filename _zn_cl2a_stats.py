# -*- coding: utf-8 -*-
import json
from pathlib import Path

root = Path(r"D:/中国设计史研究")
rows = json.loads((root / "_zn_claim_xyj09a_rows.json").read_text(encoding="utf-8"))
paths = [p for r in rows for p in r["supported_by"]]
print("claims", len(rows))
print("links", len(paths))
print("distinct_paths", len(set(paths)))
from collections import Counter
print("by_type_prefix", dict(Counter(p.split("/")[2] for p in paths)))
print("top_paths", Counter(paths).most_common(10))
claim_lines = set()
for r in rows:
    sp = r["source"]["source_span"]
    claim_lines.update(range(sp["line_start"], sp["line_end"] + 1))
print("unique_claim_lines", len(claim_lines))
print("id_span_types", dict(Counter(r["source"]["source_span"]["span_kind"] for r in rows)))
