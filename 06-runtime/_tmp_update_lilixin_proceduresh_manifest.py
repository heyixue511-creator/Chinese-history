# -*- coding: utf-8 -*-
"""Backfill batch H manifest verification and state_after."""
import json
from pathlib import Path

BATCH = Path("06-runtime/automation/2026-10-25-2011lilixin-procedures-batch-h")
path = BATCH / "manifest.json"
manifest = json.loads(path.read_text(encoding="utf-8"))

manifest["verification"] = {
    "status": "passed_with_generated_block",
    "batch_checks": {
        "ledger_rows": 30,
        "candidates": 10,
        "final_applied": 10,
        "plan_rows": 9,
        "create": 5,
        "update": 4,
        "merged_candidates": 1,
        "fingerprints_verified": 9,
        "mapping_entries": 9,
        "errors": 0,
        "index_rebuild_idempotent": True,
    },
    "content_audit": {
        "knowledge_units": 701,
        "findings": 0,
    },
    "repository_audit": {
        "structure_gate": "122/130",
        "structure_integrity": "55/65",
        "evidence_chain": "55/55",
        "knowledge_units": 701,
        "type_coverage": "8/8",
        "hierarchy_level": "v0.1",
        "deprecated_type_residue": 0,
        "hierarchy_mounted": "0/701",
        "broken_links": 0,
        "same_name_groups": 4,
        "same_name_disambiguated": 8,
        "same_name_missing": 0,
        "evidence_refs": "701/701",
        "events": 115,
        "procedures": 104,
    },
    "relation_audit": {
        "broken_target": 0,
        "invalid_relation_type": 0,
        "missing_inverse": 0,
        "weak_evidence": 0,
        "isolated_units": 701,
    },
    "rule_drift": 0,
    "skill_registry": {
        "leaf_skills": 18,
    },
    "whitespace": "pass",
    "generated_snapshot_check": {
        "steps_passed": "16/19",
        "status": "blocked",
        "reason": "工作树有 9 个生成态文件与 HEAD 不一致；commit 未获授权，按设计阻断。",
        "files": 9,
    },
    "system_upgrade_chain": {
        "checks": 18,
        "pass": 18,
        "fail": 0,
    },
    "pytest": {
        "tests": 266,
        "failures": 0,
        "errors": 0,
        "skipped": 0,
    },
    "post_apply_check": {
        "candidate_index_rows": 5339,
        "candidate_index_sha256": "sha256:995b121f8f2e6c9ea13fc05de485815a3eb5e2f960f066001fe6942f83b5937a",
        "counts": {
            "applied": 778,
            "needs_evidence": 3717,
            "no_delta": 43,
            "rejected": 801,
        },
    },
}
manifest["state_after"] = {
    "applied": 778,
    "needs_evidence": 3717,
    "no_delta": 43,
    "rejected": 801,
    "total": 5339,
}

path.write_bytes((json.dumps(manifest, ensure_ascii=False, indent=2) + "\n").encode("utf-8"))
print("verification", manifest["verification"]["status"], "state_after", manifest["state_after"])
