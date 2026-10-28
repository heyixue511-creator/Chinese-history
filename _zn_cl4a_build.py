# -*- coding: utf-8 -*-
"""Build CL3b claim rows (10 new) and 13 cross-edition corroboration patches."""
import json
from pathlib import Path

ROOT = Path(r"D:/中国设计史研究")
DOC = "2016-xiayanjing-zhongguo-yishu-shejishi-upgrade"
SRC = "03基础书籍-md文档/中国艺术设计史（升级版）_夏燕靖_2016_上海人民美术出版社.md"
DATE = "2026-10-27"


def Q(s: str) -> str:
    s = s.replace("‘", "“").replace("’", "”")
    assert '"' not in s, s
    return s


def C(cid, ctype, zh, en, confidence, supported, note, start, end, kind,
      key_lines, block_ids, chapter, section):
    for p in supported:
        assert (ROOT / p).is_file(), p
    return {
        "claim_id": cid,
        "statement_zh": Q(zh),
        "statement_en": en,
        "claim_type": ctype,
        "source": {
            "doc_id": DOC,
            "source_file": SRC,
            "source_span": {
                "line_start": start,
                "line_end": end,
                "span_kind": kind,
                "key_lines": key_lines,
                "block_ids": block_ids,
                "chapter": chapter,
                "section": section,
            },
            "candidate_id": None,
        },
        "confidence": confidence,
        "consensus": "tentative",
        "review_status": "source_backed",
        "supported_by": supported,
        "discussion_notes": Q(note),
        "created": DATE,
        "updated": DATE,
    }


CH = "夏商西周时期的设计规制"
rows = []

rows.append(C(
    "claim-0273", "historiographic_claim",
    "夏燕靖认为，夏商周时代又称先秦三代，指秦朝建立以前经历夏、商、西周及春秋、战国的历史时代，时间约为公元前2070—前221年；他并称此期是继旧石器时代、新石器时代之后被称作第三个文明期的“青铜时代”，也是我国古代文明的始发期和科学技术萌发期。",
    "Xia Yanjing holds that the Xia-Shang-Zhou era, also called the Three Dynasties of the pre-Qin period, designates the historical era before the Qin unification, spanning the Xia, Shang, Western Zhou, Spring and Autumn, and Warring States periods, roughly 2070–221 BCE. He further describes this era as the Bronze Age—the third civilizational stage after the Paleolithic and Neolithic—and as the initial phase of ancient Chinese civilization and the germinating phase of science and technology.",
    "high",
    ["04-knowledge/units/terms/qingtong-shidai.md"],
    "断言取 L609 与 L634，两处相隔较远，记 bounded。L609 的“先秦三代”与知识链接 L626 的“先秦”不完全同义：后者含原始社会，前者特指夏商周；本条取 L609 的合称，不把两者等同。来源称前后“长达1800多年”，与公元前2070—前221年的约1849年并不精确吻合，本条保留来源的约数，不另行折算。",
    609, 634, "bounded", [609, 634], ["b0068", "b0071"],
    CH, "章首"))

rows.append(C(
    "claim-0274", "factual_claim",
    "夏燕靖认为，甲骨文应是比较成熟的文字体系；汉字自商代出现之后，发展大致分为从甲骨文字到小篆、从秦汉隶书以下两个阶段，前者属古文字，后者属近代文字。",
    "Xia Yanjing holds that the oracle-bone script should be regarded as a relatively mature writing system. After the emergence of Chinese characters in the Shang, their development falls roughly into two stages: from oracle-bone script to small seal script, and from Qin-Han clerical script onward; the former belongs to ancient writing, the latter to modern writing.",
    "medium",
    ["04-knowledge/units/publications/jiaguwen-bian.md", "04-knowledge/units/terms/li-shu.md"],
    "断言取 L630。来源先说“从目前所能见到的我国最早的商代甲骨文算起，汉字出现约有3000年历史”，据此推断汉字发生更早；又说半坡陶器刻画符号“因无更加确切的证据尚难认可”。本条只取两个阶段与古文字/近代文字的划分，不把3000年写成汉字起源上限，也不把半坡符号写成已确认文字。“近代文字”是来源用语，不等同于现代文字学术语。",
    630, 630, "line", [630], ["b0071"],
    CH, "知识链接：我国早期文字"))

rows.append(C(
    "claim-0275", "evaluative_claim",
    "夏燕靖评价，以容器为主的青铜器是世界青铜器中独树一帜的器皿；中国有铭文青铜器达万余件，且不少是铭文长篇巨制。",
    "Xia Yanjing evaluates vessel-form bronzes as a distinctive category among the world's bronze traditions, noting that China has more than ten thousand inscribed bronzes, many bearing lengthy inscriptions.",
    "medium",
    ["04-knowledge/units/terms/qingtongqi.md"],
    "断言取 L658。“独树一帜”与“万余件”均来自来源的比较性表述；来源称大多数其他地区的青铜器没有铭文或铭文很短，但未给统计范围、著录口径与计数方法。本条保留评价与数量，不把“万余件”写成已独立核验的普查数字，也不把“独树一帜”升格为世界青铜器分类的定论。",
    658, 658, "line", [658], ["b0076"],
    CH, "1. 青铜鼎器与礼制性设计 / 1）青铜器的出现"))

rows.append(C(
    "claim-0276", "factual_claim",
    "夏燕靖指出，空体容器的制作需用合范法；合范法在商周时普遍应用，其工序包括制泥模、翻外范、制内范、合范、浇铸、脱范打磨。",
    "Xia Yanjing states that hollow vessels required piece-mold casting (hefan fa), which was widely used in the Shang and Zhou. The process includes making a clay model, taking outer molds, making an inner mold, assembling the molds, casting, and removing the molds and finishing.",
    "high",
    ["04-knowledge/units/procedures/hefan-fa.md"],
    "断言取 L668。来源详记外范拍泥、按器形切分、做三角榫、内范刮模或另制、子母扣防错位、留浇铸孔等步骤；器物耳部等突出部分另用分铸法。本条只取主工序链，不把分铸法并入合范法，也不把工序写成唯一复原方案。",
    668, 668, "line", [668], ["b0078"],
    CH, "1. 青铜鼎器与礼制性设计 / 2）青铜器的制作工艺 / ① 合范法"))

rows.append(C(
    "claim-0277", "factual_claim",
    "夏燕靖称，司母戊大方鼎通高133厘米、长110厘米、重875千克；据铸痕与坩埚容量推算，铸造至少需一两百名工匠同时操作，加上运输、烧炭、管理人员约需两三百人。",
    "Xia Yanjing records that the Simuwu ding is 133 cm high, 110 cm long, and weighs 875 kg. On the basis of casting seams and crucible capacity, he estimates that at least one to two hundred artisans were needed to work simultaneously, and that with transport, charcoal-burning, and supervisory personnel the total reached about two to three hundred.",
    "medium",
    ["04-knowledge/units/works/simuwu-ding.md", "04-knowledge/units/procedures/hefan-fa.md", "04-knowledge/units/places/wuguancun-tomb.md"],
    "断言取 L682。来源只给通高、长与重量，未给宽度；875千克与其余来源的875公斤同值异写。工匠数是据鼎身8块外范、鼎底4块、鼎足各3块及坩埚一次约熔铜12.7千克推算，不是直接考古证据；`works/simuwu-ding.md` 另记各册对腹范数与鼎耳接铸/分铸的复原存在分歧，本条不择一而定。",
    682, 682, "line", [682], ["b0080"],
    CH, "1. 青铜鼎器与礼制性设计 / 2）青铜器的制作工艺 / ③ 大件铸造"))

rows.append(C(
    "claim-0278", "historiographic_claim",
    "夏燕靖指出，学界对失蜡法是西域传入还是植根本土存在两种看法；他并称新近考古发掘证明，我国春秋时期采用的失蜡法实为中原的古老技术，曾侯乙尊盘、淅川铜禁等透空附饰可证。",
    "Xia Yanjing notes two competing views on whether lost-wax casting was introduced from the Western Regions or originated locally. He further reports that recent archaeological discoveries prove the lost-wax casting used in China during the Spring and Autumn period was in fact an ancient Central Plains technique, as evidenced by the openwork ornaments of the Zenghouyi zun-pan and the Xichuan bronze altar.",
    "medium",
    ["04-knowledge/units/procedures/lost-wax-casting.md", "04-knowledge/units/procedures/fenshi-fa.md", "04-knowledge/units/works/zenghouyi-zunpan.md", "04-knowledge/units/places/xichuan-xiasi-chumu.md"],
    "断言取 L688。来源并列西域传入说与本土说，随后以1977年随县曾侯乙尊盘、1979年淅川铜禁等论证本土说；“证明”是来源的判断，证据主要是器形、纹饰与技术风格的比较，未给合金成分、年代测定或工艺实验。曾侯乙墓属战国初期，来源却称“春秋时期采用的失蜡法”，时代表述不完全一致；本条保留“春秋时期”与例证时代的张力，不把本土说写成学界定论。",
    688, 688, "line", [688], ["b0082"],
    CH, "1. 青铜鼎器与礼制性设计 / 知识链接：失蜡法的西域传入与本土既有技术的争辩"))

rows.append(C(
    "claim-0279", "interpretive_claim",
    "夏燕靖认为，商早期鼎、斝等柱状足呈锥状足并与器腹相通，是因为当时还没有掌握对范芯浇铸全封闭的技术。",
    "Xia Yanjing argues that the conical, hollow legs of early Shang ding and jia, which open into the vessel body, are explained by the fact that craftsmen had not yet mastered the technique of casting a fully enclosed mold core.",
    "medium",
    ["04-knowledge/units/procedures/hefan-fa.md", "04-knowledge/units/terms/ding.md"],
    "断言取 L736。来源由器物外形推定技术限制，未给范芯结构复原、浇铸实验或失败铸件；这是因果解释而非直接观察，故路由 interpretive。“柱状足呈锥状足”保留来源的并置表述，不改写为单一的“锥形足”。",
    736, 736, "line", [736], ["b0085"],
    CH, "1. 青铜鼎器与礼制性设计 / 5）形制设计"))

rows.append(C(
    "claim-0280", "historiographic_claim",
    "夏燕靖把青铜器造型与装饰的变化分为商早期、殷商期、西周期和春秋期四个阶段：商早期形制简单，爵、觚、斝成套酒器已出现，鼎、斝等柱状足呈锥状并与器腹相通；殷商早期仍有陶器特征，后期造型庄严典重、全身施饰；西周晚期至春秋中期造型纹饰日趋简约，带状花纹增多；春秋晚期至战国初期进入衰落期，青铜器世俗化、轻便适用、质薄形巧，纹饰出现狩猎、习射、采桑、宴乐、攻战等生活图案。",
    "Xia Yanjing divides changes in bronze vessel form and decoration into four phases: early Shang, Yin-Shang, Western Zhou, and Spring and Autumn. In the early Shang, forms were relatively simple, sets of jue, gu, and jia wine vessels had appeared, and the legs of ding and jia were conical and open into the body. In the early Yin-Shang, vessels still retained pottery-like features; in the late Yin-Shang they became solemn and heavy, with all-over decoration. From the late Western Zhou to the mid-Spring and Autumn, forms and ornament grew simpler and banded patterns increased. From the late Spring and Autumn to the early Warring States, bronze vessels entered a decline phase, becoming secular, light, practical, thin-walled, and cleverly formed, with hunting, archery, mulberry-picking, feasting, and battle scenes appearing in decoration.",
    "medium",
    ["04-knowledge/units/terms/qingtongqi.md", "04-knowledge/units/works/simuwu-ding.md", "04-knowledge/units/works/lianhe-fanghu.md", "04-knowledge/units/terms/ding.md"],
    "断言取 L736-L740，记 bounded。来源称“四个时期的转变”，但后两期实际写作“西周晚期至春秋中期”与“春秋晚期至战国初期”，并不与“西周期”“春秋期”完全对齐；“殷商期”内部又分早期与后期。本条保留来源的分期框架与内部不齐，不把它整理成四个等长阶段，也不把“衰落期”写成价值判断。",
    736, 740, "bounded", [736, 738, 740], ["b0085"],
    CH, "1. 青铜鼎器与礼制性设计 / 5）形制设计"))

rows.append(C(
    "claim-0281", "interpretive_claim",
    "夏燕靖指出，造车需要木工、金工、漆工、皮革工等多种工匠协作；造车水平的提高反映当时手工业技术的发展与分工的细密。",
    "Xia Yanjing notes that chariot making required cooperation among carpenters, metalworkers, lacquerers, leatherworkers, and other artisans; the improvement of chariot manufacture reflects the development of handicraft technology and the refinement of the division of labor.",
    "medium",
    ["04-knowledge/units/terms/xianqin-mache.md", "04-knowledge/units/places/yinxu.md"],
    "断言取 L914。来源由西周车制、《诗经》车马材料与车马坑遗存归结，未逐件列出木、金、漆、皮革各工种的分工清单；“反映”是作者的推论，故路由 interpretive。`terms/xianqin-mache.md` 另引《考工记》“一器而工聚焉者，车为多”记车人、轮人、舆人、辀人的分工，可与本条互补，但两者所据文献不同，不合并为同一句。",
    914, 914, "line", [914], ["b0101"],
    CH, "3. 交通运输工具的设计规范 / 1）车"))

rows.append(C(
    "claim-0282", "factual_claim",
    "夏燕靖称，十二章纹早在西周时期就是统治者的礼服纹样，后为历代封建帝王所沿用，具有政治意义。",
    "Xia Yanjing states that the twelve ornamental symbols were already used on rulers' ceremonial robes in the Western Zhou and were subsequently continued by successive dynastic emperors, carrying political significance.",
    "medium",
    ["04-knowledge/units/terms/twelve-symbols.md", "04-knowledge/units/terms/mianfu-zhidu.md"],
    "断言取 L997 与 L1005，记 bounded。L997 称十二章纹“早在西周时期就是统治者的礼服”；L1005 的知识链接又说传说虞舜时期已出现、《虞书》为周代史官追述，并称其“具有政治意义”。来源同时保留传说起源与西周礼服两种时间层次，本条以“早在西周”为断言下限，不把虞舜传说写成已证事实；政治意义出自后世解释，不写成西周原义。",
    997, 1005, "bounded", [997, 1005], ["b0114", "b0116"],
    CH, "5. 丝纺织物与服饰艺术设计 / 2）服饰的制式与设计"))

cand_ids = {
    "claim-0273": "cand-02-91", "claim-0274": "cand-02-93",
    "claim-0275": "cand-02-102", "claim-0276": "cand-02-96",
    "claim-0277": "cand-02-98", "claim-0278": "cand-02-97",
    "claim-0279": "cand-02-101", "claim-0280": "cand-02-146",
    "claim-0281": "cand-02-106", "claim-0282": "cand-02-110",
}
for r in rows:
    r["source"]["candidate_id"] = DOC + ":" + cand_ids[r["claim_id"]]

patches = [
    ("claim-0052", "cand-02-92", 611, 611, "line", [611], ["b0068"]),
    ("claim-0054", "cand-02-94", 652, 652, "line", [652], ["b0075"]),
    ("claim-0055", "cand-02-95", 656, 656, "line", [656], ["b0076"]),
    ("claim-0056", "cand-02-99", 708, 708, "line", [708], ["b0083"]),
    ("claim-0057", "cand-02-100", 710, 710, "line", [710], ["b0083"]),
    ("claim-0058", "cand-02-145", 718, 718, "line", [718], ["b0084"]),
    ("claim-0061", "cand-02-147", 876, 876, "line", [876], ["b0096"]),
    ("claim-0062", "cand-02-103", 882, 882, "line", [882], ["b0097"]),
    ("claim-0063", "cand-02-104", 905, 905, "line", [905], ["b0101"]),
    ("claim-0064", "cand-02-105", 907, 907, "line", [907], ["b0101"]),
    ("claim-0066", "cand-02-107", 950, 950, "line", [950], ["b0106"]),
    ("claim-0067", "cand-02-108", 957, 957, "line", [957], ["b0107"]),
    ("claim-0069", "cand-02-109", 967, 983, "bounded", [967, 983], ["b0110", "b0112"]),
]

patch_rows = []
for claim_id, short, start, end, kind, key_lines, blocks in patches:
    patch_rows.append({
        "claim_id": claim_id,
        "candidate_id": DOC + ":" + short,
        "corroborating_span": {
            "doc_id": DOC,
            "source_file": SRC,
            "line_start": start,
            "line_end": end,
            "span_kind": kind,
            "key_lines": key_lines,
            "block_ids": blocks,
            "chapter": CH,
            "section": "cross-edition corroboration",
            "candidate_id": DOC + ":" + short,
        },
    })

(ROOT / "_zn_cl4a_rows.json").write_text(
    json.dumps(rows, ensure_ascii=False, indent=1), encoding="utf-8")
(ROOT / "_zn_cl4a_patch.json").write_text(
    json.dumps(patch_rows, ensure_ascii=False, indent=1), encoding="utf-8")
print(json.dumps({
    "rows": len(rows), "patches": len(patch_rows),
    "ids": [r["claim_id"] for r in rows],
    "candidates": sorted(cand_ids.values()) + sorted(p["candidate_id"].split(":")[1] for p in patch_rows),
}, ensure_ascii=False))
