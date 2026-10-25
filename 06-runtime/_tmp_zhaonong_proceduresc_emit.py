# -*- coding: utf-8 -*-
"""Emit ledger, apply-plan, canonical mapping and manifest for Zhaonong 2009 procedure batch C."""
import hashlib
import json
from pathlib import Path

import yaml

ROOT = Path(".")
BATCH = Path("06-runtime/automation/2026-10-25-2009zhaonong-procedures-batch-c")
BATCH.mkdir(parents=True, exist_ok=True)
PREFIX = "2009-zhaonong-zhongguo-yishu-shejishi:"
DATE = "2026-10-25"
DOC = "2009-zhaonong-zhongguo-yishu-shejishi"

CREATES = [
    ("cand-06-44", "bo-rou-diao", "薄肉雕", "sculpture_technique", "北朝（麦积山语境）", "麦积山上七佛阁长廊上方以薄肉雕表现飞天，将浮雕与绘画结合；因衣裙飘带飞舞、鲜花散浮而称散花楼"),
    ("cand-06-57", "guan-gang-fa", "灌钢法", "metalworking_technique", "隋唐（仅记推广）", "因鼓风与炼炉的出现，灌钢法在隋唐得以推广；来源只有一句，未给原料、配比与操作"),
    ("cand-06-87", "ta-ben", "拓本", "reproduction_technique", "隋唐（来源语境）", "造纸水平提高与纸张应用使拓本技术出现有了可能，并为印刷术产生提供必要条件"),
    ("cand-07-146", "huozi-yinshua", "活字印刷", "printing_technique", "北宋庆历年间", "胶泥刻字、火烧成陶质单字，铁版排字，松脂蜡与纸灰固定，平板压平；双版更互，木格按韵贮字"),
    ("cand-08-132", "fu-shao-fa", "覆烧法", "ceramic_technique", "北宋中期；宋代景德镇仿定窑", "定窑将瓷坯反扣于垫圈上，组装大型匣钵，增加装烧数量以提高产量和质量；景德镇在拉坯、过内范、修足等工序中仿定窑覆烧并形成自身技术特点"),
    ("cand-08-205", "zao-jia", "造甲", "armor_making", "宋代", "铠甲五十步强弩不能入；箭矢仅能自缀孔钻穿，钻空刮铁使箭头反卷，见其坚硬"),
    ("cand-08-206", "zao-jian", "造剑", "metalworking_technique", "宋代", "造剑不用太钢劲的钢材，剑身以柔铁为主，百炼成钢化为绕指柔，以弹力和韧性为特色"),
    ("cand-09-14", "tao-se-yinshua", "套色印刷", "printing_technique", "元代（1341）", "1341 年中兴路无闻和尚《金刚经注》扉页黑红套色图画，经文红色正文、黑色注文"),
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
    if fm.get("source_count") != 1:
        raise SystemExit(f"source_count mismatch {target}: {fm.get('source_count')}")
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

assert len(ledger) == 24, len(ledger)
assert len(plan) == 8, len(plan)
assert len(mapping) == 8, len(mapping)

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
    "work_package": "2026-10-25-2009zhaonong-procedures-batch-c",
    "goal": "处理赵农《中国艺术设计史》2009 册第 18—25 个 procedure 候选：8 个新建；无 update、无 no_delta、无 rejected。",
    "status": "applied",
    "date": DATE,
    "inputs": {
        "candidate_index": {
            "path": "06-runtime\\state\\candidate-index.jsonl",
            "rows_before": 5339,
            "sha256_before": "sha256:9b74996849218dae35fcfa7250d779ee15228e727900b28099d6dcbc03833f6c",
            "sha256_scope": "CRLF→LF 归一后",
            "counts_before": {
                "applied": 699,
                "needs_evidence": 3796,
                "no_delta": 43,
                "rejected": 801,
            },
        },
        "source": {
            "doc_id": DOC,
            "file": "03基础书籍-md文档/中国艺术设计史_赵农_2009_高等教育出版社.md",
            "spans": ["L4061", "L4166", "L4354", "L5041-L5060", "L5307", "L5309", "L5579", "L6014"],
        },
    },
    "method": {
        "rules": [
            "procedure 候选按实体而非 slug 对账：先与既有 procedure KU 的标题与内容对齐，再定 create／update。",
            "工序条目只写来源所记材料、步骤、工具、产量与实例；来源未载的工序参数写入证据边界。",
            "来源的判断与推测照录并标明主语；原文异体与疑似讹字照录并注明。",
            "同一技术家族中窑具或工序不同的实例分列，互指而不合并。",
        ],
        "source_policy": "02-sources 只读；本批写 04-knowledge/units/procedures，8 条均为新建。",
    },
    "outputs": {
        "apply_plan": {
            "path": "06-runtime\\automation\\2026-10-25-2009zhaonong-procedures-batch-c\\apply-plan.jsonl",
            "rows": 8,
            "create": 8,
            "update": 0,
        },
        "ledger": {
            "path": "06-runtime\\automation\\2026-10-25-2009zhaonong-procedures-batch-c\\candidate-decision-ledger.jsonl",
            "rows": 24,
            "candidates": 8,
            "applied": 8,
            "no_delta": 0,
            "rejected": 0,
        },
        "canonical_mapping": {
            "path": "06-runtime\\automation\\2026-10-25-2009zhaonong-procedures-batch-c\\canonical-mapping.json",
            "entries": 8,
        },
    },
    "verification": {"status": "pending"},
}

(BATCH / "manifest.json").write_bytes(
    (json.dumps(manifest, ensure_ascii=False, indent=2) + "\n").encode("utf-8")
)
print("ledger", len(ledger), "plan", len(plan), "mapping", len(mapping))
