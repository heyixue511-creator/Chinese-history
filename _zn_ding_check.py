import json, re
from pathlib import Path

root = Path(r"D:/中国设计史研究")
src_dir = root / "03基础书籍-md文档"


def norm(s):
    return "".join(ch for ch in s if ch.isalnum() or "\u4e00" <= ch <= "\u9fff")


big = "\n".join(norm(p.read_text(encoding="utf-8", errors="replace").replace("\r\n", "\n"))
                for p in sorted(src_dir.glob("*.md")))
for f in ["04-knowledge/units/terms/ding.md"]:
    text = (root / f).read_text(encoding="utf-8").replace("\r\n", "\n")
    lines = text.split("\n")
    end = next(i for i in range(1, len(lines)) if lines[i].strip() == "---")
    report = []
    for ln in range(end + 1, len(lines)):
        line = lines[ln]
        for m in re.finditer(r'"([^"]{4,})"', line):
            q = m.group(1)
            if len(norm(q)) < 4:
                continue
            if norm(q) not in big:
                report.append({"line": ln + 1, "quote": q[:80]})
    (root / "_zn_ding_ascii.json").write_text(json.dumps(report, ensure_ascii=False, indent=1), encoding="utf-8")
    print("findings:", len(report))
