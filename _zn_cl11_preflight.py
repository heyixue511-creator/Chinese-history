# -*- coding: utf-8 -*-
"""Preflight CL8a: validate 4 claim rows, 8 patches, spans, blocks, keywords."""
import json
from pathlib import Path

import yaml

ROOT = Path(r"D:/中国设计史研究")
DOC = "2016-xiayanjing-zhongguo-yishu-shejishi-upgrade"
SRC = ROOT / "03基础书籍-md文档/中国艺术设计史（升级版）_夏燕靖_2016_上海人民美术出版社.md"
REG = ROOT / "04-knowledge/quality/claim-registry.yml"
CAND = ROOT / "06-runtime/state/candidate-index.jsonl"
ROWS = json.loads((ROOT / "_zn_cl11_rows.json").read_text(encoding="utf-8"))
PATCH = json.loads((ROOT / "_zn_cl11_patch.json").read_text(encoding="utf-8"))

lines = SRC.read_text(encoding="utf-8").splitlines()
reg_text = REG.read_text(encoding="utf-8")
reg = yaml.safe_load(reg_text)
assert len(reg) == 359, len(reg)
assert reg_text.splitlines()[2] == "# total: 359", reg_text.splitlines()[2]
assert reg[-1]["claim_id"] == "claim-0359"

cand_rows = [json.loads(l) for l in CAND.read_text(encoding="utf-8").splitlines() if l.strip()]
cand = {r["candidate_id"]: r for r in cand_rows}
assert len(cand) == len(cand_rows)

NEW_IDS = [f"claim-{i:04d}" for i in range(360, 364)]
assert [r["claim_id"] for r in ROWS] == NEW_IDS
assert len(PATCH) == 8
assert len({p["claim_id"] for p in PATCH}) == 8

KEYWORDS = {
    "claim-0360": ["限色", "首创", "普遍应用"],
    "claim-0361": ["300余家", "洋纱、洋布挤占"],
    "claim-0362": ["1861年", "缫丝业是我国近代民族工业的摇篮"],
    "claim-0363": ["《剪辫通令》", "冲垮了历代积习下来的衣冠等级制度"],
}

PATCH_KEYWORDS = {
    "claim-0239": ["伴随着近代手工业和对外贸易萌生和发展", "中断了"],
    "claim-0240": ["不是在资本主义萌芽的基础上自然地发展起来", "欧风美雨"],
    "claim-0241": ["西装基本款形基础", "垫肩收腰"],
    "claim-0242": ["具有本土意识的产品造型设计", "萌芽阶段"],
    "claim-0243": ["洋务运动是我国近代巨大社会变革", "现代设计孕育的土壤"],
    "claim-0244": ["东方式的淡雅、朴素和内敛", "书籍装帧设计的风格特色"],
    "claim-0245": ["并不是纯传统的", "折中主义的新形式"],
    "claim-0246": ["首次进行的具有规划设计意识", "新工艺、新材料"],
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
        print("MISSING_KEYWORD", cid, missing, text[:200])
    assert '"' not in row["statement_zh"], cid
    assert '"' not in row["discussion_notes"], cid
    assert row["consensus"] == "tentative" and row["review_status"] == "source_backed"
    assert row["created"] == "2026-10-27" and row["updated"] == "2026-10-27"
    for p in row["supported_by"]:
        assert (ROOT / p).is_file(), (cid, p)
    used_candidates.add(src["candidate_id"])
    for mc in src.get("merged_candidate_ids") or []:
        m = cand[mc]
        assert m["state"] == "needs_evidence", (cid, mc, m["state"])
        assert m["candidate_type"] == "claim", mc
        used_candidates.add(mc)

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
        print("PATCH_MISSING_KEYWORD", claim_id, cid, missing, text[:200])
    assert text.strip(), cid
    used_candidates.add(cid)
    patched.add(claim_id)

assert len(used_candidates) == 12, len(used_candidates)
assert len(patched) == 8, len(patched)

chapter = [r for r in cand_rows
           if r["candidate_type"] == "claim"
           and r["candidate_id"].startswith(DOC + ":")
           and r["state"] == "needs_evidence"
           and 4713 <= r["payload"]["source_span"]["line_start"] <= 5123]
print("chapter_candidates", len(chapter))
assert len(chapter) == 12, len(chapter)
assert len(used_candidates) == 12

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
