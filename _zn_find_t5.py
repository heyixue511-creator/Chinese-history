from pathlib import Path
u=Path(r"D:/中国设计史研究/04-knowledge/units")
import re
for d in ["places","terms","procedures","institutions","publications"]:
    fs=sorted(p.stem for p in (u/d).glob("*.md"))
    print("==",d)
    for s in fs:
        if any(k in s for k in ["han","qin","ding","xin","cheng","jiang","yang","qi","jin","tong","zhu","wa","jing","qi","zhi","shao","fu","gong","ling","mu","kiln","yao"]):
            print(s, end=" ")
    print()
