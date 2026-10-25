# -*- coding: utf-8 -*-
"""Emit ledger, apply-plan, canonical mapping and manifest for the Tianzibing 2010 event batch."""
import hashlib
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from _tmp_tianzibing_events_items import ITEMS_TZ

ROOT = Path(".")
BATCH = Path("06-runtime/automation/2026-10-25-2010tianzibing-events-batch")
BATCH.mkdir(parents=True, exist_ok=True)
PREFIX = "2010-tianzibing-zhongguo-gongyi-meishushi:"
DATE = "2026-10-25"
DOC = "2010-tianzibing-zhongguo-gongyi-meishushi"

UPDATES = [
    {
        "cand": "cand-04-42",
        "entity": "武王伐纣",
        "target_ref": "04-knowledge/units/events/king-wu-conquers-zhou.md",
        "span": "L1280",
        "note": "补入田自秉 2010 所记周文王时国势渐强、武王联合反对商的各部落灭商建周并建都镐京；另加别名“武王灭商”。",
    },
    {
        "cand": "cand-06-49",
        "entity": "秦灭六国",
        "target_ref": "04-knowledge/units/events/qin-mie-liuguo.md",
        "span": "L2075-L2079",
        "note": "补入田自秉 2010 所记商鞅变法基础、灭六国顺序、吸收他国文化、没收民间兵器运咸阳销毁与“统一性和巨大性”判断。",
    },
    {
        "cand": "cand-09-03",
        "entity": "千秋节",
        "target_ref": "04-knowledge/units/events/qianqiu-festival.md",
        "span": "L3327",
        "note": "补入田自秉 2010 所引《唐书·礼乐志》、群臣献甘露寿酒与铜镜祝寿互赠、“千秋金鉴节”别称及皇室赏赐、纪念品、有柄舞镜等用途。",
    },
    {
        "cand": "cand-09-28",
        "entity": "陈桥驿兵变",
        "target_ref": "04-knowledge/units/events/chenqiao-mutiny.md",
        "span": "L3476",
        "note": "补入田自秉 2010 所记 960 年赵匡胤夺取政权、建立宋朝、定都东京（今开封）、结束唐末以来分裂割据与辽、西夏并立形势；田自秉未用“陈桥驿”之名。",
    },
    {
        "cand": "cand-09-29",
        "entity": "靖康之难",
        "target_ref": "04-knowledge/units/events/jingkang-zhibian.md",
        "span": "L3476",
        "note": "补入田自秉 2010 所记 1125 年辽亡于金、1127 年金兵破开封、宋室南迁临安与宋金对峙、1279 年南宋亡于元；南宋亡年与夏燕靖 2016 的 1276 年并存。",
    },
    {
        "cand": "cand-11-18",
        "entity": "郑和下西洋",
        "target_ref": "04-knowledge/units/events/zhenghe-voyages.md",
        "span": "L4174",
        "note": "补入田自秉 2010 所记成祖派太监郑和七下西洋、远到亚非等 30 多个国家、扩大中外经济文化交流，并记迁都北京与安定西北的同期举措。",
    },
    {
        "cand": "cand-13-58",
        "entity": "1958 年首次全国艺人代表会议",
        "target_ref": "04-knowledge/units/events/national-craft-artists-conference-1957.md",
        "span": "L5051",
        "note": "补入田自秉 2010 所记 1958 年首次全国艺人代表会议与 1979 年代表会议；与夏燕靖 2016 的 1957 年 7 月 22 日相差一年，两说并存，不作来源外裁决。",
    },
    {
        "cand": "cand-13-61",
        "entity": "1914 年巴拿马博览会北京雕漆获奖",
        "target_ref": "04-knowledge/units/events/banama-saihui.md",
        "span": "L5194-L5196",
        "note": "补入田自秉 2010 所记北京雕漆 1914 年在巴拿马博览会获一等奖、民国初年畸形发展、多仿清作品，以及解放后雕漆厂品种与镂空手法；获奖年份比开幕早一年。",
    },
]

NO_DELTA = [
    {
        "cand": "cand-13-59",
        "entity": "1979 年全国工艺美术艺人、创作设计人员代表大会",
        "target_ref": "04-knowledge/units/events/crafts-artist-title-1979.md",
        "note": "既有 event KU 已记 1979-08-08—16 会议、杨士惠等 34 人获“工艺美术家”称号与 8 月 11 日学会恢复。",
    },
    {
        "cand": "cand-14-18",
        "entity": "中央工艺美术学院成立",
        "target_ref": "04-knowledge/units/institutions/central-academy-arts-design.md",
        "note": "既有 institution KU 已记 1956-05-21 国务院批准、11-01 建院典礼，并明记田自秉只记 1956 年学院成立。",
    },
]


def fingerprint(path: Path):
    data = path.read_bytes()
    text = data.decode("utf-8").replace("\r\n", "\n")
    payload = text.encode("utf-8")
    return {
        "sha256": "sha256:" + hashlib.sha256(payload).hexdigest(),
        "bytes": len(payload),
        "lines": text.count("\n"),
    }


def norm_text(path: Path) -> str:
    return path.read_bytes().decode("utf-8").replace("\r\n", "\n")


ledger = []
plan = []
mapping = []

for item in ITEMS_TZ:
    cid = PREFIX + item["cand"]
    target = f"04-knowledge/units/events/{item['slug']}.md"
    path = ROOT / target
    if not path.exists():
        raise SystemExit(f"missing {target}")
    fm = norm_text(path).split("---\n", 2)[1]
    if f'title: "{item["title"]}（{item["en"]}）"' not in fm:
        raise SystemExit(f"title mismatch {target}")
    fp = fingerprint(path)
    ledger.append({
        "candidate_id": cid,
        "expected_state": "needs_evidence",
        "state": "ready_for_review",
        "decision": {
            "status": "pending",
            "reason": f"已完成语义复读：既有 KU 无对应实体，提交 create {target}",
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
            "reason": f"canonical 候选语义复读完成，批准按 exact change-set 新建 {target}",
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
            "reason": f"已按 exact change-set 新建 {target}",
            "decided_by": "Agent",
            "decided_at": DATE,
        },
        "updated_at": DATE,
        "target_ref": target,
    })
    plan.append({
        "action": "create",
        "target_ref": target,
        "candidate_id": cid,
        "entity": item["title"],
        "before": None,
        "after_sha256": fp["sha256"],
        "bytes": fp["bytes"],
        "lines": fp["lines"],
        "note": f"新建{item['sub']}：{item['date']}；{item['result']}",
    })
    mapping.append({
        "entity": item["title"],
        "target_ref": target,
        "action": "create",
        "canonical_candidate": cid,
        "merged_candidates": [],
    })

BEFORE = json.loads((Path(__file__).parent / "_tmp_tianzibing_before.json").read_text(encoding="utf-8"))

for up in UPDATES:
    cid = PREFIX + up["cand"]
    target = up["target_ref"]
    path = ROOT / target
    if not path.exists():
        raise SystemExit(f"missing {target}")
    before = BEFORE[up["target_ref"].rsplit("/", 1)[1][:-3]]
    fp = fingerprint(path)
    if fp["sha256"] == before["sha256"]:
        raise SystemExit(f"unchanged {target}")
    ledger.append({
        "candidate_id": cid,
        "expected_state": "needs_evidence",
        "state": "ready_for_review",
        "decision": {
            "status": "pending",
            "reason": f"已完成语义复读：既有 {target} 可承载但缺田自秉 2010 记载，提交 update",
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
            "reason": f"canonical 候选语义复读完成，批准按 exact change-set 补写 {target}",
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
            "reason": f"已按 exact change-set 补入田自秉 2010 记载：{target}",
            "decided_by": "Agent",
            "decided_at": DATE,
        },
        "updated_at": DATE,
        "target_ref": target,
    })
    plan.append({
        "action": "update",
        "target_ref": target,
        "candidate_id": cid,
        "entity": up["entity"],
        "before": before,
        "after_sha256": fp["sha256"],
        "bytes": fp["bytes"],
        "lines": fp["lines"],
        "note": up["note"],
    })
    mapping.append({
        "entity": up["entity"],
        "target_ref": target,
        "action": "update",
        "canonical_candidate": cid,
        "merged_candidates": [],
        "note": up["note"],
    })

for nd in NO_DELTA:
    cid = PREFIX + nd["cand"]
    ledger.append({
        "candidate_id": cid,
        "expected_state": "needs_evidence",
        "state": "ready_for_review",
        "decision": {
            "status": "pending",
            "reason": f"已完成语义复读：既有 {nd['target_ref']} 可完整承载，提交 no_delta",
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
            "reason": f"canonical 候选语义复读完成，批准判 no_delta（{nd['target_ref']}）",
            "decided_by": "Agent",
            "decided_at": DATE,
        },
        "updated_at": DATE,
    })
    ledger.append({
        "candidate_id": cid,
        "expected_state": "approved",
        "state": "no_delta",
        "decision": {
            "status": "approved",
            "reason": f"既有 {nd['target_ref']} 已完整覆盖候选内容，无需写回；判定 no_delta",
            "decided_by": "Agent",
            "decided_at": DATE,
        },
        "updated_at": DATE,
        "target_ref": nd["target_ref"],
    })
    mapping.append({
        "entity": nd["entity"],
        "target_ref": nd["target_ref"],
        "action": "no_delta",
        "canonical_candidate": cid,
        "merged_candidates": [],
        "note": nd["note"],
    })

assert len(ledger) == 66, len(ledger)
assert len(plan) == 20, len(plan)
assert len(mapping) == 22, len(mapping)

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
    "work_package": "2026-10-25-2010tianzibing-events-batch",
    "goal": "处理田自秉《中国工艺美术史（修订本）》2010 册的 22 个 event 候选：12 个新建 event KU，8 个补入既有 KU，2 个由既有 KU 覆盖判 no_delta。",
    "status": "applied",
    "date": DATE,
    "inputs": {
        "candidate_index": {
            "path": "06-runtime\\state\\candidate-index.jsonl",
            "rows_before": 5339,
            "sha256_before": "sha256:1d7195a284cbbd1b143a373fd55747db366724cbb36047a6b9396dd5da71ed9b",
            "sha256_scope": "CRLF→LF 归一后",
            "counts_before": {
                "applied": 623,
                "needs_evidence": 3876,
                "no_delta": 39,
                "rejected": 801,
            },
        },
        "source": {
            "doc_id": DOC,
            "file": "03基础书籍-md文档/中国工艺美术史（修订本）_田自秉_2010_东方出版中心.md",
            "spans": [i["span"] for i in ITEMS_TZ] + [u["span"] for u in UPDATES] + ["L5051", "L5725-L5727"],
        },
    },
    "method": {
        "rules": [
            "既有同题 KU 可承载但缺田自秉 2010 记载的判 update，按 exact change-set 补入来源、描述、核心内容、匹配质量与参考文献。",
            "已有专条完整覆盖候选内容的判 no_delta，并在 mapping 记明覆盖点。",
            "无对应实体的判 create，只写来源所记时间、地点、参与者、过程与结果。",
            "两册年份、人数或评价不一致者并列保留并写明差异，不作来源外裁决。",
        ],
        "source_policy": "02-sources 只读；本批写 04-knowledge/units/events 与 04-knowledge/units/institutions 的既有条目。",
    },
    "outputs": {
        "apply_plan": {
            "path": "06-runtime\\automation\\2026-10-25-2010tianzibing-events-batch\\apply-plan.jsonl",
            "rows": 20,
            "create": 12,
            "update": 8,
        },
        "ledger": {
            "path": "06-runtime\\automation\\2026-10-25-2010tianzibing-events-batch\\candidate-decision-ledger.jsonl",
            "rows": 66,
            "candidates": 22,
            "applied": 20,
            "no_delta": 2,
            "rejected": 0,
        },
        "canonical_mapping": {
            "path": "06-runtime\\automation\\2026-10-25-2010tianzibing-events-batch\\canonical-mapping.json",
            "entries": 22,
        },
    },
    "verification": {"status": "pending"},
}

(BATCH / "manifest.json").write_bytes(
    (json.dumps(manifest, ensure_ascii=False, indent=2) + "\n").encode("utf-8")
)
print("ledger", len(ledger), "plan", len(plan), "mapping", len(mapping))
