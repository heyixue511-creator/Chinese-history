import hashlib
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
PKG = ROOT / "06-runtime" / "automation" / "2026-10-25-2010tianzibing-institutions-batch-t"
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
        "cand-06-07",
        "蜀郡、成都、广汉郡工官",
        "04-knowledge/units/institutions/shujun-chengdu-guanghanjun-gongguan.md",
        "新建government_office：田自秉 L2145 记官方制铜机构有少府属尚方令、考工令及蜀郡、成都、广汉郡工官，蜀郡广汉所制最精；L2561 记三处工官每年各用费五百万。来源未给设置年代、员额、隶属与治所",
    ),
    (
        "cand-07-10",
        "暴室",
        "04-knowledge/units/institutions/baoshi.md",
        "新建government_office：田自秉 L2519 引《三辅黄图》记未央宫有暴室，主掖庭织作染练之署；与平准令并列，来源未给隶属、员额与设置年代",
    ),
    (
        "cand-07-11",
        "平准令",
        "04-knowledge/units/institutions/pingzhunling.md",
        "新建government_office：田自秉 L2519 引《续汉书·百官志》记平准令主练染作彩色；与暴室并列，来源未给隶属、员额与其他职能",
    ),
    (
        "cand-07-87",
        "严道木官",
        "04-knowledge/units/institutions/yandao-muguan.md",
        "新建government_office：田自秉 L2697 引《汉书·地理志》‘严道有木官’，为专事运输木材的官吏；来源未给隶属、员额、运输路线与木材品种",
    ),
    (
        "cand-08-06",
        "南朝染署",
        "04-knowledge/units/institutions/nanchao-ranshu.md",
        "新建government_office：田自秉 L2912 记南朝少府下有平准令管理染织生产，后避宋顺帝刘准讳改名为染署；来源未给设置年份、员额与内部署作",
    ),
]

updates = [
    (
        "cand-06-04",
        "尚方",
        "04-knowledge/units/institutions/shangfang.md",
        {
            "sha256": "sha256:56610b01c400d3e0e7ae7bff9db14d6881ed1f78c64a52a1e27d83183488d9d0",
            "bytes": 4379,
            "lines": 90,
        },
        "更新government_office：补田自秉 L2145 少府隶属、汉武帝分左中右三官署、中尚方制鼎壶，L2249 引《后汉书》尚方掌御刀剑玩好器物及左/中/右分工（弩机/装饰具/镜槃釜）；与赵农蔡伦条并录",
    ),
    (
        "cand-06-05",
        "长安东、西织室",
        "04-knowledge/units/institutions/dongxi-zhishi.md",
        {
            "sha256": "sha256:115f5b57e3c814a60f6dcbae2648671da7bdb8b81c106456c621c45724b06d5c",
            "bytes": 4279,
            "lines": 89,
        },
        "更新government_office：补田自秉 L2442 引《汉书·百官公卿表》少府属东织室令丞、西织室令丞，河平元年省东织、更名西织为织室，绥和废；并录与夏燕靖‘东汉’说的时代冲突",
    ),
    (
        "cand-07-18",
        "汉代漆器作坊官员",
        "04-knowledge/units/institutions/han-dai-qiqi-zuofang-guan-yuan.md",
        {
            "sha256": "sha256:8bd97fd08287bf52e50c7e81e47cdb62336a7a100e4b3e38c5ae8e06cd0a051a",
            "bytes": 5232,
            "lines": 91,
        },
        "更新government_office：补田自秉 L2561-L2567 八郡名单、蜀郡成都广汉工官每年各用费五百万、梓潼武都工官、蜀郡广汉主要中心、乐浪铭文与约百年铭文年代；与夏燕靖 6—8 道及‘金属铸器铭文’说并录",
    ),
]

rejects = [
    (
        "cand-01-04",
        "东方出版中心",
        "来源 L23-L61 为该书 CIP/版权页（出版发行、地址、电话、印刷、开本、字数、印张、版次、ISBN、定价），非设计史机构，未提供可立目的机构史内容",
    ),
    (
        "cand-03-31",
        "中国历史博物馆",
        "候选仅因 L953 记司母戊鼎“现陈列于中国历史博物馆”而触发；来源未记该馆的机构沿革、职能、藏品管理或设计史活动，仅作展陈地点，不足以立 institution 条目",
    ),
]

order = [
    "cand-01-04", "cand-03-31", "cand-06-04", "cand-06-05", "cand-06-07",
    "cand-07-10", "cand-07-11", "cand-07-18", "cand-07-87", "cand-08-06",
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
    "goal": "处理田自秉《中国工艺美术史（修订本）》2010 册 institution 候选 10 个：5 个新建、3 个更新、0 个 no_delta、2 个 rejected。",
    "status": "applied",
    "date": DATE,
    "inputs": {
        "candidate_index": {
            "path": "06-runtime\\state\\candidate-index.jsonl",
            "rows_before": 5339,
            "sha256_before": "sha256:8cefbf52f6898b906cc24f846ed2f8cb8e5d6dff7cc95953d44460c6e94d3cf8",
            "sha256_scope": "CRLF→LF 归一后",
            "counts_before": {"applied": 887, "needs_evidence": 3588, "no_delta": 56, "rejected": 808},
        },
        "source": {
            "doc_id": DOC,
            "file": "03基础书籍-md文档/中国工艺美术史（修订本）_田自秉_2010_东方出版中心.md",
            "spans": [
                "L23-L61", "L953-L1445", "L2145", "L2249", "L2442",
                "L2519", "L2561-L2567", "L2697", "L2912-L2916",
            ],
        },
    },
    "method": {
        "rules": [
            "institution 候选按实体对账：先与既有 institution KU 的标题、别名与正文对齐，再定 create／update／no_delta／rejected。",
            "候选“东方出版中心”判 rejected：L23-L61 为 CIP／版权页，只有出版发行、地址、电话、印刷、开本、字数、印张、版次、ISBN、定价，非设计史机构。",
            "候选“中国历史博物馆”判 rejected：仅 L953 记司母戊鼎现陈列于该馆，无机构沿革、职能或设计史活动，只作展陈地点。",
            "候选“尚方”判 update 既有 `institutions/shangfang.md`：补少府隶属、汉武帝分左中右三官署、中尚方制鼎壶、左中右产品分工；赵农蔡伦条与田自秉制度条并录，不裁断官制层级。",
            "候选“东织室、西织室”判 update 既有 `institutions/dongxi-zhishi.md`：补《汉书·百官公卿表》少府属东织室令丞、西织室令丞、河平元年省东织更名西织为织室、绥和废；与夏燕靖 2016“东汉”说并录，标时代冲突。",
            "候选“蜀郡、广汉郡工官”判 create：按来源所列“蜀郡、成都、广汉郡工官”立目，合铜器 L2145 与漆器 L2561 两处；成都与蜀郡的层级关系来源未给，不擅自合并为二。",
            "候选“暴室”判 create：未央宫主掖庭织作染练之署；与平准令并列，来源未给二者分工。",
            "候选“平准令”判 create：汉代主练染作彩色的官署；不据官名补入来源未记的平准物价职能，也不与南朝平准令合并。",
            "候选“汉代八郡漆器工官”判 update 既有 `institutions/han-dai-qiqi-zuofang-guan-yuan.md`：补八郡名单、蜀郡成都广汉工官每年各用费五百万、梓潼武都工官、乐浪铭文与铭文年代；11 种分工另见 procedure KU，不重复展开；6—8 道与 11 种分工、金属铸器铭文与漆器铭文两说并录。",
            "候选“严道木官”判 create：专事运输木材的官吏；作者“规模很大，品种繁多”标为来源判断，不当作独立数据。",
            "候选“染署”判 create 南朝染署：南朝少府下平准令避宋顺帝刘准讳改名；北朝司染署与隋唐织染署不并入本条，沿革关系来源未给。",
            "03基础书籍-md文档只读；本批写 04-knowledge/units/institutions，5 条新建、3 条更新、2 条 rejected。",
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

assert len(ledger) == 26, len(ledger)
assert len(plan) == 8, len(plan)
assert len(mapping) == 8, len(mapping)
print(json.dumps({
    "ledger": len(ledger), "plan": len(plan), "mapping": len(mapping),
    "creates": len(creates), "updates": len(updates), "rejected": len(rejects),
}, ensure_ascii=False))
