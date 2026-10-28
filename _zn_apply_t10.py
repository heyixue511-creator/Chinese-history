# -*- coding: utf-8 -*-
"""Apply batch T9 decisions to the candidate index."""
import json
from collections import Counter
from pathlib import Path

ROOT = Path(r"D:/中国设计史研究")
INDEX = ROOT / "06-runtime/state/candidate-index.jsonl"
DATE = "2026-10-27"

cfg = json.loads((ROOT / "_zn_decisions_t10.json").read_text(encoding="utf-8"))
by_cid = {d["cid"]: d for d in cfg["decisions"]}

rows = []
before = Counter()
changed = 0
for line in INDEX.read_text(encoding="utf-8").splitlines():
    if not line.strip():
        continue
    r = json.loads(line)
    before[r["state"]] += 1
    d = by_cid.get(r["candidate_id"])
    if d:
        assert r["state"] == "needs_evidence", r["candidate_id"]
        if d["action"] == "rejected":
            r["state"] = "rejected"
            reason = d["approve"]
            status = "rejected"
        elif d["action"] == "no_delta":
            r["state"] = "no_delta"
            reason = d["approve"]
            status = "approved"
        else:
            r["state"] = "applied"
            reason = d["apply_note"]
            status = "approved"
        r["target_ref"] = d["target"]
        r["decision"] = {
            "decided_at": DATE,
            "decided_by": "Agent",
            "reason": reason,
            "status": status,
        }
        r["lifecycle_class"] = "terminal"
        r["updated_at"] = DATE
        changed += 1
    rows.append(r)

assert changed == len(by_cid), (changed, len(by_cid))

tmp = INDEX.with_suffix(".jsonl.tmp")
with tmp.open("w", encoding="utf-8", newline="\n") as h:
    for r in rows:
        h.write(json.dumps(r, ensure_ascii=False, sort_keys=True) + "\n")
tmp.replace(INDEX)

after = Counter(r["state"] for r in rows)
print(json.dumps({"changed": changed, "rows": len(rows), "before": before, "after": after}, ensure_ascii=False))
