import hashlib
import json
import pathlib
import re
import subprocess
import sys

import yaml

ROOT = pathlib.Path(__file__).resolve().parents[1]
PKG = ROOT / "06-runtime" / "automation" / "2026-10-25-2011lilixin-institutions-batch-x"
DOC = "2011-lilixin-zhongguo-sheji-yishu-shilun"
DATE = "2026-10-25"
TARGETS = [
    "04-knowledge/units/institutions/guowuyuan-xuewei-weiyuanhui.md",
    "04-knowledge/units/institutions/zhongyang-lishi-yuyan-yanjiusuo.md",
    "04-knowledge/units/institutions/southeast-university.md",
    "04-knowledge/units/institutions/swedish-museum-of-far-eastern-antiquities.md",
    "04-knowledge/units/institutions/shosoin.md",
    "04-knowledge/units/institutions/song-dai-huayuan.md",
    "04-knowledge/units/institutions/qingjiang-chuanchang.md",
    "04-knowledge/units/institutions/chengyi-gongsuo.md",
    "04-knowledge/units/institutions/jiangnan-zhizao-zongju.md",
    "04-knowledge/units/institutions/china-commercial-art-writers-association.md",
    "04-knowledge/units/institutions/neiwufu-zaobanchu.md",
]
EXPECTED = {
    TARGETS[0]: {"action": "create", "sources": 3, "version": 1},
    TARGETS[1]: {"action": "create", "sources": 1, "version": 1},
    TARGETS[2]: {"action": "create", "sources": 3, "version": 1},
    TARGETS[3]: {"action": "create", "sources": 1, "version": 1},
    TARGETS[4]: {"action": "create", "sources": 4, "version": 1},
    TARGETS[5]: {"action": "create", "sources": 1, "version": 1},
    TARGETS[6]: {"action": "create", "sources": 3, "version": 1},
    TARGETS[7]: {"action": "create", "sources": 1, "version": 1},
    TARGETS[8]: {"action": "update", "sources": 4, "version": 3},
    TARGETS[9]: {"action": "create", "sources": 1, "version": 1},
    TARGETS[10]: {"action": "update", "sources": 5, "version": 4},
}
SECTIONS = ["## 描述", "## 核心内容", "## 在层级体系中的位置", "## 相关知识元", "## 验证状态", "## 参考文献"]
TITLE_RE = re.compile(r'[一-鿿].*[（(][^（）)]*[A-Za-zÀ-ÿ][^（）)]*[）)]')


def fp(path: pathlib.Path) -> dict:
    text = path.read_bytes().decode("utf-8").replace("\r\n", "\n").replace("\r", "\n")
    data = text.encode("utf-8")
    return {
        "sha256": "sha256:" + hashlib.sha256(data).hexdigest(),
        "bytes": len(data),
        "lines": text.count("\n"),
    }


def load(path: pathlib.Path):
    return json.loads(path.read_text(encoding="utf-8"))


def parse_md(path: pathlib.Path):
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise AssertionError(f"{path}: missing frontmatter")
    end = text.find("\n---\n", 4)
    if end < 0:
        raise AssertionError(f"{path}: unterminated frontmatter")
    front = yaml.safe_load(text[4:end])
    body = text[end + 5:]
    return text, front, body


errors = []
warnings = []


def check(cond, message):
    if not cond:
        errors.append(message)


# --- ledger ---
ledger_path = PKG / "candidate-decision-ledger.jsonl"
ledger = [json.loads(line) for line in ledger_path.read_text(encoding="utf-8").splitlines() if line.strip()]
check(len(ledger) == 33, f"ledger rows {len(ledger)} != 33")
by_candidate = {}
for row in ledger:
    by_candidate.setdefault(row["candidate_id"], []).append(row)
check(len(by_candidate) == 11, f"ledger candidates {len(by_candidate)} != 11")
for cid, rows in by_candidate.items():
    check([r.get("state") for r in rows] == ["ready_for_review", "approved", "applied"], f"{cid}: state sequence {[r.get('state') for r in rows]}")
    check([r.get("expected_state") for r in rows] == ["needs_evidence", "ready_for_review", "approved"], f"{cid}: expected sequence")
    check(rows[-1].get("target_ref") in TARGETS, f"{cid}: target_ref {rows[-1].get('target_ref')!r}")
    for row in rows:
        check(row.get("updated_at") == DATE, f"{cid}: updated_at")
        check(row.get("decision", {}).get("decided_at") == DATE, f"{cid}: decided_at")
        check(row.get("decision", {}).get("decided_by") == "Agent", f"{cid}: decided_by")
    check(rows[1]["decision"].get("status") == "approved", f"{cid}: row2 status")
    check(rows[2]["decision"].get("status") == "approved", f"{cid}: row3 status")

# --- plan ---
plan_path = PKG / "apply-plan.jsonl"
plan = [json.loads(line) for line in plan_path.read_text(encoding="utf-8").splitlines() if line.strip()]
check(len(plan) == 11, f"plan rows {len(plan)} != 11")
check({r["target_ref"] for r in plan} == set(TARGETS), "plan targets mismatch")
check(sum(1 for r in plan if r["action"] == "create") == 9, "plan create != 9")
check(sum(1 for r in plan if r["action"] == "update") == 2, "plan update != 2")
plan_by_ref = {r["target_ref"]: r for r in plan}
for ref, expected in EXPECTED.items():
    row = plan_by_ref.get(ref)
    check(row is not None, f"plan missing {ref}")
    if row is None:
        continue
    check(row["action"] == expected["action"], f"{ref}: action {row['action']}")
    check(row.get("candidate_id", "").startswith(DOC + ":"), f"{ref}: candidate_id prefix")
    actual = fp(ROOT / ref)
    check(row["after_sha256"] == actual["sha256"], f"{ref}: after_sha256 plan={row['after_sha256']} disk={actual['sha256']}")
    for key in ("bytes", "lines"):
        check(row[key] == actual[key], f"{ref}: {key} plan={row[key]} disk={actual[key]}")
    if expected["action"] == "update":
        check(isinstance(row.get("before"), dict), f"{ref}: update before missing")
    else:
        check(row.get("before") is None, f"{ref}: create before not null")
    check(row.get("entity"), f"{ref}: entity empty")
    check(len(row.get("note", "")) >= 40, f"{ref}: note too short")

# --- mapping ---
mapping = load(PKG / "canonical-mapping.json")
check(len(mapping) == 11, f"mapping entries {len(mapping)} != 11")
check({m["target_ref"] for m in mapping} == set(TARGETS), "mapping targets mismatch")
map_by_ref = {m["target_ref"]: m for m in mapping}
for row in plan:
    m = map_by_ref.get(row["target_ref"])
    check(m is not None, f"mapping missing {row['target_ref']}")
    if m:
        check(m["canonical_candidate"] == row["candidate_id"], f"{row['target_ref']}: canonical mismatch")
        check(m["entity"] == row["entity"], f"{row['target_ref']}: entity mismatch")
        check(m["action"] == row["action"], f"{row['target_ref']}: action mismatch")
southeast = map_by_ref.get(TARGETS[2])
check(southeast is not None and southeast["merged_candidates"] == [f"{DOC}:cand-06-03"], "southeast merged_candidates")
for m in mapping:
    if m["target_ref"] != TARGETS[2]:
        check(m["merged_candidates"] == [], f"{m['target_ref']}: unexpected merged_candidates")

# --- markdown ---
for ref, expected in EXPECTED.items():
    text, front, body = parse_md(ROOT / ref)
    check(front.get("type") == "institution", f"{ref}: type {front.get('type')}")
    check(front.get("sub_type") in {"government_office", "commercial_enterprise", "publishing_house", "design_school", "research_institute", "craft_workshop", "professional_society", "museum", "design_firm", "film_studio", "academy"}, f"{ref}: sub_type {front.get('sub_type')}")
    check(front.get("source_count") == expected["sources"], f"{ref}: source_count {front.get('source_count')} != {expected['sources']}")
    check(len(front.get("sources") or []) == expected["sources"], f"{ref}: sources len != source_count")
    check(front.get("version") == expected["version"], f"{ref}: version {front.get('version')} != {expected['version']}")
    check(str(front.get("created")) == DATE and str(front.get("updated")) == DATE, f"{ref}: dates")
    check(front.get("evidence_status") == "source_backed", f"{ref}: evidence_status")
    check(front.get("confidence") in {"low", "medium", "high"}, f"{ref}: confidence")
    check(front.get("consensus") == "tentative", f"{ref}: consensus")
    check(TITLE_RE.search(front.get("title", "")), f"{ref}: title not bilingual: {front.get('title')!r}")
    for source in front.get("sources") or []:
        er = source.get("evidence_ref") or {}
        check(er.get("doc_id") in {
            "2004-gaofeng-zhongguo-shejishi",
            "2009-xiayanjing-zhongguo-shejishi",
            "2009-zhaonong-zhongguo-yishu-shejishi",
            "2010-tianzibing-zhongguo-gongyi-meishushi",
            "2011-lilixin-zhongguo-sheji-yishu-shilun",
            "2016-xiayanjing-zhongguo-yishu-shejishi-upgrade",
        }, f"{ref}: unknown doc_id {er.get('doc_id')!r}")
        check(er.get("source_file", "").startswith("03基础书籍-md文档/"), f"{ref}: source_file")
    positions = [body.find(s) for s in SECTIONS]
    check(all(p >= 0 for p in positions), f"{ref}: missing section {[s for s, p in zip(SECTIONS, positions) if p < 0]}")
    check(positions == sorted(positions), f"{ref}: sections out of order")
    check("## " not in body[:0], "noop")
    # no extra H2 sections
    h2 = [line.strip() for line in body.splitlines() if line.startswith("## ")]
    check(h2 == SECTIONS, f"{ref}: H2 sections {h2}")

# --- rebuild index ---
proc = subprocess.run(
    [sys.executable, "scripts/build_discovery_index.py"],
    cwd=ROOT,
    capture_output=True,
    text=True,
    encoding="utf-8",
)
check(proc.returncode == 0, f"build_discovery_index failed: {proc.stderr[-1000:]}")
index_path = ROOT / "06-runtime" / "state" / "candidate-index.jsonl"
index = [json.loads(line) for line in index_path.read_text(encoding="utf-8").splitlines() if line.strip()]
check(len(index) == 5339, f"candidate index rows {len(index)} != 5339")
counts = {}
for row in index:
    counts[row["state"]] = counts.get(row["state"], 0) + 1
expected_counts = {"applied": 930, "needs_evidence": 3540, "no_delta": 57, "rejected": 812}
check(counts == expected_counts, f"candidate counts {counts} != {expected_counts}")
index_by_id = {row["candidate_id"]: row for row in index}
check(len(index_by_id) == len(index), "duplicate candidate_id in index")
for cid in by_candidate:
    row = index_by_id.get(cid)
    check(row is not None, f"index missing {cid}")
    if row:
        check(row["state"] == "applied", f"{cid}: index state {row['state']}")
        check(row.get("target_ref") == by_candidate[cid][-1]["target_ref"], f"{cid}: index target_ref")
        check(row.get("decision", {}).get("status") == "approved", f"{cid}: index decision")

index_fp = fp(index_path)

result = {
    "ok": not errors,
    "errors": errors,
    "warnings": warnings,
    "ledger_rows": len(ledger),
    "plan_rows": len(plan),
    "mapping_entries": len(mapping),
    "index_rows": len(index),
    "index_sha256": index_fp["sha256"],
    "index_bytes": index_fp["bytes"],
    "index_lines": index_fp["lines"],
    "counts": counts,
    "targets": len(TARGETS),
}
print(json.dumps(result, ensure_ascii=False, indent=2))
raise SystemExit(0 if not errors else 1)
