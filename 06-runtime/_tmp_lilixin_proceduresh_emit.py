# -*- coding: utf-8 -*-
"""Emit ledger, apply-plan, canonical mapping and manifest for Li Lixin procedure batch H."""
import hashlib
import json
from pathlib import Path

import yaml

ROOT = Path(".")
BATCH = Path("06-runtime/automation/2026-10-25-2011lilixin-procedures-batch-h")
BATCH.mkdir(parents=True, exist_ok=True)
PREFIX = "2011-lilixin-zhongguo-sheji-yishu-shilun:"
DATE = "2026-10-25"

# (candidate, slug, expected title fragment, sub_type, entity label, note)
CREATES = [
    ("cand-01-35", "qianzhu-maozhu", "嵌铸法与铆铸法", "metalworking_technique", "嵌铸法与铆铸法",
     "三星堆太阳形器以嵌铸法和铆铸法分五部分二次铸成；来源仅图注"),
    ("cand-02-06", "shiqi-dazhi-sanfa", "石器打制三法", "stoneworking_technique", "石器打制三法",
     "砸击法、锤击法、碰砧法；砸击法有完整动作与石片尺寸特征"),
    ("cand-02-92", "tihua-jishu", "提花技术", "textile_technique", "提花技术",
     "商代两件提花实物，自商代至汉代定型标准化，汉代提花机部件"),
    ("cand-03-76", "yin-xunlu-zhizuo", "银熏炉制作工序", "metalworking_technique", "银熏炉制作工序",
     "法门寺银熏炉：钣金成型、附件浇铸、纹饰涂金；长度数据存疑照录"),
    ("cand-03-77", "fenben-fuzhi", "粉本复制", "reproduction_technique", "粉本复制",
     "画稿经扎孔、扑粉、勾勒印漏完成复制，用于刺绣、缂丝"),
]

UPDATES = [
    ("cand-02-35", "hefan-fa", "合范法", "metalworking_technique", "合范法",
     "补入李立新范铸法道路判断、八阶段、六齐、分铸法与一模翻范数演变", []),
    ("cand-02-40", "zhuo-yu", "琢玉", "stoneworking_technique", "琢玉",
     "补入李立新刮摩名义、雕琢六步、良渚原始砣具与三代青铜砣具", []),
    ("cand-03-78", "zaozhishu", "造纸术", "papermaking_technique", "造纸术",
     "补入李立新所记《天工开物》杀青造纸流程与篇章定位", []),
    ("cand-04-07", "duanban-taoyin", "短版套印", "printing_technique", "短版套印",
     "补入李立新所记胡正言改进分色套印、短版拱花与十竹斋画谱", []),
]

# candidate merged into another candidate's target: (candidate, canonical candidate, target, note)
MERGED = [
    ("cand-04-44", "cand-02-35", "04-knowledge/units/procedures/hefan-fa.md",
     "块范铸造法与范铸法同实，并入合范法（canonical cand-02-35）"),
]

BEFORE = json.loads(Path("06-runtime/_tmp_pre_h_hashes.json").read_text(encoding="utf-8"))


def fingerprint(path: Path):
    data = path.read_bytes()
    text = data.decode("utf-8").replace("\r\n", "\n")
    payload = text.encode("utf-8")
    return {
        "sha256": "sha256:" + hashlib.sha256(payload).hexdigest(),
        "bytes": len(payload),
        "lines": text.count("\n"),
    }


def ledger_rows(cid, target, kind):
    rows = []
    for expected, state, reason in [
        ("needs_evidence", "ready_for_review", f"已完成语义复读：{kind} {target}"),
        ("ready_for_review", "approved", f"canonical 候选语义复读完成，批准按 exact change-set {kind} {target}"),
        ("approved", "applied", f"已按 exact change-set {kind} {target}"),
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
        rows.append(row)
    return rows


ledger = []
plan = []
mapping = []

for cand, slug, title, sub, entity, note in CREATES:
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
    ledger.extend(ledger_rows(cid, target, "新建"))
    plan.append({
        "action": "create",
        "target_ref": target,
        "candidate_id": cid,
        "entity": entity,
        "before": None,
        "after_sha256": fp["sha256"],
        "bytes": fp["bytes"],
        "lines": fp["lines"],
        "note": f"新建{sub}：{note}",
    })
    mapping.append({
        "entity": entity,
        "target_ref": target,
        "action": "create",
        "canonical_candidate": cid,
        "merged_candidates": [],
    })

for cand, slug, title, sub, entity, note, extra in UPDATES:
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
    before = BEFORE[slug]
    fp = fingerprint(path)
    ledger.extend(ledger_rows(cid, target, "更新"))
    plan.append({
        "action": "update",
        "target_ref": target,
        "candidate_id": cid,
        "entity": entity,
        "before": before,
        "after_sha256": fp["sha256"],
        "bytes": fp["bytes"],
        "lines": fp["lines"],
        "note": f"更新{sub}：{note}",
    })
    mapping.append({
        "entity": entity,
        "target_ref": target,
        "action": "update",
        "canonical_candidate": cid,
        "merged_candidates": [],
    })

for cand, canonical, target, note in MERGED:
    cid = PREFIX + cand
    ledger.extend(ledger_rows(cid, target, "合并更新"))
    for m in mapping:
        if m["target_ref"] == target:
            m["merged_candidates"].append(cid)
            break
    else:
        raise SystemExit(f"no mapping target {target}")

assert len(ledger) == 30, len(ledger)
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
    "work_package": "2026-10-25-2011lilixin-procedures-batch-h",
    "goal": "处理李立新《中国设计艺术史论》10 个 procedure 候选：5 个新建、4 个更新（其中 2 个候选合并到合范法）；无 no_delta、无 rejected。",
    "status": "applied",
    "date": DATE,
    "inputs": {
        "candidate_index": {
            "path": "06-runtime\\state\\candidate-index.jsonl",
            "rows_before": 5339,
            "sha256_before": "sha256:99795771d9a714a38617b6625b317ad76b8fde9953ac73f4a6b8f81d251251ff",
            "sha256_scope": "CRLF→LF 归一后",
            "counts_before": {
                "applied": 768,
                "needs_evidence": 3727,
                "no_delta": 43,
                "rejected": 801,
            },
        },
        "source": {
            "doc_id": "2011-lilixin-zhongguo-sheji-yishu-shilun",
            "file": "03基础书籍-md文档/中国设计艺术史论_李立新_2011_人民出版社.md",
            "spans": [
                "L260", "L431", "L433", "L442", "L447", "L631-L635", "L642",
                "L794-L796", "L857", "L985", "L990", "L1161", "L1185", "L1200",
                "L1246", "L1560",
            ],
        },
    },
    "method": {
        "rules": [
            "procedure 候选按实体而非 slug 对账：先与既有 procedure KU 的标题与内容对齐，再定 create／update。",
            "同一实体在来源中分处两节时合并候选：范铸法与块范铸造法同指陶土制模作范，合入合范法一条。",
            "工序条目只写来源所记材料、步骤、工具、产量与实例；来源未载的工序参数写入证据边界。",
            "原文异写、同名异指与跨册差异照录并注明：银熏炉长度“295cm”与夏燕靖所记“29.5 厘米”并存；李立新作“短版拱花”，六册无“饾版”写法。",
        ],
        "source_policy": "02-sources 只读；本批写 04-knowledge/units/procedures，5 条新建、4 条更新。",
    },
    "outputs": {
        "apply_plan": {
            "path": "06-runtime\\automation\\2026-10-25-2011lilixin-procedures-batch-h\\apply-plan.jsonl",
            "rows": 9,
            "create": 5,
            "update": 4,
        },
        "ledger": {
            "path": "06-runtime\\automation\\2026-10-25-2011lilixin-procedures-batch-h\\candidate-decision-ledger.jsonl",
            "rows": 30,
            "candidates": 10,
            "applied": 10,
            "no_delta": 0,
            "rejected": 0,
        },
        "canonical_mapping": {
            "path": "06-runtime\\automation\\2026-10-25-2011lilixin-procedures-batch-h\\canonical-mapping.json",
            "entries": 9,
            "merged_candidates": [PREFIX + "cand-04-44"],
        },
    },
    "verification": {"status": "pending"},
}

(BATCH / "manifest.json").write_bytes(
    (json.dumps(manifest, ensure_ascii=False, indent=2) + "\n").encode("utf-8")
)
print("ledger", len(ledger), "plan", len(plan), "mapping", len(mapping))
for row in plan:
    print(row["action"], row["target_ref"], row["after_sha256"][:20], row["bytes"], row["lines"])
