# -*- coding: utf-8 -*-
"""Emit ledger, apply-plan, canonical mapping and manifest for Zhaonong 2009 procedure batch D."""
import hashlib
import json
from pathlib import Path

import yaml

ROOT = Path(".")
BATCH = Path("06-runtime/automation/2026-10-25-2009zhaonong-procedures-batch-d")
BATCH.mkdir(parents=True, exist_ok=True)
PREFIX = "2009-zhaonong-zhongguo-yishu-shejishi:"
DATE = "2026-10-25"

CREATES = [
    ("cand-10-102", "gong-hua", "拱花", "printing_technique", "明代（明末）", "以刻版压印使花纹凸显，犹如钢印；吴发祥、胡正言用于笺谱"),
    ("cand-10-116", "ci-huazi", "瓷活字", "printing_technique", "清代中期", "徐志定在泥活字上挂釉烧成瓷活字，为最早瓷活字样式，印有《周易说略》"),
    ("cand-10-120", "shiyin-ben", "石印本", "printing_technique", "晚清", "石材制版、胶性药墨过写药纸、覆石揭纸，依油水分离印成书籍，提高图版质量"),
    ("cand-10-122", "xian-zhuang", "线装", "bookbinding_technique", "明代中期", "封面封底裁齐，书页三边裁齐，丝线四孔装订，上下角厚纸包角，封面贴书目标签"),
    ("cand-10-140", "ming-changcheng-qiangti-gouzhu", "明长城墙体构筑", "construction_technique", "明代", "山海关至山西段墙体外包巨砖石条，内以黄土、石灰、江米质黏合，设垛口与烽火台"),
    ("cand-11-068", "huo-pao-zhuzao", "火炮铸造", "metalworking_technique", "明代至清代", "锻造以熟铁瓦片钉连锉磨；铸造经铸型、合模、浇注、验膛、镟膛、钻火门等十一项工序"),
    ("cand-12-30", "xiandai-zaozhi-jishu", "现代造纸技术", "papermaking_technique", "近代至 1949 年后", "以木材为原料，硫酸盐法和中性亚硫酸盐法连续蒸煮制浆并高速造纸"),
    ("cand-12-32", "qianzi-yinshua", "铅字印刷", "printing_technique", "19 世纪末传入", "凸版形式，活铅字排版组合，轮转机印刷；1980 年前报刊广泛采用"),
    ("cand-12-33", "zhaoxiang-zhiban", "照相制版", "printing_technique", "现代", "采用胶片感光原理，将细致图像制作成版式印刷，弥补铅字印刷简单缺陷"),
    ("cand-12-34", "siwang-yinshua", "丝网印刷", "printing_technique", "现代", "利用照相感光方法在丝网上制成漏版，进行细致印刷"),
    ("cand-12-35", "tongban-yinshua", "铜版印刷", "printing_technique", "现代", "蜡涂铜版、刻刀刻画、酸腐蚀加深线条、去蜡后油墨印刷"),
    ("cand-12-36", "dianzi-zhaopai", "电子照排", "printing_technique", "20 世纪末", "随计算机桌面印刷系统普及出现，解决设计印刷难题，推动版面设计发展"),
]

UPDATES = [
    ("cand-09-67", "huozi-yinshua", "活字印刷", "printing_technique", "北宋庆历年间；元代王祯木活字",
     "补入赵农 2009 王祯活木字：枣梨木版锯成单字、转轮检字、三万活字印《旌德县志》",
     "sha256:e552711a7cf5e9deb5222e42a446af2c9ba0e46adc7ec4b342a856e9b3af1a54", 6641, 94),
    ("cand-10-101", "duanban-taoyin", "短版套印", "printing_technique", "明代创造；清代盛行",
     "补入赵农 2009 明末短版技术：分小块套印、短钉定义、朱墨黛紫黄、笺谱与徽派刻工",
     "sha256:030828f4051683525e03ee9ea52556d733b9782b8fee1fcd6a0c93f3f8f70c6c", 3844, 81),
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


def ledger_rows(cid, target, kind):
    rows = []
    for expected, state, reason in [
        ("needs_evidence", "ready_for_review", f"已完成语义复读：{kind} {target}"),
        ("ready_for_review", "approved", f"canonical 候选语义复读完成，批准按 exact change-set {kind} {target}"),
        ("approved", "applied", f"已按 exact change-set {kind} {target}"),
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
        rows.append(row)
    return rows


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
    ledger.extend(ledger_rows(cid, target, "新建"))
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

for cand, slug, title, sub, date, result, before_sha, before_bytes, before_lines in UPDATES:
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
    ledger.extend(ledger_rows(cid, target, "更新"))
    plan.append({
        "action": "update",
        "target_ref": target,
        "candidate_id": cid,
        "entity": title,
        "before": {
            "sha256": before_sha,
            "bytes": before_bytes,
            "lines": before_lines,
        },
        "after_sha256": fp["sha256"],
        "bytes": fp["bytes"],
        "lines": fp["lines"],
        "note": f"更新{sub}：{date}；{result}",
    })
    mapping.append({
        "entity": title,
        "target_ref": target,
        "action": "update",
        "canonical_candidate": cid,
        "merged_candidates": [],
    })

assert len(ledger) == 42, len(ledger)
assert len(plan) == 14, len(plan)
assert len(mapping) == 14, len(mapping)

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
    "work_package": "2026-10-25-2009zhaonong-procedures-batch-d",
    "goal": "处理赵农《中国艺术设计史》2009 册第 26—39 个 procedure 候选：12 个新建、2 个更新；无 no_delta、无 rejected。",
    "status": "applied",
    "date": DATE,
    "inputs": {
        "candidate_index": {
            "path": "06-runtime\\state\\candidate-index.jsonl",
            "rows_before": 5339,
            "sha256_before": "sha256:ac232887c84e6dab62629948268cdcb9ef51f803792719dfc9a7a86521526277",
            "sha256_scope": "CRLF→LF 归一后",
            "counts_before": {
                "applied": 707,
                "needs_evidence": 3788,
                "no_delta": 43,
                "rejected": 801,
            },
        },
        "source": {
            "doc_id": "2009-zhaonong-zhongguo-yishu-shejishi",
            "file": "03基础书籍-md文档/中国艺术设计史_赵农_2009_高等教育出版社.md",
            "spans": ["L6819", "L7195", "L7202", "L7242", "L7255-L7257", "L7263", "L6539-L6541", "L7553-L7564", "L8139-L8149", "L8153-L8160", "L8162", "L8164"],
        },
    },
    "method": {
        "rules": [
            "procedure 候选按实体而非 slug 对账：先与既有 procedure KU 的标题与内容对齐，再定 create／update。",
            "工序条目只写来源所记材料、步骤、工具、产量与实例；来源未载的工序参数写入证据边界。",
            "来源的判断与推测照录并标明主语；原文异体与疑似讹字照录并注明。",
            "同一技术家族中材料或工序不同的实例分列，互指而不合并。",
        ],
        "source_policy": "02-sources 只读；本批写 04-knowledge/units/procedures，12 条新建、2 条更新。",
    },
    "outputs": {
        "apply_plan": {
            "path": "06-runtime\\automation\\2026-10-25-2009zhaonong-procedures-batch-d\\apply-plan.jsonl",
            "rows": 14,
            "create": 12,
            "update": 2,
        },
        "ledger": {
            "path": "06-runtime\\automation\\2026-10-25-2009zhaonong-procedures-batch-d\\candidate-decision-ledger.jsonl",
            "rows": 42,
            "candidates": 14,
            "applied": 14,
            "no_delta": 0,
            "rejected": 0,
        },
        "canonical_mapping": {
            "path": "06-runtime\\automation\\2026-10-25-2009zhaonong-procedures-batch-d\\canonical-mapping.json",
            "entries": 14,
        },
    },
    "verification": {"status": "pending"},
}

(BATCH / "manifest.json").write_bytes(
    (json.dumps(manifest, ensure_ascii=False, indent=2) + "\n").encode("utf-8")
)
print("ledger", len(ledger), "plan", len(plan), "mapping", len(mapping))
