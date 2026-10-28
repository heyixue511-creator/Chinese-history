# -*- coding: utf-8 -*-
import json
import re
from pathlib import Path

root = Path(r"D:/中国设计史研究")
src = root / "03基础书籍-md文档/中国艺术设计史（升级版）_夏燕靖_2016_上海人民美术出版社.md"
lines = src.read_text(encoding="utf-8").splitlines()
print("total_lines", len(lines))
for i in range(3059, 3594):
    t = lines[i].strip()
    if re.match(r"^(第.{1,4}章|\d+[\.、)]|[（(]\d+[）)]|\d+）)", t):
        print(i + 1, t[:70])
m = json.loads((root / "06-runtime/automation/2026-10-27-2016xiayanjing-claims-batch-cl5a/manifest.json").read_text(encoding="utf-8"))
print("scope_spans", len(m["scope_spans"]), m["scope_spans"])
idx = (root / "06-runtime/automation/index.md").read_text(encoding="utf-8")
print("index_head", idx.splitlines()[:6])
