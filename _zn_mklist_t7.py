# -*- coding: utf-8 -*-
from pathlib import Path

ROOT = Path(r"D:/中国设计史研究")
U = ROOT / "04-knowledge/units"
creates = [
    ("terms", "liuchao-gongjiang-zhidu"),
    ("terms", "pan-kou-hu"),
    ("works", "huangyou-ci-bianhu"),
    ("terms", "hunping"),
    ("terms", "lianhua-wen"),
    ("works", "zhulin-qixian-rongqiqi-zhuanhua"),
    ("terms", "tonghua-bu"),
    ("persons", "su-shi-qianqin"),
    ("works", "niaoshou-wen-qi"),
    ("works", "dunhuang-125-126-ku-xiu"),
    ("terms", "liuchao-tongjing"),
    ("persons", "dai-kui"),
    ("works", "waguan-si-jiazhu-foxiang"),
    ("terms", "ban-qi"),
    ("terms", "lvchen-qi"),
    ("works", "beiwei-muban-qihua"),
    ("works", "xiao-jing-mu-shizhu"),
    ("works", "wangwen-boli-bei"),
]
updates = []
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
(ROOT / "_zn_t7_files.txt").write_text("\n".join(cpaths) + "\n", encoding="utf-8", newline="\n")
(ROOT / "_zn_t7_all_files.txt").write_text(
    "\n".join(cpaths + ["04-knowledge/units/" + u for u in updates]) + "\n",
    encoding="utf-8", newline="\n",
)
print(len(cpaths), len(cpaths) + len(updates))
