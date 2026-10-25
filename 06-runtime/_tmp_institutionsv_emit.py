import hashlib
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
PKG = ROOT / "06-runtime" / "automation" / "2026-10-25-2010tianzibing-institutions-batch-v"
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
        "cand-11-53",
        "果园厂",
        "04-knowledge/units/institutions/guoyuanchang.md",
        "新建government_office：田自秉 L4385-L4391 记明代永乐时期设官营果园厂，张德刚、包亮掌理制漆技艺，出雕漆、填漆，称‘厂制’；高丰 L4626 补永乐迁都北京后设厂、《嘉兴府志》张德刚召入、嘉兴派与云南派风格；并与洪武南京漆园、清代造办处漆作区分",
    ),
    (
        "cand-12-34",
        "吴彩霞绣坊",
        "04-knowledge/units/institutions/wucaixia-xiufang.md",
        "新建craft_workshop：田自秉 L4659 记胡莲仙于光绪年间迁居长沙，在司门口开设吴彩霞绣坊，湘绣之名渐为人知；魏氏共同提高技艺并在长沙近郊农村传授，为湘绣奠基",
    ),
    (
        "cand-12-102",
        "诸匠营",
        "04-knowledge/units/institutions/zhujiangying.md",
        "新建government_office：田自秉 L4933 记太平天国设诸匠营，按军制编组，有土营、木营、金匠营、织营、绣锦营、镌刻营等；引《金陵举义文存》南京城内一个机营分馆 3000 余人；与百工衙并列不合并",
    ),
    (
        "cand-12-103",
        "百工衙",
        "04-knowledge/units/institutions/baigongya.md",
        "新建government_office：田自秉 L4933 记太平天国另设百工衙，分服用、建筑、日用品、印刷、美术五类，列典织衙、缝衣衙、国帽衙、金靴衙、梳篦衙、典妆衙、典木衙、油漆衙、典铜衙、典竹衙、典石衙、洋遮衙、镌刻衙、刷书衙、绣锦衙、结彩衙等；并录典织衙改织营、绣锦衙与绣锦营未明关系",
    ),
    (
        "cand-13-10",
        "中国纺织建设公司",
        "04-knowledge/units/institutions/zhongguo-fangzhi-jianshe-gongsi.md",
        "新建commercial_enterprise：田自秉 L4995 记抗战胜利后江南较大棉纺织业为四大家族‘中国纺织建设公司’所垄断；单句来源，confidence 定为 low",
    ),
    (
        "cand-13-11",
        "中国蚕丝公司",
        "04-knowledge/units/institutions/zhongguo-cansi-gongsi.md",
        "新建commercial_enterprise：田自秉 L4995 记江浙丝绸敌伪时被‘中支蚕丝组织’掠夺，抗战胜利后为国民党‘中国蚕丝公司’垄断，盛泽产丝区没落；单句来源，confidence 定为 low",
    ),
    (
        "cand-13-12",
        "桥儿沟陶瓷厂",
        "04-knowledge/units/institutions/qiaoergou-taocichang.md",
        "新建craft_workshop：田自秉 L5023-L5025 引 1944 年 5 月 13 日《解放日报》记延安桥儿沟陶瓷厂用石膏模型、改造窑炉，出品近 200 种，能制白瓷杯碟，原料为本地瓷土；中共七大代表用其茶具",
    ),
]

updates = [
    (
        "cand-12-51",
        "造办处",
        "04-knowledge/units/institutions/neiwufu-zaobanchu.md",
        {
            "sha256": "sha256:31a38778d346c3bee412243f3ffa4485d22407338e54d1878705c10c917fab02",
            "bytes": 6177,
            "lines": 103,
        },
        "更新government_office：补田自秉 2010 L4707、L4729、L4743、L4747、L4778，记清初珐琅作康熙五十七年与造办处合并、画珐琅广东产地与‘粤东祥林店’、造办处漆作上承果园厂、清代雕漆多为造办处产品、造办处管理玉器制作；版本3、source_count 4",
    ),
]

rejects = [
    (
        "cand-12-21",
        "苏州织造",
        "候选由田自秉 L4629-L4631 的‘苏州织造’标题触发。该段以‘苏州的丝织’为主语，末句明言‘苏州织造，虽只是一个地区产品’；全段只给苏州丝织的织机、工人、宫廷用品品种、纹样与补子用色等级，未给织造局／署的设置、隶属、设官、衙署、匠役、产量与管理制度。来源把‘苏州织造’作为地区丝织产品与产业叙述，不足以立 institution 条目；相关数字已作为‘三大织造中心’的对照保留在 `institutions/jiangning-zhizaoju.md`。",
    ),
]

order = [
    "cand-11-53", "cand-12-21", "cand-12-34", "cand-12-51",
    "cand-12-102", "cand-12-103", "cand-13-10", "cand-13-11", "cand-13-12",
]
assert len(order) == 9

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
    "goal": "处理田自秉《中国工艺美术史（修订本）》2010 册 institution 候选 9 个：7 个新建、1 个更新、0 个 no_delta、1 个 rejected。",
    "status": "applied",
    "date": DATE,
    "inputs": {
        "candidate_index": {
            "path": "06-runtime\\state\\candidate-index.jsonl",
            "rows_before": 5339,
            "sha256_before": "sha256:85ff2f6b65cb718336440e288ff6f4a190decfd2975c2039c614899a5d9b18d9",
            "sha256_scope": "CRLF→LF 归一后",
            "counts_before": {"applied": 904, "needs_evidence": 3568, "no_delta": 56, "rejected": 811},
        },
        "source": {
            "doc_id": DOC,
            "file": "03基础书籍-md文档/中国工艺美术史（修订本）_田自秉_2010_东方出版中心.md",
            "spans": [
                "L4385-L4391", "L4629-L4631", "L4659", "L4707-L4778",
                "L4933", "L4995", "L5023-L5025",
            ],
        },
    },
    "method": {
        "rules": [
            "institution 候选按实体对账：先与既有 institution KU 的标题、别名与正文对齐，再定 create／update／no_delta／rejected。",
            "候选“果园厂”判 create：田自秉 L4385-L4391 明言其为明代封建官营漆器生产机构，永乐时期设厂，张德刚、包亮掌理制漆技艺，出雕漆、填漆；高丰 L4626 补永乐迁都北京后设厂、《嘉兴府志》张德刚召入与嘉兴派／云南派风格。洪武南京漆园等与果园厂不是同一机构，不合并。",
            "候选“苏州织造”判 rejected：田自秉 L4629-L4631 以“苏州的丝织”为主语，末句明言“苏州织造，虽只是一个地区产品”；全段只给产业数字、品种、纹样与补子等级，未给织造局／署的设置、隶属、设官、衙署、匠役、产量与管理制度，不足以立 institution 条目；相关数字已作为“三大织造中心”的对照保留在 `institutions/jiangning-zhizaoju.md`。",
            "候选“吴彩霞绣坊”判 create：田自秉 L4659 记胡莲仙光绪年间在长沙司门口开设吴彩霞绣坊，湘绣之名渐为人知；魏氏共同提高技艺并在长沙近郊农村传授。绣坊坊名、开设者、时间、地点与作用明确，规模与存续缺失。",
            "候选“造办处”判 update 既有 `institutions/neiwufu-zaobanchu.md`：补田自秉 L4707、L4729、L4743、L4747、L4778 的珐琅作康熙五十七年合并、画珐琅广东产地、造办处漆作、雕漆与玉器管理；不另建“珐琅作”“造办处漆作”薄条目。",
            "候选“诸匠营”判 create：田自秉 L4933 记太平天国设诸匠营，按军制编组，列土营、木营、金匠营、织营、绣锦营、镌刻营等；与百工衙并列，不合并。",
            "候选“百工衙”判 create：田自秉 L4933 记百工衙分服用、建筑、日用品、印刷、美术五类，列各衙名；与诸匠营并列，不合并；并录“典织衙后改为织营”“绣锦衙／绣锦营”两处交叉线索，不据名强行归一。",
            "候选“中国纺织建设公司”判 create：田自秉 L4995 只一句，记抗战胜利后江南较大棉纺织业为四大家族“中国纺织建设公司”所垄断；名称、时期、性质与垄断对象明确，组织细节全缺，confidence 定为 low。",
            "候选“中国蚕丝公司”判 create：田自秉 L4995 只一句，记江浙丝绸敌伪时为“中支蚕丝组织”掠夺，抗战胜利后为国民党“中国蚕丝公司”垄断，盛泽产丝区没落；两主体先后并列，来源未说明接收或继承关系，confidence 定为 low。",
            "候选“桥儿沟陶瓷厂”判 create：田自秉 L5023-L5025 引 1944 年 5 月 13 日《解放日报》记桥儿沟陶瓷厂用石膏模型、改造窑炉、出品近 200 种、能制白瓷杯碟、原料为本地瓷土，中共七大代表用其茶具；与子长瓷窑、建华瓷厂、磁州陶瓷研究所分条。",
            "03基础书籍-md文档只读；本批写 04-knowledge/units/institutions，7 条新建、1 条更新、1 条 rejected。",
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

assert len(ledger) == 25, len(ledger)
assert len(plan) == 8, len(plan)
assert len(mapping) == 8, len(mapping)
print(json.dumps({
    "ledger": len(ledger), "plan": len(plan), "mapping": len(mapping),
    "creates": len(creates), "updates": len(updates), "rejected": len(rejects),
}, ensure_ascii=False))
