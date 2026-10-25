# -*- coding: utf-8 -*-
"""Backfill batch E manifest verification and state_after."""
import json
from pathlib import Path

BATCH = Path("06-runtime/automation/2026-10-25-2010tianzibing-procedures-batch-e")
path = BATCH / "manifest.json"
manifest = json.loads(path.read_text(encoding="utf-8"))

manifest["verification"] = {
    "status": "passed_with_generated_block",
    "batch_checks": {
        "ledger_rows": 45,
        "candidates": 15,
        "final_applied": 15,
        "plan_rows": 15,
        "create": 8,
        "update": 7,
        "fingerprints_verified": 15,
        "mapping_entries": 15,
        "errors": 0,
        "index_rebuild_idempotent": True,
    },
    "content_audit": {
        "knowledge_units": 670,
        "findings": 0,
    },
    "repository_audit": {
        "structure_gate": "122/130",
        "structure_integrity": "55/65",
        "evidence_chain": "55/55",
        "knowledge_units": 670,
        "type_coverage": "8/8",
        "hierarchy_level": "v0.1",
        "deprecated_type_residue": 0,
        "hierarchy_mounted": "0/670",
        "broken_links": 0,
        "same_name_groups": 4,
        "same_name_disambiguated": 8,
        "same_name_missing": 0,
        "evidence_refs": "670/670",
        "events": 115,
        "procedures": 73,
    },
    "relation_audit": {
        "broken_target": 0,
        "invalid_relation_type": 0,
        "missing_inverse": 0,
        "weak_evidence": 0,
        "isolated_units": 670,
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
        "candidate_index_sha256": "sha256:df8689e7eab91637112551608733ca0a085c2d6f66a1918d79136598edcaeef7",
        "counts": {
            "applied": 736,
            "needs_evidence": 3759,
            "no_delta": 43,
            "rejected": 801,
        },
    },
}
manifest["state_after"] = {
    "applied": 736,
    "needs_evidence": 3759,
    "no_delta": 43,
    "rejected": 801,
    "total": 5339,
}

path.write_bytes((json.dumps(manifest, ensure_ascii=False, indent=2) + "\n").encode("utf-8"))
print("verification", manifest["verification"]["status"], "state_after", manifest["state_after"])
