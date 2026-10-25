# -*- coding: utf-8 -*-
"""Emit ledger, apply-plan, mapping and manifest for the 2016 modern events batch."""
import hashlib
import json
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from _tmp_2016_modern_items_a import ITEMS_A
from _tmp_2016_modern_items_b import ITEMS_B
from _tmp_2016_modern_items_c import ITEMS_C

WP = Path("06-runtime/automation/2026-10-25-2016-modern-events-batch")
WP.mkdir(parents=True, exist_ok=True)
DATE = "2026-10-25"
PREFIX = "2016-xiayanjing-zhongguo-yishu-shejishi-upgrade:"
INDEX = Path("06-runtime/state/candidate-index.jsonl")
ITEMS = ITEMS_A + ITEMS_B + ITEMS_C

CREATES = [
    (item["cand"], f"04-knowledge/units/events/{item['slug']}.md", item["title"],
     f"新建{item['sub']}：{item['date']}；{item['result']}")
    for item in ITEMS
]

NO_DELTA = [
    ("cand-09-50", "04-knowledge/units/works/zhongshan-ling-1929.md", "中山陵建筑设计竞图",
     "既有 work KU 已完整记录 1927 年公开征图、条例引文、吕彦直首奖与钟形平面"),
    ("cand-10-34", "04-knowledge/units/persons/pang-xunqin.md", "1957年对庞薰琴为首的反党集团的斗争",
     "既有 person KU 已逐字记录 1957 年 7—9 月学院展开三个月斗争及两版姓名字形差异"),
    ("cand-10-53", "04-knowledge/units/institutions/central-academy-arts-design.md", "中央工艺美术学院获工艺美术历史及理论专业博士学位授予点",
     "既有 institution KU 已记录 1986 年 7 月经国务院学位委员会批准获博士学位授予点"),
    ("cand-11-03", "04-knowledge/units/institutions/central-academy-arts-design.md", "中央工艺美术学院与清华大学合并",
     "既有 institution KU 已记录 1999 年 11 月 20 日合并成立清华大学美术学院"),
]


def fingerprint(path):
    data = path.read_bytes()
    text = data.decode("utf-8").replace("\r\n", "\n")
    payload = text.encode("utf-8")
    return {"sha256": "sha256:" + hashlib.sha256(payload).hexdigest(),
            "bytes": len(payload), "lines": text.count("\n")}


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


index_rows = [json.loads(l) for l in INDEX.read_text(encoding="utf-8").splitlines() if l.strip()]
by_id = {r["candidate_id"]: r for r in index_rows}
before_hash = fingerprint(INDEX)
before_counts = Counter(r["state"] for r in index_rows)
spans = []
for cid, *_ in CREATES + NO_DELTA:
    r = by_id[PREFIX + cid]
    sp = r["payload"].get("source_span", {})
    spans.append(f"L{sp.get('line_start')}-L{sp.get('line_end')}" if sp.get("line_end") != sp.get("line_start") else f"L{sp.get('line_start')}")

ledger, plan, mapping = [], [], []
for cid, target, entity, note in CREATES:
    full = PREFIX + cid
    ledger.extend(rows(full, target, "create"))
    fp = fingerprint(Path(target))
    plan.append({"action": "create", "target_ref": target, "candidate_id": full, "entity": entity,
                 "before": None, "after_sha256": fp["sha256"], "bytes": fp["bytes"],
                 "lines": fp["lines"], "note": note})
    mapping.append({"entity": entity, "target_ref": target, "action": "create",
                    "canonical_candidate": full, "merged_candidates": []})

for cid, target, entity, note in NO_DELTA:
    full = PREFIX + cid
    ledger.extend(rows(full, target, "no_delta"))
    mapping.append({"entity": entity, "target_ref": target, "action": "no_delta",
                    "canonical_candidate": full, "merged_candidates": [], "note": note})

with (WP / "candidate-decision-ledger.jsonl").open("w", encoding="utf-8", newline="") as fh:
    for row in ledger:
        fh.write(json.dumps(row, ensure_ascii=False) + "\n")
with (WP / "apply-plan.jsonl").open("w", encoding="utf-8", newline="") as fh:
    for row in plan:
        fh.write(json.dumps(row, ensure_ascii=False) + "\n")
(WP / "canonical-mapping.json").write_text(json.dumps(mapping, ensure_ascii=False, indent=2), encoding="utf-8")

after_counts = Counter(before_counts)
after_counts["needs_evidence"] -= len(CREATES) + len(NO_DELTA)
after_counts["applied"] += len(CREATES)
after_counts["no_delta"] += len(NO_DELTA)

manifest = {
    "work_package": WP.name,
    "goal": "处理夏燕靖《中国艺术设计史（升级版）》2016 册现代设计大事记的 37 个 event 候选：33 个新建 event KU，4 个由既有 KU 覆盖判 no_delta。",
    "status": "applied",
    "date": DATE,
    "inputs": {
        "candidate_index": {
            "path": str(INDEX), "rows_before": len(index_rows),
            "sha256_before": before_hash["sha256"],
            "sha256_scope": "CRLF→LF 归一后",
            "counts_before": dict(sorted(before_counts.items())),
        },
        "source": {
            "doc_id": "2016-xiayanjing-zhongguo-yishu-shejishi-upgrade",
            "file": "03基础书籍-md文档/中国艺术设计史（升级版）_夏燕靖_2016_上海人民美术出版社.md",
            "spans": spans,
        },
    },
    "method": {
        "rules": [
            "事件若无既有 KU 可承载，且来源给出时间、地点、参与者、过程或行业信息，建 event KU。",
            "事件若已被既有 work/person/institution KU 完整覆盖，判 no_delta，不重复建条。",
            "事件条目只写来源所记事实；未给出处、主办、展品数、议程或统计口径时写入证据边界。",
            "展览类用 sub_type: exhibition；会议、学会、论坛、设计周用 professional_event；政策、建筑、行业变动用 historical_event。",
        ],
        "source_policy": "02-sources 只读；本批只写 04-knowledge/units/events。",
    },
    "outputs": {
        "apply_plan": {"path": str(WP / "apply-plan.jsonl"), "rows": len(plan), "create": len(CREATES), "update": 0},
        "ledger": {"path": str(WP / "candidate-decision-ledger.jsonl"), "rows": len(ledger),
                   "candidates": len(CREATES) + len(NO_DELTA), "applied": len(CREATES),
                   "no_delta": len(NO_DELTA), "rejected": 0},
        "canonical_mapping": {"path": str(WP / "canonical-mapping.json"), "entries": len(mapping)},
    },
    "state_after": {"applied": after_counts["applied"], "no_delta": after_counts["no_delta"],
                    "rejected": after_counts["rejected"], "needs_evidence": after_counts["needs_evidence"],
                    "total": len(index_rows)},
    "verification": {"status": "pending"},
    "notes": [
        "4 个 no_delta 分别由 works/zhongshan-ling-1929.md、persons/pang-xunqin.md、institutions/central-academy-arts-design.md 覆盖；其中后两者共用机构条。",
        "展览类 12 条用 exhibition；会议、学会、论坛、设计周 11 条用 professional_event；其余 10 条用 historical_event。",
        "1972 年全国工艺美术展览会的“4 个多月”与“民族文化宫、17000 余件”分见来源两处，KU 并列保留，不代为拼合。",
        "1959 年书籍装帧展、1982 年广告展、1999 年书籍装帧展等只记来源所载日期、地点、主办与结果，未补外部展史资料。",
    ],
}
(WP / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
print("ledger", len(ledger), "plan", len(plan), "mapping", len(mapping), "before", dict(before_counts))
