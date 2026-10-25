# -*- coding: utf-8 -*-
"""Inventory of active unit candidates by type and book."""
import json
from collections import Counter
from pathlib import Path

rows = [json.loads(l) for l in Path("06-runtime/state/candidate-index.jsonl").read_text(encoding="utf-8").splitlines() if l.strip()]
active = [r for r in rows if r.get("lifecycle_class") == "active" and r.get("candidate_type") == "unit"]
by_type = Counter(r["payload"].get("unit_type") for r in active)
print("active unit candidates by type:", dict(by_type.most_common()))
by_book_type = {}
for r in active:
    book = r["candidate_id"].split(":")[0]
    t = r["payload"].get("unit_type")
    by_book_type.setdefault(t, Counter())[book] += 1
for t in ["event", "procedure", "institution", "place", "publication", "person", "work", "term"]:
    print(t, dict(by_book_type.get(t, {}).most_common()))
with Path("06-runtime/_tmp_inv4.txt").open("w", encoding="utf-8") as fh:
    for t, c in by_book_type.items():
        fh.write(f"{t}\t" + "\t".join(f"{b}:{n}" for b, n in c.most_common()) + "\n")
