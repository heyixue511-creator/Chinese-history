import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
PKG = ROOT / "06-runtime" / "automation" / "2026-10-25-2011lilixin-institutions-batch-x"
manifest_path = PKG / "manifest.json"
manifest = json.loads(manifest_path.read_text(encoding="utf-8"))

manifest["verification"] = {
    "batch_checks": {
        "ledger_rows": 33,
        "candidates": 11,
        "final_applied": 11,
        "final_no_delta": 0,
        "final_rejected": 0,
        "plan_rows": 11,
        "create": 9,
        "update": 2,
        "merged_candidates": 1,
        "fingerprints_verified": 11,
        "mapping_entries": 11,
        "errors": 0,
        "index_rebuild_idempotent": True,
    },
    "content_audit": {
        "knowledge_units": 825,
        "findings": 0,
    },
    "repository_audit": {
        "structure_gate": "122/130",
        "structure_integrity": "55/65",
        "evidence_chain": "55/55",
        "knowledge_units": 825,
        "type_coverage": "8/8",
        "structure_node_coverage": "0/4",
        "hierarchy_level": "v0.1",
        "deprecated_type_residue": 0,
        "hierarchy_mounted": "0/825",
        "broken_links": 0,
        "same_name_groups": 4,
        "same_name_disambiguated": 8,
        "same_name_missing": 0,
        "evidence_refs": "825/825",
        "events": 115,
        "institutions": 144,
    },
    "relation_audit": {
        "broken_target": 0,
        "invalid_relation_type": 0,
        "missing_inverse": 0,
        "weak_evidence": 0,
        "unbaselined_generic_evidence_backed": 0,
        "isolated_units": 825,
        "over_connected": 0,
    },
    "rule_drift": 0,
    "skill_registry": {
        "leaf_skills": 18,
    },
    "whitespace": "pass",
    "generated_snapshot_check": {
        "steps_passed": "16/19",
        "status": "blocked",
        "reason": "工作树有 10 个生成态文件与 HEAD 不一致；commit 未获授权，按设计阻断。",
        "files": 10,
    },
    "system_upgrade_chain": {
        "checks": 18,
        "pass": 18,
        "fail": 0,
    },
    "pytest": {
        "tests": 250,
        "subtests": 16,
        "failures": 0,
        "errors": 0,
        "skipped": 0,
    },
    "post_apply_check": {
        "candidate_index_rows": 5339,
        "candidate_index_sha256": "sha256:0fb76ef90783b643feeb2a8543cba07fc4617ab1bddf6986ca3d3d70319964c4",
        "counts": {
            "applied": 930,
            "needs_evidence": 3540,
            "no_delta": 57,
            "rejected": 812,
        },
    },
}

manifest_path.write_text(
    json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
)
print(json.dumps({
    "status": manifest["status"],
    "state_after": manifest["state_after"],
    "verification_keys": list(manifest["verification"]),
}, ensure_ascii=False, indent=2))
