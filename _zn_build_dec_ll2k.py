# -*- coding: utf-8 -*-
"""Build the LL2k decisions JSON (chapter 4 opening and section 1, L1380-L1429)."""
import json
from pathlib import Path

ROOT = Path(r"D:/中国设计史研究")
DOC = "2011-lilixin-zhongguo-sheji-yishu-shilun"
SRC = "03基础书籍-md文档/中国设计艺术史论_李立新_2011_人民出版社.md"
U = "04-knowledge/units/"


def C(cid, entity, target, analysis, approve, apply_note, note=None):
    return {
        "cid": f"{DOC}:{cid}", "entity": entity, "action": "create", "target": U + target,
        "analysis": analysis, "approve": approve, "apply_note": apply_note,
        "note": note or f"canonical: {U}{target}。{cid} 并入该条。",
    }


def UPD(cid, entity, target, analysis, approve, apply_note, note=None):
    d = C(cid, entity, target, analysis, approve, apply_note, note)
    d["action"] = "update"
    return d


D = [
    C("cand-04-84", "黄地织金五龙蔓草纹重锦靠背",
      "works/huang-di-zhi-jin-wu-long-man-cao-wen-zhong-jin-kao-bei.md",
      "cand-04-84 跨度为 L1405-L1406，即图4-2 的图版行与图注行。L1406 只给器名“黄地织金五龙蔓草纹重锦靠背（清代）”；L1401 在同一节官营手工业论述中把该图作为“精美绝伦、极度豪奢的高档商品”的例证。现有 works 下无该器条目，`terms/zhijin-yin.md` 与 `terms/jinxi-gongyi.md` 记织金、织锦工艺，不承担单件器物。",
      "图注可独立检索，且与官营手工业条、织金与织锦工艺条分工不同，按 work 建条；图版未视觉核验，尺寸、藏地、织造机构与纹样布局均未载，置信度 low。",
      "新建 works/huang-di-zhi-jin-wu-long-man-cao-wen-zhong-jin-kao-bei.md，记图注、官营手工业高档商品语境与未载项。"),
    C("cand-04-28", "家庭手工业",
      "terms/jia-ting-shou-gong-ye.md",
      "cand-04-28 跨度为 L1410-L1412。L1410 给家庭手工业的层次定位、自给自足、家庭作为生产制作单位与交换场所、家庭作坊与农业结合、“男耕女织”持续表现、贯穿全部历程，以及不能从农业分离导致分工与技术难以提高的限制；L1412 给官营与民营造物的技术与特殊技巧几乎都源自家庭承传、“家专其业”是唐代工商业基本情况。现有 `terms/guanying-shougongye.md` 记官营手工业、`terms/shougong-gongchang.md` 记手工工场，terms 下无家庭手工业专条。",
      "定义、层次、自给自足、分工限制与技术承传均可复查，且与官营手工业条、手工工场条分工不同，按 term 建 D 维度条。",
      "新建 terms/jia-ting-shou-gong-ye.md，记定义、自给自足、家庭生产单位、贯穿历程、分工限制与技术承传，未载规模与商品化比例。"),
    UPD("cand-04-30", "和雇",
        "terms/hegu-zhi.md",
        "cand-04-30 跨度为 L1420。L1420 记隋唐大部分工匠不愿作无偿劳役而选择短期“和雇”或宁愿自设作坊，并以何明远“资财巨万，家有绫机五百张”与上都通化门长店聚集受雇工匠为例；L1422 记宋明和雇制普遍采用、改变生产关系、官营手工业比重相对下降。既有 `terms/hegu-zhi.md` 只收赵农 L5484 的宋代和雇制取代唐代徭役制、劳动观念与标准需求，本候选补李立新两行，形成两册对照。",
        "既有条已定义和雇制，本候选补隋唐短期和雇与宋明普遍采用，并暴露两册起始时段差异，宜更新不宜另建“和雇”条；两说并列，不裁定。",
        "更新 terms/hegu-zhi.md：补李立新 L1420、L1422 要点、何明远与通化门长店例证、两册时段差异；source_count 1→2、version 1→2。",
        note="canonical: 04-knowledge/units/terms/hegu-zhi.md。cand-04-30 并入该条，不另建“和雇”条。"),
]

for d in D:
    if not (ROOT / d["target"]).exists():
        raise SystemExit("target missing " + d["target"])

cfg = {
    "doc": DOC,
    "file": SRC,
    "rules": [
        "来源只读；正文以李立新 2011 册 Markdown 文本为主，不以来源外知识补写。",
        "引文照录：同行用“ ”，句内再含引号或跨行拼接用「 」；正文禁用 ASCII 双引号。",
        "cand-04-30 更新既有 terms/hegu-zhi.md；该条原有赵农 L5484 证据，本批补李立新 L1420、L1422，两册对和雇制起始时段的叙述差异并列，不裁定。",
        "cand-04-29 工商食官跨度为 L1394-L1831（含并入的 cand-05-34），终点尚未复读，本批不写入 decisions，保持 needs_evidence，待终点覆盖后单独裁定。",
        "图4-2 只读到图注与论述语境，未视觉核验图版；图注所载器名、工艺与朝代之外不补尺寸、藏地与织造机构。",
        "同实体先检索既有 KU 与同批目标；能归并者按 update 或 no_delta 处理，不重复建条。",
    ],
    "scope_spans": [[1380, 1429]],
    "scope_note": "覆盖 L1380-L1429：第四章“造物历史中的原生状态”标题与开篇（L1380-L1386），第一节“民间与官营生产模式的消长状态”前半（L1388-L1429）；止于第二节“个体特色与地域色调”（L1430）之前。L1430 以后留待 LL2l。",
    "deferred": [
        {
            "cid": f"{DOC}:cand-04-29",
            "entity": "工商食官",
            "span": "L1394-L1831",
            "reason": "长跨度候选，终点 L1831 尚未复读，且 payload 含 merged_candidate_ids（cand-05-34）；本批只读到 L1394 的起始论述，不能据半段裁定。",
            "next": "待 L1831 覆盖后单独裁定。",
        }
    ],
    "decisions": D,
}

out = ROOT / "_zn_decisions_ll2k.json"
out.write_text(json.dumps(cfg, ensure_ascii=False, indent=1) + "\n", encoding="utf-8", newline="\n")
print(json.dumps({"decisions": len(D), "create": sum(1 for d in D if d["action"] == "create"),
                  "update": sum(1 for d in D if d["action"] == "update"),
                  "no_delta": sum(1 for d in D if d["action"] == "no_delta"),
                  "rejected": sum(1 for d in D if d["action"] == "rejected"),
                  "deferred": len(cfg["deferred"])}, ensure_ascii=False))
