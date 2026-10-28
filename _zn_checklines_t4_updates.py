# -*- coding: utf-8 -*-
"""Line-claim check for T4 update files: every quote on a claimed line must hit one claimed line."""
import re
from pathlib import Path

ROOT = Path(r"D:/中国设计史研究")
SRC = ROOT / "03基础书籍-md文档/中国工艺美术史（修订本）_田自秉_2010_东方出版中心.md"
lines = SRC.read_text(encoding="utf-8").splitlines()

FILES = [
    "04-knowledge/units/works/yanle-shuilu-gongzhan-wen-hu.md",
    "04-knowledge/units/works/zenghouyi-zunpan.md",
    "04-knowledge/units/works/caiqi-mudiao-dongwu-zuoping.md",
    "04-knowledge/units/works/wudao-renwu-dongwu-wen-sanse-jin.md",
    "04-knowledge/units/terms/chunqiu-zhanguo-qingtong-chuishiqi.md",
    "04-knowledge/units/terms/tongjing.md",
    "04-knowledge/units/persons/ganjiang.md",
]

claim_re = re.compile(r"（(L[0-9][0-9,、\s\-–]*)）")
quote_re = re.compile(r"“([^”]+)”")


def norm(s):
    return re.sub(r"[^0-9A-Za-z一-鿿]", "", s)


def expand(claim):
    nums = set()
    for part in claim.replace(" ", "").replace("、", ",").split(","):
        if not part:
            continue
        if "–" in part or "-" in part:
            a, b = re.split(r"[–-]", part, maxsplit=1)
            nums.update(range(int(a[1:]), int(b[1:]) + 1))
        else:
            nums.add(int(part[1:]))
    return nums


problems = []
checked = 0
for f in FILES:
    text = (ROOT / f).read_text(encoding="utf-8").replace("\r\n", "\n")
    for i, line in enumerate(text.split("\n"), start=1):
        claims = set()
        for c in claim_re.findall(line):
            claims |= expand(c)
        if not claims:
            continue
        for q in quote_re.findall(line):
            checked += 1
            qn = norm(q)
            hits = [j + 1 for j, src in enumerate(lines) if qn in norm(src)]
            if not hits:
                problems.append((f, i, "MISSING", q[:40], sorted(claims)))
            elif not (set(hits) & claims):
                problems.append((f, i, "LINE", q[:40], sorted(claims), hits[:8]))

print("quotes checked on claimed lines:", checked)
print("problems:", len(problems))
for p in problems:
    print(" | ".join(str(x) for x in p))
