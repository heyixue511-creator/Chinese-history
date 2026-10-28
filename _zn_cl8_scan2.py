# -*- coding: utf-8 -*-
import re
from pathlib import Path

src = Path(r"D:/中国设计史研究/03基础书籍-md文档/中国艺术设计史（升级版）_夏燕靖_2016_上海人民美术出版社.md")
lines = src.read_text(encoding="utf-8").splitlines()
pat = re.compile(r"^(#{1,6}\s|\*\*|第[一二三四五六七八九十0-9]+[章节]|[一二三四五六七八九十]+、|\d+[．.]\s?|[（(]\d+[）)]|\d+）)")
for i in range(3059, 3594):
    t = lines[i].strip()
    if t and pat.match(t):
        print(i + 1, repr(t[:80]))
