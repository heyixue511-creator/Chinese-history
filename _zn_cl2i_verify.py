# -*- coding: utf-8 -*-
import json
from collections import Counter
from pathlib import Path
import yaml

ROOT = Path(r"D:/中国设计史研究")
REG = ROOT / "04-knowledge/quality/claim-registry.yml"
CAND = ROOT / "06-runtime/state/candidate-index.jsonl"
text = REG.read_text(encoding="utf-8")
rows = yaml.safe_load(text)
print("total", len(rows), "header", text.splitlines()[2])
print("ids_ok", [r["claim_id"] for r in rows[237:]] == [f"claim-{i:04d}" for i in range(238, 247)])
print("types", dict(Counter(r["claim_type"] for r in rows[237:])))
print("confidence", dict(Counter(r["confidence"] for r in rows[237:])))
print("supported_by", sum(1 for r in rows[237:] if r.get("supported_by")))
print("links", sum(len(r.get("supported_by") or []) for r in rows[237:]))
print("distinct", len({p for r in rows[237:] for p in r.get("supported_by") or []}))
print("tentative", all(r["consensus"] == "tentative" for r in rows))
print("source_backed", all(r["review_status"] == "source_backed" for r in rows))
print("span_kinds", dict(Counter(r["source"]["source_span"]["span_kind"] for r in rows[237:])))
index = [json.loads(l) for l in CAND.read_text(encoding="utf-8").splitlines() if l.strip()]
print("cand_rows", len(index))
print("cand_states", dict(Counter(r["state"] for r in index)))
print("cand_lifecycle", dict(Counter(r["lifecycle_class"] for r in index)))
targets = [f"2009-xiayanjing-zhongguo-shejishi:cand-{n}" for n in
           ["06-74", "06-59", "06-60", "06-61", "06-62", "06-63", "06-64", "06-65", "06-66"]]
by = {r["candidate_id"]: r for r in index}
print("cl2i_applied", sum(1 for c in targets if by[c]["state"] == "applied" and by[c]["candidate_type"] == "claim"))
print("cl2i_targets", all(by[c].get("target_ref", "").startswith("claim/") for c in targets))
print("cl2i_terminal", all(by[c].get("lifecycle_class") == "terminal" for c in targets))
print("refs", [by[c]["target_ref"] for c in targets])
