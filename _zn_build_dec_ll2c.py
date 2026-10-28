# -*- coding: utf-8 -*-
"""Build the LL2c decisions JSON."""
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


def REJ(cid, entity, target, analysis, approve, note=None):
    return {
        "cid": f"{DOC}:{cid}", "entity": entity, "action": "rejected", "target": U + target,
        "analysis": analysis, "approve": approve,
        "apply_note": "不新建条目；内容已由现有 KU 覆盖。",
        "note": note or f"{cid} 与 {U}{target} 重复，标 rejected 并保留 target_ref。",
    }


D = [
    C("cand-01-79", "轴心时代", "terms/zhouxin-shidai.md",
      "cand-01-79 跨度为 L402-L674。L402 在第二节末以“春秋战国‘轴心时代’人性觉悟时期”作前提提及；L674 给“中轴”之说的来源、雅斯贝斯的时段与各地哲学家名单、人类意识觉醒、春秋战国作为中国历史前后转折“中轴”的定位，以及“轴心”说不足以完全把握中国历史演进与中国造物历史文化特殊性的限定。全库 terms 下无轴心时代条目，persons 下无雅斯贝斯条目；本条与人物条分工为概念与提出者。",
      "跨度两端均有直接文本；概念定义、中国位置与两点限定可复查。该候选自 LL2b 转来，本批收束，宜独立成条。",
      "新建 terms/zhouxin-shidai.md，记提出、时段、中国名单、意识觉醒、中国位置、框架限定、精英思想与 L402 前期提及；原书版本与理论史未载。"),
    C("cand-01-80", "审曲面势", "terms/shenqu-mianshi.md",
      "cand-01-80 跨度为 L406-L678。L406 把“审曲面势”列为轴心时代多种造物思想之首；L678 给《考工记》原文、李立新对“审视”的解释、四要素“天有时、地有气、材有美、工有巧”与逐项释义。既有 terms/baigong.md 在职能义一节已引同一句并转述李立新的解释，但该条主语是百工的职能，没有以“审曲面势”为本体的概念条目；terms/tianshi-diqi-caimei-gongqiao.md 只据夏燕靖 2016 册立四要素。",
      "同一句在百工条中服务于职能义，在四要素条中只取后半；本候选的“审曲面势”本体与“审视”释义无条目承担，宜新建概念条，并与两条互链而不重复其分工。",
      "新建 terms/shenqu-mianshi.md，记定位、原文、审视、四要素、天时、地气、材美工巧与 L406 前期提及；成书版本与训释史未载。"),
    C("cand-02-138", "雅斯贝斯", "persons/yasibeisi.md",
      "cand-02-138 跨度为 L674。该行给“中轴”之说来自雅斯贝斯的“轴心时代”理论、公元前800—公元前200年的时段、中国与印度、伊朗、巴勒斯坦、古希腊的哲学家名单、人类意识觉醒的判断；persons 下无雅斯贝斯条目。",
      "理论来源、时段与各地名单可复查；生卒、国籍与著作出处未载，按 medium 建条并标音译。",
      "新建 persons/yasibeisi.md，记理论来源、时段、各地名单与意识觉醒；生卒、国籍、身份与著作未载。"),
    C("cand-02-53", "阴阳五行", "terms/yinyang-wuxing.md",
      "cand-02-53 跨度为 L680。该行给阴阳五行说的构成（原始阴阳观与五行说结合）、用于社会人事历史、物质运动与时空统一的一体化动态模式、五行相生与四时五方流转变换的和谐整体、对春秋战国造物思想的影响，并以《考工记》五色与五方对应、服色规范和曾侯乙墓漆衣箱天象图为例；terms 下无阴阳五行条目。",
      "定义、五色引文、服色规范与天象图例可复查；起源、成型年代与文献谱系未载，按 medium 建条。",
      "新建 terms/yinyang-wuxing.md，记定义、和谐整体、五色、服色规范、天象图例与 L406 前期提及；起源与谱系未载。"),
    C("cand-02-55", "曾侯乙墓漆衣箱天象图", "works/zenghouyi-tianxiang-tu.md",
      "cand-02-55 跨度为 L680-L683。L680 给天象图的图像内容（东宫与西宫的青龙、白虎，中有北斗，环以二十八宿古文）、阴阳五行的宇宙模式与“仰观俯察”的图形判断；L683 图题作“图1-22 曾侯乙墓漆衣箱天象图”。既有 works/zenghouyi-lacquer-clothing-chests.md 记同墓漆木衣箱并明确声明不把天象图并入衣箱描述；places/zenghouyi-tomb.md 只有一句提及。",
      "图像内容、宇宙模式与图题可复查；衣箱尺寸、图像尺寸、绘制技法与衣箱编号未载，按 medium 建条并声明图版未视觉核验。",
      "新建 works/zenghouyi-tianxiang-tu.md，记图题、图像内容、宇宙模式与图形判断；尺寸、技法与箱号未载。"),
    REJ("cand-02-57", "车马人物出行图", "places/baoshan-chumu.md",
        "cand-02-57 跨度为 L685-L688。L685 记包山大冢楚墓漆奁盖圈上的《车马人物出行图》，给出直径 28 厘米的奁盖圈、展开为长 87.4 厘米、高 5.2 厘米的漆纹样作品，并以“有机整体”与阴阳对立实体作解释；L688 为图题。既有 places/baoshan-chumu.md 已完整收录这批数据与“时间中的空间连续变化”等判断。",
        "既有包山楚墓条已覆盖同一器物、尺寸与解释，单独立条只重复同一段，不增加可检索信息。"),
    C("cand-02-143", "鹿角立鹤", "works/lujiao-lihe.md",
      "cand-02-143 跨度为 L692-L701。L693 图题作“图1-24 鹿角立鹤”；L701 在“天神、地祇、人鬼”句后以（图1—24）回指。正文没有形制、材质、尺寸与出土信息；works 下无该器条目。",
      "图题与回指关系可复查；图题只给器名，正文未展开形制，按 low 建条并声明图版未视觉核验。",
      "新建 works/lujiao-lihe.md，记图题与引及语境；形制、材质、尺寸与出土未载，不据外部知识补写。"),
    C("cand-02-62", "镇墓兽", "terms/zhenmushou.md",
      "cand-02-62 跨度为 L701。该行给楚墓出土数百件“镇墓兽”、共同特征为兽首插有真正的鹿角、置于墓室的两项功能（辟邪驱鬼、争取冥福），并以天神、地祇、人鬼观念为语境；terms/xiangsheng-xing.md 只以鸮形器推测其功能，未立专条。",
      "出土规模、共同特征与两项功能可复查；形制分类、尺寸、墓号与统计口径未载，按 medium 建条。",
      "新建 terms/zhenmushou.md，记出土规模、共同特征、观念语境；形制分类、尺寸与统计口径未载。"),
    UPD("cand-02-60", "楚帛书", "works/chu-boshu.md",
        "cand-02-60 跨度为 L701-L704。L701 把“长沙子弹库战国帛书上的神怪图纹（图1—26）”列为神怪观念的例证；L704 图题作“图1-26 楚帛书（湖南长沙子弹库楚墓出土）”。既有 works/chu-boshu.md 据高丰 2004 册记出土、38×45 厘米、900 余字、中心双篇与四周图文，未含李立新册。",
        "既有条已覆盖高丰一侧，本候选补的是李立新的神怪观念语境与图题，宜更新不宜新建；两册详略不同，须并列而不改写。",
        "更新 works/chu-boshu.md：补李立新 L701、L704 三条要点与两册分工，新增“五、李立新 2011 的神怪图纹语境”，证据边界顺延为“六”，来源数升为 2，版本升为 2。"),
    UPD("cand-02-63", "宴乐渔猎攻战纹壶", "works/yanle-shuilu-gongzhan-wen-hu.md",
        "cand-02-63 跨度为 L706-L709。L706 把采桑、攻战、狩猎、宴乐与鸟兽草木纹饰列为战国纹饰清新生活气息的例证；L709 图题作“图1-27 宴乐渔猎攻战纹壶图形展开图”。既有 works/yanle-shuilu-gongzhan-wen-hu.md 已收高丰、赵农、田自秉三册，“宴乐渔猎攻战纹壶”本就在别名中。",
        "既有条已覆盖三册，本候选补的是李立新册的器名、图题与世俗化语境；李立新未标出土地，按器名并入而保留归属边界，宜更新不宜新建。",
        "更新 works/yanle-shuilu-gongzhan-wen-hu.md：补李立新 L706、L709 三条要点与归属边界，描述补一段，来源数升为 4，版本升为 4。"),
    C("cand-02-144", "素面青铜器大府镐", "works/dafu-gao.md",
      "cand-02-144 跨度为 L706-L712。L706 以素面青铜器与铜镜、带钩、铜灯并列，说明造物日用化的趋势；L712 图题作“图1-28 素面青铜器大府镐”。正文只称“素面青铜器”，未单称此器，也没有形制、尺寸、铭文与出土信息；works 下无该器条目。",
      "图题与类属语境可复查；正文不描述本器，按 low 建条并声明图版未视觉核验。",
      "新建 works/dafu-gao.md，记图题、日用化语境与器名说明；形制、尺寸与铭文未载。"),
    C("cand-02-64", "宗白华", "persons/zongbaihua.md",
      "cand-02-64 跨度为 L714。该行在诸子百家造物思想前引宗白华“工匠艺术家更要走在哲学家的前面”一段，L716 以莲鹤方壶为例说明“艺术抢先表现的一个新境界”；persons 下无宗白华条目，works/lianhe-fanghu.md 已引同一句但只承担器物条。",
      "引文、例证与引用语境可复查；生卒、机构与著作出处未载，按 medium 建条。",
      "新建 persons/zongbaihua.md，记引文、莲鹤方壶例证与引用语境；生卒、机构、身份与著作未载。"),
    C("cand-02-150", "九流十家", "terms/jiuliu-shijia.md",
      "cand-02-150 跨度为 L718。该行给出“九流十家”的提法、王室衰微与权力下移、官营手工业削弱、私营手工业发展、大型制造业主与巨商出现、士人游离旧等级秩序并带来思想与精神自由，以及其知识背景与技艺修养同政治需要结合；L723 续给“六种不同思想”的归纳体例。terms 下无九流十家条目。",
      "提法、社会背景与士人论述可复查；名目、师承与文献出处未载，按 medium 建条。",
      "新建 terms/jiuliu-shijia.md，记提法、社会背景、巨商、士人、讨论范围与六家体例；名目与师承未载。"),
    C("cand-02-67", "大器免成", "terms/daqi-miancheng.md",
      "cand-02-67 跨度为 L731。该行给“大器晚成”按《帛书》乙本读作“大器免成”、“晚者，免之借，免成，犹无成”的训释、《吕氏春秋》“成”的层与调和二解、器外之层即饰层、免成当是免饰之意、老子不喜繁缛精细与“不装饰的装饰”的判断。persons/laozi.md 已收老子造物思想，但没有“大器免成”的文本训释条。",
      "命题、训释、二解与免饰判断可复查；《帛书》版本、释文与训释学术史未载，按 medium 建条并与老子条互链。",
      "新建 terms/daqi-miancheng.md，记命题、训释、层与调和、饰层、免饰、老子态度与不装饰的装饰；版本与学术史未载。"),
    REJ("cand-02-68", "重本抑末", "persons/han-fei-zi.md",
        "cand-02-68 跨度为 L735。该行记韩非的“重本抑末”思想，并下判断称其在一定程度上扼杀了造物的创造性活动、给后世造物设计带来很大的负面影响。既有 persons/han-fei-zi.md 已收韩非的功利造物思想与同一句否定判断。",
        "既有韩非条已覆盖同一引文与评价，单独立条只重复同一段，不增加可检索信息。"),
]

for d in D:
    if d["action"] in ("create", "update") and not (ROOT / d["target"]).exists():
        raise SystemExit("missing target " + d["target"])

cfg = {
    "doc": DOC,
    "file": SRC,
    "rules": [
        "来源只读；正文只据李立新 2011 册 Markdown 文本，不以来源外知识补写。",
        "引文照录：同行用“ ”，跨行拼接用「 」；正文禁用 ASCII 双引号。",
        "图注单独成条时保留图题与说明的行位，不连读被正文或图注隔开的两处。",
        "relation 只记可为后续审查提供线索的既有条目，不写入正式 relations。",
        "同一对象不重复建条：既有 KU 已覆盖者 rejected，形制相符可互补者 update。",
        "cand-01-79 与 cand-01-80 的跨度起点在 LL2b 复读范围内、终点在本批范围内，本批据两端复读收束，不再留 needs_evidence。",
    ],
    "scope_spans": [[672, 739]],
    "scope_note": "覆盖 L672-L739：第五节“轴心时代的造物思想”全节，含 L674 轴心时代、L678 审曲面势、L680-L688 阴阳五行与两件漆器图、L690-L712 形式法则与神怪及日用观念、图1-24 至图1-28 图注、L714-L737 诸子造物思想、L739 节末；止于第六节标题（L741）之前。",
    "decisions": D,
    "extras": [
        {
            "target": "04-knowledge/units/terms/baigong.md",
            "entity": "百工",
            "parent_cid": f"{DOC}:cand-01-80",
            "note": "在相关知识元补入 terms/shenqu-mianshi.md 链接，并顺带修正三处分析性引号与一处 OCR 异文引号，使全库引文审计可通过。",
        },
        {
            "target": "04-knowledge/units/terms/tianshi-diqi-caimei-gongqiao.md",
            "entity": "天时地气材美工巧",
            "parent_cid": f"{DOC}:cand-01-80",
            "note": "在相关知识元补入 terms/shenqu-mianshi.md 链接，标明李立新册对同一句四要素的逐项释义见该条。",
        },
    ],
}

out = ROOT / "_zn_decisions_ll2c.json"
out.write_text(json.dumps(cfg, ensure_ascii=False, indent=1) + "\n", encoding="utf-8", newline="\n")
print(json.dumps({"decisions": len(D), "create": sum(1 for d in D if d["action"] == "create"),
                  "update": sum(1 for d in D if d["action"] == "update"),
                  "rejected": sum(1 for d in D if d["action"] == "rejected"),
                  "extras": len(cfg["extras"])}, ensure_ascii=False))
