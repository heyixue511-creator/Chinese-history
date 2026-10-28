# -*- coding: utf-8 -*-
"""Build CL2e claim rows (Xia Yanjing 2009, ch.6 Sui-Tang-Five Dynasties)."""
import json
from pathlib import Path

ROOT = Path(r"D:/中国设计史研究")
DOC = "2009-xiayanjing-zhongguo-shejishi"
SRC = "03基础书籍-md文档/中国设计史_夏燕靖_2009_上海人民美术出版社.md"
DATE = "2026-10-27"
CH = "隋唐五代时期的艺术设计"

ROWS = []


def Q(s: str) -> str:
    s = s.replace("‘", "“").replace("’", "”")
    assert '"' not in s, s
    return s


def C(cid, ctype, zh, en, confidence, supported, note, start, end, kind,
      key_lines, block_ids, section):
    ROWS.append({
        "claim_id": None,
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
                "chapter": CH,
                "section": section,
            },
            "candidate_id": DOC + ":" + cid,
        },
        "confidence": confidence,
        "consensus": "tentative",
        "review_status": "source_backed",
        "supported_by": supported,
        "discussion_notes": Q(note),
        "created": DATE,
        "updated": DATE,
    })


C("cand-04-11", "historiographic_claim",
  "夏燕靖认为，隋唐两代是我国封建社会的鼎盛时期，隋朝虽时间短暂，但其开创之功为唐代的发展和繁荣奠定了基础；唐代以博大的历史胸襟对外开放贸易，成为世界性的经济文化交流中心。",
  "Xia Yanjing holds that the Sui and Tang were the zenith of Chinese feudal society; although the Sui was short-lived, its founding achievements laid the basis for Tang development and prosperity, and the Tang, open to trade and tolerant of diverse cultures, became a world centre of economic and cultural exchange.",
  "high",
  ["04-knowledge/units/terms/juntian-zhi.md",
   "04-knowledge/units/terms/zuyongdiao.md",
   "04-knowledge/units/terms/sichou-zhilu.md"],
  "候选作 periodization，按类型映射路由 historiographic；候选跨度 L1967-L1990 含章标题、两幅历史地图与知识链接“唐”国号考，实际断言分置 L1969 与 L1971 两段，故记 contiguous 并以两句为 key_lines；安史之乱后的分裂叙述留在来源。",
  1969, 1971, "contiguous", [1969, 1971], ["b0268"], "章首导论")

C("cand-04-13", "factual_claim",
  "夏燕靖据《唐六典》指出，唐代官府规定不同工种的工匠须接受9个月到4年的技术训练，金属工学习4年、乐器车辂工学习3年、竹木漆工学习1年，学习过程中每季度测试、年终考试。",
  "Citing the Tang Liudian, Xia Yanjing notes that Tang government workshops required artisans of different trades to undergo nine months to four years of technical training—four years for metalworkers, three for musical-instrument and carriage makers, one for bamboo, wood, and lacquer workers—with quarterly tests and a year-end examination.",
  "high",
  ["04-knowledge/units/institutions/shaofujian.md",
   "04-knowledge/units/institutions/jiangzuojian.md",
   "04-knowledge/units/terms/guanying-shougongye.md"],
  "候选作 basic_fact，路由 factual；候选跨度 L1993-L1998 为“隋唐官营手工业”知识链接框，断言取 L1995 的训练年限与考核制度；少府监、将作监各万余人及临时雇工数未写入主句。",
  1995, 1995, "line", [1995], ["b0270"], "知识链接：隋唐官营手工业")

C("cand-04-14", "interpretive_claim",
  "夏燕靖认为，隋唐官营手工业主要为满足皇室、官府和军事需要，经营矿冶、制盐、丝织、制瓷、铸钱、造船等行业，在规模、组织、分工和工艺水平上居主导地位；唐中叶后还承办水利交通等公共工程，产品通过贡赐、贸易和专卖流通。",
  "Xia Yanjing argues that Sui-Tang state handicrafts served mainly imperial, official, and military needs, operating mines, salt works, silk weaving, porcelain, coin casting, and shipbuilding, and dominated in scale, organization, division of labour, and craftsmanship; after the mid-Tang they also undertook water and transport works, with products circulating through tribute, trade, and monopoly sales.",
  "high",
  ["04-knowledge/units/terms/guanying-shougongye.md",
   "04-knowledge/units/institutions/shaofujian.md",
   "04-knowledge/units/institutions/jiangzuojian.md"],
  "候选作 interpretation；“居于主导地位”是作者对官营手工业结构位置的判断，保留原语气；矿冶、制盐、丝织、制瓷、铸钱、造船等行业清单按来源照录，未据后世官营范围补写。",
  2001, 2001, "line", [2001], ["b0271"], "1. 手工业的繁荣促进了其设计水平的提高｜1）官营手工业的兴盛")

C("cand-04-16", "interpretive_claim",
  "夏燕靖认为，唐代行业性质的社会组织协调内部关系、规定产销条例与价格竞争，得到官府的承认和保护，手工业者的社会地位普遍提高，标志着隋唐手工业已发展到一个新的阶段。",
  "Xia Yanjing argues that Tang trade organizations coordinated internal relations and regulated production, marketing, and price competition; recognized and protected by the government, they raised the social standing of artisans and marked a new stage in Sui-Tang handicraft development.",
  "medium",
  ["04-knowledge/units/terms/shougongye-hanghui.md",
   "04-knowledge/units/terms/zuopu.md",
   "04-knowledge/units/terms/guanying-shougongye.md"],
  "候选作 interpretation，默认路由 interpretive；候选跨度 L2003-L2013 含“作铺”与行会两段，断言取 L2012 的协调、规约、地位提高与阶段判断；染行、织锦行、金银行、绢行等行名留在来源。",
  2012, 2012, "line", [2012], ["b0272"], "1. 手工业的繁荣促进了其设计水平的提高｜2）民间手工业")

C("cand-04-17", "interpretive_claim",
  "夏燕靖认为，隋唐五代尤其是唐代出现了中外文化科技交流的高潮，设计的发展得力于外来文化的营养，同时以自身的优秀文化成果影响周边国家和地区。",
  "Xia Yanjing argues that the Sui-Tang-Five Dynasties period, especially the Tang, saw a climax of cultural and technological exchange with foreign lands: design drew nourishment from foreign cultures while Chinese achievements in turn influenced neighbouring countries and regions.",
  "high",
  ["04-knowledge/units/terms/sichou-zhilu.md",
   "04-knowledge/units/terms/yisilan-wenhua.md",
   "04-knowledge/units/events/6th-century-fangzhi-jishu-waichuan.md"],
  "候选作 interpretation；L2018 同时给出“输入”与“输出”两个方向，断言保留双向表述，未简化为单向影响；“怎样估价也不为过分”的强烈评价未写入主句。",
  2018, 2018, "line", [2018], ["b0273"], "3）五代手工业")

C("cand-04-18", "factual_claim",
  "夏燕靖指出，隋代除继续生产传统的青瓷外，白瓷已经烧制成功并得以大量生产。",
  "Xia Yanjing notes that in the Sui, besides continued production of traditional celadon, white porcelain was successfully fired and produced in quantity.",
  "high",
  ["04-knowledge/units/terms/baici.md",
   "04-knowledge/units/terms/qing-ci.md"],
  "候选作 basic_fact，路由 factual；L2024 前文列隋墓出土与窑址，后半列饮食器、盛贮器等用途分类，断言只取青瓷延续与白瓷成功大量生产两项。",
  2024, 2024, "line", [2024], ["b0274"], "2. 陶瓷工艺与陶瓷设计的发展")

C("cand-04-20", "factual_claim",
  "夏燕靖指出，隋代陶瓷的器形和装饰设计基本上与前代相似，但仍有明显变化，其中桥形耳和钮状耳较多、最富特色，几何纹、弦纹、绳纹、联珠纹以及莲瓣、忍冬等植物纹和龙、凤等动物纹也有所增加。",
  "Xia Yanjing notes that Sui ceramic forms and decoration were broadly similar to those of the preceding period but showed clear changes: bridge-shaped and button-shaped handles were common and most distinctive, while geometric, string, cord, and linked-pearl motifs, plant motifs such as lotus petals and honeysuckle, and animal motifs such as dragons and phoenixes increased.",
  "high",
  ["04-knowledge/units/terms/qing-ci.md",
   "04-knowledge/units/terms/baici.md",
   "04-knowledge/units/works/bai-you-lv-cai-si-xi-lian-ban-gang.md"],
  "候选作 basic_fact，路由 factual；候选跨度 L2026-L2047 含天鸡壶、瓶、罐三类器形比对与图 6-6、6-7，断言取 L2041 的总结句；器形细部与护胎釉工艺未逐条写入。",
  2041, 2041, "line", [2041], ["b0275"], "1）造型设计的特点")

C("cand-04-21", "interpretive_claim",
  "夏燕靖认为，《陶录》所称唐代“始有窑名”，实际是指当时开始出现若干著名的陶瓷制作中心，这在一定程度上反映了陶瓷业的兴盛和各地窑产品不同的艺术特色。",
  "Xia Yanjing argues that the Taolu's statement that kilns first acquired names in the Tang actually refers to the emergence of several famous ceramic production centres, reflecting both the prosperity of the industry and the distinct artistic character of wares from different localities.",
  "medium",
  ["04-knowledge/units/terms/tang-dai-qingci-yao.md",
   "04-knowledge/units/places/yue-kiln.md",
   "04-knowledge/units/places/xing-kiln.md"],
  "候选作 interpretation；本条是对《陶录》“陶至唐而盛，始有窑名”的释义修正，断言以“实际是指”保留作者的重新解释，不把“始有窑名”当作唐代窑业已普遍命名的直接证据。",
  2050, 2050, "line", [2050], ["b0276"], "2）重要的陶瓷类别")

C("cand-04-23", "interpretive_claim",
  "夏燕靖认为，唐代越窑几乎专门提供宫廷用品，由官府督造，是后来历代御器厂或官窑的前身；当时将这种窑所产出的成品称作秘色。",
  "Xia Yanjing argues that the Tang Yue kilns supplied almost exclusively for the court under official supervision and were the forerunner of later imperial factories and official kilns; their products were called mise.",
  "high",
  ["04-knowledge/units/places/yue-kiln.md",
   "04-knowledge/units/terms/mise-porcelain.md",
   "04-knowledge/units/institutions/ciyaoguan.md"],
  "候选作 interpretation；“御器厂或官窑的前身”是作者的制度史回溯判断，保留“前身”而非直接称唐代已有御器厂；同段越窑胎骨、釉色与茶酒器造型留在来源。",
  2056, 2056, "line", [2056], ["b0277"], "2）重要的陶瓷类别｜① 青瓷")

C("cand-04-25", "factual_claim",
  "夏燕靖指出，1987年陕西扶风法门寺地宫出土16件晚唐越窑秘色瓷，采用“支钉撑烧法”，比北宋汝窑提早100余年，是我国首次发现唐代秘色瓷的实物。",
  "Xia Yanjing notes that in 1987 the crypt of Famen Temple in Fufeng, Shaanxi, yielded sixteen late-Tang Yue ware mise porcelains fired by the spurred-support method, more than a century earlier than Northern Song Ru ware; this was the first discovery of actual Tang mise porcelain in China.",
  "high",
  ["04-knowledge/units/terms/mise-porcelain.md",
   "04-knowledge/units/procedures/zhiding-zhishao.md",
   "04-knowledge/units/places/yue-kiln.md"],
  "候选作 basic_fact，路由 factual；候选跨度 L2065-L2068 为“唐代秘色瓷”知识链接框，断言取 L2067；来源作“扶凤县”，断言按通行地名写“扶风”，不另改来源原文；“民间不能使用”之说留在来源。",
  2067, 2067, "line", [2067], ["b0278"], "知识链接：唐代秘色瓷")

C("cand-04-27", "factual_claim",
  "夏燕靖指出，邢窑由初唐开始生产白瓷，到中唐流行并普及全国；《国史补》称“内邱白瓷瓯”“天下无贵贱通用之”。",
  "Xia Yanjing notes that the Xing kilns began producing white porcelain in the early Tang and by the mid-Tang their wares were fashionable and distributed nationwide; the Guoshi Bu records the Neiqiu white-porcelain bowl as used by high and low alike.",
  "high",
  ["04-knowledge/units/places/xing-kiln.md",
   "04-knowledge/units/terms/baici.md",
   "04-knowledge/units/publications/guo-shi-bu.md"],
  "候选作 basic_fact，路由 factual；元稹绝句与“洁白如银雪”“玉璧底”等描述留在来源，断言只取邢窑起烧、中唐普及与《国史补》两条引文。",
  2071, 2071, "line", [2071], ["b0279"], "② 白瓷")

C("cand-04-30", "historiographic_claim",
  "夏燕靖把唐三彩的兴衰概括为三个阶段：最初烧制于高宗时期，开元年间达到极盛，“安史之乱”后逐渐衰微。",
  "Xia Yanjing periodizes Tang sancai into three phases: first fired under Emperor Gaozong, at its height during the Kaiyuan era, and declining after the An Lushan rebellion.",
  "high",
  ["04-knowledge/units/terms/tang-sancai.md",
   "04-knowledge/units/terms/yaobian.md",
   "04-knowledge/units/works/sancai-nv-yong.md"],
  "候选作 periodization，路由 historiographic；候选跨度 L2085-L2102 含胎釉配方、素烧与釉烧两步法、窑变控制与器类，断言只取 L2095 的三期兴衰；烧制地点西安、洛阳与扬州作坊留在来源。",
  2095, 2095, "line", [2095], ["b0281"], "④ 唐三彩")

C("cand-04-31", "interpretive_claim",
  "夏燕靖认为，唐代租庸调制规定每丁年纳绢2丈、绵3两，或麻布2丈5尺、麻3斤，这一制度对纺织业的发展起到了推动作用。",
  "Xia Yanjing argues that the Tang zu-yong-diao tax system, which required each adult male to pay two zhang of silk and three liang of floss, or two zhang five chi of hemp cloth and three jin of hemp, helped stimulate textile production.",
  "high",
  ["04-knowledge/units/terms/zuyongdiao.md",
   "04-knowledge/units/terms/juntian-zhi.md",
   "04-knowledge/units/terms/jia-ting-shou-gong-ye.md"],
  "候选作 interpretation；税额是制度事实，“对纺织业发展起到推动作用”是作者的因果判断，故整条按 interpretive 路由，未拆成 factual 与 causal 两条；《唐六典》八至九等分级留在来源。",
  2107, 2107, "line", [2107], ["b0282"], "3. 纺织印染业的进步与设计品种的丰富")

C("cand-04-32", "historiographic_claim",
  "夏燕靖指出，唐中期江南丝织业的工艺水平和产量都已超过北方，当时有“蜀桑万亩、吴蚕万机”之说。",
  "Xia Yanjing notes that by the mid-Tang the Jiangnan silk industry had surpassed the north in both craftsmanship and output, hence the saying of ten thousand mu of Shu mulberries and ten thousand looms of Wu silkworms.",
  "high",
  ["04-knowledge/units/terms/shu-brocade.md",
   "04-knowledge/units/terms/zhijin.md",
   "04-knowledge/units/terms/ling-silk.md"],
  "候选作 periodization，路由 historiographic；“超过北方”是区域消长判断，保留“唐中期”时点；定州绫机500架、南诏掠织工数万等例证留在来源。",
  2111, 2111, "line", [2111], ["b0283"], "1) 丝织业")

C("cand-04-35", "interpretive_claim",
  "夏燕靖认为，唐代的锦以纬锦为主并达到很高水平，唐锦的艺术风格以富丽绚烂、清新流畅为特征。",
  "Xia Yanjing argues that Tang brocade was predominantly weft-faced and reached a high level, its artistic style characterized by rich splendour and fresh fluency.",
  "high",
  ["04-knowledge/units/terms/weft-brocade.md",
   "04-knowledge/units/terms/zhijin.md",
   "04-knowledge/units/terms/lianzhu-wen.md"],
  "候选作 interpretation；“富丽绚烂、清新流畅”是风格评价，保留为作者判断；联珠纹、团窠纹、对称纹、散花、几何纹、晕绸等图案分类留在来源，未逐类立条。",
  2119, 2119, "line", [2119], ["b0285"], "1) 丝织业｜② 锦")

C("cand-04-38", "interpretive_claim",
  "夏燕靖认为，陵阳公样是当时中西文化交流的产物，集秀美富丽于一体，既突破了六朝以来的传统装饰风格，又吸收外来营养而富有独创性。",
  "Xia Yanjing argues that the Lingyang Gong pattern was a product of Sino-Western cultural exchange, combining elegance with richness; it broke through the traditional decorative style inherited from the Six Dynasties while absorbing foreign elements with originality.",
  "high",
  ["04-knowledge/units/terms/lingyang-gong-pattern.md",
   "04-knowledge/units/terms/lianzhu-wen.md",
   "04-knowledge/units/terms/weft-brocade.md"],
  "候选作 interpretation；窦师伦被尊称“陵阳公”的命名缘由、对狮对羊对鹿对凤题材与团窠联珠结构留在来源；断言保留“中西文化交流的产物”这一作者定性。",
  2125, 2125, "line", [2125], ["b0286"], "知识链接：陵阳公样")

C("cand-04-42", "factual_claim",
  "夏燕靖据《旧唐书·五行志》与《朝野佥载》指出，唐代北方和西北毛织业发达，安乐公主的羽裙正看、侧看、日中、影中各为一色，百鸟之状尽在裙中，引发贵族效仿，以致奇禽异鸟的毛羽被采之殆尽。",
  "Citing the Jiu Tang Shu and Chaoye Qianzai, Xia Yanjing notes that wool weaving flourished in the north and northwest; Princess Anle's feather skirt showed one colour seen frontally, another from the side, another in sunlight, and another in shadow, with the forms of a hundred birds within it, prompting aristocratic imitation until rare bird feathers were all but exhausted.",
  "medium",
  ["04-knowledge/units/works/anle-gongzhu-yuqun.md"],
  "候选作 basic_fact，路由 factual；羽裙故事属文献转引，断言以“据《旧唐书·五行志》与《朝野佥载》”保留双重出处；“采之殆尽”是史文夸张，未改写为生态事实；绒褐、西川毡、覆鞍毡等毛织品名留在来源。",
  2154, 2154, "line", [2154], ["b0291"], "2）棉、麻、毛纺织技术")

C("cand-04-45", "factual_claim",
  "夏燕靖据《唐六典》指出，唐代织染署设青、绛、黄、白、皂、紫六色练染之作，染料以植物染料为主，靛蓝等已作为外贸商品出口西亚等地。",
  "Citing the Tang Liudian, Xia Yanjing notes that the Tang Weaving and Dyeing Bureau maintained six scouring-and-dyeing workshops for blue, crimson, yellow, white, black, and purple; dyes were mainly vegetable, and indigo was already exported to West Asia and elsewhere as a trade commodity.",
  "high",
  ["04-knowledge/units/institutions/zhiranshu.md",
   "04-knowledge/units/terms/jiaoxie.md",
   "04-knowledge/units/terms/jiaxie.md",
   "04-knowledge/units/procedures/jiezhi-yinhua.md"],
  "候选作 basic_fact，路由 factual；《唐六典》引文只取六色之名与“大抵以草木而成”，张萱《捣练图》与绞缬、夹缬、蜡缬、介质印花四类工艺留在来源，另以 KU 链接承接。",
  2164, 2164, "line", [2164], ["b0293"], "3）印染业")

C("cand-04-47", "factual_claim",
  "夏燕靖据《旧唐书·舆服志》指出，唐代官员袍衫主要以颜色区别等级：贞观四年定三品以上紫色、五品以上绯色、六品七品绿色、八品九品青色；公元674年又细化为深浅绯、绿、青并配金、玉、银、石带。",
  "Citing the Jiu Tang Shu treatise on carriages and dress, Xia Yanjing notes that Tang official robes distinguished rank mainly by colour: in 630 those of the third rank and above wore purple, the fifth and above crimson, the sixth and seventh green, and the eighth and ninth blue; in 674 the scheme was refined into deep and pale shades of crimson, green, and blue, with gold, jade, silver, and stone belts.",
  "high",
  ["04-knowledge/units/terms/pinse-yi.md",
   "04-knowledge/units/terms/gongfu.md",
   "04-knowledge/units/terms/yuanling-paoshan.md"],
  "候选作 basic_fact，路由 factual；候选跨度 L2181-L2199 含幞头形制、圆领袍衫、横襕、红鞏带与平民服色，断言只取 L2196-L2198 的两度服色令；断言分置两段，故记 contiguous；阎立本《步辇图》佐证留在来源。",
  2196, 2198, "contiguous", [2196, 2198], ["b0295"], "4. 服装工艺与服饰设计的特色形成｜1）男服")

C("cand-04-50", "historiographic_claim",
  "夏燕靖指出，中唐之前中原妇女喜欢穿着翻领窄袖的胡服，盛唐以后胡服影响逐渐减弱，衣衫加宽、袖子放大，到中晚唐一般妇女服装袖宽超过四尺。",
  "Xia Yanjing notes that before the mid-Tang women in the Central Plains favoured Hu dress with turned-down collars and narrow sleeves; after the High Tang its influence waned, garments and sleeves widened, and by the mid-to-late Tang ordinary women's sleeves exceeded four chi.",
  "high",
  ["04-knowledge/units/terms/hufu.md",
   "04-knowledge/units/terms/pibo.md",
   "04-knowledge/units/terms/shiliu-qun.md"],
  "候选作 periodization，路由 historiographic；候选跨度 L2200-L2218 含衫襦袄裙、披帛与裙式演变，断言取 L2208 的胡服消长与袖宽变化；《簪花仕女图》与南唐二陵陶塑作为例证留在来源。",
  2208, 2208, "line", [2208], ["b0296"], "2）女装")

C("cand-04-54", "interpretive_claim",
  "夏燕靖认为，唐代金银器制作既有官作即中尚署下设的金银作坊院，又有行作即民间金银行、金银铺；唐代后期白银事实上成为正式货币，金银铺因此兼有金融机构的性质。",
  "Xia Yanjing argues that Tang gold and silver work was produced both by the official Jinyin Zuofangyuan under the Zhongshang Office and by private gold-and-silver guilds and shops; in the late Tang silver in fact became a formal currency, so these shops also took on the character of financial institutions.",
  "high",
  ["04-knowledge/units/institutions/jinyin-zuofangyuan.md",
   "04-knowledge/units/works/wensiyuan-yin-xunlu.md",
   "04-knowledge/units/works/tang-yin-xiangnang.md"],
  "候选作 interpretation；“事实上成为正式货币”与“兼有金融机构性质”是作者对货币史的制度判断，保留“事实上”限定；金坑14处、银场56处、吹灰法炼银与天宝银铤50两留在来源。",
  2227, 2227, "line", [2227], ["b0299"], "5. 金属工艺设计的成熟｜1）金属工艺的繁荣")

C("cand-04-55", "interpretive_claim",
  "夏燕靖认为，唐代金银器制作于中唐进入全盛时期，其造型与纹样深受波斯萨珊王朝影响，但多为“西方”器形、“东方”纹样，形成中西结合的设计特色。",
  "Xia Yanjing argues that Tang gold and silver work reached its height in the mid-Tang; its forms and motifs were deeply influenced by Sasanian Persia, yet it mostly combined Western shapes with Eastern motifs, producing a Sino-Western design character.",
  "high",
  ["04-knowledge/units/institutions/jinyin-zuofangyuan.md",
   "04-knowledge/units/works/wensiyuan-yin-xunlu.md",
   "04-knowledge/units/works/tang-yin-xiangnang.md",
   "04-knowledge/units/procedures/jinyin-pingtuo.md"],
  "候选作 interpretation；“西方器形、东方纹样”是作者对器形与纹样来源的分离判断，保留引号内表述；何家村270件、丁卯桥956件、法门寺121件与车床切削、鎏金、錾刻等工艺留在来源。",
  2234, 2234, "line", [2234], ["b0300"], "5. 金属工艺设计的成熟｜2）金银器的制作工艺与设计特色")

C("cand-04-59", "interpretive_claim",
  "夏燕靖认为，伊斯兰文化自唐代开始对我国艺术设计产生较大影响，主要见于釉彩、金银、纺织、建筑工艺及各类装饰艺术；青瓷釉料配制与伊斯兰釉彩存在联系，青花所用钴料均产自伊斯兰地区，唐三彩也得益于西域釉陶工艺。",
  "Xia Yanjing argues that Islamic culture began to exert a substantial influence on Chinese design from the Tang, chiefly in glazes, metalwork, textiles, architecture, and ornament; celadon glaze preparation is linked to Islamic glazing, the cobalt used in blue-and-white came from Islamic regions, and Tang sancai benefited from Western Regions glazed-pottery techniques.",
  "medium",
  ["04-knowledge/units/terms/yisilan-wenhua.md",
   "04-knowledge/units/terms/blue-and-white-porcelain.md",
   "04-knowledge/units/terms/tang-sancai.md",
   "04-knowledge/units/terms/qing-ci.md"],
  "候选作 interpretation；来源以“可以说是受到……影响是可能的”“看来主要是归功于”等限定语表述，断言保留联系性而非写成已证因果；钴毒砂、苏麻离青、回青等钴料名按来源照录。",
  2265, 2265, "line", [2265], ["b0302"], "知识链接：伊斯兰文化")

C("cand-04-61", "factual_claim",
  "夏燕靖指出，唐代确已存在在金属上涂饰珐琅的工艺，例证为日本正仓院所藏“黄金琉璃钿背十二棱镜”与1980年陕西蓝田出土的涂有白色珐琅釉质的窖藏银饰；这是明代景泰蓝的滥觞。",
  "Xia Yanjing notes that enamelling on metal did exist in the Tang, evidenced by the twelve-faceted mirror with gold and glass inlay in the Shosoin, Japan, and by silver ornaments with white enamel glaze from a 1980 hoard find at Lantian, Shaanxi; this was the forerunner of Ming cloisonné.",
  "medium",
  ["04-knowledge/units/terms/tangjing.md",
   "04-knowledge/units/terms/jingtai-lan.md",
   "04-knowledge/units/terms/falangcai.md",
   "04-knowledge/units/procedures/jingtailan-zhizuo.md"],
  "候选作 attribution，按类型映射路由 factual；两件实物证据与“唐代确有存在”的判断分别保留，“明代景泰蓝的滥觞”是作者的技术史溯源，写在句末而不改写为唐代已有景泰蓝；唐镜合金比例70:25:5与沈括《梦溪笔谈》留在来源。",
  2277, 2277, "line", [2277], ["b0303"], "3）铜器工艺的高度发达")

C("cand-04-62", "factual_claim",
  "夏燕靖指出，扬州施桥镇出土的唐代木船是世界最早的水密舱结构实物，也是世界造船史上的创举，既增强了远洋航行的安全性，也增强了船体的横向强度。",
  "Xia Yanjing notes that the Tang wooden ship excavated at Shiqiao in Yangzhou is the world's earliest physical example of watertight bulkheads and a landmark in shipbuilding history, strengthening both the safety of ocean voyages and the hull's transverse strength.",
  "high",
  ["04-knowledge/units/terms/shuimi-cang.md",
   "04-knowledge/units/terms/plank-boat.md",
   "04-knowledge/units/works/liangtou-jian-chuan.md"],
  "候选作 basic_fact，路由 factual；“世界最早”“创举”是来源的评价性判断，随文保留而不另升为 evaluative；断言句被空行 L2288 分隔于 L2287 与 L2289，故记 contiguous；唐代海船载重近万石与外国商人搭乘留在来源。",
  2287, 2289, "contiguous", [2287, 2289], ["b0305"], "6. 造船与家具制造业的发展与设计特色｜1）造船业")

C("cand-04-64", "historiographic_claim",
  "夏燕靖把隋唐家具的发展趋势概括为：家具逐渐向高形、成套化发展，种类有所增加，用材除紫檀、黄杨、沉香、花梨等硬木外，还使用竹藤等材料。",
  "Xia Yanjing summarizes the Sui-Tang trend in furniture as a gradual move toward high forms and suites, with more types and a wider range of materials—hardwoods such as rosewood, boxwood, agarwood, and huanghuali, as well as bamboo and rattan.",
  "high",
  ["04-knowledge/units/terms/gaoxing-jiaju.md",
   "04-knowledge/units/terms/huchuang.md",
   "04-knowledge/units/terms/yizi.md"],
  "候选作 periodization，路由 historiographic；候选跨度 L2291-L2319 含几、案、挟轼、箱、柜、胡床、屏风与桌椅等品种，断言只取 L2293 的高形化、成套化与用材趋势；具体器物形制留在来源。",
  2293, 2293, "line", [2293], ["b0306"], "6. 造船与家具制造业的发展与设计特色｜2）家具业")

C("cand-04-69", "interpretive_claim",
  "夏燕靖认为，宇文恺把宫城、官署和居民区严格区分开来，划分整齐明确、布局完整对称，是其一大创造，对后世都城建设有重大影响。",
  "Xia Yanjing argues that Yuwen Kai's strict separation of palace, government offices, and residential quarters, with clear divisions and a complete symmetrical layout, was a major innovation with far-reaching influence on later capital planning.",
  "high",
  ["04-knowledge/units/places/daxing-cheng.md",
   "04-knowledge/units/persons/yuwen-kai.md",
   "04-knowledge/units/terms/lifang-zhi.md"],
  "候选作 interpretation；候选跨度 L2320-L2366 含赵州桥、大兴城选址、规模、城门、里坊与街道，断言取 L2338 的区划创造判断；108里坊、朱雀大街宽150米等数据留在来源。",
  2338, 2338, "line", [2338], ["b0307"], "7. 建筑设计的成熟与繁荣")

C("cand-04-71", "interpretive_claim",
  "夏燕靖认为，隋唐建筑设计强调艺术与结构的统一，没有华而不实的构件，建筑色调简洁明快、屋顶舒展平远、门窗朴实无华，给人以庄重、大方的印象，这是后来宋元明清建筑所少见的特色。",
  "Xia Yanjing argues that Sui-Tang architecture stressed the unity of art and structure, with no merely ornamental members; its restrained colours, broad low roofs, and plain doors and windows give an impression of dignity and generosity rarely matched in later Song, Yuan, Ming, and Qing building.",
  "high",
  ["04-knowledge/units/works/daming-gong.md",
   "04-knowledge/units/works/dayan-ta-652.md",
   "04-knowledge/units/works/zhaozhou-qiao-595-605.md"],
  "候选作 interpretation；本条是对隋唐建筑整体风格的品评，“宋元明清所少见”是跨时代比较判断，保留作者评价；斗栱、出檐、琉璃与砖塔三型等形制描述留在来源。",
  2365, 2365, "line", [2365], ["b0307"], "7. 建筑设计的成熟与繁荣")

C("cand-04-72", "interpretive_claim",
  "夏燕靖认为，五代战乱时期四川地区相对安定、市场繁荣，伴随商业与手工业制造水平的提高，商业传销方式的艺术设计已经出现，商家的门匾题字和经营招牌的美化十分普及。",
  "Xia Yanjing argues that while warfare prevailed in the Five Dynasties, Sichuan remained relatively stable with a flourishing market; as commerce and handicraft improved, design for commercial promotion appeared, and the embellishment of shop plaques and signboards became widespread.",
  "medium",
  ["04-knowledge/units/terms/wudai-shiguo.md",
   "04-knowledge/units/terms/zhaopai.md",
   "04-knowledge/units/terms/huangzi.md",
   "04-knowledge/units/terms/zuopu.md"],
  "候选作 interpretation；“商业传销方式的艺术设计已经出现”是作者以现代设计概念概括五代店招现象，保留该判断；前、后蜀“府库之积”引文与竹木编制品留在来源，未并入本条。",
  2377, 2377, "line", [2377], ["b0308"], "8. 五代十国时期艺术设计")

C("cand-04-74", "interpretive_claim",
  "夏燕靖指出，五代柴窑只见于历史文献记述，至今仍是没有确切考据的疑问，可能是周世宗向钱氏提出的贡瓷要求，属于越窑秘色瓷一类产品。",
  "Xia Yanjing notes that the Five Dynasties Chai kiln is known only from historical texts and remains without firm archaeological confirmation; it may have been a tribute-porcelain demand made by Emperor Shizong of Zhou to the Qian family, and would belong to the Yue ware mise porcelain category.",
  "medium",
  ["04-knowledge/units/terms/chai-yao.md",
   "04-knowledge/units/terms/mise-porcelain.md",
   "04-knowledge/units/places/yue-kiln.md"],
  "候选作 interpretation；来源以“也许是”“属于……一类产品”双重限定，断言保留推测语气，不把柴窑等同于越窑秘色瓷；“雨过天青”“青如天、明如镜、薄如纸、声如磬”与“片瓦值千金”留在来源。",
  2381, 2381, "line", [2381], ["b0309"], "8. 五代十国时期艺术设计｜1）陶瓷工艺")

C("cand-04-75", "interpretive_claim",
  "夏燕靖认为，五代越窑青瓷大量运用划花、刻花、印花手法装饰荷花、牡丹、秋葵、龙凤、鹦鹉、人物和风景等题材，承袭了唐代金银器、铜镜、织绣的艺术设计特点。",
  "Xia Yanjing argues that Five Dynasties Yue celadon made extensive use of incised, carved, and stamped decoration with themes such as lotus, peony, hollyhock, dragon and phoenix, parrots, figures, and landscape, inheriting design features from Tang metalwork, mirrors, and textiles.",
  "medium",
  ["04-knowledge/units/places/yue-kiln.md",
   "04-knowledge/units/works/yue-kiln-lianhua-wan-heye-tuo.md",
   "04-knowledge/units/terms/tangjing.md",
   "04-knowledge/units/terms/zhijin.md"],
  "候选作 interpretation；“承袭唐代金银器、铜镜、织绣”是跨媒材的风格溯源判断，保留“承袭”而非写成直接传播证据；吴越钱氏一次贡瓷14万件与秘色为最上品留在来源。",
  2381, 2381, "line", [2381], ["b0309"], "8. 五代十国时期艺术设计｜1）陶瓷工艺")

C("cand-04-77", "interpretive_claim",
  "夏燕靖认为，柳宗元《梓人传》以其治理天下的“相道”联系工匠经验来论述工艺设计思想，具有独到性，特别是对总体设计原则的把握与运用已超越了先前的设计理念。",
  "Xia Yanjing argues that Liu Zongyuan's Ziren Zhuan uses the statesman's art of governing to discuss craft design through the experience of a master carpenter; its distinctive approach, especially its grasp and application of overall design principles, surpassed earlier design ideas.",
  "medium",
  ["04-knowledge/units/publications/ziren-zhuan.md",
   "04-knowledge/units/persons/liu-zongyuan.md",
   "04-knowledge/units/terms/jiangren-yingguo.md"],
  "候选作 interpretation；“独到性”与“超越了先前的设计理念”是作者的文学—设计史评价，保留判断语气；“规矩绳墨以定制”“善运众工而不伐艺”引文留在来源。",
  2387, 2387, "line", [2387], ["b0311"], "知识链接：《梓人传》")

C("cand-04-118", "historiographic_claim",
  "夏燕靖认为，五代十国时期形成青瓷、白瓷、黑瓷三大瓷窑体系，这一时期初步创立的陶瓷品种为宋代的名窑名瓷打下了坚实基础。",
  "Xia Yanjing argues that the Five Dynasties and Ten Kingdoms saw the formation of three great kiln systems—celadon, white, and black—and that the ceramic types first established then laid a firm foundation for the famous kilns and wares of the Song.",
  "medium",
  ["04-knowledge/units/terms/songdai-yaoxi.md",
   "04-knowledge/units/terms/qing-ci.md",
   "04-knowledge/units/terms/baici.md",
   "04-knowledge/units/terms/black-porcelain.md"],
  "候选作 periodization，路由 historiographic；候选仅有单行 L2394，位于《梓人传》框插入后的续文，断言取三大窑系与“为宋代名窑打下基础”的前后分期判断；徐寅《贡余秘色茶盏》诗留在来源。",
  2394, 2394, "line", [2394], ["b0311"], "8. 五代十国时期艺术设计｜1）陶瓷工艺")

C("cand-04-79", "evaluative_claim",
  "夏燕靖认为，五代十国时期各地区发展不平衡，艺术设计总的气势已无法与唐代相比；从风格上说，它失去了初唐的清秀、盛唐的华丽，只继承中晚唐的洗炼和沉稳，随后渐渐形成比较拘谨、秀气、柔弱的时代风格。",
  "Xia Yanjing holds that uneven regional development in the Five Dynasties and Ten Kingdoms left art design with an overall force no longer comparable to the Tang; in style it lost the freshness of the early Tang and the splendour of the High Tang, inherited only the refinement and composure of the mid-to-late Tang, and gradually formed a more restrained, delicate, and fragile period style.",
  "medium",
  ["04-knowledge/units/terms/wudai-shiguo.md"],
  "候选作 periodization，但断言主体是对五代风格高下的品评而非时间分期，按“以评价为主”改路由 evaluative_claim，并在 review 中复核；候选跨度 L2405-L2417 含王建墓漆器、蔡庄木俑与螺钿经函，断言只取 L2416 的总结评价。",
  2416, 2416, "line", [2416], ["b0313"], "8. 五代十国时期艺术设计")


def main():
    assert len(ROWS) == 34, len(ROWS)
    types = {"factual_claim", "interpretive_claim", "synthetic_claim",
             "evaluative_claim", "contested_claim", "historiographic_claim"}
    seen = set()
    for i, row in enumerate(ROWS):
        row["claim_id"] = "claim-%04d" % (132 + i)
        assert row["claim_type"] in types, row["claim_type"]
        assert row["confidence"] in {"high", "medium", "low"}
        assert row["statement_zh"].startswith("夏燕靖"), row["claim_id"]
        assert row["statement_en"].strip()
        assert row["discussion_notes"].strip()
        assert row["consensus"] == "tentative"
        assert row["review_status"] == "source_backed"
        cid = row["source"]["candidate_id"]
        assert cid not in seen, cid
        seen.add(cid)
        sp = row["source"]["source_span"]
        assert 1967 <= sp["line_start"] <= sp["line_end"] <= 2443, sp
        assert sp["key_lines"] and all(sp["line_start"] <= x <= sp["line_end"] for x in sp["key_lines"]), sp
        assert sp["block_ids"], sp
        assert sp["span_kind"] in {"line", "contiguous", "bounded"}
        if sp["span_kind"] == "line":
            assert sp["line_start"] == sp["line_end"]
        for p in row["supported_by"]:
            assert p.startswith("04-knowledge/units/"), p
            assert (ROOT / p).exists(), p
    assert len({r["source"]["candidate_id"] for r in ROWS}) == 34
    (ROOT / "_zn_claim_xyj09e_rows.json").write_text(
        json.dumps(ROWS, ensure_ascii=False, indent=2), encoding="utf-8")
    from collections import Counter
    print(json.dumps({
        "claims": len(ROWS),
        "with_support": sum(1 for r in ROWS if r["supported_by"]),
        "links": sum(len(r["supported_by"]) for r in ROWS),
        "distinct_support": len({p for r in ROWS for p in r["supported_by"]}),
        "types": dict(Counter(r["claim_type"] for r in ROWS)),
        "confidence": dict(Counter(r["confidence"] for r in ROWS)),
        "span_kinds": dict(Counter(r["source"]["source_span"]["span_kind"] for r in ROWS)),
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
