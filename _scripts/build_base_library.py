# -*- coding: utf-8 -*-
"""按《中国设计史相关文献总汇.md》的 102 个 ref_id 重建基础文献库。

用法：
    python build_base_library.py            # 只预览匹配结果
    python build_base_library.py --copy     # 清空并重建 00-基础文献 的六个层文件夹
    python build_base_library.py --rename   # 只去掉库内文件名中的 ref_id 前缀，不重拷

102 个 ref_id = 六层表内 99 个唯一编号 + B292/B431/B459（马格林第2卷重复文件）。
去重后 94 种著作，全部有 PDF；其中 6 种从《现当代设计史》三目录之外的 D 盘目录补入。
入库文件名不带 ref_id，编号与文件的对应关系见 00_文献对照索引.md。
"""
import csv
import os
import re
import shutil
import sys

ROOT = r"D:\《现当代设计史》"
DST = r"D:\中国设计史研究\00-基础文献"
PERI = r"D:\中国设计史研究\00-基础文献\00-外围参照"

S1 = "01-对象层_中国设计造物"
S2 = "02-视角层_中国学者世界设计史"
S3 = "03-接受层_外来文本中译"
S4 = "04-方法层_去殖民与全球设计史"
S5 = "05-结构层_全球史与经济史"
S6 = "06-区域层_东亚日本"
S7 = "99-外围参照（不计入102）"

SEC_NAMES = {
    S1: "一、对象层：中国设计／造物（40 个 ref_id）",
    S2: "二、视角层：中国学者写的世界／外国设计史（13 个 ref_id）",
    S3: "三、接受层：外来设计文本进入中文（14 个 ref_id）",
    S4: "四、方法层：去殖民与全球设计史（19 个 ref_id）",
    S5: "五、结构层：全球史与经济史（8 个 ref_id）",
    S6: "六、区域层：东亚／日本（8 个 ref_id）",
    S7: "七、外围参照（不计入 102 个 ref_id）",
}

# 每条：sec 层；ids 编号（第一个为主编号，其余为同书重复文件/互见编号）；
# keys 文件名必须全部包含的片段；prefer 命中多条时的优先路径片段；
# exclude 命中后排除的片段；stem 入库文件名（不含 .pdf）；note 备注。
WORKS = [
    # ---------------- 对象层 40 ----------------
    dict(sec=S1, ids=["B511"], author="赵农", title="中国艺术设计史", year="2004",
         keys=["中国艺术设计史 (赵农)"], stem="B511_赵农_中国艺术设计史_2004"),
    dict(sec=S1, ids=["B477"], author="夏燕靖", title="中国艺术设计史", year="2010",
         keys=["中国艺术设计史 (夏燕靖"], stem="B477_夏燕靖_中国艺术设计史_2010"),
    dict(sec=S1, ids=["B476"], author="夏燕靖", title="中国艺术设计史（升级版）", year="2016",
         keys=["中国艺术设计史 升级版"], stem="B476_夏燕靖_中国艺术设计史（升级版）_2016"),
    dict(sec=S1, ids=["B516"], author="霍维国、霍光", title="中国室内设计史（第2版）", year="2007",
         keys=["中国室内设计史 第2版"], stem="B516_霍维国等_中国室内设计史（第2版）_2007",
         note="第2版；初版年份待核"),
    dict(sec=S1, ids=["B514"], author="邹德侬、戴路、张向炜", title="中国现代建筑史", year="2010",
         keys=["中国现代建筑史 (邹德侬)"], stem="B514_邹德侬等_中国现代建筑史_2010"),
    dict(sec=S1, ids=["B469"], author="刘小羊", title="中国平面设计史论稿", year="2016",
         keys=["中国平面设计史论稿"], stem="B469_刘小羊_中国平面设计史论稿_2016"),
    dict(sec=S1, ids=["B465"], author="万长林", title="香港平面设计史", year="2012",
         keys=["香港平面设计史"], stem="B465_万长林_香港平面设计史_2012"),
    dict(sec=S1, ids=["B472"], author="周博", title="断裂与绵延：中国现代设计史研究", year="2023",
         keys=["周博：《断裂与绵延"], stem="B472_周博_断裂与绵延_2023"),
    dict(sec=S1, ids=["B500"], author="沈榆", title="观念的演进：中国现代设计史", year="2021",
         keys=["观念的演进_中国现代设计史"], prefer="参考文献PDF",
         stem="B500_沈榆_观念的演进_2021"),
    dict(sec=S1, ids=["B485"], author="曹小鸥", title="中国现代设计思想：生活、启蒙、变迁", year="2018",
         keys=["中国现代设计思想"], stem="B485_曹小鸥_中国现代设计思想_2018"),
    dict(sec=S1, ids=["B495"], author="杭间", title="设计道：中国设计的基本问题", year="2008",
         keys=["设计道 中国设计的基本问题"], stem="B495_杭间_设计道_2008"),
    dict(sec=S1, ids=["B493"], author="杭间", title="中国工艺美学史（第三版修订本）", year="2018",
         keys=["中国工艺美学史"], stem="B493_杭间_中国工艺美学史（第三版修订本）_2018"),
    dict(sec=S1, ids=["B494"], author="杭间", title="手艺的思想（修订版）", year="2017",
         keys=["手艺的思想"], stem="B494_杭间_手艺的思想（修订版）_2017"),
    dict(sec=S1, ids=["B491"], author="李砚祖", title="造物之美：产品设计的艺术与文化", year="2000",
         keys=["造物之美"], stem="B491_李砚祖_造物之美_2000"),
    dict(sec=S1, ids=["B479"], author="孔铮桢、綦明", title="物用之美：中国设计艺术的历史与理论", year="2014",
         src_path=r"D:\MinerU\物用之美  中国设计艺术的历史与理论 -- 孔铮桢,綦明著 -- 2014, 2014 -- 北京_中国青年出版社 -- isbn13 9787515324098 -- a131177b4355d43c2109c877c262e746 -- Anna’s Archive.pdf",
         stem="B479_孔铮桢等_物用之美_2014", note="库外补入：D:\\MinerU；原三目录未收"),
    dict(sec=S1, ids=["B496"], author="柳冠中", title="事理学方法论", year="2019",
         keys=["事理学方法论"], stem="B496_柳冠中_事理学方法论_2019"),
    dict(sec=S1, ids=["B497"], author="柳冠中", title="设计方法论", year="",
         keys=["设计方法论 (柳冠中)"], stem="B497_柳冠中_设计方法论"),
    dict(sec=S1, ids=["B512"], author="赵江洪", title="设计艺术的含义", year="1999",
         keys=["设计艺术的含义"], stem="B512_赵江洪_设计艺术的含义_1999"),
    dict(sec=S1, ids=["B471"], author="周博", title="中国现代文字设计图史", year="2017",
         keys=["中国现代文字设计图史"], stem="B471_周博_中国现代文字设计图史_2017"),
    dict(sec=S1, ids=["B499"], author="樊进、龙红（主编）", title="中国当代设计全集 第4卷 平面类编 图案篇", year="2015",
         keys=["中国当代设计全集 第4卷"], stem="B499_樊进等_中国当代设计全集第4卷_2015"),
    dict(sec=S1, ids=["B492"], author="杭间、靳埭强、胡恩威", title="包豪斯道路：历史、遗泽、世界与中国", year="2014",
         keys=["包豪斯道路"], stem="B492_杭间等_包豪斯道路_2014"),
    dict(sec=S1, ids=["B517"], author="靳埭强、杭间（主编）", title="中国现代设计与包豪斯", year="2013",
         keys=["中国现代设计与包豪斯"], stem="B517_靳埭强等_中国现代设计与包豪斯_2013"),
    dict(sec=S1, ids=["B505"], author="林素幸", title="移动的美术馆：20世纪初中国的书籍装帧设计与商业美术", year="",
         keys=["移动的美术馆"], stem="B505_林素幸_移动的美术馆",
         note="期刊论文，无独立版权页"),
    dict(sec=S1, ids=["B089"], author="Craig Clunas", title="Superfluous Things: Material Culture and Social Status in Early Modern China", year="1991",
         keys=["Superfluous Things"], stem="B089_Clunas_Superfluous Things_1991"),
    dict(sec=S1, ids=["B079"], author="Christopher A. Reed", title="Gutenberg in Shanghai: Chinese Print Capitalism, 1876–1937", year="2004",
         keys=["Gutenberg in Shanghai"], stem="B079_Reed_Gutenberg in Shanghai_2004"),
    dict(sec=S1, ids=["B326"], author="Zhang Hongxing & Parker", title="China Design Now", year="2008",
         keys=["China design now"], stem="B326_Zhang & Parker_China Design Now_2008"),
    dict(sec=S1, ids=["B288"], author="维克多·马格林", title="世界设计史（第1卷：史前至一战）", year="2020",
         keys=["世界设计史1：史前至一战"], stem="B288_马格林_世界设计史（第1卷）_2020",
         note="中译本；B467、B506 为同书重复文件；出版年据报告，未核版权页"),
    dict(sec=S1, ids=["B289"], author="Victor Margolin", title="World History of Design, Vol. 2: World War I to World War II", year="2015",
         keys=["World History of Design World War I to World War II"],
         stem="B289_Margolin_World History of Design Vol.2_2015",
         note="英文第2卷；B292、B431、B459 为同书重复文件，以 B289 为准"),
    dict(sec=S1, ids=["B004"], author="Glenn Adamson, Giorgio Riello, Sarah Teasley (eds.)", title="Global Design History", year="2011",
         keys=["Global Design History"], stem="B004_Adamson et al_Global Design History_2011",
         note="B169 为同书重复文件"),
    dict(sec=S1, ids=["B102"], author="David Raizman", title="History of Modern Design (3rd ed.)", year="2023",
         keys=["(NEW)History of Modern Design Third Edition"], stem="B102_Raizman_History of Modern Design_3rd_2023"),
    dict(sec=S1, ids=["B103"], author="Dennis P. Doordan (ed.)", title="Design History: An Anthology", year="",
         keys=["Design History An Anthology"], stem="B103_Doordan_Design History An Anthology"),
    dict(sec=S1, ids=["B153"], author="Robert Finlay", title="The Pilgrim Art: Cultures of Porcelain in World History", year="2010",
         keys=["The pilgrim art"], stem="B153_Finlay_The Pilgrim Art_2010",
         note="对象层与结构层互见"),
    dict(sec=S1, ids=["B168"], author="Giorgio Riello", title="Cotton: The Fabric That Made the Modern World", year="2013",
         keys=["Cotton The Fabric That Made the Modern World"], stem="B168_Riello_Cotton_2013",
         note="对象层与结构层互见"),
    dict(sec=S1, ids=["B383"], author="S. J. Vainker", title="Chinese Pottery and Porcelain: From Prehistory to the Present", year="1991",
         keys=["Chinese pottery and porcelain"], stem="B383_Vainker_Chinese Pottery and Porcelain_1991"),
    dict(sec=S1, ids=["B147"], author="Emmanuel Cooper", title="Ten Thousand Years of Pottery", year="",
         keys=["Ten Thousand Years of Pottery"], stem="B147_Cooper_Ten Thousand Years of Pottery"),
    dict(sec=S1, ids=["B180"], author="John Guy", title="Woven Cargoes: Indian Textiles in the East", year="1998",
         keys=["Woven cargoes"], stem="B180_Guy_Woven Cargoes_1998"),
    dict(sec=S1, ids=["B073"], author="Charlotte Benton, Tim Benton, Ghislaine Wood (eds.)", title="Art Deco 1910–1939", year="2003",
         keys=["Art Deco 1910"], stem="B073_Benton_Art Deco 1910-1939_2003"),
    dict(sec=S1, ids=["B164"], author="Geoffrey & Susan Jellicoe", title="The Landscape of Man", year="1975",
         keys=["The landscape of man"], stem="B164_Jellicoe_The Landscape of Man_1975"),
    dict(sec=S1, ids=["B425"], author="Tim Barringer & Tom Flynn (eds.)", title="Colonialism and the Object: Empire, Material Culture and the Museum", year="1998",
         keys=["Colonialism and the object"], stem="B425_Barringer & Flynn_Colonialism and the Object_1998",
         note="对象层与方法层互见"),
    dict(sec=S1, ids=["B265"], author="Stefan R. Landsberger", title="Chinese Propaganda Posters: From Revolution to Modernization", year="1995",
         keys=["Chinese propaganda posters"], stem="B265_Landsberger_Chinese Propaganda Posters_1995"),

    # ---------------- 视角层 13 ----------------
    dict(sec=S2, ids=["B503"], author="王受之", title="世界现代设计史（第2版）", year="2015",
         keys=["世界现代设计史（王受之2015第二版）"], prefer="基础文献\\现代设计\\国内",
         stem="B503_王受之_世界现代设计史（第2版）_2015",
         note="出版年据目录/清单，未核版权页"),
    dict(sec=S2, ids=["B501"], author="王受之", title="世界平面设计史", year="2002",
         keys=["世界平面设计史 (王受之)"], stem="B501_王受之_世界平面设计史_2002"),
    dict(sec=S2, ids=["B486"], author="朱和平", title="世界现代设计史", year="2013",
         keys=["世界现代设计史 (朱和平编著"], stem="B486_朱和平_世界现代设计史_2013"),
    dict(sec=S2, ids=["B487"], author="朱和平", title="现代设计史（五南繁体版）", year="2012",
         keys=["现代设计史 -- 朱和平主编 -- 2012"], stem="B487_朱和平_现代设计史（五南版）_2012"),
    dict(sec=S2, ids=["B498"], author="梁梅", title="世界现代设计史", year="2013",
         keys=["世界现代设计史 梁梅著"], stem="B498_梁梅_世界现代设计史_2013"),
    dict(sec=S2, ids=["B481"], author="张夫也", title="外国工艺美术史（第2版）", year="2015",
         keys=["外国工艺美术史（第2版）"], stem="B481_张夫也_外国工艺美术史（第2版）_2015"),
    dict(sec=S2, ids=["B482"], author="张夫也", title="外国现代设计史", year="2009",
         keys=["外国现代设计史"], prefer="2009 -- 北京：高等教育出版社",
         stem="B482_张夫也_外国现代设计史_2009", note="选用2009年高等教育出版社版"),
    dict(sec=S2, ids=["B468"], author="何人可", title="工业设计史（第4版）", year="2010",
         keys=["工业设计史(何人可第四版)"], prefer="参考文献PDF",
         stem="B468_何人可_工业设计史（第4版）_2010"),
    dict(sec=S2, ids=["B508"], author="胡天璇、曾山、王庆", title="外国近现代设计史", year="2012",
         keys=["外国近现代设计史"], stem="B508_胡天璇等_外国近现代设计史_2012"),
    dict(sec=S2, ids=["B504"], author="王树良、张玉花（主编）", title="现代设计史（白金版）", year="2012",
         keys=["现代设计史 白金版"], stem="B504_王树良等_现代设计史（白金版）_2012"),
    dict(sec=S2, ids=["B513"], author="邵宏（主编）", title="西方设计：一部为生活制作艺术的历史", year="2010",
         keys=["西方设计一部为生活制作艺术的历史"], stem="B513_邵宏_西方设计_2010"),
    dict(sec=S2, ids=["B489"], author="李砚祖（编）", title="外国设计艺术经典论著选读（上）", year="2006",
         keys=["外国设计艺术经典论著选读 上"], stem="B489_李砚祖_外国设计艺术经典论著选读（上）_2006"),
    dict(sec=S2, ids=["B490"], author="李砚祖（编）", title="外国设计艺术经典论著选读（下）", year="",
         keys=["外国设计艺术经典论著选读 下"], stem="B490_李砚祖_外国设计艺术经典论著选读（下）",
         note="无版权页，出版项待核"),

    # ---------------- 接受层 14 ----------------
    dict(sec=S3, ids=["B480"], author="尼古拉斯·佩夫斯纳", title="现代设计的先驱者：从威廉·莫里斯到沃尔特·格罗皮乌斯", year="2019",
         keys=["现代设计的先驱者"], stem="B480_佩夫斯纳_现代设计的先驱者_2019",
         note="中译本，据2004重订版；与 B324（1949第2版）、B353（1960修订版）版次不同"),
    dict(sec=S3, ids=["B515"], author="阿德里安·福蒂", title="欲求之物：1750年以来的设计与社会", year="2001",
         keys=["欲求之物"], stem="B515_福蒂_欲求之物_2001",
         note="中译本；库中另有1986年英文原版可参"),
    dict(sec=S3, ids=["B478"], author="大卫·瑞兹曼", title="现代设计史（第2版）", year="2013",
         keys=["现代设计史  第2版 -- (美)大卫·瑞兹曼"], exclude="(OCR)",
         stem="B478_瑞兹曼_现代设计史（第2版）_2013",
         note="中译本；选用非OCR版"),
    dict(sec=S3, ids=["B467"], author="维克多·马格林", title="世界设计史（第1卷）", year="2020",
         keys=[], alias_of="B288", note="B288 的重复文件，见 B288 行"),
    dict(sec=S3, ids=["B506"], author="维克多·马格林", title="世界设计史（第1卷）", year="2020",
         keys=[], alias_of="B288", note="B288 的重复文件，见 B288 行"),
    dict(sec=S3, ids=["B466", "B507"], author="维克多·马格林", title="世界设计史（第2卷）", year="2015",
         keys=["世界设计史2"], stem="B466_马格林_世界设计史（第2卷）_2015",
         note="中译本；B507 为同书重复文件；出版年据报告，未核版权页"),
    dict(sec=S3, ids=["B065"], author="维克多·马格林、理查德·布坎南（编）", title="设计的观念：设计问题读本", year="2018",
         src_path=r"D:\维克多-个案\00-PDF\设计理论研究系列  凤凰文库  设计的观念  设计问题读本 -- (美)维克多·马格林(Victor Margolin),(美)理查德·布坎南(Richard Buchanan)编 ; -- Di 1 ban, Nan jing, 2018 -- 南京：江苏凤凰美术出版社 -- isbn13 9787558032486 -- 53bc70c1e66347d6efac7db5cfe1b219 -- Anna’s Archive.pdf",
         stem="B065_马格林等_设计的观念_2018",
         note="中译本，2018年江苏凤凰美术出版社；库外补入：D:\\维克多-个案\\00-PDF；英文原版可另在参考文献PDF查阅"),
    dict(sec=S3, ids=["B509"], author="彭妮·斯帕克", title="唯有粉红：审美品位的性别政治学", year="2018",
         keys=["唯有粉红"], stem="B509_斯帕克_唯有粉红_2018"),
    dict(sec=S3, ids=["B510"], author="托尼·弗赖、克莱夫·迪尔诺特、苏珊·斯图尔特", title="设计与历史的质疑", year="2020",
         src_path=r"D:\补充文献\设计与历史的质疑 = Design and the question of history -- Tony Fry; Clive Dilnot; Susan Catherine Huston Stewart -- Feng huang wen ku ： she ji li lun yan jiu -- isbn13 9787558064906 -- 11850cb2716e09b8a89d729c.pdf",
         stem="B510_弗赖等_设计与历史的质疑_2020", note="库外补入：D:\\补充文献（顶层）；原三目录未收"),
    dict(sec=S3, ids=["B470"], author="史蒂文·海勒、西摩·切瓦斯特", title="平面设计200年（第4版）", year="",
         keys=["(NEW)平面设计200年"], stem="B470_海勒等_平面设计200年",
         note="第4版中译；无版权页，出版项待核"),
    dict(sec=S3, ids=["B233"], author="Jonathan M. Woodham", title="Dictionary of Modern Design", year="2007",
         keys=["DICTIONARY OF MODERN DESIGN"], stem="B233_Woodham_Dictionary of Modern Design_2007",
         note="英文工具书"),
    dict(sec=S3, ids=["B463"], author="克劳斯·雷曼", title="设计教育 教育设计", year="2016",
         src_path=r"D:\补充文献\设计教育 教育设计 = Design teaching -- teaching design -- (德)克劳斯·雷曼(Klaus Lehmann)著, 雷曼 Lehmann, Klaus 1934- -- 2016, 2016 -- 江苏凤凰美术出版社 -- isbn13 9787558008603 -- b99285af3a1b04a72bf3e111ec2f3db7 -- Anna’s Archive.pdf",
         stem="B463_雷曼_设计教育 教育设计_2016", note="库外补入：D:\\补充文献（顶层）；原三目录未收"),
    dict(sec=S3, ids=["B462"], author="良品计划", title="MUJI 無印良品", year="2010",
         keys=["MUJI 無印良品"], stem="B462_良品计划_MUJI 無印良品_2010"),

    # ---------------- 方法层 19 ----------------
    dict(sec=S4, ids=["B169"], author="Glenn Adamson et al.", title="Global Design History", year="2011",
         keys=[], alias_of="B004", note="B004 的重复文件，见 B004 行"),
    dict(sec=S4, ids=["B284"], author="Victor Margolin", title="A World History of Design and the History of the World（2005 论文）", year="2005",
         src_path=r"D:\维克多-个案\00-PDF\Margolin, Victor, A World History of Design and the History of the World, 2005.pdf",
         stem="B284_Margolin_A World History of Design and the History of the World_2005",
         note="库外补入：D:\\维克多-个案\\00-PDF；原三目录未收"),
    dict(sec=S4, ids=["B292"], author="Victor Margolin", title="World History of Design, Vol. 2", year="2015",
         keys=[], alias_of="B289", note="B289 的重复文件，见 B289 行"),
    dict(sec=S4, ids=["B431"], author="Victor Margolin", title="World History of Design, Vol. 2", year="2015",
         keys=[], alias_of="B289", note="B289 的重复文件（题名页标明第2卷），见 B289 行"),
    dict(sec=S4, ids=["B459"], author="Victor Margolin", title="World History of Design, Vol. 2", year="2015",
         keys=[], alias_of="B289", note="B289 的重复文件，见 B289 行"),
    dict(sec=S4, ids=["B139"], author="Elizabeth (Dori) Tunstall", title="Decolonizing Design: A Cultural Justice Guidebook", year="",
         keys=["Decolonizing Design"], stem="B139_Tunstall_Decolonizing Design"),
    dict(sec=S4, ids=["B031", "B032"], author="Arturo Escobar", title="Designs for the Pluriverse", year="2018",
         keys=["Designs for the Pluriverse"], stem="B031_Escobar_Designs for the Pluriverse_2018",
         note="以 B031 为工作本；B032 为同书重复文件"),
    dict(sec=S4, ids=["P044"], author="Madina Tlostanova et al.", title="Border Thinking and Disidentification", year="",
         keys=["Border thinking and disidentification"], stem="P044_Tlostanova_Border Thinking and Disidentification"),
    dict(sec=S4, ids=["B461"], author="Zeynep Çelik", title="Displaying the Orient: Architecture of Islam at Nineteenth-Century World's Fairs", year="",
         keys=["Displaying the Orient"], stem="B461_Celik_Displaying the Orient"),
    dict(sec=S4, ids=["B174"], author="Alexis Kriegel", title="Grand Designs: Labor, Empire, and the Museum in Victorian Culture", year="",
         keys=["Grand Designs Labor"], stem="B174_Kriegel_Grand Designs"),
    dict(sec=S4, ids=["B082"], author="Christopher Pinney", title="Camera Indica: The Social Life of Indian Photographs", year="",
         keys=["Camera Indica"], stem="B082_Pinney_Camera Indica"),
    dict(sec=S4, ids=["B038"], author="Arnold J. Bauer", title="Goods, Power, History: Latin America's Material Culture", year="",
         keys=["Goods, power, history"], stem="B038_Bauer_Goods, Power, History"),
    dict(sec=S4, ids=["B209"], author="Jeremy Prestholdt", title="Domesticating the World: African Consumerism and the Genealogies of Globalization", year="",
         keys=["Domesticating the World"], stem="B209_Prestholdt_Domesticating the World"),
    dict(sec=S4, ids=["B019"], author="Ami Ayalon", title="The Arabic Print Revolution: Cultural Production and Mass Readership", year="",
         keys=["The Arabic Print Revolution"], stem="B019_Ayalon_The Arabic Print Revolution"),
    dict(sec=S4, ids=["B414"], author="Ruben Pater", title="The Politics of Design", year="2016",
         src_path=r"D:\补充文献\The Politics of Design： A (Not So) Global Design Manual for -- [writer and designer] Ruben Pater -- 2, 2016 -- Bis B_V_, Uitgeverij (BIS Publishers) -- isbn13 9789063694227 -- 4dac1837ef9eb740ad94c186.pdf",
         stem="B414_Pater_The Politics of Design_2016",
         note="库外补入：D:\\补充文献（顶层）；原三目录未收；2016年第2版"),
    dict(sec=S4, ids=["B422"], author="Mike Featherstone et al. (eds.)", title="Problematizing Global Knowledge (Theory, Culture & Society 23:2–3)", year="2006",
         keys=["Problematizing_Global_Knowledge"], stem="B422_Featherstone_Problematizing Global Knowledge_2006"),
    dict(sec=S4, ids=["B245"], author="Kajri Jain", title="Gods in the Bazaar: The Economies of Indian Calendar Art", year="",
         keys=["Gods in the Bazaar"], stem="B245_Jain_Gods in the Bazaar"),
    dict(sec=S4, ids=["P030"], author="Kenneth Frampton", title="Towards a Critical Regionalism: Six Points for an Architecture of Resistance", year="",
         keys=["kenneth-frampton-towards"], stem="P030_Frampton_Six Points towards a Critical Regionalism"),

    # ---------------- 结构层 8 ----------------
    dict(sec=S5, ids=["B258"], author="Kenneth Pomeranz", title="The Great Divergence", year="",
         keys=["The Great Divergence"], stem="B258_Pomeranz_The Great Divergence"),
    dict(sec=S5, ids=["B483"], author="文一", title="伟大的中国工业革命", year="",
         keys=["伟大的中国工业革命"], stem="B483_文一_伟大的中国工业革命"),
    dict(sec=S5, ids=["B040"], author="Sven Beckert", title="Empire of Cotton: A Global History", year="2014",
         keys=["Empire of Cotton"], stem="B040_Beckert_Empire of Cotton_2014"),
    dict(sec=S5, ids=["B304"], author="Maxine Berg", title="Luxury and Pleasure in Eighteenth-Century Britain", year="2007",
         keys=["Luxury and Pleasure in Eighteenth-Century Britain"], stem="B304_Berg_Luxury and Pleasure_2007"),
    dict(sec=S5, ids=["B212"], author="Joel Mokyr", title="The Lever of Riches", year="",
         keys=["The lever of riches"], stem="B212_Mokyr_The Lever of Riches"),
    dict(sec=S5, ids=["B131"], author="Maxine Berg", title="The Age of Manufactures, 1700–1820", year="",
         keys=["The Age of Manufactures"], stem="B131_Berg_The Age of Manufactures 1700-1820"),
    dict(sec=S5, ids=["B189"], author="Eric Hobsbawm", title="The Age of Revolution 1789–1848", year="",
         keys=["Age of Revolution 1789-1848"], stem="B189_Hobsbawm_Age of Revolution 1789-1848"),
    dict(sec=S5, ids=["B484"], author="L. S. Stavrianos", title="全球通史：1500年以后的世界", year="2001",
         keys=["《全球通史-1500年以后的世界》"], stem="B484_Stavrianos_全球通史_1500年以后的世界",
         note="无独立版权页，出版项待核"),

    # ---------------- 区域层 8 ----------------
    dict(sec=S6, ids=["B163"], author="Gennifer Weisenfeld", title="Mavo: Japanese Artists and the Avant-Garde, 1905–1931", year="",
         keys=["Mavo  Japanese Artists"], stem="B163_Weisenfeld_Mavo"),
    dict(sec=S6, ids=["B197"], author="James H. Fraser & Steven Heller", title="Japanese Modern Graphic Design Between the Wars", year="1996",
         keys=["Japanese Modern Graphic Design Between the Wars"], stem="B197_Fraser & Heller_Japanese Modern Graphic Design"),
    dict(sec=S6, ids=["B318"], author="柳宗悦", title="The Unknown Craftsman: A Japanese Insight into Beauty", year="",
         keys=["The unknown craftsman"], stem="B318_Yanagi_The Unknown Craftsman"),
    dict(sec=S6, ids=["B293"], author="Marius B. Jansen", title="The Making of Modern Japan", year="2000",
         keys=["The Making of Modern Japan"], stem="B293_Jansen_The Making of Modern Japan_2000"),
    dict(sec=S6, ids=["B450"], author="Siegfried Wichmann", title="Japonisme: The Japanese Influence on Western Art since 1858", year="",
         keys=["Japonisme  the Japanese influence"], stem="B450_Wichmann_Japonisme"),
    dict(sec=S6, ids=["B242"], author="谷崎润一郎", title="In Praise of Shadows（阴翳礼赞）", year="",
         keys=["In Praise of Shadows"], stem="B242_Tanizaki_In Praise of Shadows"),
    dict(sec=S6, ids=["B252"], author="Kathryn B. Hiesinger & Felice Fischer", title="Japanese Design: A Survey since 1950", year="",
         keys=["JAPANESE DESIGN A SURVEY SINCE 1950"], stem="B252_Hiesinger & Fischer_Japanese Design since 1950"),
    dict(sec=S6, ids=["B259"], author="原研哉", title="Designing Design", year="",
         keys=["Designing Design"], stem="B259_Hara_Designing Design"),
]

# 外围参照：不计入 102，单独放 00-外围参照
PERIPHERAL = [
    dict(sec=S7, ids=["W01"], author="Alain Weill", title="The Poster: A Worldwide Survey and History", year="2004",
         keys=["worldwide survey"], stem="W01_Weill_The Poster_2004"),
    dict(sec=S7, ids=["W02"], author="John F. Pile & Judith Gura", title="A History of Interior Design", year="",
         keys=["A History of Interior Design"], prefer="(NEW)A History of Interior Design, 5th Edition",
         stem="W02_Pile & Gura_A History of Interior Design", note="优先第5版"),
    dict(sec=S7, ids=["W03"], author="Owen Jones", title="The Grammar of Ornament", year="",
         keys=["390-"], stem="W03_Jones_The Grammar of Ornament"),
    dict(sec=S7, ids=["W04"], author="Philip B. Meggs & Alston W. Purvis", title="Meggs' History of Graphic Design", year="",
         keys=["History of Graphic Design"], prefer="参考文献PDF", stem="W04_Meggs_History of Graphic Design"),
    dict(sec=S7, ids=["W05"], author="Johanna Drucker & Emily McVarish", title="Graphic Design History: A Critical Guide", year="",
         keys=["a critical guide (Drucker"], prefer="参考文献PDF", stem="W05_Drucker & McVarish_Graphic Design History"),
    dict(sec=S7, ids=["W06"], author="Prasannan Parthasarathi", title="Why Europe Grew Rich and Asia Did Not", year="2011",
         keys=["Why Europe Grew Rich"], stem="W06_Parthasarathi_Why Europe Grew Rich_2011"),
    dict(sec=S7, ids=["W07"], author="Mike Davis", title="Late Victorian Holocausts", year="",
         keys=["Late Victorian Holocausts"], stem="W07_Davis_Late Victorian Holocausts"),
    dict(sec=S7, ids=["W08"], author="Fiona Kerlogue", title="Batik: Design, Style & History", year="2004",
         keys=["Batik _ design, style"], stem="W08_Kerlogue_Batik_2004"),
    dict(sec=S7, ids=["W09"], author="周博", title="现代设计伦理思想史", year="",
         keys=["现代设计伦理思想史"], stem="W09_周博_现代设计伦理思想史",
         note="边界文献，不立条；出版年待核"),
]


def safe(name):
    for a, b in [("/", "／"), ("\\", "＼"), (":", "："), ("?", "？"),
                 ("*", "＊"), ('"', "＂"), ("<", "＜"), (">", "＞"), ("|", "｜")]:
        name = name.replace(a, b)
    return name.strip().rstrip(".")


ID_PREFIX = re.compile(r"^[A-Z]\d{2,3}_")


def dest_name(w):
    """入库文件名去掉 ref_id 前缀，只留著者／书名／年份。"""
    return safe(ID_PREFIX.sub("", w["stem"])) + ".pdf"


def all_pdfs():
    out = []
    for dp, _dn, fn in os.walk(ROOT):
        for f in fn:
            if f.lower().endswith(".pdf"):
                out.append(os.path.join(dp, f))
    return out


def disp(src):
    root = os.path.abspath(ROOT) + os.sep
    if os.path.abspath(src).lower().startswith(root.lower()):
        return os.path.relpath(src, ROOT)
    return src


def match_work(w, paths):
    if w.get("src_path"):
        p = w["src_path"]
        return (p if os.path.exists(p) else None), ([p] if os.path.exists(p) else [])
    if w.get("missing"):
        return None, []
    if w.get("alias_of"):
        return None, []
    hits = [p for p in paths
            if all(k.lower() in os.path.basename(p).lower() for k in w["keys"])]
    if w.get("exclude"):
        hits = [p for p in hits if w["exclude"].lower() not in os.path.basename(p).lower()]
    if w.get("prefer"):
        pref = [p for p in hits if w["prefer"].lower() in p.lower()]
        if pref:
            hits = pref
    return (hits[0] if len(hits) == 1 else None), hits


def main():
    paths = all_pdfs()
    rows = []          # 102 register rows
    copies = []        # unique files to copy
    problems = []
    primary_file = {}  # primary id -> (src, destname, srcroot)
    used_src = {}

    for w in WORKS:
        src, hits = match_work(w, paths)
        if w.get("alias_of"):
            pid = w["alias_of"]
            if pid not in primary_file:
                problems.append(f"ALIAS BEFORE PRIMARY: {w['ids']} -> {pid}")
                continue
            src2, destname = primary_file[pid]
            for rid in w["ids"]:
                rows.append(dict(sec=w["sec"], rid=rid, author=w["author"], title=w["title"],
                                 year=w["year"], status="互见", dest=destname,
                                 src=disp(src2), note=w.get("note", "")))
            continue
        if w.get("missing"):
            for i, rid in enumerate(w["ids"]):
                rows.append(dict(sec=w["sec"], rid=rid, author=w["author"], title=w["title"],
                                 year=w["year"], status="缺藏", dest="", src="", note=w.get("note", "")))
            continue
        if src is None:
            problems.append(f"{w['ids'][0]} {w['title']}: {len(hits)} hits")
            for h in hits[:10]:
                problems.append("    " + h)
            for rid in w["ids"]:
                rows.append(dict(sec=w["sec"], rid=rid, author=w["author"], title=w["title"],
                                 year=w["year"], status="匹配异常", dest="", src="", note=w.get("note", "")))
            continue
        if src in used_src:
            problems.append(f"DUPLICATE SOURCE: {w['ids'][0]} -> {src} (also {used_src[src]})")
        used_src[src] = w["ids"][0]
        oldname = safe(w["stem"]) + ".pdf"
        destname = dest_name(w)
        primary_file[w["ids"][0]] = (src, destname)
        copies.append((w["sec"], src, oldname, destname))
        for i, rid in enumerate(w["ids"]):
            rows.append(dict(sec=w["sec"], rid=rid, author=w["author"], title=w["title"],
                             year=w["year"], status=("已入库" if i == 0 else "互见"),
                             dest=destname, src=disp(src),
                             note=w.get("note", "")))

    # 逐个核对 102 行
    ids = [r["rid"] for r in rows]
    print(f"PDF pool: {len(paths)}")
    print(f"Register rows: {len(rows)}  unique ids: {len(set(ids))}")
    print(f"Unique files: {len(copies)}")
    print(f"Missing rows: {sum(1 for r in rows if r['status'] == '缺藏')}")
    print(f"Alias rows: {sum(1 for r in rows if r['status'] == '互见')}")
    print("=" * 110)
    for r in rows:
        print(f"{r['rid']} | {r['sec'][:2]} | {r['status']} | {r['title'][:45]:<45} | {r['dest'][:55]}")
    if problems:
        print("=" * 110)
        print("PROBLEMS")
        for p in problems:
            print(" -", p)

    mode = "copy" if "--copy" in sys.argv else ("rename" if "--rename" in sys.argv else "")
    if not mode:
        return

    peri_rows = []
    if mode == "copy":
        # 重建：只删除本脚本命名的层文件夹
        for sec in [S1, S2, S3, S4, S5, S6]:
            folder = os.path.join(DST, sec)
            if os.path.isdir(folder):
                shutil.rmtree(folder)
            os.makedirs(folder, exist_ok=True)
        legacy = os.path.join(DST, "07-外围参照")
        if os.path.isdir(legacy):
            shutil.rmtree(legacy)
        os.makedirs(PERI, exist_ok=True)

        for sec, src, _oldname, destname in copies:
            shutil.copy2(src, os.path.join(DST, sec, destname))

        # 外围参照单独入库
        for w in PERIPHERAL:
            src, hits = match_work(w, paths)
            if src is None:
                problems.append(f"{w['ids'][0]} {w['title']}: {len(hits)} hits")
                continue
            destname = dest_name(w)
            shutil.copy2(src, os.path.join(PERI, destname))
            peri_rows.append((w, destname, disp(src)))
    else:
        # 只改文件名：去掉 ref_id 前缀，不动内容
        renamed = skipped = 0
        for sec, _src, oldname, destname in copies:
            folder = os.path.join(DST, sec)
            old = os.path.join(folder, oldname)
            new = os.path.join(folder, destname)
            if oldname == destname:
                skipped += 1
                continue
            if os.path.exists(new):
                skipped += 1
                continue
            if not os.path.exists(old):
                problems.append(f"RENAME SOURCE MISSING: {oldname}")
                continue
            os.rename(old, new)
            renamed += 1
        print(f"Renamed {renamed} files, {skipped} unchanged/already renamed")
        for w in PERIPHERAL:
            oldname = safe(w["stem"]) + ".pdf"
            destname = dest_name(w)
            old = os.path.join(PERI, oldname)
            new = os.path.join(PERI, destname)
            if oldname != destname and os.path.exists(old) and not os.path.exists(new):
                os.rename(old, new)
                renamed += 1
            if os.path.exists(new):
                peri_rows.append((w, destname, ""))

    # CSV：102 行
    csv_path = os.path.join(DST, "00_入库清单.csv")
    with open(csv_path, "w", encoding="utf-8-sig", newline="") as fh:
        wr = csv.writer(fh)
        wr.writerow(["层", "编号", "著者", "著作", "年份", "状态", "入库文件名", "来源文件", "备注"])
        for r in rows:
            wr.writerow([r["sec"], r["rid"], r["author"], r["title"], r["year"],
                         r["status"], r["dest"], r["src"], r["note"]])

    # Markdown 索引
    ext_rows = [r for r in rows if r["status"] == "已入库" and os.path.isabs(r["src"])]
    ext_ids = "、".join(r["rid"] for r in ext_rows)
    L = []
    L.append("# 基础文献入库清单（按 102 个 ref_id 重建）")
    L.append("")
    L.append("**生成日期**：2026-10-22  ")
    L.append("**依据文档**：`中国设计史相关文献总汇.md`  ")
    L.append(f"**检索范围**：`{ROOT}` 全库（参考文献PDF／基础文献／补充文献），另从 D 盘其他目录补入 {len(ext_rows)} 种（见第二节）  ")
    L.append("**口径**：102 个 ref_id = 六层表内 99 个唯一编号 + B292／B431／B459（马格林第2卷重复文件）；去重后 94 种著作。  ")
    L.append(f"**结果**：102 行全部登记；{sum(1 for r in rows if r['status']=='已入库')} 个主编号有 PDF；"
             f"{sum(1 for r in rows if r['status']=='互见')} 个编号与主编号共用同一 PDF；"
             f"{sum(1 for r in rows if r['status']=='缺藏')} 个编号缺藏。物理文件 {len(copies)} 个。")
    L.append("")
    L.append("## 说明")
    L.append("")
    L.append("1. **102 是 ref_id 数，不是 PDF 文件数。** 同书重复文件（B169→B004、B467/B506→B288、"
             "B292/B431/B459→B289、B032→B031、B507→B466）只入一份，其余编号在索引中标“互见”。")
    L.append(f"2. **94 是去重后的著作种数，全部有 PDF。** 其中 {94-len(ext_rows)} 种在《现当代设计史》三目录内，"
             f"{len(ext_rows)} 种从 D 盘其他目录补入（{ext_ids}，见第二节）。")
    L.append("3. 接受层优先采用文档所据中文译本；B065 用 2018 年中译《设计的观念》（库外补入），"
             "英文原版可另在 `参考文献PDF` 查阅。")
    L.append("4. B480 用 2019 年中译（据 2004 重订版）；B324（1949 第2版）、B353（1960 修订版）"
             "不属这 102 个 ref_id，未计入，英文原版可另在 `参考文献PDF` 查阅。")
    L.append("5. 文件名中的年份、版次取自文档著录或原文件名，均未核版权页；引用前须按文档第 10 节核版权页。")
    L.append("6. 8.2 外围参照 9 种不计入 102，另置本目录下 `00-外围参照`。")
    L.append("7. 入库文件名不带 ref_id 前缀；编号与文件的对应见本表“编号”列，"
             "按编号排序请用 `00_入库清单.csv`。")
    L.append("")
    L.append("## 一、102 个 ref_id 逐条登记")
    L.append("")
    for sec in [S1, S2, S3, S4, S5, S6]:
        block = [r for r in rows if r["sec"] == sec]
        if not block:
            continue
        L.append(f"### {SEC_NAMES[sec]}")
        L.append("")
        L.append("| 编号 | 著者 | 著作 | 年份 | 状态 | 入库文件名 | 备注 |")
        L.append("| --- | --- | --- | --- | --- | --- | --- |")
        for r in block:
            fn = f"`{r['dest']}`" if r["dest"] else "—"
            L.append(f"| {r['rid']} | {r['author']} | {r['title']} | {r['year']} | {r['status']} | {fn} | {r['note']} |")
        L.append("")
    L.append(f"## 二、库外补入 {len(ext_rows)} 种")
    L.append("")
    L.append(f"以下 {len(ext_rows)} 种不在 `D:\\《现当代设计史》` 三目录内，从 D 盘其他目录补入；现已全部入库。")
    L.append("")
    for r in ext_rows:
        L.append(f"- **{r['rid']}** {r['author']}《{r['title']}》{('，' + r['year']) if r['year'] else ''}。"
                 f"来源：`{r['src']}`")
    L.append("")
    L.append("## 三、外围参照（不计入 102）")
    L.append("")
    L.append("以下 9 种属文档 8.2，不立条，另置本目录下 `00-外围参照`。")
    L.append("")
    L.append("| 编号 | 著者 | 著作 | 入库文件名 |")
    L.append("| --- | --- | --- | --- |")
    for w, destname, _src in peri_rows:
        L.append(f"| {w['ids'][0]} | {w['author']} | {w['title']} | `{destname}` |")
    L.append("")
    L.append("## 四、跨层互见与重复文件")
    L.append("")
    L.append("- B153、B168 同属对象层与结构层，文件在 `01-对象层_中国设计造物`。")
    L.append("- B004、B289、B425 同属对象层与方法层，文件在 `01-对象层_中国设计造物`。")
    L.append("- B288 同属对象层与接受层，中译第1卷文件在 `01-对象层_中国设计造物`；B467、B506 为同书重复文件。")
    L.append("- B289（英文第2卷）与 B292、B431、B459 为同书四份，以 B289 为准。")
    L.append("- B466、B507 为同书两份，以 B466 为准。")
    L.append("- B031、B032 为同书两份，以 B031 为工作本。")
    L.append("- B004、B169 为同书两份，以 B004 为准。")
    L.append("")
    with open(os.path.join(DST, "00_文献对照索引.md"), "w", encoding="utf-8") as fh:
        fh.write("\n".join(L))

    print("=" * 110)
    print(f"Copied {len(copies)} files into {DST}")
    print(f"Copied {len(peri_rows)} peripheral files into {PERI}")
    print("Wrote 00_文献对照索引.md and 00_入库清单.csv")


if __name__ == "__main__":
    main()
