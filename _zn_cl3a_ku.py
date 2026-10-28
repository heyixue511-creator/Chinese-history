# -*- coding: utf-8 -*-
import sys
from pathlib import Path

ROOT = Path(r"D:/中国设计史研究/04-knowledge/units")
names = sys.argv[1:]
for name in names:
    p = ROOT / name
    print("\n=====", name, "=====")
    print(p.read_text(encoding="utf-8")[:1200].strip())
