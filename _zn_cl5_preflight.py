# -*- coding: utf-8 -*-
"""Preflight CL3d: validate 17 claim rows, 7 patches, spans, blocks, keywords."""
import json
from pathlib import Path

import yaml

ROOT = Path(r"D:/中国设计史研究")
DOC = "2016-xiayanjing-zhongguo-yishu-shejishi-upgrade"
SRC = ROOT / "03基础书籍-md文档/中国艺术设计史（升级版）_夏燕靖_2016_上海人民美术出版社.md"
REG = ROOT / "04-knowledge/quality/claim-registry.yml"
CAND = ROOT / "06-runtime/state/candidate-index.jsonl"
ROWS = json.loads((ROOT / "_zn_cl5_rows.json").read_text(encoding="utf-8"))
PATCH = json.loads((ROOT / "_zn_cl5_patch.json").read_text(encoding="utf-8"))

lines = SRC.read_text(encoding="utf-8").splitlines()
reg_text = REG.read_text(encoding="utf-8")
reg = yaml.safe_load(reg_text)
assert len(reg) == 299, len(reg)
assert reg_text.splitlines()[2] == "# total: 299", reg_text.splitlines()[2]
assert reg[-1]["claim_id"] == "claim-0299"

cand_rows = [json.loads(l) for l in CAND.read_text(encoding="utf-8").splitlines() if l.strip()]
cand = {r["candidate_id"]: r for r in cand_rows}
assert len(cand) == len(cand_rows)

NEW_IDS = [f"claim-{i:04d}" for i in range(300, 317)]
assert [r["claim_id"] for r in ROWS] == NEW_IDS
assert len(PATCH) == 7

KEYWORDS = {
    "claim-0300": ["统一文字", "度量衡", "重要的条件"],
    "claim-0301": ["官手工业", "工官", "规模庞大", "分工细致"],
    "claim-0302": ["几十种", "整地农具8种", "谷物加工农具5种", "桔槔"],
    "claim-0303": ["二牛抬杠", "犁壁", "11世纪", "近千年"],
    "claim-0304": ["秦陵铜车马", "车舆", "系驾", "科学的证明"],
    "claim-0305": ["虹管灯", "缸灯", "虹吸", "铜牛灯"],
    "claim-0306": ["李约瑟", "提花机", "4个世纪"],
    "claim-0307": ["捣练", "砧杵", "草木灰", "脱胶"],
    "claim-0308": ["蜡染", "蜡缬", "绞缬", "夹缬"],
    "claim-0309": ["罢黜百家", "董仲舒", "阶级等级"],
    "claim-0310": ["漆器", "规模庞大", "新的高峰"],
    "claim-0311": ["6-8道", "金银扣器", "10倍"],
    "claim-0312": ["独轮车", "蒲元", "千余年"],
    "claim-0313": ["可载万人", "上起宫室", "初步成熟"],
    "claim-0314": ["成熟期的肇始", "2000年", "民族建筑"],
    "claim-0315": ["陈景元", "宣太后", "歪髻", "芈"],
    "claim-0316": ["脚踏提综", "斜织机", "10倍以上"],
}

PATCH_KEYWORDS = {
    "claim-0103": ["客观上", "冶铁技术", "交流和全面提高"],
    "claim-0104": ["兴起于春秋", "完全占统治地位"],
    "claim-0106": ["镜面微凸", "照出人面", "科学原理"],
    "claim-0107": ["李希霍芬", "丝绸之路", "1877"],
    "claim-0108": ["东汉晚期", "浙江", "成熟的青瓷器"],
    "claim-0110": ["多子盒", "9子", "11子", "集约性"],
    "claim-0114": ["设计理论", "重皇权", "典章"],
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

assert len(used_candidates) == 25, len(used_candidates)
assert len(patched) == 7, len(patched)

chapter = [r for r in cand_rows
           if r["candidate_type"] == "claim"
           and r["candidate_id"].startswith(DOC + ":")
           and r["state"] == "needs_evidence"
           and 1609 <= r["payload"]["source_span"]["line_start"] <= 2064]
print("chapter_candidates", len(chapter))
assert len(chapter) == 25, len(chapter)
assert len(used_candidates) == 25

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
