# -*- coding: utf-8 -*-
"""Verify every quoted span in batch-T12 create entries against the sources, with line claims."""
import importlib.util
import re
from pathlib import Path

ROOT = Path(r"D:/中国设计史研究")
SRCS = [
    ROOT / "03基础书籍-md文档/中国工艺美术史（修订本）_田自秉_2010_东方出版中心.md",
    ROOT / "03基础书籍-md文档/中国设计史_夏燕靖_2009_上海人民美术出版社.md",
]
BOOKS = [(p.name, p.read_text(encoding="utf-8").splitlines()) for p in SRCS]

E = []
for name in ("_zn_t12_e1.py", "_zn_t12_e2.py", "_zn_t12_e3.py", "_zn_t12_e4.py"):
    spec = importlib.util.spec_from_file_location(name.replace(".py", ""), ROOT / name)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    E += m.E

CREATE_SLUGS = set(
    x.strip().split("/")[-1][:-3]
    for x in (ROOT / "_zn_t12_all_files.txt").read_text(encoding="utf-8").splitlines()
    if x.strip()
)
E = [e for e in E if e["slug"] in CREATE_SLUGS]

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
for e in E:
    for p in e["points"]:
        m = line_claim.search(p)
        claims = expand(m.group(1)) if m else set()
        for q in quote_re.findall(p):
            qn = norm(q)
            hits = single_line_hits(qn)
            if not hits:
                problems.append((e["slug"], "MISSING", q[:40], sorted(claims), "not found in any single line"))
                continue
            if claims and not any(n in claims for _, n in hits):
                problems.append((e["slug"], "LINE", q[:40], sorted(claims), hits[:8]))
        for q in xquote_re.findall(p):
            qn = norm(q)
            if qn not in WHOLE:
                problems.append((e["slug"], "X-MISSING", q[:40], sorted(claims), "not found"))
                continue
            hits = single_line_hits(qn)
            if hits and claims and not any(n in claims for _, n in hits):
                problems.append((e["slug"], "X-LINE", q[:40], sorted(claims), hits[:8]))
    for q in quote_re.findall(e["desc"]):
        if norm(q) not in WHOLE:
            problems.append((e["slug"], "DESC-MISSING", q[:40], [], "not found"))
    for q in xquote_re.findall(e["desc"]):
        if norm(q) not in WHOLE:
            problems.append((e["slug"], "DESC-X-MISSING", q[:40], [], "not found"))

print("entries:", len(E))
print("quotes checked:", sum(len(re.findall(r"“[^”]+”", p)) for e in E for p in e["points"]))
print("problems:", len(problems))
for x in problems:
    print(" | ".join(str(i) for i in x))
