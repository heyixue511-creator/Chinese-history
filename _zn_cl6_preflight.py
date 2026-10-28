# -*- coding: utf-8 -*-
"""Preflight CL3e: validate 5 claim rows, 8 patches, spans, blocks, keywords."""
import json
from pathlib import Path

import yaml

ROOT = Path(r"D:/中国设计史研究")
DOC = "2016-xiayanjing-zhongguo-yishu-shejishi-upgrade"
SRC = ROOT / "03基础书籍-md文档/中国艺术设计史（升级版）_夏燕靖_2016_上海人民美术出版社.md"
REG = ROOT / "04-knowledge/quality/claim-registry.yml"
CAND = ROOT / "06-runtime/state/candidate-index.jsonl"
ROWS = json.loads((ROOT / "_zn_cl6_rows.json").read_text(encoding="utf-8"))
PATCH = json.loads((ROOT / "_zn_cl6_patch.json").read_text(encoding="utf-8"))

lines = SRC.read_text(encoding="utf-8").splitlines()
reg_text = REG.read_text(encoding="utf-8")
reg = yaml.safe_load(reg_text)
assert len(reg) == 316, len(reg)
assert reg_text.splitlines()[2] == "# total: 316", reg_text.splitlines()[2]
assert reg[-1]["claim_id"] == "claim-0316"

cand_rows = [json.loads(l) for l in CAND.read_text(encoding="utf-8").splitlines() if l.strip()]
cand = {r["candidate_id"]: r for r in cand_rows}
assert len(cand) == len(cand_rows)

NEW_IDS = [f"claim-{i:04d}" for i in range(317, 322)]
assert [r["claim_id"] for r in ROWS] == NEW_IDS
assert len(PATCH) == 8

KEYWORDS = {
    "claim-0317": ["进入到瓷器的时代", "坚固耐用", "耐酸碱", "易洗涤"],
    "claim-0318": ["生产规模扩大", "彩绘、描金、戗金、填漆", "装饰艺术化"],
    "claim-0319": ["平纹经线彩锦", "纬线起花", "菱纹锦", "双兽对鸟纹锦"],
    "claim-0320": ["脚踏纺车", "大月氏", "吴服", "拜占庭"],
    "claim-0321": ["服妖", "南梁", "跪坐传统", "唐宋"],
}

PATCH_KEYWORDS = {
    "claim-0115": ["300余年", "私营手工业普遍低迷", "曲折中有所发展"],
    "claim-0116": ["划时代的大事", "青花", "粉彩"],
    "claim-0117": ["南方青瓷", "北方青瓷", "各有千秋"],
    "claim-0119": ["魏晋风度", "宽衣博带", "华带飞髻"],
    "claim-0122": ["广铸佛像", "铜的缺乏", "日用铜器生产的衰落"],
    "claim-0129": ["犍陀罗", "中国形式的造像艺术"],
    "claim-0130": ["气韵生动", "古代设计思想的优秀传统精髓"],
    "claim-0131": ["施用有宜", "对人有益", "实用传统"],
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

assert len(used_candidates) == 13, len(used_candidates)
assert len(patched) == 8, len(patched)

chapter = [r for r in cand_rows
           if r["candidate_type"] == "claim"
           and r["candidate_id"].startswith(DOC + ":")
           and r["state"] == "needs_evidence"
           and 2065 <= r["payload"]["source_span"]["line_start"] <= 2460]
print("chapter_candidates", len(chapter))
assert len(chapter) == 13, len(chapter)
assert len(used_candidates) == 13

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
