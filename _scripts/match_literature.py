# -*- coding: utf-8 -*-
"""Match books listed in 中国设计史相关文献总汇.md against the PDF library.

Usage:
    python match_literature.py            # preview only
    python match_literature.py --copy     # copy matched PDFs
"""
import os
import shutil
import sys

SRC = r"D:\《现当代设计史》\参考文献PDF"
DST = r"D:\中国设计史研究\00-基础文献"

# (section, ref_ids, author, title, year, match_key, dest_stem, note)
# section: folder name
S1 = "01-对象层_中国设计造物"
S2 = "02-视角层_中国学者世界设计史"
S3 = "03-接受层_外来文本中译"
S4 = "04-方法层_去殖民与全球设计史"
S5 = "05-结构层_全球史与经济史"
S6 = "06-区域层_东亚日本"
S7 = "07-外围参照"

WORKS = [
    # ---------- 对象层 ----------
    (S1, "B511", "赵农", "中国艺术设计史", "2004", "中国艺术设计史 (赵农)", "B511_赵农_中国艺术设计史_2004", ""),
    (S1, "B477", "夏燕靖", "中国艺术设计史", "2010", "中国艺术设计史 (夏燕靖", "B477_夏燕靖_中国艺术设计史_2010", ""),
    (S1, "B476", "夏燕靖", "中国艺术设计史（升级版）", "2016", "中国艺术设计史 升级版", "B476_夏燕靖_中国艺术设计史（升级版）_2016", ""),
    (S1, "B472", "周博", "断裂与绵延：中国现代设计史研究", "2023", "周博：《断裂与绵延", "B472_周博_断裂与绵延_2023", ""),
    (S1, "B500", "沈榆", "观念的演进：中国现代设计史", "2021", "观念的演进_中国现代设计史", "B500_沈榆_观念的演进_2021", ""),
    (S1, "B493", "杭间", "中国工艺美学史（第三版修订本）", "2018", "中国工艺美学史", "B493_杭间_中国工艺美学史（第三版修订本）_2018", ""),
    (S1, "B494", "杭间", "手艺的思想（修订版）", "2017", "手艺的思想", "B494_杭间_手艺的思想（修订版）_2017", ""),
    (S1, "B491", "李砚祖", "造物之美：产品设计的艺术与文化", "2000", "造物之美", "B491_李砚祖_造物之美_2000", ""),
    (S1, "B496", "柳冠中", "事理学方法论", "2019", "事理学方法论", "B496_柳冠中_事理学方法论_2019", ""),
    (S1, "B497", "柳冠中", "设计方法论", "", "设计方法论 (柳冠中)", "B497_柳冠中_设计方法论", ""),
    (S1, "B512", "赵江洪", "设计艺术的含义", "1999", "设计艺术的含义", "B512_赵江洪_设计艺术的含义_1999", ""),
    (S1, "B471", "周博", "中国现代文字设计图史", "2017", "中国现代文字设计图史", "B471_周博_中国现代文字设计图史_2017", ""),
    (S1, "B492", "杭间、靳埭强、胡恩威", "包豪斯道路：历史、遗泽、世界与中国", "2014", "包豪斯道路", "B492_杭间等_包豪斯道路_2014", ""),
    (S1, "B089", "Craig Clunas", "Superfluous Things", "1991", "Superfluous Things", "B089_Clunas_Superfluous Things_1991", ""),
    (S1, "B289", "Victor Margolin", "World History of Design, Vol. 2", "2015", "World History of Design World War I to World War II", "B289_Margolin_World History of Design Vol.2_2015", ""),
    (S1, "B103", "Dennis P. Doordan (ed.)", "Design History: An Anthology", "", "Design History An Anthology", "B103_Doordan_Design History An Anthology", ""),
    (S1, "B153", "Robert Finlay", "The Pilgrim Art", "2010", "The pilgrim art", "B153_Finlay_The Pilgrim Art_2010", ""),
    (S1, "B168", "Giorgio Riello", "Cotton: The Fabric That Made the Modern World", "2013", "Cotton The Fabric That Made the Modern World", "B168_Riello_Cotton_2013", ""),
    (S1, "B383", "S. J. Vainker", "Chinese Pottery and Porcelain", "1991", "Chinese pottery and porcelain", "B383_Vainker_Chinese Pottery and Porcelain_1991", ""),
    (S1, "B147", "Emmanuel Cooper", "Ten Thousand Years of Pottery", "", "Ten Thousand Years of Pottery", "B147_Cooper_Ten Thousand Years of Pottery", ""),
    (S1, "B180", "John Guy", "Woven Cargoes", "1998", "Woven cargoes", "B180_Guy_Woven Cargoes_1998", ""),
    (S1, "B073", "Benton, Benton, Wood (eds.)", "Art Deco 1910–1939", "2003", "Art Deco 1910", "B073_Benton_Art Deco 1910-1939_2003", ""),
    (S1, "B164", "Geoffrey & Susan Jellicoe", "The Landscape of Man", "1975", "The landscape of man", "B164_Jellicoe_The Landscape of Man_1975", ""),
    # ---------- 视角层 ----------
    (S2, "B482", "张夫也", "外国现代设计史", "2009", "外国现代设计史", "B482_张夫也_外国现代设计史_2009", ""),
    (S2, "B468", "何人可", "工业设计史（第4版）", "2010", "工业设计史(何人可第四版)", "B468_何人可_工业设计史（第4版）_2010", ""),
    (S2, "B513", "邵宏", "西方设计：一部为生活制作艺术的历史", "2010", "西方设计一部为生活制作艺术的历史", "B513_邵宏_西方设计_2010", ""),
    # ---------- 接受层 ----------
    (S3, "B480", "Nikolaus Pevsner", "Pioneers of Modern Design（英文原版，非2019中译）", "", "Pioneers of modern design", "B480_Pevsner_Pioneers of Modern Design_英文原版", "文档所据为2019年中译（2004重订版）；库中仅有英文原版"),
    (S3, "B515", "Adrian Forty", "Objects of Desire（英文原版，非2001中译）", "1986", "Objects of desire", "B515_Forty_Objects of Desire_英文原版1986", "文档所据为2001年中译；库中仅有1986年英文版"),
    (S3, "B065", "Victor Margolin & Richard Buchanan (eds.)", "The Idea of Design（英文原版，非2018中译）", "", "The idea of design", "B065_Margolin & Buchanan_The Idea of Design_英文原版", "文档所据为2018年中译《设计的观念》；库中仅有英文原版"),
    (S3, "B509", "彭妮·斯帕克", "唯有粉红：审美品位的性别政治学", "2018", "唯有粉红", "B509_斯帕克_唯有粉红_2018", ""),
    (S3, "B462", "良品计划", "MUJI 無印良品", "2010", "MUJI 無印良品", "B462_良品计划_MUJI 無印良品_2010", ""),
    # ---------- 方法层 ----------
    (S4, "B139", "Elizabeth (Dori) Tunstall", "Decolonizing Design", "", "Decolonizing Design", "B139_Tunstall_Decolonizing Design", ""),
    (S4, "B031／B032", "Arturo Escobar", "Designs for the Pluriverse", "2018", "Designs for the Pluriverse", "B031_Escobar_Designs for the Pluriverse_2018", ""),
    (S4, "P044", "Tlostanova et al.", "Border Thinking and Disidentification", "", "Border thinking and disidentification", "P044_Tlostanova_Border Thinking and Disidentification", ""),
    (S4, "B461", "Zeynep Çelik", "Displaying the Orient", "", "Displaying the Orient", "B461_Celik_Displaying the Orient", ""),
    (S4, "B038", "Arnold J. Bauer", "Goods, Power, History", "", "Goods, power, history", "B038_Bauer_Goods, Power, History", ""),
    (S4, "B209", "Jeremy Prestholdt", "Domesticating the World", "", "Domesticating the World", "B209_Prestholdt_Domesticating the World", ""),
    (S4, "B019", "Ami Ayalon", "The Arabic Print Revolution", "", "The Arabic Print Revolution", "B019_Ayalon_The Arabic Print Revolution", ""),
    (S4, "P030", "Kenneth Frampton", "Towards a Critical Regionalism: Six Points", "", "kenneth-frampton-towards", "P030_Frampton_Six Points towards a Critical Regionalism", ""),
    # ---------- 结构层 ----------
    (S5, "B258", "Kenneth Pomeranz", "The Great Divergence", "", "The Great Divergence", "B258_Pomeranz_The Great Divergence", ""),
    (S5, "B483", "文一", "伟大的中国工业革命", "", "伟大的中国工业革命", "B483_文一_伟大的中国工业革命", ""),
    (S5, "B040", "Sven Beckert", "Empire of Cotton", "2014", "Empire of Cotton", "B040_Beckert_Empire of Cotton_2014", ""),
    (S5, "B304", "Maxine Berg", "Luxury and Pleasure in Eighteenth-Century Britain", "2007", "Luxury and Pleasure in Eighteenth-Century Britain", "B304_Berg_Luxury and Pleasure_2007", ""),
    (S5, "B131", "Maxine Berg", "The Age of Manufactures, 1700–1820", "", "The Age of Manufactures", "B131_Berg_The Age of Manufactures 1700-1820", ""),
    (S5, "B189", "Eric Hobsbawm", "The Age of Revolution 1789–1848", "", "Age of Revolution 1789-1848", "B189_Hobsbawm_Age of Revolution 1789-1848", ""),
    (S5, "B484", "L. S. Stavrianos", "全球通史：1500年以后的世界", "2001", "《全球通史-1500年以后的世界》", "B484_Stavrianos_全球通史_1500年以后的世界", ""),
    # ---------- 区域层 ----------
    (S6, "B197", "James H. Fraser & Steven Heller", "Japanese Modern Graphic Design Between the Wars", "1996", "Japanese Modern Graphic Design Between the Wars", "B197_Fraser & Heller_Japanese Modern Graphic Design", ""),
    (S6, "B318", "柳宗悦", "The Unknown Craftsman", "", "The unknown craftsman", "B318_Yanagi_The Unknown Craftsman", ""),
    (S6, "B293", "Marius B. Jansen", "The Making of Modern Japan", "2000", "The Making of Modern Japan", "B293_Jansen_The Making of Modern Japan_2000", ""),
    (S6, "B242", "谷崎润一郎", "In Praise of Shadows（阴翳礼赞）", "", "In Praise of Shadows", "B242_Tanizaki_In Praise of Shadows", ""),
    (S6, "B259", "原研哉", "Designing Design", "", "Designing Design", "B259_Hara_Designing Design", ""),
    # ---------- 外围参照 ----------
    (S7, "W01", "Alain Weill", "The Poster: A Worldwide Survey and History", "2004", "worldwide survey", "W01_Weill_The Poster_2004", ""),
    (S7, "W02", "John F. Pile & Judith Gura", "A History of Interior Design", "", "A History of Interior Design", "W02_Pile & Gura_A History of Interior Design", ""),
    (S7, "W03", "Owen Jones", "The Grammar of Ornament", "", "390-", "W03_Jones_The Grammar of Ornament", ""),
    (S7, "W04", "Philip B. Meggs & Alston W. Purvis", "Meggs' History of Graphic Design", "", "History of Graphic Design", "W04_Meggs_History of Graphic Design", ""),
    (S7, "W05", "Johanna Drucker & Emily McVarish", "Graphic Design History: A Critical Guide", "", "a critical guide (Drucker", "W05_Drucker & McVarish_Graphic Design History", ""),
    (S7, "W06", "Prasannan Parthasarathi", "Why Europe Grew Rich and Asia Did Not", "2011", "Why Europe Grew Rich", "W06_Parthasarathi_Why Europe Grew Rich_2011", ""),
    (S7, "W07", "Mike Davis", "Late Victorian Holocausts", "", "Late Victorian Holocausts", "W07_Davis_Late Victorian Holocausts", ""),
    (S7, "W08", "Fiona Kerlogue", "Batik: Design, Style & History", "2004", "Batik _ design, style", "W08_Kerlogue_Batik_2004", ""),
    (S7, "W09", "周博", "现代设计伦理思想史（边界文献，不立条）", "", "现代设计伦理思想史", "W09_周博_现代设计伦理思想史_2018", "出版年待核；文件名中的2018仅为入库命名"),
]

MISSING = [
    # (section, ref_id, work, year, note)
    (S1, "B516", "霍维国、霍光《中国室内设计史》", "2007", "中国建筑工业出版社"),
    (S1, "B514", "邹德侬、戴路、张向炜《中国现代建筑史》", "2010", "中国建筑工业出版社"),
    (S1, "B469", "刘小羊《中国平面设计史论稿》", "2016", "广西师范大学出版社"),
    (S1, "B465", "万长林《香港平面设计史》", "2012", "贵州教育出版社"),
    (S1, "B485", "曹小鸥《中国现代设计思想：生活、启蒙、变迁》", "2018", "出版项待核"),
    (S1, "B495", "杭间《设计道：中国设计的基本问题》", "2008", "出版项待核"),
    (S1, "B479", "孔铮桢、綦明《物用之美》", "2014", "中国青年出版社"),
    (S1, "B499", "樊进、龙红《中国当代设计全集》第4卷", "2015", "商务印书馆"),
    (S1, "B517", "靳埭强、杭间《中国现代设计与包豪斯》", "2013", "人民美术出版社"),
    (S1, "B505", "林素幸《移動的美術館》", "", "期刊论文"),
    (S1, "B079", "Christopher A. Reed《Gutenberg in Shanghai》", "2004", "UBC Press"),
    (S1, "B326", "Zhang & Parker《China Design Now》", "2008", "V&A Publishing"),
    (S1, "B288", "马格林《世界设计史》第1卷（中译）", "", "库中仅有第2卷英文版"),
    (S1, "B004", "Adamson, Riello, Teasley (eds.)《Global Design History》", "2011", "Routledge"),
    (S1, "B102", "David Raizman《History of Modern Design》3rd", "2023", "Laurence King"),
    (S1, "B425", "Barringer & Flynn (eds.)《Colonialism and the Object》", "1998", "Routledge"),
    (S1, "B265", "Stefan R. Landsberger《Chinese Propaganda Posters》", "1995", "M.E. Sharpe"),

    (S2, "B503", "王受之《世界现代设计史》2版", "2015", ""),
    (S2, "B501", "王受之《世界平面设计史》", "2002", ""),
    (S2, "B486", "朱和平《世界现代设计史》", "2013", ""),
    (S2, "B487", "朱和平《現代設計史》（五南繁体版）", "2012", ""),
    (S2, "B498", "梁梅《世界现代设计史》", "2013", ""),
    (S2, "B481", "张夫也《外国工艺美术史》", "2015", ""),
    (S2, "B508", "胡天璇等《外国近现代设计史》", "2012", ""),
    (S2, "B504", "王树良等《现代设计史（白金版）》", "2012", ""),
    (S2, "B489", "李砚祖《外国设计艺术经典论著选读（上）》", "2006", ""),
    (S2, "B490", "李砚祖《外国设计艺术经典论著选读（下）》", "", "出版项待核"),

    (S3, "B478", "瑞兹曼《现代设计史》2版", "2013", "中译"),
    (S3, "B288／B467／B506", "马格林《世界设计史》第1卷（中译）", "", "库中无"),
    (S3, "B466／B507", "马格林《世界设计史》第2卷（中译）", "2015", "库中仅有英文第2卷"),
    (S3, "B510", "弗赖等《设计与历史的质疑》", "2020", "中译"),
    (S3, "B470", "海勒、切瓦斯特《平面设计200年》", "", ""),
    (S3, "B233", "伍德姆《牛津现代设计词典》", "2007", "英文工具书重印"),
    (S3, "B463", "雷曼《设计教育 教育设计》", "2016", "中译"),

    (S4, "B004／B169", "《Global Design History》", "2011", "Routledge"),
    (S4, "B284", "马格林《A World History of Design…》（2005 论文）", "2005", ""),
    (S4, "B425", "《Colonialism and the Object》", "1998", "Routledge"),
    (S4, "B174", "Kriegel《Grand Designs》", "", ""),
    (S4, "B082", "Pinney《Camera Indica》", "", ""),
    (S4, "B414", "Pater《The Politics of Design》", "", ""),
    (S4, "B422", "Featherstone 等《Problematizing Global Knowledge》", "2006", "期刊专号 23:2–3"),
    (S4, "B245", "Jain《Gods in the Bazaar》", "", ""),

    (S5, "B212", "Mokyr《财富的杠杆》／《The Lever of Riches》", "", ""),

    (S6, "B163", "Weisenfeld《Mavo》", "", ""),
    (S6, "B450", "Wichmann《Japonisme》", "", ""),
    (S6, "B252", "Hiesinger & Fischer《Japanese Design Since 1950》", "", ""),

    (S7, "W10", "Wendy Wong《Hong Kong Comics》", "", "外围参照"),
    (S7, "W11", "Lent & Xu《Comics Art in China》", "", "外围参照"),
    (S7, "W12", "李砚祖、王春雨《室内设计史》", "", "边界文献"),
    (S7, "W13", "Berg 报告所涉瓷器研究（未具名）", "", "无法检索"),
]


def safe(name):
    for a, b in [("/", "／"), ("\\", "＼"), (":", "："), ("?", "？"),
                 ("*", "＊"), ('"', "＂"), ("<", "＜"), (">", "＞"), ("|", "｜")]:
        name = name.replace(a, b)
    return name.strip().rstrip(".")


def main():
    files = [f for f in os.listdir(SRC) if f.lower().endswith(".pdf")]
    used = {}
    rows = []
    problems = []
    for sec, ids, author, title, year, key, stem, note in WORKS:
        hits = [f for f in files if key.lower() in f.lower()]
        if len(hits) == 1:
            src = hits[0]
            if src in used:
                problems.append(f"DUPLICATE SOURCE: {ids} -> {src} (already used by {used[src]})")
            used[src] = ids
            rows.append((sec, ids, author, title, year, src, safe(stem) + ".pdf", note))
        elif not hits:
            problems.append(f"NO MATCH: {ids} {author} {title} [key={key}]")
        else:
            problems.append(f"AMBIGUOUS: {ids} [key={key}] -> {len(hits)} hits:\n    " + "\n    ".join(hits))

    print(f"Source PDFs: {len(files)}")
    print(f"Matched: {len(rows)}")
    print(f"Missing entries (declared): {len(MISSING)}")
    print("=" * 100)
    for r in rows:
        print(f"{r[0][:2]} | {r[1]:<14} | {r[2][:22]:<22} | {r[3][:40]:<40} | {r[4]:<5} | {r[5][:60]}")
    print("=" * 100)
    if problems:
        print("PROBLEMS:")
        for p in problems:
            print(" -", p)
    else:
        print("No matching problems.")

    total = 0
    for r in rows:
        total += os.path.getsize(os.path.join(SRC, r[5]))
    print(f"\nTotal size of matched files: {total/1024/1024/1024:.2f} GB")

    if "--copy" in sys.argv:
        for sec, ids, author, title, year, src, dstname, note in rows:
            folder = os.path.join(DST, sec)
            os.makedirs(folder, exist_ok=True)
            shutil.copy2(os.path.join(SRC, src), os.path.join(folder, dstname))
        print(f"\nCopied {len(rows)} files into {DST}")

        # CSV manifest
        import csv
        csv_path = os.path.join(DST, "00_入库清单.csv")
        with open(csv_path, "w", encoding="utf-8-sig", newline="") as fh:
            w = csv.writer(fh)
            w.writerow(["层", "编号", "著者", "著作", "年份", "入库文件名", "原文件名", "备注"])
            for sec, ids, author, title, year, src, dstname, note in rows:
                w.writerow([sec, ids, author, title, year, dstname, src, note])

        # Markdown index
        sec_names = {
            S1: "一、对象层：中国设计／造物",
            S2: "二、视角层：中国学者写的世界／外国设计史",
            S3: "三、接受层：外来设计文本进入中文",
            S4: "四、方法层：去殖民与全球设计史",
            S5: "五、结构层：全球史与经济史",
            S6: "六、区域层：东亚／日本",
            S7: "七、外围参照与边界文献（不立条）",
        }
        lines = []
        lines.append("# 基础文献入库清单")
        lines.append("")
        lines.append("**生成日期**：2026-10-22  ")
        lines.append(f"**来源库**：`{SRC}`（348 个 PDF）  ")
        lines.append("**依据文档**：`中国设计史相关文献总汇.md`  ")
        lines.append(f"**入库文件**：{len(rows)} 个（按文档层次分七个文件夹）")
        lines.append("")
        lines.append("## 说明")
        lines.append("")
        lines.append("1. 同一著作在文档多层出现时只入一份，放入其首次作为主条目出现的层；其余层在下方索引中互见。")
        lines.append("2. 文件名统一为 `编号_著者_著作_年份.pdf`；与原文件名不完全一致时，以本索引与 `00_入库清单.csv` 的记录为准。")
        lines.append("3. 文档接受层所据为中文译本，而库中仅有英文原版者（B480、B515、B065），已入英文原版并在备注中标明，不能当作中译本使用。")
        lines.append("4. 文件名中的版次、年份来自原文件名，未核版权页；引用前仍须按文档第 10 节的办法核版权页。")
        lines.append("5. 未入库者见第二部分；其中多数为中文专著，来源库未收藏。")
        lines.append("")
        lines.append("## 一、已入库")
        lines.append("")
        for sec in [S1, S2, S3, S4, S5, S6, S7]:
            block = [r for r in rows if r[0] == sec]
            if not block:
                continue
            lines.append(f"### {sec_names[sec]}")
            lines.append("")
            lines.append("| 编号 | 著者 | 著作 | 年份 | 入库文件名 | 备注 |")
            lines.append("| --- | --- | --- | --- | --- | --- |")
            for _, ids, author, title, year, src, dstname, note in block:
                lines.append(f"| {ids} | {author} | {title} | {year} | `{dstname}` | {note} |")
            lines.append("")
        lines.append("## 二、未入库（来源库中未找到）")
        lines.append("")
        lines.append("按文档层次登记；同一著作跨层重复者分别列出，便于逐层核对。")
        lines.append("")
        for sec in [S1, S2, S3, S4, S5, S6, S7]:
            block = [m for m in MISSING if m[0] == sec]
            if not block:
                continue
            lines.append(f"### {sec_names[sec]}")
            lines.append("")
            lines.append("| 编号 | 著作 | 年份 | 出版项／说明 |")
            lines.append("| --- | --- | --- | --- |")
            for _, ids, work, year, note in block:
                lines.append(f"| {ids} | {work} | {year} | {note} |")
            lines.append("")
        lines.append("## 三、跨层互见")
        lines.append("")
        lines.append("- B153《The Pilgrim Art》、B168《Cotton》同属对象层与结构层，文件在 `01-对象层_中国设计造物`。")
        lines.append("- B289 马格林第 2 卷同属对象层与方法层，文件在 `01-对象层_中国设计造物`。")
        lines.append("- B040《Empire of Cotton》、B258《The Great Divergence》、B483《伟大的中国工业革命》、B484《全球通史》同属结构层与 8.2 外围参照，文件在 `05-结构层_全球史与经济史`。")
        lines.append("- 8.2 外围参照中的 Weill、Pile／Gura、Owen Jones、Meggs、Drucker／McVarish、Parthasarathi、Mike Davis、Batik 研究，另置于 `07-外围参照`。")
        lines.append("")
        lines.append("## 四、未处理的项")
        lines.append("")
        lines.append("- 8.2“Berg 报告所涉瓷器研究”未具名，无法检索，未入库。")
        lines.append("- 文档 8.1 所列王受之、张夫也、朱和平、梁梅、邵宏、何人可、胡天璇等，本属视角层，已在 `02-视角层_中国学者世界设计史` 或未入库清单中处理，不另立边界条目。")
        lines.append("- 文档第 11 节提到的帕帕奈克、诺曼，是“本库之外”的举例，不属文档书目，未纳入。")
        lines.append("")
        with open(os.path.join(DST, "00_文献对照索引.md"), "w", encoding="utf-8") as fh:
            fh.write("\n".join(lines))
        print("Wrote 00_文献对照索引.md and 00_入库清单.csv")


if __name__ == "__main__":
    main()
