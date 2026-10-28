# -*- coding: utf-8 -*-
"""Match chapter candidates against existing KUs by title/alias tokens."""
import json
import re
import sys
from pathlib import Path

ROOT = Path(r"D:/中国设计史研究")
rows = json.load(open(ROOT / "_zn_ch6_rows.json", encoding="utf-8"))


def norm(s):
    s = re.sub(r"[《》（）()·、，,。\s]", "", s or "")
    return s


index = {}
for p in (ROOT / "04-knowledge/units").rglob("*.md"):
    text = p.read_text(encoding="utf-8")
    fm = text.split("\n---\n", 1)[0]
    title = re.search(r"(?m)^title: (.+)$", fm)
    t = title.group(1) if title else ""
    keys = {norm(t)}
    m = re.search(r"(?ms)^aliases:\n((?:  - .+\n?)+)", fm)
    if m:
        for line in m.group(1).split("\n"):
            v = line.strip()[2:].strip().strip('"')
            if v and v not in ("[]",):
                keys.add(norm(v))
    m2 = re.search(r"(?m)^term_zh: (.+)$", fm)
    if m2:
        keys.add(norm(m2.group(1)))
    for k in keys:
        if k:
            index.setdefault(k, []).append(str(p.relative_to(ROOT / "04-knowledge/units")).replace("\\", "/"))

for r in rows:
    p = r["payload"]
    title = p.get("title", "")
    slug = p.get("proposed_slug", "")
    hits = set()
    for k in {norm(title), norm(re.sub(r"（.*?）", "", title)), norm(re.sub(r"《(.*?)》", r"\1", title))}:
        hits.update(index.get(k, []))
    if slug:
        for path in index.values():
            if any(x.endswith("/" + slug + ".md") for x in path):
                hits.update(path)
    if hits:
        print(f"{r['candidate_id'].split(':')[1]} | {title} | {p.get('unit_type')} -> {sorted(hits)}")
