# -*- coding: utf-8 -*-
import json
from pathlib import Path

src = Path("06-runtime/automation/2026-10-25-overlap-candidates-batch/apply-plan.jsonl")
rows = [json.loads(l) for l in src.read_text(encoding="utf-8").splitlines() if l.strip()]
lines = [f"{r['action']}\t{r['target_ref'].replace('04-knowledge/units/', '')}\t{r['note']}" for r in rows]
Path("06-runtime/_tmp_plan_list.txt").write_text("\n".join(lines), encoding="utf-8")
print(len(lines))
