# -*- coding: utf-8 -*-
"""Finalize manifest for Zhaonong 2009 procedure batch C."""
import json
from pathlib import Path

BATCH = Path("06-runtime/automation/2026-10-25-2009zhaonong-procedures-batch-c")
path = BATCH / "manifest.json"
manifest = json.loads(path.read_text(encoding="utf-8"))

manifest["verification"] = {
    "status": "passed_with_generated_block",
    "batch_checks": {
        "ledger_rows": 24,
        "candidates": 8,
        "final_applied": 8,
        "plan_rows": 8,
        "create": 8,
        "update": 0,
        "fingerprints_verified": 8,
        "mapping_entries": 8,
        "errors": 0,
        "index_rebuild_idempotent": True,
    },
    "content_audit": {"knowledge_units": 650, "findings": 0},
    "repository_audit": {
        "structure_gate": "122/130",
        "structure_integrity": "55/65",
        "evidence_chain": "55/55",
        "rule_authority": "20/20",
        "frontmatter": "20/20",
        "verification_semantics": "20/20",
        "traceability": "7/15",
        "data_flow": "10/10",
        "report_freshness": "10/10",
        "engineering_safety": "5/5",
        "knowledge_units": 650,
        "type_coverage": "8/8",
        "hierarchy_level": "v0.1",
        "deprecated_type_residue": 0,
        "hierarchy_mounted": "0/650",
        "broken_links": 0,
        "same_name_groups": 4,
        "same_name_disambiguated": 8,
        "same_name_missing": 0,
        "evidence_refs": "650/650",
        "events": 115,
        "procedures": 53,
    },
    "relation_audit": {
        "broken_target": 0,
        "invalid_relation_type": 0,
        "missing_inverse": 0,
        "weak_evidence": 0,
        "isolated_units": 650,
    },
    "rule_drift": 0,
    "skill_registry": {"leaf_skills": 18},
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
    "pytest": {"tests": 266, "failures": 0, "errors": 0, "skipped": 0},
    "post_apply_check": {
        "candidate_index_rows": 5339,
        "candidate_index_sha256": "sha256:ac232887c84e6dab62629948268cdcb9ef51f803792719dfc9a7a86521526277",
        "counts": {
            "applied": 707,
            "needs_evidence": 3788,
            "no_delta": 43,
            "rejected": 801,
        },
    },
}
manifest["state_after"] = {
    "applied": 707,
    "needs_evidence": 3788,
    "no_delta": 43,
    "rejected": 801,
    "total": 5339,
}

path.write_bytes((json.dumps(manifest, ensure_ascii=False, indent=2) + "\n").encode("utf-8"))
print("manifest finalized")
