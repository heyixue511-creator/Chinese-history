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
print("ids_ok", [r["claim_id"] for r in rows[219:]] == [f"claim-{i:04d}" for i in range(220, 238)])
print("types", dict(Counter(r["claim_type"] for r in rows[219:])))
print("confidence", dict(Counter(r["confidence"] for r in rows[219:])))
print("supported_by", sum(1 for r in rows[219:] if r.get("supported_by")))
print("links", sum(len(r.get("supported_by") or []) for r in rows[219:]))
print("distinct", len({p for r in rows[219:] for p in r.get("supported_by") or []}))
print("tentative", all(r["consensus"] == "tentative" for r in rows))
print("source_backed", all(r["review_status"] == "source_backed" for r in rows))
print("span_kinds", dict(Counter(r["source"]["source_span"]["span_kind"] for r in rows[219:])))
index = [json.loads(l) for l in CAND.read_text(encoding="utf-8").splitlines() if l.strip()]
print("cand_rows", len(index))
print("cand_states", dict(Counter(r["state"] for r in index)))
print("cand_lifecycle", dict(Counter(r["lifecycle_class"] for r in index)))
targets = [f"2009-xiayanjing-zhongguo-shejishi:cand-{n}" for n in
           ["05-63", "05-64", "05-91", "05-69", "05-70", "05-71",
            "05-75", "05-76", "05-78", "05-79", "05-80", "05-83",
            "05-85", "06-55", "06-56", "06-57", "06-58", "06-77"]]
by = {r["candidate_id"]: r for r in index}
print("cl2h_applied", sum(1 for c in targets if by[c]["state"] == "applied" and by[c]["candidate_type"] == "claim"))
print("cl2h_targets", all(by[c].get("target_ref", "").startswith("claim/") for c in targets))
print("cl2h_terminal", all(by[c].get("lifecycle_class") == "terminal" for c in targets))
print("refs", [by[c]["target_ref"] for c in targets])
