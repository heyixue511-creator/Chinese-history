# -*- coding: utf-8 -*-
"""Tighten two CL2i statements to the source wording, then refresh artifacts."""
import hashlib
import json
import os
from pathlib import Path

import yaml

ROOT = Path(r"D:/中国设计史研究")
REG = ROOT / "04-knowledge/quality/claim-registry.yml"
PKG = ROOT / "06-runtime/automation/2026-10-27-2009xiayanjing-claims-batch-cl2i"
DATE = "2026-10-27"


def sha256_text(text: str) -> str:
    data = text.replace("\r\n", "\n").encode("utf-8")
    return "sha256:" + hashlib.sha256(data).hexdigest()


def write_atomic(path: Path, text: str) -> None:
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(text, encoding="utf-8", newline="\n")
    os.replace(tmp, path)


rows = json.loads((ROOT / "_zn_claim_xyj09i_rows.json").read_text(encoding="utf-8"))
by_id = {r["claim_id"]: r for r in rows}

by_id["claim-0241"]["statement_zh"] = (
    "夏燕靖认为，中山装是在西装基本款形基础上糅合中国传统文化意识形成的，"
    "整体廓形垫肩收腰、均衡对称，穿着稳重大方；其四个口袋、前襟五粒钮扣与袖口三粒扣，"
    "据说分别取意于礼义廉耻、五权分立与三民主义。"
)
by_id["claim-0241"]["statement_en"] = (
    "Xia Yanjing argues that the Zhongshan suit was formed by blending Chinese cultural "
    "meanings into a basic Western-suit cut, with padded shoulders, a fitted waist, symmetry "
    "and a dignified look; its four pockets, five front buttons and three cuff buttons were "
    "reportedly intended to signify the four virtues, the five-power system and the Three "
    "Principles of the People."
)
by_id["claim-0241"]["discussion_notes"] = (
    "候选作 interpretation，路由 interpretive；断言取 L3958。同段先述早期背面有缝、九粒钮扣与胖裥，"
    "再述定型款，本条取定型款及其寓意；来源以“据说”引出《易经》与周代礼仪依据，"
    "断言以“据说”保留传闻性质，不写成已证制度事实。terms/zhongshanzhuang.md 并列 2009 与赵农两说，"
    "terms/xifu.md 只承载西装基本款形背景。"
)

by_id["claim-0245"]["statement_zh"] = (
    "夏燕靖认为，中国固有式建筑并不是纯传统的宫室式，而是受西方建筑思潮强烈影响、"
    "近于折衷主义的新形式；由于依赖不熟悉中国建筑的外国建筑师和受西方建筑思想影响的留学生，"
    "纯粹的“中国式”难以实现，许多建筑留下模仿或拼凑的痕迹，"
    "南京金陵大学北大楼、北京辅仁大学教学楼是典型样式。"
)
by_id["claim-0245"]["statement_en"] = (
    "Xia Yanjing argues that Chinese inherent-style architecture was not purely traditional "
    "palace architecture but a new, quasi-eclectic form strongly shaped by Western architectural "
    "currents; because the work relied on foreign architects unfamiliar with Chinese architecture "
    "and on returned students shaped by Western architectural thought, a pure Chinese style was "
    "difficult to realize, and many buildings bore traces of imitation or patchwork, with Nanjing "
    "University's North Building and Beijing Fu Jen University's teaching building as typical examples."
)
by_id["claim-0245"]["discussion_notes"] = (
    "候选作 interpretation，路由 interpretive；断言取 L4108。L4106 的中国固有式定义、"
    "《上海市市中心区域规划》规定与五四背景，由 terms/zhongguo-guyou-shi-jianzhu.md、"
    "publications/shanghai-center-plan.md 承载；L4108 末句举金陵大学北大楼、辅仁大学教学楼。"
    "“由于依赖……难以实现”按原文“要依靠……事实上是不可能实现的”改写，保留条件关系，"
    "不写成单一决定论。来源未给两校建筑的年代、建筑师与图纸，实例只作类型例证，不另建 works 条。"
)

(ROOT / "_zn_claim_xyj09i_rows.json").write_text(
    json.dumps(rows, ensure_ascii=False, indent=1), encoding="utf-8")

registry_rows = yaml.safe_load(REG.read_text(encoding="utf-8"))
assert len(registry_rows) == 246
index = {r["claim_id"]: i for i, r in enumerate(registry_rows)}
for cid in ("claim-0241", "claim-0245"):
    i = index[cid]
    registry_rows[i]["statement_zh"] = by_id[cid]["statement_zh"]
    registry_rows[i]["statement_en"] = by_id[cid]["statement_en"]
    registry_rows[i]["discussion_notes"] = by_id[cid]["discussion_notes"]
    registry_rows[i]["updated"] = DATE

header = "# Claim Registry v1.0\n# generated: 2026-10-27\n# total: 246\n"
text = header + yaml.safe_dump(
    registry_rows, allow_unicode=True, sort_keys=False,
    default_flow_style=False, width=100000,
)
assert text.count("\n- claim_id:") == 246
write_atomic(REG, text)

(PKG / "claim-rows.jsonl").write_text(
    "".join(json.dumps(r, ensure_ascii=False, sort_keys=True) + "\n" for r in rows),
    encoding="utf-8", newline="\n",
)

apply_rows = []
for row in rows:
    canonical = json.dumps(row, ensure_ascii=False, sort_keys=True)
    apply_rows.append({
        "action": "claim_create",
        "claim_id": row["claim_id"],
        "candidate_ids": [row["source"]["candidate_id"]],
        "target_ref": f"claim/{row['claim_id']}",
        "after_sha256": sha256_text(canonical),
        "bytes": len(canonical.encode("utf-8")),
        "before": None,
        "note": "新建 claim-registry 行；来源 " + row["source"]["source_file"],
    })
(PKG / "apply-plan.jsonl").write_text(
    "".join(json.dumps(r, ensure_ascii=False, sort_keys=True) + "\n" for r in apply_rows),
    encoding="utf-8", newline="\n",
)

manifest = json.loads((PKG / "manifest.json").read_text(encoding="utf-8"))
manifest["after_sha256"] = sha256_text(text)
manifest["after_bytes"] = len(text.encode("utf-8"))
manifest["claim_rows"] = len(rows)
(PKG / "manifest.json").write_text(
    json.dumps(manifest, ensure_ascii=False, indent=1, sort_keys=True) + "\n",
    encoding="utf-8", newline="\n",
)

print(json.dumps({
    "after_sha256": manifest["after_sha256"],
    "after_bytes": manifest["after_bytes"],
    "patched": ["claim-0241", "claim-0245"],
}, ensure_ascii=False))
