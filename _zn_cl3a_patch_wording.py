# -*- coding: utf-8 -*-
"""Tighten claim-0263 to the source wording and fix a note spacing, then refresh artifacts."""
import hashlib
import json
import os
from pathlib import Path

import yaml

ROOT = Path(r"D:/中国设计史研究")
REG = ROOT / "04-knowledge/quality/claim-registry.yml"
PKG = ROOT / "06-runtime/automation/2026-10-27-2016xiayanjing-claims-batch-cl3a"
DATE = "2026-10-27"


def sha256_text(text: str) -> str:
    data = text.replace("\r\n", "\n").encode("utf-8")
    return "sha256:" + hashlib.sha256(data).hexdigest()


def write_atomic(path: Path, text: str) -> None:
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(text, encoding="utf-8", newline="\n")
    os.replace(tmp, path)


rows = json.loads((ROOT / "_zn_cl3a_rows.json").read_text(encoding="utf-8"))
by_id = {r["claim_id"]: r for r in rows}

by_id["claim-0263"]["statement_zh"] = (
    "夏燕靖认为，从旧石器中晚期起，黄河流域就成为我国远古文化的发展中心；"
    "他并称从中石器时代起，黄河流域就是我国远古文化的中心区域，"
    "并为黄河流域历代王朝在此建都夯实了基础。"
)
by_id["claim-0263"]["statement_en"] = (
    "Xia Yanjing argues that the Yellow River basin became the developmental center "
    "of China's remote antiquity from the middle and late Paleolithic, and that from "
    "the Mesolithic it was the central region of China's ancient culture, laying the "
    "foundation for successive dynasties in the Yellow River basin to establish their "
    "capitals there."
)
by_id["claim-0272"]["discussion_notes"] = by_id["claim-0272"]["discussion_notes"].replace(
    "01-79 记merged_candidate_ids", "01-79 记 merged_candidate_ids"
)

(ROOT / "_zn_cl3a_rows.json").write_text(
    json.dumps(rows, ensure_ascii=False, indent=1), encoding="utf-8")

registry_rows = yaml.safe_load(REG.read_text(encoding="utf-8"))
assert len(registry_rows) == 272
index = {r["claim_id"]: i for i, r in enumerate(registry_rows)}
for cid in ("claim-0263", "claim-0272"):
    i = index[cid]
    registry_rows[i]["statement_zh"] = by_id[cid]["statement_zh"]
    registry_rows[i]["statement_en"] = by_id[cid]["statement_en"]
    registry_rows[i]["discussion_notes"] = by_id[cid]["discussion_notes"]
    registry_rows[i]["updated"] = DATE

header = "# Claim Registry v1.0\n# generated: 2026-10-27\n# total: 272\n"
text = header + yaml.safe_dump(
    registry_rows, allow_unicode=True, sort_keys=False,
    default_flow_style=False, width=100000,
)
assert text.count("\n- claim_id:") == 272
write_atomic(REG, text)

(PKG / "claim-rows.jsonl").write_text(
    "".join(json.dumps(r, ensure_ascii=False, sort_keys=True) + "\n" for r in rows),
    encoding="utf-8", newline="\n",
)

apply_rows = [json.loads(l) for l in (PKG / "apply-plan.jsonl").read_text(
    encoding="utf-8").splitlines() if l.strip()]
for ar in apply_rows:
    if ar["action"] == "claim_create" and ar["claim_id"] in ("claim-0263", "claim-0272"):
        canonical = json.dumps(by_id[ar["claim_id"]], ensure_ascii=False, sort_keys=True)
        ar["after_sha256"] = sha256_text(canonical)
        ar["bytes"] = len(canonical.encode("utf-8"))
(PKG / "apply-plan.jsonl").write_text(
    "".join(json.dumps(r, ensure_ascii=False, sort_keys=True) + "\n" for r in apply_rows),
    encoding="utf-8", newline="\n",
)

manifest = json.loads((PKG / "manifest.json").read_text(encoding="utf-8"))
manifest["after_sha256"] = sha256_text(text)
manifest["after_bytes"] = len(text.encode("utf-8"))
(PKG / "manifest.json").write_text(
    json.dumps(manifest, ensure_ascii=False, indent=1, sort_keys=True) + "\n",
    encoding="utf-8", newline="\n",
)

print(json.dumps({
    "after_sha256": manifest["after_sha256"],
    "after_bytes": manifest["after_bytes"],
    "patched": ["claim-0263", "claim-0272"],
}, ensure_ascii=False))
