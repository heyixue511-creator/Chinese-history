# -*- coding: utf-8 -*-
"""Search 2009 claims for possible Wei-Jin duplicates."""
import yaml
from pathlib import Path

ROOT = Path(r"D:/中国设计史研究")
rows = yaml.safe_load((ROOT / "04-knowledge/quality/claim-registry.yml").read_text(encoding="utf-8"))
old = [r for r in rows if r["source"]["doc_id"] == "2009-xiayanjing-zhongguo-shejishi"]
print("2009 claims", len(old))
keys = ["瓷", "白瓷", "青瓷", "黑瓷", "釉", "缬", "胡床", "胡服", "气韵", "刘昼", "刘子",
        "云岗", "云冈", "龙门", "敦煌", "犍陀罗", "佛像", "漆", "锦", "铜镜", "独轮",
        "提花", "马钧", "莲花尊", "鸡头壶", "琉璃瓦", "嵩岳", "砖塔", "石窟", "佛教",
        "谢赫", "魏晋", "南北朝", "服饰", "纺织", "印染", "造像", "石雕", "金属", "冶铜"]
seen = set()
for r in old:
    s = r["statement_zh"]
    hit = [k for k in keys if k in s]
    if hit:
        sp = r["source"]["source_span"]
        print(r["claim_id"], sp["line_start"], sp["line_end"], hit)
        print("   ", s[:160])
        seen.add(r["claim_id"])
print("hits", len(seen))
