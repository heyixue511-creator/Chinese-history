from pathlib import Path
u=Path(r"D:/中国设计史研究/04-knowledge/units")
for rel,kws in [("terms/dian-la-man.md",["铜鼓"]),("places/xianyang.md",["蒜头瓶","茧形壶"]),("terms/yuhuchun-ping.md",["蒜头瓶"]),("places/dengxian-xuezhuang-huaxiangzhuan-mu.md",["画象砖"]),("places/mancheng-hanmu.md",["长乐宫钟","鸟篆文壶"]),("terms/ding.md",["鼎形铜灯"])]:
    t=(u/rel).read_text(encoding="utf-8").splitlines()
    print("=== "+rel)
    for i,l in enumerate(t,1):
        if any(k in l for k in kws): print(i,l[:220])
