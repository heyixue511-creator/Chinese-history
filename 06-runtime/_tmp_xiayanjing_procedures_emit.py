# -*- coding: utf-8 -*-
"""Emit ledger, apply-plan, canonical mapping and manifest for Xiayanjing 2009 procedure batch 1."""
import hashlib
import json
from pathlib import Path

import yaml

ROOT = Path(".")
BATCH = Path("06-runtime/automation/2026-10-25-2009xiayanjing-procedures-batch-1")
BATCH.mkdir(parents=True, exist_ok=True)
PREFIX = "2009-xiayanjing-zhongguo-shejishi:"
DATE = "2026-10-25"
DOC = "2009-xiayanjing-zhongguo-shejishi"

CREATES = [
    ("cand-01-16", "mozhi-shiqi", "磨制石器", "stoneworking_technique", "约 10000 多年前", "打制粗坯后研磨，使器形规整、刃口锋利、表面光洁；促进新石器革命"),
    ("cand-01-27", "lunzhi-fa", "轮制法", "ceramic_technique", "仰韶文化中期起", "泥料置陶轮快速转动、提拉成形；器形规整、厚薄均匀，器表有平行密集轮纹"),
    ("cand-01-60", "hefan-fa", "合范法", "metalworking_technique", "商周", "泥模雕纹→外范分块做三角榫→内范刮模或另制→子母扣合范→浇铸脱范打磨"),
    ("cand-02-03", "ye-tie-shu-qi-yuan", "冶铁术在中国的出现", "metalworking_technique", "商代—春秋战国", "商代铁刃铜器与西周晚期人工冶铁；春秋后期掌握冶铁并普遍使用铁器"),
    ("cand-02-04", "sheng-tie-ye-zhu-ji-shu", "生铁冶铸技术", "metalworking_technique", "春秋中期", "块炼铁到生铁铸造；公元前 513 年铸刑鼎；六合程桥白口铸铁铁丸；排橐鼓风"),
    ("cand-02-06", "sheng-tie-rou-hua-ji-shu", "生铁柔化技术", "metalworking_technique", "战国早期", "洛阳铁锛铁镈、铜绿山六角锄、易县铁鐏；白心与黑心可锻铸铁"),
    ("cand-02-15", "yin-wen-mo-yin", "印纹（模印）装饰", "metalworking_technique", "春秋战国", "印花模子趁模胎未冷盖印，一模多用；纹样由单独纹样到二方、四方连续"),
    ("cand-02-17", "cuo-jin-yin-cuo-tong", "错金银与错铜", "metalworking_technique", "春秋中期", "栾书缶错金铭文 40 余字；燕、赵、蔡等国以红铜镶嵌图案"),
]


def fingerprint(path: Path):
    data = path.read_bytes()
    text = data.decode("utf-8").replace("\r\n", "\n")
    payload = text.encode("utf-8")
    return {
        "sha256": "sha256:" + hashlib.sha256(payload).hexdigest(),
        "bytes": len(payload),
        "lines": text.count("\n"),
    }


ledger = []
plan = []
mapping = []

for cand, slug, title, sub, date, result in CREATES:
    cid = PREFIX + cand
    target = f"04-knowledge/units/procedures/{slug}.md"
    path = ROOT / target
    if not path.exists():
        raise SystemExit(f"missing {target}")
    fm = yaml.safe_load(path.read_text(encoding="utf-8").split("---\n", 2)[1])
    if title not in fm.get("title", ""):
        raise SystemExit(f"title mismatch {target}: {fm.get('title')}")
    if fm.get("sub_type") != sub:
        raise SystemExit(f"sub_type mismatch {target}: {fm.get('sub_type')}")
    fp = fingerprint(path)
    for expected, state, reason in [
        ("needs_evidence", "ready_for_review", f"已完成语义复读：既有 KU 无对应实体，提交 create {target}"),
        ("ready_for_review", "approved", f"canonical 候选语义复读完成，批准按 exact change-set 新建 {target}"),
        ("approved", "applied", f"已按 exact change-set 新建 {target}"),
    ]:
        row = {
            "candidate_id": cid,
            "expected_state": expected,
            "state": state,
            "decision": {
                "status": "pending" if state == "ready_for_review" else "approved",
                "reason": reason,
                "decided_by": "Agent",
                "decided_at": DATE,
            },
            "updated_at": DATE,
        }
        if state == "applied":
            row["target_ref"] = target
        ledger.append(row)
    plan.append({
        "action": "create",
        "target_ref": target,
        "candidate_id": cid,
        "entity": title,
        "before": None,
        "after_sha256": fp["sha256"],
        "bytes": fp["bytes"],
        "lines": fp["lines"],
        "note": f"新建{sub}：{date}；{result}",
    })
    mapping.append({
        "entity": title,
        "target_ref": target,
        "action": "create",
        "canonical_candidate": cid,
        "merged_candidates": [],
    })

assert len(ledger) == 24, len(ledger)
assert len(plan) == 8, len(plan)
assert len(mapping) == 8, len(mapping)

(BATCH / "candidate-decision-ledger.jsonl").write_bytes(
    ("\n".join(json.dumps(r, ensure_ascii=False) for r in ledger) + "\n").encode("utf-8")
)
(BATCH / "apply-plan.jsonl").write_bytes(
    ("\n".join(json.dumps(r, ensure_ascii=False) for r in plan) + "\n").encode("utf-8")
)
(BATCH / "canonical-mapping.json").write_bytes(
    (json.dumps(mapping, ensure_ascii=False, indent=2) + "\n").encode("utf-8")
)

manifest = {
    "work_package": "2026-10-25-2009xiayanjing-procedures-batch-1",
    "goal": "处理夏燕靖《中国设计史》2009 册的 8 个早期工艺 procedure 候选：全部新建，无 no_delta、无 rejected。",
    "status": "applied",
    "date": DATE,
    "inputs": {
        "candidate_index": {
            "path": "06-runtime\\state\\candidate-index.jsonl",
            "rows_before": 5339,
            "sha256_before": "sha256:d7c810b762cf18d89acaa6a3c672ca8c68981447cab53063fac8663dfc89213f",
            "sha256_scope": "CRLF→LF 归一后",
            "counts_before": {
                "applied": 667,
                "needs_evidence": 3828,
                "no_delta": 43,
                "rejected": 801,
            },
        },
        "source": {
            "doc_id": DOC,
            "file": "03基础书籍-md文档/中国设计史_夏燕靖_2009_上海人民美术出版社.md",
            "spans": ["L278-L297", "L322-L327", "L499-L510", "L812-L824", "L825-L838", "L839-L844", "L872-L882", "L872-L882"],
        },
    },
    "method": {
        "rules": [
            "procedure 候选按实体而非 slug 对账：先与既有 procedure KU 的标题与内容对齐，再定 create／update。",
            "工序条目只写来源所记材料、步骤、工具、产量与实例；来源未载的工序参数写入证据边界。",
            "来源的判断与推测照录并标明主语，不提升为定论；原文截断处照录并注明。",
            "同一来源行段并记两种工艺的，分建两条并在相关知识元互指，不合并为一条。",
        ],
        "source_policy": "02-sources 只读；本批写 04-knowledge/units/procedures。",
    },
    "outputs": {
        "apply_plan": {
            "path": "06-runtime\\automation\\2026-10-25-2009xiayanjing-procedures-batch-1\\apply-plan.jsonl",
            "rows": 8,
            "create": 8,
            "update": 0,
        },
        "ledger": {
            "path": "06-runtime\\automation\\2026-10-25-2009xiayanjing-procedures-batch-1\\candidate-decision-ledger.jsonl",
            "rows": 24,
            "candidates": 8,
            "applied": 8,
            "no_delta": 0,
            "rejected": 0,
        },
        "canonical_mapping": {
            "path": "06-runtime\\automation\\2026-10-25-2009xiayanjing-procedures-batch-1\\canonical-mapping.json",
            "entries": 8,
        },
    },
    "verification": {"status": "pending"},
}

(BATCH / "manifest.json").write_bytes(
    (json.dumps(manifest, ensure_ascii=False, indent=2) + "\n").encode("utf-8")
)
print("ledger", len(ledger), "plan", len(plan), "mapping", len(mapping))
