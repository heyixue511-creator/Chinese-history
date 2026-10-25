# -*- coding: utf-8 -*-
"""Emit ledger, apply-plan, canonical mapping and manifest for Zhaonong 2009 procedure batch B."""
import hashlib
import json
from pathlib import Path

import yaml

ROOT = Path(".")
BATCH = Path("06-runtime/automation/2026-10-25-2009zhaonong-procedures-batch-b")
BATCH.mkdir(parents=True, exist_ok=True)
PREFIX = "2009-zhaonong-zhongguo-yishu-shejishi:"
DATE = "2026-10-25"
DOC = "2009-zhaonong-zhongguo-yishu-shejishi"

CREATES = [
    ("cand-03-43", "zhuo-yu", "琢玉", "stoneworking_technique", "商周", "玉料选择、切割、磨制、钻孔、雕刻；金属工具与铊子（砣机）广泛使用；西周兼用阴刻、浮雕、圆雕、透雕"),
    ("cand-04-90", "bai-lian-gang", "百炼钢", "metalworking_technique", "秦汉（西汉中期普遍）", "块铁多次加热锻打，杂质减少、体积变小、韧度与强度加大而转化为钢；百炼成钢"),
    ("cand-04-91", "chao-gang", "炒钢", "metalworking_technique", "西汉中期", "生铁加热、添入矿石搅拌以降低含炭程度，再锻制，提高百炼钢制器的速度和质量"),
    ("cand-04-93", "chromate-oxidation-treatment", "铬盐氧化防锈处理", "metalworking_technique", "秦代", "秦俑坑青铜剑剑身脊刃对称，表面经铬盐氧化防锈处理，出土后仍寒光闪烁"),
    ("cand-05-19", "zaozhishu", "造纸术", "papermaking_technique", "西汉出现；东汉蔡伦改进", "以树肤、麻头、敝布、鱼网造纸；元兴元年奏上，天下称蔡侯纸；西汉麻纸见于罗布泊与灞桥"),
    ("cand-05-35", "han-dai-qiqi-zhizuo-fengong", "汉代漆器制作分工", "lacquer_technique", "汉代", "漆器铭文见素工、髹工、上工、黄涂工、画工、雕工、清工、供工、造工等工种，分工细致"),
    ("cand-05-54", "huodong-lianchuang-zhimo", "活动帘床纸模抄纸法", "papermaking_technique", "三国以后", "竹帘置框架中连续抄捞湿纸并晾晒；纸药、施胶、涂布提高纸张性能"),
    ("cand-05-56", "ran-zhi", "染纸（潢纸）", "papermaking_technique", "东汉开始；魏晋沿用", "黄柏皮中的柏碱加入纸浆染纸，增美观并防虫蛀；《齐民要术》记潢纸不宜太深"),
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
    "work_package": "2026-10-25-2009zhaonong-procedures-batch-b",
    "goal": "处理赵农《中国艺术设计史》2009 册第 10—17 个 procedure 候选：8 个新建；无 update、无 no_delta、无 rejected。",
    "status": "applied",
    "date": DATE,
    "inputs": {
        "candidate_index": {
            "path": "06-runtime\\state\\candidate-index.jsonl",
            "rows_before": 5339,
            "sha256_before": "sha256:c104eef43891c1fc726b8f570ff7389a170ffe96e40c9ddc521e86933067932e",
            "sha256_scope": "CRLF→LF 归一后",
            "counts_before": {
                "applied": 691,
                "needs_evidence": 3804,
                "no_delta": 43,
                "rejected": 801,
            },
        },
        "source": {
            "doc_id": DOC,
            "file": "03基础书籍-md文档/中国艺术设计史_赵农_2009_高等教育出版社.md",
            "spans": ["L1686-L1690", "L2743-L2747", "L2763", "L3127-L3138", "L3230-L3234", "L3413-L3421", "L3419"],
        },
    },
    "method": {
        "rules": [
            "procedure 候选按实体而非 slug 对账：先与既有 procedure KU 的标题与内容对齐，再定 create／update。",
            "工序条目只写来源所记材料、步骤、工具、产量与实例；来源未载的工序参数写入证据边界。",
            "来源的判断与推测照录并标明主语；原文异体与疑似讹字照录并注明。",
            "同一段并记的两种工艺按材料与工序分列，互指而不合并。",
        ],
        "source_policy": "02-sources 只读；本批写 04-knowledge/units/procedures，8 条均为新建。",
    },
    "outputs": {
        "apply_plan": {
            "path": "06-runtime\\automation\\2026-10-25-2009zhaonong-procedures-batch-b\\apply-plan.jsonl",
            "rows": 8,
            "create": 8,
            "update": 0,
        },
        "ledger": {
            "path": "06-runtime\\automation\\2026-10-25-2009zhaonong-procedures-batch-b\\candidate-decision-ledger.jsonl",
            "rows": 24,
            "candidates": 8,
            "applied": 8,
            "no_delta": 0,
            "rejected": 0,
        },
        "canonical_mapping": {
            "path": "06-runtime\\automation\\2026-10-25-2009zhaonong-procedures-batch-b\\canonical-mapping.json",
            "entries": 8,
        },
    },
    "verification": {"status": "pending"},
}

(BATCH / "manifest.json").write_bytes(
    (json.dumps(manifest, ensure_ascii=False, indent=2) + "\n").encode("utf-8")
)
print("ledger", len(ledger), "plan", len(plan), "mapping", len(mapping))
