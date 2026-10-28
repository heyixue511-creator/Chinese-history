# -*- coding: utf-8 -*-
"""Build the LL2f decisions JSON (Buddhist penetration, L944-L1029)."""
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
    C("cand-03-05", "傅抱石", "persons/fu-bao-shi.md",
      "cand-03-05 跨度为 L946。该行记设计艺术与佛教的关联在东汉有腊缬佛像和摩崖造像，魏晋南北朝佛教建筑、佛塔、夹纻佛像等造物大量出现，并用“傅抱石先生的话说，魏晋南北朝时代‘洵可说是完全的佛教美术’时代”概括。persons 下无傅抱石条目；既有 events/liuchao-buddhist-caves.md 记石窟造物，但不收这一人物称引。",
      "称引与上下文均可复查；人物生卒、身份与出处未载，按 medium 建条只登记这一处称引，不补来源外生平。",
      "新建 persons/fu-bao-shi.md，记称引、前后文与未载项。"),
    C("cand-03-03", "杨泓", "persons/yang-hong.md",
      "cand-03-03 跨度为 L960-L1025。L960 引其研究：佛教艺术造型在江南的影响主要用于装饰器物的图纹，没有将佛像尊为礼拜的圣像；L1025 记其从敦煌莫高窟十六国至隋的壁画、雕塑中寻到公元5至10世纪中国家具演变的重要线索。persons 下无杨泓条目（persons/yang-xun.md 为明代杨埙，非一人）。",
      "两处研究结论可复查；生卒、任职机构与发表出处未载，按 medium 建条聚合两处，不补来源外生平。",
      "新建 persons/yang-hong.md，记江南佛教艺术判断、家具史线索与方法意义。"),
    C("cand-03-04", "石兴邦", "persons/shi-xing-bang.md",
      "cand-03-04 跨度为 L971。该行引石兴邦对八重宝函的判断：八重宝函之三的第四重宝函四面造像及旁边供养神符合密宗仪轨，正面主尊为思维相六臂如意观世音菩萨，与现图胎藏界曼荼罗中观世音第二位尊者相同。places/famen-si-digong.md 已把该判断作为地宫密教仪轨证据抄录，但 persons 下无石兴邦条目；本批建人物条以承载其研究者身份与判断，并与地宫条互链。",
      "判断原文完整、可复查；生卒、机构与出处未载，按 medium 建条，不把地宫条的器物叙述复制进人物条。",
      "新建 persons/shi-xing-bang.md，记密宗仪轨判断与未载项。"),
    C("cand-03-65", "曼荼罗", "terms/man-tuo-luo.md",
      "cand-03-65 跨度为 L971。该行给曼荼罗定义、南亚密宗在地画圆或方区域并建土坛的来源、现图曼荼罗的区分，以及法门寺地宫实物与放置程序、捧真身菩萨莲花底座、石兴邦八重宝函判断的三重对应；L983 另记汉化密宗曼荼罗在宋代之后衰微而在日本流传光大，法海寺毗卢遮那佛曼荼罗属藏密而非汉密。terms 下无曼荼罗条目；places/famen-si-digong.md 只把它作为地宫陈设的解释概念。",
      "定义、来源、现图区分与流变均可复查；传入年代、经典依据与坛场尺寸未载，按 medium 建条并链接地宫条与石兴邦条。",
      "新建 terms/man-tuo-luo.md，记定义、南亚来源、现图曼荼罗、法门寺对应、图2-16 与汉化流变。",
      ),
    C("cand-03-66", "五供", "terms/wu-gong.md",
      "cand-03-66 跨度为 L985。该行给供具定义与四类供物，记“三具足”即香炉一具、烛台一对、花瓶一对，按个数为五又称“五具足”，民间称“五供”，并举唐咸通九年王玠刻印《金刚经》卷首图与元刻本《金刚经》卷首图两例，称其为通用至今的佛教造物设计。terms 下无五供或三具足条目；publications/jingangjing-868.md 只记卷首图，未立供具组合条。",
      "组合名目、计数与两处图例均可复查；定名年代、尺寸与材质未载，按 medium 建条。",
      "新建 terms/wu-gong.md，记供具定义、四类供物、三具足／五具足、唐元图例与通用性。",
      ),
    UPD("cand-03-39", "唐咸通九年木刻版画《金刚般若波罗蜜经》卷首图", "publications/jingangjing-868.md",
        "cand-03-39 跨度为 L980-L985。L981 图题作“图2-18 唐咸通九年木刻版画《金刚般若波罗蜜经》卷首图”，L985 记王玠刻印《金刚经》卷首图佛前有一带盖香炉、左右一对高足高盖形器皿，作为五供的唐代图例。既有 publications/jingangjing-868.md 已收赵农所记同一咸通九年本的出土、7纸连接、扉页说法图与卷尾题记，但未收李立新册的版画定名与佛前供器；候选 knowledge_match 记 novel，实为同本异称，应更新而非新建。",
        "同一卷的两个来源，合并著录可避免把卷首图拆成独立作品条；图版未核，只记文字。",
        "更新 publications/jingangjing-868.md：补图题与卷首图内容两条、两册分工一条，来源升为2，版本升为2。"),
    UPD("cand-03-40", "鎏金卧龟莲花纹朵带五足银熏炉", "works/wensiyuan-yin-xunlu.md",
        "cand-03-40 跨度为 L985-L988。L985-L990 记法门寺地宫鎏金卧龟莲花纹朵带五足银熏炉：钣金成型、附件浇铸、纹饰涂金，盖沿忍冬纹、盖面五朵莲花各卧一龟、下层莲瓣镂孔、腹壁流云纹与五只独角天龙兽足，并判断盖形、流云纹与绶带盘结为中国原有造型纹饰，以金刚结、八吉祥说明中国化；原文尺寸作295cm、腹深70cm。既有 works/wensiyuan-yin-xunlu.md 收夏燕靖 2016 同器实测29.5cm／7cm／5.363千克、铭文与藏地，works/yin-xunlu.md 为唐宋同名异器合条，places/famen-si-digong.md 已收器形与数值存疑；候选 knowledge_match 记 novel，实为同器，应更新最精确的器物条。",
        "同器已有两处器物条，本批选文思院造专条承载李立新的汉化判断与尺寸异文，不另建新条；不合并既有重复条，留待后续治理。",
        "更新 works/wensiyuan-yin-xunlu.md：补尺寸异文、汉化判断、金刚结、八吉祥与两册分工，来源升为2，版本升为2。"),
    REJ("cand-03-38", "捧真身菩萨", "places/famen-si-digong.md",
        "cand-03-38 跨度为 L971-L978。该段只给捧真身菩萨侧面观图2-17，并记其莲花底座即典型曼荼罗坛；无尺寸、材质、出土位置与制作年代。places/famen-si-digong.md 已完整收录该图题与莲花底座判断，并把它置于地宫陈设叙述中。",
        "单图注加一句判断不足以独立成 work 条；内容已由地宫条覆盖，rejected 并保留 target_ref。"),
    REJ("cand-03-41", "阮咸（日本正仓院藏）", "institutions/shosoin.md",
        "cand-03-41 跨度为 L1022-L1023。L1023 图题作“图2-23 阮咸（日本正仓院藏）”，L1020 记从正仓院所藏中国设计物品与唐代佛教艺术品对照可获知中国造物艺术东传日本。institutions/shosoin.md 已收图2-23 阮咸与 L1020-L1023 东传判断；terms/ruan-xian.md 记乐器本体。",
        "图注只到图题一级，无器物尺寸、槽腹、弦柱与入藏编号；对象已由正仓院条覆盖，rejected 并保留 target_ref。"),
    REJ("cand-03-42", "葵口圈足秘色瓷碗", "terms/mise-porcelain.md",
        "cand-03-42 跨度为 L1025-L1028。L1025 以1987年法门寺塔基地宫发现十三件“秘色瓷”说明秘色越器之谜被解开，L1028 图题作“图2-24 葵口圈足秘色瓷碗（法门寺地宫出土）”。terms/mise-porcelain.md 已收 L1025、L1028 两行，含十三件口径、方法论意义与图2-24 图版条；places/famen-si-digong.md 亦记图2-24。",
        "本条只补图题，无独立器形、尺寸与工艺信息；已由秘色瓷条覆盖，rejected 并保留 target_ref。"),
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
    ],
    "scope_spans": [[944, 1029]],
    "scope_note": "覆盖 L944-L1029：第二章第二节“佛教的渗透及其设计史意义”全节，含 L946 佛教向艺术领域渗透、L953-L960 造像建寺与江南佛教器物、L964-L966 汉化佛教法器与庄严具、L971-L983 曼荼罗、L985-L990 供具与银熏炉、L992-L1005 钟鼓磬木鱼、L1007-L1009 佛教与设计观念、L1014-L1028 佛教造物艺术研究的三项内容与图2-13至图2-24；止于第三节标题（L1030）之前。",
    "decisions": D,
}

out = ROOT / "_zn_decisions_ll2f.json"
out.write_text(json.dumps(cfg, ensure_ascii=False, indent=1) + "\n", encoding="utf-8", newline="\n")
print(json.dumps({"decisions": len(D), "create": sum(1 for d in D if d["action"] == "create"),
                  "update": sum(1 for d in D if d["action"] == "update"),
                  "rejected": sum(1 for d in D if d["action"] == "rejected"),
                  "extras": len(cfg.get("extras", []))}, ensure_ascii=False))
