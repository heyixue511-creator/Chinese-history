# -*- coding: utf-8 -*-
"""Emit ledger, apply-plan, canonical mapping and manifest for Tian Zibing procedure batch F."""
import hashlib
import json
from pathlib import Path

import yaml

ROOT = Path(".")
BATCH = Path("06-runtime/automation/2026-10-25-2010tianzibing-procedures-batch-f")
BATCH.mkdir(parents=True, exist_ok=True)
PREFIX = "2010-tianzibing-zhongguo-gongyi-meishushi:"
DATE = "2026-10-25"

CREATES = [
    ("cand-06-46", "mosu-jiehe-zhi-taoyong", "模塑结合制陶俑", "ceramic_technique", "秦代", "陶模初胎、覆细泥、刻划着彩，头身腿分模粘接，先烧后接或先接后烧"),
    ("cand-07-22", "qiqi-mutai-san-zuofa", "漆器木胎三作法", "lacquerware_technique", "汉代", "木胎旋制、剜削、卷制三法及其适用器形与胎体轻重"),
    ("cand-07-42", "pingmian-tidi-fa", "平面剔地法", "sculpture_technique", "东汉", "保留图像石面、剔去空余部分；武氏祠与沂南加刻细线"),
    ("cand-07-61", "liuchao-qingci-zhuangshi-liufa", "六朝青瓷装饰六法", "ceramic_technique", "六朝", "压印、刻花、堆贴、塑饰、雕镂、釉彩六法及褐彩演变"),
    ("cand-08-10", "bian-xiu", "辫绣", "textile_technique", "战国至清", "辫绣即锁子绣，开口填充花纹、闭口表现线条，历代沿用至苏绣拉梭子"),
    ("cand-08-61", "jian-yin", "碱印", "textile_technique", "唐代", "碱剂脱胶与染料酸碱性差异形成浅地深花或深地浅花，纸板镂花套色"),
    ("cand-08-62", "ta-yin-yinhua", "拓印（印花）", "textile_technique", "唐代", "刻印花模涂色盖印，为唐代印染中唯一的非防染直接印花"),
    ("cand-08-65", "yun-jian-xiu", "纭裥绣", "textile_technique", "唐代", "又称退晕绣或抢针绣，以深浅色阶表现对象"),
    ("cand-09-24", "bo-lou", "拨镂", "ivory_carving_technique", "唐代", "象牙染红绿诸色后刻花，或在刻纹上涂色，制红牙、绿牙拨镂尺"),
    ("cand-09-50", "hua-hua", "画花", "ceramic_technique", "宋代", "磁州窑系白釉画黑花、黑釉画褐花（铁锈花），开后世花绘装饰"),
    ("cand-09-51", "diao-you", "雕釉", "ceramic_technique", "宋代", "先施白釉或黑釉，剔刻花纹以外空间露出瓷胎，形成胎釉对比"),
]

UPDATES = [
    ("cand-07-19", "han-dai-qiqi-zhizuo-fengong", "汉代漆器制作分工", "lacquer_technique", "汉代",
     "补入田自秉乐浪漆器铭文十一工种、各工职掌、洪工存疑与发达期年代"),
    ("cand-08-59", "la-ran", "蜡染", "textile_technique", "秦汉至现代",
     "补入田自秉唐代蜡缬工序、宋代瑶族夹板灌蜡法与近现代苗族布依族蜡染"),
    ("cand-09-18", "quan-die-fa", "圈叠法", "lacquerware_technique", "唐代至宋代",
     "补入田自秉木条圈卷法：薄木条卷成器形、外裱麻布、涂漆，及监利福田唐墓实例"),
    ("cand-09-40", "fu-shao-fa", "覆烧法（定窑与景德镇）", "ceramic_technique", "北宋中期",
     "补入田自秉定瓷薄胎覆烧原因、涩边铜金银镶口与定器有芒另建汝窑"),
]

BEFORE = json.loads(Path("06-runtime/_tmp_pre_f_hashes.json").read_text(encoding="utf-8"))


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
    "work_package": "2026-10-25-2010tianzibing-procedures-batch-f",
    "goal": "处理田自秉《中国工艺美术史》2010 册第 16—30 个 procedure 候选：11 个新建、4 个更新；无 no_delta、无 rejected。",
    "status": "applied",
    "date": DATE,
    "inputs": {
        "candidate_index": {
            "path": "06-runtime\\state\\candidate-index.jsonl",
            "rows_before": 5339,
            "sha256_before": "sha256:df8689e7eab91637112551608733ca0a085c2d6f66a1918d79136598edcaeef7",
            "sha256_scope": "CRLF→LF 归一后",
            "counts_before": {
                "applied": 736,
                "needs_evidence": 3759,
                "no_delta": 43,
                "rejected": 801,
            },
        },
        "source": {
            "doc_id": "2010-tianzibing-zhongguo-gongyi-meishushi",
            "file": "03基础书籍-md文档/中国工艺美术史（修订本）_田自秉_2010_东方出版中心.md",
            "spans": [
                "L2125-L2129", "L2565", "L2589", "L2617-L2641", "L2829-L2843",
                "L1970, L2537, L2931, L3274, L4655", "L3258, L3826, L5128",
                "L3262", "L3264", "L3274", "L3404", "L3440, L3456",
                "L3528, L3554", "L3601",
            ],
        },
    },
    "method": {
        "rules": [
            "procedure 候选按实体而非 slug 对账：先与既有 procedure KU 的标题与内容对齐，再定 create／update。",
            "工序条目只写来源所记材料、步骤、工具、产量与实例；来源未载的工序参数写入证据边界。",
            "同一段落中的相邻工序按实体拆分：可独立成工序的另立条目，属于既有条目的补写则判 update。",
            "原文异体、同名异指与两册表述差异照录并注明，不据来源外材料裁定。",
        ],
        "source_policy": "02-sources 只读；本批写 04-knowledge/units/procedures，11 条新建、4 条更新。",
    },
    "outputs": {
        "apply_plan": {
            "path": "06-runtime\\automation\\2026-10-25-2010tianzibing-procedures-batch-f\\apply-plan.jsonl",
            "rows": 15,
            "create": 11,
            "update": 4,
        },
        "ledger": {
            "path": "06-runtime\\automation\\2026-10-25-2010tianzibing-procedures-batch-f\\candidate-decision-ledger.jsonl",
            "rows": 45,
            "candidates": 15,
            "applied": 15,
            "no_delta": 0,
            "rejected": 0,
        },
        "canonical_mapping": {
            "path": "06-runtime\\automation\\2026-10-25-2010tianzibing-procedures-batch-f\\canonical-mapping.json",
            "entries": 15,
        },
    },
    "verification": {"status": "pending"},
}

(BATCH / "manifest.json").write_bytes(
    (json.dumps(manifest, ensure_ascii=False, indent=2) + "\n").encode("utf-8")
)
print("ledger", len(ledger), "plan", len(plan), "mapping", len(mapping))
