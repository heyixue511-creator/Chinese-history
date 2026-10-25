import hashlib
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
PKG = ROOT / "06-runtime" / "automation" / "2026-10-25-2010tianzibing-institutions-batch-u"
PKG.mkdir(parents=True, exist_ok=True)
DOC = "2010-tianzibing-zhongguo-gongyi-meishushi"
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
        "cand-08-07",
        "后赵邺城织锦署",
        "04-knowledge/units/institutions/houzhao-yecheng-zhijinshu.md",
        "新建government_office：田自秉 L2918 引晋·陵朔《邺中记》记后赵邺城设织锦署，列大登高至核桃文锦等锦名及青白黄绿紫蜀六色绨；与东晋锦署同名异实，`institutions/jinshu.md` 已作对照，本条不并入",
    ),
    (
        "cand-09-95",
        "瓷窑官",
        "04-knowledge/units/institutions/ciyaoguan.md",
        "新建government_office：田自秉 L3693 记辽代因瓷业兴起设专管窑务的瓷窑官，引《宋会要辑稿》太平兴国四年幽州来归事，判断设置当在太平兴国以前；窑场与‘官’字款作旁证，不推断瓷窑官驻窑",
    ),
    (
        "cand-10-15",
        "四川锦院",
        "04-knowledge/units/institutions/sichuan-jinyuan.md",
        "新建government_office：田自秉 L3792-L3794 记元丰六年建四川锦院，募军匠500人，挽综164、杼54、练染11、纺绎110，织机154张，用丝125000两、染料211000斤；南宋乾道四年合三厂为锦院；列四类产品；与汴梁绫锦院分条",
    ),
    (
        "cand-10-27",
        "绣院",
        "04-knowledge/units/institutions/xiuyuan.md",
        "新建government_office：田自秉 L3830-L3832 记宋代设绣院，绣工300余人，制人物花鸟山水楼阁，针法称神针，向画绣发展；引《筠清轩秘录》《存素堂丝绣录》；与‘文绣院’是否同一机构未说明，不合并",
    ),
    (
        "cand-10-68",
        "纳失失局",
        "04-knowledge/units/institutions/nashishiju.md",
        "新建government_office：田自秉 L4036-L4042 记元在弘州（今原阳）、荨麻林（今万全西北）设纳失失局，移入3300多户回族工匠；织染杂造人匠都总管府下设弘州、荨麻林纳失失局；别失八里局、忽丹八里局亦产纳失失；并录纳石失/纳失失/纳失思/纳克实与‘畏兀兀’译名张力",
    ),
    (
        "cand-10-72",
        "木棉提举司",
        "04-knowledge/units/institutions/mumian-tijusi.md",
        "新建government_office：田自秉 L4072 记至元二十六年（1289）在浙东、江东、江西、湖广、福建设木棉提举司，以都提举司总管，每年上缴棉布10万匹；松江以棉织为副业者1000多家；不并入黄道婆条",
    ),
]

updates = [
    (
        "cand-09-33",
        "辽代绫锦院",
        "04-knowledge/units/institutions/lingjinyuan.md",
        {
            "sha256": "sha256:2e1cb4360a3e54f899c4cb0d032e2d12ad2c62ce78e1b8b91dd618d752deab58",
            "bytes": 7699,
            "lines": 119,
        },
        "更新government_office：同名跨朝代绫锦院条补田自秉 L3488 辽代上京、祖州设院，灵锦显霸四州植桑麻，宜州‘民工织纴，多技巧’，对外赠与锦罗绮纱縠缎，赤峰辽墓织金丝织品；版本3，source_count 仍为6",
    ),
    (
        "cand-09-34",
        "西夏官营手工业机构群",
        "04-knowledge/units/institutions/xi-xia-guan-ying-shou-gong-ye-jigou.md",
        {
            "sha256": "sha256:4bb0068d90e3262be1a71aac5130144a58a6fbb6632d1e999d8266b7716a05d8",
            "bytes": 4868,
            "lines": 99,
        },
        "更新government_office：补田自秉 L3494 同一七机构清单、‘出车（造车）院’异写、毡毯氆氇毛布与银川贺兰山墓葬；并录‘造车院／出车院’用字差异，不另立第八机构；版本2、source_count 2",
    ),
    (
        "cand-10-66",
        "建康织染局",
        "04-knowledge/units/institutions/jiankanglu-zhiranju.md",
        {
            "sha256": "sha256:515e29fc47c0c69564eb0b18e937ee176fbc58d1d1def4f4fe2a3426c85f01ad",
            "bytes": 5050,
            "lines": 90,
        },
        "更新government_office：补田自秉 L4030 同引《金陵新志》东织染局‘三千六户、机154张、额造4527段’与元代设司／局背景、至元十六年掠夺工匠42万人；并录‘三千六户／三千六百户’；加别名‘建康织染局’；版本2、source_count 2",
    ),
]

rejects = [
    (
        "cand-09-14",
        "正仓院（日本）",
        "候选由田自秉 L3392 记‘在日本正仓院，还保存有我国唐代的螺钿工艺多种’触发，L3388 亦仅记正仓院藏金银平脱器；两处都只把正仓院作唐代漆器的收藏地，未给其机构沿革、职能、管理制度、隶属或院址，与‘中国历史博物馆’同类，不足以立 institution 条目",
    ),
]

order = [
    "cand-08-07", "cand-09-14", "cand-09-33", "cand-09-34", "cand-09-95",
    "cand-10-15", "cand-10-27", "cand-10-66", "cand-10-68", "cand-10-72",
]
assert len(order) == 10

create_map = {c[0]: c for c in creates}
update_map = {u[0]: u for u in updates}
reject_map = {r[0]: r for r in rejects}
assert set(create_map) | set(update_map) | set(reject_map) == set(order)

ledger = []
for n in order:
    if n in reject_map:
        _, title, reason = reject_map[n]
        ledger.append({
            "candidate_id": cid(n), "expected_state": "needs_evidence", "state": "rejected",
            "decision": {"status": "rejected", "reason": reason, "decided_by": "Agent", "decided_at": DATE},
            "updated_at": DATE,
        })
        continue
    if n in create_map:
        _, title, target, note = create_map[n]
        action = "新建"
    else:
        _, title, target, before, note = update_map[n]
        action = "更新"
    ledger.append({
        "candidate_id": cid(n), "expected_state": "needs_evidence", "state": "ready_for_review",
        "decision": {"status": "pending", "reason": f"已完成语义复读：{action} {target}", "decided_by": "Agent", "decided_at": DATE},
        "updated_at": DATE,
    })
    ledger.append({
        "candidate_id": cid(n), "expected_state": "ready_for_review", "state": "approved",
        "decision": {"status": "approved", "reason": f"canonical 候选语义复读完成，批准{action} {target}", "decided_by": "Agent", "decided_at": DATE},
        "updated_at": DATE,
    })
    ledger.append({
        "candidate_id": cid(n), "expected_state": "approved", "state": "applied",
        "decision": {"status": "approved", "reason": f"已判定 applied：{action} {target}", "decided_by": "Agent", "decided_at": DATE},
        "updated_at": DATE, "target_ref": target,
    })

plan = []
for n in order:
    if n in create_map:
        _, title, target, note = create_map[n]
        f = fp(ROOT / target)
        plan.append({
            "action": "create", "target_ref": target, "candidate_id": cid(n),
            "entity": title, "before": None, "after_sha256": f["sha256"], "bytes": f["bytes"],
            "lines": f["lines"], "note": note,
        })
    elif n in update_map:
        _, title, target, before, note = update_map[n]
        f = fp(ROOT / target)
        plan.append({
            "action": "update", "target_ref": target, "candidate_id": cid(n),
            "entity": title, "before": before, "after_sha256": f["sha256"], "bytes": f["bytes"],
            "lines": f["lines"], "note": note,
        })

mapping = []
for n in order:
    if n in create_map:
        _, title, target, note = create_map[n]
        action = "create"
    elif n in update_map:
        _, title, target, before, note = update_map[n]
        action = "update"
    else:
        continue
    mapping.append({
        "entity": title, "target_ref": target, "action": action,
        "canonical_candidate": cid(n), "merged_candidates": [],
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
    "goal": "处理田自秉《中国工艺美术史（修订本）》2010 册 institution 候选 10 个：6 个新建、3 个更新、0 个 no_delta、1 个 rejected。",
    "status": "applied",
    "date": DATE,
    "inputs": {
        "candidate_index": {
            "path": "06-runtime\\state\\candidate-index.jsonl",
            "rows_before": 5339,
            "sha256_before": "sha256:05dd4761a548d3bdf08e6cb7516d57135ad2f5e2263a6f836a6c2de4290ce6cc",
            "sha256_scope": "CRLF→LF 归一后",
            "counts_before": {"applied": 895, "needs_evidence": 3578, "no_delta": 56, "rejected": 810},
        },
        "source": {
            "doc_id": DOC,
            "file": "03基础书籍-md文档/中国工艺美术史（修订本）_田自秉_2010_东方出版中心.md",
            "spans": [
                "L2918", "L3388-L3392", "L3488", "L3494", "L3693",
                "L3792-L3794", "L3830-L3832", "L4030", "L4036-L4042", "L4072",
            ],
        },
    },
    "method": {
        "rules": [
            "institution 候选按实体对账：先与既有 institution KU 的标题、别名与正文对齐，再定 create／update／no_delta／rejected。",
            "候选“后赵邺城织锦署”判 create：田自秉 L2918 引《邺中记》记后赵邺城织锦署及锦名、色名；与东晋锦署同名异实，`institutions/jinshu.md` 已将其作为对照，本条不并入东晋锦署。",
            "候选“正仓院（日本）”判 rejected：L3392 与 L3388 都只把正仓院作唐代漆器的收藏地，未给机构沿革、职能、管理制度、隶属或院址，与“中国历史博物馆”同类。",
            "候选“辽代绫锦院”判 update 既有 `institutions/lingjinyuan.md`：补田自秉 L3488 上京、祖州设院、灵锦显霸四州植桑麻、宜州织纴、对外赠与品种与赤峰辽墓织金丝织品；同名跨朝代合并条不拆。",
            "候选“西夏官营手工业机构群”判 update 既有 `institutions/xi-xia-guan-ying-shou-gong-ye-jigou.md`：补田自秉 L3494 同一七机构清单、“出车（造车）院”异写、毡毯氆氇毛布与银川墓葬；不另立第八机构。",
            "候选“瓷窑官”判 create：辽代因瓷业兴起设专管窑务的瓷窑官，引《宋会要辑稿》太平兴国四年事，作者判断设置当在太平兴国以前；窑场与“官”字款只作旁证，不推断瓷窑官驻窑。",
            "候选“四川锦院”判 create：元丰六年建院、军匠 500 人、四类工种、织机 154 张、用丝与染料数、四类产品均明确；与汴梁绫锦院分条，不把“锦院”通名当作同一机构。",
            "候选“绣院”判 create：宋代绣院 300 余人、神针、向画绣发展；来源作“绣院”，与“文绣院”是否同一机构未说明，不合并、不互训。",
            "候选“建康织染局”判 update 既有 `institutions/jiankanglu-zhiranju.md`：补田自秉 L4030 同引《金陵新志》东织染局数字与元代设司／局背景；并录“三千六户／三千六百户”两写。",
            "候选“纳失失局”判 create：弘州、荨麻林、别失八里、忽丹八里诸局；3,300 多户回族工匠；织染杂造人匠都总管府隶属；并录纳石失／纳失失／纳失思／纳克实与“畏兀兀”译名张力，不强行判定各局同级。",
            "候选“木棉提举司”判 create：至元二十六年（1289）设于浙东、江东、江西、湖广、福建，以都提举司总管，每年上缴棉布 10 万匹；黄道婆条只作人物与技术传播背景，不并入。",
            "03基础书籍-md文档只读；本批写 04-knowledge/units/institutions，6 条新建、3 条更新、1 条 rejected。",
        ],
    },
    "outputs": {
        "apply_plan": {"path": f"06-runtime\\automation\\{PKG.name}\\apply-plan.jsonl", "rows": len(plan), "create": len(creates), "update": len(updates)},
        "ledger": {"path": f"06-runtime\\automation\\{PKG.name}\\candidate-decision-ledger.jsonl", "rows": len(ledger), "candidates": len(order), "applied": len(creates) + len(updates), "no_delta": 0, "rejected": len(rejects)},
        "canonical_mapping": {"path": f"06-runtime\\automation\\{PKG.name}\\canonical-mapping.json", "entries": len(mapping), "merged_candidates": []},
    },
    "state_after": {},
}
(PKG / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

assert len(ledger) == 28, len(ledger)
assert len(plan) == 9, len(plan)
assert len(mapping) == 9, len(mapping)
print(json.dumps({
    "ledger": len(ledger), "plan": len(plan), "mapping": len(mapping),
    "creates": len(creates), "updates": len(updates), "rejected": len(rejects),
}, ensure_ascii=False))
