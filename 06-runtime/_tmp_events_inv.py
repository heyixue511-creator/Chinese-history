# -*- coding: utf-8 -*-
"""Write UTF-8 shortlists for active events and existing event KUs."""
import json
import re
from pathlib import Path

rows = [json.loads(l) for l in Path("06-runtime/state/candidate-index.jsonl").read_text(encoding="utf-8").splitlines() if l.strip()]
active = [r for r in rows if r["state"] == "needs_evidence" and r["candidate_type"] == "unit" and r["payload"].get("unit_type") == "event"]
lines = []
for r in active:
    p = r["payload"]
    s = p.get("source_span", {})
    lines.append(f"{r['candidate_id']}\t{s.get('line_start')}-{s.get('line_end')}\t{p.get('title')}\t{p.get('proposed_slug')}")
Path("06-runtime/_tmp_events.tsv").write_text("\n".join(lines), encoding="utf-8")
print("events", len(lines))

existing = []
for path in sorted(Path("04-knowledge/units/events").glob("*.md")):
    text = path.read_text(encoding="utf-8")
    m = re.search(r"^title:\s*(.+)$", text, re.M)
    d = re.search(r"^date:\s*(.+)$", text, re.M)
    existing.append(f"{path.stem}\t{m.group(1).strip() if m else '?'}\t{d.group(1).strip() if d else '?'}")
Path("06-runtime/_tmp_events_existing.tsv").write_text("\n".join(existing), encoding="utf-8")
print("existing", len(existing))
