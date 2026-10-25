import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
PKG = ROOT / "06-runtime" / "automation" / "2026-10-25-xiayanjing2009-places-batch-y"
p = PKG / "manifest.json"
m = json.loads(p.read_text(encoding="utf-8"))
m["verification"] = {
    "batch_checks": {
        "ledger_rows": 9,
        "candidates": 3,
        "final_applied": 3,
        "final_no_delta": 0,
        "final_rejected": 0,
        "plan_rows": 3,
        "create": 2,
        "update": 1,
        "merged_candidates": 0,
        "fingerprints_verified": 3,
        "mapping_entries": 3,
        "errors": 0,
        "index_rebuild_idempotent": True,
    },
    "content_audit": {"knowledge_units": 827, "findings": 0},
    "repository_audit": {
        "structure_gate": "122/130",
        "structure_integrity": "55/65",
        "evidence_chain": "55/55",
        "knowledge_units": 827,
        "type_coverage": "8/8",
        "structure_node_coverage": "0/4",
        "hierarchy_level": "v0.1",
        "deprecated_type_residue": 0,
        "hierarchy_mounted": "0/827",
        "broken_links": 0,
        "same_name_groups": 4,
        "same_name_disambiguated": 8,
        "same_name_missing": 0,
        "evidence_refs": "827/827",
        "events": 115,
        "institutions": 144,
        "places": 41,
    },
    "relation_audit": {
        "broken_target": 0,
        "invalid_relation_type": 0,
        "missing_inverse": 0,
        "weak_evidence": 0,
        "unbaselined_generic_evidence_backed": 0,
        "isolated_units": 827,
        "over_connected": 0,
    },
    "rule_drift": 0,
    "skill_registry": {"leaf_skills": 18},
    "whitespace": "pass",
    "generated_snapshot_check": {
        "steps_passed": "16/19",
        "status": "blocked",
        "reason": "工作树有 10 个生成态文件与 HEAD 不一致；commit 未获授权，按设计阻断。",
        "files": 10,
    },
    "system_upgrade_chain": {"checks": 18, "pass": 18, "fail": 0},
    "pytest": {"tests": 250, "subtests": 16, "failures": 0, "errors": 0, "skipped": 0},
    "post_apply_check": {
        "candidate_index_rows": 5339,
        "candidate_index_sha256": "sha256:39f64e7d09fa93c28f0c8598fb85dbe77cb6e4df03d5d3d2025bdafa437841f0",
        "counts": {"applied": 933, "needs_evidence": 3537, "no_delta": 57, "rejected": 812},
    },
}
p.write_text(json.dumps(m, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"status": m["status"], "state_after": m["state_after"]}, ensure_ascii=False, indent=2))
