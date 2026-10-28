# -*- coding: utf-8 -*-
import json
from pathlib import Path

root = Path(r"D:/中国设计史研究")
blocks = [json.loads(l) for l in (root / "03-processing/2009-xiayanjing-zhongguo-shejishi/source-map.jsonl").read_text(encoding="utf-8").splitlines() if l.strip()]
lines = [791,801,835,841,853,857,863,870,874,875,876,900,912,938,954,983,1006,1034,1059,1067,1088,1096,1128,1132,1157,1161,1177,1185,1202,1206,1214,1222,1228,1232,1244,1245,1246,1248,1259]
for ln in lines:
    hits = [b["block_id"] for b in blocks if b["line_start"] <= ln <= b["line_end"]]
    print(ln, ",".join(hits))
print("---cand-03-03 blocks---")
for b in blocks:
    if b["line_start"] <= 1262 and b["line_end"] >= 1255:
        print(b["block_id"], b["block_type"], b["line_start"], b["line_end"])
