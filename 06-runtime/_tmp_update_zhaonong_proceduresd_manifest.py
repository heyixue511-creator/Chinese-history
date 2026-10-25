# -*- coding: utf-8 -*-
"""Backfill batch D manifest verification and state_after."""
import json
from pathlib import Path

BATCH = Path("06-runtime/automation/2026-10-25-2009zhaonong-procedures-batch-d")
path = BATCH / "manifest.json"
manifest = json.loads(path.read_text(encoding="utf-8"))

manifest["verification"] = {
    "status": "passed_with_generated_block",
    "batch_checks": {
        "ledger_rows": 42,
        "candidates": 14,
        "final_applied": 14,
        "plan_rows": 14,
        "create": 12,
        "update": 2,
        "fingerprints_verified": 14,
        "mapping_entries": 14,
        "errors": 0,
        "index_rebuild_idempotent": True,
    },
    "content_audit": {
        "knowledge_units": 662,
        "findings": 0,
    },
    "repository_audit": {
        "structure_gate": "122/130",
        "structure_integrity": "55/65",
        "evidence_chain": "55/55",
        "knowledge_units": 662,
        "type_coverage": "8/8",
        "hierarchy_level": "v0.1",
        "deprecated_type_residue": 0,
        "hierarchy_mounted": "0/662",
        "broken_links": 0,
        "same_name_groups": 4,
        "same_name_disambiguated": 8,
        "same_name_missing": 0,
        "evidence_refs": "662/662",
        "events": 115,
        "procedures": 65,
    },
    "relation_audit": {
        "broken_target": 0,
        "invalid_relation_type": 0,
        "missing_inverse": 0,
        "weak_evidence": 0,
        "isolated_units": 662,
    },
    "rule_drift": 0,
    "skill_registry": {
        "leaf_skills": 18,
    },
    "whitespace": "pass",
    "generated_snapshot_check": {
        "steps_passed": "17/19",
        "status": "blocked",
        "reason": "工作树有 9 个生成态文件与 HEAD 不一致；commit 未获授权，按设计阻断。",
        "files": 9,
    },
    "system_upgrade_chain": {
        "checks": 18,
        "pass": 18,
        "fail": 0,
        "behavioral_ready": True,
    },
    "pytest": {
        "tests": 266,
        "failures": 0,
        "errors": 0,
        "skipped": 0,
    },
    "post_apply_check": {
        "candidate_index_rows": 5339,
        "candidate_index_sha256": "sha256:813de48a1d67aecd6cce88af36649be59d3cf6cf652424e582b4001c8d02c28a",
        "counts": {
            "applied": 721,
            "needs_evidence": 3774,
            "no_delta": 43,
            "rejected": 801,
        },
    },
}
manifest["state_after"] = {
    "applied": 721,
    "needs_evidence": 3774,
    "no_delta": 43,
    "rejected": 801,
    "total": 5339,
}

path.write_bytes((json.dumps(manifest, ensure_ascii=False, indent=2) + "\n").encode("utf-8"))
print("verification", manifest["verification"]["status"], "state_after", manifest["state_after"])
