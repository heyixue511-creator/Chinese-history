import re
from pathlib import Path
u=Path(r"D:/中国设计史研究/04-knowledge/units")
for kw in ["金胜","小金灶","蒜头瓶","茧形壶","画象砖","铜鼓","规矩镜","说唱俑","兵马俑","长乐宫钟","鸟篆文壶","阳信家","右玉","银首人形灯","鼎形铜灯","牛灯","竹节","博山炉"]:
    hits=[]
    for f in u.rglob("*.md"):
        t=f.read_text(encoding="utf-8")
        if kw in t:
            hits.append(f.relative_to(u).as_posix())
    print(kw, len(hits), hits[:10])
