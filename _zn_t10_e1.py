# -*- coding: utf-8 -*-
"""T10 entries, part 1: Yuan ceramics, glaze, glass, and embroidery."""

DEFAULT_REL = "relation 未审查，不写入正式 `relations`。"


def W(slug, plain, en, sub, tags, desc, points, quality, dim, sec, conf, scope, lines,
      aliases=None, rel=None):
    return {
        "slug": slug, "dir": "works", "type": "work", "sub": sub,
        "title": plain, "plain": plain, "en": en,
        "tn": f"来源未提供英文名；{en} 为描述性说明，故标 provisional。",
        "tags": tags, "aliases": aliases or [], "desc": desc, "points": points,
        "rel": rel or DEFAULT_REL,
        "quality": quality, "dim": dim, "sec": sec, "conf": conf,
        "scope": scope, "lines": lines, "meta": {},
    }


def TER(slug, plain, en, sub, tags, desc, points, quality, dim, sec, conf, scope, lines,
        aliases=None, rel=None):
    return {
        "slug": slug, "dir": "terms", "type": "term", "sub": sub,
        "title": plain, "plain": plain, "en": en,
        "tn": f"来源未提供英文名；{en} 为描述性说明或通行译名，故标 provisional。",
        "tags": tags, "aliases": aliases or [], "desc": desc, "points": points,
        "rel": rel or DEFAULT_REL,
        "quality": quality, "dim": dim, "sec": sec, "conf": conf,
        "scope": scope, "lines": lines, "meta": {},
    }


def PER(slug, plain, en, sub, tags, desc, points, quality, dim, sec, conf, scope, lines,
        aliases=None, rel=None):
    return {
        "slug": slug, "dir": "persons", "type": "person", "sub": sub,
        "title": plain, "plain": plain, "en": en,
        "tn": f"来源未提供英文名；{en} 为音译加身份说明，故标 provisional。",
        "tags": tags, "aliases": aliases or [], "desc": desc, "points": points,
        "rel": rel or DEFAULT_REL,
        "quality": quality, "dim": dim, "sec": sec, "conf": conf,
        "scope": scope, "lines": lines, "meta": {},
    }


E = [
    W(
        "lanyou-miaojin-yi", "蓝釉描金匜", "Blue-Glazed Gilt-Decorated Yi Ewer", "porcelain_vessel",
        ["元代", "景德镇窑", "蓝釉", "描金", "保定", "瓷器"],
        "蓝釉描金匜是1964年保定出土的元代中期景德镇窑瓷器。来源记瓷匜通体蓝釉，内面用金绘出流云及折枝花；蓝釉和金彩互相衬托，有的器物突出花纹部分，而将花纹以外的地方挂蓝釉，产生蓝与白的色彩对比，显得庄重而高雅。来源未给尺寸、窑口、藏地与图版。",
        [
            "**date**: 元代中期（来源；1964年保定出土）",
            "**器名与出土（L3977）**: “1964年，保定出土的蓝釉描金匜，是元代中期所产的一件珍品。”",
            "**釉色与装饰（L3977）**: “瓷匜通体蓝釉，内面用金绘出流云及折枝花。”",
            "**色彩处理（L3977）**: “蓝釉和金彩互相衬托，有的则是突出花纹部分，而将花纹以外的地方挂蓝釉，使产生蓝与白的色彩对比，显得庄重而高雅。”",
            "**品种背景（L3977）**: “元代景德镇窑除烧制影青外，还烧成了一种蓝釉。”",
            "**原文未载**: 尺寸、重量、窑口、藏地、图版、同出器物",
        ],
        "L3977 一段给器名、出土年份与地点、时代判断、通体蓝釉、内面金绘流云折枝花与两种蓝白对比处理；尺寸、窑口与藏地未载。",
        "B", ["C"], "medium",
        "本条是 B 维度元代景德镇窑蓝釉描金瓷匜的单器锚点，金绘流云折枝花的纹样属 C 维度。Theme/Topic 尚未 materialize。",
        "L3977",
        rel="`places/jingdezhen-kiln.md` 已引 L3977 记同一件匜，本条为单器展开，不重复窑口总述；`terms/blue-and-white-porcelain.md` 记青花，`terms/youlihong.md` 记釉里红，与本条同属元代景德镇彩釉品种。relation 未审查。",
    ),
    W(
        "qinghua-baleng-longwen-ping", "青花八棱海水龙纹瓶", "Blue-and-White Octagonal Dragon-and-Wave Vase", "porcelain_vessel",
        ["元代", "青花", "八棱瓶", "海水龙纹", "图注"],
        "青花八棱海水龙纹瓶是田自秉册插图1所注的元代青花器。图注只记器名与时代，正文青花段未对这件瓶作形制、纹样、尺寸或藏地说明。本条只据图注立条，图版未视觉核验。",
        [
            "**date**: 元代（图注）",
            "**图注（L3992）**: “青花八棱海水龙纹瓶”",
            "**图版位置（L3991、L3992）**: 插图1，位于青花起源与流行段之后；图注原文作“青花八棱海水龙纹瓶(元)”。",
            "**器形与纹样**: 仅据器名知为八棱瓶，饰海水龙纹；来源未给尺寸、胎釉、款识、藏地与出土信息。",
            "**证据边界**: 图注是唯一来源，正文未描述此器；不据器名推补画面细节。",
            "**原文未载**: 尺寸、胎釉、款识、藏地、出土、图版核验",
        ],
        "仅 L3992 图注一行，器名与时代可证；其余全缺。",
        "B", ["C"], "low",
        "本条是 B 维度元代青花单器的图注锚点，海水龙纹的纹样属 C 维度。Theme/Topic 尚未 materialize。",
        "L3991, L3992",
        rel="`terms/blue-and-white-porcelain.md` 记元代青花起源、钴料与成熟时序；`places/jingdezhen-kiln.md` 记景德镇窑青花；本条为图注单器锚点。relation 未审查。",
    ),
    W(
        "sancai-longfeng-liuliyou-xianglu", "三彩龙凤琉璃釉香炉", "Sancai Dragon-and-Phoenix Glazed Censer", "sancai_vessel",
        ["元代", "琉璃", "三彩", "香炉", "元大都", "龙凤纹"],
        "三彩龙凤琉璃釉香炉是元大都出土的元代琉璃器。来源记炉身浮雕凤纹（原文作风纹），炉顶塑成山形，有一龙盘绕其间，蓝色和黄色琉璃釉相互衬映，形象庄重大方；来源把它与任塘刻铭琉璃香炉并列为出色的元代琉璃作品。来源未给尺寸、藏地、窑口与图版。",
        [
            "**date**: 元（来源；元大都出土）",
            "**出土与器名（L4026）**: “另一元大都出土的三彩龙凤琉璃香炉”",
            "**炉身与炉顶（L4026）**: “炉身浮雕风纹，炉顶塑成山形，有一龙盘绕其间，蓝色和黄色琉璃釉相互衬映，形象庄重大方”",
            "**原文异文（L4026）**: 原文作“风纹”，按器名及上下文疑为凤纹，照录不改。",
            "**同段评语（L4026）**: “都是出色的元代琉璃作品（插图3）。”",
            "**图注（L4020）**: “三彩龙凤琉璃釉香炉”",
            "**原文未载**: 尺寸、重量、窑口、藏地、图版核验",
        ],
        "L4026 给器名、出土、炉身浮雕、炉顶山形与龙、蓝黄釉对比和庄重大方的评语；L4020 图注给器名与时代；尺寸、窑口与藏地未载。",
        "B", ["C"], "medium",
        "本条是 B 维度元代琉璃香炉的单器锚点，龙凤纹与蓝黄釉配色属 C 维度。Theme/Topic 尚未 materialize。",
        "L4020, L4026",
        rel="`terms/liuli.md` 记琉璃的建筑砖瓦义、铅釉陶与元代山西产地；`persons/rentang.md` 同批记同段任塘刻铭琉璃香炉；`places/yuan-dadu.md` 记元大都。relation 未审查。",
    ),
    PER(
        "rentang", "任塘", "Ren Tang", "craftsman",
        ["元代", "琉璃", "汾阳", "待诏", "香炉", "至大元年"],
        "任塘是元代至大年间的汾阳琉璃待诏。来源记故宫博物院藏有至大元年汾阳琉璃待诏任塘刻铭的琉璃香炉，炉身浮雕牡丹、莲花、龙纹等。来源未给任塘的生卒、籍贯细节、师承、作坊与其它作品。",
        [
            "**name_original**: 任塘",
            "**时代**: 元至大元年（来源作“至大元年”）",
            "**身份（L4026）**: “故宫博物院藏有至大元年汾阳琉璃待诏任塘刻铭的琉璃香炉”",
            "**作品纹样（L4026）**: “炉身浮雕牡丹、莲花、龙纹等”",
            "**职名说明**: 琉璃待诏为来源所记职名，属官府琉璃工匠；来源未给所属机构、品秩与任职方式。",
            "**原文未载**: 生卒、籍贯、师承、作坊、作品数量、刻铭全文",
        ],
        "L4026 一句给时代、汾阳籍、职名、刻铭与藏器纹样；生平与作坊未载。",
        "B", ["D"], "low",
        "本条是 B 维度元代琉璃工匠的人物锚点，琉璃待诏的官府身份属 D 维度。Theme/Topic 尚未 materialize。",
        "L4026",
        rel="`terms/liuli.md` 记元代琉璃与山西产地；`works/sancai-longfeng-liuliyou-xianglu.md` 同批记同段元大都出土香炉，来源未说与任塘作品的关系；`places/yuan-dadu.md` 记元大都。relation 未审查。",
    ),
    TER(
        "huoshidi", "火石底", "Huoshidi (Firestone Base)", "ceramic_technique",
        ["元代", "陶瓷", "胎体", "护胎釉", "火石底"],
        "火石底是元代陶瓷胎体处理方式的俗称。来源记元代陶瓷胎质厚重，多有杂质斑点，常在胎上涂一层护胎釉，俗称火石底。来源未给护胎釉的原料、配比、施涂方法、烧成温度与产地差异。",
        [
            "**时代**: 元",
            "**定义（L3998）**: “元代陶瓷的造型，胎质厚重，多有杂质斑点。常在胎上涂一层护胎釉，俗称‘火石底’。”",
            "**工艺位置**: 属胎体表面处理，在施釉与彩绘之前，与釉色、纹饰分列。",
            "**原文未载**: 护胎釉原料、配比、施涂方法、烧成温度、产地差异",
        ],
        "L3998 一句给胎质、杂质斑点、护胎釉与俗称；工艺细节全缺。",
        "B", [], "medium",
        "本条是 B 维度元代陶瓷胎体处理的术语，护胎釉与烧成的关系属工艺技术。Theme/Topic 尚未 materialize。",
        "L3998",
        rel="`places/jingdezhen-kiln.md` 记景德镇窑胎釉与品种；`terms/blue-and-white-porcelain.md` 与 `terms/youlihong.md` 记元代景德镇彩瓷；本条为胎体处理术语，不与釉色条合并。relation 未审查。",
    ),
    TER(
        "yuan-dai-cixiu-zhenfa", "元代刺绣针法", "Yuan Embroidery Stitch Types", "embroidery_type",
        ["元代", "刺绣", "针法", "辫针", "平针", "打子", "抢针"],
        "元代刺绣针法是田自秉册所举元代已使用的七种刺绣针法。来源称现今刺绣工艺中的一些主要针法在元代就已使用，并分别介绍辫针、平针、打子、抢针、鳞针、网针、切针的名称、别称与表现效果。来源未给各针法的起落、行针方向、用线股数、底料与针具。",
        [
            "**时代**: 元",
            "**总述（L4084）**: “现今刺绣工艺中的一些主要针法，在元代就已使用。”",
            "**辫针（L4086）**: “这是一种历史悠久的针法，也是使用最早的一种刺绣法。”原文又称“现今称为‘拉梭子’”，特点为“具有牢固和纹样清晰的特点，适于表现线条”。",
            "**平针（L4088）**: “它能表现出光洁的平面。”",
            "**打子（L4090）**: “针路形成一圈一圈的小球，适于表现花心或各种点状物。”",
            "**抢针（L4092）**: “是表现物象色彩深浅浓淡的一种针法。它既可由浅到深，也可由深到浅。使产生退晕的效果和层次的变化，富有装饰感。”",
            "**鳞针、网针、切针（L4094、L4096、L4098）**: 鳞针“表现鱼鳞般的形状，适于表现鱼身，或在大的面积中使用”；网针“针法编织成各种几何形网状”；切针“用于表现轮廓线的整齐划一”。",
            "**原文未载**: 各针法起落、行针方向、用线股数、底料、针具、元代实物对应关系",
        ],
        "L4084-L4098 逐条给七种针法的名称、别称与效果；操作细节与实物对应未载。",
        "B", ["C"], "medium",
        "本条是 B 维度元代刺绣针法的清单级术语，针法形成的纹样效果属 C 维度。Theme/Topic 尚未 materialize。",
        "L4084, L4086, L4088, L4090, L4092, L4094, L4096, L4098",
        rel="`procedures/bian-xiu.md` 记辫绣历代沿革与清代拉梭子称谓；`procedures/yun-jian-xiu.md` 记唐代纭裥绣与抢针绣别名；本条把元代七种针法作清单级术语，不重复单针法沿革。relation 未审查。",
    ),
    W(
        "jininglu-cixiu-jiashan", "集宁路刺绣夹衫", "Jininglu Embroidered Jacket", "embroidered_garment",
        ["元代", "刺绣", "夹衫", "集宁路", "内蒙古", "人物故事"],
        "集宁路刺绣夹衫是内蒙古集宁路故城遗址元代窖藏所出刺绣服饰。来源记夹衫在两肩及前胸部位用刺绣装饰，绣有多种动物、植物与人物故事纹样；并判断其具有江南刺绣特点，可能在江南制作，或由江南绣工在北方官府工场制作。来源未给尺寸、形制、底色、针法组合与藏地。",
        [
            "**date**: 元",
            "**出土（L4100）**: “在内蒙古自治区集宁市附近的元代集宁路故城遗址，曾发现元代窖藏的一批丝织品，其中有刺绣夹衫一件”",
            "**装饰部位（L4100）**: “在两肩及前胸部位均用刺绣装饰，绣有多种纹样。”",
            "**动物纹（L4100）**: “动物纹有仙鹤、凤凰、野兔、角鹿、彩蝶、双鲤、鹭鸶、乌龟等”",
            "**植物纹（L4100）**: “植物纹有荷花、野菊、水草、芦苇、牡丹、幽兰、灵芝、百合、牵牛、竹叶以及云纹等。”",
            "**人物故事（L4100）**: “一女子盘坐在莲池旁的柳树下，凝视池中鸳鸯戏水；一男子头戴幞头，坐于枫树下；另一女子骑着驴扬鞭驱行在树林间；还有一幅表现人们游乐的湖舟图。”",
            "**产地判断（L4100）**: “这些刺绣具有江南地区刺绣的特点，也表现了江南地区的景色，可能是在江南地区制作的，或者是在北方官府工场，由来自江南的绣工制作的。”",
            "**原文未载**: 尺寸、形制、底色、针法组合、藏地、图版",
        ],
        "L4100 一段给遗址、窖藏、夹衫、装饰部位、三类纹样与产地推测；尺寸、针法与藏地未载。",
        "B", ["C", "E"], "medium",
        "本条是 B 维度元代刺绣服饰的单器锚点，纹样题材属 C 维度，江南与北方官府工场的制作推测属 E 维度。Theme/Topic 尚未 materialize。",
        "L4100",
        rel="`institutions/bintieju.md` 引集宁路总管府遗址的冶铁遗存，与本条同为集宁路考古材料但工艺门类不同；`terms/yuan-dai-cixiu-zhenfa.md` 记元代七种针法，来源未说夹衫所用针法。relation 未审查。",
    ),
]
