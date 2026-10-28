# -*- coding: utf-8 -*-
"""Build the LL2p decisions JSON (conclusion)."""
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
    UPD("cand-05-58", "木制海船", "works/houzhu-chuan.md",
        "cand-05-58 跨度为 L1926-L1930，语境在结论章第二节论“延续性”。图注 L1927-L1928 题“木制海船”，记长约 3500 厘米、船身扁阔尖底方头、十三个水密隔舱、多桅多舱、升降舵、大型远洋海船、南宋、泉州海外交通史博物馆。existing `works/houzhu-chuan.md` 记赵农所见泉州后渚宋船残骸，长 24.20 米、宽 9.15 米、载重 200 吨以上。图注未称后渚船，但与后渚船在出土地、收藏单位与隔舱数上相合；本条按 update 并入，保留图注原名并把两处长度口径并列，不裁定。",
        "图注尺度、隔舱、桅舵、南宋年代与收藏单位均可复查，按 update 并入后渚船条；图注未给船名、出土年份与残骸尺寸，两处长度口径不同。",
        "更新 works/houzhu-chuan.md：加李立新为第二来源，补图注原题、长约 3500 厘米、尖底方头、十三个水密隔舱、多桅多舱、升降舵、南宋与泉州海外交通史博物馆，并列 24.20 米与约 35 米两种口径，version 1→2。"),
    C("cand-05-62", "鎏金银浑天仪", "works/liujin-yin-huntianyi.md",
      "cand-05-62 为 L1952-L1954 图注。图注记清代鎏金银浑天仪有地平线、子午环、赤道环、太阳、月亮、地球等，地球刻经纬线及各大洲名称，设计精巧，可手工操作，引自《中国文物精华大辞典》。existing `works/huntianyi.md` 是东汉张衡浑天仪，`works/shuiyun-huntianyi.md` 是水运浑天仪，均非此清器；`terms/guifanhua.md` 是原则条，不是器物。本条按 work 新建。",
      "年代、构件、地球刻纹与操作方式均可复查，按 work 建 B 维度条；尺寸、重量、制作年代、作坊与现藏单位未载。",
      "新建 works/liujin-yin-huntianyi.md，记清代、地平线、子午环、赤道环、太阳月亮地球、经纬线与各大洲名称、手工操作，并说明图注插在规范化一节而未自证为规范化例证。"),
    C("cand-05-64", "本元特征", "terms/benyuan-tezheng.md",
      "cand-05-64 为 L1972-L1980，是结论章八项特质之七。原文以艺术源自实用器物、设计史复现艺术历史的原初存在、实用物质与审美精神两种特性统一可转化、造物设计扮演“母体”角色立论。existing terms 下无本元特征条；`terms/yishu-shejishi.md` 记艺术设计史，`terms/sanzhong-zaowu-sheji.md` 记三种造物设计，均不承担这一特质。本条按 term 新建。",
      "艺术源自实用、两种特性、转化路径、母体角色与学术意义均可复查，按 term 建 A 维度条；“本元”的出处与定义边界未载，标题脚注未读。",
      "新建 terms/benyuan-tezheng.md，记八项特质之七、艺术源自实用、设计史的对象、两种特性及其转化、母体角色与学术意义，注明标题带脚注号 ① 而本批未读该脚注。"),
    C("cand-05-65", "变与统", "terms/bian-yu-tong.md",
      "cand-05-65 为 L1982-L1985，是结论章八项特质之八。原文以变与统为设计史发展的阴阳两极：变是适应工艺制作条件与社会时势，不是抛弃传统而是变其刻板烦琐；统是整合、延续，化凌乱为协调；并指出传统社会可演绎阶段性突破而近代落后于欧美。existing terms 下无变与统条；`terms/jieduanxing-tupo-tuijin.md` 记阶段性突破推进，`terms/liangxiang-yanhua.md` 记两向演化，层次不同。本条按 term 新建。",
      "阴阳两极定位、变与统定义、统的整合机制、阶段性突破与近代转折均可复查，按 term 建 A 维度条；概念出处与量化指标未载。",
      "新建 terms/bian-yu-tong.md，记阴阳两极定位、变的定义与性质、统的定义与机制、阶段性突破与近代落后，注明概念学派出处未载。"),
    UPD("cand-05-73", "鎏金忍冬纹镂孔银香球", "works/tang-yin-xiangnang.md",
        "cand-05-73 为 L2019-L2023 图注，语境在结论章第三节论设计现代化艰难性。图注标题作“鎏金忍冬纹镂孔银香球”，记直径 5.4 厘米、钣金成型、上下半球子母口、两个同心圆环与焚香金盂、对称活轴、盂面始终平衡、陀螺仪原理、唐、西安市文物管理委员会藏。existing `works/tang-yin-xiangnang.md` 是唐代银香囊的器类条，已收何家村、沙坡村、法门寺各件并记“其余直径大多在五厘米左右”，5.4 厘米正在此范围；本条按 update 并入器类条，不另建单件重复条目。",
        "器名、直径、成型、同心圆环、平衡效果与原理判断均可复查，按 update 并入唐代银香囊条；出土地点、出土年份、重量、链长与现藏编号未载。",
        "更新 works/tang-yin-xiangnang.md：加李立新为第四来源，补“鎏金忍冬纹镂孔银香球”器名、直径 5.4 厘米、钣金成型、子母口、两个同心圆环与对称活轴、陀螺仪原理、西安市文物管理委员会收藏，并列“镂孔”与“镂空”两种写法，version 2→3。"),
]

for d in D:
    if not (ROOT / d["target"]).exists():
        raise SystemExit("target missing " + d["target"])

cfg = {
    "doc": DOC,
    "file": SRC,
    "rules": [
        "来源只读；正文以李立新 2011 册 Markdown 文本为主。",
        "引文照录：同行用“ ”，句内再含引号或跨行拼接用「 」；正文禁用 ASCII 双引号。",
        "图注只读到文字，图版未视觉核验；图注不能替代正文论证。",
        "木制海船图注未称后渚船，按出土地、收藏单位与隔舱数三项线索并入后渚船条；两处长度口径并列，不裁定。",
        "鎏金忍冬纹镂孔银香球并入唐代银香囊器类条，不另建单件重复条目。",
        "结论章八项特质中，仅本元特征与变与统有 unit 候选；整合性、延续性、适应性、礼乐性、规范化、地域性六项不越出候选另建条目。",
        "同实体先检索既有 KU 与同批目标；能归并者按 update 处理，不重复建条。",
    ],
    "scope_spans": [[1861, 2033]],
    "scope_note": "覆盖 L1861-L2033：结论全篇，含第一节“对设计史运行规律的认识”L1863-L1912（图表六 L1871、鸭形玻璃注 L1892）、第二节“对中国传统设计艺术特质的认识”L1914-L1984（八项特质，其中第 7 项本元特征 L1972-L1980、第 8 项变与统 L1982-L1985）、第三节“对设计现代化艰难性的历史思考”L1986-L2033（鎏金忍冬纹镂孔银香球 L2019-L2023），止于参考文献标题 L2034 之前。图表六与其余图注只读到文字，未视觉核验。",
    "deferred": [],
    "decisions": D,
}

out = ROOT / "_zn_decisions_ll2p.json"
out.write_text(json.dumps(cfg, ensure_ascii=False, indent=1) + "\n", encoding="utf-8", newline="\n")
print(json.dumps({"decisions": len(D), "create": 3, "update": 2, "deferred": 0}, ensure_ascii=False))
