# -*- coding: utf-8 -*-
"""Remove previously generated chapter 8 KU files and rebuild the file list."""
import importlib.util
import json
from pathlib import Path

ROOT = Path(r"D:/中国设计史研究")
UNIT = ROOT / "04-knowledge/units"


def load(name):
    path = ROOT / name
    spec = importlib.util.spec_from_file_location(path.stem, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.E


entries = []
for part in ("_zn_ch8_e1.py", "_zn_ch8_e2.py", "_zn_ch8_e3.py"):
    entries += load(part)

paths = []
removed = 0
for e in entries:
    p = UNIT / e["dir"] / (e["slug"] + ".md")
    paths.append(str(p.relative_to(ROOT)).replace("\\", "/"))
    if p.exists():
        p.unlink()
        removed += 1

(ROOT / "_zn_ch8_files.txt").write_text("\n".join(paths) + "\n", encoding="utf-8", newline="\n")
print(json.dumps({"entries": len(entries), "removed": removed}, ensure_ascii=False))
