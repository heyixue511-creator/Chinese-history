# -*- coding: utf-8 -*-
"""Emit ledger, apply-plan, mapping and manifest for the overlap batch."""
import hashlib
import json
from pathlib import Path

WP = Path("06-runtime/automation/2026-10-25-overlap-candidates-batch")
WP.mkdir(parents=True, exist_ok=True)
DATE = "2026-10-25"
result = json.loads(Path("06-runtime/_tmp_overlap_update_result.json").read_text(encoding="utf-8"))

NO_DELTA = [
    (["2004-gaofeng-zhongguo-shejishi:cand-07-24", "2009-xiayanjing-zhongguo-shejishi:cand-07-35"], "庞薰琹", "04-knowledge/units/persons/pang-xunqin.md"),
    (["2009-xiayanjing-zhongguo-shejishi:cand-03-60"], "水碓", "04-knowledge/units/works/shui-dui.md"),
    (["2009-xiayanjing-zhongguo-shejishi:cand-04-06"], "龙门石窟", "04-knowledge/units/places/longmen-grottoes.md"),
    (["2009-zhaonong-zhongguo-yishu-shejishi:cand-02-10"], "干栏式", "04-knowledge/units/terms/ganlan-shi-jianzhu.md"),
    (["2009-zhaonong-zhongguo-yishu-shejishi:cand-04-08"], "彩漆动物座屏", "04-knowledge/units/works/caiqi-mudiao-dongwu-zuoping.md"),
    (["2010-tianzibing-zhongguo-gongyi-meishushi:cand-03-30"], "司母戊鼎", "04-knowledge/units/works/simuwu-ding.md"),
    (["2016-xiayanjing-zhongguo-yishu-shejishi-upgrade:cand-06-13"], "汝窑", "04-knowledge/units/places/ru-kiln.md"),
    (["2016-xiayanjing-zhongguo-yishu-shejishi-upgrade:cand-06-15"], "定窑", "04-knowledge/units/places/ding-kiln.md"),
    (["2016-xiayanjing-zhongguo-yishu-shejishi-upgrade:cand-08-04"], "黄成", "04-knowledge/units/persons/huang-dacheng.md"),
    (["2016-xiayanjing-zhongguo-yishu-shejishi-upgrade:cand-11-26"], "李诫", "04-knowledge/units/persons/li-cheng.md"),
]


def ledger_rows(cid, target, action, merged=False):
    if action == "update":
        r1 = f"已完成语义复读：候选含既有 KU 未载的实质内容，提交 update {target}"
        r2 = f"canonical 候选语义复读完成，批准按 exact change-set 更新 {target}"
        r3 = f"已按 exact change-set 更新 {target}"
        if merged:
            r3 += "；同组同实体候选归档为本 KU"
        final = "applied"
    elif action == "create":
        r1 = f"已完成语义复读：既有 KU 无对应实体，提交 create {target}"
        r2 = f"canonical 候选语义复读完成，批准按 exact change-set 新建 {target}"
        r3 = f"已按 exact change-set 新建 {target}；同组候选归档为本 KU"
        final = "applied"
    else:
        r1 = f"已完成语义复读：既有 {target} 已覆盖候选实质内容，提交 no_delta 判定"
        r2 = "语义复读确认无实质增量，批准 no_delta"
        r3 = f"既有 {target} 已完整覆盖候选内容，无需写回；判定 no_delta"
        final = "no_delta"
    return [
        {
            "candidate_id": cid,
            "expected_state": "needs_evidence",
            "state": "ready_for_review",
            "decision": {"status": "pending", "reason": r1, "decided_by": "Agent", "decided_at": DATE},
            "updated_at": DATE,
        },
        {
            "candidate_id": cid,
            "expected_state": "ready_for_review",
            "state": "approved",
            "decision": {"status": "approved", "reason": r2, "decided_by": "Agent", "decided_at": DATE},
            "updated_at": DATE,
        },
        {
            "candidate_id": cid,
            "expected_state": "approved",
            "state": final,
            "decision": {"status": "approved", "reason": r3, "decided_by": "Agent", "decided_at": DATE},
            "updated_at": DATE,
            "target_ref": target,
        },
    ]


def main():
    ledger = []
    mapping = []
    apply_plan = []

    for item in result["updates"]:
        target = item["target_ref"]
        merged = len(item["candidate_ids"]) > 1
        for cid in item["candidate_ids"]:
            ledger.extend(ledger_rows(cid, target, "update", merged))
        mapping.append(
            {
                "entity": item["entity"],
                "target_ref": target,
                "action": "update",
                "canonical_candidate": item["primary"],
                "merged_candidates": item["candidate_ids"][1:],
            }
        )
        apply_plan.append(
            {
                "action": "update",
                "target_ref": target,
                "candidate_id": item["primary"],
                "entity": item["entity"],
                "before": item["before"],
                "after_sha256": item["after"]["sha256"],
                "bytes": item["after"]["bytes"],
                "lines": item["after"]["lines"],
                "note": item["note"],
            }
        )

    create = result["create"]
    ledger.extend(ledger_rows(create["primary"], create["target_ref"], "create"))
    mapping.append(
        {
            "entity": create["entity"],
            "target_ref": create["target_ref"],
            "action": "create",
            "canonical_candidate": create["primary"],
            "merged_candidates": [],
        }
    )
    apply_plan.append(
        {
            "action": "create",
            "target_ref": create["target_ref"],
            "candidate_id": create["primary"],
            "entity": create["entity"],
            "before": None,
            "after_sha256": create["after"]["sha256"],
            "bytes": create["after"]["bytes"],
            "lines": create["after"]["lines"],
            "note": create["note"],
        }
    )

    for cids, entity, target in NO_DELTA:
        for cid in cids:
            ledger.extend(ledger_rows(cid, target, "no_delta"))
        mapping.append(
            {
                "entity": entity,
                "target_ref": target,
                "action": "no_delta",
                "canonical_candidate": cids[0],
                "merged_candidates": cids[1:],
            }
        )

    with (WP / "candidate-decision-ledger.jsonl").open("w", encoding="utf-8", newline="") as fh:
        for row in ledger:
            fh.write(json.dumps(row, ensure_ascii=False) + "\n")
    with (WP / "apply-plan.jsonl").open("w", encoding="utf-8", newline="") as fh:
        for row in apply_plan:
            fh.write(json.dumps(row, ensure_ascii=False) + "\n")
    (WP / "canonical-mapping.json").write_text(
        json.dumps(mapping, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    sources = {
        "2004": "高丰《中国设计史》",
        "2009xy": "夏燕靖《中国设计史》",
        "2009zn": "赵农《中国艺术设计史》",
        "2010": "田自秉《中国工艺美术史（修订本）》",
        "2011": "李立新《中国设计艺术史论》",
        "2016": "夏燕靖《中国艺术设计史（升级版）》",
    }
    manifest = {
        "work_package": "2026-10-25-overlap-candidates-batch",
        "goal": "清算未分组 unit 候选中与既有 KU 重叠的 53 个候选：逐条语义复读后按 update/create/no_delta 写回，避免重复建条。",
        "status": "applied",
        "date": DATE,
        "inputs": {
            "candidate_index": {
                "path": "06-runtime/state/candidate-index.jsonl",
                "rows_before": 5339,
                "sha256_before": "sha256:d5229189c1f55a2c7f0a0c41ab11a8146aeaaf21898ae6a4d95bdf5b3a341cc8",
                "needs_evidence_before": 4023,
                "rows_after": 5339,
                "sha256_after": "sha256:7ee850800bf8b2fc21a3a25d54c412be72b41e27ceb515ab8f72311dc5197e6b",
            },
            "scope": {
                "documents": sources,
                "unit_candidates_total": 2660,
                "overlap_candidates": 53,
                "match_method": "候选 title/alias 去空白与标点后与 504 个既有 KU 的 title/aliases 精确匹配；再逐条回读原文与现有 KU 判定增量。",
            },
        },
        "method": {
            "reject_rules": [
                "同实体重复候选只保留 canonical，其余并入同一 KU，不另建条。",
                "既有 KU 已完整覆盖候选内容时判 no_delta，不重复写回。",
                "部分覆盖时只追加缺失事实，不重写既有段落；两册冲突数值并列保留，不裁定。",
            ],
            "source_policy": "02-sources 只读；所有写回只改 04-knowledge/units。",
        },
        "outputs": {
            "apply_plan": {
                "path": "06-runtime/automation/2026-10-25-overlap-candidates-batch/apply-plan.jsonl",
                "rows": len(apply_plan),
                "update": sum(1 for r in apply_plan if r["action"] == "update"),
                "create": sum(1 for r in apply_plan if r["action"] == "create"),
            },
            "ledger": {
                "path": "06-runtime/automation/2026-10-25-overlap-candidates-batch/candidate-decision-ledger.jsonl",
                "rows": len(ledger),
                "candidates": len(ledger) // 3,
                "applied": 42,
                "no_delta": 11,
                "rejected": 0,
            },
            "canonical_mapping": {
                "path": "06-runtime/automation/2026-10-25-overlap-candidates-batch/canonical-mapping.json",
                "entries": len(mapping),
            },
        },
        "state_after": {
            "applied": 542,
            "no_delta": 26,
            "rejected": 801,
            "needs_evidence": 3970,
            "total": 5339,
        },
        "verification": {
            "status": "passed_except_commit_gate",
            "content_quality": {
                "command": "python scripts/audit_content_quality.py",
                "units": 505,
                "findings": 0,
            },
            "repo_audit": {
                "command": "python scripts/audit_repo.py",
                "structural_health": "122/130",
                "evidence_refs_resolvable": "505/505",
                "broken_links": 0,
            },
            "discovery_index": {
                "command": "python scripts/build_discovery_index.py",
                "idempotent": True,
                "rows": 5339,
                "sha256_after": "sha256:7ee850800bf8b2fc21a3a25d54c412be72b41e27ceb515ab8f72311dc5197e6b",
            },
            "sync_closure": {
                "command": "python scripts/run_sync_closure.py --refresh-generated --full --check-generated",
                "result": "steps 1-16 passed; step 17 blocked by design",
                "failed_step": "check generated snapshots",
                "reason": "该步执行 git diff --exit-code HEAD；工作树未提交，需用户当次明确授权 commit 后才能通过",
            },
            "system_upgrade_chain": {"pass": 18, "fail": 0},
            "tests": {"command": "python -m pytest tests -q", "passed": 250, "failed": 0},
        },
        "notes": [
            "候选“管子”按人物语义写回 persons/guan-zhong.md，不写 publications/guanzi.md。",
            "jiazhu-tai 合并 2010“夹纻”与 2016“夹纻胎”两个候选；dulunche 合并 2009“独轮车”与 2011“鹿车”两个候选。",
            "妙应寺白塔 53 米与 50.9 米、开封铁塔褐色琉璃瓦与 28 种琉璃砖均并列保留，不裁定。",
        ],
    }
    (WP / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")

    print("ledger", len(ledger), "apply_plan", len(apply_plan), "mapping", len(mapping))


if __name__ == "__main__":
    main()
