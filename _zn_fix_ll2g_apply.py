# -*- coding: utf-8 -*-
"""Refresh the LL2g apply-plan hash after a pre-closure frontmatter fix."""
import hashlib
import json
from pathlib import Path

ROOT = Path(r"D:/中国设计史研究")
PKG = ROOT / "06-runtime/automation/2026-10-27-2011lilixin-units-batch-ll2g"
TARGET = "04-knowledge/units/publications/feng-ge-wen-ti.md"

data = (ROOT / TARGET).read_bytes().replace(b"\r\n", b"\n")
metrics = {
    "after_sha256": "sha256:" + hashlib.sha256(data).hexdigest(),
    "bytes": len(data),
    "lines": data.count(b"\n"),
}

path = PKG / "apply-plan.jsonl"
rows = [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]
changed = []
for row in rows:
    if row["target_ref"] == TARGET:
        changed.append({"old": row["after_sha256"], "new": metrics["after_sha256"]})
        row.update(metrics)
assert len(changed) == 1, changed
with path.open("w", encoding="utf-8", newline="\n") as h:
    for row in rows:
        h.write(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n")
print(json.dumps({"rows": len(rows), "changed": changed}, ensure_ascii=False))
