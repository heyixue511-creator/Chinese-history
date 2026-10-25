# -*- coding: utf-8 -*-
"""Export a digest of active candidates for one book prefix and unit type."""
import json
import sys
from pathlib import Path

book = sys.argv[1]
utype = sys.argv[2]
out_path = Path(sys.argv[3])
rows = [json.loads(l) for l in Path("06-runtime/state/candidate-index.jsonl").read_text(encoding="utf-8").splitlines() if l.strip()]
items = [r for r in rows if r.get("lifecycle_class") == "active" and r.get("candidate_type") == "unit"
         and r["candidate_id"].split(":")[0] == book and r["payload"].get("unit_type") == utype]
items.sort(key=lambda r: (r["payload"].get("source_span", {}).get("line_start") or 0, r["candidate_id"]))
lines = []
for r in items:
    p = r["payload"]
    span = p.get("source_span", {})
    lines.append(f"{r['candidate_id']}\tL{span.get('line_start')}-L{span.get('line_end')}\t{p.get('title')}\t{p.get('proposed_slug')}")
    lines.append(f"  summary: {p.get('summary','').replace(chr(10),' ')}")
out_path.write_text("\n".join(lines), encoding="utf-8")
print(book, utype, "count", len(items))
