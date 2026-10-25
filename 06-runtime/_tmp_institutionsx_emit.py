import hashlib
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
PKG = ROOT / "06-runtime" / "automation" / "2026-10-25-2011lilixin-institutions-batch-x"
PKG.mkdir(parents=True, exist_ok=True)
DOC = "2011-lilixin-zhongguo-sheji-yishu-shilun"
DATE = "2026-10-25"


def fp(path: pathlib.Path) -> dict:
    raw = path.read_bytes()
    text = raw.decode("utf-8").replace("\r\n", "\n").replace("\r", "\n")
    data = text.encode("utf-8")
    return {
        "sha256": "sha256:" + hashlib.sha256(data).hexdigest(),
        "bytes": len(data),
        "lines": text.count("\n"),
    }


creates = [
    {
        "candidate_id": f"{DOC}:cand-01-11",
        "entity": "国务院学位委员会",
        "target_ref": "04-knowledge/units/institutions/guowuyuan-xuewei-weiyuanhui.md",
        "note": "新建government_office：李立新 L179-L181 记本科目录用“艺术设计”、研究生目录用“设计艺术”，作者判二者内涵相同、通用；补夏燕靖 2016 L5905 记 1986 年 7 月批准中央工艺美术学院博士学位授予点，高丰 2004 L136-L140 题署记张道一为艺术学科评议组召集人；1998 年两次目录调整另见事件条目，不重复",
    },
    {
        "candidate_id": f"{DOC}:cand-01-43",
        "entity": "中央历史语言研究所",
        "target_ref": "04-knowledge/units/institutions/zhongyang-lishi-yuyan-yanjiusuo.md",
        "note": "新建research_institute：李立新 L283 记傅斯年主持该所，倡导“上穷碧落下黄泉，动手动脚找东西”，引“一分材料出一分货”与“史学便是史料学”三句话；来源只作史学方法例证，未给成立年份、隶属、所址、组织与人员，confidence 定为 low",
    },
    {
        "candidate_id": f"{DOC}:cand-01-56",
        "entity": "东南大学",
        "target_ref": "04-knowledge/units/institutions/southeast-university.md",
        "note": "新建academy：李立新 L341 记 1994 年 6 月张道一倡导组建我国第一个艺术学系，L2446-L2448 记李立新 1999 年 9 月入学、2002 年 6 月 15 日答辩；补高丰 2004 题署记张道一为艺术学系主任，夏燕靖 2016 L6021 记 1995 年计算机艺术会议承办；候选合并 cand-06-03，设立、答辩、会议三个事件分记",
    },
    {
        "candidate_id": f"{DOC}:cand-02-91",
        "entity": "瑞典远东古物博物馆",
        "target_ref": "04-knowledge/units/institutions/swedish-museum-of-far-eastern-antiquities.md",
        "note": "新建museum：李立新 L794 只一句，记该馆藏中国青铜钺，钺上丝织物残痕为平纹底起菱形花纹的提花织物；来源只作提花技术证据，未给馆史、藏品总目与入藏信息，confidence 定为 low；英文名按该馆通名，名实对应待外部核对",
    },
    {
        "candidate_id": f"{DOC}:cand-03-21",
        "entity": "正仓院",
        "target_ref": "04-knowledge/units/institutions/shosoin.md",
        "note": "新建museum：李立新 L1020-L1023 记日本奈良正仓院所藏中国设计物品可证中国造物东传日本；补田自秉 2010 L3254、L3392 记唐代夹缬屏风与螺钿琵琶、阮咸，高丰 2004 L2998 记 55 面唐代铜镜，夏燕靖 2009 L2148 称“奈良东大寺正仓院”并记夹缬屏风；四源称法并存，不写日本寺院史",
    },
    {
        "candidate_id": f"{DOC}:cand-03-22",
        "entity": "宋代宫廷画院",
        "target_ref": "04-knowledge/units/institutions/song-dai-huayuan.md",
        "note": "新建government_office：李立新 L1155-L1157 记宋代宫廷画院、院体画及对文思院、甲库、文绣院、绫锦院等工艺机构的影响；与既有 events/song-dai-huayuan-sheli.md 分工为“机构本体”与“设立事件”，不判 no_delta，因类型与指称侧面不同",
    },
    {
        "candidate_id": f"{DOC}:cand-03-23",
        "entity": "清江船厂",
        "target_ref": "04-knowledge/units/institutions/qingjiang-chuanchang.md",
        "note": "新建government_office：李立新 L1204 引《漕船志》记 8,873 名工匠、七类工种与十六府及“军余工办”征调；夏燕靖 2009 L3750、2016 L4607 记江苏淮南清江船厂主要造内河漕船、也造部分海船；明初官营 2 万余人、年造 3,000 余只为合计，不归本厂；与龙江船厂分记",
    },
    {
        "candidate_id": f"{DOC}:cand-04-11",
        "entity": "成衣公所",
        "target_ref": "04-knowledge/units/institutions/chengyi-gongsuo.md",
        "note": "新建professional_society：李立新 L1261 引《长州县禁止无业游民在成衣公所寻衅滋扰碑》，判当时已有专业衣工与成衣业行会；来源未给成立年份、公所址、行规、成员、经费与存续时间，未引碑文，confidence 定为 low；同段江南成衣业背景不归公所",
    },
    {
        "candidate_id": f"{DOC}:cand-04-17",
        "entity": "江南制造局",
        "target_ref": "04-knowledge/units/institutions/jiangnan-zhizao-zongju.md",
        "note": "更新既有jiangnan-zhizao-zongju：既有条目已记 1865 年创办、曾国藩／李鸿章、兵工厂、造船与 1868 年翻译馆；补李立新 2011 L1293 记上海江南制造局自创办至 1904 年生产机器设备 467 台（座）、零件及工具 115.3 万件，并置于官办企业制造枪炮、轮船与机器设备的序列；source_count 3→4、version 2→3，alias 增江南制造局、上海江南制造局",
    },
    {
        "candidate_id": f"{DOC}:cand-04-25",
        "entity": "中国商业美术作家协会",
        "target_ref": "04-knowledge/units/institutions/china-commercial-art-writers-association.md",
        "note": "新建professional_society：李立新 L1313 记 1934 年上海成立，入会者 500 余人，同年办展览，先后出版工商业美术作品选集两辑；同段尚美图案馆、大熊工商美术社、上海美术供应社与月份牌画家工作室不并入；来源写作“庞薰栗”，照录并标原文如此",
    },
    {
        "candidate_id": f"{DOC}:cand-05-09",
        "entity": "宫廷玻璃厂",
        "target_ref": "04-knowledge/units/institutions/neiwufu-zaobanchu.md",
        "note": "更新既有neiwufu-zaobanchu：既有条目已据高丰 2004 列造办处下设玻璃厂，但无玻璃厂细节；补李立新 2011 L1683 记康熙时设宫廷玻璃厂、雇用欧洲工匠制造精细工艺品、玻璃器生产恢复，并区分博山作坊与近代大型玻璃厂；李立新未明说隶属造办处，按高丰所记合并，名实待考；source_count 4→5、version 3→4，不另建 gongting-boli-chang",
    },
]

updates = {
    "04-knowledge/units/institutions/jiangnan-zhizao-zongju.md": {
        "sha256": "sha256:126c9a3037f01218cfde85650d53762282a1b7734168b91badfe84dce5645767",
        "bytes": 6039,
        "lines": 100,
    },
    "04-knowledge/units/institutions/neiwufu-zaobanchu.md": {
        "sha256": "sha256:6740bbbaa34f21d6d21ba22935d6c0f35498d88f6423562066e07247a95ee385",
        "bytes": 8829,
        "lines": 120,
    },
}

created = {c["candidate_id"] for c in creates}

ledger = []
for c in creates:
    cid = c["candidate_id"]
    target = c["target_ref"]
    action_word = "新建" if target not in updates else "更新"
    ledger.append({
        "candidate_id": cid,
        "expected_state": "needs_evidence",
        "state": "ready_for_review",
        "decision": {
            "status": "pending",
            "reason": f"已完成语义复读：{action_word} {target}",
            "decided_by": "Agent",
            "decided_at": DATE,
        },
        "updated_at": DATE,
    })
    ledger.append({
        "candidate_id": cid,
        "expected_state": "ready_for_review",
        "state": "approved",
        "decision": {
            "status": "approved",
            "reason": f"canonical 候选语义复读完成，批准{action_word} {target}",
            "decided_by": "Agent",
            "decided_at": DATE,
        },
        "updated_at": DATE,
    })
    ledger.append({
        "candidate_id": cid,
        "expected_state": "approved",
        "state": "applied",
        "decision": {
            "status": "approved",
            "reason": f"已判定 applied：{action_word} {target}",
            "decided_by": "Agent",
            "decided_at": DATE,
        },
        "updated_at": DATE,
        "target_ref": target,
    })

plan = []
for c in creates:
    target = c["target_ref"]
    f = fp(ROOT / target)
    plan.append({
        "action": "update" if target in updates else "create",
        "target_ref": target,
        "candidate_id": c["candidate_id"],
        "entity": c["entity"],
        "before": updates.get(target),
        "after_sha256": f["sha256"],
        "bytes": f["bytes"],
        "lines": f["lines"],
        "note": c["note"],
    })

mapping = []
for c in creates:
    merged = []
    if c["candidate_id"] == f"{DOC}:cand-01-56":
        merged = [f"{DOC}:cand-06-03"]
    mapping.append({
        "entity": c["entity"],
        "target_ref": c["target_ref"],
        "action": "update" if c["target_ref"] in updates else "create",
        "canonical_candidate": c["candidate_id"],
        "merged_candidates": merged,
    })

assert len(ledger) == 33, len(ledger)
assert len(plan) == 11, len(plan)
assert sum(1 for r in plan if r["action"] == "create") == 9
assert sum(1 for r in plan if r["action"] == "update") == 2
assert len(mapping) == 11
assert len({r["target_ref"] for r in plan}) == 11

(PKG / "candidate-decision-ledger.jsonl").write_text(
    "\n".join(json.dumps(r, ensure_ascii=False) for r in ledger) + "\n", encoding="utf-8"
)
(PKG / "apply-plan.jsonl").write_text(
    "\n".join(json.dumps(r, ensure_ascii=False) for r in plan) + "\n", encoding="utf-8"
)
(PKG / "canonical-mapping.json").write_text(
    json.dumps(mapping, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
)

manifest = {
    "work_package": "2026-10-25-2011lilixin-institutions-batch-x",
    "goal": "处理李立新《中国设计艺术史论》2011 册 institution 候选 11 个：9 个新建、2 个更新、0 个 no_delta、0 个 rejected。",
    "status": "applied",
    "date": DATE,
    "inputs": {
        "candidate_index": {
            "path": "06-runtime\\state\\candidate-index.jsonl",
            "rows_before": 5339,
            "sha256_before": "sha256:d4acbebb5344a706051add749ada42c0817bc1ce735aaedc6d927182232687c8",
            "sha256_scope": "CRLF→LF 归一后",
            "counts_before": {
                "applied": 919,
                "needs_evidence": 3551,
                "no_delta": 57,
                "rejected": 812,
            },
        },
        "source": {
            "doc_id": DOC,
            "file": "03基础书籍-md文档/中国设计艺术史论_李立新_2011_人民出版社.md",
            "spans": [
                "L179-L181",
                "L283",
                "L341, L2446-L2448",
                "L794",
                "L1020-L1023",
                "L1155-L1157",
                "L1204",
                "L1261",
                "L1293",
                "L1313",
                "L1683",
            ],
        },
    },
    "method": {
        "rules": [
            "institution 候选按实体对账：先与既有 institution KU 的标题、别名与正文对齐，再定 create／update／no_delta／rejected。",
            "候选“国务院学位委员会”判 create：李立新 L179-L181 记其在本科目录用“艺术设计”、研究生目录用“设计艺术”，作者判二者内涵相同、通用；补夏燕靖 2016 L5905 的 1986 年学位授权与高丰 2004 L136-L140 的学科评议职务；1998 年两次目录调整已由事件条目承载，不在本条重复。",
            "候选“中央历史语言研究所”判 create：李立新 L283 记傅斯年主持该所、倡导“上穷碧落下黄泉，动手动脚找东西”，并引“一分材料出一分货”与“史学便是史料学”三句话；来源只作史学方法例证，未给成立年份、隶属、所址、组织与人员，confidence 定为 low。",
            "候选“东南大学”判 create：候选合并 cand-06-03；李立新 L341 记 1994 年 6 月张道一倡导组建我国第一个艺术学系，L2446-L2448 记李立新 1999 年 9 月入学、2002 年 6 月 15 日答辩；补高丰 2004 题署的“东南大学艺术学系主任”与夏燕靖 2016 L6021 的 1995 年计算机艺术会议承办；设立、答辩、会议三个事件分记，本条只登记学校与艺术学系本体。",
            "候选“瑞典远东古物博物馆”判 create：李立新 L794 只一句，记该馆藏中国青铜钺、钺上丝织物残痕为平纹底起菱形花纹的提花织物；来源只作提花技术证据，未给馆史、藏品总目与入藏信息，confidence 定为 low；英文名按该馆通名，来源未给英译，名实对应待外部核对。",
            "候选“正仓院”判 create：李立新 L1020-L1023 记日本奈良正仓院所藏中国设计物品可证中国造物东传日本；补田自秉 2010 L3254、L3392 的唐代夹缬屏风与螺钿琵琶、阮咸，高丰 2004 L2998 的 55 面唐代铜镜，夏燕靖 2009 L2148 的“奈良东大寺正仓院”称法与夹缬屏风；四源称法并存，不写日本寺院史或藏品总目。",
            "候选“宋代宫廷画院”判 create：李立新 L1155-L1157 记宋代宫廷画院、院体画及对文思院、甲库、文绣院、绫锦院等工艺机构的影响；既有 `events/song-dai-huayuan-sheli.md` 记同一来源的设立事件，本条与其分工为“机构本体”与“设立事件”，不判 no_delta，因 type 与指称侧面不同。",
            "候选“清江船厂”判 create：李立新 L1204 引《漕船志》记 8,873 名工匠、七类工种与十六府及“军余工办”征调；夏燕靖 2009 L3750、2016 L4607 记江苏淮南清江船厂主要造内河漕船、也造部分海船；明初官营 2 万余人、年造 3,000 余只是合计，不归本厂；与南京龙江船厂分记。",
            "候选“成衣公所”判 create：李立新 L1261 引《长州县禁止无业游民在成衣公所寻衅滋扰碑》，判当时已有专业衣工与成衣业行会；来源未给成立年份、公所址、行规、成员、经费与存续时间，未引碑文，confidence 定为 low；同段江南成衣业与衣庄背景不归公所。",
            "候选“江南制造局”判 update 既有 `institutions/jiangnan-zhizao-zongju.md`：既有条目已记 1865 年创办、曾国藩／李鸿章、兵工厂、造船与 1868 年翻译馆；补李立新 2011 L1293 的 1904 年前产量与官办企业定位，source_count 3→4、version 2→3，alias 增“江南制造局”“上海江南制造局”，不另建重复条目。",
            "候选“中国商业美术作家协会”判 create：李立新 L1313 记 1934 年上海成立、入会者 500 余人、同年办展览、先后出版工商业美术作品选集两辑；同段尚美图案馆、大熊工商美术社、上海美术供应社与月份牌画家工作室不并入；来源写作“庞薰栗”，照录并标“原文如此”。",
            "候选“宫廷玻璃厂”判 update 既有 `institutions/neiwufu-zaobanchu.md`：既有条目已据高丰 2004 列造办处下设玻璃厂但无细节；补李立新 2011 L1683 的康熙时设厂、雇用欧洲工匠、玻璃器生产恢复，并区分博山作坊与近代大型玻璃厂；李立新未明说隶属造办处，按高丰所记合并，名实待考；source_count 4→5、version 3→4，不另建 `gongting-boli-chang`。",
            "03基础书籍-md文档只读；本批写 04-knowledge/units/institutions，9 条新建、2 条更新；不 commit、不 push。",
        ]
    },
    "outputs": {
        "apply_plan": {
            "path": "06-runtime\\automation\\2026-10-25-2011lilixin-institutions-batch-x\\apply-plan.jsonl",
            "rows": 11,
            "create": 9,
            "update": 2,
        },
        "ledger": {
            "path": "06-runtime\\automation\\2026-10-25-2011lilixin-institutions-batch-x\\candidate-decision-ledger.jsonl",
            "rows": 33,
            "candidates": 11,
            "applied": 11,
            "no_delta": 0,
            "rejected": 0,
        },
        "canonical_mapping": {
            "path": "06-runtime\\automation\\2026-10-25-2011lilixin-institutions-batch-x\\canonical-mapping.json",
            "entries": 11,
            "merged_candidates": [f"{DOC}:cand-06-03"],
        },
    },
    "state_after": {
        "applied": 930,
        "needs_evidence": 3540,
        "no_delta": 57,
        "rejected": 812,
        "total": 5339,
    },
}

(PKG / "manifest.json").write_text(
    json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
)

print(json.dumps({
    "ledger_rows": len(ledger),
    "plan_rows": len(plan),
    "create": sum(1 for r in plan if r["action"] == "create"),
    "update": sum(1 for r in plan if r["action"] == "update"),
    "mapping_entries": len(mapping),
    "pkg": str(PKG),
}, ensure_ascii=False, indent=2))
