# -*- coding: utf-8 -*-
"""Show 2009 claims 0255-0257 for patch planning."""
import json
from pathlib import Path

import yaml

ROOT = Path(r"D:/中国设计史研究")
REG = ROOT / "04-knowledge/quality/claim-registry.yml"
rows = yaml.safe_load(REG.read_text(encoding="utf-8"))
for r in rows:
    if r["claim_id"] in {"claim-0255", "claim-0256", "claim-0257"}:
        print(json.dumps(r, ensure_ascii=False, indent=1))
        print("=" * 60)
print("total", len(rows))
