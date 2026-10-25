# -*- coding: utf-8 -*-
"""Fill state_after and verification for the Li Lixin 2011 event batch manifest."""
import json
from pathlib import Path

WP = Path("06-runtime/automation/2026-10-25-2011lilixin-events-batch/manifest.json")
data = json.loads(WP.read_text(encoding="utf-8"))

data["state_after"] = {
    "applied": 652,
    "no_delta": 43,
    "rejected": 801,
    "needs_evidence": 3843,
    "total": 5339,
}

data["verification"] = {
    "status": "passed_with_generated_block",
    "batch_checks": {
        "ledger_rows": 33,
        "ledger_candidates": 11,
        "final_applied": 9,
        "final_no_delta": 2,
        "plan_rows": 9,
        "plan_create": 8,
        "plan_update": 1,
        "plan_fingerprints_match_disk": 9,
        "mapping_entries": 11,
        "cross_check_errors": 0,
        "rebuild_idempotent": True,
    },
    "content_quality": {"units": 606, "findings": 0},
    "repository_audit": {
        "structural_health": "122/130",
        "knowledge_structure": "55/65",
        "evidence_chain": "55/55",
        "evidence_citations": "606/606",
        "broken_links": 0,
        "frontmatter_missing": 0,
        "type_coverage": "8/8",
        "event_units": 112,
        "duplicate_cross_type_groups": 4,
        "duplicate_groups_disambiguated": 8,
        "duplicate_groups_without_disambiguation": 0,
    },
    "rule_drift": {"findings": 0},
    "skill_registry": {"skills": 18, "leaf": 18, "router": 0},
    "whitespace_check": "pass",
    "generated_snapshot_check": {
        "status": "blocked",
        "step": "17/19",
        "exit_code": 1,
        "reason": "工作树未提交，9 个生成态文件与 HEAD 不一致；--check-generated 按设计阻断，待授权提交后复核。",
        "differing_files": [
            "05-outputs/index/index.md",
            "05-outputs/knowledge-graph-data.js",
            "05-outputs/knowledge-graph-data.json",
            "06-runtime/automation/index.md",
            "06-runtime/governance/governance-backlog.md",
            "06-runtime/state/candidate-index.jsonl",
            "06-runtime/state/current-health.json",
            "06-runtime/state/discovery-manifest.json",
            "06-runtime/state/generated-projections-manifest.json",
        ],
    },
    "system_upgrade_chain": {"total_checks": 18, "pass": 18, "fail": 0, "behavioral_ready": True},
    "pytest": {"tests": 250, "subtests": 16, "status": "pass"},
    "post_apply_check": {
        "errors": 0,
        "candidate_states": {
            "needs_evidence": 3843,
            "applied": 652,
            "no_delta": 43,
            "rejected": 801,
        },
        "index_rows": 5339,
        "index_sha256": "sha256:aaa3c28b584f8ce731d3c7e2762e4996875adb653be6768622cf0db54e2c3826",
    },
}

WP.write_bytes((json.dumps(data, ensure_ascii=False, indent=2) + "\n").encode("utf-8"))
print("manifest updated")
