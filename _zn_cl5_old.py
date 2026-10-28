# -*- coding: utf-8 -*-
"""List 2009-edition claims for cross-edition dedup."""
import yaml
from pathlib import Path

ROOT = Path(r"D:/中国设计史研究")
REG = ROOT / "04-knowledge/quality/claim-registry.yml"
rows = yaml.safe_load(REG.read_text(encoding="utf-8"))
for r in rows:
    if r["source"]["doc_id"] != "2009-xiayanjing-zhongguo-shejishi":
        continue
    sp = r["source"]["source_span"]
    print("|".join([
        r["claim_id"], r["claim_type"],
        f'{sp["line_start"]}-{sp["line_end"]}',
        str(sp.get("chapter", ""))[:20],
        r["statement_zh"][:150],
    ]))
