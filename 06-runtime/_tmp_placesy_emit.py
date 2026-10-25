import hashlib
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
PKG = ROOT / "06-runtime" / "automation" / "2026-10-25-xiayanjing2009-places-batch-y"
PKG.mkdir(parents=True, exist_ok=True)
DOC = "2009-xiayanjing-zhongguo-shejishi"
DATE = "2026-10-25"


def fp(path: pathlib.Path) -> dict:
    text = path.read_bytes().decode("utf-8").replace("\r\n", "\n").replace("\r", "\n")
    data = text.encode("utf-8")
    return {
        "sha256": "sha256:" + hashlib.sha256(data).hexdigest(),
        "bytes": len(data),
        "lines": text.count("\n"),
    }


creates = [
    {
        "candidate_id": f"{DOC}:cand-01-90",
        "entity": "三星堆遗址",
        "target_ref": "04-knowledge/units/places/sanxingdui.md",
        "note": "更新既有sanxingdui：既有条目已引夏燕靖 2016 L971-L990、赵农 2009；补夏燕靖 2009 L748-L766 的服饰材质与织造细节——商代衣服材料以皮、革、丝、麻为主，已能织造极薄的绸和提花几何纹的锦、绮，奴隶主与贵族以穿着此种材质为荣；2009 与 2016 为同一作者前后版，正文基本对应，source_count 2→3、version 1→2",
    },
    {
        "candidate_id": f"{DOC}:cand-02-19",
        "entity": "郑韩故城制陶作坊遗址",
        "target_ref": "04-knowledge/units/places/zhenghan-gucheng-taofang-yizhi.md",
        "note": "新建archaeological_site：夏燕靖 2009 L883-L888 记郑韩故城新郑发掘的东周大型制陶作坊遗址，区域内有窑址群、作坊建筑群、陶制排水管道、陶洗池，出土大型存储类陶器与带印证筒板瓦；单源、单段，未给发掘年份、面积、窑数、布局、产品谱系与存续时间，confidence 定为 low；同页明器定义与陶瓷纹样图版不并入",
    },
    {
        "candidate_id": f"{DOC}:cand-06-07",
        "entity": "三山五园",
        "target_ref": "04-knowledge/units/places/sanshan-wuyuan.md",
        "note": "新建garden：夏燕靖 2009 L3688-L3698 记清代康熙、乾隆年间皇家园林建设高潮中在北京筑“三山五园”，即万寿山清漪园（后改颐和园）、玉泉山静明园、香山静宜园、圆明园（含圆明、长春、万春三园）；单源，未给各园始建／毁废年份、占地、设计者与工程组织，confidence 定为 medium；私家园林与《园冶》不并入",
    },
]

updates = {
    "04-knowledge/units/places/sanxingdui.md": {
        "sha256": "sha256:62a90e02af0f2187da65f5cfc5e7e79eed04e4aba126db2e2cf49b77c0333c9f",
        "bytes": 3646,
        "lines": 83,
    },
}

ledger = []
for c in creates:
    cid, target = c["candidate_id"], c["target_ref"]
    action_word = "更新" if target in updates else "新建"
    ledger.append({
        "candidate_id": cid,
        "expected_state": "needs_evidence",
        "state": "ready_for_review",
        "decision": {"status": "pending", "reason": f"已完成语义复读：{action_word} {target}", "decided_by": "Agent", "decided_at": DATE},
        "updated_at": DATE,
    })
    ledger.append({
        "candidate_id": cid,
        "expected_state": "ready_for_review",
        "state": "approved",
        "decision": {"status": "approved", "reason": f"canonical 候选语义复读完成，批准{action_word} {target}", "decided_by": "Agent", "decided_at": DATE},
        "updated_at": DATE,
    })
    ledger.append({
        "candidate_id": cid,
        "expected_state": "approved",
        "state": "applied",
        "decision": {"status": "approved", "reason": f"已判定 applied：{action_word} {target}", "decided_by": "Agent", "decided_at": DATE},
        "updated_at": DATE,
        "target_ref": target,
    })

plan = []
for c in creates:
    target = c["target_ref"]
    f = fp(ROOT / target)
    plan.append({
        "action": "update" if target in updates else "create",
        "target_ref": target,
        "candidate_id": c["candidate_id"],
        "entity": c["entity"],
        "before": updates.get(target),
        "after_sha256": f["sha256"],
        "bytes": f["bytes"],
        "lines": f["lines"],
        "note": c["note"],
    })

mapping = [
    {
        "entity": c["entity"],
        "target_ref": c["target_ref"],
        "action": "update" if c["target_ref"] in updates else "create",
        "canonical_candidate": c["candidate_id"],
        "merged_candidates": [],
    }
    for c in creates
]

assert len(ledger) == 9
assert len(plan) == 3
assert len(mapping) == 3
assert sum(1 for r in plan if r["action"] == "create") == 2
assert sum(1 for r in plan if r["action"] == "update") == 1

(PKG / "candidate-decision-ledger.jsonl").write_text(
    "\n".join(json.dumps(r, ensure_ascii=False) for r in ledger) + "\n", encoding="utf-8"
)
(PKG / "apply-plan.jsonl").write_text(
    "\n".join(json.dumps(r, ensure_ascii=False) for r in plan) + "\n", encoding="utf-8"
)
(PKG / "canonical-mapping.json").write_text(
    json.dumps(mapping, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
)

manifest = {
    "work_package": "2026-10-25-xiayanjing2009-places-batch-y",
    "goal": "处理夏燕靖《中国设计史》2009 册 place 候选 3 个：2 个新建、1 个更新、0 个 no_delta、0 个 rejected。",
    "status": "applied",
    "date": DATE,
    "inputs": {
        "candidate_index": {
            "path": "06-runtime\\state\\candidate-index.jsonl",
            "rows_before": 5339,
            "sha256_before": "sha256:0fb76ef90783b643feeb2a8543cba07fc4617ab1bddf6986ca3d3d70319964c4",
            "sha256_scope": "CRLF→LF 归一后",
            "counts_before": {"applied": 930, "needs_evidence": 3540, "no_delta": 57, "rejected": 812},
        },
        "source": {
            "doc_id": DOC,
            "file": "03基础书籍-md文档/中国设计史_夏燕靖_2009_上海人民美术出版社.md",
            "spans": ["L748-L766", "L883-L888", "L3688-L3698"],
        },
    },
    "method": {
        "rules": [
            "place 候选按地名实体与既有 39 个 place KU 对账，再定 create／update／no_delta／rejected。",
            "候选“三星堆遗址”判 update 既有 `places/sanxingdui.md`：既有条目已引夏燕靖 2016 L971-L990 与赵农 2009，但正文只概括“衣料、式样、配饰的差异”，未收 2009 L748-L766 的材质与织造细节；补“皮、革、丝、麻”“极薄的绸和提花几何纹的锦、绮”“奴隶主和贵族以穿着此种材质为荣”，source_count 2→3、version 1→2。2009 与 2016 为同一作者前后版，正文基本对应；更新不把两版重复计为独立互证。",
            "候选“郑韩故城制陶作坊遗址”判 create：夏燕靖 2009 L883-L888 记郑韩故城新郑的东周大型制陶作坊遗址，遗迹有窑址群、作坊建筑群、陶制排水管道、陶洗池，出土大型存储类陶器与带印证筒板瓦；来源只有一段，未给发掘年份、面积、窑数、布局、产品谱系、工匠组织与存续时间，confidence 定为 low；同页“明器”定义与陶瓷器皿纹样图版不归本遗址。",
            "候选“三山五园”判 create：夏燕靖 2009 L3688-L3698 记清代康熙、乾隆年间皇家园林建设高潮中在北京筑“三山五园”，即万寿山清漪园（后改颐和园）、玉泉山静明园、香山静宜园、圆明园（含圆明、长春、万春三园）；来源只给群名与园名，未给各园始建／毁废年份、占地、设计者、工程组织与存续细节，confidence 定为 medium；同段私家园林与《园冶》不并入。",
            "place 的文件名使用无声调小写汉语拼音 kebab-case；三星堆走既有条目 update，不新建 `sanxingdui-yizhi.md`，避免同实体重复。",
            "03基础书籍-md文档只读；本批写 04-knowledge/units/places；不 commit、不 push。",
        ]
    },
    "outputs": {
        "apply_plan": {"path": "06-runtime\\automation\\2026-10-25-xiayanjing2009-places-batch-y\\apply-plan.jsonl", "rows": 3, "create": 2, "update": 1},
        "ledger": {"path": "06-runtime\\automation\\2026-10-25-xiayanjing2009-places-batch-y\\candidate-decision-ledger.jsonl", "rows": 9, "candidates": 3, "applied": 3, "no_delta": 0, "rejected": 0},
        "canonical_mapping": {"path": "06-runtime\\automation\\2026-10-25-xiayanjing2009-places-batch-y\\canonical-mapping.json", "entries": 3, "merged_candidates": []},
    },
    "state_after": {"applied": 933, "needs_evidence": 3537, "no_delta": 57, "rejected": 812, "total": 5339},
}

(PKG / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"ledger": len(ledger), "plan": len(plan), "mapping": len(mapping), "pkg": str(PKG)}, ensure_ascii=False, indent=2))
