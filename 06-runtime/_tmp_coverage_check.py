# -*- coding: utf-8 -*-
"""Check coverage of candidate topics in existing KU files."""
from pathlib import Path

BASE = Path("04-knowledge/units")
CHECKS = [
    ("works/miaoying-si-baita.md", ["1271", "至元八年", "阿尼哥", "50.9", "覆钵"]),
    ("works/zhongshan-ling-1929.md", ["1927", "竞图", "吕彦直", "征求", "首奖"]),
    ("works/guiguxiashan-qinghua-guan.md", ["2005", "1568", "克里斯蒂", "拍卖"]),
    ("terms/zhisun-fu.md", ["1321", "元英宗", "质孙", "一色衣"]),
    ("works/zhenghe-baochuan.md", ["1405", "七下西洋", "郑和", "贸易瓷"]),
    ("persons/dayu.md", ["九鼎", "荆山", "九州", "铸"]),
    ("persons/shang-tang.md", ["灭夏", "七十乘", "良车", "甘泽"]),
    ("persons/mozi.md", ["止楚攻宋", "公输盘", "云梯", "禽滑厘"]),
    ("persons/pang-xunqin.md", ["1957", "反党", "斗争"]),
    ("persons/guo-shoujing.md", ["授时历", "1276", "太史局", "简仪"]),
    ("persons/anige.md", ["白塔", "1271", "至元八年", "妙应寺"]),
    ("works/renmin-dahuitang-1959.md", ["十大建筑", "国庆工程", "1958"]),
    ("persons/sun-yat-sen.md", ["剪辫", "易服", "中山装"]),
    ("terms/zhongshanzhuang.md", ["剪辫", "易服", "1912"]),
    ("terms/sichou-zhilu.md", ["张骞", "西域", "公元前138"]),
    ("terms/blue-and-white-porcelain.md", ["克拉克", "1602"]),
    ("events/xinhai-geming.md", ["剪辫", "易服", "中山装"]),
    ("works/da-yu-ding.md", ["九鼎", "禹"]),
    ("terms/keju", ["科举"]),
]
out = []
for rel, kws in CHECKS:
    p = BASE / rel
    if not p.exists():
        out.append(f"## {rel} MISSING")
        continue
    text = p.read_text(encoding="utf-8")
    hits = []
    for kw in kws:
        idx = text.find(kw)
        if idx >= 0:
            start = max(0, idx - 60)
            end = min(len(text), idx + 120)
            snippet = text[start:end].replace("\n", " ")
            hits.append(f"  [{kw}] …{snippet}…")
    out.append(f"## {rel} ({len(hits)}/{len(kws)} keywords)")
    out.extend(hits)
Path("06-runtime/_tmp_coverage.txt").write_text("\n".join(out), encoding="utf-8")
print("written", len(CHECKS))
