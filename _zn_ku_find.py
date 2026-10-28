# -*- coding: utf-8 -*-
"""Find KU files whose names match any given keyword."""
import sys
from pathlib import Path

ROOT = Path(r"D:/中国设计史研究/04-knowledge/units")
keywords = [k.lower() for k in sys.argv[1:]]
for d in sorted(ROOT.iterdir()):
    if not d.is_dir():
        continue
    hits = [p.stem for p in sorted(d.glob("*.md"))
            if any(k in p.stem.lower() for k in keywords)]
    if hits:
        print(d.name, len(hits))
        print("  ", " ".join(hits))
