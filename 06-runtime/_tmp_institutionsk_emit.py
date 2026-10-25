import hashlib
import json
import pathlib
import subprocess

ROOT = pathlib.Path(__file__).resolve().parents[1]
PKG = ROOT / "06-runtime" / "automation" / "2026-10-25-2016xiayanjing-institutions-batch-k"
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
        "cand-02-39",
        "商代王室制陶作坊",
        "institutions/shang-royal-pottery-workshop.md",
        "新建craft_workshop：郑州商代窑场约1400平方米、陶窑14座、几十万件陶片，陶杵陶拍陶印模；白陶与明器分工",
    ),
    (
        "cand-02-42",
        "周代制陶职官",
        "institutions/zhou-pottery-officials.md",
        "新建government_office：西周制陶者称土工/搏埴之工，陶人用陶车制甗鬲、旅人用模型制簋豆；《考工记》两工种",
    ),
    (
        "cand-02-85",
        "周代染人与掌染草",
        "institutions/zhou-ranren-zhangrancao.md",
        "新建government_office：合并染人、掌染草两候选；《周礼》职业名称，从事印染与染料生产",
    ),
    (
        "cand-03-110",
        "长安东、西织室",
        "institutions/dongxi-zhishi.md",
        "新建government_office：长安东、西织室织作缯帛文绣之服；临淄、襄邑服官织工数千人",
    ),
    (
        "cand-03-68",
        "稷下学宫",
        "institutions/jixia-xuegong.md",
        "新建academy：多数学者认为《考工记》为齐国官书，作者为齐稷下学宫学者；仅承载作者归属，confidence low",
    ),
    (
        "cand-03-86",
        "秦代工室与工官",
        "institutions/qin-gongshi-gongguan.md",
        "新建government_office：秦简载朝廷有工室、县有工官及附属机构；产品质量不合格工官工师制造者受罚",
    ),
    (
        "cand-04-02",
        "秦汉官营陶窑",
        "institutions/qin-han-guan-ying-tao-yao.md",
        "新建craft_workshop：渭河官营陶窑成片烧砖瓦，始皇陵夔凤纹大瓦当直径约40厘米；西汉中叶后盛行",
    ),
    (
        "cand-04-08",
        "汉代漆器作坊官员",
        "institutions/han-dai-qiqi-zuofang-guan-yuan.md",
        "新建government_office：汉朝廷至郡国设管理漆器生产作坊官员；铭文记地点年代工序工官姓名，工序6—8道",
    ),
    (
        "cand-05-110",
        "工部",
        "institutions/gongbu.md",
        "新建government_office：《唐六典》工部尚书正三品、四属工部屯田虞部水部；掌天下百工屯田山泽政令",
    ),
    (
        "cand-05-111",
        "中尚署",
        "institutions/zhongshang-shu.md",
        "新建government_office：唐代官作金银器由中尚署下设金银作坊院生产，与民间金银行、金银铺并行；上级待核",
    ),
    (
        "cand-05-14",
        "太府寺",
        "institutions/taifu-si.md",
        "新建government_office：来源称隋代官手工业主要由工部下设的太府寺掌管；与通行九寺制度张力已标注",
    ),
    (
        "cand-06-10",
        "西夏官营手工业机构",
        "institutions/xi-xia-guan-ying-shou-gong-ye-jigou.md",
        "新建government_office：合并七机构；《天盛律令》载制金司、织绢院、铁工院、木工院、纸工院、砖瓦院、造车院",
    ),
]

updates = [
    (
        "cand-05-44",
        "染织署",
        "institutions/zhiranshu.md",
        "更新government_office：补2016知识链接L2691“染织署”异写、全国织造印染刺绣与上贡质量/技工管理、唐太宗绣师、清代三织造局连续性",
    ),
]

rejected = [
    (
        "cand-01-02",
        "南京艺术学院",
        "拒绝：南京艺术学院。来源L11-100为作者介绍，仅记夏燕靖为南京艺术学院教授及该书出版信息，无机构沿革、设计教育制度或设计实践内容；不建institution KU。若后续处理设计教育机构，应以有机构史内容的来源另立。",
    ),
    (
        "cand-01-103",
        "上海人民美术出版社",
        "拒绝：上海人民美术出版社。来源L37-69为版权页与出版发行信息，只有出版社名、地址、版次等，无机构史或设计生产内容；不建institution KU。",
    ),
    (
        "cand-03-31",
        "舟师",
        "拒绝：舟师。来源L1368-1371记楚吴越建立最早水军——舟师，并出现专门造船工场——船宫；舟师本身是军事组织，不是设计或手工业机构，船宫已有KU承载造船场；不建institution KU。",
    ),
    (
        "cand-04-69",
        "九品官位制度",
        "拒绝：九品官位制度。来源L2243记魏初曹丕采纳陈群建议制定九品官位制度，以紫绯绿三色为九品之别；这是官位等级与服色制度，不是设计机构或官营手工业组织；若立目应归制度/术语类，不建institution KU。",
    ),
]

merged = {
    "cand-02-143": ("染人", "cand-02-85", "institutions/zhou-ranren-zhangrancao.md"),
    "cand-02-144": ("掌染草", "cand-02-85", "institutions/zhou-ranren-zhangrancao.md"),
}

# ledger in candidate order
order = [
    "cand-01-02", "cand-01-103", "cand-02-143", "cand-02-144", "cand-02-39",
    "cand-02-42", "cand-02-85", "cand-03-110", "cand-03-31", "cand-03-68",
    "cand-03-86", "cand-04-02", "cand-04-08", "cand-04-69", "cand-05-110",
    "cand-05-111", "cand-05-14", "cand-05-44", "cand-06-10",
]
assert len(order) == 19

create_map = {c[0]: c for c in creates}
update_map = {u[0]: u for u in updates}
reject_map = {r[0]: r for r in rejected}

ledger = []
for n in order:
    if n in reject_map:
        _, title, reason = reject_map[n]
        ledger.append({
            "candidate_id": cid(n),
            "expected_state": "needs_evidence",
            "state": "rejected",
            "decision": {"status": "rejected", "reason": reason, "decided_by": "Agent", "decided_at": DATE},
            "updated_at": DATE,
        })
        continue
    if n in merged:
        title, canon, target = merged[n]
        verb = "并入"
        reason1 = f"已完成语义复读：并入 {target}"
        reason2 = f"canonical 候选语义复读完成，批准并入 {target}"
        reason3 = f"并入 {cid(canon)} 同一实体：{title} 与周代染人、掌染草同指《周礼》一句证据，统一以周代染人与掌染草立目"
    elif n in create_map:
        _, title, target, note = create_map[n]
        verb = "新建"
        reason1 = f"已完成语义复读：新建 {target}"
        reason2 = f"canonical 候选语义复读完成，批准新建 {target}"
        reason3 = f"已判定 applied：新建 {target}"
    else:
        _, title, target, note = update_map[n]
        verb = "更新"
        reason1 = f"已完成语义复读：更新 {target}"
        reason2 = f"canonical 候选语义复读完成，批准更新 {target}"
        reason3 = f"已判定 applied：更新 {target}"
    ledger.append({
        "candidate_id": cid(n), "expected_state": "needs_evidence", "state": "ready_for_review",
        "decision": {"status": "pending", "reason": reason1, "decided_by": "Agent", "decided_at": DATE},
        "updated_at": DATE,
    })
    ledger.append({
        "candidate_id": cid(n), "expected_state": "ready_for_review", "state": "approved",
        "decision": {"status": "approved", "reason": reason2, "decided_by": "Agent", "decided_at": DATE},
        "updated_at": DATE,
    })
    ledger.append({
        "candidate_id": cid(n), "expected_state": "approved", "state": "applied",
        "decision": {"status": "approved", "reason": reason3, "decided_by": "Agent", "decided_at": DATE},
        "updated_at": DATE, "target_ref": f"04-knowledge/units/{target}",
    })

plan = []
for n, title, target, note in creates:
    p = ROOT / "04-knowledge" / "units" / target
    f = fp(p)
    plan.append({
        "action": "create", "target_ref": f"04-knowledge/units/{target}", "candidate_id": cid(n),
        "entity": title, "before": None, "after_sha256": f["sha256"], "bytes": f["bytes"],
        "lines": f["lines"], "note": note,
    })
for n, title, target, note in updates:
    p = ROOT / "04-knowledge" / "units" / target
    rel = f"04-knowledge/units/{target}"
    before = fp_bytes(subprocess.check_output(["git", "show", f"HEAD:{rel}"], cwd=ROOT))
    after = fp(p)
    plan.append({
        "action": "update", "target_ref": rel, "candidate_id": cid(n), "entity": title,
        "before": before, "after_sha256": after["sha256"], "bytes": after["bytes"],
        "lines": after["lines"], "note": note,
    })

mapping = []
for n, title, target, note in creates:
    entry = {
        "entity": title, "target_ref": f"04-knowledge/units/{target}", "action": "create",
        "canonical_candidate": cid(n), "merged_candidates": [],
    }
    if n == "cand-02-85":
        entry["merged_candidates"] = [cid("cand-02-143"), cid("cand-02-144")]
    mapping.append(entry)
for n, title, target, note in updates:
    mapping.append({
        "entity": title, "target_ref": f"04-knowledge/units/{target}", "action": "update",
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
    "goal": "处理夏燕靖《中国艺术设计史（升级版）》2016 册 institution 候选第一组（先秦至西夏）19 个：12 个新建、1 个更新、4 个 rejected；染人、掌染草并入周代染人与掌染草。",
    "status": "applied",
    "date": DATE,
    "inputs": {
        "candidate_index": {
            "path": "06-runtime\\state\\candidate-index.jsonl",
            "rows_before": 5339,
            "sha256_before": "sha256:11c953156359976c341e07e27c9c59fef9ea19cca38a41a5f5d4d558e6343f87",
            "sha256_scope": "CRLF→LF 归一后",
            "counts_before": {"applied": 804, "needs_evidence": 3682, "no_delta": 50, "rejected": 803},
        },
        "source": {
            "doc_id": DOC,
            "file": "03基础书籍-md文档/中国艺术设计史（升级版）_夏燕靖_2016_上海人民美术出版社.md",
            "spans": ["L11-L100", "L872-L879", "L971-L990", "L1368-L1371", "L1536-L1555", "L1622-L1634", "L1731-L1736", "L1808-L1855", "L1860-L1870", "L2243", "L2506-L2511", "L2675-L2702", "L2790-L2795", "L3012-L3021", "L3092-L3124"],
        },
    },
    "method": {
        "rules": [
            "institution 候选按实体而非 slug 对账：先与既有 37 个 institution KU 的标题、别名和正文对齐，再定 create／update／no_delta／rejected。",
            "职官、职业名与机构名混称时，只有能承载机构或职官制度内容者建 institution；纯作者单位、出版社、军事组织、官位等级判 rejected。",
            "同一句证据下的染人、掌染草与周代染人与掌染草合并为一个实体，保留 merged_candidates 映射。",
            "来源只给一句隶属关系、机构本体信息不足者，降低 confidence 并在正文标注证据边界，不以来源外知识补写。",
            "来源表述与通行制度史有张力时（太府寺“工部下设”、东西织室“东汉”与长安），照录并标注，不据通行说法改写。",
            "03基础书籍-md文档只读；本批写 04-knowledge/units/institutions，12 条新建、1 条更新。",
        ],
    },
    "outputs": {
        "apply_plan": {"path": f"06-runtime\\automation\\{PKG.name}\\apply-plan.jsonl", "rows": len(plan), "create": len(creates), "update": len(updates)},
        "ledger": {"path": f"06-runtime\\automation\\{PKG.name}\\candidate-decision-ledger.jsonl", "rows": len(ledger), "candidates": len(order), "applied": len(creates) + len(updates) + len(merged), "no_delta": 0, "rejected": len(rejected)},
        "canonical_mapping": {"path": f"06-runtime\\automation\\{PKG.name}\\canonical-mapping.json", "entries": len(mapping), "merged_candidates": [cid("cand-02-143"), cid("cand-02-144")]},
    },
    "state_after": {},
}
(PKG / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

assert len(ledger) == 49, len(ledger)
assert len(plan) == 13, len(plan)
assert len(mapping) == 13, len(mapping)
print(json.dumps({"ledger": len(ledger), "plan": len(plan), "mapping": len(mapping), "creates": len(creates), "updates": len(updates), "rejected": len(rejected)}, ensure_ascii=False))
