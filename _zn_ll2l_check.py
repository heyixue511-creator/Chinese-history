# -*- coding: utf-8 -*-
"""Verify every quoted span in batch-LL2l entries against the source."""
import importlib.util
import re
from pathlib import Path

ROOT = Path(r"D:/中国设计史研究")
SRC = ROOT / "03基础书籍-md文档/中国设计艺术史论_李立新_2011_人民出版社.md"
BOOKS = [
    (SRC.name, SRC.read_text(encoding="utf-8").splitlines()),
]

PARTS = ("_zn_ll2l_e1.py",)
E = []
for name in PARTS:
    spec = importlib.util.spec_from_file_location(name.replace(".py", ""), ROOT / name)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    E += getattr(m, "E", [])
X = []

line_claim = re.compile(r"（(L[0-9][0-9,、\s\-–]*)）")
quote_re = re.compile(r"“([^”]+)”")
xquote_re = re.compile(r"「([^」]+)」")


def norm(s):
    return re.sub(r"[^0-9A-Za-z一-鿿]", "", s)


WHOLE = norm("\n".join("\n".join(lines) for _, lines in BOOKS))


def expand(claim):
    nums = set()
    for part in claim.replace(" ", "").replace("、", ",").split(","):
        if not part:
            continue
        if "–" in part or "-" in part:
            a, b = re.split(r"[–-]", part, maxsplit=1)
            nums.update(range(int(a[1:]), int(b[1:]) + 1))
        else:
            nums.add(int(part[1:]))
    return nums


def single_line_hits(qn):
    hits = []
    for book, lines in BOOKS:
        for i, ln in enumerate(lines):
            if qn in norm(ln):
                hits.append((book, i + 1))
    return hits


problems = []
units = [(e["slug"], e["points"], e["desc"]) for e in E]

for slug, points, desc in units:
    for p in points:
        m = line_claim.search(p)
        claims = expand(m.group(1)) if m else set()
        for q in quote_re.findall(p):
            qn = norm(q)
            hits = single_line_hits(qn)
            if not hits:
                problems.append((slug, "MISSING", q[:40], sorted(claims), "not found in any single line"))
                continue
            if claims and not any(n in claims for _, n in hits):
                problems.append((slug, "LINE", q[:40], sorted(claims), hits[:8]))
        for q in xquote_re.findall(p):
            qn = norm(q)
            if qn not in WHOLE:
                problems.append((slug, "X-MISSING", q[:40], sorted(claims), "not found"))
                continue
            hits = single_line_hits(qn)
            if hits and claims and not any(n in claims for _, n in hits):
                problems.append((slug, "X-LINE", q[:40], sorted(claims), hits[:8]))
    for q in quote_re.findall(desc):
        if norm(q) not in WHOLE:
            problems.append((slug, "DESC-MISSING", q[:40], [], "not found"))
    for q in xquote_re.findall(desc):
        if norm(q) not in WHOLE:
            problems.append((slug, "DESC-X-MISSING", q[:40], [], "not found"))

print("create entries:", len(E))
print("quotes checked:", sum(len(re.findall(r"“[^”]+”", p)) for _, pts, _ in units for p in pts))
print("problems:", len(problems))
for x in problems:
    print(" | ".join(str(i) for i in x))
