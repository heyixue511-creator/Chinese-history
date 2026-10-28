# -*- coding: utf-8 -*-
"""Preflight CL9a: validate 15 claim rows, 7 patches, spans, blocks, keywords."""
import json
from pathlib import Path

import yaml

ROOT = Path(r"D:/中国设计史研究")
DOC = "2016-xiayanjing-zhongguo-yishu-shejishi-upgrade"
SRC = ROOT / "03基础书籍-md文档/中国艺术设计史（升级版）_夏燕靖_2016_上海人民美术出版社.md"
REG = ROOT / "04-knowledge/quality/claim-registry.yml"
CAND = ROOT / "06-runtime/state/candidate-index.jsonl"
ROWS = json.loads((ROOT / "_zn_cl12_rows.json").read_text(encoding="utf-8"))
PATCH = json.loads((ROOT / "_zn_cl12_patch.json").read_text(encoding="utf-8"))

lines = SRC.read_text(encoding="utf-8").splitlines()
reg_text = REG.read_text(encoding="utf-8")
reg = yaml.safe_load(reg_text)
assert len(reg) == 363, len(reg)
assert reg_text.splitlines()[2] == "# total: 363", reg_text.splitlines()[2]
assert reg[-1]["claim_id"] == "claim-0363"

cand_rows = [json.loads(l) for l in CAND.read_text(encoding="utf-8").splitlines() if l.strip()]
cand = {r["candidate_id"]: r for r in cand_rows}
assert len(cand) == len(cand_rows)

NEW_IDS = [f"claim-{i:04d}" for i in range(364, 379)]
assert [r["claim_id"] for r in ROWS] == NEW_IDS
assert len(PATCH) == 7
assert len({p["claim_id"] for p in PATCH}) == 7

KEYWORDS = {
    "claim-0364": ["1954年6月", "云锦研究工作组", "最早的工艺美术研究机构"],
    "claim-0365": ["巩固民间美术工艺的成就", "热爱生活", "高度的创造性"],
    "claim-0366": ["产业价值", "就业价值", "市场价值", "文化价值"],
    "claim-0367": ["中央工艺美术学院的成立", "综合性高等工艺美术教育"],
    "claim-0368": ["装饰用得恰当", "功能和结构"],
    "claim-0369": ["3年建厂目标", "不能批量设计和制造汽车"],
    "claim-0370": ["两次发掘", "始烧于唐", "初步定论"],
    "claim-0371": ["1970年", "半数以上", "47%"],
    "claim-0372": ["2005年", "3343户", "1430亿元"],
    "claim-0373": ["非物质文化遗产", "文化场所"],
    "claim-0374": ["20世纪80年代初", "开始起步"],
    "claim-0375": ["3R", "Reduce", "Recycle", "Reuse"],
    "claim-0376": ["自主设计研发", "完全的知识产权"],
    "claim-0377": ["优化教育结构", "课程结构", "地区结构"],
    "claim-0378": ["1957-1965年", "第一个繁荣时期", "中国动画学派"],
}

PATCH_KEYWORDS = {
    "claim-0247": ["两大历史阶段"],
    "claim-0248": ["三种办学思路", "反右运动"],
    "claim-0249": ["首次聘请", "包给各省市人民政府"],
    "claim-0250": ["23.4亿元", "118"],
    "claim-0251": ["红、光、亮", "空洞、单调、贫乏"],
    "claim-0252": ["完整的产业体系", "特殊经济地位"],
    "claim-0253": ["核心因素", "科技创新与设计研发"],
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

assert len(used_candidates) == 22, len(used_candidates)
assert len(patched) == 7, len(patched)

chapter = [r for r in cand_rows
           if r["candidate_type"] == "claim"
           and r["candidate_id"].startswith(DOC + ":")
           and r["state"] == "needs_evidence"
           and 5124 <= r["payload"]["source_span"]["line_start"] <= 5544]
print("chapter_candidates", len(chapter))
assert len(chapter) == 22, len(chapter)
assert used_candidates == {r["candidate_id"] for r in chapter}

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
