# -*- coding: utf-8 -*-
import re, sys
from pathlib import Path
ROOT = Path(r"D:/中国设计史研究")
files = [x.strip() for x in (ROOT/sys.argv[1]).read_text(encoding="utf-8").splitlines() if x.strip()]
pat = re.compile(r"`((?:persons|works|places|terms|publications|institutions|procedures|events)/[a-z0-9\-]+\.md)`")
missing = []
for f in files:
    text = (ROOT/f).read_text(encoding="utf-8")
    for m in set(pat.findall(text)):
        if not (ROOT/"04-knowledge/units"/m).exists():
            missing.append((f, m))
for f, m in missing:
    print("MISSING", m, "<-", f)
print("missing:", len(missing))
