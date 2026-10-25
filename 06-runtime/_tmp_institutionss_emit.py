import hashlib
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
PKG = ROOT / "06-runtime" / "automation" / "2026-10-25-2009zhaonong-institutions-batch-s"
PKG.mkdir(parents=True, exist_ok=True)
DOC = "2009-zhaonong-zhongguo-yishu-shejishi"
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
        "cand-12-27",
        "纶章造纸局",
        "04-knowledge/units/institutions/lunzhang-zaozhi-ju.md",
        "新建commercial_enterprise：1891年李鸿章创建，为中国近代第一家引进国外造纸技术的工场；来源未给地点，既有现代造纸技术条目作“上海”，本条标待核",
    ),
    (
        "cand-12-29",
        "广州造纸厂",
        "04-knowledge/units/institutions/guangzhou-zaozhichang.md",
        "新建commercial_enterprise：民国时期能产一定数量新闻纸，因依赖进口纸浆，抗战爆发后无法规模化生产；来源未给创设年份、设备、产量与战后结局",
    ),
    (
        "cand-12-38",
        "英美烟草公司",
        "04-knowledge/units/institutions/yingmei-yancao-gongsi.md",
        "新建commercial_enterprise：五册来源合记招贴、哈德门/老刀牌/红锡包、月份牌、包装、规模最大的广告部与中国画家名单、驻厂设计师；并录“丁纳/丁讷”与张光宇身份差异",
    ),
    (
        "cand-12-68",
        "中国人民银行",
        "04-knowledge/units/institutions/zhongguo-renmin-yinhang.md",
        "新建government_office：1948年12月首次发行人民币，已发行5套，元角分、十进位、铸币与纸币、按时更新、引进技术、防伪设计；来源未给行址、隶属与各套年份",
    ),
    (
        "cand-12-85",
        "福州马尾船政学堂绘事院",
        "04-knowledge/units/institutions/fuzhou-mawei-chuanzheng-xuetang-huishiyuan.md",
        "新建design_school：1867年在福州马尾船政学堂设立绘事院，与1888年江南船政局工艺学堂并列为中国设计教育起点；与既有福建船政局条不重复",
    ),
    (
        "cand-12-86",
        "江南船政局工艺学堂",
        "04-knowledge/units/institutions/jiangnan-chuanzhengju-gongyi-xuetang.md",
        "新建design_school：1888年江南船政局开办工艺学堂，为设计教育起点之一；“江南船政局”所指未明，与江南制造总局的关系待核，不作等同",
    ),
    (
        "cand-12-92",
        "北平国立艺专",
        "04-knowledge/units/institutions/beiping-guoli-yizhuan.md",
        "新建design_school：1949年以前设工艺/实用美术专业，北平国立艺专图案系与杭州国立艺专图案系并列最具实力；来源未给创办年份、课程与师资",
    ),
    (
        "cand-12-93",
        "杭州国立艺专",
        "04-knowledge/units/institutions/hangzhou-guoli-yizhuan.md",
        "新建design_school：图案系最具实力，1950年改名中央美术学院华东分院、实用美术系并入中央美术学院，1956年成立中央工艺美术学院；田自秉记求学经历；并录校名与段首异常",
    ),
    (
        "cand-12-95",
        "无锡、大连、北京、西北轻工学院",
        "04-knowledge/units/institutions/qinggongbu-qinggong-xueyuan.md",
        "新建design_school（院校群，1个候选并列四校）：四校与中央工艺美术学院同属轻工部，但从工业产品设计角度注重教学与市场调研，教学方向各有侧重",
    ),
    (
        "cand-12-137",
        "大生纱厂",
        "04-knowledge/units/institutions/dasheng-shachang.md",
        "新建commercial_enterprise：1899年张謇在南通创办，后办二/三/八厂；高丰作实业成就、赵农作“官商一体”反例，两册评价相反并录",
    ),
    (
        "cand-12-165",
        "伊文思图书公司",
        "04-knowledge/units/institutions/yiwensi-tushu-gongsi.md",
        "新建commercial_enterprise：1926年上海南京路出现销售打字机广告；高丰作“霓虹灯/橱窗/南京东路”，赵农作“吊灯广告/南京路”，两说并录",
    ),
]

order = [
    "cand-12-27", "cand-12-29", "cand-12-38", "cand-12-68",
    "cand-12-85", "cand-12-86", "cand-12-92", "cand-12-93",
    "cand-12-95", "cand-12-137", "cand-12-165",
]
assert len(order) == 11
assert [c[0] for c in creates] == order

create_map = {c[0]: c for c in creates}

ledger = []
for n in order:
    _, title, target, note = create_map[n]
    ledger.append({
        "candidate_id": cid(n), "expected_state": "needs_evidence", "state": "ready_for_review",
        "decision": {"status": "pending", "reason": f"已完成语义复读：新建 {target}", "decided_by": "Agent", "decided_at": DATE},
        "updated_at": DATE,
    })
    ledger.append({
        "candidate_id": cid(n), "expected_state": "ready_for_review", "state": "approved",
        "decision": {"status": "approved", "reason": f"canonical 候选语义复读完成，批准新建 {target}", "decided_by": "Agent", "decided_at": DATE},
        "updated_at": DATE,
    })
    ledger.append({
        "candidate_id": cid(n), "expected_state": "approved", "state": "applied",
        "decision": {"status": "approved", "reason": f"已判定 applied：新建 {target}", "decided_by": "Agent", "decided_at": DATE},
        "updated_at": DATE, "target_ref": target,
    })

plan = []
for n, title, target, note in creates:
    f = fp(ROOT / target)
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

with (PKG / "candidate-decision-ledger.jsonl").open("w", encoding="utf-8", newline="\n") as f:
    for row in ledger:
        f.write(json.dumps(row, ensure_ascii=False) + "\n")
with (PKG / "apply-plan.jsonl").open("w", encoding="utf-8", newline="\n") as f:
    for row in plan:
        f.write(json.dumps(row, ensure_ascii=False) + "\n")
(PKG / "canonical-mapping.json").write_text(json.dumps(mapping, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

manifest = {
    "work_package": PKG.name,
    "goal": "处理赵农《中国艺术设计史》2009 册 institution 候选 11 个：11 个新建、0 个更新、0 个 no_delta、0 个 rejected。",
    "status": "applied",
    "date": DATE,
    "inputs": {
        "candidate_index": {
            "path": "06-runtime\\state\\candidate-index.jsonl",
            "rows_before": 5339,
            "sha256_before": "sha256:69d4e8658b17451b7b9a2f186948640e321aa32a66c0aa865a6d4da8ecd5902a",
            "sha256_scope": "CRLF→LF 归一后",
            "counts_before": {"applied": 876, "needs_evidence": 3599, "no_delta": 56, "rejected": 808},
        },
        "source": {
            "doc_id": DOC,
            "file": "03基础书籍-md文档/中国艺术设计史_赵农_2009_高等教育出版社.md",
            "spans": [
                "L8137-L8150", "L8166-L8221", "L8248-L8266",
                "L8359-L8409", "L8484-L8560",
            ],
        },
    },
    "method": {
        "rules": [
            "institution 候选按实体对账：先与既有 institution KU 的标题、别名与正文对齐，再定 create／update／no_delta／rejected。",
            "候选“纶章造纸局”按近代机器造纸工场立目：1891 年李鸿章创建、中国近代第一家引进国外造纸技术的工场；来源未给地点，既有现代造纸技术条目的“上海”不作本条依据，标待核。",
            "候选“广州造纸厂”按民国造纸厂立目：能产一定数量新闻纸、依赖进口纸浆、抗战爆发后无法规模化生产；不补创设年份、设备与战后结局。",
            "候选“英美烟草公司”按近代外资烟草公司立目，合五册来源：招贴与品牌、月份牌、包装、规模最大的广告部与中国画家名单、驻厂设计师；丁纳／丁讷与张光宇身份差异并录，不裁断。",
            "候选“中国人民银行”按国家货币发行机构立目：1948 年 12 月首次发行人民币、5 套、元角分十进位、铸币与纸币、更新、技术引进与防伪；同段民国货币背景与本机构沿革分开。",
            "候选“福州马尾船政学堂绘事院”按船政学堂内设绘图教育机构立目：1867 年设立；与既有福建船政局条不重复，该条记船政局与求实堂艺局而未记绘事院。",
            "候选“江南船政局工艺学堂”按 1888 年工艺学堂立目；来源“江南船政局”所指未明，不与既有江南制造总局条等同，地点与上级机构标待核。",
            "候选“北平国立艺专”按民国国立美术专科学校立目：1949 年以前设工艺／实用美术专业，图案系与杭州国立艺专并列最具实力；不补创办年份与课程。",
            "候选“杭州国立艺专”按民国国立美术专科学校立目：图案系实力、1950 年改名中央美术学院华东分院、实用美术系并入中央美术学院、1956 年中央工艺美术学院成立；校名两写与段首标题异常并录。",
            "候选“无锡、大连、北京、西北轻工学院”为 1 个候选并列四校，按院校群立目：与中央工艺美术学院同属轻工部，但侧重工业产品设计与市场调研；不拆成四条。",
            "候选“大生纱厂”按近代纺织企业立目：1899 年张謇在南通创办、后办二／三／八厂；高丰“实业成就”与赵农“官商一体”评价相反，并录为史学立场差异。",
            "候选“伊文思图书公司”按上海图书公司立目：1926 年打字机广告；高丰作霓虹灯／橱窗／南京东路，赵农作吊灯广告／南京路，两说并录。",
            "03基础书籍-md文档只读；本批写 04-knowledge/units/institutions，11 条新建、0 条更新、0 条 rejected。",
        ],
    },
    "outputs": {
        "apply_plan": {"path": f"06-runtime\\automation\\{PKG.name}\\apply-plan.jsonl", "rows": len(plan), "create": len(creates), "update": 0},
        "ledger": {"path": f"06-runtime\\automation\\{PKG.name}\\candidate-decision-ledger.jsonl", "rows": len(ledger), "candidates": len(order), "applied": len(creates), "no_delta": 0, "rejected": 0},
        "canonical_mapping": {"path": f"06-runtime\\automation\\{PKG.name}\\canonical-mapping.json", "entries": len(mapping), "merged_candidates": []},
    },
    "state_after": {},
}
(PKG / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

assert len(ledger) == 33, len(ledger)
assert len(plan) == 11, len(plan)
assert len(mapping) == 11, len(mapping)
print(json.dumps({
    "ledger": len(ledger), "plan": len(plan), "mapping": len(mapping),
    "creates": len(creates), "updates": 0, "rejected": 0,
}, ensure_ascii=False))
