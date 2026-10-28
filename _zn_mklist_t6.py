# -*- coding: utf-8 -*-
from pathlib import Path

ROOT = Path(r"D:/中国设计史研究")
U = ROOT / "04-knowledge/units"
creates = [
    ("persons", "zhang-anshi"),
    ("persons", "chen-baoguang"),
    ("persons", "shi-you"),
    ("publications", "jijiu-pian"),
    ("terms", "yunqi-wen"),
    ("terms", "zhuyu-wen"),
    ("terms", "shuangling-wen"),
    ("works", "wanshi-ruyi-jin"),
    ("terms", "yinhua-fucai-sha"),
    ("terms", "jinyinse-yinhua-sha"),
    ("terms", "xinqi-xiu"),
    ("terms", "changshou-xiu"),
    ("terms", "chengyun-xiu"),
    ("works", "qianjin-tao"),
    ("terms", "man-sheng"),
    ("works", "xiangyang-leigutai-qiren-wen-qilian"),
    ("works", "sishui-laoding"),
    ("works", "fangzhi-tu-huaxiangshi"),
    ("works", "baiyu-shuangchi-guwen-bi"),
    ("works", "xianyang-yuma"),
    ("terms", "han-badao"),
]
updates = [
    "terms/rongquan-jin.md",
]
cpaths = []
for d, s in creates:
    p = U / d / (s + ".md")
    if not p.exists():
        raise SystemExit("missing " + str(p))
    cpaths.append(p.relative_to(ROOT).as_posix())
for u in updates:
    p = ROOT / "04-knowledge/units" / u
    if not p.exists():
        raise SystemExit("missing " + str(p))
(ROOT / "_zn_t6_files.txt").write_text("\n".join(cpaths) + "\n", encoding="utf-8", newline="\n")
(ROOT / "_zn_t6_all_files.txt").write_text(
    "\n".join(cpaths + ["04-knowledge/units/" + u for u in updates]) + "\n",
    encoding="utf-8", newline="\n",
)
print(len(cpaths), len(cpaths) + len(updates))
