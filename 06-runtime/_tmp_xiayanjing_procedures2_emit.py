# -*- coding: utf-8 -*-
"""Emit ledger, apply-plan, canonical mapping and manifest for Xiayanjing 2009 procedure batch 2."""
import hashlib
import json
from pathlib import Path

import yaml

ROOT = Path(".")
BATCH = Path("06-runtime/automation/2026-10-25-2009xiayanjing-procedures-batch-2")
BATCH.mkdir(parents=True, exist_ok=True)
PREFIX = "2009-xiayanjing-zhongguo-shejishi:"
DATE = "2026-10-25"
DOC = "2009-xiayanjing-zhongguo-shejishi"

CREATES = [
    ("cand-02-32", "xiu-qi", "髹漆", "lacquer_technique", "战国", "髹漆工艺有描彩漆、镶嵌、针刻；纹样行动物纹、云纹、几何图案；色彩丰富、线条奔放"),
    ("cand-02-60", "lian-gang-ji-shu", "炼钢技术", "metalworking_technique", "春秋战国", "长沙杨家山春秋晚期钢剑含碳 0.5%—0.6%；易县燕下都战国钢剑钢戟钢矛为块炼铁渗碳锻打"),
    ("cand-03-107", "han-dai-zhijin-cixiu", "汉代织锦与刺绣工艺", "textile_technique", "汉代", "织锦经线显花、五色以上、东汉蜀锦加金；刺绣针法有平针、锁绣、钉线绣"),
    ("cand-04-93", "zhi-quan-fu-shao", "支圈覆烧", "ceramic_technique", "南宋中期", "景德镇等窑支圈覆烧，窑具一次性使用，保证质量、减少变形、提高装烧密度"),
    ("cand-04-95", "pearl-ground-sgraffito", "珍珠地划花", "ceramic_technique", "宋代", "主题纹样空隙处划饰细密珍珠纹，为磁州窑系装饰方法之一"),
    ("cand-05-95", "ming-qing-caici-zhuangshi", "明清彩瓷装饰技法", "ceramic_technique", "明成化—清康熙", "斗彩、素三彩、五彩、珐琅彩、粉彩的工序与风格"),
]

UPDATES = [
    {
        "cand": "cand-03-26",
        "entity": "蜡染（蜡缬）",
        "target_ref": "04-knowledge/units/procedures/la-ran.md",
        "before": {
            "sha256": "sha256:7b54521f8c8b3f64074e594b242353fbecf3b8630b5dbf4c7b72abb6ea459103",
            "bytes": 3114,
            "lines": 79,
        },
        "note": "补入夏燕靖 2009 的西南少数民族秦汉蜡染、“阑干斑布”名称、点线结合纹样、向中原与亚洲传播及民丰蓝白印花布的命名差异。",
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
        ("needs_evidence", "ready_for_review", f"已完成语义复读：既有 {target} 可承载但缺夏燕靖 2009 记载，提交 update"),
        ("ready_for_review", "approved", f"canonical 候选语义复读完成，批准按 exact change-set 补写 {target}"),
        ("approved", "applied", f"已按 exact change-set 补入夏燕靖 2009 记载：{target}"),
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

assert len(ledger) == 21, len(ledger)
assert len(plan) == 7, len(plan)
assert len(mapping) == 7, len(mapping)

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
    "work_package": "2026-10-25-2009xiayanjing-procedures-batch-2",
    "goal": "处理夏燕靖《中国设计史》2009 册剩余 7 个 procedure 候选：6 个新建，1 个补入既有蜡染 KU；无 no_delta、无 rejected。",
    "status": "applied",
    "date": DATE,
    "inputs": {
        "candidate_index": {
            "path": "06-runtime\\state\\candidate-index.jsonl",
            "rows_before": 5339,
            "sha256_before": "sha256:6cf8954a8170f21e78358517f435623b9f702e7a91b8f9dc366380790069b410",
            "sha256_scope": "CRLF→LF 归一后",
            "counts_before": {
                "applied": 675,
                "needs_evidence": 3820,
                "no_delta": 43,
                "rejected": 801,
            },
        },
        "source": {
            "doc_id": DOC,
            "file": "03基础书籍-md文档/中国设计史_夏燕靖_2009_上海人民美术出版社.md",
            "spans": ["L956-L961", "L1140-L1147", "L1426-L1431", "L1433-L1441", "L2548-L2551", "L2552-L2589", "L3589-L3591"],
        },
    },
    "method": {
        "rules": [
            "procedure 候选按实体而非 slug 对账：先与既有 procedure KU 的标题与内容对齐，再定 create／update。",
            "工序条目只写来源所记材料、步骤、工具、产量与实例；来源未载的工序参数写入证据边界。",
            "来源的判断与推测照录并标明主语；原文截断处照录并注明。",
            "两种来源对同一出土物的命名不一致时并列记录，不裁定名称。",
        ],
        "source_policy": "02-sources 只读；本批写 04-knowledge/units/procedures，并对既有蜡染 KU 补入夏燕靖 2009 来源。",
    },
    "outputs": {
        "apply_plan": {
            "path": "06-runtime\\automation\\2026-10-25-2009xiayanjing-procedures-batch-2\\apply-plan.jsonl",
            "rows": 7,
            "create": 6,
            "update": 1,
        },
        "ledger": {
            "path": "06-runtime\\automation\\2026-10-25-2009xiayanjing-procedures-batch-2\\candidate-decision-ledger.jsonl",
            "rows": 21,
            "candidates": 7,
            "applied": 7,
            "no_delta": 0,
            "rejected": 0,
        },
        "canonical_mapping": {
            "path": "06-runtime\\automation\\2026-10-25-2009xiayanjing-procedures-batch-2\\canonical-mapping.json",
            "entries": 7,
        },
    },
    "verification": {"status": "pending"},
}

(BATCH / "manifest.json").write_bytes(
    (json.dumps(manifest, ensure_ascii=False, indent=2) + "\n").encode("utf-8")
)
print("ledger", len(ledger), "plan", len(plan), "mapping", len(mapping))
