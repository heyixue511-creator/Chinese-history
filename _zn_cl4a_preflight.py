# -*- coding: utf-8 -*-
"""Preflight CL3b: validate 10 claim rows, 13 patches, spans, blocks, keywords."""
import json
from pathlib import Path

import yaml

ROOT = Path(r"D:/中国设计史研究")
DOC = "2016-xiayanjing-zhongguo-yishu-shejishi-upgrade"
SRC = ROOT / "03基础书籍-md文档/中国艺术设计史（升级版）_夏燕靖_2016_上海人民美术出版社.md"
REG = ROOT / "04-knowledge/quality/claim-registry.yml"
CAND = ROOT / "06-runtime/state/candidate-index.jsonl"
ROWS = json.loads((ROOT / "_zn_cl4a_rows.json").read_text(encoding="utf-8"))
PATCH = json.loads((ROOT / "_zn_cl4a_patch.json").read_text(encoding="utf-8"))

lines = SRC.read_text(encoding="utf-8").splitlines()
reg_text = REG.read_text(encoding="utf-8")
reg = yaml.safe_load(reg_text)
assert len(reg) == 272, len(reg)
assert reg_text.splitlines()[2] == "# total: 272", reg_text.splitlines()[2]
assert reg[-1]["claim_id"] == "claim-0272"

cand_rows = [json.loads(l) for l in CAND.read_text(encoding="utf-8").splitlines() if l.strip()]
cand = {r["candidate_id"]: r for r in cand_rows}
assert len(cand) == len(cand_rows)

NEW_IDS = [f"claim-{i:04d}" for i in range(273, 283)]
assert [r["claim_id"] for r in ROWS] == NEW_IDS
assert len(PATCH) == 13

KEYWORDS = {
    "claim-0273": ["先秦三代", "青铜时代", "始发期"],
    "claim-0274": ["甲骨文应是比较成熟的文字体系", "古文字", "近代文字"],
    "claim-0275": ["独树一帜", "万余件"],
    "claim-0276": ["合范法", "泥模", "浇铸"],
    "claim-0277": ["133厘米", "875千克", "一两百名工匠"],
    "claim-0278": ["两种相对的看法", "新近考古发掘证明", "曾侯乙"],
    "claim-0279": ["柱状足呈锥状足", "范芯浇铸全封闭"],
    "claim-0280": ["四个时期", "商早期", "殷商后期", "西周晚期至春秋中期", "春秋晚期到战国初期"],
    "claim-0281": ["木工", "金工", "漆工", "皮革工"],
    "claim-0282": ["西周时期就是统治者的礼服", "政治意义"],
}

PATCH_KEYWORDS = {
    "claim-0052": ["夏朝", "二里头"],
    "claim-0054": ["商晚期和西周早期", "统治权力"],
    "claim-0055": ["礼制", "社会等级"],
    "claim-0056": ["藏礼于器", "九鼎"],
    "claim-0057": ["莲鹤方壶", "礼器"],
    "claim-0058": ["殷商", "西周", "造型"],
    "claim-0061": ["陶器", "设计意识"],
    "claim-0062": ["原始瓷器", "商代中期"],
    "claim-0063": ["甘泽之战", "车战"],
    "claim-0064": ["商代车", "车马坑"],
    "claim-0066": ["建筑特点", "木结构"],
    "claim-0067": ["营建都邑", "周礼·考工记"],
    "claim-0069": ["深衣制", "上衣下裳"],
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

# Patch validation.
reg_by_id = {r["claim_id"]: r for r in reg}
patched = set()
for p in PATCH:
    claim_id = p["claim_id"]
    assert claim_id in reg_by_id, claim_id
    claim = reg_by_id[claim_id]
    assert claim["source"]["doc_id"] == "2009-xiayanjing-zhongguo-shejishi", claim_id
    assert not claim["source"].get("merged_candidate_ids"), claim_id
    assert not claim["source"].get("corroborating_spans"), claim_id
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
    missing = [k for k in PATCH_KEYWORDS[claim_id] if k not in text]
    if missing:
        bad += 1
        print("PATCH_MISSING_KEYWORD", claim_id, cid, missing, text[:160])
    assert text.strip(), cid
    used_candidates.add(cid)
    patched.add(claim_id)

assert len(used_candidates) == 23, len(used_candidates)
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
assert bad == 0
