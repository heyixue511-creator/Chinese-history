# -*- coding: utf-8 -*-
"""Normalize ASCII double/single quotes to Chinese quotes in tongjing.md body."""
from pathlib import Path

p = Path(r"D:/中国设计史研究/04-knowledge/units/terms/tongjing.md")
text = p.read_text(encoding="utf-8").replace("\r\n", "\n")
lines = text.split("\n")
# locate end of frontmatter
end = None
if lines[0].strip() == "---":
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            end = i
            break
assert end is not None

odd = []
for i in range(end + 1, len(lines)):
    ln = lines[i]
    if ln.count('"') % 2 or ln.count("'") % 2:
        odd.append((i + 1, ln.count('"'), ln.count("'")))
if odd:
    raise SystemExit("odd quote counts: " + repr(odd))


def conv(line):
    out = []
    dq = True
    sq = True
    for ch in line:
        if ch == '"':
            out.append("“" if dq else "”")
            dq = not dq
        elif ch == "'":
            out.append("‘" if sq else "’")
            sq = not sq
        else:
            out.append(ch)
    return "".join(out)


for i in range(end + 1, len(lines)):
    lines[i] = conv(lines[i])

p.write_text("\n".join(lines), encoding="utf-8", newline="\n")
print("normalized body lines:", len(lines) - end - 1)
