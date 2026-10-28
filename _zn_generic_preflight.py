# -*- coding: utf-8 -*-
"""Generic claim-batch preflight.

Checks source spans, block membership, keywords, candidate coverage and
baseline state before any write-back.
"""
import json
from collections import Counter
from pathlib import Path

import yaml

ROOT = Path(r"D:/中国设计史研究")
CFG = json.loads((ROOT / "_zn_batch_config.json").read_text(encoding="utf-8"))
DOC = CFG["doc_id"]
SRC = ROOT / CFG["source_file"]
DATE = CFG["date"]
SCOPE = CFG["scope"]
BASE = CFG["baseline"]
EXP = CFG["expected"]
REG = ROOT / "04-knowledge/quality/claim-registry.yml"
CAND = ROOT / "06-runtime/state/candidate-index.jsonl"
SMAP = ROOT / "03-processing" / DOC / "source-map.jsonl"
NEW = json.loads((ROOT / CFG["rows_file"]).read_text(encoding="utf-8"))
PATCH = json.loads((ROOT / CFG["patch_file"]).read_text(encoding="utf-8"))
LO, HI = SCOPE["line_start"], SCOPE["line_end"]

lines = SRC.read_text(encoding="utf-8").splitlines()
blocks = {}
for line in SMAP.read_text(encoding="utf-8").splitlines():
    if not line.strip():
        continue
    b = json.loads(line)
    blocks[b["block_id"]] = b
print("source-map blocks", len(blocks))

reg_text = REG.read_text(encoding="utf-8")
reg = yaml.safe_load(reg_text)
assert len(reg) == BASE["registry_total"], len(reg)
assert reg_text.splitlines()[2] == f"# total: {BASE['registry_total']}"
assert reg[-1]["claim_id"] == BASE["last_claim"]
assert len({r["claim_id"] for r in reg}) == len(reg)
print("registry", len(reg), "last", reg[-1]["claim_id"])

index = [json.loads(l) for l in CAND.read_text(encoding="utf-8").splitlines() if l.strip()]
by_cand = {r["candidate_id"]: r for r in index}
counts = Counter(r["state"] for r in index)
assert counts["applied"] == BASE["applied"], counts
assert counts["needs_evidence"] == BASE["needs"], counts
assert counts["no_delta"] == BASE["no_delta"], counts
assert counts["rejected"] == BASE["rejected"], counts
print("candidate states", dict(counts))

used = []
problems = []
span_text_cache = {}


def span_text(start, end):
    key = (start, end)
    if key not in span_text_cache:
        span_text_cache[key] = " ".join(lines[start - 1:end])
    return span_text_cache[key]


def check_row(row):
    cid = row.get("claim_id", "?")
    cand_id = row["source"]["candidate_id"]
    if cand_id in used:
        problems.append((cid, "duplicate candidate", cand_id))
    used.append(cand_id)
    if not cand_id.startswith(DOC + ":"):
        problems.append((cid, "doc prefix", cand_id))
    c = by_cand.get(cand_id)
    if not c:
        problems.append((cid, "candidate missing", cand_id))
        return
    if c["state"] != "needs_evidence":
        problems.append((cid, "state", c["state"]))
    if c["candidate_type"] != "claim":
        problems.append((cid, "type", c["candidate_type"]))
    span = row["source"]["source_span"]
    s, e = span["line_start"], span["line_end"]
    if not (LO <= s <= e <= HI):
        problems.append((cid, "span out of scope", (s, e, LO, HI)))
    if not (s <= min(span["key_lines"]) and max(span["key_lines"]) <= e):
        problems.append((cid, "key_lines out of span", span["key_lines"]))
    for b in span["block_ids"]:
        if b not in blocks:
            problems.append((cid, "block missing", b))
            continue
        bs = blocks[b].get("line_start") or blocks[b].get("span", {}).get("line_start")
        be = blocks[b].get("line_end") or blocks[b].get("span", {}).get("line_end")
        if bs is None or be is None:
            bs = blocks[b].get("source_span", {}).get("line_start")
            be = blocks[b].get("source_span", {}).get("line_end")
        if bs is not None and not (bs <= e and s <= be):
            problems.append((cid, "block outside span", (b, bs, be, s, e)))
    text = span_text(s, e)
    for kw in CFG.get("keywords", {}).get(cid, []):
        if kw not in text:
            problems.append((cid, "keyword missing", kw))
    if span.get("chapter") != SCOPE.get("chapter") and SCOPE.get("chapter"):
        problems.append((cid, "chapter label", span.get("chapter")))


for row in NEW:
    check_row(row)

patch_used = []
for p in PATCH:
    cid = p["candidate_id"]
    patch_used.append(cid)
    if cid in used:
        problems.append((p["claim_id"], "candidate used twice", cid))
    c = by_cand.get(cid)
    if not c:
        problems.append((p["claim_id"], "patch candidate missing", cid))
        continue
    if c["state"] != "needs_evidence" or c["candidate_type"] != "claim":
        problems.append((p["claim_id"], "patch candidate state", (c["state"], c["candidate_type"])))
    if p["claim_id"] not in {r["claim_id"] for r in reg}:
        problems.append((p["claim_id"], "target claim missing", p["claim_id"]))
    span = p["corroborating_span"]
    s, e = span["line_start"], span["line_end"]
    if not (LO <= s <= e <= HI):
        problems.append((p["claim_id"], "patch span out of scope", (s, e)))
    if not (s <= min(span["key_lines"]) and max(span["key_lines"]) <= e):
        problems.append((p["claim_id"], "patch key_lines out of span", span["key_lines"]))
    for b in span["block_ids"]:
        if b not in blocks:
            problems.append((p["claim_id"], "patch block missing", b))
    text = span_text(s, e)
    for kw in CFG.get("patch_keywords", {}).get(p["claim_id"], []):
        if kw not in text:
            problems.append((p["claim_id"], "patch keyword missing", kw))

# completeness: every needs_evidence claim candidate fully inside scope must be used
inside = [
    r["candidate_id"] for r in index
    if r["candidate_id"].startswith(DOC + ":")
    and r["candidate_type"] == "claim"
    and r["state"] == "needs_evidence"
    and LO <= r["payload"]["source_span"]["line_start"]
    and r["payload"]["source_span"]["line_end"] <= HI
]
all_used = set(used) | set(patch_used)
missing = sorted(set(inside) - all_used)
extra = sorted(all_used - set(inside))
if missing:
    problems.append(("coverage", "unused candidates in scope", missing))
if extra:
    problems.append(("coverage", "used candidates outside scope", extra))
if len(inside) != EXP["candidates"]:
    problems.append(("coverage", "scope candidate count", (len(inside), EXP["candidates"])))

assert len(NEW) == EXP["claims"], (len(NEW), EXP["claims"])
assert len(PATCH) == EXP["patches"], (len(PATCH), EXP["patches"])
assert len({r["claim_id"] for r in NEW}) == len(NEW)

types = Counter(r["claim_type"] for r in NEW)
links = sum(len(r["supported_by"]) for r in NEW)
distinct = len({x for r in NEW for x in r["supported_by"]})
for p in {x for r in NEW for x in r["supported_by"]}:
    if not (ROOT / p).is_file():
        problems.append(("support", "missing KU", p))
if types != Counter(EXP["types"]):
    problems.append(("types", dict(types), EXP["types"]))
if links != EXP["links"]:
    problems.append(("links", links, EXP["links"]))
if distinct != EXP["distinct"]:
    problems.append(("distinct", distinct, EXP["distinct"]))

print(json.dumps({
    "scope": SCOPE,
    "claims": len(NEW),
    "patches": len(PATCH),
    "types": dict(types),
    "links": links,
    "distinct": distinct,
    "scope_claim_candidates": len(inside),
    "used": len(all_used),
    "missing": len(missing),
    "extra": len(extra),
    "problems": problems[:20],
    "problem_count": len(problems),
}, ensure_ascii=False, indent=1))

if problems:
    raise SystemExit(1)
print("PREFLIGHT OK")
