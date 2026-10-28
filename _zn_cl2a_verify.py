# -*- coding: utf-8 -*-
import json
from collections import Counter
from pathlib import Path

import yaml

root = Path(r"D:/中国设计史研究")
reg = (root / "04-knowledge/quality/claim-registry.yml").read_text(encoding="utf-8")
rows = yaml.safe_load(reg)
print("registry_rows", len(rows))
print("registry_header_total", [l for l in reg.splitlines()[:3]])
print("first_last", rows[0]["claim_id"], rows[-1]["claim_id"])
print("claim_0001_0036_untouched", [r["claim_id"] for r in rows[:36]] == [f"claim-{i:04d}" for i in range(1, 37)])
print("new_ids", [r["claim_id"] for r in rows[36:]] == [f"claim-{i:04d}" for i in range(37, 70)])
print("types", dict(Counter(r["claim_type"] for r in rows[36:])))
print("confidence", dict(Counter(r["confidence"] for r in rows[36:])))
print("with_supported_by", sum(1 for r in rows[36:] if r["supported_by"]))
print("ascii_quote_zh", sum(1 for r in rows if '"' in r["statement_zh"]))

cand = [json.loads(l) for l in (root / "06-runtime/state/candidate-index.jsonl").read_text(encoding="utf-8").splitlines() if l.strip()]
print("cand_rows", len(cand))
print("states", dict(Counter(r["state"] for r in cand)))
print("lifecycle", dict(Counter(r["lifecycle_class"] for r in cand)))
claim_cands = [r for r in cand if r.get("candidate_type") == "claim"]
print("claim_cand_states", dict(Counter(r["state"] for r in claim_cands)))
wn = [r for r in cand if r["candidate_id"].startswith("2009-xiayanjing-zhongguo-shejishi:")]
print("xiayanjing09_states", dict(Counter(r["state"] for r in wn)))
newly = [r for r in cand if r["candidate_id"].startswith("2009-xiayanjing-zhongguo-shejishi:cand-01-") and r["state"] == "applied"]
print("newly_applied", len(newly), "with_target", sum(1 for r in newly if r.get("target_ref", "").startswith("claim/")))
print("bad_decision", [r["candidate_id"] for r in newly if r["decision"].get("status") != "approved" or r["decision"].get("decided_by") != "Agent"])
