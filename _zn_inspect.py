# -*- coding: utf-8 -*-
import collections
import json
import os

rows = json.load(open(r"D:/中国设计史研究/_zn_zn6a_rows.json", encoding="utf-8"))
paths = {p.replace(os.sep, "/") for r in rows for p in r["supported_by"]}
groups = collections.Counter(p.split("/")[2] for p in paths)
print(dict(groups))
for t in sorted(groups):
    print(t, groups[t], sorted(p.split("/", 3)[3] for p in paths if p.split("/")[2] == t))
print("distinct", len(paths))
