# -*- coding: utf-8 -*-
import re
from pathlib import Path

root = Path(r"D:/中国设计史研究/04-knowledge/units")
keywords = ["铁", "冶铸", "编钟", "曾侯乙", "青铜", "礼器", "陶", "明器", "彩绘", "暗纹", "青瓷", "漆", "髹", "织机", "踞织", "提综", "佩璜", "深衣", "文质", "考工记", "营国", "车轮", "战车", "战船", "楼船", "几", "席", "案", "铜镜", "剑", "论语", "墨子", "老子", "孟子", "荀子", "韩非", "管子", "士", "犁", "鼓风", "排橐", "连续", "印纹", "针刻", "夹纻", "扣器", "楚国", "江陵", "望山", "齐国", "临淄", "新郑", "侯马", "错金", "曾侯"]
rows = []
for p in sorted(root.rglob("*.md")):
    try:
        text = p.read_text(encoding="utf-8")
    except Exception:
        continue
    m = re.search(r"^title_zh:\s*(.+)$", text, re.M)
    title = m.group(1).strip().strip('"').strip("'") if m else ""
    if not title:
        m = re.search(r"^name_zh:\s*(.+)$", text, re.M)
        title = m.group(1).strip().strip('"').strip("'") if m else ""
    mid = re.search(r"^id:\s*(.+)$", text, re.M)
    ident = mid.group(1).strip() if mid else p.stem
    hit = [k for k in keywords if k in title]
    if hit:
        rows.append((p.relative_to(root.parent.parent).as_posix(), ident, title, ",".join(hit)))
for r in rows:
    print("\t".join(r))
print("TOTAL", len(rows))
