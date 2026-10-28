# -*- coding: utf-8 -*-
import re
from pathlib import Path
ROOT = Path(r"D:/中国设计史研究")
keys = ["魏晋","南北朝","白瓷","青瓷","黑瓷","缥瓷","釉陶","铅釉","瓷","丝","锦","服","九品","冠","铜镜","冶铁","钢铁","兵器","铠","卤簿","车","船","家具","胡床","高形","佛","寺","石窟","造像","气韵","刘昼","玄学","马钧","提花","织机","缬","染","花丝","金饰","蜀锦","慎","谢灵运","木屐","琉璃","砖塔","莲花"]
rows = []
for p in sorted((ROOT / "04-knowledge/units").rglob("*.md")):
    text = p.read_text(encoding="utf-8", errors="replace")
    m = re.search(r"^title:\s*(.+)$", text, re.M)
    title = m.group(1).strip().strip('"').strip("'") if m else ""
    rel = str(p.relative_to(ROOT)).replace("\\", "/")
    if any(k in title for k in keys):
        rows.append(f"{rel}\t{title}")
(ROOT / "_zn_cl2d_lookup.txt").write_text("\n".join(rows), encoding="utf-8")
print(len(rows))
