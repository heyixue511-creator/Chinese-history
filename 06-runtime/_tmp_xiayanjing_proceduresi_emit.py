# -*- coding: utf-8 -*-
"""Emit ledger, apply-plan, canonical mapping and manifest for Xia Yanjing 2016 procedure batch I."""
import hashlib
import json
from pathlib import Path

import yaml

ROOT = Path(".")
BATCH = Path("06-runtime/automation/2026-10-25-2016xiayanjing-procedures-batch-i")
BATCH.mkdir(parents=True, exist_ok=True)
PREFIX = "2016-xiayanjing-zhongguo-yishu-shejishi-upgrade:"
DATE = "2026-10-25"

CREATES = [
    ("cand-01-74", "sunmao-jiegou", "榫卯结构", "woodworking_technique", "榫卯结构",
     "干栏式建筑采用榫卯结构；来源仅一句，未展开类型与工序"),
    ("cand-02-23", "hunzhu-fa", "浑铸法", "metalworking_technique", "浑铸法",
     "浑铸法即整体浇铸，曾侯乙编钟 65 枚均用此法，并施分范合铸、复印花纹"),
    ("cand-02-24", "fenshi-fa", "焚失法", "metalworking_technique", "焚失法",
     "商代中晚期焚失法，学界假说失蜡法源于焚失法；来源未述工艺过程"),
    ("cand-02-66", "paituo-gufeng", "排橐鼓风", "metalworking_technique", "排橐鼓风",
     "春秋末年排橐：牛皮大皮囊、囊柄、人力推动、竹管通炉，大炉需 300 人"),
    ("cand-03-73", "chelun-jiance-fa", "车轮检测法", "woodworking_technique", "车轮检测法",
     "《考工记》两条车轮检测：等大圆盘验密合、悬线验辐条平直"),
    ("cand-03-97", "diezhu-jishu", "叠铸技术", "metalworking_technique", "叠铸技术",
     "东汉叠铸：温县烘范窑 500 多套泥范，一次铸几个或几十件，双孔改单孔"),
    ("cand-03-98", "shuili-gufeng", "水力鼓风冶铁", "metalworking_technique", "水力鼓风冶铁",
     "东汉初年南阳水力鼓风炉，水力转机械使皮囊张缩给高炉加氧"),
]

UPDATES = [
    ("cand-01-22", "shiqi-dazhi-sanfa", "石器打制三法", "stoneworking_technique", "石器打制三法",
     "补入夏燕靖 2016 元谋、蓝田、北京、丁村、峙峪、下川的石器序列与第二步加工、细石器、三棱尖状石器"),
    ("cand-01-29", "mozhi-shiqi", "磨制石器", "stoneworking_technique", "磨制石器",
     "补入夏燕靖 2016 升级版同段与磁山、裴李岗早期代表"),
    ("cand-02-68", "sheng-tie-rou-hua-ji-shu", "生铁柔化技术", "metalworking_technique", "生铁柔化技术",
     "补入夏燕靖 2016 升级版同段及河北易县农具“铁鐏／铁鏤”版本用字差异"),
    ("cand-03-13", "dyeing", "染色", "textile_technique", "染色",
     "补入夏燕靖 2016 练染业 7 工官、练染过程环节与“幞人／慌人”用字差异"),
]

NO_DELTA = [
    ("cand-01-39", "lunzhi-fa", "轮制法",
     "2016 升级版同段与 2009 版基本一致，既有 KU 已据 2009 版完整收录轮制工序、慢轮与器物特征，无新增语义"),
    ("cand-02-19", "hefan-fa", "合范法",
     "2016 升级版同段与 2009 版基本一致，既有 KU 已据 2009 版及田自秉、李立新完整收录合范工序，无新增语义"),
    ("cand-02-73", "yin-wen-mo-yin", "印纹（模印）装饰",
     "2016 升级版同段与 2009 版基本一致，既有 KU 已据 2009 版及田自秉完整收录印纹工序与纹样格式演变，无新增语义"),
]

BEFORE = json.loads(Path("06-runtime/_tmp_pre_i_hashes.json").read_text(encoding="utf-8"))


def fingerprint(path: Path):
    data = path.read_bytes()
    text = data.decode("utf-8").replace("\r\n", "\n")
    payload = text.encode("utf-8")
    return {
        "sha256": "sha256:" + hashlib.sha256(payload).hexdigest(),
        "bytes": len(payload),
        "lines": text.count("\n"),
    }


def ledger_rows(cid, target, kind, terminal):
    rows = []
    for expected, state, reason in [
        ("needs_evidence", "ready_for_review", f"已完成语义复读：{kind} {target}"),
        ("ready_for_review", "approved", f"canonical 候选语义复读完成，批准{kind} {target}"),
        ("approved", terminal, f"已判定 {terminal}：{kind} {target}"),
    ]:
        row = {
            "candidate_id": cid,
            "expected_state": expected,
            "state": state,
            "decision": {
                "status": "pending" if state == "ready_for_review" else "approved",
                "reason": reason,
                "decided_by": "Agent",
                "decided_at": DATE,
            },
            "updated_at": DATE,
        }
        if state == terminal:
            row["target_ref"] = target
        rows.append(row)
    return rows


ledger = []
plan = []
mapping = []

for cand, slug, title, sub, entity, note in CREATES:
    cid = PREFIX + cand
    target = f"04-knowledge/units/procedures/{slug}.md"
    path = ROOT / target
    if not path.exists():
        raise SystemExit(f"missing {target}")
    fm = yaml.safe_load(path.read_text(encoding="utf-8").split("---\n", 2)[1])
    if title not in fm.get("title", ""):
        raise SystemExit(f"title mismatch {target}: {fm.get('title')}")
    if fm.get("sub_type") != sub:
        raise SystemExit(f"sub_type mismatch {target}: {fm.get('sub_type')}")
    fp = fingerprint(path)
    ledger.extend(ledger_rows(cid, target, "新建", "applied"))
    plan.append({
        "action": "create",
        "target_ref": target,
        "candidate_id": cid,
        "entity": entity,
        "before": None,
        "after_sha256": fp["sha256"],
        "bytes": fp["bytes"],
        "lines": fp["lines"],
        "note": f"新建{sub}：{note}",
    })
    mapping.append({
        "entity": entity,
        "target_ref": target,
        "action": "create",
        "canonical_candidate": cid,
        "merged_candidates": [],
    })

for cand, slug, title, sub, entity, note in UPDATES:
    cid = PREFIX + cand
    target = f"04-knowledge/units/procedures/{slug}.md"
    path = ROOT / target
    if not path.exists():
        raise SystemExit(f"missing {target}")
    fm = yaml.safe_load(path.read_text(encoding="utf-8").split("---\n", 2)[1])
    if title not in fm.get("title", ""):
        raise SystemExit(f"title mismatch {target}: {fm.get('title')}")
    if fm.get("sub_type") != sub:
        raise SystemExit(f"sub_type mismatch {target}: {fm.get('sub_type')}")
    before = BEFORE[slug]
    fp = fingerprint(path)
    ledger.extend(ledger_rows(cid, target, "更新", "applied"))
    plan.append({
        "action": "update",
        "target_ref": target,
        "candidate_id": cid,
        "entity": entity,
        "before": before,
        "after_sha256": fp["sha256"],
        "bytes": fp["bytes"],
        "lines": fp["lines"],
        "note": f"更新{sub}：{note}",
    })
    mapping.append({
        "entity": entity,
        "target_ref": target,
        "action": "update",
        "canonical_candidate": cid,
        "merged_candidates": [],
    })

for cand, slug, title, note in NO_DELTA:
    cid = PREFIX + cand
    target = f"04-knowledge/units/procedures/{slug}.md"
    path = ROOT / target
    if not path.exists():
        raise SystemExit(f"missing {target}")
    fm = yaml.safe_load(path.read_text(encoding="utf-8").split("---\n", 2)[1])
    if title not in fm.get("title", ""):
        raise SystemExit(f"title mismatch {target}: {fm.get('title')}")
    ledger.extend(ledger_rows(cid, target, "判定 no_delta（既有 KU 可完整承载）", "no_delta"))
    mapping.append({
        "entity": fm.get("title", title),
        "target_ref": target,
        "action": "no_delta",
        "canonical_candidate": cid,
        "merged_candidates": [],
        "note": note,
    })

assert len(ledger) == 42, len(ledger)
assert len(plan) == 11, len(plan)
assert len(mapping) == 14, len(mapping)

(BATCH / "candidate-decision-ledger.jsonl").write_bytes(
    ("\n".join(json.dumps(r, ensure_ascii=False) for r in ledger) + "\n").encode("utf-8")
)
(BATCH / "apply-plan.jsonl").write_bytes(
    ("\n".join(json.dumps(r, ensure_ascii=False) for r in plan) + "\n").encode("utf-8")
)
(BATCH / "canonical-mapping.json").write_bytes(
    (json.dumps(mapping, ensure_ascii=False, indent=2) + "\n").encode("utf-8")
)

manifest = {
    "work_package": "2026-10-25-2016xiayanjing-procedures-batch-i",
    "goal": "处理夏燕靖《中国艺术设计史（升级版）》2016 册 14 个 procedure 候选：7 个新建、4 个更新、3 个 no_delta；无 rejected。",
    "status": "applied",
    "date": DATE,
    "inputs": {
        "candidate_index": {
            "path": "06-runtime\\state\\candidate-index.jsonl",
            "rows_before": 5339,
            "sha256_before": "sha256:995b121f8f2e6c9ea13fc05de485815a3eb5e2f960f066001fe6942f83b5937a",
            "sha256_scope": "CRLF→LF 归一后",
            "counts_before": {
                "applied": 778,
                "needs_evidence": 3717,
                "no_delta": 43,
                "rejected": 801,
            },
        },
        "source": {
            "doc_id": "2016-xiayanjing-zhongguo-yishu-shejishi-upgrade",
            "file": "03基础书籍-md文档/中国艺术设计史（升级版）_夏燕靖_2016_上海人民美术出版社.md",
            "spans": [
                "L353", "L359", "L361", "L363", "L367", "L380",
                "L384", "L414", "L416",
                "L432", "L570",
                "L666-L675",
                "L688", "L1081", "L1087",
                "L1120", "L1124",
                "L1258", "L1562", "L1659",
            ],
        },
    },
    "method": {
        "rules": [
            "procedure 候选按实体而非 slug 对账：先与既有 procedure KU 的标题、别名和正文对齐，再定 create／update／no_delta。",
            "夏燕靖 2016《中国艺术设计史（升级版）》与 2009《中国设计史》为同一作者前后版本；2016 段落与既有 KU 所据 2009 段落语义一致时判 no_delta，不以新版年份充当新增证据。",
            "2016 版新增内容（元谋、蓝田、丁村、峙峪、下川石器序列，练染业 7 工官，铁鐏／铁鏤异文等）写入既有 KU；2016 版独立成条的新工艺另建 KU。",
            "来源只给名称、未给工序的条目（榫卯、焚失）照立条目，confidence 定为 low，并在证据边界写明缺失项。",
            "同名异指不合并：车轮检测法与陶器轮制法分列；浑铸法与合范法、分铸法分列。",
        ],
        "source_policy": "03基础书籍-md文档只读；本批写 04-knowledge/units/procedures，7 条新建、4 条更新。",
    },
    "outputs": {
        "apply_plan": {
            "path": "06-runtime\\automation\\2026-10-25-2016xiayanjing-procedures-batch-i\\apply-plan.jsonl",
            "rows": 11,
            "create": 7,
            "update": 4,
        },
        "ledger": {
            "path": "06-runtime\\automation\\2026-10-25-2016xiayanjing-procedures-batch-i\\candidate-decision-ledger.jsonl",
            "rows": 42,
            "candidates": 14,
            "applied": 11,
            "no_delta": 3,
            "rejected": 0,
        },
        "canonical_mapping": {
            "path": "06-runtime\\automation\\2026-10-25-2016xiayanjing-procedures-batch-i\\canonical-mapping.json",
            "entries": 14,
            "merged_candidates": [],
        },
    },
    "verification": {"status": "pending"},
}

(BATCH / "manifest.json").write_bytes(
    (json.dumps(manifest, ensure_ascii=False, indent=2) + "\n").encode("utf-8")
)
print("ledger", len(ledger), "plan", len(plan), "mapping", len(mapping))
for row in plan:
    print(row["action"], row["target_ref"], row["after_sha256"][:20], row["bytes"], row["lines"])
