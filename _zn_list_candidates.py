# -*- coding: utf-8 -*-
import json
import sys
from pathlib import Path

ROOT = Path(r"D:/中国设计史研究")
DOC = "2009-xiayanjing-zhongguo-shejishi"
CHAPTER = sys.argv[1] if len(sys.argv) > 1 else "隋唐五代时期的艺术设计"
OUT = sys.argv[2] if len(sys.argv) > 2 else "_zn_cl2e_texts.txt"
rows = [json.loads(l) for l in (ROOT / "06-runtime/state/candidate-index.jsonl").read_text(encoding="utf-8").splitlines() if l.strip()]
sel = [r for r in rows if r["candidate_id"].startswith(DOC + ":")
       and r["candidate_type"] == "claim" and r["state"] == "needs_evidence"
       and ((r.get("payload") or {}).get("source_span") or {}).get("chapter") == CHAPTER]
sel.sort(key=lambda r: ((r["payload"]["source_span"]["line_start"]), r["candidate_id"]))
out = []
for r in sel:
    sp = r["payload"]["source_span"]
    blocks = " ".join(f"{b}:{sp.get('line_start')}-{sp.get('line_end')}" for b in sp.get("block_ids", []))
    out.append("## " + r["candidate_id"].split(":", 1)[1]
               + f"  L{sp['line_start']}-{sp['line_end']}  {r['payload'].get('candidate_kind') or r['payload'].get('kind') or ''}".rstrip())
    out.append("claim_text: " + (r["payload"].get("claim_text") or ""))
    out.append("blocks: " + blocks)
    out.append("")
(ROOT / OUT).write_text("\n".join(out), encoding="utf-8")
print("count", len(sel))
for line in out:
    print(line)
