# -*- coding: utf-8 -*-
"""Emit ledger, apply-plan, canonical mapping and manifest for Tian Zibing procedure batch E."""
import hashlib
import json
from pathlib import Path

import yaml

ROOT = Path(".")
BATCH = Path("06-runtime/automation/2026-10-25-2010tianzibing-procedures-batch-e")
BATCH.mkdir(parents=True, exist_ok=True)
PREFIX = "2010-tianzibing-zhongguo-gongyi-meishushi:"
DATE = "2026-10-25"

CREATES = [
    ("cand-02-51", "caihui-tao-zhizuo", "彩陶制作工艺", "ceramic_technique", "新石器时代晚期", "手捏成形、木片卵石打磨陶坯、绘红黑花纹后入窑烧成"),
    ("cand-02-52", "fengyao-jishu", "封窑技术", "ceramic_technique", "父系氏族社会", "严密封窑使铁元素还原成灰陶，控制末期空气与温度成黑陶"),
    ("cand-04-35", "sao-si-piaobai", "缫丝漂白与晾丝法", "textile_technique", "周代", "灰水沤丝、栏木灰与蜃灰漂白、离地一尺晾丝"),
    ("cand-04-39", "bangpao-xiangqian", "蚌泡镶嵌", "lacquer_technique", "周代", "木胎或编织胎外涂漆，器缘或器托镶蚌泡，为螺钿前身"),
    ("cand-03-41", "san-die-fa", "三叠法", "metalworking_technique", "商代后期", "主纹地纹之外在粗花纹上再勾刻细线，增加层次"),
    ("cand-05-91", "hanjie", "焊接", "metalworking_technique", "春秋战国", "主体铸成后用热加工补接部件或局部"),
    ("cand-05-92", "kehua", "刻划", "metalworking_technique", "战国", "随铁工具提高而出现，以刻刀在铜器上刻出细线纹"),
    ("cand-05-93", "qingtong-xiangqian", "青铜镶嵌", "metalworking_technique", "春秋战国", "嵌饰松石、红铜或金银丝，春秋多红铜、战国盛金银错"),
]

UPDATES = [
    ("cand-02-50", "mozhi-shiqi", "磨制石器", "stoneworking_technique", "旧石器时代至新石器时代",
     "补入田自秉石器制作打击、作窝、琢制、磨制、钻孔序列与管钻、两面对钻"),
    ("cand-02-73", "lunzhi-fa", "轮制法", "ceramic_technique", "新石器时代",
     "补入田自秉黑陶轮制、器形与器胎效果、封窑技术与窑室结构"),
    ("cand-03-02", "bianzhi", "编织", "textile_technique", "新石器时代",
     "补入田自秉编织起源、半坡庙底沟席纹、钱山漾竹编与辫子口用篾"),
    ("cand-03-21", "hefan-fa", "合范法", "metalworking_technique", "商周",
     "补入田自秉陶范法、泥模法工序与朱笔绘纹、支钉子母榫、绳索厚泥加固"),
    ("cand-04-34", "dyeing", "染色", "textile_technique", "商周",
     "补入田自秉《考工记》一入至七入的浸染递深色序"),
    ("cand-05-34", "cuo-jin-yin-cuo-tong", "错金银与错铜", "metalworking_technique", "春秋战国",
     "补入田自秉错石（厝石）为细砂岩的释名与文献依据"),
    ("cand-05-36", "yin-wen-mo-yin", "印纹（模印）装饰", "metalworking_technique", "春秋战国",
     "补入田自秉印纹阶段判断、盖印时机与纹样格式演变"),
]

BEFORE = json.loads(Path("06-runtime/_tmp_pre_e_hashes.json").read_text(encoding="utf-8"))


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
    ledger.extend(ledger_rows(cid, target, "新建"))
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

for cand, slug, title, sub, date, result in UPDATES:
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
        "entity": title,
        "before": before,
        "after_sha256": fp["sha256"],
        "bytes": fp["bytes"],
        "lines": fp["lines"],
        "note": f"更新{sub}：{date}；{result}",
    })
    mapping.append({
        "entity": title,
        "target_ref": target,
        "action": "update",
        "canonical_candidate": cid,
        "merged_candidates": [],
    })

assert len(ledger) == 45, len(ledger)
assert len(plan) == 15, len(plan)
assert len(mapping) == 15, len(mapping)

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
    "work_package": "2026-10-25-2010tianzibing-procedures-batch-e",
    "goal": "处理田自秉《中国工艺美术史》2010 册前 15 个 procedure 候选：8 个新建、7 个更新；无 no_delta、无 rejected。",
    "status": "applied",
    "date": DATE,
    "inputs": {
        "candidate_index": {
            "path": "06-runtime\\state\\candidate-index.jsonl",
            "rows_before": 5339,
            "sha256_before": "sha256:813de48a1d67aecd6cce88af36649be59d3cf6cf652424e582b4001c8d02c28a",
            "sha256_scope": "CRLF→LF 归一后",
            "counts_before": {
                "applied": 721,
                "needs_evidence": 3774,
                "no_delta": 43,
                "rejected": 801,
            },
        },
        "source": {
            "doc_id": "2010-tianzibing-zhongguo-gongyi-meishushi",
            "file": "03基础书籍-md文档/中国工艺美术史（修订本）_田自秉_2010_东方出版中心.md",
            "spans": ["L459", "L494", "L419-L421, L746", "L746", "L833-L835", "L913-L915", "L1164", "L1535", "L1537", "L1590", "L1780-L1782", "L1802", "L1804", "L1806", "L1808"],
        },
    },
    "method": {
        "rules": [
            "procedure 候选按实体而非 slug 对账：先与既有 procedure KU 的标题与内容对齐，再定 create／update。",
            "工序条目只写来源所记材料、步骤、工具、产量与实例；来源未载的工序参数写入证据边界。",
            "同一段落中的相邻工序按实体拆分：可独立成工序的另立条目，属于既有条目的补写则判 update。",
            "原文异体、同名异指与两册表述差异照录并注明，不据来源外材料裁定。",
        ],
        "source_policy": "02-sources 只读；本批写 04-knowledge/units/procedures，8 条新建、7 条更新。",
    },
    "outputs": {
        "apply_plan": {
            "path": "06-runtime\\automation\\2026-10-25-2010tianzibing-procedures-batch-e\\apply-plan.jsonl",
            "rows": 15,
            "create": 8,
            "update": 7,
        },
        "ledger": {
            "path": "06-runtime\\automation\\2026-10-25-2010tianzibing-procedures-batch-e\\candidate-decision-ledger.jsonl",
            "rows": 45,
            "candidates": 15,
            "applied": 15,
            "no_delta": 0,
            "rejected": 0,
        },
        "canonical_mapping": {
            "path": "06-runtime\\automation\\2026-10-25-2010tianzibing-procedures-batch-e\\canonical-mapping.json",
            "entries": 15,
        },
    },
    "verification": {"status": "pending"},
}

(BATCH / "manifest.json").write_bytes(
    (json.dumps(manifest, ensure_ascii=False, indent=2) + "\n").encode("utf-8")
)
print("ledger", len(ledger), "plan", len(plan), "mapping", len(mapping))
