# -*- coding: utf-8 -*-
"""List all remaining 2016 needs_evidence candidates (CL10a scope)."""
import json
from pathlib import Path

ROOT = Path(r"D:/中国设计史研究")
DOC = "2016-xiayanjing-zhongguo-yishu-shejishi-upgrade"
CAND = ROOT / "06-runtime/state/candidate-index.jsonl"

rows = [json.loads(l) for l in CAND.read_text(encoding="utf-8").splitlines() if l.strip()]
sel = [r for r in rows if r["candidate_id"].startswith(DOC + ":") and r["state"] == "needs_evidence"]
sel.sort(key=lambda r: (r["payload"]["source_span"]["line_start"], r["candidate_id"]))
print("count", len(sel))
for r in sel:
    span = r["payload"]["source_span"]
    p = r["payload"]
    print(json.dumps({
        "candidate_id": r["candidate_id"],
        "span": [span["line_start"], span["line_end"]],
        "kind": span.get("span_kind"),
        "key_lines": span.get("key_lines"),
        "blocks": span.get("block_ids"),
        "section": span.get("section"),
        "claim_scope": p.get("claim_scope"),
        "claim_text": p.get("claim_text"),
        "subject": p.get("subject"),
        "knowledge_match": p.get("knowledge_match"),
        "candidate_type": r["candidate_type"],
    }, ensure_ascii=False))
