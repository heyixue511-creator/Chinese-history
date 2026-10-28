from pathlib import Path
u=Path(r"D:/中国设计史研究/04-knowledge/units")
for rel in ["works/liujin-tong-jiuzun.md","works/wenjiu-tongbeilu.md","terms/boshanlu.md","terms/dongwuxing-dengju.md"]:
    t=(u/rel).read_text(encoding="utf-8").splitlines()
    print("=== "+rel)
    for i,l in enumerate(t,1):
        if "右玉" in l or "竹节" in l or "金胜" in l: print(i,l[:260])
