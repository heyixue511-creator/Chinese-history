# -*- coding: utf-8 -*-
"""Finalize the 2016 modern-events batch manifest with verification results."""
import json
from pathlib import Path

path = Path("06-runtime/automation/2026-10-25-2016-modern-events-batch/manifest.json")
data = json.loads(path.read_text(encoding="utf-8"))

ci = data["inputs"]["candidate_index"]
ci["rows_after"] = 5339
ci["sha256_after"] = "sha256:83ce7412c8090ffc659c9816c44e16c671dbcb4c037a663fa57ffd9ef519c280"
ci["needs_evidence_after"] = 3899
ci["rebuild_idempotent"] = True

data["verification"] = {
    "status": "passed_with_generated_block",
    "batch_checks": {
        "ledger_rows": 111,
        "ledger_candidates": 37,
        "final_applied": 33,
        "final_no_delta": 4,
        "plan_rows": 33,
        "plan_fingerprints_match_disk": 33,
        "mapping_entries": 37,
        "cross_check_errors": 0,
    },
    "content_quality": {
        "units": 566,
        "findings": 0,
    },
    "repository_audit": {
        "structural_health": "122/130",
        "knowledge_structure": "55/65",
        "evidence_chain": "55/55",
        "evidence_citations": "566/566",
        "broken_links": 0,
        "frontmatter_missing": 0,
        "type_coverage": "8/8",
        "event_units": 72,
        "duplicate_cross_type_groups": 4,
        "duplicate_groups_disambiguated": 8,
        "duplicate_groups_without_disambiguation": 0,
    },
    "rule_drift": {
        "findings": 0,
    },
    "skill_registry": {
        "skills": 18,
        "leaf": 18,
        "router": 0,
    },
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
    "system_upgrade_chain": {
        "total_checks": 18,
        "pass": 18,
        "fail": 0,
        "behavioral_ready": True,
    },
    "pytest": {
        "tests": 250,
        "subtests": 16,
        "status": "pass",
    },
    "post_apply_check": {
        "errors": 0,
        "candidate_states": {
            "needs_evidence": 3899,
            "applied": 603,
            "rejected": 801,
            "no_delta": 36,
        },
    },
}

path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print("manifest updated", path)
