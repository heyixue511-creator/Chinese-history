# -*- coding: utf-8 -*-
"""Emit ledger, apply-plan, canonical mapping and manifest for Xia Yanjing 2016 procedure batch J."""
import hashlib
import json
from pathlib import Path

import yaml

ROOT = Path(".")
BATCH = Path("06-runtime/automation/2026-10-25-2016xiayanjing-procedures-batch-j")
BATCH.mkdir(parents=True, exist_ok=True)
PREFIX = "2016-xiayanjing-zhongguo-yishu-shejishi-upgrade:"
DATE = "2026-10-25"

CREATES = [
    ("cand-05-30", "erci-shaocheng-fa", "二次烧成法", "ceramic_technique", "二次烧成法",
     "唐三彩胎体 1000—1100℃ 素烧、冷却施釉、850—950℃ 釉烧；人物烧后开脸", []),
    ("cand-06-18", "zhiding-zhishao", "支钉支烧法", "ceramic_technique", "支钉支烧法",
     "山字形支钉置于圆形垫饼，承托器物入匣钵烧造；晚唐秘色瓷至宋汝、官、哥窑", [PREFIX + "cand-05-31"]),
    ("cand-05-42", "jiezhi-yinhua", "介质印花", "textile_technique", "介质印花",
     "以碱剂或媒染剂为助剂，经浸染、水洗或酸碱中和显白花、绛地白花", []),
    ("cand-06-43", "song-dai-jianzhu-caihua", "宋代建筑彩画", "construction_technique", "宋代建筑彩画",
     "《营造法式》六类彩画，衬地、衬色、细色、贴金四步，梁额如意头与枋心、退晕对晕", []),
    ("cand-06-45", "pinhe-liang", "拼合梁", "woodworking_technique", "拼合梁",
     "小料拼大料，大梁加缴背补足断面并减轻负重；李彬墓肩抬轿椅实例", []),
    ("cand-07-100", "jintong-fa", "浸铜法", "metalworking_technique", "浸铜法",
     "宋元浸铜法，来源称世界最早浸铜生产铜、水法冶金起源；无工序细节", []),
    ("cand-07-54", "tiaohua-jieben", "挑花结本", "textile_technique", "挑花结本",
     "按画稿以经纬线挑制花本并编结上机；龙袍花本 60 千克、121370 根、166 米以上", []),
    ("cand-07-55", "chuai-ran", "踹染", "textile_technique", "踹染",
     "足踏四字形大石左右滚动，使漂染棉布紧密光滑；清代苏州踹坊六七百家", []),
    ("cand-08-83", "chuiyou-fa", "吹釉法", "ceramic_technique", "吹釉法",
     "径寸竹筒口蒙细纱蘸釉汁吹于坯上若干遍，均匀无损坏", []),
    ("cand-09-79", "fengxiang-nisu", "凤翔泥塑", "sculpture_technique", "凤翔泥塑",
     "选土、和泥、制坯、阴干、粉洗、描线、上色、涂油等十多道工序；品种上千", []),
]

UPDATES = [
    ("cand-06-49", "die-shao", "叠烧", "ceramic_technique", "叠烧",
     "增夏燕靖 2016 砂圈叠烧法：施釉入窑前内底刮釉露胎、叠置器足避免黏结、多为日用瓷无纹饰"),
    ("cand-07-52", "nianjin-pianjin", "捻金与片金", "textile_technique", "捻金与片金",
     "增夏燕靖 2016 盐湖一号墓辫线袄、片金与捻金的经纬显花结构、0.5 毫米皮子与纹样"),
    ("cand-07-87", "huozi-yinshua", "活字印刷", "printing_technique", "活字印刷",
     "增夏燕靖 2016 《大德旌德县志》书名、3 万多个木字、不到一月百部、敦煌维吾尔族木活字与转轮排字法"),
    ("cand-08-84", "duanban-taoyin", "短版套印", "printing_technique", "短版套印",
     "增夏燕靖 2016 数块至数十块版、逐色套印或叠印、南京中心、1626《萝轩变古笺谱》最早短版拱花印本；记“饱版”异写"),
]

NO_DELTA = [
    ("cand-05-55", "chuihui-fa", "吹灰法",
     "2016 L2794 与 2009 L2227 及既有 KU 所据田自秉文同文，已记唐代炼银渣块、吹灰法提高纯度与回收率，无新增语义"),
    ("cand-06-26", "nian-ya", "碾轧",
     "2016 L3258 所述加拈与碾轧两法，已被既有 KU 据田自秉 2010 完整收录（浆液后下机碾轧、光平洁满），2016 更简，无新增语义"),
    ("cand-07-50", "blue-and-white-porcelain", "青花瓷",
     "既有 term KU 已逐字收录 2016 L3663 的青花定义（氧化钴、罩透明釉、1300℃ 还原焰一次烧成），无工序增量"),
    ("cand-07-51", "youlihong", "釉里红",
     "既有 term KU 已逐字收录 2016 L3720 的线绘、拔白、涂绘三法与飞红判断，无新增语义"),
]

REJECTS = [
    ("cand-08-86", "换棉与出机",
     "所记为包买主购销方式与商业资本对家庭棉纺织生产的控制，属经济组织与劳动关系，不是可复现的工艺工序；不建 procedure KU。若后续立目，应归 institution 或相关经济史条目"),
    ("cand-10-14", "广告设计信息语意传达",
     "所记为广告设计的信息语意传达框架（策划、设计、表现、受众、效果评估），属设计理论与方法，不是可复现工序；不建 procedure KU"),
]

BEFORE = json.loads(Path("06-runtime/_tmp_pre_j_hashes.json").read_text(encoding="utf-8"))


def fingerprint(path: Path):
    data = path.read_bytes()
    text = data.decode("utf-8").replace("\r\n", "\n")
    payload = text.encode("utf-8")
    return {
        "sha256": "sha256:" + hashlib.sha256(payload).hexdigest(),
        "bytes": len(payload),
        "lines": text.count("\n"),
    }


def ledger_rows(cid, target, kind, terminal, reason_terminal=None):
    rows = []
    for expected, state, reason in [
        ("needs_evidence", "ready_for_review", f"已完成语义复读：{kind} {target}"),
        ("ready_for_review", "approved", f"canonical 候选语义复读完成，批准{kind} {target}"),
        ("approved", terminal, reason_terminal or f"已判定 {terminal}：{kind} {target}"),
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
        if state == terminal:
            row["target_ref"] = target
        rows.append(row)
    return rows


ledger = []
plan = []
mapping = []

for cand, slug, title, sub, entity, note, merged in CREATES:
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
    if fm.get("source_count") != 2 or len(fm.get("sources") or []) != 2:
        raise SystemExit(f"source_count mismatch {target}")
    fp = fingerprint(path)
    ledger.extend(ledger_rows(cid, target, "新建", "applied"))
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
        "merged_candidates": merged,
    })
    for mid in merged:
        ledger.extend(ledger_rows(
            mid, target, "并入", "applied",
            f"并入 {cid} 同一工艺实体：支钉撑烧法即支钉支烧法，统一以支钉支烧法立目",
        ))

for cand, slug, title, sub, entity, note in UPDATES:
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
    ledger.extend(ledger_rows(cid, target, "更新", "applied"))
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

for cand, slug, title, note in NO_DELTA:
    cid = PREFIX + cand
    target = f"04-knowledge/units/{'terms' if slug in {'blue-and-white-porcelain', 'youlihong'} else 'procedures'}/{slug}.md"
    path = ROOT / target
    if not path.exists():
        raise SystemExit(f"missing {target}")
    fm = yaml.safe_load(path.read_text(encoding="utf-8").split("---\n", 2)[1])
    if title not in fm.get("title", ""):
        raise SystemExit(f"title mismatch {target}: {fm.get('title')}")
    ledger.extend(ledger_rows(cid, target, "判定 no_delta（既有 KU 可完整承载）", "no_delta"))
    mapping.append({
        "entity": fm.get("title", title),
        "target_ref": target,
        "action": "no_delta",
        "canonical_candidate": cid,
        "merged_candidates": [],
        "note": note,
    })

for cand, title, reason in REJECTS:
    cid = PREFIX + cand
    ledger.append({
        "candidate_id": cid,
        "expected_state": "needs_evidence",
        "state": "rejected",
        "decision": {
            "status": "rejected",
            "reason": f"拒绝：{title}。{reason}",
            "decided_by": "Agent",
            "decided_at": DATE,
        },
        "updated_at": DATE,
    })

assert len(ledger) == 59, len(ledger)
assert len(plan) == 14, len(plan)
assert len(mapping) == 18, len(mapping)

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
    "work_package": "2026-10-25-2016xiayanjing-procedures-batch-j",
    "goal": "处理夏燕靖《中国艺术设计史（升级版）》2016 册剩余 21 个 procedure 候选：10 个新建、4 个更新、4 个 no_delta、2 个 rejected；其中 cand-05-31 并入 cand-06-18。",
    "status": "applied",
    "date": DATE,
    "inputs": {
        "candidate_index": {
            "path": "06-runtime\\state\\candidate-index.jsonl",
            "rows_before": 5339,
            "sha256_before": "sha256:b365aa4ab33c2b82b6fc23d1130c436ee2523eb9412fd39604cec3e4a00ad38c",
            "sha256_scope": "CRLF→LF 归一后",
            "counts_before": {
                "applied": 789,
                "needs_evidence": 3703,
                "no_delta": 46,
                "rejected": 801,
            },
        },
        "source": {
            "doc_id": "2016-xiayanjing-zhongguo-yishu-shejishi-upgrade",
            "file": "03基础书籍-md文档/中国艺术设计史（升级版）_夏燕靖_2016_上海人民美术出版社.md",
            "spans": [
                "L2600-L2606", "L2607-L2627", "L2709-L2714", "L2790-L2795",
                "L3152-L3155", "L3254-L3259", "L3407-L3426", "L3427-L3434",
                "L3452-L3469", "L3661-L3664", "L3718-L3727", "L3728-L3745",
                "L3851-L3870", "L4025", "L4173-L4188", "L4201-L4210",
                "L4341-L4367", "L4619-L4656", "L4783-L4813", "L5346-L5385",
                "L5480-L5501",
            ],
        },
    },
    "method": {
        "rules": [
            "procedure 候选按实体而非 slug 对账：先与既有 procedure KU 的标题、别名和正文对齐，再定 create／update／no_delta／rejected。",
            "夏燕靖 2016《中国艺术设计史（升级版）》与 2009《中国设计史》为同一作者前后版本；2016 段落与既有 KU 所据 2009 段落语义一致时判 no_delta，不以新版年份充当新增证据。",
            "既有 term KU 已完整承载工艺定义与分类时，procedure 候选判 no_delta，不重复立条。",
            "非可复现工序的对象（包买主购销方式、广告语意传达框架）判 rejected，单行记录，不进入 mapping。",
            "同一工艺的两个候选（支钉撑烧法与支钉支烧法）合并为一个实体，保留 merged_candidates 映射。",
        ],
        "source_policy": "03基础书籍-md文档只读；本批写 04-knowledge/units/procedures，10 条新建、4 条更新。",
    },
    "outputs": {
        "apply_plan": {
            "path": "06-runtime\\automation\\2026-10-25-2016xiayanjing-procedures-batch-j\\apply-plan.jsonl",
            "rows": 14,
            "create": 10,
            "update": 4,
        },
        "ledger": {
            "path": "06-runtime\\automation\\2026-10-25-2016xiayanjing-procedures-batch-j\\candidate-decision-ledger.jsonl",
            "rows": 59,
            "candidates": 21,
            "applied": 15,
            "no_delta": 4,
            "rejected": 2,
        },
        "canonical_mapping": {
            "path": "06-runtime\\automation\\2026-10-25-2016xiayanjing-procedures-batch-j\\canonical-mapping.json",
            "entries": 18,
            "merged_candidates": [PREFIX + "cand-05-31"],
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
