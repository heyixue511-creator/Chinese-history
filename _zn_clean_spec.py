"""Strip batch-spec jargon from KU bodies: confidence-rationale bullets and 'per spec' clauses."""
import re
from pathlib import Path

ROOT = Path(r"D:/中国设计史研究/04-knowledge/units")
files = sorted(ROOT.rglob("*.md"))
removed_bullets = 0
rewritten = 0
changed_files = []

for p in files:
    text = p.read_text(encoding="utf-8")
    lines = text.split("\n")
    out = []
    local = False
    for line in lines:
        if line.startswith("- **confidence 依据**") or line.startswith("- **confidence 依据:**"):
            removed_bullets += 1
            local = True
            continue
        new = line
        new = new.replace("，按规格表定 confidence 为 ", "，confidence 定 ")
        new = new.replace("，按规格表定 ", "，confidence 定 ")
        new = new.replace("，按规格定 ", "，confidence 定 ")
        new = new.replace("按规格表定 confidence 为 ", "confidence 定 ")
        if new != line:
            rewritten += 1
            local = True
        out.append(new)
    if local:
        p.write_text("\n".join(out), encoding="utf-8", newline="\n")
        changed_files.append(str(p.relative_to(ROOT)))

print("files changed:", len(changed_files))
print("bullets removed:", removed_bullets)
print("lines rewritten:", rewritten)
for f in changed_files:
    print(" -", f)
