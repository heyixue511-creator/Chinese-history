# -*- coding: utf-8 -*-
"""Check source blocks for duplicates and source_count consistency."""
import re
from collections import Counter
from pathlib import Path

bad = []
for path in sorted(Path("04-knowledge/units").rglob("*.md")):
    text = path.read_text(encoding="utf-8")
    m = re.search(r"^source_count:\s*(\d+)\s*$", text, re.M)
    if not m:
        bad.append((str(path), "no source_count"))
        continue
    declared = int(m.group(1))
    cites = re.findall(r"^  - citation:\s*(.+)$", text, re.M)
    if declared != len(cites):
        bad.append((str(path), f"declared {declared} vs blocks {len(cites)}"))
    dupes = [c for c, n in Counter(cites).items() if n > 1]
    if dupes:
        bad.append((str(path), f"duplicate citation x{len(dupes)}: {dupes[0][:80]}"))

print("files checked", sum(1 for _ in Path("04-knowledge/units").rglob("*.md")))
print("issues", len(bad))
for item in bad:
    print(" -", item[0], "|", item[1])
