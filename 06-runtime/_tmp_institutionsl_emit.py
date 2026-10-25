import hashlib
import json
import pathlib
import subprocess

ROOT = pathlib.Path(__file__).resolve().parents[1]
PKG = ROOT / "06-runtime" / "automation" / "2026-10-25-2016xiayanjing-institutions-batch-l"
PKG.mkdir(parents=True, exist_ok=True)
DOC = "2016-xiayanjing-zhongguo-yishu-shejishi-upgrade"
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
        "cand-06-24",
        "宋代染织管理机构",
        "04-knowledge/units/institutions/song-dai-ranzhi-guanli-jigou.md",
        "新建government_office（机构群）：中央文思院、绫锦院、裁造院、文绣院，地方洛阳、真州、定州、青州、益州、苏州、杭州、润州、湖州派出机构；来源只给名称与网络范围",
    ),
    (
        "cand-06-56",
        "刻字司",
        "04-knowledge/units/institutions/kezisi.md",
        "新建government_office：西夏朝廷设刻字司专印书籍，佛经最多，兼刻文学、法律、医术、日历、卜筮、咒文；保存与宋同时的活字印本",
    ),
    (
        "cand-07-08",
        "建康路织染局",
        "04-knowledge/units/institutions/jiankanglu-zhiranju.md",
        "新建government_office：元代官营染织司局；《金陵新志》记东织染局管人匠3600户、织机154张、额造段匹4527段",
    ),
    (
        "cand-07-09",
        "太史局",
        "04-knowledge/units/institutions/taishiju.md",
        "新建government_office：1276年忽必烈设太史局编新历，王恂、郭守敬负责；1280年成授时历，郭守敬创制简仪、高表等17种仪器",
    ),
    (
        "cand-08-19",
        "荷兰东印度公司",
        "04-knowledge/units/institutions/dutch-east-india-company.md",
        "新建commercial_enterprise：1602—1682年贩运中国青花瓷1600万件以上；17世纪掌控中西贸易瓷；1602年捕获克拉克号使克拉克瓷得名",
    ),
    (
        "cand-08-21",
        "龙江船厂",
        "04-knowledge/units/institutions/longjiang-chuanchang.md",
        "新建government_office：明代南京官营造船厂；郑和宝船长150米、宽60米、9桅12帆；龙江船厂出土铁木宝船舵杆长11.07米",
    ),
    (
        "cand-08-25",
        "德昌花边庄",
        "04-knowledge/units/institutions/dechang-huabianzhuang.md",
        "新建craft_workshop：1900年宋传典、白玉章、袁景涛在青州城内集资开设；库尔德从意大利引进花边与原料，库师娘传艺",
    ),
    (
        "cand-08-26",
        "广东工艺局",
        "04-knowledge/units/institutions/guangdong-gongyiju.md",
        "新建government_office：光绪年间广东设工艺局主管工艺品生产；工艺品种经洋庄外销，潮绣经汕头口岸输往新马泰",
    ),
    (
        "cand-08-27",
        "恒沅轧花厂",
        "04-knowledge/units/institutions/hengyuan-zhahuachang.md",
        "新建commercial_enterprise：1895年陈悦周在上海用新式脚踏轧花机设厂；1915年改用柴油机；1936年上海三县70多家工场动力化",
    ),
]

updates = [
    (
        "cand-08-18",
        "御器厂（景德镇官窑）",
        "04-knowledge/units/institutions/yuqichang.md",
        "更新government_office：补2016 L4345明清景德镇官窑总述、明代官窑58座、康熙十九年后复兴、康雍乾黄金时代；标注该段未出现“御器厂”且58座不等同珠山一处",
    ),
]

no_deltas = [
    (
        "cand-06-84",
        "金代绫锦院",
        "04-knowledge/units/institutions/lingjinyuan.md",
        "既有 lingjinyuan KU 已含 2016 L3499 金代真定、平阳、太原、河间、怀州5处绫锦院及“掌织造常课匹段之事”，候选无新增内容",
    ),
]

order = [
    "cand-06-24", "cand-06-56", "cand-06-84", "cand-07-08", "cand-07-09",
    "cand-08-18", "cand-08-19", "cand-08-21", "cand-08-25", "cand-08-26", "cand-08-27",
]
assert len(order) == 11

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
for n, title, target, note in updates:
    p = ROOT / target
    before = fp_bytes(subprocess.check_output(["git", "show", f"HEAD:{target}"], cwd=ROOT))
    after = fp(p)
    plan.append({
        "action": "update", "target_ref": target, "candidate_id": cid(n), "entity": title,
        "before": before, "after_sha256": after["sha256"], "bytes": after["bytes"],
        "lines": after["lines"], "note": note,
    })

mapping = []
for n, title, target, note in creates:
    mapping.append({
        "entity": title, "target_ref": target, "action": "create",
        "canonical_candidate": cid(n), "merged_candidates": [],
    })
for n, title, target, note in updates:
    mapping.append({
        "entity": title, "target_ref": target, "action": "update",
        "canonical_candidate": cid(n), "merged_candidates": [],
        "note": "候选“景德镇官窑”以既有御器厂 KU 为落点；补入 2016 L4345 明清官窑总述，并保留“官窑”泛称与“御器厂”专名之间的口径差异。",
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
    "goal": "处理夏燕靖《中国艺术设计史（升级版）》2016 册 institution 候选第二组（宋元明清至近代）11 个：9 个新建、1 个更新、1 个 no_delta。",
    "status": "applied",
    "date": DATE,
    "inputs": {
        "candidate_index": {
            "path": "06-runtime\\state\\candidate-index.jsonl",
            "rows_before": 5339,
            "sha256_before": "sha256:a39b9cdfd9e849e3be99e8635c5eb1c82f7764af76b832a31a75e076766d3f9d",
            "sha256_scope": "CRLF→LF 归一后",
            "counts_before": {"applied": 819, "needs_evidence": 3663, "no_delta": 50, "rejected": 807},
        },
        "source": {
            "doc_id": DOC,
            "file": "03基础书籍-md文档/中国艺术设计史（升级版）_夏燕靖_2016_上海人民美术出版社.md",
            "spans": ["L3254-L3259", "L3499", "L3553-L3564", "L3706-L3715", "L3928-L3951", "L4341-L4367", "L4341-L4426", "L4596-L4618", "L4783-L4813", "L4835-L4838"],
        },
    },
    "method": {
        "rules": [
            "institution 候选按实体而非 slug 对账：先与既有 institution KU 的标题、别名和正文对齐，再定 create／update／no_delta／rejected。",
            "候选“宋代染织管理机构”是机构群而非单一衙署：中央四院中文思院、绫锦院已有独立 KU，本条只承载“中央四院＋地方九处”的网络范围，不拆薄条目。",
            "候选“景德镇官窑”以既有御器厂 KU 为落点；来源 L4345 以“官窑”统称，未出现“御器厂”，58 座官窑与珠山一处的对应关系不推定。",
            "候选“金代绫锦院”与既有 lingjinyuan KU 的 2016 L3499 内容逐句比对，无新增，判 no_delta。",
            "来源只给机构名、地点或一句制度描述者，降低 confidence 并在正文标注证据边界，不以来源外知识补写。",
            "来源内部数字或地理异文（宝船舵杆 11 米／11.07 米、青州（蓬莱））照录并标注，不裁定。",
            "03基础书籍-md文档只读；本批写 04-knowledge/units/institutions，9 条新建、1 条更新。",
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

assert len(ledger) == 33, len(ledger)
assert len(plan) == 10, len(plan)
assert len(mapping) == 11, len(mapping)
print(json.dumps({"ledger": len(ledger), "plan": len(plan), "mapping": len(mapping), "creates": len(creates), "updates": len(updates), "no_delta": len(no_deltas)}, ensure_ascii=False))
