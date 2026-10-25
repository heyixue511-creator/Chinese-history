# -*- coding: utf-8 -*-
"""Emit decision ledger, apply-plan, mapping and manifest for the discovery-events batch."""
import hashlib
import json
from pathlib import Path

WP = Path("06-runtime/automation/2026-10-25-discovery-events-batch")
WP.mkdir(parents=True, exist_ok=True)
DATE = "2026-10-25"

CREATES = [
    {
        "candidate_id": "2010-tianzibing-zhongguo-gongyi-meishushi:cand-02-46",
        "target_ref": "04-knowledge/units/events/xianrendong-taoci-chutu.md",
        "entity": "仙人洞陶器出土",
        "note": "新建陶器起源事件：1962 年江西万年仙人洞、距今 8000 多年、来源称最早陶器资料",
    },
    {
        "candidate_id": "2010-tianzibing-zhongguo-gongyi-meishushi:cand-02-48",
        "target_ref": "04-knowledge/units/events/donghulin-muzang.md",
        "entity": "东胡林墓葬发现",
        "note": "新建原始装饰事件：1966 年北京门头沟、螺壳项链与牛肋骨骨镯、装饰的萌芽",
    },
    {
        "candidate_id": "2010-tianzibing-zhongguo-gongyi-meishushi:cand-02-49",
        "target_ref": "04-knowledge/units/events/xixiacun-canjian.md",
        "entity": "西阴村蚕茧发现",
        "note": "新建养蚕起源事件：1926 年山西夏县半个蚕茧，并与钱山漾丝织物、柴达木毛布同段并置",
    },
    {
        "candidate_id": "2010-tianzibing-zhongguo-gongyi-meishushi:cand-05-55",
        "target_ref": "04-knowledge/units/events/zenghouyi-mu-fajue.md",
        "entity": "曾侯乙墓发掘",
        "note": "新建失蜡法事件：1977 年随县铜尊铜盘，与 1979 年淅川下寺铜禁铜盏构成年代序列",
    },
    {
        "candidate_id": "2010-tianzibing-zhongguo-gongyi-meishushi:cand-05-54",
        "target_ref": "04-knowledge/units/events/mashan-yihao-mu-sichupin.md",
        "entity": "马山一号墓丝织品出土",
        "note": "新建战国染织事件：1982 年江陵马山一号墓，品种、织锦、舞人动物纹锦与刺绣",
    },
    {
        "candidate_id": "2010-tianzibing-zhongguo-gongyi-meishushi:cand-06-50",
        "target_ref": "04-knowledge/units/events/mawangdui-yihao-mu-fajue.md",
        "entity": "马王堆一号汉墓发掘",
        "note": "新建汉代丝织事件：1972 年长沙马王堆，46 段/58 件、经锦与绒圈锦结构",
    },
]

NO_DELTA = [
    {
        "candidate_id": "2010-tianzibing-zhongguo-gongyi-meishushi:cand-02-47",
        "target_ref": "04-knowledge/units/works/wudaowen-caitao-pen.md",
        "entity": "舞蹈纹彩陶盆",
        "note": "既有 KU 已完整记录 1973 年秋青海大通上孙家寨出土、尺寸与纹样，事件无可独立增量",
    },
]


def fingerprint(path):
    data = path.read_bytes()
    text = data.decode("utf-8").replace("\r\n", "\n")
    payload = text.encode("utf-8")
    return {
        "sha256": "sha256:" + hashlib.sha256(payload).hexdigest(),
        "bytes": len(payload),
        "lines": text.count("\n"),
    }


def rows(cid, target, action):
    if action == "create":
        r1 = f"已完成语义复读：既有 KU 无对应实体，提交 create {target}"
        r2 = f"canonical 候选语义复读完成，批准按 exact change-set 新建 {target}"
        r3 = f"已按 exact change-set 新建 {target}"
        final = "applied"
    else:
        r1 = f"已完成语义复读：既有 {target} 已覆盖候选实质内容，提交 no_delta 判定"
        r2 = "语义复读确认无实质增量，批准 no_delta"
        r3 = f"既有 {target} 已完整覆盖候选内容，无需写回；判定 no_delta"
        final = "no_delta"
    return [
        {"candidate_id": cid, "expected_state": "needs_evidence", "state": "ready_for_review",
         "decision": {"status": "pending", "reason": r1, "decided_by": "Agent", "decided_at": DATE},
         "updated_at": DATE},
        {"candidate_id": cid, "expected_state": "ready_for_review", "state": "approved",
         "decision": {"status": "approved", "reason": r2, "decided_by": "Agent", "decided_at": DATE},
         "updated_at": DATE},
        {"candidate_id": cid, "expected_state": "approved", "state": final,
         "decision": {"status": "approved", "reason": r3, "decided_by": "Agent", "decided_at": DATE},
         "updated_at": DATE, "target_ref": target},
    ]


ledger, plan, mapping = [], [], []
for item in CREATES:
    for cid in [item["candidate_id"]]:
        ledger.extend(rows(cid, item["target_ref"], "create"))
    now = fingerprint(Path(item["target_ref"]))
    plan.append({"action": "create", "target_ref": item["target_ref"], "candidate_id": item["candidate_id"],
                 "entity": item["entity"], "before": None, "after_sha256": now["sha256"],
                 "bytes": now["bytes"], "lines": now["lines"], "note": item["note"]})
    mapping.append({"entity": item["entity"], "target_ref": item["target_ref"], "action": "create",
                    "canonical_candidate": item["candidate_id"], "merged_candidates": []})

for item in NO_DELTA:
    ledger.extend(rows(item["candidate_id"], item["target_ref"], "no_delta"))
    mapping.append({"entity": item["entity"], "target_ref": item["target_ref"], "action": "no_delta",
                    "canonical_candidate": item["candidate_id"], "merged_candidates": []})

with (WP / "candidate-decision-ledger.jsonl").open("w", encoding="utf-8", newline="") as fh:
    for row in ledger:
        fh.write(json.dumps(row, ensure_ascii=False) + "\n")
with (WP / "apply-plan.jsonl").open("w", encoding="utf-8", newline="") as fh:
    for row in plan:
        fh.write(json.dumps(row, ensure_ascii=False) + "\n")
(WP / "canonical-mapping.json").write_text(json.dumps(mapping, ensure_ascii=False, indent=2), encoding="utf-8")

manifest = {
    "work_package": "2026-10-25-discovery-events-batch",
    "goal": "处理田自秉《中国工艺美术史》中的 7 个考古发现事件候选：6 个新建 event KU，1 个由既有 work KU 覆盖判 no_delta。",
    "status": "applied",
    "date": DATE,
    "inputs": {
        "candidate_index": {
            "path": "06-runtime/state/candidate-index.jsonl",
            "rows_before": 5339,
            "sha256_before": "sha256:7ee850800bf8b2fc21a3a25d54c412be72b41e27ceb515ab8f72311dc5197e6b",
            "needs_evidence_before": 3970,
        },
        "source": {
            "doc_id": "2010-tianzibing-zhongguo-gongyi-meishushi",
            "file": "03基础书籍-md文档/中国工艺美术史（修订本）_田自秉_2010_东方出版中心.md",
            "spans": ["L443", "L484", "L583", "L829", "L1814", "L1962", "L1972", "L2466", "L2470"],
        },
    },
    "method": {
        "rules": [
            "发现事件若无既有 KU，且来源给出时间、地点、出土物与工艺意义，建 event KU。",
            "发现事件若已被既有 work KU 完整记录（时间、地点、尺寸、纹样），判 no_delta，不重复建条。",
            "事件条目只写来源所记事实；未给器形、尺寸、发掘者时明确写入证据边界。",
        ],
        "source_policy": "02-sources 只读；本批只写 04-knowledge/units/events。",
    },
    "outputs": {
        "apply_plan": {"path": str(WP / "apply-plan.jsonl"), "rows": len(plan), "create": 6, "update": 0},
        "ledger": {"path": str(WP / "candidate-decision-ledger.jsonl"), "rows": len(ledger),
                   "candidates": 7, "applied": 6, "no_delta": 1, "rejected": 0},
        "canonical_mapping": {"path": str(WP / "canonical-mapping.json"), "entries": len(mapping)},
    },
    "state_after": {"applied": 548, "no_delta": 27, "rejected": 801, "needs_evidence": 3963, "total": 5339},
    "verification": {"status": "pending"},
    "notes": [
        "舞蹈纹彩陶盆事件由 works/wudaowen-caitao-pen.md 完整覆盖，判 no_delta。",
        "马王堆事件与 works/susha-chanyi.md 分工：后者记器物，本条记发掘数量、品种、织法与绒圈锦。",
        "曾侯乙墓发掘年份照录田自秉 1977 年，不据外部资料校正。",
    ],
}
(WP / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
print("ledger", len(ledger), "plan", len(plan), "mapping", len(mapping))
