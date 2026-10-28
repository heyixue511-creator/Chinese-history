# -*- coding: utf-8 -*-
import json
from collections import Counter
from pathlib import Path

import yaml

ROOT = Path(r"D:/中国设计史研究")
REG = ROOT / "04-knowledge/quality/claim-registry.yml"
CAND = ROOT / "06-runtime/state/candidate-index.jsonl"
DOC = "2009-xiayanjing-zhongguo-shejishi"
text = REG.read_text(encoding="utf-8")
rows = yaml.safe_load(text)
print("total", len(rows), "header", text.splitlines()[2])
assert len(rows) == 259
assert rows[-1]["claim_id"] == "claim-0259"
assert [r["claim_id"] for r in rows[246:]] == [f"claim-{i:04d}" for i in range(247, 260)]
print("ids_ok", True)
print("types", dict(Counter(r["claim_type"] for r in rows[246:])))
print("confidence", dict(Counter(r["confidence"] for r in rows[246:])))
print("supported_by", sum(1 for r in rows[246:] if r.get("supported_by")))
print("links", sum(len(r.get("supported_by") or []) for r in rows[246:]))
print("distinct", len({p for r in rows[246:] for p in r.get("supported_by") or []}))
print("tentative", all(r["consensus"] == "tentative" for r in rows))
print("source_backed", all(r["review_status"] == "source_backed" for r in rows))
print("span_kinds", dict(Counter(r["source"]["source_span"]["span_kind"] for r in rows[246:])))
print("empty_support", [r["claim_id"] for r in rows[246:] if not r.get("supported_by")])

index = [json.loads(l) for l in CAND.read_text(encoding="utf-8").splitlines() if l.strip()]
print("cand_rows", len(index))
print("cand_states", dict(Counter(r["state"] for r in index)))
print("cand_lifecycle", dict(Counter(r["lifecycle_class"] for r in index)))
targets = [DOC + ":cand-" + n for n in
           ["06-67", "06-68", "06-69", "06-70", "06-71", "06-72", "06-73",
            "07-10", "07-18", "07-22", "07-23", "07-24", "07-25"]]
by = {r["candidate_id"]: r for r in index}
print("cl2j_applied", sum(1 for c in targets if by[c]["state"] == "applied" and by[c]["candidate_type"] == "claim"))
print("cl2j_targets", all(by[c].get("target_ref", "").startswith("claim/") for c in targets))
print("cl2j_terminal", all(by[c].get("lifecycle_class") == "terminal" for c in targets))
print("refs", [by[c]["target_ref"] for c in targets])
print("remaining_xyj09", sum(1 for r in index
      if r["candidate_type"] == "claim" and r["candidate_id"].startswith(DOC + ":")
      and r["state"] == "needs_evidence"))
