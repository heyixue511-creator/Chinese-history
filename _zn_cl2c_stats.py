# -*- coding: utf-8 -*-
import json
from collections import Counter
from pathlib import Path
ROOT = Path(r"D:/中国设计史研究")
DOC = "2009-xiayanjing-zhongguo-shejishi"
rows = json.loads((ROOT / "_zn_claim_xyj09c_rows.json").read_text(encoding="utf-8"))
paths = [p for r in rows for p in r["supported_by"]]
print("links", len(paths), "distinct", len(set(paths)))
print("by_type", dict(Counter(p.split("/")[3] for p in paths)))
print("by_distinct_type", dict(Counter(p.split("/")[3] for p in set(paths))))
top = Counter(paths).most_common(6)
print("top", top)
index = [json.loads(l) for l in (ROOT / "06-runtime/state/candidate-index.jsonl").read_text(encoding="utf-8").splitlines() if l.strip()]
rem = [r for r in index if r["candidate_type"] == "claim" and r["candidate_id"].startswith(DOC + ":") and r["state"] == "needs_evidence"]
print("xyj09_remaining", len(rem))
print("rem_by_chapter", dict(Counter((r.get("payload") or {}).get("source_span", {}).get("chapter", "?") for r in rem)))
allrem = [r for r in index if r["candidate_type"] == "claim" and r["state"] == "needs_evidence"]
print("all_claim_remaining", len(allrem))
print("by_doc", dict(Counter(r["candidate_id"].split(":")[0] for r in allrem)))
