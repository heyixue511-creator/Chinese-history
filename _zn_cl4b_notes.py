# -*- coding: utf-8 -*-
import json
from pathlib import Path

ROOT = Path(r"D:/中国设计史研究")
ROWS = json.loads((ROOT / "_zn_cl4b_rows.json").read_text(encoding="utf-8"))
for r in ROWS:
    print(r["claim_id"], r["claim_type"], r["confidence"])
    print("  ", r["discussion_notes"])
