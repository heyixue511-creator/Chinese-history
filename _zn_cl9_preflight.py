# -*- coding: utf-8 -*-
"""Preflight CL6a: validate 8 claim rows, 9 patches, spans, blocks, keywords."""
import json
from pathlib import Path

import yaml

ROOT = Path(r"D:/中国设计史研究")
DOC = "2016-xiayanjing-zhongguo-yishu-shejishi-upgrade"
SRC = ROOT / "03基础书籍-md文档/中国艺术设计史（升级版）_夏燕靖_2016_上海人民美术出版社.md"
REG = ROOT / "04-knowledge/quality/claim-registry.yml"
CAND = ROOT / "06-runtime/state/candidate-index.jsonl"
ROWS = json.loads((ROOT / "_zn_cl9_rows.json").read_text(encoding="utf-8"))
PATCH = json.loads((ROOT / "_zn_cl9_patch.json").read_text(encoding="utf-8"))

lines = SRC.read_text(encoding="utf-8").splitlines()
reg_text = REG.read_text(encoding="utf-8")
reg = yaml.safe_load(reg_text)
assert len(reg) == 337, len(reg)
assert reg_text.splitlines()[2] == "# total: 337", reg_text.splitlines()[2]
assert reg[-1]["claim_id"] == "claim-0337"

cand_rows = [json.loads(l) for l in CAND.read_text(encoding="utf-8").splitlines() if l.strip()]
cand = {r["candidate_id"]: r for r in cand_rows}
assert len(cand) == len(cand_rows)

NEW_IDS = [f"claim-{i:04d}" for i in range(338, 346)]
assert [r["claim_id"] for r in ROWS] == NEW_IDS
assert len(PATCH) == 9
assert len({p["claim_id"] for p in PATCH}) == 9

KEYWORDS = {
    "claim-0338": ["有意识地使蓝紫两种釉料", "不及宋钧精细"],
    "claim-0339": ["官府投注了极大的精力", "达到一个新的高峰"],
    "claim-0340": ["黄道婆", "棉织与丝织并列"],
    "claim-0341": ["百万斤", "铜器制作呈萎缩趋势"],
    "claim-0342": ["优先发展的一个行业", "进行督导", "较大的提高"],
    "claim-0343": ["规模巨大而有完整规划的都城", "600多年"],
    "claim-0344": ["周王礼制", "《周礼·考工记》"],
    "claim-0345": ["促销的手段", "促进作用"],
}

PATCH_KEYWORDS = {
    "claim-0197": ["取消了科举制度", "酒楼茶肆", "主要原因之一"],
    "claim-0198": ["青花、釉里红", "釉下彩"],
    "claim-0200": ["造型一般很大", "胎骨厚重"],
    "claim-0202": ["划花，成为当时的主流", "先声"],
    "claim-0206": ["掠夺了大量黄金", "纸币吸收黄金"],
    "claim-0209": ["整个宋元时期", "更趋向商品化"],
    "claim-0211": ["秧马是插秧和拔秧", "综合使用器具"],
    "claim-0216": ["锡质活字", "工效大为提高"],
    "claim-0218": ["迥异的对比", "结构更趋合理", "本色"],
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

assert len(used_candidates) == 17, len(used_candidates)
assert len(patched) == 9, len(patched)

chapter = [r for r in cand_rows
           if r["candidate_type"] == "claim"
           and r["candidate_id"].startswith(DOC + ":")
           and r["state"] == "needs_evidence"
           and 3595 <= r["payload"]["source_span"]["line_start"] <= 4110]
print("chapter_candidates", len(chapter))
assert len(chapter) == 17, len(chapter)
assert len(used_candidates) == 17

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
