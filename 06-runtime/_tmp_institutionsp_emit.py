import hashlib
import json
import pathlib
import subprocess

ROOT = pathlib.Path(__file__).resolve().parents[1]
PKG = ROOT / "06-runtime" / "automation" / "2026-10-25-2009zhaonong-institutions-batch-p"
PKG.mkdir(parents=True, exist_ok=True)
DOC = "2009-zhaonong-zhongguo-yishu-shejishi"
DATE = "2026-10-25"


def fp_bytes(raw: bytes) -> dict:
    text = raw.decode("utf-8").replace("\r\n", "\n").replace("\r", "\n")
    data = text.encode("utf-8")
    return {
        "sha256": "sha256:" + hashlib.sha256(data).hexdigest(),
        "bytes": len(data),
        "lines": text.count("\n"),
    }


def fp(path: pathlib.Path) -> dict:
    return fp_bytes(path.read_bytes())


def cid(n: str) -> str:
    return f"{DOC}:{n}"


creates = [
    (
        "cand-02-59",
        "典丝",
        "04-knowledge/units/institutions/dian-si.md",
        "新建government_office：周代《考工记》所记丝织职官“典丝”，同段有筐人、慌人、染人、典妇功组织丝织生产；来源只列职名，未给员额、隶属与职掌细目",
    ),
    (
        "cand-03-23",
        "大乐司",
        "04-knowledge/units/institutions/da-yuesi.md",
        "新建government_office：西周专门音乐机构，属“大乐司”，来源称为最早的音乐教育管理部门；周代乐器约70种，《诗经》提及29种",
    ),
    (
        "cand-04-116",
        "石渠阁",
        "04-knowledge/units/institutions/shiquge.md",
        "新建government_office：汉王朝石渠阁，珍藏秦王朝留下的大量地图和书籍；来源仅一句，未给建置、隶属、员额与藏书目录",
    ),
    (
        "cand-04-73",
        "上林三官",
        "04-knowledge/units/institutions/shanglin-sanguan.md",
        "新建government_office：汉武帝改革货币、禁止民间铸钱所设“上林三官”铸币机构，罢半两钱行五铢钱；来源未释三官具体所指",
    ),
    (
        "cand-05-22",
        "尚方（尚方令）",
        "04-knowledge/units/institutions/shangfang.md",
        "新建government_office：东汉尚方，蔡伦为汉和帝时期尚方令，管理皇家工场、监制各种器械；永元九年监作秘剑及诸器械，莫不精工坚密",
    ),
    (
        "cand-08-39",
        "交子务",
        "04-knowledge/units/institutions/jiaoziwu.md",
        "新建government_office：宋仁宗天圣元年（1023）在益州设置交子务发行纸币，用铁币作储备金；来源另记私商交子、防伪印制与钱引改名",
    ),
    (
        "cand-08-64",
        "市舶司",
        "04-knowledge/units/institutions/shibosi.md",
        "新建government_office：北宋政府在泉州港设置市舶司，管理船政和贸易；来源未给设置年份、隶属、员额、税则与查验制度",
    ),
    (
        "cand-09-26",
        "驿站",
        "04-knowledge/units/institutions/yuan-dai-yizhan.md",
        "新建government_office：元代驿站网络，每隔70里设驿站，全国约1500个，驿站之间10—20里设急递铺；朝令夕至，元末许多驿站瘫痪",
    ),
    (
        "cand-09-61",
        "文思院（西夏）",
        "04-knowledge/units/institutions/xi-xia-wensiyuan.md",
        "新建government_office：西夏政府设文思院，专门管理制作金、银、玉、犀等器具；与唐宋同名文思院分条，不混为同一机构",
    ),
]

updates = []

no_deltas = [
    (
        "cand-05-105",
        "汉代长安官营纺织业",
        "04-knowledge/units/institutions/han-dai-guan-ying-sizhi-zuofang.md",
        "既有 KU 已覆盖候选语义：长安设东、西织室，织作缯帛和文绣之服；官作坊精美丝麻织物供皇室、赏赐与对外贸易。2009 L3038 的“长安有专门生产服饰的纺织业官营结构”与 L1405-L1416 同书同段网络一致，无新增机构名或制度细节，判 no_delta",
    ),
]

order = [
    "cand-02-59", "cand-03-23", "cand-04-116", "cand-04-73", "cand-05-105",
    "cand-05-22", "cand-08-39", "cand-08-64", "cand-09-26", "cand-09-61",
]
assert len(order) == 10

create_map = {c[0]: c for c in creates}
update_map = {u[0]: u for u in updates}
nod_map = {n[0]: n for n in no_deltas}

ledger = []
for n in order:
    if n in nod_map:
        _, title, target, note = nod_map[n]
        ledger.append({
            "candidate_id": cid(n), "expected_state": "needs_evidence", "state": "ready_for_review",
            "decision": {"status": "pending", "reason": f"已完成语义复读：既有 {target} 可完整承载，提交 no_delta", "decided_by": "Agent", "decided_at": DATE},
            "updated_at": DATE,
        })
        ledger.append({
            "candidate_id": cid(n), "expected_state": "ready_for_review", "state": "approved",
            "decision": {"status": "approved", "reason": f"canonical 候选语义复读完成，批准判 no_delta（{target}）", "decided_by": "Agent", "decided_at": DATE},
            "updated_at": DATE,
        })
        ledger.append({
            "candidate_id": cid(n), "expected_state": "approved", "state": "no_delta",
            "decision": {"status": "approved", "reason": f"既有 {target} 已完整覆盖候选内容，无需写回；判定 no_delta", "decided_by": "Agent", "decided_at": DATE},
            "updated_at": DATE, "target_ref": target,
        })
        continue
    if n in create_map:
        _, title, target, note = create_map[n]
        verb = "新建"
    else:
        _, title, target, note = update_map[n]
        verb = "更新"
    ledger.append({
        "candidate_id": cid(n), "expected_state": "needs_evidence", "state": "ready_for_review",
        "decision": {"status": "pending", "reason": f"已完成语义复读：{verb} {target}", "decided_by": "Agent", "decided_at": DATE},
        "updated_at": DATE,
    })
    ledger.append({
        "candidate_id": cid(n), "expected_state": "ready_for_review", "state": "approved",
        "decision": {"status": "approved", "reason": f"canonical 候选语义复读完成，批准{verb} {target}", "decided_by": "Agent", "decided_at": DATE},
        "updated_at": DATE,
    })
    ledger.append({
        "candidate_id": cid(n), "expected_state": "approved", "state": "applied",
        "decision": {"status": "approved", "reason": f"已判定 applied：{verb} {target}", "decided_by": "Agent", "decided_at": DATE},
        "updated_at": DATE, "target_ref": target,
    })

plan = []
for n, title, target, note in creates:
    p = ROOT / target
    f = fp(p)
    plan.append({
        "action": "create", "target_ref": target, "candidate_id": cid(n),
        "entity": title, "before": None, "after_sha256": f["sha256"], "bytes": f["bytes"],
        "lines": f["lines"], "note": note,
    })

mapping = []
for n, title, target, note in creates:
    mapping.append({
        "entity": title, "target_ref": target, "action": "create",
        "canonical_candidate": cid(n), "merged_candidates": [],
    })
for n, title, target, note in no_deltas:
    mapping.append({
        "entity": title, "target_ref": target, "action": "no_delta",
        "canonical_candidate": cid(n), "merged_candidates": [], "note": note,
    })

with (PKG / "candidate-decision-ledger.jsonl").open("w", encoding="utf-8", newline="\n") as f:
    for row in ledger:
        f.write(json.dumps(row, ensure_ascii=False) + "\n")
with (PKG / "apply-plan.jsonl").open("w", encoding="utf-8", newline="\n") as f:
    for row in plan:
        f.write(json.dumps(row, ensure_ascii=False) + "\n")
(PKG / "canonical-mapping.json").write_text(json.dumps(mapping, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

manifest = {
    "work_package": PKG.name,
    "goal": "处理赵农《中国艺术设计史》2009 册 institution 候选 10 个：9 个新建、0 个更新、1 个 no_delta。",
    "status": "applied",
    "date": DATE,
    "inputs": {
        "candidate_index": {
            "path": "06-runtime\\state\\candidate-index.jsonl",
            "rows_before": 5339,
            "sha256_before": "sha256:701e4dace6ff5b09abc52578683f7e384f3834f695e5410f962ce74ac2bf4a9c",
            "sha256_scope": "CRLF→LF 归一后",
            "counts_before": {"applied": 848, "needs_evidence": 3629, "no_delta": 55, "rejected": 807},
        },
        "source": {
            "doc_id": DOC,
            "file": "03基础书籍-md文档/中国艺术设计史_赵农_2009_高等教育出版社.md",
            "spans": ["L1435-L1456", "L1578-L1614", "L2618-L2644", "L2841-L2890", "L3038", "L3123-L3141", "L5258-L5280", "L5338-L5355", "L6102-L6115", "L6394-L6422"],
        },
    },
    "method": {
        "rules": [
            "institution 候选按实体而非 slug 对账：先与既有 institution KU 的标题、别名和正文对齐，再定 create／update／no_delta／rejected。",
            "候选“典丝”按周代丝织职官立目：典丝与筐人、慌人、典妇功同段，染人另有既有 KU；来源“慌人”用字照录，不据传世本改写。",
            "候选“大乐司”只登记西周音乐机构名、时代与“最早的音乐教育管理部门”定位，不写周代礼乐制度通史，也不与后世乐署直接等同。",
            "候选“石渠阁”只登记汉代皇家藏书与档案职能：珍藏秦王朝留下的大量地图和书籍；不并入后世石渠阁会议等来源外叙述。",
            "候选“上林三官”只登记汉武帝货币改革所设铸币机构与“罢半两钱，行五铢钱”关系；来源未释“三官”具体所指，不猜作三个官署。",
            "候选“汉代长安官营纺织业”判 no_delta：既有 han-dai-guan-ying-sizhi-zuofang.md 已覆盖长安东、西织室及官作坊产品流向；2009 L3038 无新增机构名或制度细节。",
            "候选“尚方”以皇家工场立目：蔡伦为汉和帝时期尚方令，管理皇家工场、监制器械；永元九年监作秘剑及诸器械；不把蔡伦个人造纸成就全部归为机构成就。",
            "候选“交子务”按北宋纸币发行机构立目：天圣元年（1023）益州设务、铁币储备、交子流通范围；私商交子只作制度背景，不归为交子务职掌。",
            "候选“市舶司”按泉州港海外贸易与船政管理机构立目：只写“管理船政和贸易”，不推定其他港口设司，不补税则与抽解比例。",
            "候选“驿站”按元代驿传网络立目：70 里一驿、约 1500 个、10—20 里急递铺、朝令夕至、元末瘫痪；不与急递铺混为同一层级。",
            "候选“文思院（西夏）”与唐宋同名文思院分条：西夏政府设文思院管理金、银、玉、犀器具；不把三者混为同一机构，不把出土金银器全部归为文思院产品。",
            "03基础书籍-md文档只读；本批写 04-knowledge/units/institutions，9 条新建、0 条更新、1 条 no_delta。",
        ],
    },
    "outputs": {
        "apply_plan": {"path": f"06-runtime\\automation\\{PKG.name}\\apply-plan.jsonl", "rows": len(plan), "create": len(creates), "update": len(updates)},
        "ledger": {"path": f"06-runtime\\automation\\{PKG.name}\\candidate-decision-ledger.jsonl", "rows": len(ledger), "candidates": len(order), "applied": len(creates) + len(updates), "no_delta": len(no_deltas), "rejected": 0},
        "canonical_mapping": {"path": f"06-runtime\\automation\\{PKG.name}\\canonical-mapping.json", "entries": len(mapping), "merged_candidates": []},
    },
    "state_after": {},
}
(PKG / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

assert len(ledger) == 30, len(ledger)
assert len(plan) == 9, len(plan)
assert len(mapping) == 10, len(mapping)
print(json.dumps({"ledger": len(ledger), "plan": len(plan), "mapping": len(mapping), "creates": len(creates), "updates": len(updates), "no_delta": len(no_deltas)}, ensure_ascii=False))
