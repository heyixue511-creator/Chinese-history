# -*- coding: utf-8 -*-
"""Purge and relist chapter 9 batch A write-back files."""
import importlib.util
from pathlib import Path

ROOT = Path(r"D:/中国设计史研究")
UNIT = ROOT / "04-knowledge/units"

spec = importlib.util.spec_from_file_location("e1", ROOT / "_zn_ch9a_e1.py")
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

paths = []
removed = 0
for e in mod.E:
    p = UNIT / e["dir"] / (e["slug"] + ".md")
    paths.append(str(p.relative_to(ROOT)).replace("\\", "/"))
    if p.exists():
        p.unlink()
        removed += 1

updates = [
    "04-knowledge/units/works/beijing-zijincheng.md",
    "04-knowledge/units/terms/central-axis.md",
    "04-knowledge/units/publications/gongcheng-zuofa.md",
    "04-knowledge/units/places/xian.md",
]
paths += updates
(ROOT / "_zn_ch9_files.txt").write_text("\n".join(paths) + "\n", encoding="utf-8", newline="\n")
print({"entries": len(mod.E), "removed": removed, "files": len(paths)})
