import hashlib
import json
import pathlib
import subprocess

ROOT = pathlib.Path(__file__).resolve().parents[1]
PKG = ROOT / "06-runtime" / "automation" / "2026-10-25-2004gaofeng-institutions-batch-n"
PKG.mkdir(parents=True, exist_ok=True)
DOC = "2004-gaofeng-zhongguo-shejishi"
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
        "cand-05-06",
        "元代画局",
        "04-knowledge/units/institutions/yuan-dai-huaju.md",
        "新建government_office：将作院属下画局，秩从八品，至元十五年置，掌描造诸色样制；只设计不制作，光画不造工匠百余户，包揽各局院产品设计",
    ),
    (
        "cand-07-11",
        "武英殿修书处",
        "04-knowledge/units/institutions/wuyingdian-xiushuchu.md",
        "新建publishing_house：清内府出版机构，康熙雍正乾隆三朝出书500余种；乾隆间金简主持刻枣木活字25.3万个，印《武英殿珍版丛书》134种2389卷",
    ),
    (
        "cand-07-14",
        "湖南瓷业公司",
        "04-knowledge/units/institutions/hunan-ciye-gongsi.md",
        "新建commercial_enterprise：清末民初醴陵官商合办新式制瓷公司，熊希龄任总理；前身1906年湖南瓷业学校，设圆器厂、琢器厂、机械室、电灯室、化学室，创烧釉下花瓷并获博览会金奖",
    ),
    (
        "cand-07-22",
        "两江师范学堂图画手工科",
        "04-knowledge/units/institutions/liangjiang-shifan-xuetang.md",
        "更新design_school：补高丰2004 L5461李瑞清1906年呈准学部设科、图画手工主科与音乐副主科、图案课与用器画、连续两届招生、吕凤子与姜丹书等毕业生，以及各地师范推广",
    ),
    (
        "cand-sup-34",
        "继昌隆缫丝厂",
        "04-knowledge/units/institutions/jichanglong-sichang.md",
        "新建commercial_enterprise：1872年侨商陈启源在广东南海创办，使用法国蒸气加热与机械缫丝直缫坐缫机，中国近代最早出现的民族资本机器工业",
    ),
    (
        "cand-sup-35",
        "上海机器织布局",
        "04-knowledge/units/institutions/shanghai-jiqi-zhibuju.md",
        "新建commercial_enterprise：1878年上海绅商集股创办的中国第一个近代纺织厂，购英美机器，1890年开机织布",
    ),
    (
        "cand-sup-36",
        "景德镇瓷业公司（江西瓷业公司）",
        "04-knowledge/units/institutions/jingdezhen-ciye-gongsi.md",
        "新建commercial_enterprise：1910年成立，本厂景德镇仍用旧法，分厂鄱阳实验改良并设陶业学堂，拟机器制瓷、煤窑烧炼",
    ),
    (
        "cand-sup-37",
        "点石斋石印局",
        "04-knowledge/units/institutions/dian-shizhai.md",
        "新建publishing_house：1876年英商在上海创设，蒸汽机、200名工人，影印旧版书并石印书籍；同期新式印刷厂10多家",
    ),
    (
        "cand-sup-77",
        "奇异公司",
        "04-knowledge/units/institutions/qiyi-gongsi.md",
        "新建commercial_enterprise：1917年美商在上海开办，我国最早的灯泡企业，近代电光源工业开始建立",
    ),
]

updates = [
    (
        "cand-07-22",
        "两江师范学堂图画手工科",
        "04-knowledge/units/institutions/liangjiang-shifan-xuetang.md",
        "更新design_school：补高丰2004 L5461李瑞清1906年呈准学部设科、图画手工主科与音乐副主科、图案课与用器画、连续两届招生、吕凤子与姜丹书等毕业生，以及各地师范推广",
    ),
]

# cand-07-22 is an update, not a create; remove it from creates.
creates = [c for c in creates if c[0] != "cand-07-22"]

no_deltas = []

order = [
    "cand-05-06", "cand-07-11", "cand-07-14", "cand-07-22",
    "cand-sup-34", "cand-sup-35", "cand-sup-36", "cand-sup-37", "cand-sup-77",
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
        "note": "候选“两江师范学堂图画手工科”以既有两江师范学堂 KU 为落点；补入高丰 2004 的设科程序、科目结构、两届招生与毕业生，保留李立新“1906 设科”、赵农“1905 开课”的层面差异。",
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
    "goal": "处理高丰《中国设计史》2004 册 institution 候选 9 个：8 个新建、1 个更新、0 个 no_delta。",
    "status": "applied",
    "date": DATE,
    "inputs": {
        "candidate_index": {
            "path": "06-runtime\\state\\candidate-index.jsonl",
            "rows_before": 5339,
            "sha256_before": "sha256:502e105303bc01eb6092553db1e3d433ae2a1353d2ba241f973ab3f646469e6e",
            "sha256_scope": "CRLF→LF 归一后",
            "counts_before": {"applied": 837, "needs_evidence": 3643, "no_delta": 52, "rejected": 807},
        },
        "source": {
            "doc_id": DOC,
            "file": "03基础书籍-md文档/中国设计史_高丰_2004_广西美术出版社.md",
            "spans": ["L3558", "L5161", "L5239", "L5243", "L5245", "L5247", "L5261-L5268", "L5461"],
        },
    },
    "method": {
        "rules": [
            "institution 候选按实体而非 slug 对账：先与既有 institution KU 的标题、别名和正文对齐，再定 create／update／no_delta／rejected。",
            "候选“两江师范学堂图画手工科”以既有两江师范学堂 KU 为落点：高丰 2004 补出李瑞清呈准学部、主副科结构、两届招生与毕业生，判 update；李立新 1906 设科、赵农 1905 开课并录。",
            "候选“元代画局”按官方设计机构立目：只设计不制作、工匠百余户、包揽各局院产品设计均入本体，不写成将作院制度通史。",
            "候选“武英殿修书处”按清代内府出版机构立目：三朝 500 余种、金简主持枣木活字 25.3 万个、《武英殿珍版丛书》134 种 2389 卷均入本体。",
            "候选“湖南瓷业公司”“景德镇瓷业公司”分别立目：前者以学校—公司—釉下花瓷为主线，后者以本厂守旧、分厂试验的双轨结构为主线，不互相替代。",
            "候选“继昌隆缫丝厂”“上海机器织布局”按企业本体立目：前者记法国蒸气加热与直缫坐缫机，后者记英美机器与 1890 开机，不写成近代纺织通史。",
            "候选“点石斋石印局”“奇异公司”按机构本体立目：只写来源给出的创设年份、创办者国籍、动力、工人数、业务或产品定位，不补英文原名与母子公司关系。",
            "来源内部异文（“奇异公司”与 General Electric 的关系、“拟用机器制瓷”是否落实）保留为未释或待核，不推定。",
            "03基础书籍-md文档只读；本批写 04-knowledge/units/institutions，8 条新建、1 条更新。",
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
assert len(plan) == 9, len(plan)
assert len(mapping) == 9, len(mapping)
print(json.dumps({"ledger": len(ledger), "plan": len(plan), "mapping": len(mapping), "creates": len(creates), "updates": len(updates), "no_delta": len(no_deltas)}, ensure_ascii=False))
