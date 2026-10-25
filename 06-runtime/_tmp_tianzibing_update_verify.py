# -*- coding: utf-8 -*-
"""Verify the eight updated event KUs in the Tianzibing 2010 batch."""
import hashlib
import json
import re
from pathlib import Path

import yaml

BASE = Path("04-knowledge/units/events")
BEFORE = json.loads(Path("06-runtime/_tmp_tianzibing_before.json").read_text(encoding="utf-8"))
SECTIONS = ["## 描述", "## 核心内容", "## 在层级体系中的位置", "## 相关知识元", "## 验证状态", "## 参考文献"]

errors = []
rows = []
for slug, info in sorted(BEFORE.items()):
    path = BASE / f"{slug}.md"
    raw = path.read_bytes()
    text = raw.decode("utf-8")
    fm = yaml.safe_load(text.split("---\n", 2)[1])
    body = text.split("---\n", 2)[2]
    n_src = len(fm["sources"])
    if fm["source_count"] != n_src:
        errors.append(f"{slug}: source_count {fm['source_count']} != sources {n_src}")
    refs = re.findall(r"^\d+\. ", body, re.M)
    ref_sec = body.split("## 参考文献", 1)[1]
    n_ref = re.findall(r"^\d+\. ", ref_sec, re.M)
    if len(n_ref) != n_src:
        errors.append(f"{slug}: references {len(n_ref)} != sources {n_src}")
    for sec in SECTIONS:
        if sec not in text:
            errors.append(f"{slug}: missing {sec}")
    if re.search(r"(夏燕靖 2016|赵农 2009) 有直接记载", text) and n_src > 1:
        errors.append(f"{slug}: stale single-source source_basis")
    doc_ids = [s["evidence_ref"]["doc_id"] for s in fm["sources"]]
    if "2010-tianzibing-zhongguo-gongyi-meishushi" not in doc_ids:
        errors.append(f"{slug}: missing tianzibing source")
    if str(fm["updated"]) != "2026-10-25":
        errors.append(f"{slug}: updated {fm['updated']}")
    if "田自秉" not in body.split("## 参考文献")[0]:
        errors.append(f"{slug}: body does not mention 田自秉")
    norm = text.replace("\r\n", "\n")
    after = hashlib.sha256(norm.encode("utf-8")).hexdigest()
    rows.append({
        "slug": slug,
        "before": info,
        "after_sha256": "sha256:" + after,
        "bytes": len(norm.encode("utf-8")),
        "lines": norm.count("\n"),
        "sources": n_src,
        "refs": len(n_ref),
    })

print("errors", len(errors))
for e in errors:
    print(" -", e)
print(json.dumps(rows, ensure_ascii=False, indent=1))
Path("06-runtime/_tmp_tianzibing_after.json").write_text(
    json.dumps(rows, ensure_ascii=False, indent=1), encoding="utf-8"
)
