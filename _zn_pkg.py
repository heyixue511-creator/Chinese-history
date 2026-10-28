"""Build a unit work package from a decisions JSON file.

Usage: python _zn_pkg.py <decisions.json> <package-name> <goal> <date>

decisions.json: list of {
  "cid": "2009-zhaonong-zhongguo-yishu-shejishi:cand-01-12",
  "entity": "石器时期",
  "action": "create|update|no_delta|rejected",
  "target": "04-knowledge/units/terms/shiji-shiqi.md",
  "analysis": "...", "approve": "...", "apply_note": "...", "note": "..."
}
Optional global fields in the JSON object instead of list:
  {"doc": "...", "file": "...", "package": "...", "goal": "...", "date": "...",
   "extras": [ {"target": "...", "entity": "...", "parent_cid": "...", "note": "..."} ],
   "decisions": [ ... ]}
"""
import hashlib
import json
import subprocess
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(r"D:/中国设计史研究")
INDEX = ROOT / "06-runtime/state/candidate-index.jsonl"


def norm_bytes(data):
    return data.replace(b"\r\n", b"\n")


def file_metrics(path):
    data = norm_bytes(path.read_bytes())
    return {
        "after_sha256": "sha256:" + hashlib.sha256(data).hexdigest(),
        "bytes": len(data),
        "lines": data.count(b"\n"),
    }


def head_blob(relpath):
    proc = subprocess.run(["git", "show", "HEAD:" + relpath], capture_output=True, cwd=str(ROOT))
    if proc.returncode != 0:
        return None
    data = norm_bytes(proc.stdout)
    return {"before": "sha256:" + hashlib.sha256(data).hexdigest(), "before_source": "head_blob"}


def main():
    cfg = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    if isinstance(cfg, list):
        cfg = {"decisions": cfg}
    pkg_name = sys.argv[2]
    goal = sys.argv[3]
    date = sys.argv[4]
    doc = cfg["doc"]
    source_file = cfg["file"]
    decisions = cfg["decisions"]
    extras = cfg.get("extras", [])
    pkg = ROOT / "06-runtime/automation" / pkg_name

    index_data = norm_bytes(INDEX.read_bytes())
    counts_before = Counter()
    for line in index_data.decode("utf-8").splitlines():
        if line.strip():
            counts_before[json.loads(line)["state"]] += 1
    rows_before = index_data.count(b"\n")
    sha_before = "sha256:" + hashlib.sha256(index_data).hexdigest()

    cand_rows = {}
    for line in INDEX.read_text(encoding="utf-8").splitlines():
        if line.strip():
            r = json.loads(line)
            cand_rows[r["candidate_id"]] = r

    ledger, apply_plan, mapping = [], [], []
    created, updated, no_delta, rejected, spans = [], [], [], [], []
    for d in decisions:
        cid = d["cid"]
        row = cand_rows[cid]
        span = row["payload"]["source_span"]
        spans.append((int(span["line_start"]), int(span["line_end"])))
        base = {"candidate_id": cid, "updated_at": date}
        ledger.append({
            **base, "expected_state": "needs_evidence", "state": "ready_for_review",
            "decision": {"decided_at": date, "decided_by": "Agent", "reason": d["analysis"], "status": "pending"},
        })
        if d["action"] == "rejected":
            ledger.append({
                **base, "expected_state": "ready_for_review", "state": "rejected", "target_ref": d["target"],
                "decision": {"decided_at": date, "decided_by": "Agent", "reason": d["approve"], "status": "rejected"},
            })
            rejected.append(d["target"])
            mapping.append({
                "entity": d["entity"], "target_ref": d["target"], "action": d["action"],
                "canonical_candidate": cid, "merged_candidates": [], "note": d["note"],
            })
            continue
        ledger.append({
            **base, "expected_state": "ready_for_review", "state": "approved",
            "decision": {"decided_at": date, "decided_by": "Agent", "reason": d["approve"], "status": "approved"},
        })
        terminal = "no_delta" if d["action"] == "no_delta" else "applied"
        ledger.append({
            **base, "expected_state": "approved", "state": terminal, "target_ref": d["target"],
            "decision": {"decided_at": date, "decided_by": "Agent", "reason": d["apply_note"], "status": "approved"},
        })
        if d["action"] == "create":
            m = file_metrics(ROOT / d["target"])
            apply_plan.append({
                "action": "create", "after_sha256": m["after_sha256"], "before": None,
                "bytes": m["bytes"], "candidate_id": cid, "entity": d["entity"],
                "lines": m["lines"], "note": d["apply_note"], "target_ref": d["target"],
            })
            created.append(d["target"])
        elif d["action"] == "update":
            m = file_metrics(ROOT / d["target"])
            head = head_blob(d["target"])
            before, before_source = (None, "untracked_no_head_blob") if head is None else (head["before"], head["before_source"])
            apply_plan.append({
                "action": "update", "after_sha256": m["after_sha256"], "before": before,
                "before_source": before_source, "bytes": m["bytes"], "candidate_id": cid,
                "entity": d["entity"], "lines": m["lines"], "note": d["apply_note"], "target_ref": d["target"],
            })
            updated.append(d["target"])
        else:
            no_delta.append(d["target"])
        mapping.append({
            "entity": d["entity"], "target_ref": d["target"], "action": d["action"],
            "canonical_candidate": cid, "merged_candidates": [], "note": d["note"],
        })

    for e in extras:
        m = file_metrics(ROOT / e["target"])
        head = head_blob(e["target"])
        before, before_source = (None, "untracked_no_head_blob") if head is None else (head["before"], head["before_source"])
        apply_plan.append({
            "action": "update", "after_sha256": m["after_sha256"], "before": before,
            "before_source": before_source, "bytes": m["bytes"], "candidate_id": e["parent_cid"],
            "entity": e["entity"], "lines": m["lines"], "note": e["note"], "target_ref": e["target"],
        })
        updated.append(e["target"])

    spans.sort()
    updated_unique = list(dict.fromkeys(updated))
    merged = []
    for s, en in spans:
        if merged and s <= merged[-1][1] + 1:
            merged[-1][1] = max(merged[-1][1], en)
        else:
            merged.append([s, en])
    covered = sum(en - s + 1 for s, en in merged)
    scope = "覆盖 %d 行：%s。" % (
        covered,
        "、".join(("L%d" % s) if s == en else ("L%d-L%d" % (s, en)) for s, en in merged),
    )

    manifest = {
        "work_package": pkg_name,
        "goal": goal,
        "status": "applied",
        "date": date,
        "inputs": {
            "candidate_index": {
                "path": "06-runtime/state/candidate-index.jsonl",
                "rows_before": rows_before,
                "sha256_before": sha_before,
                "sha256_scope": "CRLF→LF 归一",
                "counts_before": {
                    "needs_evidence": counts_before["needs_evidence"],
                    "applied": counts_before["applied"],
                    "rejected": counts_before["rejected"],
                    "no_delta": counts_before["no_delta"],
                },
            },
            "source": {
                "doc_id": doc,
                "file": source_file,
                "spans": cfg.get("scope_spans", merged),
                "spans_scope": cfg.get("scope_note", scope),
                "candidates_in_scope": len(decisions),
                **(
                    {"candidate_spans_union": merged}
                    if cfg.get("scope_spans") is not None
                    else {}
                ),
            },
        },
        "method": {"rules": cfg.get("rules", [])},
        "outputs": {
            "knowledge_units": {
                "create": len(created),
                "update": sum(1 for d in decisions if d["action"] == "update"),
                "no_delta": len(no_delta),
                "rejected": len(rejected),
                "paths_created": created,
                "paths_updated": updated_unique,
                "paths_no_delta": no_delta,
                "paths_rejected": rejected,
                "notes": cfg.get("notes", ""),
            }
        },
    }

    pkg.mkdir(parents=True, exist_ok=True)
    with (pkg / "candidate-decision-ledger.jsonl").open("w", encoding="utf-8", newline="\n") as h:
        for row in ledger:
            h.write(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n")
    with (pkg / "apply-plan.jsonl").open("w", encoding="utf-8", newline="\n") as h:
        for row in apply_plan:
            h.write(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n")
    (pkg / "canonical-mapping.json").write_text(
        json.dumps(mapping, ensure_ascii=False, indent=1) + "\n", encoding="utf-8", newline="\n"
    )
    (pkg / "manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n"
    )
    print(json.dumps({"pkg": pkg_name, "ledger": len(ledger), "apply": len(apply_plan),
                      "create": len(created), "update": len(updated), "no_delta": len(no_delta),
                      "rejected": len(rejected), "covered": covered}, ensure_ascii=False))


if __name__ == "__main__":
    main()
