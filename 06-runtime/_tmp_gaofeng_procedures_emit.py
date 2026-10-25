# -*- coding: utf-8 -*-
"""Emit ledger, apply-plan, canonical mapping and manifest for the Gaofeng 2004 procedure batch."""
import hashlib
import json
from pathlib import Path

ROOT = Path(".")
BATCH = Path("06-runtime/automation/2026-10-25-2004gaofeng-procedures-batch")
BATCH.mkdir(parents=True, exist_ok=True)
PREFIX = "2004-gaofeng-zhongguo-shejishi:"
DATE = "2026-10-25"
DOC = "2004-gaofeng-zhongguo-shejishi"

CREATES = [
    {
        "cand": "cand-05-11",
        "slug": "quan-die-fa",
        "title": "圈叠法",
        "sub": "lacquerware_technique",
        "date": "宋代",
        "result": "以 0.2 厘米厚杉木薄长条卷制成胎，胎型轻薄结实、不易变形，宋代实用漆器广泛运用",
    },
    {
        "cand": "cand-sup-58",
        "slug": "la-ran",
        "title": "蜡染",
        "sub": "textile_technique",
        "date": "东汉",
        "result": "尼雅出土东汉蜡染花布，来源据此判断汉代蜡染工艺技术已经成熟",
    },
    {
        "cand": "cand-sup-59",
        "slug": "lan-yinhua-bu",
        "title": "蓝印花布",
        "sub": "textile_technique",
        "date": "汉代",
        "result": "洛甫县出土汉代蓝印花布，来源据此判断汉代蓝印花布工艺技术已经成熟",
    },
    {
        "cand": "cand-sup-75",
        "slug": "duanban-taoyin",
        "title": "短版套印",
        "sub": "printing_technique",
        "date": "明代—清代",
        "result": "明代创造，清代《芥子园画传》采用并发展；清代出现五色、六色套印刻本",
    },
]

UPDATES = [
    {
        "cand": "cand-04-13",
        "entity": "雕版印刷术",
        "target_ref": "04-knowledge/units/procedures/diaoban-yinshua.md",
        "span": "L3102-L3118",
        "before": {
            "sha256": "sha256:0c83f9199ff8db7d732e08909e4b91d36990fc07be0bed18f4c3aa766aae0f0c",
            "bytes": 3836,
            "lines": 82,
        },
        "note": "补入高丰 2004 的发明时间考辨、四步工艺程序、梓木梨木枣木用材、刻工作用与日印 1500—2000 印张的产量。",
    },
]


def fingerprint(path: Path):
    data = path.read_bytes()
    text = data.decode("utf-8").replace("\r\n", "\n")
    payload = text.encode("utf-8")
    return {
        "sha256": "sha256:" + hashlib.sha256(payload).hexdigest(),
        "bytes": len(payload),
        "lines": text.count("\n"),
    }


def norm_text(path: Path) -> str:
    return path.read_bytes().decode("utf-8").replace("\r\n", "\n")


ledger = []
plan = []
mapping = []

for item in CREATES:
    cid = PREFIX + item["cand"]
    target = f"04-knowledge/units/procedures/{item['slug']}.md"
    path = ROOT / target
    if not path.exists():
        raise SystemExit(f"missing {target}")
    fm = norm_text(path).split("---\n", 2)[1]
    title_line = next((ln for ln in fm.splitlines() if ln.startswith("title:")), "")
    if item["title"] not in title_line:
        raise SystemExit(f"title mismatch {target}: {title_line}")
    fp = fingerprint(path)
    for expected, state, reason in [
        ("needs_evidence", "ready_for_review", f"已完成语义复读：既有 KU 无对应实体，提交 create {target}"),
        ("ready_for_review", "approved", f"canonical 候选语义复读完成，批准按 exact change-set 新建 {target}"),
        ("approved", "applied", f"已按 exact change-set 新建 {target}"),
    ]:
        row = {
            "candidate_id": cid,
            "expected_state": expected,
            "state": state,
            "decision": {
                "status": "pending" if state == "ready_for_review" else "approved",
                "reason": reason,
                "decided_by": "Agent",
                "decided_at": DATE,
            },
            "updated_at": DATE,
        }
        if state == "applied":
            row["target_ref"] = target
        ledger.append(row)
    plan.append({
        "action": "create",
        "target_ref": target,
        "candidate_id": cid,
        "entity": item["title"],
        "before": None,
        "after_sha256": fp["sha256"],
        "bytes": fp["bytes"],
        "lines": fp["lines"],
        "note": f"新建{item['sub']}：{item['date']}；{item['result']}",
    })
    mapping.append({
        "entity": item["title"],
        "target_ref": target,
        "action": "create",
        "canonical_candidate": cid,
        "merged_candidates": [],
    })

for up in UPDATES:
    cid = PREFIX + up["cand"]
    target = up["target_ref"]
    path = ROOT / target
    if not path.exists():
        raise SystemExit(f"missing {target}")
    fp = fingerprint(path)
    if fp["sha256"] == up["before"]["sha256"]:
        raise SystemExit(f"unchanged {target}")
    for expected, state, reason in [
        ("needs_evidence", "ready_for_review", f"已完成语义复读：既有 {target} 可承载但缺高丰 2004 记载，提交 update"),
        ("ready_for_review", "approved", f"canonical 候选语义复读完成，批准按 exact change-set 补写 {target}"),
        ("approved", "applied", f"已按 exact change-set 补入高丰 2004 记载：{target}"),
    ]:
        row = {
            "candidate_id": cid,
            "expected_state": expected,
            "state": state,
            "decision": {
                "status": "pending" if state == "ready_for_review" else "approved",
                "reason": reason,
                "decided_by": "Agent",
                "decided_at": DATE,
            },
            "updated_at": DATE,
        }
        if state == "applied":
            row["target_ref"] = target
        ledger.append(row)
    plan.append({
        "action": "update",
        "target_ref": target,
        "candidate_id": cid,
        "entity": up["entity"],
        "before": up["before"],
        "after_sha256": fp["sha256"],
        "bytes": fp["bytes"],
        "lines": fp["lines"],
        "note": up["note"],
    })
    mapping.append({
        "entity": up["entity"],
        "target_ref": target,
        "action": "update",
        "canonical_candidate": cid,
        "merged_candidates": [],
        "note": up["note"],
    })

assert len(ledger) == 15, len(ledger)
assert len(plan) == 5, len(plan)
assert len(mapping) == 5, len(mapping)

(BATCH / "candidate-decision-ledger.jsonl").write_bytes(
    ("\n".join(json.dumps(r, ensure_ascii=False) for r in ledger) + "\n").encode("utf-8")
)
(BATCH / "apply-plan.jsonl").write_bytes(
    ("\n".join(json.dumps(r, ensure_ascii=False) for r in plan) + "\n").encode("utf-8")
)
(BATCH / "canonical-mapping.json").write_bytes(
    (json.dumps(mapping, ensure_ascii=False, indent=2) + "\n").encode("utf-8")
)

manifest = {
    "work_package": "2026-10-25-2004gaofeng-procedures-batch",
    "goal": "处理高丰《中国设计史》2004 册的 5 个 procedure 候选：4 个新建 procedure KU，1 个补入既有雕版印刷 KU；无 no_delta、无 rejected。",
    "status": "applied",
    "date": DATE,
    "inputs": {
        "candidate_index": {
            "path": "06-runtime\\state\\candidate-index.jsonl",
            "rows_before": 5339,
            "sha256_before": "sha256:3a715412cd64619e7787b9e749c77955a1aabf7b1f5da627bc744bcb38262bb0",
            "sha256_scope": "CRLF→LF 归一后",
            "counts_before": {
                "applied": 662,
                "needs_evidence": 3833,
                "no_delta": 43,
                "rejected": 801,
            },
        },
        "source": {
            "doc_id": DOC,
            "file": "03基础书籍-md文档/中国设计史_高丰_2004_广西美术出版社.md",
            "spans": ["L3102-L3118", "L3692-L3697", "L2181", "L2181", "L5174"],
        },
    },
    "method": {
        "rules": [
            "既有同题 KU 可承载但缺高丰 2004 记载的判 update；无对应实体的判 create。",
            "工序条目只写来源所记材料、步骤、工具、产量与实例；来源未载的工序参数写入证据边界。",
            "来源的判断与推测照录并标明主语，不提升为定论。",
            "同一来源行同时记两种工艺的，分建两条并在相关知识元互指，不合并为一条。",
        ],
        "source_policy": "02-sources 只读；本批写 04-knowledge/units/procedures，并对既有 procedure KU 补入高丰来源。",
    },
    "outputs": {
        "apply_plan": {
            "path": "06-runtime\\automation\\2026-10-25-2004gaofeng-procedures-batch\\apply-plan.jsonl",
            "rows": 5,
            "create": 4,
            "update": 1,
        },
        "ledger": {
            "path": "06-runtime\\automation\\2026-10-25-2004gaofeng-procedures-batch\\candidate-decision-ledger.jsonl",
            "rows": 15,
            "candidates": 5,
            "applied": 5,
            "no_delta": 0,
            "rejected": 0,
        },
        "canonical_mapping": {
            "path": "06-runtime\\automation\\2026-10-25-2004gaofeng-procedures-batch\\canonical-mapping.json",
            "entries": 5,
        },
    },
    "verification": {"status": "pending"},
}

(BATCH / "manifest.json").write_bytes(
    (json.dumps(manifest, ensure_ascii=False, indent=2) + "\n").encode("utf-8")
)
print("ledger", len(ledger), "plan", len(plan), "mapping", len(mapping))
