# -*- coding: utf-8 -*-
"""Active unit candidate inventory by unit_type and document."""
import json
from collections import Counter, defaultdict
from pathlib import Path

rows = [json.loads(l) for l in Path("06-runtime/state/candidate-index.jsonl").read_text(encoding="utf-8").splitlines() if l.strip()]
active = [r for r in rows if r["state"] == "needs_evidence" and r["candidate_type"] == "unit"]

docs = {
    "2004": "2004-gaofeng",
    "2009xy": "2009-xiayanjing",
    "2009zn": "2009-zhaonong",
    "2010": "2010-tianzibing",
    "2011": "2011-lilixin",
    "2016": "2016-xiayanjing",
}
def doc_of(cid):
    for k, v in docs.items():
        if cid.startswith(v):
            return k
    return "?"

matrix = defaultdict(Counter)
for r in active:
    matrix[doc_of(r["candidate_id"])][r["payload"].get("unit_type", "?")] += 1

types = sorted({t for c in matrix.values() for t in c})
print("doc " + " ".join(f"{t:>10}" for t in types) + "  total")
for d in docs:
    c = matrix[d]
    print(f"{d:>4} " + " ".join(f"{c[t]:>10}" for t in types) + f"  {sum(c.values())}")
print("all  " + " ".join(f"{sum(matrix[d][t] for d in docs):>10}" for t in types))

# shortlist events and procedures, which are the smallest groups
for target in ("event", "procedure"):
    pick = [r for r in active if r["payload"].get("unit_type") == target]
    print(f"\n== {target}: {len(pick)} ==")
    for r in pick:
        p = r["payload"]
        span = p.get("source_span", {})
        print(f"{r['candidate_id']}\t{span.get('line_start')}-{span.get('line_end')}\t{p.get('title')}\t{p.get('proposed_slug')}")
