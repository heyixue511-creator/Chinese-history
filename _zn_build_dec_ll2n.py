# -*- coding: utf-8 -*-
"""Build the LL2n decisions JSON (chapter 5 section 3)."""
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
    return {
        "cid": f"{DOC}:{cid}", "entity": entity, "action": "update", "target": U + target,
        "analysis": analysis, "approve": approve, "apply_note": apply_note,
        "note": note or f"canonical: {U}{target}。{cid} 并入该条。",
    }


D = [
    UPD("cand-04-82", "曾侯尊盘", "works/zenghouyi-zunpan.md",
        "cand-04-82 跨度为 L1635-L1636，正文语境在 L1640-L1642。L1636 图5-7 图注作“曾侯尊盘”，L1640 把它作为曾国墓葬耗铜的例证：战国小国国君乙的墓葬耗掉十多吨青铜铸造六十五件大型陪葬青铜器，L1642 由此引出铜材缺乏、规模缩小的判断。existing works 下已有 `works/zenghouyi-zunpan.md`（赵农、夏燕靖 2016、田自秉三源），本条并入该条，不另建重复器物。",
        "图注与墓葬耗铜句均可复查，按 update 并入既有曾侯尊盘条；李立新未给尊盘尺寸、藏地与合金配比，耗铜句只作墓葬规模旁证，不改写尊盘形制。",
        "更新 works/zenghouyi-zunpan.md：加李立新为第四来源、补“曾侯尊盘”别名、图5-7 图注与曾国墓葬耗铜、六十五件大型青铜器的旁证，version 2→3。"),
    C("cand-05-03", "两向演化", "terms/liangxiang-yanhua.md",
      "cand-05-03 跨度为 L1649-L1664。L1651 给定义：同一物品渗入社会规范、伦理思想或宗教思想后分化为与本来的物品大为悬殊的面貌，冕服、缂丝、刺绣品与陶瓷名窑艺术品走一路，普通服饰、纺织品、刺绣品与陶瓷品沿自我生成的路子前行；两向发展体现一般造物与经典造物的关系与造物设计艺术的基本规律。L1656-L1660 以建筑居室为例，宫廷建筑与民居分途演化。existing terms 下无该概念条；`terms/sanzhong-zaowu-sheji.md` 是设计分工三分，不是演化机制。",
      "定义、两路对举与建筑例证均可复查，按 term 建 B 维度条；“两向演化”一名的理论出处未载，不补来源外谱系。",
      "新建 terms/liangxiang-yanhua.md，记定义、两路对举、关系判断与建筑居室的两系演化，别名“两向发展”。"),
    UPD("cand-05-06", "玻璃器（中国古代玻璃）", "terms/liuli.md",
        "cand-05-06 跨度为 L1667-L1683。该段以玻璃器为“几度沉浮”的例证，给春秋末期至近代的分期、器类与成分判断。existing terms 下已有 `terms/liuli.md`，其第一义即原始玻璃，与李立新所称玻璃器同指中国古代玻璃；本条按 update 并入该条，不另建重复术语。",
        "分期、器类与例证均可复查，按 update 并入琉璃条第一义；李立新记钠钡玻璃，田自秉记铅钡玻璃，两说抵触，并列照录不裁定。",
        "更新 terms/liuli.md：加李立新为第二来源、补玻璃器历代沉浮与春秋至近代分期、加“玻璃器”别名，并记钠钡/铅钡的成分分歧，version 1→2。"),
    C("cand-05-14", "画像石", "terms/huaxiangshi.md",
      "cand-05-14 跨度为 L1710-L1723。L1710 给定名、年代、分布、数量与厚葬背景，L1715 分墓室与祠堂两系并给传承来源，L1717 给东汉末的断裂与起落判断，L1723 给明清砖雕余绪，L1713、L1720-L1721 为图注。existing terms 下无画像石条；`terms/huaxiangzhuan.md` 是画像砖，属另一类材料。",
      "定名、年代、分布、数量与两系传承均可复查，按 term 建 C 维度条；尺寸、雕刻技法分类与拓片目录未载。",
      "新建 terms/huaxiangshi.md，记定名与年代、分布与数量、厚葬背景、墓室与祠堂两系、断裂与余绪，别名“汉画像石”。"),
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
        "L1635-L1636 与 L1640-L1642 同属图5-7 的图注与正文语境，分建会拆散同一证据，按 update 并入既有 `works/zenghouyi-zunpan.md`。",
        "玻璃器与琉璃同指中国古代玻璃，按 update 并入 `terms/liuli.md`；钠钡/铅钡两说不裁定。",
        "两向演化与三种造物设计是不同概念，画像石与画像砖是两类材料，均不合并。",
        "同实体先检索既有 KU 与同批目标；能归并者按 update 或 no_delta 处理，不重复建条。",
    ],
    "scope_spans": [[1603, 1737]],
    "scope_note": "覆盖 L1603-L1737：第五章第三节“演化与突破”全节，含七类演化情况（L1607 本为一般造物而后显赫一时、L1617 主导地位消亡或退其次、L1649 同一造物两向演化、L1665 几度沉浮起落、L1698 一物衍生另一物、L1708 断裂、L1729 突破）与全节小结 L1737；止于第六章标题 L1739 之前。",
    "deferred": [],
    "decisions": D,
}

out = ROOT / "_zn_decisions_ll2n.json"
out.write_text(json.dumps(cfg, ensure_ascii=False, indent=1) + "\n", encoding="utf-8", newline="\n")
print(json.dumps({"decisions": len(D), "create": 2, "update": 2, "deferred": 0}, ensure_ascii=False))
