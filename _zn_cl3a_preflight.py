# -*- coding: utf-8 -*-
"""Preflight CL3a: validate claim rows, source spans, block ids, and patches."""
import json
from pathlib import Path

import yaml

ROOT = Path(r"D:/中国设计史研究")
DOC = "2016-xiayanjing-zhongguo-yishu-shejishi-upgrade"
SRC = ROOT / "03基础书籍-md文档/中国艺术设计史（升级版）_夏燕靖_2016_上海人民美术出版社.md"
REG = ROOT / "04-knowledge/quality/claim-registry.yml"
CAND = ROOT / "06-runtime/state/candidate-index.jsonl"
ROWS = json.loads((ROOT / "_zn_cl3a_rows.json").read_text(encoding="utf-8"))
PATCH = json.loads((ROOT / "_zn_cl3a_patch.json").read_text(encoding="utf-8"))

lines = SRC.read_text(encoding="utf-8").splitlines()
reg_text = REG.read_text(encoding="utf-8")
reg = yaml.safe_load(reg_text)
assert len(reg) == 259, len(reg)
assert reg_text.splitlines()[2] == "# total: 259", reg_text.splitlines()[2]
assert reg[-1]["claim_id"] == "claim-0259"

cand_rows = [json.loads(l) for l in CAND.read_text(encoding="utf-8").splitlines() if l.strip()]
cand = {r["candidate_id"]: r for r in cand_rows}
assert len(cand) == len(cand_rows)

NEW_IDS = [f"claim-{i:04d}" for i in range(260, 273)]
assert [r["claim_id"] for r in ROWS] == NEW_IDS

KEYWORDS = {
    "claim-0260": ["传统学科分类法", "技艺", "营造"],
    "claim-0261": ["人与古猿", "制造工具"],
    "claim-0262": ["华夏文明", "多点起源"],
    "claim-0263": ["黄河流域", "发展中心"],
    "claim-0264": ["原始社会的设计", "造物活动"],
    "claim-0265": ["最早陶器", "仙人洞"],
    "claim-0266": ["仰韶文化", "私有制度萌芽"],
    "claim-0267": ["陶器比石器更为重要"],
    "claim-0268": ["陶鬻", "实用与美观"],
    "claim-0269": ["有座古城", "中华第一城"],
    "claim-0270": ["鱼鳍形足陶鼎", "水鸟形陶壶"],
    "claim-0271": ["巢居和穴居", "美的规律"],
    "claim-0272": ["最早实现犁耕", "学界尚有争议"],
}

used_candidates = set()
bad = 0
for row in ROWS:
    cid = row["claim_id"]
    src = row["source"]
    c = cand[src["candidate_id"]]
    assert c["state"] == "needs_evidence", (cid, c["state"])
    assert c["candidate_type"] == "claim", cid
    cspan = c["payload"]["source_span"]
    span = src["source_span"]
    assert cspan["line_start"] <= span["line_start"] <= span["line_end"] <= cspan["line_end"], (
        cid, cspan, span)
    assert set(span["block_ids"]) <= set(cspan["block_ids"]), (cid, span["block_ids"], cspan["block_ids"])
    assert span["key_lines"] and all(span["line_start"] <= n <= span["line_end"] for n in span["key_lines"]), cid
    assert span["span_kind"] in {"line", "contiguous", "bounded"}, cid
    text = "\n".join(lines[n - 1] for n in span["key_lines"])
    missing = [k for k in KEYWORDS[cid] if k not in text]
    if missing:
        bad += 1
        print("MISSING_KEYWORD", cid, missing, text[:160])
    assert '"' not in row["statement_zh"], cid
    assert '"' not in row["discussion_notes"], cid
    assert row["consensus"] == "tentative" and row["review_status"] == "source_backed"
    assert row["created"] == "2026-10-27" and row["updated"] == "2026-10-27"
    for p in row["supported_by"]:
        assert (ROOT / p).is_file(), (cid, p)
    used_candidates.add(src["candidate_id"])
    for m in src.get("merged_candidate_ids") or []:
        assert cand[m]["state"] == "needs_evidence", (cid, m)
        used_candidates.add(m)

# Patch validation.
reg_by_id = {r["claim_id"]: r for r in reg}
patched = set()
for p in PATCH:
    claim_id = p["claim_id"]
    assert claim_id in reg_by_id, claim_id
    claim = reg_by_id[claim_id]
    assert claim["source"]["doc_id"] == "2009-xiayanjing-zhongguo-shejishi", claim_id
    assert not claim["source"].get("merged_candidate_ids"), claim_id
    cid = p["candidate_id"]
    c = cand[cid]
    assert c["state"] == "needs_evidence", (cid, c["state"])
    assert c["candidate_type"] == "claim", cid
    cspan = c["payload"]["source_span"]
    span = p["corroborating_span"]
    assert cspan["line_start"] <= span["line_start"] <= span["line_end"] <= cspan["line_end"], (
        cid, cspan, span)
    assert set(span["block_ids"]) <= set(cspan["block_ids"]), (cid, span["block_ids"], cspan["block_ids"])
    assert span["key_lines"] and all(span["line_start"] <= n <= span["line_end"] for n in span["key_lines"]), cid
    text = "\n".join(lines[n - 1] for n in span["key_lines"])
    assert text.strip(), cid
    used_candidates.add(cid)
    patched.add(claim_id)

assert len(used_candidates) == 27, len(used_candidates)
assert len(patched) == 13, len(patched)
print("registry", len(reg), "header", reg_text.splitlines()[2])
print("rows", len(ROWS), "patches", len(PATCH), "patched_claims", len(patched))
print("used_candidates", len(used_candidates), "bad", bad)
print("candidate_states", {s: sum(1 for r in cand_rows if r["state"] == s)
                           for s in sorted({r["state"] for r in cand_rows})})
print("2016_needs", sum(1 for r in cand_rows
                        if r["candidate_type"] == "claim"
                        and r["candidate_id"].startswith(DOC + ":")
                        and r["state"] == "needs_evidence"))
