# -*- coding: utf-8 -*-
from pathlib import Path

ROOT = Path(r"D:/中国设计史研究")
U = ROOT / "04-knowledge/units"
creates = [
    ("works", "liujin-yinzhu-jie-xunlu"),
    ("works", "changlegong-zhong"),
    ("works", "cuojin-yin-niaozhuanwen-hu"),
    ("works", "jinyincuo-shouliewen-tongcheshi"),
    ("works", "xiche-tu-kongxinzhuan"),
    ("works", "cailian-huaxiangzhuan"),
    ("works", "wanjian-wuyue-huaxiangzhuan"),
    ("works", "shuochangyong"),
    ("works", "qiyu-yunmeng-shuihudi-33"),
    ("works", "fengniaoxing-shao"),
    ("works", "qihui-mushu-mubi"),
    ("works", "yinshou-renxing-deng"),
    ("works", "hanjiang-niudeng"),
    ("works", "yangxinjia-tonglu"),
    ("works", "jinsheng-han"),
    ("works", "xiao-jinzao"),
    ("terms", "suantouping"),
    ("terms", "jianxinghu"),
    ("terms", "guijujing"),
    ("terms", "tonggu"),
    ("terms", "huaxiangzhuan"),
    ("terms", "gong-zu-tu"),
    ("terms", "ao-qin-tongqi"),
]
updates = [
    "works/tongbenma.md",
    "terms/si-shen.md",
    "works/qin-bing-ma-yong.md",
    "works/liujin-tong-jiuzun.md",
    "works/yishe-shouhuo-huaxiangzhuan.md",
    "works/shuihudi-qin-bamboo-slips.md",
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
(RN := ROOT / "_zn_t5_files.txt").write_text("\n".join(cpaths) + "\n", encoding="utf-8", newline="\n")
(ROOT / "_zn_t5_all_files.txt").write_text(
    "\n".join(cpaths + ["04-knowledge/units/" + u for u in updates]) + "\n",
    encoding="utf-8", newline="\n",
)
print(len(cpaths), len(cpaths) + len(updates))
