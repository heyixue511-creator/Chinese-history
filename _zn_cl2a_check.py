# -*- coding: utf-8 -*-
import json
from pathlib import Path

WANT = set("""cand-01-03 cand-01-04 cand-01-05 cand-01-92 cand-01-07 cand-01-15 cand-01-19 cand-01-28 cand-01-26 cand-01-30 cand-01-41 cand-01-42 cand-01-45 cand-01-48 cand-01-50 cand-01-51 cand-01-55 cand-01-57 cand-01-59 cand-01-64 cand-01-65 cand-01-67 cand-01-68 cand-01-70 cand-01-74 cand-01-76 cand-01-78 cand-01-80 cand-01-82 cand-01-83 cand-01-85 cand-01-87 cand-01-89""".split())
P = Path("06-runtime/state/candidate-index.jsonl")
out = []
for line in P.read_text(encoding="utf-8").splitlines():
    r = json.loads(line)
    cid = r.get("candidate_id", "")
    if cid.startswith("2009-xiayanjing-zhongguo-shejishi:") and cid.split(":")[1] in WANT:
        sp = (r.get("payload") or {}).get("source_span") or {}
        out.append((cid.split(":")[1], sp.get("line_start"), sp.get("line_end"), r.get("state"), r.get("candidate_type"), (r.get("payload") or {}).get("claim_scope")))
for x in sorted(out):
    print(x)
print("count", len(out))
