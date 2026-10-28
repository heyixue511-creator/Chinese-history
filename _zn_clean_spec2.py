"""Second cleanup pass: '按规格记' variants."""
import re
from pathlib import Path

ROOT = Path(r"D:/中国设计史研究/04-knowledge/units")
changed = []
for p in sorted(ROOT.rglob("*.md")):
    text = p.read_text(encoding="utf-8")
    new = text
    new = new.replace("，按规格记 ", "，confidence 定 ")
    new = new.replace("，confidence 按规格记 ", "，confidence 定 ")
    new = new.replace("；按规格记 ", "；confidence 定 ")
    if new != text:
        p.write_text(new, encoding="utf-8", newline="\n")
        changed.append(str(p.relative_to(ROOT)))
print("changed:", len(changed))
for c in changed:
    print(" -", c)
