# -*- coding: utf-8 -*-
import re
from pathlib import Path
ROOT = Path(r"D:/中国设计史研究")
rows = []
for p in sorted((ROOT / "04-knowledge/units").rglob("*.md")):
    text = p.read_text(encoding="utf-8", errors="replace")
    m = re.search(r"^title:\s*(.+)$", text, re.M)
    title = m.group(1).strip().strip('"').strip("'") if m else ""
    rows.append((str(p.relative_to(ROOT)).replace("\\", "/"), title))
keys = ["铁","冶","铜","镜","车","船","丝","绸","瓷","陶","漆","纺","织","染","绣","瓦","砖","汉","秦","农具","犁","耧","灯","炉","礼","儒","考工","营造","建筑","家具","带钩","服饰","冠","印","玉","剑","兵器","墓","俑","园林","斗","拱"]
for path, title in rows:
    if any(k in title for k in keys) or any(k in path for k in ["iron","tong","copper","silk","porcelain","lacquer","qin","han","jade","kiln","chariot","boat"]):
        print(f"{path}\t{title}")
