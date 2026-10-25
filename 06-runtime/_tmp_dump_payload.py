# -*- coding: utf-8 -*-
"""Dump full payloads for a chosen candidate set."""
import json
import sys
from pathlib import Path

ids = [line.strip() for line in Path(sys.argv[1]).read_text(encoding="utf-8").splitlines() if line.strip()]
rows = [json.loads(l) for l in Path("06-runtime/state/candidate-index.jsonl").read_text(encoding="utf-8").splitlines() if l.strip()]
by_id = {r["candidate_id"]: r for r in rows}
out = []
for cid in ids:
    r = by_id.get(cid)
    if not r:
        out.append(f"{cid}\tMISSING")
        continue
    p = r["payload"]
    out.append(f"### {cid}\n{json.dumps(p, ensure_ascii=False, indent=1)}\n")
Path(sys.argv[2]).write_text("\n".join(out), encoding="utf-8")
print("dumped", len(ids))
