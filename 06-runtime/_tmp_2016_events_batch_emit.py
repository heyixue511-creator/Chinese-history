# -*- coding: utf-8 -*-
"""Emit ledger, apply-plan, mapping and manifest for the 2016 ancient-to-Yuan event batch."""
import hashlib
import json
from collections import Counter
from pathlib import Path

WP = Path("06-runtime/automation/2026-10-25-2016-ancient-events-batch")
WP.mkdir(parents=True, exist_ok=True)
DATE = "2026-10-25"
PREFIX = "2016-xiayanjing-zhongguo-yishu-shejishi-upgrade:"
INDEX = Path("06-runtime/state/candidate-index.jsonl")

CREATES = [
    ("cand-02-88", "04-knowledge/units/events/yu-casts-nine-cauldrons.md", "禹铸九鼎", "新建传说事件：夏禹收九牧之金铸九鼎、迁鼎、列鼎等级与问鼎典故"),
    ("cand-02-45", "04-knowledge/units/events/ganshi-battle.md", "甘泽之战", "新建车战起源事件：《尚书·甘誓》、夏后启与有扈氏、甲士与徒卒"),
    ("cand-02-86", "04-knowledge/units/events/shang-tang-overthrows-xia.md", "商汤灭夏", "新建商早期车战事件：良车七十乘、奚仲造车与有辐车轮"),
    ("cand-02-87", "04-knowledge/units/events/king-wu-conquers-zhou.md", "武王伐纣", "新建商末车船事件：战车 300 辆、孟津渡河、舟字与舵桨记载"),
    ("cand-02-65", "04-knowledge/units/events/jin-casting-legal-cauldron.md", "晋国铸刑鼎", "新建春秋生铁冶铸事件：前 513 年刑鼎、白口铁与排橐鼓风"),
    ("cand-03-55", "04-knowledge/units/events/mozi-zhi-chu-gong-song.md", "墨子止楚攻宋", "新建攻守器械事件：约前 444 年云梯、九攻九拒与墨守成规"),
    ("cand-03-82", "04-knowledge/units/events/qin-mie-liuguo.md", "秦灭六国", "新建统一制度事件：前 221 年、统一文字货币度量衡、长城与始皇陵"),
    ("cand-03-92", "04-knowledge/units/events/zhangqian-chushi-xiyu.md", "张骞出使西域", "新建丝路开通事件：前 138/119 年两次出使、长安至地中海东岸"),
    ("cand-03-93", "04-knowledge/units/events/qin-qian-yetie-haozu.md", "秦迁六国冶铁豪族", "新建官营冶铁政策事件：迁卓氏程氏孔氏、铁官与技术交流"),
    ("cand-03-121", "04-knowledge/units/events/han-wudi-duzun-rushu.md", "汉武帝独尊儒术", "新建服饰等级背景事件：罢黜百家、董仲舒理论与汉代袍服"),
    ("cand-04-50", "04-knowledge/units/events/xiao-wen-gai-zhi.md", "孝文改制", "新建汉化服饰事件：改拓跋姓氏、群臣皆服汉魏衣冠"),
    ("cand-06-03", "04-knowledge/units/events/jingkang-zhibian.md", "靖康之难", "新建宋室南迁事件：1126—1127 年、临安、淮水大散关界线"),
    ("cand-06-30", "04-knowledge/units/events/fucangshan-tomb.md", "浮仓山南宋墓", "新建南宋服饰发现：1975 年福建浮仓山、成组女服与印金刺绣"),
    ("cand-06-81", "04-knowledge/units/events/deyang-xiaoquan-silver-find.md", "德阳孝泉镇宋代银器出土", "新建宋代银器发现：1959 年 117 件、24 种、圆球形银熏炉"),
    ("cand-06-54", "04-knowledge/units/events/xixia-mausoleum.md", "西夏王陵发掘", "新建西夏纺织发现：20 世纪 70 年代初、丝织 10 余片与茂花闪色绵 3 片"),
    ("cand-06-59", "04-knowledge/units/events/yuan-abolish-keju.md", "元代科举废止", "新建元代社会背景事件：废科举、士人流向民间与民间工艺发达"),
    ("cand-07-62", "04-knowledge/units/events/qingshousi-tomb-textiles.md", "1955年北京庆寿寺双塔出土丝织品", "新建元代丝织发现：1955 年、4 片纳石失金锦、紫阳荷花缂丝"),
    ("cand-07-59", "04-knowledge/units/events/boyan-collects-song-regalia.md", "1272年伯颜收取宋宫冕服图籍", "新建元代服制转向事件：至元十二年收取衮冕符玺图籍、蒙古发式"),
    ("cand-07-61", "04-knowledge/units/events/yanyou-fuse.md", "延祐元年（1314）贵族夫人服色规定", "新建元代服色制度事件：三档金饰、南熏殿画像考引文与顾姑冠"),
    ("cand-08-87", "04-knowledge/units/events/queue-and-dress-edicts.md", "清初剃发易服", "新建清代服饰政策事件：留头不留发、金之俊十从十不从"),
    ("cand-08-88", "04-knowledge/units/events/zhenghe-voyages.md", "郑和下西洋", "新建贸易瓷高峰事件：1405 年左右、七下西洋、亚非中国风"),
    ("cand-08-90", "04-knowledge/units/events/qing-opens-sea-ban-1684.md", "1684年清廷开放海禁", "新建清代造船业事件：1684 年开海、福建四厂与民营造船"),
]

NO_DELTA = [
    ("cand-07-56", "04-knowledge/units/works/guiguxiashan-qinghua-guan.md", "2005年“鬼谷下山”青花罐伦敦拍卖", "既有 work KU 已完整记录 2005-07-12、1568.8 万英镑、尺寸与存世 8 件"),
    ("cand-07-60", "04-knowledge/units/terms/zhisun-fu.md", "1321年元英宗定制质孙服", "既有 term KU 已完整记录 1321 年定制、一色衣、上衣连下裳与等级"),
    ("cand-07-57", "04-knowledge/units/persons/guo-shoujing.md", "1276年设太史局编《授时历》", "既有 person KU 已完整记录 1276 年设太史局、1280 年成历与 17 种仪器"),
    ("cand-07-58", "04-knowledge/units/works/miaoying-si-baita.md", "至元八年建妙应寺白塔", "既有 work KU 已完整记录 1271 年、阿尼哥、50.9 米与覆钵式形制"),
    ("cand-08-89", "04-knowledge/units/terms/blue-and-white-porcelain.md", "克拉克号被捕获", "既有 term KU 已记录 1602 年荷兰东印度公司捕获克拉克号与命名由来"),
]


def fingerprint(path):
    data = path.read_bytes()
    text = data.decode("utf-8").replace("\r\n", "\n")
    payload = text.encode("utf-8")
    return {"sha256": "sha256:" + hashlib.sha256(payload).hexdigest(),
            "bytes": len(payload), "lines": text.count("\n")}


def rows(cid, target, action):
    if action == "create":
        r1 = f"已完成语义复读：既有 KU 无对应实体，提交 create {target}"
        r2 = f"canonical 候选语义复读完成，批准按 exact change-set 新建 {target}"
        r3 = f"已按 exact change-set 新建 {target}"
        final = "applied"
    else:
        r1 = f"已完成语义复读：既有 {target} 已覆盖候选实质内容，提交 no_delta 判定"
        r2 = "语义复读确认无实质增量，批准 no_delta"
        r3 = f"既有 {target} 已完整覆盖候选内容，无需写回；判定 no_delta"
        final = "no_delta"
    return [
        {"candidate_id": cid, "expected_state": "needs_evidence", "state": "ready_for_review",
         "decision": {"status": "pending", "reason": r1, "decided_by": "Agent", "decided_at": DATE},
         "updated_at": DATE},
        {"candidate_id": cid, "expected_state": "ready_for_review", "state": "approved",
         "decision": {"status": "approved", "reason": r2, "decided_by": "Agent", "decided_at": DATE},
         "updated_at": DATE},
        {"candidate_id": cid, "expected_state": "approved", "state": final,
         "decision": {"status": "approved", "reason": r3, "decided_by": "Agent", "decided_at": DATE},
         "updated_at": DATE, "target_ref": target},
    ]


index_rows = [json.loads(l) for l in INDEX.read_text(encoding="utf-8").splitlines() if l.strip()]
by_id = {r["candidate_id"]: r for r in index_rows}
before_hash = fingerprint(INDEX)
before_counts = Counter(r["state"] for r in index_rows)
spans = []
for cid, *_ in CREATES + NO_DELTA:
    r = by_id[PREFIX + cid]
    sp = r["payload"].get("source_span", {})
    spans.append(f"L{sp.get('line_start')}-L{sp.get('line_end')}" if sp.get("line_end") != sp.get("line_start") else f"L{sp.get('line_start')}")

ledger, plan, mapping = [], [], []
for cid, target, entity, note in CREATES:
    full = PREFIX + cid
    ledger.extend(rows(full, target, "create"))
    fp = fingerprint(Path(target))
    plan.append({"action": "create", "target_ref": target, "candidate_id": full, "entity": entity,
                 "before": None, "after_sha256": fp["sha256"], "bytes": fp["bytes"],
                 "lines": fp["lines"], "note": note})
    mapping.append({"entity": entity, "target_ref": target, "action": "create",
                    "canonical_candidate": full, "merged_candidates": []})

for cid, target, entity, note in NO_DELTA:
    full = PREFIX + cid
    ledger.extend(rows(full, target, "no_delta"))
    mapping.append({"entity": entity, "target_ref": target, "action": "no_delta",
                    "canonical_candidate": full, "merged_candidates": [], "note": note})

with (WP / "candidate-decision-ledger.jsonl").open("w", encoding="utf-8", newline="") as fh:
    for row in ledger:
        fh.write(json.dumps(row, ensure_ascii=False) + "\n")
with (WP / "apply-plan.jsonl").open("w", encoding="utf-8", newline="") as fh:
    for row in plan:
        fh.write(json.dumps(row, ensure_ascii=False) + "\n")
(WP / "canonical-mapping.json").write_text(json.dumps(mapping, ensure_ascii=False, indent=2), encoding="utf-8")

after_counts = Counter(before_counts)
after_counts["needs_evidence"] -= len(CREATES) + len(NO_DELTA)
after_counts["applied"] += len(CREATES)
after_counts["no_delta"] += len(NO_DELTA)

manifest = {
    "work_package": WP.name,
    "goal": "处理夏燕靖《中国艺术设计史（升级版）》2016 册中古代至元代的 27 个 event 候选：22 个新建 event KU，5 个由既有 KU 覆盖判 no_delta。",
    "status": "applied",
    "date": DATE,
    "inputs": {
        "candidate_index": {
            "path": str(INDEX), "rows_before": len(index_rows),
            "sha256_before": before_hash["sha256"],
            "counts_before": dict(sorted(before_counts.items())),
        },
        "source": {
            "doc_id": "2016-xiayanjing-zhongguo-yishu-shejishi-upgrade",
            "file": "03基础书籍-md文档/中国艺术设计史（升级版）_夏燕靖_2016_上海人民美术出版社.md",
            "spans": spans,
        },
    },
    "method": {
        "rules": [
            "事件若无既有 KU 可承载，且来源给出时间、地点、参与者、过程或工艺信息，建 event KU。",
            "事件若已被既有 work/person/term KU 完整覆盖，判 no_delta，不重复建条。",
            "事件条目只写来源所记事实；未给年代、遗址编号、尺寸或检测数据时明确写入证据边界。",
            "发现类候选（墓、窖藏、陵墓、塔内清理）用 sub_type: discovery；其余用 historical_event。",
        ],
        "source_policy": "02-sources 只读；本批只写 04-knowledge/units/events。",
    },
    "outputs": {
        "apply_plan": {"path": str(WP / "apply-plan.jsonl"), "rows": len(plan), "create": len(CREATES), "update": 0},
        "ledger": {"path": str(WP / "candidate-decision-ledger.jsonl"), "rows": len(ledger),
                   "candidates": len(CREATES) + len(NO_DELTA), "applied": len(CREATES),
                   "no_delta": len(NO_DELTA), "rejected": 0},
        "canonical_mapping": {"path": str(WP / "canonical-mapping.json"), "entries": len(mapping)},
    },
    "state_after": {"applied": after_counts["applied"], "no_delta": after_counts["no_delta"],
                    "rejected": after_counts["rejected"], "needs_evidence": after_counts["needs_evidence"],
                    "total": len(index_rows)},
    "verification": {"status": "pending"},
    "notes": [
        "5 个 no_delta 分别由 works/guiguxiashan-qinghua-guan.md、terms/zhisun-fu.md、persons/guo-shoujing.md、works/miaoying-si-baita.md、terms/blue-and-white-porcelain.md 覆盖。",
        "浮仓山、德阳、西夏王陵、庆寿寺四处为发现类候选，sub_type 用 discovery。",
        "传说事件（禹铸九鼎、甘泽之战）按来源叙述建条，不据外部考订补年代或器物。",
        "《吕氏春秋》篇名、使者名、元上三鼎一簋等原文异写照录，未改写。",
    ],
}
(WP / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
print("ledger", len(ledger), "plan", len(plan), "mapping", len(mapping), "before", dict(before_counts))
