# -*- coding: utf-8 -*-
"""Emit ledger, apply-plan, canonical mapping and manifest for the Li Lixin 2011 event batch."""
import hashlib
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from _tmp_lilixin_events_items import ITEMS_LLX

ROOT = Path(".")
BATCH = Path("06-runtime/automation/2026-10-25-2011lilixin-events-batch")
BATCH.mkdir(parents=True, exist_ok=True)
PREFIX = "2011-lilixin-zhongguo-sheji-yishu-shilun:"
DATE = "2026-10-25"
DOC = "2011-lilixin-zhongguo-sheji-yishu-shilun"

UPDATES = [
    {
        "cand": "cand-03-121",
        "entity": "北魏孝文帝、孝明帝服饰改制",
        "target_ref": "04-knowledge/units/events/xiaomingdi-fushi-gaige.md",
        "span": "L930",
        "before": {
            "sha256": "sha256:97fc632df480828064a9b927a6f5dc9bde922d58bb33db3fff3953076d4b1c3f",
            "bytes": 4212,
            "lines": 83,
        },
        "note": "补入李立新 2011 所记孝文帝制订朝服吸收熟悉南朝典制者参与设计、孝明帝改制后服饰趋向博大程度超过南朝、胡服后演变为隋唐流行服装；候选兼含两帝，孝文帝整体汉化另见 events/xiao-wen-gai-zhi.md。",
    },
]

NO_DELTA = [
    {
        "cand": "cand-03-81",
        "entity": "1987 年法门寺塔基地宫发现十三件秘色瓷",
        "target_ref": "04-knowledge/units/terms/mise-porcelain.md",
        "note": "既有 term KU 已记 1987 年法门寺地宫发现、李立新“十三件”说与三说并存，并已引李立新 2011 原文。",
        "span": "L1025-L1028",
    },
    {
        "cand": "cand-03-83",
        "entity": "《天工开物》成书（1636 年）",
        "target_ref": "04-knowledge/units/publications/tiangong-kaiwu.md",
        "note": "既有 publication KU 已记李立新作 1636 年撰成、与高丰与夏燕靖 1637 年刊行说并列，并已引李立新 2011。",
        "span": "L1183",
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

for item in ITEMS_LLX:
    cid = PREFIX + item["cand"]
    target = f"04-knowledge/units/events/{item['slug']}.md"
    path = ROOT / target
    if not path.exists():
        raise SystemExit(f"missing {target}")
    fm = norm_text(path).split("---\n", 2)[1]
    if f'title: "{item["title"]}（{item["en"]}）"' not in fm:
        raise SystemExit(f"title mismatch {target}")
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
    ledger.append({
        "candidate_id": cid,
        "expected_state": "needs_evidence",
        "state": "ready_for_review",
        "decision": {
            "status": "pending",
            "reason": f"已完成语义复读：既有 {target} 可承载但缺李立新 2011 记载，提交 update",
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
            "reason": f"canonical 候选语义复读完成，批准按 exact change-set 补写 {target}",
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
            "reason": f"已按 exact change-set 补入李立新 2011 记载：{target}",
            "decided_by": "Agent",
            "decided_at": DATE,
        },
        "updated_at": DATE,
        "target_ref": target,
    })
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

assert len(ledger) == 33, len(ledger)
assert len(plan) == 9, len(plan)
assert len(mapping) == 11, len(mapping)

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
    "work_package": "2026-10-25-2011lilixin-events-batch",
    "goal": "处理李立新《中国设计艺术史论》2011 册的 11 个 event 候选：8 个新建 event KU，1 个补入既有 KU，2 个由既有 KU 覆盖判 no_delta。",
    "status": "applied",
    "date": DATE,
    "inputs": {
        "candidate_index": {
            "path": "06-runtime\\state\\candidate-index.jsonl",
            "rows_before": 5339,
            "sha256_before": "sha256:781faf8b4d7d1a637c32b71bf676fa85374c290d789ba91e1e5140fb5cd7f603",
            "sha256_scope": "CRLF→LF 归一后",
            "counts_before": {
                "applied": 643,
                "needs_evidence": 3854,
                "no_delta": 41,
                "rejected": 801,
            },
        },
        "source": {
            "doc_id": DOC,
            "file": "03基础书籍-md文档/中国设计艺术史论_李立新_2011_人民出版社.md",
            "spans": [i["span"] for i in ITEMS_LLX] + [u["span"] for u in UPDATES] + [n["span"] for n in NO_DELTA],
        },
    },
    "method": {
        "rules": [
            "既有同题 KU 可承载但缺李立新 2011 记载的判 update；已有专条完整覆盖的判 no_delta；无对应实体的判 create。",
            "事件条目只写来源所记时间、地点、参与者、过程与结果；来源未载的年份、人物、数据与过程写入证据边界。",
            "来源的判断与推测照录并标明主语（来源认为／有学者认为），不提升为定论。",
            "候选兼含两个相邻事件而既有 KU 以其中一个为主体的，补入另一事件作为前奏或后续，并在 mapping 注明另一专条。",
        ],
        "source_policy": "02-sources 只读；本批写 04-knowledge/units/events，并对 terms 与 publications 的既有条目不重复写回。",
    },
    "outputs": {
        "apply_plan": {
            "path": "06-runtime\\automation\\2026-10-25-2011lilixin-events-batch\\apply-plan.jsonl",
            "rows": 9,
            "create": 8,
            "update": 1,
        },
        "ledger": {
            "path": "06-runtime\\automation\\2026-10-25-2011lilixin-events-batch\\candidate-decision-ledger.jsonl",
            "rows": 33,
            "candidates": 11,
            "applied": 9,
            "no_delta": 2,
            "rejected": 0,
        },
        "canonical_mapping": {
            "path": "06-runtime\\automation\\2026-10-25-2011lilixin-events-batch\\canonical-mapping.json",
            "entries": 11,
        },
    },
    "verification": {"status": "pending"},
}

(BATCH / "manifest.json").write_bytes(
    (json.dumps(manifest, ensure_ascii=False, indent=2) + "\n").encode("utf-8")
)
print("ledger", len(ledger), "plan", len(plan), "mapping", len(mapping))
