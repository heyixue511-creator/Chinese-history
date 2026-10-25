# -*- coding: utf-8 -*-
"""Emit ledger, apply-plan, canonical mapping and manifest for the Zhaonong event batch."""
import hashlib
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from _tmp_zhaonong_events_a import ITEMS_A
from _tmp_zhaonong_events_b import ITEMS_B
from _tmp_zhaonong_events_c import ITEMS_C

ROOT = Path(".")
BATCH = Path("06-runtime/automation/2026-10-25-2009zhaonong-events-batch")
BATCH.mkdir(parents=True, exist_ok=True)
PREFIX = "2009-zhaonong-zhongguo-yishu-shejishi:"
DATE = "2026-10-25"
ITEMS = ITEMS_A + ITEMS_B + ITEMS_C

NO_DELTA = [
    {
        "cand": "cand-08-210",
        "entity": "靖康之变",
        "target_ref": "04-knowledge/units/events/jingkang-zhibian.md",
        "note": "既有 event KU 已记 1126—1127 年靖康之变、徽钦二帝北迁与北宋灭亡",
    },
    {
        "cand": "cand-11-155",
        "entity": "剪辫子",
        "target_ref": "04-knowledge/units/events/jianbian-yifu-1912.md",
        "note": "既有 event KU 已记 1912 年《剪辫通令》《服制条例》与中山装定礼服",
    },
    {
        "cand": "cand-12-96",
        "entity": "1998年高等教育专业学科目录调整",
        "target_ref": "04-knowledge/units/events/1998-moe-major-catalog.md",
        "note": "既有 event KU 已记 1998 年 7 月教育部本科专业目录调整与“艺术设计专业”设置",
    },
]


def fingerprint(path: Path):
    raw = path.read_bytes()
    text = raw.replace(b"\r\n", b"\n")
    return {
        "after_sha256": "sha256:" + hashlib.sha256(text).hexdigest(),
        "bytes": len(raw),
        "lines": text.decode("utf-8").count("\n"),
    }


ledger = []
plan = []
mapping = []

for item in ITEMS:
    cid = PREFIX + item["cand"]
    target = f"04-knowledge/units/events/{item['slug']}.md"
    path = ROOT / target
    if not path.exists():
        raise SystemExit(f"missing {target}")
    fp = fingerprint(path)
    ledger.append({
        "candidate_id": cid,
        "expected_state": "needs_evidence",
        "state": "ready_for_review",
        "decision": {
            "status": "pending",
            "reason": f"已完成语义复读：既有 KU 无对应实体，提交 create {target}",
            "decided_by": "Agent",
            "decided_at": DATE,
        },
        "updated_at": DATE,
    })
    ledger.append({
        "candidate_id": cid,
        "expected_state": "ready_for_review",
        "state": "approved",
        "decision": {
            "status": "approved",
            "reason": f"canonical 候选语义复读完成，批准按 exact change-set 新建 {target}",
            "decided_by": "Agent",
            "decided_at": DATE,
        },
        "updated_at": DATE,
    })
    ledger.append({
        "candidate_id": cid,
        "expected_state": "approved",
        "state": "applied",
        "decision": {
            "status": "approved",
            "reason": f"已按 exact change-set 新建 {target}",
            "decided_by": "Agent",
            "decided_at": DATE,
        },
        "updated_at": DATE,
        "target_ref": target,
    })
    plan.append({
        "action": "create",
        "target_ref": target,
        "candidate_id": cid,
        "entity": item["title"],
        "before": None,
        "after_sha256": fp["after_sha256"],
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

for nd in NO_DELTA:
    cid = PREFIX + nd["cand"]
    ledger.append({
        "candidate_id": cid,
        "expected_state": "needs_evidence",
        "state": "ready_for_review",
        "decision": {
            "status": "pending",
            "reason": f"已完成语义复读：既有 {nd['target_ref']} 可完整承载，提交 no_delta",
            "decided_by": "Agent",
            "decided_at": DATE,
        },
        "updated_at": DATE,
    })
    ledger.append({
        "candidate_id": cid,
        "expected_state": "ready_for_review",
        "state": "approved",
        "decision": {
            "status": "approved",
            "reason": f"canonical 候选语义复读完成，批准判 no_delta（{nd['target_ref']}）",
            "decided_by": "Agent",
            "decided_at": DATE,
        },
        "updated_at": DATE,
    })
    ledger.append({
        "candidate_id": cid,
        "expected_state": "approved",
        "state": "no_delta",
        "decision": {
            "status": "approved",
            "reason": f"既有 {nd['target_ref']} 已完整覆盖候选内容，无需写回；判定 no_delta",
            "decided_by": "Agent",
            "decided_at": DATE,
        },
        "updated_at": DATE,
        "target_ref": nd["target_ref"],
    })
    mapping.append({
        "entity": nd["entity"],
        "target_ref": nd["target_ref"],
        "action": "no_delta",
        "canonical_candidate": cid,
        "merged_candidates": [],
        "note": nd["note"],
    })

assert len(ledger) == 69, len(ledger)
assert len(plan) == 20, len(plan)
assert len(mapping) == 23, len(mapping)

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
    "work_package": "2026-10-25-2009zhaonong-events-batch",
    "goal": "处理赵农《中国艺术设计史》2009 册的 23 个 event 候选：20 个新建 event KU，3 个由既有 KU 覆盖判 no_delta。",
    "status": "applied",
    "date": DATE,
    "inputs": {
        "candidate_index": {
            "path": "06-runtime\\state\\candidate-index.jsonl",
            "rows_before": 5339,
            "sha256_before": "sha256:83ce7412c8090ffc659c9816c44e16c671dbcb4c037a663fa57ffd9ef519c280",
            "sha256_scope": "CRLF→LF 归一后",
            "counts_before": {
                "applied": 603,
                "needs_evidence": 3899,
                "no_delta": 36,
                "rejected": 801,
            },
        },
        "source": {
            "doc_id": "2009-zhaonong-zhongguo-yishu-shejishi",
            "file": "03基础书籍-md文档/中国艺术设计史_赵农_2009_高等教育出版社.md",
            "spans": [i["span"] for i in ITEMS] + ["L5405-L5430", "L8006-L8055", "L8359-L8409"],
        },
    },
    "method": {
        "rules": [
            "事件已有同题专条且内容完整覆盖时判 no_delta；仅被更大事件条顺带提及者仍建专条。",
            "事件条目只写来源所记时间、地点、参与者、过程与结果；来源未载的年份、人物、数据与过程写入证据边界。",
            "传说事件与来源作“传说”者照录传说属性，不据外部考订改写为史实。",
            "来源两处记载并见者并列保留，不代为拼合成单一事实。",
        ],
        "source_policy": "02-sources 只读；本批只写 04-knowledge/units/events。",
    },
    "outputs": {
        "apply_plan": {
            "path": "06-runtime\\automation\\2026-10-25-2009zhaonong-events-batch\\apply-plan.jsonl",
            "rows": 20,
            "create": 20,
            "update": 0,
        },
        "ledger": {
            "path": "06-runtime\\automation\\2026-10-25-2009zhaonong-events-batch\\candidate-decision-ledger.jsonl",
            "rows": 69,
            "candidates": 23,
            "applied": 20,
            "no_delta": 3,
            "rejected": 0,
        },
        "canonical_mapping": {
            "path": "06-runtime\\automation\\2026-10-25-2009zhaonong-events-batch\\canonical-mapping.json",
            "entries": 23,
        },
    },
    "verification": {"status": "pending"},
}

(BATCH / "manifest.json").write_bytes(
    (json.dumps(manifest, ensure_ascii=False, indent=2) + "\n").encode("utf-8")
)
print("ledger", len(ledger), "plan", len(plan), "mapping", len(mapping))
