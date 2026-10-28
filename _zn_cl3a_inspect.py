# -*- coding: utf-8 -*-
"""Dump CL3a candidate payloads and overlapping existing claims for adjudication."""
import json
from pathlib import Path

import yaml

ROOT = Path(r"D:/中国设计史研究")
DOC = "2016-xiayanjing-zhongguo-yishu-shejishi-upgrade"
CAND = ROOT / "06-runtime/state/candidate-index.jsonl"
REG = ROOT / "04-knowledge/quality/claim-registry.yml"

rows = [json.loads(l) for l in CAND.read_text(encoding="utf-8").splitlines() if l.strip()]
sel = [r for r in rows if r["candidate_id"].startswith(DOC + ":") and r["candidate_type"] == "claim"
       and (r.get("payload") or {}).get("source_span", {}).get("line_start", 99999) <= 606]
sel.sort(key=lambda r: (r["payload"]["source_span"]["line_start"], r["candidate_id"]))

print("=== CANDIDATES", len(sel), "===")
for r in sel:
    p = r["payload"]
    sp = p["source_span"]
    print("\n###", r["candidate_id"], r["state"])
    print("span", sp)
    print("scope:", p.get("claim_scope"))
    print("text:", p.get("claim_text"))
    print("match:", json.dumps(p.get("knowledge_match"), ensure_ascii=False))
    print("confidence:", p.get("proposed_confidence"))
    print("support_note:", p.get("support_note"))

claims = yaml.safe_load(REG.read_text(encoding="utf-8"))
print("\n\n=== CLAIMS 0036-0052 ===")
for c in claims:
    n = int(c["claim_id"].split("-")[1])
    if 36 <= n <= 52:
        print("\n###", c["claim_id"], c["claim_type"], c["confidence"])
        print(c["statement_zh"])
        print("source:", c["source"]["doc_id"], c["source"]["source_span"]["line_start"],
              c["source"]["source_span"]["line_end"], "cand",
              c["source"]["candidate_id"])
        print("supported_by:", c.get("supported_by"))

kws = ["良渚", "陶鬻", "陶鬶", "犁耕", "石犁", "干栏", "巢居", "穴居", "华夏文明",
       "技艺", "营造", "私有制", "分工", "仙人洞", "陶器", "设计起源", "工具"]
print("\n\n=== KEYWORD OVERLAP (outside 0036-0052) ===")
seen = set()
for c in claims:
    n = int(c["claim_id"].split("-")[1])
    if 36 <= n <= 52:
        continue
    text = c["statement_zh"]
    hit = [k for k in kws if k in text]
    if hit and c["claim_id"] not in seen:
        seen.add(c["claim_id"])
        print(c["claim_id"], c["claim_type"], hit)
        print("  ", text[:260].replace("\n", " "))
