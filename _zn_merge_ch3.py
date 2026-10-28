"""Merge chapter 3 decision fragments into one decisions JSON, ordered by source line."""
import json
import sys
from pathlib import Path

ROOT = Path(r"D:/中国设计史研究")
INDEX = ROOT / "06-runtime/state/candidate-index.jsonl"

fragments = sys.argv[1:-1]
out_path = Path(sys.argv[-1])

merged = {}
for frag in fragments:
    data = json.loads(Path(frag).read_text(encoding="utf-8"))
    if isinstance(data, dict):
        data = data["decisions"]
    for d in data:
        if d["cid"] in merged:
            raise SystemExit("duplicate cid: " + d["cid"])
        merged[d["cid"]] = d

rows = {}
for line in INDEX.read_text(encoding="utf-8").splitlines():
    if not line.strip():
        continue
    row = json.loads(line)
    rows[row["candidate_id"]] = row

missing = [c for c in merged if c not in rows]
if missing:
    raise SystemExit("cid not in index: " + ", ".join(missing))

targets = [d["target"] for d in merged.values()]
dupes = sorted({t for t in targets if targets.count(t) > 1})

ordered = sorted(merged.values(), key=lambda d: int(rows[d["cid"]]["payload"]["source_span"]["line_start"]))
cfg = {
    "doc": "2009-zhaonong-zhongguo-yishu-shejishi",
    "file": "03基础书籍-md文档/中国艺术设计史_赵农_2009_高等教育出版社.md",
    "rules": [
        "第三章 60 条 unit 候选逐条语义复读后分流为 create / update / no_delta；cand-04-* 前缀的条目按 payload.source_span.chapter 归入第三章。",
        "来源新建 consensus=tentative、evidence_status=source_backed、version=1、source_count=1；更新按实际并入来源数提高 source_count，其余字段不动。",
        "原文错字、内部矛盾照录并标注，不径改；只有图注而无正文的条目 confidence 记 low，不据图补形制。",
        "同一实体命中两条候选时，一条落 create/update，另一条走 no_delta 指向同一文件，不重复建 KU。",
    ],
    "decisions": ordered,
}
out_path.write_text(json.dumps(cfg, ensure_ascii=False, indent=1) + "\n", encoding="utf-8", newline="\n")
print(json.dumps({
    "decisions": len(ordered),
    "create": sum(1 for d in ordered if d["action"] == "create"),
    "update": sum(1 for d in ordered if d["action"] == "update"),
    "no_delta": sum(1 for d in ordered if d["action"] == "no_delta"),
    "duplicate_targets": dupes,
}, ensure_ascii=False))
