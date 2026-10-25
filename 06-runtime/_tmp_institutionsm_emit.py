import hashlib
import json
import pathlib
import subprocess

ROOT = pathlib.Path(__file__).resolve().parents[1]
PKG = ROOT / "06-runtime" / "automation" / "2026-10-25-2016xiayanjing-institutions-batch-m"
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
        "cand-09-19",
        "安庆军械所",
        "04-knowledge/units/institutions/anqing-junxiesuo.md",
        "新建government_office：1862年曾国藩筹设我国第一家近代军事工业；试制第一台蒸汽机与第一艘木壳轮船“黄鹄号”，揭开自造轮船序幕",
    ),
    (
        "cand-09-75",
        "第一汽车制造厂",
        "04-knowledge/units/institutions/diyi-qiche-zhizaochang.md",
        "新建commercial_enterprise：1950年中苏商定苏联援建第一个载重汽车厂；1953-07-15长春奠基；1956-07-13解放牌下线；1958-05-05东风牌轿车诞生",
    ),
    (
        "cand-09-120",
        "上海砖瓦锯木厂",
        "04-knowledge/units/institutions/shanghai-zhuanwa-jumuchang.md",
        "新建commercial_enterprise：1853年英商在上海租界开设第一家近代大型建材工业，专为租界建筑提供建筑材料",
    ),
    (
        "cand-09-121",
        "盖茨公司（Getz Bros. & Co.）",
        "04-knowledge/units/institutions/getz-bros.md",
        "新建commercial_enterprise：20世纪初上海南京路规模较大的装饰材料供应商，代理石材、瓷砖、壁纸、夹板；《建筑月刊》广告提供样品、报价与施工技术支持",
    ),
    (
        "cand-10-12",
        "汉诺威工业设计论坛",
        "04-knowledge/units/institutions/hannuowei-gongye-sheji-luntan.md",
        "新建professional_society：来源称德国历史最悠久的工业设计机构，举办“if design award china 2007”；李宁半坡专业篮球鞋获设计大奖",
    ),
    (
        "cand-10-28",
        "中央手工业管理局（中央手工业管理总局）",
        "04-knowledge/units/institutions/zhongyang-shougongye-guanliju.md",
        "新建government_office：1954-12-08成立并随后举行第四次全国手工业生产合作会议；1956年毛泽东谈话；1961-09恢复为总局；1965年初撤消改建第二轻工业部",
    ),
    (
        "cand-11-09",
        "教育部",
        "04-knowledge/units/institutions/jiaoyubu.md",
        "新建government_office：1952年院系调整建立实用美术系科；1960年与文化部联合召开全国艺术教育工作会议；1998年颁布本科专业目录，工艺美术专业改为艺术设计专业",
    ),
]

updates = [
    (
        "cand-09-20",
        "江南机器制造总局",
        "04-knowledge/units/institutions/jiangnan-zhizao-zongju.md",
        "更新government_office：补2016 L4959、L4965“第一家使用机器的近代军事工业和机器工业”、1868年翻译馆与“西学东渐”先声；并录“曾国藩同李鸿章共同筹建”与“江南机器制造总局”名称异文",
    ),
]

no_deltas = [
    (
        "cand-11-10",
        "清华大学美术学院",
        "04-knowledge/units/institutions/central-academy-arts-design.md",
        "既有 central-academy-arts-design KU 的 2016 source location 已含 L6073-L6087，正文已记1999-11-20中央工艺美术学院与清华大学合并成立清华大学美术学院，候选无新增内容",
    ),
]

order = [
    "cand-09-19", "cand-09-20", "cand-09-75", "cand-09-120", "cand-09-121",
    "cand-10-12", "cand-10-28", "cand-11-09", "cand-11-10",
]
assert len(order) == 9

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
        "note": "候选“江南机器制造总局”以既有江南制造总局 KU 为落点；补入 2016 L4959、L4965，并保留“曾国藩支持下由李鸿章创办”与“曾国藩同李鸿章共同筹建”的表述差异。",
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
    "goal": "处理夏燕靖《中国艺术设计史（升级版）》2016 册 institution 候选第三组（现代）9 个：7 个新建、1 个更新、1 个 no_delta。",
    "status": "applied",
    "date": DATE,
    "inputs": {
        "candidate_index": {
            "path": "06-runtime\\state\\candidate-index.jsonl",
            "rows_before": 5339,
            "sha256_before": "sha256:6fc239d0d49d8d921d48262a74e7fbcc5e434ddf24c8c3cdc13f551c6246ca72",
            "sha256_scope": "CRLF→LF 归一后",
            "counts_before": {"applied": 829, "needs_evidence": 3652, "no_delta": 51, "rejected": 807},
        },
        "source": {
            "doc_id": DOC,
            "file": "03基础书籍-md文档/中国艺术设计史（升级版）_夏燕靖_2016_上海人民美术出版社.md",
            "spans": ["L4929-L4943", "L4929-L4972", "L5091-L5101", "L5319-L5343", "L5452-L5468", "L5597-L5746", "L6059-L6072", "L6073-L6090"],
        },
    },
    "method": {
        "rules": [
            "institution 候选按实体而非 slug 对账：先与既有 institution KU 的标题、别名和正文对齐，再定 create／update／no_delta／rejected。",
            "候选“江南机器制造总局”与既有江南制造总局 KU 同指一局：2016 L4959、L4965 新增“第一家使用机器的近代军事工业和机器工业”、1868 年翻译馆与“西学东渐”先声，判 update；创办表述与名称异文并录，不据一说改写另一说。",
            "候选“清华大学美术学院”与既有 central-academy-arts-design KU 逐句比对：2016 source location 已含 L6073-L6087，合并成立内容已完整收录，判 no_delta。",
            "候选“中央手工业管理局（中央手工业管理总局）”按同一机构沿革立目：1954 年成立、1961 年恢复、1965 年撤消改建均入本条；中华全国手工业合作社联合总社筹备委员会另记，不并入局本体。",
            "候选“教育部”只承载来源明确给出的三次设计教育制度动作；院系调整、艺术教育会议、专业目录更名分别标行号，不写教育部部史。",
            "来源只给机构名、地点或一句制度描述者，降低 confidence 并在正文标注证据边界，不以来源外知识补写。",
            "来源内部异文（“创办”／“共同筹建”、“江南制造总局”／“江南机器制造总局”、1965 年“撤消”）照录并标注，不裁定。",
            "03基础书籍-md文档只读；本批写 04-knowledge/units/institutions，7 条新建、1 条更新。",
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

assert len(ledger) == 27, len(ledger)
assert len(plan) == 8, len(plan)
assert len(mapping) == 9, len(mapping)
print(json.dumps({"ledger": len(ledger), "plan": len(plan), "mapping": len(mapping), "creates": len(creates), "updates": len(updates), "no_delta": len(no_deltas)}, ensure_ascii=False))
