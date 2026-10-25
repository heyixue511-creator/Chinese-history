# -*- coding: utf-8 -*-
"""Fill verification and post-apply state for the Gaofeng 2004 procedure batch."""
import json
from pathlib import Path

BATCH = Path("06-runtime/automation/2026-10-25-2004gaofeng-procedures-batch/manifest.json")
manifest = json.loads(BATCH.read_text(encoding="utf-8"))

manifest["inputs"]["source"]["spans"] = ["L3102-L3118", "L3692-L3697", "L2181", "L5174"]

manifest["state_after"] = {
    "applied": 667,
    "needs_evidence": 3828,
    "no_delta": 43,
    "rejected": 801,
    "total": 5339,
}

manifest["verification"] = {
    "status": "passed_with_generated_block",
    "batch_checks": {
        "ledger_rows": 15,
        "candidates": 5,
        "final_applied": 5,
        "plan_rows": 5,
        "create": 4,
        "update": 1,
        "fingerprints_verified": 5,
        "mapping_entries": 5,
        "errors": 0,
        "index_rebuild_idempotent": True,
    },
    "content_audit": {
        "knowledge_units": 613,
        "findings": 0,
    },
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
        "knowledge_units": 613,
        "type_coverage": "8/8",
        "hierarchy_level": "v0.1",
        "deprecated_type_residue": 0,
        "hierarchy_mounted": "0/613",
        "broken_links": 0,
        "same_name_groups": 4,
        "same_name_disambiguated": 8,
        "same_name_missing": 0,
        "evidence_refs": "613/613",
        "events": 115,
        "procedures": 16,
    },
    "relation_audit": {
        "broken_target": 0,
        "invalid_relation_type": 0,
        "missing_inverse": 0,
        "weak_evidence": 0,
        "isolated_units": 613,
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
    "pytest": {
        "tests": 266,
        "failures": 0,
        "errors": 0,
        "skipped": 0,
    },
    "post_apply_check": {
        "candidate_index_rows": 5339,
        "candidate_index_sha256": "sha256:d7c810b762cf18d89acaa6a3c672ca8c68981447cab53063fac8663dfc89213f",
        "counts": {
            "applied": 667,
            "needs_evidence": 3828,
            "no_delta": 43,
            "rejected": 801,
        },
    },
}

BATCH.write_bytes((json.dumps(manifest, ensure_ascii=False, indent=2) + "\n").encode("utf-8"))
print("manifest updated", manifest["status"], manifest["verification"]["status"])
