import hashlib
import json
import pathlib
import subprocess

ROOT = pathlib.Path(__file__).resolve().parents[1]
PKG = ROOT / "06-runtime" / "automation" / "2026-10-25-2009xiayanjing-institutions-batch-o"
PKG.mkdir(parents=True, exist_ok=True)
DOC = "2009-xiayanjing-zhongguo-shejishi"
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
        "cand-03-20",
        "汉代官营丝织作坊",
        "04-knowledge/units/institutions/han-dai-guan-ying-sizhi-zuofang.md",
        "新建government_office：秦汉官营丝织作坊网络，规模扩大并采用先进提花织机，生产锦绣绮罗；成都为蜀锦集散中心，长安设东、西织室，临淄、襄邑设服官，织工多达数千人",
    ),
    (
        "cand-07-19",
        "全国高校工业设计学会",
        "04-knowledge/units/institutions/quanguo-gaoxiao-gongye-sheji-xuehui.md",
        "新建professional_society：1985年3月2—6日在北京成立，同时召开第一次全国工业设计教育学术交流会；成立大会另见 events/industrial-design-society-1985.md",
    ),
]

updates = []

no_deltas = [
    (
        "cand-03-37",
        "汉代官营漆器作坊",
        "04-knowledge/units/institutions/han-dai-qiqi-zuofang-guan-yuan.md",
        "既有 KU 已据夏燕靖 2016 升级版覆盖 2009 L1516-L1518 的全部语义：秦代设官府管理的漆器作坊、汉代中央到郡国设作坊官员、山东河南陕西江苏广东广西分布、漆器商品化、蜀郡广汉郡著名、金属铸器铭文记录地点年代工序工官、六至八道工序、金银扣器价值十倍；2009 为同一作者较早版本，无新增语义",
    ),
    (
        "cand-05-14",
        "西夏刻字司",
        "04-knowledge/units/institutions/kezisi.md",
        "既有 KU 已据夏燕靖 2016 升级版覆盖 2009 L2874 的全部语义：朝廷设刻字司专印书籍、佛经最多、兼刻文学法律医术日历卜筮咒文、西夏活字印本与西传桥梁推见；2009 为同一作者较早版本，无新增语义",
    ),
    (
        "cand-06-54",
        "中央手工业管理局",
        "04-knowledge/units/institutions/zhongyang-shougongye-guanliju.md",
        "既有 KU 已据夏燕靖 2016 升级版覆盖 2009 L4550-L4568 的全部语义：1954 年 12 月 8 日中央手工业管理局成立、之后举行第四次全国手工业生产合作会议；2016 另含 1955 年总社筹委会、1956 年毛泽东谈话、1960 年教育会议、1961 年恢复与 1965 年撤消改建；2009 为同一作者较早版本，无新增语义",
    ),
]

order = ["cand-03-20", "cand-03-37", "cand-05-14", "cand-06-54", "cand-07-19"]
assert len(order) == 5

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
    "goal": "处理夏燕靖《中国设计史》2009 册 institution 候选 5 个：2 个新建、0 个更新、3 个 no_delta。",
    "status": "applied",
    "date": DATE,
    "inputs": {
        "candidate_index": {
            "path": "06-runtime\\state\\candidate-index.jsonl",
            "rows_before": 5339,
            "sha256_before": "sha256:160a6fa5552b9eb4c67225576d189b4e1610cfb7f25a9ae122203442b06e0cc1",
            "sha256_scope": "CRLF→LF 归一后",
            "counts_before": {"applied": 846, "needs_evidence": 3634, "no_delta": 52, "rejected": 807},
        },
        "source": {
            "doc_id": DOC,
            "file": "03基础书籍-md文档/中国设计史_夏燕靖_2009_上海人民美术出版社.md",
            "spans": ["L1405-L1416", "L1516-L1518", "L2874", "L4550-L4568", "L4824"],
        },
    },
    "method": {
        "rules": [
            "institution 候选按实体而非 slug 对账：先与既有 institution KU 的标题、别名和正文对齐，再定 create／update／no_delta／rejected。",
            "候选“汉代官营丝织作坊”按官营生产网络合并立目：承载作坊规模、提花织机、织物品种、成都蜀锦集散、长安东、西织室、临淄与襄邑服官及产品流向；东、西织室与三服官已有独立 KU，本条不重复其制度细节。",
            "候选“汉代官营漆器作坊”判 no_delta：既有 han-dai-qiqi-zuofang-guan-yuan.md 已据 2016 升级版完整覆盖 2009 同段全部语义；2009 为同一作者较早版本，无新增语义。",
            "候选“西夏刻字司”判 no_delta：既有 kezisi.md 已据 2016 升级版完整覆盖 2009 同段，包括佛经最多、书籍门类、活字印本与西传桥梁推见。",
            "候选“中央手工业管理局”判 no_delta：既有 zhongyang-shougongye-guanliju.md 已据 2016 升级版覆盖 2009 的 1954 年成立与第四次全国手工业生产合作会议，并另含后续沿革。",
            "候选“全国高校工业设计学会”按 professional_society 立目：只登记 1985 年 3 月 2—6 日在北京成立及第一次全国工业设计教育学术交流会；成立大会另见 events/industrial-design-society-1985.md，两条并存不互相替代。",
            "2009 夏燕靖与 2016 夏燕靖为同一作者的前后版本；对 2016 已覆盖而 2009 无新增语义的候选，不重复立目，判 no_delta 并在 mapping 说明中登记。",
            "03基础书籍-md文档只读；本批写 04-knowledge/units/institutions，2 条新建、0 条更新。",
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

assert len(ledger) == 15, len(ledger)
assert len(plan) == 2, len(plan)
assert len(mapping) == 5, len(mapping)
print(json.dumps({"ledger": len(ledger), "plan": len(plan), "mapping": len(mapping), "creates": len(creates), "updates": len(updates), "no_delta": len(no_deltas)}, ensure_ascii=False))
