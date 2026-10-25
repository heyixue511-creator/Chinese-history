# -*- coding: utf-8 -*-
"""Emit ledger, apply-plan, canonical mapping and manifest for the Xiayanjing 2009 event batch."""
import hashlib
import json
from pathlib import Path

ROOT = Path(".")
BATCH = Path("06-runtime/automation/2026-10-25-2009xiayanjing-events-batch")
BATCH.mkdir(parents=True, exist_ok=True)
PREFIX = "2009-xiayanjing-zhongguo-shejishi:"
DATE = "2026-10-25"
DOC = "2009-xiayanjing-zhongguo-shejishi"

CREATES = [
    {
        "cand": "cand-03-108",
        "slug": "6th-century-fangzhi-jishu-waichuan",
        "title": "中国纺织印染技术外传",
        "sub": "historical_event",
        "date": "公元6世纪",
        "result": "脚踏纺车、提花机经阿富汗、伊朗西传，工匠到中亚、西亚传艺，日本、波斯与拜占庭获丝绸、工匠与蚕种",
    },
    {
        "cand": "cand-06-82",
        "slug": "1972-1976-dingci-huifu",
        "title": "定瓷恢复",
        "sub": "historical_event",
        "date": "1972—1976年",
        "result": "1974 年定瓷厂在曲阳建立，两年后恢复工作展开，两次发掘定窑遗址并得“始烧于唐、兴盛于宋、失传于元”初步定论",
    },
    {
        "cand": "cand-07-15",
        "slug": "zhongguo-gongyi-meishupin-baihuajiang",
        "title": "中国工艺美术品百花奖",
        "sub": "professional_event",
        "date": "1981—1984年（第一至四届）",
        "result": "第一至三届分别评出金杯奖作品六件、七件、三件；第四届记俞家荣仿明衮服获金杯奖",
    },
]

UPDATES = [
    {
        "cand": "cand-03-81",
        "entity": "孝文改制",
        "target_ref": "04-knowledge/units/events/xiao-wen-gai-zhi.md",
        "span": "L1773-L1776",
        "before": {
            "sha256": "sha256:5409486ac488e8ec4bb4010e60632291230a6c88a9c7e650f55d922a7ea2d2b5",
            "bytes": 3380,
            "lines": 79,
        },
        "note": "补入夏燕靖 2009 年表同条记载，文字与 2016 升级版基本一致；两版互证孝文改制内容。",
    },
    {
        "cand": "cand-07-04",
        "entity": "全国工艺美术艺人代表会议（1957）",
        "target_ref": "04-knowledge/units/events/national-craft-artists-conference-1957.md",
        "span": "L4594-L4607",
        "before": {
            "sha256": "sha256:cbb335a28d80194dd5dde9c8cffff6d534e7561a5d8bd5fecb68a9ac72ff7ef0",
            "bytes": 5701,
            "lines": 91,
        },
        "note": "补入夏燕靖 2009 年表 7 月 22 日的明确日期与“保护、发展和提高”方针、“适用、经济、美观”原则；2009 与 2016 正文月份一致。",
    },
    {
        "cand": "cand-07-11",
        "entity": "周恩来1972年提倡手工艺",
        "target_ref": "04-knowledge/units/events/zhou-enlai-handicraft-1972.md",
        "span": "L4694-L4711",
        "before": {
            "sha256": "sha256:c4e1bf56f49d2ad41b707b2a6cf61d53a5f62225ec990848fe9d6acbc2a72a4",
            "bytes": 4032,
            "lines": 80,
        },
        "note": "补入夏燕靖 2009 年表同条记载，文字与 2016 升级版基本一致。",
    },
    {
        "cand": "cand-07-12",
        "entity": "中国向联合国总部赠送工艺品（1974）",
        "target_ref": "04-knowledge/units/events/united-nations-gift-1974.md",
        "span": "L4694-L4711",
        "before": {
            "sha256": "sha256:9ca2f9881a2039e84cc32bcd15715f78362b8a53aa7bc03fd6d7bef85377fbfe",
            "bytes": 3999,
            "lines": 79,
        },
        "note": "补入夏燕靖 2009 年表所记 10 月 7 日赠送与天津、北京产地；任务下达与尺寸仍仅 2016 所记。",
    },
    {
        "cand": "cand-07-13",
        "entity": "全国工艺美术艺人、创作设计人员代表大会（1979）",
        "target_ref": "04-knowledge/units/events/crafts-artist-title-1979.md",
        "span": "L4736-L4745",
        "before": {
            "sha256": "sha256:1d97d524d7faf74ab22f9faba318cde55721c100e427f3e2c69b500ea3fae3fc",
            "bytes": 3821,
            "lines": 80,
        },
        "note": "补入夏燕靖 2009 年表同条记载，文字与 2016 升级版基本一致，并同记 1 月赴日展览与 8 月 11 日学会恢复。",
    },
    {
        "cand": "cand-07-16",
        "entity": "全国高等院校工艺美术教学座谈会（1982）",
        "target_ref": "04-knowledge/units/events/national-crafts-education-symposium-1982.md",
        "span": "L4768-L4787",
        "before": {
            "sha256": "sha256:09acc397df8e408079b16582eefd07d25b207b2c2f3f1bae0d0da89c2cf26bc1",
            "bytes": 3761,
            "lines": 80,
        },
        "note": "补入夏燕靖 2009 年表同条记载，文字与 2016 升级版基本一致。",
    },
    {
        "cand": "cand-07-20",
        "entity": "中国工业设计代表团首次参加ICSID'89",
        "target_ref": "04-knowledge/units/events/icsid-1989-nagoya.md",
        "span": "L4896-L4915",
        "before": {
            "sha256": "sha256:8abc109c2ff333aa8ee3c0ff319dc2d9bf92d18129ca50eedcd42665be867562",
            "bytes": 3802,
            "lines": 80,
        },
        "note": "补入夏燕靖 2009 年表同条记载，文字与 2016 升级版基本一致。",
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

for item in CREATES:
    cid = PREFIX + item["cand"]
    target = f"04-knowledge/units/events/{item['slug']}.md"
    path = ROOT / target
    if not path.exists():
        raise SystemExit(f"missing {target}")
    fm = norm_text(path).split("---\n", 2)[1]
    if f'title: "{item["title"]}（' not in fm:
        raise SystemExit(f"title mismatch {target}")
    fp = fingerprint(path)
    for expected, state, reason in [
        ("needs_evidence", "ready_for_review", f"已完成语义复读：既有 KU 无对应实体，提交 create {target}"),
        ("ready_for_review", "approved", f"canonical 候选语义复读完成，批准按 exact change-set 新建 {target}"),
        ("approved", "applied", f"已按 exact change-set 新建 {target}"),
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
        if state == "applied":
            row["target_ref"] = target
        ledger.append(row)
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

for up in UPDATES:
    cid = PREFIX + up["cand"]
    target = up["target_ref"]
    path = ROOT / target
    if not path.exists():
        raise SystemExit(f"missing {target}")
    fp = fingerprint(path)
    if fp["sha256"] == up["before"]["sha256"]:
        raise SystemExit(f"unchanged {target}")
    for expected, state, reason in [
        ("needs_evidence", "ready_for_review", f"已完成语义复读：既有 {target} 可承载但缺夏燕靖 2009 记载，提交 update"),
        ("ready_for_review", "approved", f"canonical 候选语义复读完成，批准按 exact change-set 补写 {target}"),
        ("approved", "applied", f"已按 exact change-set 补入夏燕靖 2009 记载：{target}"),
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
        if state == "applied":
            row["target_ref"] = target
        ledger.append(row)
    plan.append({
        "action": "update",
        "target_ref": target,
        "candidate_id": cid,
        "entity": up["entity"],
        "before": up["before"],
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

assert len(ledger) == 30, len(ledger)
assert len(plan) == 10, len(plan)
assert len(mapping) == 10, len(mapping)

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
    "work_package": "2026-10-25-2009xiayanjing-events-batch",
    "goal": "处理夏燕靖《中国设计史》2009 册的 10 个 event 候选：3 个新建 event KU，7 个补入既有 event KU；无 no_delta、无 rejected。",
    "status": "applied",
    "date": DATE,
    "inputs": {
        "candidate_index": {
            "path": "06-runtime\\state\\candidate-index.jsonl",
            "rows_before": 5339,
            "sha256_before": "sha256:aaa3c28b584f8ce731d3c7e2762e4996875adb653be6768622cf0db54e2c3826",
            "sha256_scope": "CRLF→LF 归一后",
            "counts_before": {
                "applied": 652,
                "needs_evidence": 3843,
                "no_delta": 43,
                "rejected": 801,
            },
        },
        "source": {
            "doc_id": DOC,
            "file": "03基础书籍-md文档/中国设计史_夏燕靖_2009_上海人民美术出版社.md",
            "spans": [i for i in ["L1764-L1766", "L1773-L1776", "L4331", "L4594-L4607", "L4694-L4711", "L4694-L4711", "L4736-L4745", "L4758-L4819", "L4768-L4787", "L4896-L4915"]],
        },
    },
    "method": {
        "rules": [
            "既有同题 KU 可承载但缺夏燕靖 2009 记载的判 update；既有专条已完整覆盖且已引夏燕靖 2009 的判 no_delta；无对应实体的判 create。",
            "2009 与 2016 两版条目文字基本一致的，在 update 中并列两版并注明差异，不以新版覆盖旧版。",
            "事件条目只写来源所记时间、地点、参与者、过程与结果；来源未载的年份、人物、数据与过程写入证据边界。",
            "来源的判断与推测照录并标明主语，不提升为定论。",
        ],
        "source_policy": "02-sources 只读；本批写 04-knowledge/units/events，并对既有 event KU 补入 2009 来源。",
    },
    "outputs": {
        "apply_plan": {
            "path": "06-runtime\\automation\\2026-10-25-2009xiayanjing-events-batch\\apply-plan.jsonl",
            "rows": 10,
            "create": 3,
            "update": 7,
        },
        "ledger": {
            "path": "06-runtime\\automation\\2026-10-25-2009xiayanjing-events-batch\\candidate-decision-ledger.jsonl",
            "rows": 30,
            "candidates": 10,
            "applied": 10,
            "no_delta": 0,
            "rejected": 0,
        },
        "canonical_mapping": {
            "path": "06-runtime\\automation\\2026-10-25-2009xiayanjing-events-batch\\canonical-mapping.json",
            "entries": 10,
        },
    },
    "verification": {"status": "pending"},
}

(BATCH / "manifest.json").write_bytes(
    (json.dumps(manifest, ensure_ascii=False, indent=2) + "\n").encode("utf-8")
)
print("ledger", len(ledger), "plan", len(plan), "mapping", len(mapping))
