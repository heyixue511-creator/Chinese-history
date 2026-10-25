# -*- coding: utf-8 -*-
"""Emit ledger, apply-plan, canonical mapping and manifest for Zhaonong 2009 procedure batch A."""
import hashlib
import json
from pathlib import Path

import yaml

ROOT = Path(".")
BATCH = Path("06-runtime/automation/2026-10-25-2009zhaonong-procedures-batch-a")
BATCH.mkdir(parents=True, exist_ok=True)
PREFIX = "2009-zhaonong-zhongguo-yishu-shejishi:"
DATE = "2026-10-25"
DOC = "2009-zhaonong-zhongguo-yishu-shejishi"

CREATES = [
    ("cand-01-38", "daogeng-huozhong", "刀耕火种", "agricultural_technique", "新石器时代", "砍伐森林→晒干→烧荒→木棒尖头点孔种植；前期弃地轮换，后期翻耕连作，石锄作用重要"),
    ("cand-01-44", "zhitao", "制陶", "ceramic_technique", "新石器时代", "黏土加砂与水调和成陶泥，经拌泥、淘洗、加料、盘泥、拉坯、制器；出现专业陶作坊与分工"),
    ("cand-02-15", "bianzhi", "编织", "textile_technique", "新石器时代", "河姆渡苇席残片最大1平方米、绳索粗细1.2厘米与2—3毫米；良渚与仰韶出现十字纹、人字纹、梅花眼、辫子口、棋盘格纹"),
    ("cand-02-35", "divination", "占卜", "ritual_technique", "商代", "龟腹甲背甲分开打磨、牛肩胛骨去骨臼刮磨，背面钻孔不穿透，蓍草烧灼取兆；龟曰卜、蓍曰筮"),
    ("cand-02-58", "dyeing", "染色", "textile_technique", "商周", "草染与石染两类，线染、匹染、多次浸染、媒染；染色成为社会生产职业"),
    ("cand-03-124", "rammed-earth-board-construction", "夯土板筑", "construction_technique", "商代—战国", "雍城遗址3300×3200米；挖槽、夯土坚实、板筑；木板改圆木使受力均匀，咸阳见平夯与窝夯"),
    ("cand-03-143", "turquoise-inlay", "错石工艺", "metalworking_technique", "春秋战国", "绿松石用漆汁粘嵌铜器錾槽中打磨；越王勾践剑剑格兽面纹错石为典型"),
]

UPDATES = [
    {
        "cand": "cand-01-18",
        "entity": "磨制技术",
        "target_ref": "04-knowledge/units/procedures/mozhi-shiqi.md",
        "before": {
            "sha256": "sha256:e3a50eae5e3848872e63660c4e4f4a0d82571f6faff82b15cbfea2af06c0ea41",
            "bytes": 4243,
            "lines": 74,
        },
        "note": "补入赵农 2009 的砺石加砂子与水的磨制介质、石质与玉质区分、刀脊刀刃与工具武器分离、石纺轮、复合绑捆与玉材位置。",
    },
    {
        "cand": "cand-03-142",
        "entity": "错金银",
        "target_ref": "04-knowledge/units/procedures/cuo-jin-yin-cuo-tong.md",
        "before": {
            "sha256": "sha256:c7a8ae55c79ef83573a634075faf96f8aefe4ff646c6e7e6fb0e90b093bd4887",
            "bytes": 3504,
            "lines": 76,
        },
        "note": "补入赵农 2009 的错金银技术定义与磨石错平磨光工序、战国兵器带钩车器铜镜等器类、汲县《水陆攻战图鉴》错铜作品；错石另列。",
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


ledger = []
plan = []
mapping = []

for cand, slug, title, sub, date, result in CREATES:
    cid = PREFIX + cand
    target = f"04-knowledge/units/procedures/{slug}.md"
    path = ROOT / target
    if not path.exists():
        raise SystemExit(f"missing {target}")
    fm = yaml.safe_load(path.read_text(encoding="utf-8").split("---\n", 2)[1])
    if title not in fm.get("title", ""):
        raise SystemExit(f"title mismatch {target}: {fm.get('title')}")
    if fm.get("sub_type") != sub:
        raise SystemExit(f"sub_type mismatch {target}: {fm.get('sub_type')}")
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
        "entity": title,
        "before": None,
        "after_sha256": fp["sha256"],
        "bytes": fp["bytes"],
        "lines": fp["lines"],
        "note": f"新建{sub}：{date}；{result}",
    })
    mapping.append({
        "entity": title,
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
        ("needs_evidence", "ready_for_review", f"已完成语义复读：既有 {target} 可承载但缺赵农 2009 记载，提交 update"),
        ("ready_for_review", "approved", f"canonical 候选语义复读完成，批准按 exact change-set 补写 {target}"),
        ("approved", "applied", f"已按 exact change-set 补入赵农 2009 记载：{target}"),
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

assert len(ledger) == 27, len(ledger)
assert len(plan) == 9, len(plan)
assert len(mapping) == 9, len(mapping)

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
    "work_package": "2026-10-25-2009zhaonong-procedures-batch-a",
    "goal": "处理赵农《中国艺术设计史》2009 册前 9 个 procedure 候选：7 个新建，2 个补入既有磨制石器与错金银 KU；无 no_delta、无 rejected。",
    "status": "applied",
    "date": DATE,
    "inputs": {
        "candidate_index": {
            "path": "06-runtime\\state\\candidate-index.jsonl",
            "rows_before": 5339,
            "sha256_before": "sha256:f25748ccaf593f1a825641b8a5565cbd07f6a71fe80784ff23602ab4abd40ada",
            "sha256_scope": "CRLF→LF 归一后",
            "counts_before": {
                "applied": 682,
                "needs_evidence": 3813,
                "no_delta": 43,
                "rejected": 801,
            },
        },
        "source": {
            "doc_id": DOC,
            "file": "03基础书籍-md文档/中国艺术设计史_赵农_2009_高等教育出版社.md",
            "spans": ["L513-L558", "L559-L591", "L606-L627", "L901-L935", "L1128-L1185", "L1435-L1456", "L2100-L2139", "L2192-L2252"],
        },
    },
    "method": {
        "rules": [
            "procedure 候选按实体而非 slug 对账：先与既有 procedure KU 的标题与内容对齐，再定 create／update。",
            "工序条目只写来源所记材料、步骤、工具、产量与实例；来源未载的工序参数写入证据边界。",
            "来源的判断与推测照录并标明主语；原文截断、异体与疑似讹字照录并注明。",
            "两种来源对同一出土物的命名不一致时并列记录，不裁定名称。",
        ],
        "source_policy": "02-sources 只读；本批写 04-knowledge/units/procedures，并对既有磨制石器与错金银 KU 补入赵农 2009 来源。",
    },
    "outputs": {
        "apply_plan": {
            "path": "06-runtime\\automation\\2026-10-25-2009zhaonong-procedures-batch-a\\apply-plan.jsonl",
            "rows": 9,
            "create": 7,
            "update": 2,
        },
        "ledger": {
            "path": "06-runtime\\automation\\2026-10-25-2009zhaonong-procedures-batch-a\\candidate-decision-ledger.jsonl",
            "rows": 27,
            "candidates": 9,
            "applied": 9,
            "no_delta": 0,
            "rejected": 0,
        },
        "canonical_mapping": {
            "path": "06-runtime\\automation\\2026-10-25-2009zhaonong-procedures-batch-a\\canonical-mapping.json",
            "entries": 9,
        },
    },
    "verification": {"status": "pending"},
}

(BATCH / "manifest.json").write_bytes(
    (json.dumps(manifest, ensure_ascii=False, indent=2) + "\n").encode("utf-8")
)
print("ledger", len(ledger), "plan", len(plan), "mapping", len(mapping))
