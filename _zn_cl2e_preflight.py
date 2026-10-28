# -*- coding: utf-8 -*-
import json
from collections import Counter
from pathlib import Path
import yaml

ROOT = Path(r"D:/中国设计史研究")
REG = ROOT / "04-knowledge/quality/claim-registry.yml"
CAND = ROOT / "06-runtime/state/candidate-index.jsonl"
rows = json.loads((ROOT / "_zn_claim_xyj09e_rows.json").read_text(encoding="utf-8"))
text = REG.read_text(encoding="utf-8")
parsed = yaml.safe_load(text)
print("registry", len(parsed), "header131", "# total: 131" in text)
print("last_id", parsed[-1]["claim_id"])
index = [json.loads(l) for l in CAND.read_text(encoding="utf-8").splitlines() if l.strip()]
by = {r["candidate_id"]: r for r in index}
print("states", dict(Counter(r["state"] for r in index)))
bad = []
for row in rows:
    cid = row["source"]["candidate_id"]
    c = by.get(cid)
    if not c:
        bad.append((cid, "missing")); continue
    sp = row["source"]["source_span"]
    csp = (c.get("payload") or {}).get("source_span") or {}
    ok = (c["state"] == "needs_evidence" and c["candidate_type"] == "claim"
          and csp.get("line_start", 1) <= sp["line_start"] <= sp["line_end"] <= csp.get("line_end", 0))
    if not ok:
        bad.append((cid, c["state"], c["candidate_type"], csp, sp["line_start"], sp["line_end"]))
print("bad", len(bad))
for b in bad:
    print(b)
