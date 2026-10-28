from pathlib import Path
u=Path(r"D:/中国设计史研究/04-knowledge/units")
for d in ["places","terms","procedures","institutions","persons","publications","works"]:
    fs=sorted(p.name for p in (u/d).glob("*.md"))
    print("==",d,len(fs))
    print(" ".join(fs))
