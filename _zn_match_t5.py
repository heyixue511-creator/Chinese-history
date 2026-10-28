# -*- coding: utf-8 -*-
"""Recall existing KUs for T5 candidate names."""
import json
import re
from pathlib import Path

ROOT = Path(r"D:/中国设计史研究")
UNITS = ROOT / "04-knowledge/units"
INDEX = ROOT / "06-runtime/state/candidate-index.jsonl"
DOC = "2010-tianzibing-zhongguo-gongyi-meishushi"

rows = [json.loads(l) for l in INDEX.read_text(encoding="utf-8").splitlines() if l.strip()]
cands = [
    r for r in rows
    if r["candidate_id"].startswith(DOC + ":")
    and r["state"] == "needs_evidence"
    and r["candidate_type"] == "unit"
    and 2069 <= r["payload"]["source_span"]["line_start"] <= 2712
]

files = sorted(UNITS.rglob("*.md"))
docs = []
for f in files:
    text = f.read_text(encoding="utf-8")
    title = re.search(r"^title:\s*(.+)$", text, re.M)
    aliases = re.search(r"^aliases:\n((?:\s+-\s+.+\n)+)", text, re.M)
    docs.append((
        f.relative_to(UNITS).as_posix(),
        title.group(1) if title else "",
        aliases.group(1) if aliases else "",
        text,
    ))

for r in cands:
    p = r["payload"]
    name = re.sub(r"（.*?）|\(.*?\)", "", p.get("title") or "").strip()
    name = name.split("、")[0]
    hits = []
    for rel, title, aliases, text in docs:
        if name and (name in title or name in aliases or name in rel):
            hits.append(rel)
    print(r["candidate_id"].split(":")[1], p.get("title"), "=>", ", ".join(hits[:8]) or "-")
