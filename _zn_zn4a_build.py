# -*- coding: utf-8 -*-
"""Build 赵农 2009 第四章 claim rows (24 new claims, no merges)."""
import json
from pathlib import Path

ROOT = Path(r"D:/中国设计史研究")
DOC = "2009-zhaonong-zhongguo-yishu-shejishi"
SRC = "03基础书籍-md文档/中国艺术设计史_赵农_2009_高等教育出版社.md"
DATE = "2026-10-27"
CH = "第四章 统一的气量——秦汉时期的设计"

T = "04-knowledge/units/terms/"
P = "04-knowledge/units/places/"
R = "04-knowledge/units/persons/"
W = "04-knowledge/units/works/"
B = "04-knowledge/units/publications/"
I = "04-knowledge/units/institutions/"
PR = "04-knowledge/units/procedures/"
E = "04-knowledge/units/events/"


def Q(s: str) -> str:
    s = s.replace("‘", "“").replace("’", "”")
    assert '"' not in s, s
    return s


def C(claim_id, cand, ctype, zh, en, supported, note, start, end, key_lines, block_ids, section):
    for p in supported:
        assert (ROOT / p).is_file(), p
    return {
        "claim_id": claim_id,
        "statement_zh": Q(zh),
        "statement_en": en,
        "claim_type": ctype,
        "source": {
            "doc_id": DOC,
            "source_file": SRC,
            "source_span": {
                "line_start": start,
                "line_end": end,
                "span_kind": "line" if start == end else "bounded",
                "key_lines": key_lines,
                "block_ids": block_ids,
                "chapter": CH,
                "section": section,
            },
            "candidate_id": DOC + ":" + cand,
        },
        "confidence": "medium",
        "consensus": "tentative",
        "review_status": "source_backed",
        "supported_by": supported,
        "discussion_notes": Q(note),
        "created": DATE,
        "updated": DATE,
    }


rows = []

rows.append(C(
    "claim-0501", "cand-04-44", "historiographic_claim",
    "赵农认为，汉武帝实行“罢黜百家，独尊儒术”的政策，从黄老之学到独尊儒术，在圣化孔子学说的背景下加强中央集权，从而使儒学成为一种政治伦理的教义。",
    "Zhao Nong holds that Emperor Wu of Han adopted the policy of “dismissing the Hundred Schools and honoring Confucianism alone”; moving from Huang-Lao thought to Confucian orthodoxy, he strengthened central power by sanctifying Confucius's teaching, turning Confucianism into a political-ethical doctrine.",
    [E + "han-wudi-duzun-rushu.md", R + "dong-zhong-shu.md", R + "han-wu-di.md", R + "confucius.md"],
    "断言取 L2513。政策转变与“政治伦理教义”为原文直述；来源把“外儒内法”与圣化孔子并置，未给诏令原文与实施范围。概念见 events/han-wudi-duzun-rushu、persons/dong-zhong-shu、persons/han-wu-di、persons/confucius。",
    2479, 2566, [2513], ["b0098"], "第一节 绪论"))

rows.append(C(
    "claim-0502", "cand-04-41", "historiographic_claim",
    "赵农认为，秦朝虽骤败、功过参半，但后来汉承秦制，新兴的汉帝国在许多方面延续了秦始皇的政治制度。",
    "Zhao Nong holds that although Qin collapsed quickly and is judged with mixed merits, the Han followed Qin institutions, and the new empire continued Qin Shi Huang's political system in many respects.",
    [R + "qin-shi-huang.md", T + "qin-ban-liang.md", T + "han-wu-zhu.md"],
    "断言取 L2492，并以 L2633“汉承秦制，活动的货币也是以黄金和铜钱定制”为制度层面的例子。汉承秦制的具体制度清单未展开；货币例子见 terms/qin-ban-liang、terms/han-wu-zhu。概念见 persons/qin-shi-huang。",
    2479, 2644, [2492, 2633], ["b0098", "b0101"], "第一节 绪论"))

rows.append(C(
    "claim-0503", "cand-04-76", "interpretive_claim",
    "赵农认为，后人推测圆形方孔钱币体现了天圆地方的宇宙观，这仅仅是一种文化的联想；方孔的实际功能是穿木棍便于打磨锉齐并使货币重量统一。",
    "Zhao Nong holds that the later inference that round coins with square holes embody the cosmic scheme of heaven-round and earth-square is merely a cultural association; the square hole's practical function was to take a wooden rod for filing the edges and standardizing weight.",
    [T + "qin-ban-liang.md", T + "tianyuan-difang.md"],
    "断言取 L2627。方孔便于打磨、统一重量为原文功能解释；“仅仅是文化的联想”为作者判断，未给钱范工艺与重量实测。概念见 terms/qin-ban-liang、terms/tianyuan-difang。",
    2618, 2644, [2627], ["b0101"], "第二节 文字与货币"))

rows.append(C(
    "claim-0504", "cand-04-108", "historiographic_claim",
    "赵农认为，度量衡标准的制定和颁布使手工业生产技术和器具的设计有了重要依据；从建筑、兵器、服饰、乐器、车辆到粮食、物什的分配，度量衡愈来愈重要。",
    "Zhao Nong holds that setting and promulgating weights and measures gave craft production and implement design an important basis; from architecture, weapons, dress, instruments, and vehicles to grain and goods distribution, measures grew increasingly important.",
    [T + "qin-quan.md", W + "shang-yang-fang-sheng.md", T + "qin-ban-liang.md"],
    "断言取 L2835 与 L2837。秦权、商鞅方升、秦半两为原文所举统一度量衡的实物与制度例证；度量衡对手工业设计的具体作用未给工艺参数。概念见 terms/qin-quan、works/shang-yang-fang-sheng、terms/qin-ban-liang。",
    2813, 2838, [2835, 2837], ["b0109"], "第四节 兵器与农具"))

rows.append(C(
    "claim-0505", "cand-04-120", "historiographic_claim",
    "赵农指出，《史记·项羽本纪》所记“烧秦宫室，火三月不灭”并未具体指正阿房宫，阿房宫是否修建完毕因此成为悬疑。",
    "Zhao Nong notes that the Shiji account of Xiang Yu “burning the Qin palaces, with fires lasting three months” does not specifically identify the Epang Palace, so whether it was completed remains an open question.",
    [W + "epang-palace.md", B + "efang-palace-fu.md", B + "shiji.md"],
    "断言取 L2909。原文同时引《阿房宫赋》与《史记·秦始皇本纪》“阿房宫未成”，形成赋盛与史疑的张力；未给遗址考古报告。概念见 works/epang-palace、publications/efang-palace-fu、publications/shiji。",
    2891, 2914, [2909], ["b0112"], "第五节 建筑与雕塑"))

rows.append(C(
    "claim-0506", "cand-04-146", "historiographic_claim",
    "赵农认为，革故鼎新的结果往往因人废物，改朝换代、玉石俱焚，破坏大于建设，这也是中国封建社会的一个恶劣传统。",
    "Zhao Nong holds that dynastic change often destroys what the previous order built—people and things alike—so that destruction exceeds construction; he calls this a harmful tradition of Chinese feudal society.",
    [],
    "断言取 L2913。该句紧接阿房宫兴废叙述，是由个案上升的历史判断；“破坏大于建设”为作者评价，来源未给历代都城毁建的统计。库内无对应制度条目，未强行链接。",
    2913, 2913, [2913], ["b0112"], "第五节 建筑与雕塑"))

rows.append(C(
    "claim-0507", "cand-04-128", "interpretive_claim",
    "赵农认为，以兵马俑为陪葬的内容是中国古代陪葬方式的一种极致；已出土的汉代帝王陵墓的陪葬规模和制度，均无法与秦始皇陵及秦兵马俑相比。",
    "Zhao Nong holds that burial with a terracotta army is an extreme of ancient Chinese funerary practice; the scale and system of burial goods in excavated Han imperial tombs cannot compare with the Qin Shi Huang mausoleum and its terracotta army.",
    [W + "qin-bing-ma-yong.md", W + "qin-shi-huang-ling.md"],
    "断言取 L2969。兵马俑为陪葬“极致”、汉陵无法相比为作者评价；来源未给汉陵陪葬坑的统计口径与比较指标。概念见 works/qin-bing-ma-yong、works/qin-shi-huang-ling。",
    2930, 2987, [2969], ["b0114"], "第五节 建筑与雕塑"))

rows.append(C(
    "claim-0508", "cand-05-03", "interpretive_claim",
    "赵农认为，中国古代的墓葬制度建立在土地观念的基础上，这是受农耕文化生产方式影响的结果，因此埋入地下是生者对死者的处置方式。",
    "Zhao Nong holds that ancient Chinese burial institutions rest on ideas of land, shaped by the agricultural mode of production; burial underground is therefore the living's way of disposing of the dead.",
    [T + "fudou-xing-fengtu-fangzhong.md", W + "qin-shi-huang-ling.md"],
    "断言取 L2990。土地观念与农耕生产方式的因果为作者解释；来源未给史前至秦汉墓葬形态的序列统计。概念见 terms/fudou-xing-fengtu-fangzhong、works/qin-shi-huang-ling。",
    2988, 3011, [2990], ["b0115"], "第五节 建筑与雕塑"))

rows.append(C(
    "claim-0509", "cand-05-04", "interpretive_claim",
    "赵农认为，封土植树一是为了祭祀，二是昭示墓主人的权威，是奢侈豪华的生活写照。",
    "Zhao Nong holds that raising mounds and planting trees served first sacrifice and second the display of the tomb owner's authority, mirroring luxurious living.",
    [T + "fudou-xing-fengtu-fangzhong.md", W + "qin-shi-huang-ling.md"],
    "断言取 L2995，并以《礼记·檀弓上》《周易·系辞传下》《周礼·冢人》为文献背景。祭祀与昭示权威两项功能为作者判断；引文未给版本与注疏。概念见 terms/fudou-xing-fengtu-fangzhong、works/qin-shi-huang-ling。",
    2988, 3011, [2995], ["b0115"], "第五节 建筑与雕塑"))

rows.append(C(
    "claim-0510", "cand-05-08", "synthetic_claim",
    "赵农认为，在秦汉国家统一的背景下服饰形成了一种文化规范；丝织业、桑麻业已经非常发达成熟，尤其黄河流域丝绸生产水平的提高推动了服饰文化的进步，丝绸生产业的发达使汉代成为名副其实的丝绸之国。",
    "Zhao Nong holds that under Qin-Han unification dress became a cultural norm; sericulture and textile production were already highly developed, and rising silk output in the Yellow River basin drove dress culture forward, making Han China a true “silk country.”",
    [I + "han-dai-guan-ying-sizhi-zuofang.md", PR + "han-dai-zhijin-cixiu.md",
     W + "susha-chanyi.md", P + "mawangdui-hanmu.md"],
    "断言综合 L3025 与 L3031。“锦绣襄邑”“罗绮朝歌”等产地与《为焦仲卿妻作》诗句为原文论据；丝绸之国为作者评价，未给产量与贸易统计。概念见 institutions/han-dai-guan-ying-sizhi-zuofang、procedures/han-dai-zhijin-cixiu、works/susha-chanyi、places/mawangdui-hanmu。",
    3014, 3049, [3025, 3031], ["b0117"], "第六节 服饰与铜镜"))

rows.append(C(
    "claim-0511", "cand-05-104", "interpretive_claim",
    "赵农指出，丝绸之路的开通对于汉代文化的广泛传播以及西域文化的引进交流有着重要作用。",
    "Zhao Nong states that the opening of the Silk Road played an important role in spreading Han culture and in bringing in cultures from the Western Regions.",
    [T + "sichou-zhilu.md", R + "zhang-qian.md"],
    "断言取 L3036。丝绸之路的文化交流作用为原文判断；来源未给贸易品类、路线长度与使节往返的统计。概念见 terms/sichou-zhilu、persons/zhang-qian。",
    3036, 3036, [3036], ["b0117"], "第六节 服饰与铜镜"))

rows.append(C(
    "claim-0512", "cand-05-109", "interpretive_claim",
    "赵农据《后汉书·逸民列传》孟光“更为椎髻，着布衣，操作而前”的记载，推测椎髻应是一种家居妇女的发式。",
    "Citing the Hou Hanshu account that Meng Guang “changed to a mallet-shaped bun, wore plain cloth, and came forward to work,” Zhao Nong infers that the zhuiji bun was a hairstyle for women at home.",
    [],
    "断言取 L3044 与 L3046。原文明确标为“推测”；《后汉书》引文未给版本与页次，库内无椎髻条目，未强行链接。",
    3044, 3046, [3044, 3046], ["b0117"], "第六节 服饰与铜镜"))

rows.append(C(
    "claim-0513", "cand-05-11", "interpretive_claim",
    "赵农认为，袍子的改变导致了裤子的发展：裤子最初是无裆的“绔”，即无裆的“胫衣”；东汉出现直裾袍，里面的裤子演变为有裆的制式，这是东汉服饰发展的一个主要变化现象。",
    "Zhao Nong argues that changes in the robe drove the development of trousers: trousers were first the crotchless ku, or “leg garment”; with the Eastern Han straight-hem robe, the trousers beneath became crotch-sewn—a major change in Eastern Han dress.",
    [T + "han-dai-pao-fu.md", T + "ku.md"],
    "断言取 L3059-L3061。袍制变化与裤子由无裆到有裆的因果为原文建立，并以东汉画像石为旁证；未给实物测量与图像编年。概念见 terms/han-dai-pao-fu、terms/ku。",
    3050, 3074, [3059, 3061], ["b0118"], "第六节 服饰与铜镜"))

rows.append(C(
    "claim-0514", "cand-05-14", "interpretive_claim",
    "赵农认为，汉镜中的文字常记载制镜人的姓氏，有商标的性质，如“田氏作竟真大好”，常作为商品出售的商标说明；作为社会经济的文化体现，汉镜制作也有着广泛的市场应用。",
    "Zhao Nong holds that Han mirror inscriptions often record the maker's surname and function as trademarks, as in “the Tian family's mirror is truly excellent,” serving as a mark for goods sold; as a cultural expression of the economy, Han mirror making had wide market application.",
    [T + "tongjing.md"],
    "断言取 L3094。“田氏作竟真大好”为原文所举铭文；商标性质与市场应用为作者推断，未给镜铭统计、作坊遗址与流通范围。概念见 terms/tongjing。",
    3075, 3099, [3094], ["b0119"], "第六节 服饰与铜镜"))

rows.append(C(
    "claim-0515", "cand-05-110", "evaluative_claim",
    "赵农认为，汉人十分重视生活质量，所以在生活器皿的设计中有着精致和机巧的特点。",
    "Zhao Nong holds that Han people valued quality of life highly, so their household vessels were designed with refinement and ingenuity.",
    [T + "tongjing.md"],
    "断言取 L3098，前引《为焦仲卿妻作》《陌上桑》诗句。“重视生活质量”与器皿精致机巧的因果为作者判断，未给器物形态与使用场景的量化比较。概念见 terms/tongjing。",
    3098, 3098, [3098], ["b0119"], "第六节 服饰与铜镜"))

rows.append(C(
    "claim-0516", "cand-05-111", "evaluative_claim",
    "赵农认为，生存环境的改善是人们的愿望，同时也是生活知识范围明显提高带来的结果；汉代国力强盛、汉人行走四方，将汉文化辐射到四方并带回各民族的生活物品，因而汉人的精神矫健、文化张扬丰满，显示着汉民族洋洋洒洒的豪迈情怀。",
    "Zhao Nong holds that improving the living environment was both a popular aspiration and a result of greatly expanded practical knowledge; with a strong state and wide travel, Han people spread their culture and brought back goods from other peoples, producing an energetic spirit and expansive, confident culture.",
    [T + "boshanlu.md", W + "cuojin-boshanlu.md"],
    "断言取 L3119，位于香炉节末。博山炉与《薰炉铭》为前文器物背景；精神状态与文化交流的因果为作者评价，未给器物使用阶层与出土分布。概念见 terms/boshanlu、works/cuojin-boshanlu。",
    3119, 3119, [3119], ["b0120"], "第六节 服饰与铜镜"))

rows.append(C(
    "claim-0517", "cand-05-23", "historiographic_claim",
    "赵农认为，造纸术在西汉时期已经出现，1933年新疆罗布泊、1957年西安灞桥相继发现西汉麻纸；蔡伦在东汉时期的研制无疑是一种集大成的推进。",
    "Zhao Nong holds that papermaking already existed in the Western Han, citing Western Han hemp paper found at Lop Nur in 1933 and at Baqiao in Xi'an in 1957; Cai Lun's Eastern Han work was a synthesizing advance.",
    [PR + "zaozhishu.md", R + "cai-lun.md"],
    "断言取 L3129。两处西汉麻纸发现为原文所记；蔡伦“集大成”为史学评价，未给纸样检测报告与蔡侯纸工艺复原。概念见 procedures/zaozhishu、persons/cai-lun。",
    3123, 3141, [3129], ["b0122"], "第七节 造纸与灯具"))

rows.append(C(
    "claim-0518", "cand-05-26", "historiographic_claim",
    "赵农认为，地动仪的出现是中国古代文明光辉灿烂的结晶；这是世界上第一个测量地震的仪器，今人复制了地动仪的木质模型。",
    "Zhao Nong holds that the seismograph is a brilliant crystallization of ancient Chinese civilization; it was the world's first instrument for measuring earthquakes, and a wooden model has been reconstructed in modern times.",
    [W + "houfeng-dizhenyi.md", R + "zhang-heng.md"],
    "断言取 L3148 与 L3150，并引《后汉书·张衡传》详述构造。“世界上第一个”为原文定位，未给同类仪器的跨文明比较；复原模型的可动性未核。概念见 works/houfeng-dizhenyi、persons/zhang-heng。",
    3142, 3155, [3148, 3150], ["b0123"], "第七节 造纸与灯具"))

rows.append(C(
    "claim-0519", "cand-05-31", "interpretive_claim",
    "赵农认为，司南在唐宋时期被指南针替代，原因在于司南准确性不够：司南多为天然磁石所制，加工过程中磁性不断散失，造成方向精准度失偏。",
    "Zhao Nong holds that the sinan was replaced by the magnetic compass in the Tang-Song period because its accuracy was insufficient: made mostly of natural lodestone, it lost magnetism during working, so directional precision declined.",
    [T + "sinan.md", B + "lun-heng.md"],
    "断言取 L3161，并以王充《论衡·是应篇》“司南之杓……其柢指南”为汉代的用法证据。磁性散失导致失准为作者解释，未给磁石剩磁与指向误差的实测。概念见 terms/sinan、publications/lun-heng。",
    3156, 3194, [3161], ["b0124"], "第七节 造纸与灯具"))

rows.append(C(
    "claim-0520", "cand-05-34", "evaluative_claim",
    "赵农评价，长信宫灯是一件构思精妙、意味浓郁的艺术设计作品，其设计思想超越了时空，亦是难得的超凡脱俗的佳作。",
    "Zhao Nong evaluates the Changxin Palace Lamp as an ingeniously conceived and richly meaningful work of design whose ideas transcend time—an exceptionally refined masterpiece.",
    [W + "changxin-palace-lamp.md"],
    "断言取 L3210。虹吸净烟与灯罩调光为原文所记结构；“超越时空”“超凡脱俗”为作者评价，未给灯具尺寸、铸造工艺与烟气净化效果的实测。概念见 works/changxin-palace-lamp。",
    3195, 3227, [3210], ["b0125"], "第七节 造纸与灯具"))

rows.append(C(
    "claim-0521", "cand-05-112", "interpretive_claim",
    "赵农认为，灯具的广泛使用说明汉代人们活动时间的延长以及生活空间的增大；一种器具的应用往往会改变人们的生活经验。",
    "Zhao Nong holds that the wide use of lamps shows that Han people extended their active hours and enlarged their living space; the adoption of an implement often changes lived experience.",
    [T + "dongwuxing-dengju.md", T + "chang-deng.md"],
    "断言取 L3212。碗灯、豆灯、盘灯与各阶层选择为 L3214 的补充；“活动时间延长、生活空间增大”为作者推论，未给照明时长与室内面积的实测。概念见 terms/dongwuxing-dengju、terms/chang-deng。",
    3212, 3212, [3212], ["b0125"], "第七节 造纸与灯具"))

rows.append(C(
    "claim-0522", "cand-05-113", "interpretive_claim",
    "赵农认为，灯具的大量使用对人们的生活质量和精神意识有积极提高，使黑夜不再黑暗；从生活功能到审美意识的改变也推动了社会生产水平的提高。",
    "Zhao Nong holds that the mass use of lamps actively raised Han people's quality of life and spiritual awareness, so that night was no longer dark; changes from practical function to aesthetic awareness also drove production forward.",
    [W + "changxin-palace-lamp.md", T + "dongwuxing-dengju.md"],
    "断言取 L3218 与 L3226（中间隔图注）。“推动社会生产水平提高”为作者评价，未给灯具产量、作坊规模与照明成本的统计。概念见 works/changxin-palace-lamp、terms/dongwuxing-dengju。",
    3218, 3226, [3218, 3226], ["b0125"], "第七节 造纸与灯具"))

rows.append(C(
    "claim-0523", "cand-05-36", "historiographic_claim",
    "赵农认为，秦汉开始了中华民族的统一，这是中国社会繁荣强大的基础；秦汉王朝疆域的拓展为后世中国发展规划了辽阔的社会舞台和空间；国家制度、经济水平与文化规范的成熟，使中国社会此后能够不断调整发展机制，即使遭遇政体动摇、纲纪涣散、战乱叠生，仍能在历史进步中实现国家统一与民族融合，从而避免了欧洲中世纪长期政教合一的历史悲剧。",
    "Zhao Nong holds that Qin-Han unification began the unification of the Chinese nation and laid the basis for prosperity; territorial expansion opened a vast stage for later China, and mature state institutions, economy, and cultural norms enabled society to adjust its mechanisms repeatedly—preserving unity and ethnic integration even amid dynastic crisis and war, and thus avoiding Europe's long medieval theocracy.",
    [R + "qin-shi-huang.md", R + "han-wu-di.md", W + "qin-han-changcheng.md", P + "han-chang-an.md"],
    "断言取 L3240-L3242。统一、制度成熟与自我调整的长时段判断为作者立论，并以欧洲中世纪政教合一作比较；未给制度指标与欧洲史分期依据。概念见 persons/qin-shi-huang、persons/han-wu-di、works/qin-han-changcheng、places/han-chang-an。",
    3236, 3248, [3240, 3242], ["b0127"], "第八节 结论"))

rows.append(C(
    "claim-0524", "cand-05-37", "evaluative_claim",
    "赵农评价，秦汉时期的艺术设计历史伴随时代洪流衍生出自己的华章，展示磅礴大气的风韵；人们在衣食住行各方面开始认识和使用器具，设计发明了许多创造性器物，提高了中华民族的社会生活品质，并在设计实践中展示了秦汉文化的精神内涵。",
    "Zhao Nong evaluates Qin-Han design history as producing its own brilliant chapter amid the era's currents, displaying a grand and expansive character; in clothing, food, housing, and travel people came to know and use implements, invented many creative vessels, raised the quality of life, and expressed the spiritual content of Qin-Han culture through design.",
    [W + "qin-bing-ma-yong.md", W + "changxin-palace-lamp.md"],
    "断言取 L3247。衣食住行与创造性器物的总括为作者评价；兵马俑与长信宫灯为本册代表性器物，未给器物谱系与使用阶层的统计。概念见 works/qin-bing-ma-yong、works/changxin-palace-lamp。",
    3236, 3248, [3247], ["b0127"], "第八节 结论"))

for row in rows:
    assert row["statement_zh"].strip() and row["statement_en"].strip()

(ROOT / "_zn_zn4a_rows.json").write_text(
    json.dumps(rows, ensure_ascii=False, indent=1) + "\n", encoding="utf-8", newline="\n")
(ROOT / "_zn_zn4a_patch.json").write_text("[]\n", encoding="utf-8", newline="\n")

from collections import Counter
print(json.dumps({
    "rows": len(rows),
    "types": dict(Counter(r["claim_type"] for r in rows)),
    "links": sum(len(r["supported_by"]) for r in rows),
    "distinct": len({p for r in rows for p in r["supported_by"]}),
}, ensure_ascii=False))
