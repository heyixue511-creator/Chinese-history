import json, re, sys
from pathlib import Path

root = Path(r"D:/中国设计史研究")
src_dir = root / "03基础书籍-md文档"


def norm(s):
    return "".join(ch for ch in s if ch.isalnum() or "\u4e00" <= ch <= "\u9fff")


corpus = []
for p in sorted(src_dir.glob("*.md")):
    text = p.read_text(encoding="utf-8", errors="replace").replace("\r\n", "\n")
    corpus.append((p.name, norm(text)))
big = "\n".join(c[1] for c in corpus)

args = sys.argv[1:]
if len(args) == 1 and args[0].startswith("@"):
    files = [x.strip() for x in (root / args[0][1:]).read_text(encoding="utf-8").splitlines() if x.strip()]
else:
    files = args
report = []
for f in files:
    p = root / f
    text = p.read_text(encoding="utf-8").replace("\r\n", "\n")
    lines = text.split("\n")
    start = 0
    if lines and lines[0].strip() == "---":
        for i in range(1, len(lines)):
            if lines[i].strip() == "---":
                start = i + 1
                break
    for ln in range(start, len(lines)):
        line = lines[ln]
        for m in re.finditer(r"“([^“”]*)”", line):
            q = m.group(1)
            if len(norm(q)) < 2:
                continue
            if norm(q) not in big:
                report.append({"file": f, "line": ln + 1, "quote": q, "status": "MISS"})
        if "“" in line and line.count("“") != line.count("”"):
            report.append({"file": f, "line": ln + 1, "quote": line.strip()[:120], "status": "UNBALANCED"})
        if re.search(r"“[^“”]*“[^”]*”", line):
            report.append({"file": f, "line": ln + 1, "quote": line.strip()[:120], "status": "NESTED"})

out = root / "_zn_audit_result.json"
out.write_text(json.dumps(report, ensure_ascii=False, indent=1), encoding="utf-8")
print("findings:", len(report))
