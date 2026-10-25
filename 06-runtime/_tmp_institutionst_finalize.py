import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
PKG = ROOT / "06-runtime" / "automation" / "2026-10-25-2010tianzibing-institutions-batch-t"
path = PKG / "manifest.json"
manifest = json.loads(path.read_text(encoding="utf-8"))

manifest["verification"] = {
    "batch_checks": {
        "ledger_rows": 26,
        "candidates": 10,
        "final_applied": 8,
        "final_no_delta": 0,
        "final_rejected": 2,
        "plan_rows": 8,
        "create": 5,
        "update": 3,
        "merged_candidates": 0,
        "fingerprints_verified": 8,
        "mapping_entries": 8,
        "errors": 0,
        "index_rebuild_idempotent": True,
    },
    "content_audit": {"knowledge_units": 797, "findings": 0},
    "repository_audit": {
        "structure_gate": "122/130",
        "structure_integrity": "55/65",
        "evidence_chain": "55/55",
        "knowledge_units": 797,
        "type_coverage": "8/8",
        "hierarchy_level": "v0.1",
        "deprecated_type_residue": 0,
        "hierarchy_mounted": "0/797",
        "broken_links": 0,
        "same_name_groups": 4,
        "same_name_disambiguated": 8,
        "same_name_missing": 0,
        "evidence_refs": "797/797",
        "events": 115,
        "institutions": 116,
    },
    "relation_audit": {
        "broken_target": 0,
        "invalid_relation_type": 0,
        "missing_inverse": 0,
        "weak_evidence": 0,
        "unbaselined_generic_evidence_backed": 0,
        "isolated_units": 797,
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
        "candidate_index_sha256": "sha256:05dd4761a548d3bdf08e6cb7516d57135ad2f5e2263a6f836a6c2de4290ce6cc",
        "counts": {"applied": 895, "needs_evidence": 3578, "no_delta": 56, "rejected": 810},
    },
}
manifest["state_after"] = {"applied": 895, "needs_evidence": 3578, "no_delta": 56, "rejected": 810, "total": 5339}

path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"status": manifest["status"], "state_after": manifest["state_after"],
                  "verification_keys": list(manifest["verification"])}, ensure_ascii=False))
