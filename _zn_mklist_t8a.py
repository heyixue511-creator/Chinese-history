# -*- coding: utf-8 -*-
from pathlib import Path

ROOT = Path(r"D:/中国设计史研究")
U = ROOT / "04-knowledge/units"
creates = [
    ("terms", "juntian-zhi"),
    ("publications", "jingxing-ji"),
    ("terms", "sui-longbing-shuangshen-hu"),
    ("works", "yue-kiln-lianhua-wan-heye-tuo"),
    ("works", "baiyou-lianzuo-zhutai"),
    ("works", "tongguan-yao-you-guan"),
    ("terms", "jiaotai"),
    ("works", "lushan-yao-ci-paigu"),
    ("works", "sancai-guan"),
    ("works", "sancai-nv-yong"),
    ("works", "huwang-jin"),
    ("terms", "yunjian"),
    ("works", "yunjian-jin-qun"),
    ("works", "yuntou-jin-xie"),
    ("terms", "guiguan-bu"),
    ("terms", "baidie-bu"),
    ("terms", "hongxian-tan"),
]
updates = [
    "terms/baici.md",
    "terms/mise-porcelain.md",
    "works/fengshou-longbing-hu.md",
    "works/lianzhu-luwen-jin.md",
    "terms/tuanhua-wen.md",
    "works/anle-gongzhu-yuqun.md",
]
cpaths = []
for d, s in creates:
    p = U / d / (s + ".md")
    if not p.exists():
        raise SystemExit("missing " + str(p))
    cpaths.append(p.relative_to(ROOT).as_posix())
for u in updates:
    p = U / u
    if not p.exists():
        raise SystemExit("missing " + str(p))
(ROOT / "_zn_t8a_files.txt").write_text("\n".join(cpaths) + "\n", encoding="utf-8", newline="\n")
(ROOT / "_zn_t8a_all_files.txt").write_text(
    "\n".join(cpaths + ["04-knowledge/units/" + u for u in updates]) + "\n",
    encoding="utf-8", newline="\n",
)
print(len(cpaths), len(cpaths) + len(updates))
