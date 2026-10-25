import hashlib
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
PKG = ROOT / "06-runtime" / "automation" / "2026-10-25-2010tianzibing-institutions-batch-w"
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
        "cand-13-82",
        "建华瓷厂",
        "04-knowledge/units/institutions/jianhua-cichang.md",
        "新建craft_workshop：田自秉 L5023-L5025 记关中衣食村建华瓷厂生产质地较好的细瓷，有古铜、淡红、白、黑等色釉，产品供应本区并运销陇东；与桥儿沟陶瓷厂、子长瓷窑、磁州陶瓷研究所分条",
    ),
    (
        "cand-13-83",
        "解放区第一个陶瓷研究所",
        "04-knowledge/units/institutions/jiefangqu-diyige-taoci-yanjiusuo.md",
        "新建research_institute：田自秉 L5023-L5025 记河北磁州解放后立即恢复陶瓷生产，成立解放区第一个陶瓷研究所，为发展解放区陶瓷工艺生产作出贡献；来源未给正式所名、年份与隶属，confidence 定为 low",
    ),
    (
        "cand-13-13",
        "延安玻璃厂",
        "04-knowledge/units/institutions/yanan-bolichang.md",
        "新建craft_workshop：田自秉 L5027 记 1941 年在延安白手起家创建第一个玻璃厂，克服原料调配与坩埚制作困难，产出杯、瓶、灯罩等器皿，因原料含铁微带绿色；来源未给正式厂名",
    ),
    (
        "cand-13-15",
        "苏州刺绣研究所",
        "04-knowledge/units/institutions/suzhou-cixiu-yanjiusuo.md",
        "新建research_institute：田自秉 L5138-L5142 记 1957 年成立苏州刺绣研究所，研究创新苏绣传统技艺；同段记“猫”“金鱼”代表作、双面绣与乱针绣，但不把段内苏绣成就全部归所",
    ),
    (
        "cand-13-14",
        "北京珐琅厂",
        "04-knowledge/units/institutions/beijing-falangchang.md",
        "新建craft_workshop：田自秉 L5176-L5178 记景泰蓝仍以北京为生产中心，北京珐琅厂规模较大，北京工艺美术厂设景泰蓝车间，上海等地也发展生产；单句来源，confidence 定为 low",
    ),
    (
        "cand-13-16",
        "广东南海藤厂",
        "04-knowledge/units/institutions/guangdong-nanhai-tengchang.md",
        "新建craft_workshop：田自秉 L5258 记解放后建立许多大型藤编工艺厂，广东南海藤厂为其中之一；单句来源，同段藤编工艺背景不专属该厂，confidence 定为 low",
    ),
]

updates = [
    (
        "cand-13-81",
        "云锦研究所",
        "04-knowledge/units/institutions/nanjing-yunjin-yanjiusuo.md",
        {
            "sha256": "sha256:e7a06c22a3e5c7d5e18ccd5c712aa2fc9f947537e8d38a151e884662670c6254",
            "bytes": 3598,
            "lines": 84,
        },
        "更新research_institute：候选“云锦研究所”与既有南京市云锦研究所对账，判同一机构 update；补田自秉 2010 L5103 的解放前衰落、解放后恢复扩大生产、建所总结艺人经验、整理传统图案、开展创新，以及八句口诀、五类图案组织、雨花锦等新创用品；补 alias“云锦研究所”，版本2、source_count 3",
    ),
]

no_deltas = [
    (
        "cand-14-21",
        "杭州国立艺术专科学校",
        "04-knowledge/units/institutions/hangzhou-guoli-yizhuan.md",
        "既有 04-knowledge/units/institutions/hangzhou-guoli-yizhuan.md 已完整覆盖候选内容：该条 sources 已含田自秉 2010 L5723，正文照录“解放前在杭州国立艺术专科学校做学生、常去浙江省图书馆阅览《格古要论》《骨董琐记》”并讨论“杭州国立艺专／国立杭州艺术专科学校”名称差异，无需写回；判定 no_delta",
    ),
]

order = [
    "cand-13-82", "cand-13-83", "cand-13-13", "cand-13-81",
    "cand-13-15", "cand-13-14", "cand-13-16", "cand-14-21",
]
assert len(order) == 8

create_map = {c[0]: c for c in creates}
update_map = {u[0]: u for u in updates}
no_delta_map = {n[0]: n for n in no_deltas}
assert set(create_map) | set(update_map) | set(no_delta_map) == set(order)

ledger = []
for n in order:
    if n in no_delta_map:
        _, title, target, reason = no_delta_map[n]
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
            "decision": {"status": "approved", "reason": reason, "decided_by": "Agent", "decided_at": DATE},
            "updated_at": DATE, "target_ref": target,
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
    "goal": "处理田自秉《中国工艺美术史（修订本）》2010 册 institution 候选 8 个：6 个新建、1 个更新、1 个 no_delta、0 个 rejected。",
    "status": "applied",
    "date": DATE,
    "inputs": {
        "candidate_index": {
            "path": "06-runtime\\state\\candidate-index.jsonl",
            "rows_before": 5339,
            "sha256_before": "sha256:0f317aa0940599417617c2dbf16b5abba561d4d258d564a005dac5889366553a",
            "sha256_scope": "CRLF→LF 归一后",
            "counts_before": {"applied": 912, "needs_evidence": 3559, "no_delta": 56, "rejected": 812},
        },
        "source": {
            "doc_id": DOC,
            "file": "03基础书籍-md文档/中国工艺美术史（修订本）_田自秉_2010_东方出版中心.md",
            "spans": [
                "L5023-L5027", "L5103", "L5138-L5142", "L5176-L5178",
                "L5256-L5258", "L5723",
            ],
        },
    },
    "method": {
        "rules": [
            "institution 候选按实体对账：先与既有 institution KU 的标题、别名与正文对齐，再定 create／update／no_delta／rejected。",
            "候选“建华瓷厂”判 create：田自秉 L5025 记关中衣食村的建华瓷厂生产质地较好的细瓷，有古铜、淡红、白、黑等色釉，产品供应本区并运销陇东；厂名、地点、产品与销售范围明确，创设年份与隶属缺失。",
            "候选“解放区第一个陶瓷研究所”判 create：田自秉 L5025 记河北磁州解放后立即恢复陶瓷生产并成立解放区第一个陶瓷研究所；来源未给正式所名、成立年份、隶属、人员与研究内容，confidence 定为 low，不补造正式所名。",
            "候选“延安玻璃厂”判 create：田自秉 L5027 记 1941 年在延安白手起家创建第一个玻璃厂，克服原料调配与坩埚制作困难，产出杯、瓶、灯罩等器皿；来源未给正式厂名，条目名按地点与通称转写，并在正文标注。",
            "候选“云锦研究所”判 update 既有 `institutions/nanjing-yunjin-yanjiusuo.md`：该条已记南京市云锦研究所 1957 年 7 月由江苏省人民政府批准建立；田自秉 L5103 的“云锦研究所”在南京、名称与“解放后建立”时期上一致，按同一机构合并记录，补田自秉的建立背景、研究所工作、八句口诀、图案组织与新创生活用品，不另建重复条目；来源未明说同指，名实张力写入验证状态。",
            "候选“苏州刺绣研究所”判 create：田自秉 L5140 记 1957 年成立苏州刺绣研究所，专门从事苏绣传统技艺的研究和创新工作；同段“猫”“金鱼”、双面绣与乱针绣的叙述不全部归所，正文标注段内指代不明。",
            "候选“北京珐琅厂”判 create：田自秉 L5178 只一句，记景泰蓝仍以北京为生产中心，北京珐琅厂规模较大，北京工艺美术厂设景泰蓝车间，上海等地也发展生产；名称、地点与规模判断明确，组织细节全缺，confidence 定为 low。",
            "候选“广东南海藤厂”判 create：田自秉 L5258 只一句，记解放后建立许多大型藤编工艺厂，广东南海藤厂为其中之一；同段藤编工艺背景不专属该厂，confidence 定为 low。",
            "候选“杭州国立艺术专科学校”判 no_delta：既有 `institutions/hangzhou-guoli-yizhuan.md` 已含田自秉 2010 L5723 为第二源，正文完整照录“解放前在杭州国立艺术专科学校做学生、常去浙江省图书馆阅览《格古要论》《骨董琐记》”并讨论校名差异，候选无新增语义。",
            "03基础书籍-md文档只读；本批写 04-knowledge/units/institutions，6 条新建、1 条更新、1 条 no_delta。",
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

assert len(ledger) == 24, len(ledger)
assert len(plan) == 7, len(plan)
assert len(mapping) == 7, len(mapping)
print(json.dumps({
    "ledger": len(ledger), "plan": len(plan), "mapping": len(mapping),
    "creates": len(creates), "updates": len(updates), "no_delta": len(no_deltas),
}, ensure_ascii=False))
