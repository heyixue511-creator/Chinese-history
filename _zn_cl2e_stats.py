# -*- coding: utf-8 -*-
import json
from collections import Counter
from pathlib import Path
import yaml

ROOT = Path(r"D:/中国设计史研究")
DOC = "2009-xiayanjing-zhongguo-shejishi"
rows = json.loads((ROOT / "_zn_claim_xyj09e_rows.json").read_text(encoding="utf-8"))
paths = [p for r in rows for p in r["supported_by"]]
print("links", len(paths), "distinct", len(set(paths)))
print("by_type", dict(Counter(p.split("/")[2] for p in paths)))
print("by_distinct_type", dict(Counter(p.split("/")[2] for p in set(paths))))
print("top", Counter(paths).most_common(6))
index = [json.loads(l) for l in (ROOT / "06-runtime/state/candidate-index.jsonl").read_text(encoding="utf-8").splitlines() if l.strip()]
rem = [r for r in index if r["candidate_type"] == "claim" and r["candidate_id"].startswith(DOC + ":") and r["state"] == "needs_evidence"]
print("xyj09_remaining", len(rem))
print("rem_by_chapter", dict(Counter((r.get("payload") or {}).get("source_span", {}).get("chapter", "?") for r in rem)))
allrem = [r for r in index if r["candidate_type"] == "claim" and r["state"] == "needs_evidence"]
print("all_claim_remaining", len(allrem))
print("by_doc", dict(Counter(r["candidate_id"].split(":")[0] for r in allrem)))
reg = yaml.safe_load((ROOT / "04-knowledge/quality/claim-registry.yml").read_text(encoding="utf-8"))
print("claims", len(reg), "with_supported_by", sum(1 for r in reg if r.get("supported_by")),
      "with_supports", sum(1 for r in reg if r.get("supports")),
      "with_en", sum(1 for r in reg if r.get("statement_en")))
rel = yaml.safe_load((ROOT / "04-knowledge/quality/relation-index.yml").read_text(encoding="utf-8"))
if isinstance(rel, dict):
    for k, v in rel.items():
        if isinstance(v, list):
            print("relation_key", k, len(v))
else:
    print("relation_entries", len(rel))
health = json.loads((ROOT / "06-runtime/state/current-health.json").read_text(encoding="utf-8"))
print("health_keys", list(health)[:12])
print("health", json.dumps(health, ensure_ascii=False)[:600])
auto = ROOT / "06-runtime/automation"
dirs = [d for d in auto.iterdir() if d.is_dir()]
files = [f for d in dirs for f in d.rglob("*") if f.is_file()]
print("batches", len(dirs), "files", len(files), "bytes", sum(f.stat().st_size for f in files))
