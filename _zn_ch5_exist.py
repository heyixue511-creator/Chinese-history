# -*- coding: utf-8 -*-
"""For each ch5 candidate, look for existing KU files whose title/aliases contain the entity."""
import io, json, re
from pathlib import Path

ROOT = Path(r"D:/中国设计史研究")
UNITS = ROOT / "04-knowledge/units"
rows = json.load(io.open("_zn_ch5_rows.json", encoding="utf-8"))

index = []
for p in sorted(UNITS.rglob("*.md")):
    txt = p.read_text(encoding="utf-8")
    m = re.search(r"^title:\s*(.+)$", txt, re.M)
    title = m.group(1).strip() if m else ""
    am = re.search(r"^aliases:\s*\n((?:\s+-\s*.+\n)+)", txt, re.M)
    aliases = re.findall(r"-\s*(.+)", am.group(1)) if am else []
    index.append((p.relative_to(UNITS).as_posix(), title, aliases))

for r in rows:
    p = r["payload"]
    name = (p.get("title") or "").strip()
    bare = re.sub(r"[《》()（）]", "", name)
    core = re.sub(r"[（(].*?[）)]", "", bare).strip()
    hits = []
    for rel, title, aliases in index:
        hay = title + " " + " ".join(aliases)
        if core and (core in hay or (len(bare) > 1 and bare in hay)):
            hits.append(rel + " [" + title + "]")
    print("%-12s %-24s -> %s" % (r["candidate_id"].split(":")[1], name, "; ".join(hits) if hits else "-"))
