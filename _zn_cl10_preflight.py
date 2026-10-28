# -*- coding: utf-8 -*-
"""Preflight CL7a: validate 14 claim rows, 7 patches, spans, blocks, keywords."""
import json
from pathlib import Path

import yaml

ROOT = Path(r"D:/中国设计史研究")
DOC = "2016-xiayanjing-zhongguo-yishu-shejishi-upgrade"
SRC = ROOT / "03基础书籍-md文档/中国艺术设计史（升级版）_夏燕靖_2016_上海人民美术出版社.md"
REG = ROOT / "04-knowledge/quality/claim-registry.yml"
CAND = ROOT / "06-runtime/state/candidate-index.jsonl"
ROWS = json.loads((ROOT / "_zn_cl10_rows.json").read_text(encoding="utf-8"))
PATCH = json.loads((ROOT / "_zn_cl10_patch.json").read_text(encoding="utf-8"))

lines = SRC.read_text(encoding="utf-8").splitlines()
reg_text = REG.read_text(encoding="utf-8")
reg = yaml.safe_load(reg_text)
assert len(reg) == 345, len(reg)
assert reg_text.splitlines()[2] == "# total: 345", reg_text.splitlines()[2]
assert reg[-1]["claim_id"] == "claim-0345"

cand_rows = [json.loads(l) for l in CAND.read_text(encoding="utf-8").splitlines() if l.strip()]
cand = {r["candidate_id"]: r for r in cand_rows}
assert len(cand) == len(cand_rows)

NEW_IDS = [f"claim-{i:04d}" for i in range(346, 360)]
assert [r["claim_id"] for r in ROWS] == NEW_IDS
assert len(PATCH) == 7
assert len({p["claim_id"] for p in PATCH}) == 7

KEYWORDS = {
    "claim-0346": ["桑、麻、棉的栽植面积", "主要养蚕区"],
    "claim-0347": ["最高水平的代表", "妆花缎"],
    "claim-0348": ["3.1亿匹", "六七千万户"],
    "claim-0349": ["倡从而优伶不从", "保留着前朝的服饰"],
    "claim-0350": ["植物染料为主", "远销国外"],
    "claim-0351": ["补服定型于明代", "洪武二十四年"],
    "claim-0352": ["十从十不从", "大大缓解了", "民怨"],
    "claim-0353": ["黄金时代", "历史上的高峰"],
    "claim-0354": ["1600万件以上", "荷兰东印度公司"],
    "claim-0355": ["两次高峰"],
    "claim-0356": ["研究的总体水平要高于国内", "学术价值"],
    "claim-0357": ["现存最大的古代宫殿建筑群", "皇权至高无上"],
    "claim-0358": ["简洁内敛", "素逸剔透"],
    "claim-0359": ["造船设计业达到了顶峰", "150米", "12帆"],
}

PATCH_KEYWORDS = {
    "claim-0220": ["机房出资、机工出力", "资本主义", "萌芽"],
    "claim-0227": ["既保留了汉族服制中的某些特点", "本民族的习俗礼仪"],
    "claim-0231": ["成为我国瓷器的主流", "600年不衰"],
    "claim-0229": ["最大成就", "高质量白釉"],
    "claim-0234": ["加快设计施工的进度", "不利于建筑设计的多样化发展"],
    "claim-0235": ["世界园林之母", "杰出代表之一"],
    "claim-0236": ["滥用雕镂、镶嵌、彩绘", "实用简练原则"],
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

assert len(used_candidates) == 21, len(used_candidates)
assert len(patched) == 7, len(patched)

chapter = [r for r in cand_rows
           if r["candidate_type"] == "claim"
           and r["candidate_id"].startswith(DOC + ":")
           and r["state"] == "needs_evidence"
           and 4111 <= r["payload"]["source_span"]["line_start"] <= 4712]
print("chapter_candidates", len(chapter))
assert len(chapter) == 21, len(chapter)
assert len(used_candidates) == 21

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
