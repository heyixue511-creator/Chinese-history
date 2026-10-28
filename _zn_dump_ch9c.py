# -*- coding: utf-8 -*-
"""Compact semantic re-read dump for batch-B files."""
import re
from pathlib import Path

ROOT = Path(r"D:/中国设计史研究")
files = [x.strip() for x in (ROOT / "_zn_ch9c_files.txt").read_text(encoding="utf-8").splitlines() if x.strip()]
for f in files:
    text = (ROOT / f).read_text(encoding="utf-8")
    fm, body = text.split("---\n", 2)[1], text.split("---\n", 2)[2]
    get = lambda k: (re.search(rf"^{k}: (.*)$", fm, re.M) or [None, ""])[1]
    desc = body.split("## 描述\n\n")[1].split("\n\n")[0]
    points = body.split("## 核心内容\n\n")[1].split("\n\n")[0].count("\n- ")
    scope = (re.search(r"scope_note: (.*)", body) or [None, ""])[1]
    rel = body.split("## 相关知识元\n\n")[1].split("\n\n")[0]
    quality = (re.search(r"匹配质量: (.*)", body) or [None, ""])[1]
    print(f"### {f}")
    print(f"T={get('title')} | type={get('type')} | dim={get('primary_dimension')} | conf={get('confidence')} | sc={get('source_count')} | v={get('version')} | pts={points}")
    print("D:", desc[:150].replace("\n", " "))
    print("S:", scope[:110])
    print("R:", rel[:110])
    print("Q:", quality[:110])
