# -*- coding: utf-8 -*-
"""Preflight CL4a: validate 11 claim rows, 18 patches, spans, blocks, keywords."""
import json
from pathlib import Path

import yaml

ROOT = Path(r"D:/中国设计史研究")
DOC = "2016-xiayanjing-zhongguo-yishu-shejishi-upgrade"
SRC = ROOT / "03基础书籍-md文档/中国艺术设计史（升级版）_夏燕靖_2016_上海人民美术出版社.md"
REG = ROOT / "04-knowledge/quality/claim-registry.yml"
CAND = ROOT / "06-runtime/state/candidate-index.jsonl"
ROWS = json.loads((ROOT / "_zn_cl7_rows.json").read_text(encoding="utf-8"))
PATCH = json.loads((ROOT / "_zn_cl7_patch.json").read_text(encoding="utf-8"))

lines = SRC.read_text(encoding="utf-8").splitlines()
reg_text = REG.read_text(encoding="utf-8")
reg = yaml.safe_load(reg_text)
assert len(reg) == 321, len(reg)
assert reg_text.splitlines()[2] == "# total: 321", reg_text.splitlines()[2]
assert reg[-1]["claim_id"] == "claim-0321"

cand_rows = [json.loads(l) for l in CAND.read_text(encoding="utf-8").splitlines() if l.strip()]
cand = {r["candidate_id"]: r for r in cand_rows}
assert len(cand) == len(cand_rows)

NEW_IDS = [f"claim-{i:04d}" for i in range(322, 333)]
assert [r["claim_id"] for r in ROWS] == NEW_IDS
assert len(PATCH) == 18
assert len({p["claim_id"] for p in PATCH}) == 16

KEYWORDS = {
    "claim-0322": ["300多年", "三省六部制", "科举制", "大运河"],
    "claim-0323": ["三大特点", "丰富多彩", "兼容并蓄", "承前启后"],
    "claim-0324": ["纳资代役", "手工业行会", "改进的动力"],
    "claim-0325": ["关键时期", "经验体系", "中外文化科技交流"],
    "claim-0326": ["第一个高峰", "青瓷则是其主流"],
    "claim-0327": ["厚葬之风", "冥器", "唐三彩", "主要原因"],
    "claim-0328": ["介质印花", "一大进步"],
    "claim-0329": ["70:25:5", "微向外凸", "梦溪笔谈"],
    "claim-0330": ["敞肩拱", "赵州桥", "最高水平"],
    "claim-0331": ["9个月", "世界都市建设史上的一大奇迹"],
    "claim-0332": ["南禅寺大殿", "佛光寺大殿", "两座木结构殿堂"],
}

PATCH_KEYWORDS = {
    "claim-0132": ["鼎盛时期", "全面繁荣"],
    "claim-0134": ["居于主导地位", "工艺水平"],
    "claim-0139": ["陶至唐而盛", "始有窑名"],
    "claim-0140": ["专供宫廷", "官府督造", "御器厂"],
    "claim-0141": ["法门寺", "16件", "支钉撑烧法"],
    "claim-0145": ["江南丝织业", "蜀桑万亩", "吴蚕万机"],
    "claim-0146": ["纬锦为主", "很高的水平"],
    "claim-0147": ["陵阳公样", "中西文化交流"],
    "claim-0150": ["贞观四年", "紫色", "绯色"],
    "claim-0153": ["中唐进入全盛", "波斯萨珊", "西方"],
    "claim-0154": ["伊斯兰文化自唐代", "青花", "钴"],
    "claim-0155": ["景泰蓝的滥觞", "珐琅"],
    "claim-0156": ["扬州施桥镇", "水密舱"],
    "claim-0163": ["梓人传", "规矩绳墨", "善运众工"],
    "claim-0164": ["三大瓷窑体系", "宋代的名窑名瓷"],
    "claim-0165": ["初唐的清秀", "盛唐的华丽", "拘谨、秀气、柔弱"],
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

assert len(used_candidates) == 29, len(used_candidates)
assert len(patched) == 16, len(patched)

chapter = [r for r in cand_rows
           if r["candidate_type"] == "claim"
           and r["candidate_id"].startswith(DOC + ":")
           and r["state"] == "needs_evidence"
           and 2461 <= r["payload"]["source_span"]["line_start"] <= 3055]
print("chapter_candidates", len(chapter))
assert len(chapter) == 29, len(chapter)
assert len(used_candidates) == 29

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
