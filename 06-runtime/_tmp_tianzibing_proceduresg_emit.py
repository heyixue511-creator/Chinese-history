# -*- coding: utf-8 -*-
"""Emit ledger, apply-plan, canonical mapping and manifest for Tian Zibing procedure batch G."""
import hashlib
import json
from pathlib import Path

import yaml

ROOT = Path(".")
BATCH = Path("06-runtime/automation/2026-10-25-2010tianzibing-procedures-batch-g")
BATCH.mkdir(parents=True, exist_ok=True)
PREFIX = "2010-tianzibing-zhongguo-gongyi-meishushi:"
DATE = "2026-10-25"

CREATES = [
    ("cand-09-65", "muye-jianzhi-tiehua", "木叶与剪纸贴花", "ceramic_technique", "宋代",
     "吉州窑在瓷胎上粘贴木叶与剪纸后施釉烧成，形成独创花纹；黑釉玳瑁斑与洒釉"),
    ("cand-09-97", "ci-xiu-hua", "瓷绣花", "ceramic_technique", "宋代",
     "用针刺出花纹，与刻花、印花、画花并列构成宋瓷主要装饰方法"),
    ("cand-10-04", "die-shao", "叠烧", "ceramic_technique", "金代",
     "器内底刮去一圈釉，另一器皿足置于无釉圈内叠装烧制，增产降本"),
    ("cand-10-09", "hualuo-zhiji", "花罗织机与织造", "textile_technique", "宋代",
     "斫刀代投杼与打纬、另挂绞综脚踏提花，织出实地亮花与亮地暗花"),
    ("cand-10-13", "yin-jing", "印经", "textile_technique", "西夏",
     "经线分段包扎染色后织造，织物呈直向参差彩色斑纹；茂花闪色锦实例"),
    ("cand-10-16", "nian-ya", "碾轧", "textile_technique", "宋代",
     "织物经浆桶浸泡捣杵后碾轧，或未下机涂浆再碾轧，达到光平洁满"),
    ("cand-10-69", "nianjin-pianjin", "捻金与片金", "textile_technique", "元代",
     "捻金以薄金片缠线捻成金线，片金以薄金片切条织入锦中"),
    ("cand-11-03", "juan-su-tai-gu-hei-guang", "卷素胎骨与黑光", "lacquerware_technique", "元代",
     "脆松薄片旋床胶粘成卷素胎骨，经梢当、胶漆布、粗中细灰、糙漆与黑光"),
    ("cand-11-50", "jingtailan-zhizuo", "景泰蓝制作七过程", "metalworking_technique", "明代",
     "制胎、掐丝、烧焊、点蓝、烧蓝、磨光、镀金七过程"),
    ("cand-11-65", "cuanbian", "攒边", "woodworking_technique", "明代",
     "四边 45 度格角榫攒起，中心板出榫装入四边通槽，兼顾加固、伸缩与美观"),
    ("cand-12-45", "shua-yin-fa", "刷印法", "textile_technique", "清代",
     "木板刻花卉人物鸟兽蒙布搓抹染色，得华彩如绘的彩印花布"),
    ("cand-12-58", "tiehua-zhizuo", "铁画制作", "metalworking_technique", "清代",
     "低碳钢依画稿经剪花、锻打、焊接、退火、烘漆制成铁画"),
    ("cand-12-89", "taoliao", "套料", "glassmaking_technique", "清代",
     "几种不同色彩原料套烧后磨出花纹，套外为花纹色、套内为地色"),
    ("cand-13-55", "yudiao-taocai-qiaose", "玉雕套裁与巧色", "stoneworking_technique", "新中国",
     "套裁利用余料再刻部件，巧色依玉石色泽因材施艺；制作过程即设计过程"),
    ("cand-13-56", "zhubian-yishu-jiagong", "竹编艺术加工方法", "bamboo_weaving_technique", "新中国",
     "编织、车花、拼花、穿珠、翻簧五法，辅以刻花、烫花、彩漆"),
]

UPDATES = [
    ("cand-10-33", "lost-wax-casting", "失蜡法", "metalworking_technique", "宋代记载",
     "补入田自秉 L3849 所引赵希鹄《洞天清禄集》铜器蜡模铸造程序"),
    ("cand-12-44", "lan-yinhua-bu", "蓝印花布", "textile_technique", "汉代至清代",
     "补入田自秉 L4687 所引康熙《松江府志》《长洲县志》刮印花工序、名称与清代产地"),
]

BEFORE = json.loads(Path("06-runtime/_tmp_pre_g_hashes.json").read_text(encoding="utf-8"))


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

assert len(ledger) == 51, len(ledger)
assert len(plan) == 17, len(plan)
assert len(mapping) == 17, len(mapping)

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
    "work_package": "2026-10-25-2010tianzibing-procedures-batch-g",
    "goal": "处理田自秉《中国工艺美术史》2010 册第 31—47 个 procedure 候选：15 个新建、2 个更新；无 no_delta、无 rejected。",
    "status": "applied",
    "date": DATE,
    "inputs": {
        "candidate_index": {
            "path": "06-runtime\\state\\candidate-index.jsonl",
            "rows_before": 5339,
            "sha256_before": "sha256:8fd6ad4475d98fe25a0b937dc5378bce97815d59774f9ee5a99b5d15291e86ff",
            "sha256_scope": "CRLF→LF 归一后",
            "counts_before": {
                "applied": 751,
                "needs_evidence": 3744,
                "no_delta": 43,
                "rejected": 801,
            },
        },
        "source": {
            "doc_id": "2010-tianzibing-zhongguo-gongyi-meishushi",
            "file": "03基础书籍-md文档/中国工艺美术史（修订本）_田自秉_2010_东方出版中心.md",
            "spans": [
                "L3642", "L3674", "L3739", "L3769-L3773", "L3783-L3790",
                "L3810", "L3849", "L4042-L4046", "L4136", "L4377",
                "L4441", "L4687", "L4733-L4735", "L4848-L4855",
                "L5228-L5232", "L5288-L5290",
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
        "source_policy": "02-sources 只读；本批写 04-knowledge/units/procedures，15 条新建、2 条更新。",
    },
    "outputs": {
        "apply_plan": {
            "path": "06-runtime\\automation\\2026-10-25-2010tianzibing-procedures-batch-g\\apply-plan.jsonl",
            "rows": 17,
            "create": 15,
            "update": 2,
        },
        "ledger": {
            "path": "06-runtime\\automation\\2026-10-25-2010tianzibing-procedures-batch-g\\candidate-decision-ledger.jsonl",
            "rows": 51,
            "candidates": 17,
            "applied": 17,
            "no_delta": 0,
            "rejected": 0,
        },
        "canonical_mapping": {
            "path": "06-runtime\\automation\\2026-10-25-2010tianzibing-procedures-batch-g\\canonical-mapping.json",
            "entries": 17,
        },
    },
    "verification": {"status": "pending"},
}

(BATCH / "manifest.json").write_bytes(
    (json.dumps(manifest, ensure_ascii=False, indent=2) + "\n").encode("utf-8")
)
print("ledger", len(ledger), "plan", len(plan), "mapping", len(mapping))
