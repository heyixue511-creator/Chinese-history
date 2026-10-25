# -*- coding: utf-8 -*-
"""Extract source spans for a list of candidate ids."""
import json
import sys
from pathlib import Path

ids = [l.strip() for l in Path(sys.argv[1]).read_text(encoding="utf-8").splitlines() if l.strip()]
rows = [json.loads(l) for l in Path("06-runtime/state/candidate-index.jsonl").read_text(encoding="utf-8").splitlines() if l.strip()]
by_id = {r["candidate_id"]: r for r in rows}
cache = {}
out = []
for cid in ids:
    r = by_id.get(cid)
    if not r:
        out.append(f"### {cid} MISSING\n")
        continue
    p = r["payload"]
    span = p.get("source_span", {})
    ref = r["evidence_refs"][0]
    src = ref.split("#")[0]
    start = span.get("line_start")
    end = span.get("line_end")
    if src not in cache:
        cache[src] = Path(src).read_text(encoding="utf-8").splitlines()
    lines = cache[src]
    body = "\n".join(lines[(start or 1) - 1:end or start or 1])
    out.append(f"### {cid} | {p.get('title')} | L{start}-L{end}\n{body}\n")
Path(sys.argv[2]).write_text("\n".join(out), encoding="utf-8")
print("extracted", len(ids), "chars", sum(len(x) for x in out))
