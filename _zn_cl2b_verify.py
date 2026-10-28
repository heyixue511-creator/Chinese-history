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
print("ids_ok", [r["claim_id"] for r in rows[69:]] == [f"claim-{i:04d}" for i in range(70, 103)])
print("types", dict(Counter(r["claim_type"] for r in rows[69:])))
print("supported_by", sum(1 for r in rows[69:] if r.get("supported_by")))
print("links", sum(len(r.get("supported_by") or []) for r in rows[69:]))
print("tentative", all(r["consensus"] == "tentative" for r in rows))
print("source_backed", all(r["review_status"] == "source_backed" for r in rows))
index = [json.loads(l) for l in CAND.read_text(encoding="utf-8").splitlines() if l.strip()]
print("cand_states", dict(Counter(r["state"] for r in index)))
print("cand_lifecycle", dict(Counter(r["lifecycle_class"] for r in index)))
applied = [r for r in index if r["state"] == "applied" and r["candidate_id"].startswith("2009-xiayanjing-zhongguo-shejishi:cand-02-")]
print("cl2b_applied", len(applied))
print("cl2b_targets", all(r.get("target_ref", "").startswith("claim/") for r in applied))
