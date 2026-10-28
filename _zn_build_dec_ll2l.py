# -*- coding: utf-8 -*-
"""Build the LL2l decisions JSON (chapter 4 section 2, L1430-L1470)."""
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


D = [
    C("cand-04-36", "张成云纹剔犀漆盒",
      "works/zhang-cheng-yun-wen-ti-xi-qi-he.md",
      "cand-04-36 跨度为 L1447-L1450。L1447 记张成所作另一剔犀漆盒今藏安徽省博物馆、盒呈圆形、雕云纹三组、雕刻刀口深达1cm、刻法深峻、古朴醇厚，并给嘉兴西塘扬汇剔红与剔犀的整体工艺水平；L1450 图4-4 图注定名为“张成云纹剔犀漆盒”。existing `persons/zhang-cheng.md` 已收该盒，但 works 下无单器条；`works/zhang-cheng-tihong-box.md` 是田自秉所记另一件剔红山水人物圆盒，不是此盒。",
      "图注与形制可独立检索，且与张成人物条、张成剔红圆盒条分工不同，按 work 建条；尺寸、递藏与款识未载，图版未视觉核验。",
      "新建 works/zhang-cheng-yun-wen-ti-xi-qi-he.md，记图注、藏地、器形、云纹三组与刀口深度。"),
    C("cand-04-37", "杨茂剔红观瀑图八方盘",
      "works/yang-mao-ti-hong-guan-pu-tu-ba-fang-pan.md",
      "cand-04-37 跨度为 L1447-L1457。L1447 记杨茂《剔红花卉渣斗》与“剔红观瀑图八方盘”，称后者已受院画风格影响但四周相连花卉浮雕效果极佳，并引《格古要论》“张成、杨茂者，剔红最得名”；L1457 图4-5 图注定名。existing `persons/yang-mao.md` 已收该盘，works 下无单器条。",
      "风格评价与图注可独立检索，且与杨茂人物条分工不同，按 work 建条；尺寸、藏地与递藏未载，图版未视觉核验。",
      "新建 works/yang-mao-ti-hong-guan-pu-tu-ba-fang-pan.md，记图注、院画风格影响与花卉浮雕评价。"),
    C("cand-04-83", "紫砂瓜形壶",
      "works/zi-sha-gua-xing-hu.md",
      "cand-04-83 跨度为 L1463-L1464。L1464 图4-6 图注只给“紫砂瓜形壶（明代）”；L1461 以宜兴紫砂“方非一式，圆不一样”与龚春、时大彬、制壶四大家、陈鸣远、杨彭年、邵大亨等名家谱系说明地域造物的块团形式。existing `terms/zisha-tao.md` 记紫砂陶，`works/zisha-donglinggua.md` 是夏燕靖所记清代“东陵瓜”，非此壶。",
      "图注可独立检索，且与紫砂陶条、东陵瓜条分工不同，按 work 建条；仅图注与整体语境，制作者、尺寸与藏地未载，置信度 low。",
      "新建 works/zi-sha-gua-xing-hu.md，记图注、宜兴紫砂整体评价与名家谱系，未载项明列。"),
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
        "图4-3 对鹿纹样与陵阳公样、窦师纶相关候选（cand-04-31、cand-04-32）已在此前批次并入 terms/lingyang-gong-pattern.md、persons/dou-shilun.md，本批不重复建条；图4-3 不另建单图条。",
        "张成、杨茂人物候选（cand-04-34、cand-04-35）已并入既有 person 条，本批只建器物条，不重复写人物。",
        "图4-4、图4-5、图4-6 只读到图注与正文描述，未视觉核验图版；图注之外不补尺寸、藏地与递藏。",
        "同实体先检索既有 KU 与同批目标；能归并者按 update 或 no_delta 处理，不重复建条。",
    ],
    "scope_spans": [[1430, 1470]],
    "scope_note": "覆盖 L1430-L1470：第四章第二节“个体特色与地域色调”全节，含地域性造物的地理与人文条件（L1432-L1438）、扬州制镜与吕氏家族（L1440）、陵阳公样与窦师纶（L1445）、元代嘉兴髹漆与张成、杨茂、彭君宝（L1447-L1459）、宜兴紫砂（L1461-L1464）、地域集群的交流（L1466-L1470）；止于第三节“一般造物与经典造物之间的互动关系”（L1472）之前。",
    "deferred": [],
    "decisions": D,
}

out = ROOT / "_zn_decisions_ll2l.json"
out.write_text(json.dumps(cfg, ensure_ascii=False, indent=1) + "\n", encoding="utf-8", newline="\n")
print(json.dumps({"decisions": len(D), "create": len(D), "deferred": 0}, ensure_ascii=False))
