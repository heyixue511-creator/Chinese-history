# -*- coding: utf-8 -*-
import json

SRC = r"D:/中国设计史研究/03基础书籍-md文档/中国艺术设计史_赵农_2009_高等教育出版社.md"
rows = json.load(open(r"D:/中国设计史研究/_zn_zn6a_rows.json", encoding="utf-8"))
lines = open(SRC, encoding="utf-8").read().split("\n")

out = []
for r in rows:
    sp = r["source"]["source_span"]
    out.append("=== %s  L%d-%d" % (r["claim_id"], sp["line_start"], sp["line_end"]))
    for k in sp["key_lines"]:
        out.append("L%d: %s" % (k, lines[k - 1].strip()))
open(r"D:/中国设计史研究/_zn_keylines.txt", "w", encoding="utf-8", newline="\n").write("\n".join(out) + "\n")
print("lines", len(out))
