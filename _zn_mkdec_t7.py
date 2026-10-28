# -*- coding: utf-8 -*-
"""Build the batch T7 (Six Dynasties) decision file."""
import json
from collections import Counter
from pathlib import Path

ROOT = Path(r"D:/中国设计史研究")
DOC = "2010-tianzibing-zhongguo-gongyi-meishushi"

D = []


def add(cand, entity, action, target, analysis, approve, apply_note):
    D.append({
        "cid": f"{DOC}:cand-{cand}",
        "entity": entity,
        "action": action,
        "target": target,
        "analysis": analysis,
        "approve": approve,
        "apply_note": apply_note,
        "note": f"canonical: {target}。cand-{cand} 记 no_delta，并入该条。" if action == "no_delta"
        else f"canonical: {target}。",
    })


# ---- D: institutions ----
add("07-44", "六朝工匠制度（百工、番役、纳资代役）", "create",
    "04-knowledge/units/terms/liuchao-gongjiang-zhidu.md",
    "候选为六朝工匠制度（L2721）。检索发现 `terms/gong-zu-tu.md` 记汉代工、卒、徒与工巧奴，`terms/liuchao-gongjiang-zhidu` 不存在；institutions 下亦无百工户籍或番役条。新建术语条：记三国已有独立户籍的百工、东晋番役、南朝纳资代役、手工业者可经营自己的手工业、部分脱离旧人身依附关系，并保留来源“促进某些工艺品种发展”的因果判断与缥瓷、蜀锦二例。来源未给百工人数、番役年限、纳资数额与南北差异，confidence 取 medium。",
    "批准新建 04-knowledge/units/terms/liuchao-gongjiang-zhidu.md：单册单源，consensus=tentative；与汉代工卒徒条分工互指。",
    "写入 terms/liuchao-gongjiang-zhidu.md（新建）；引用 L2721；制度年代与数额作未载。")

# ---- persons: literary mentions ----
add("07-55", "潘岳", "no_delta",
    "04-knowledge/units/terms/piao-ci.md",
    "候选为潘岳（L2745）。检索发现 `terms/piao-ci.md` 已引 L2745-L2753，正文明确记“晋潘岳《笙赋》‘倾缥瓷以酌酝’”，并在核心内容列出该文献。田自秉本段只把潘岳作为《笙赋》作者引出，未给生卒、籍贯、官职、文集与其他工艺记载；单独立条会得到只有一句赋文的空条。故 no_delta，文献线索留在缥瓷条内。",
    "不新建潘岳条；已有 terms/piao-ci.md 保存《笙赋》引文与语境。",
    "cand-07-55 记 no_delta，target 指向 terms/piao-ci.md。")

add("07-50", "杜毓", "no_delta",
    "04-knowledge/units/places/ou-kiln.md",
    "候选为杜毓（L2753）。检索发现 `places/ou-kiln.md` 已引 L2753，正文记“杜毓《薈赋》‘器择陶拣，出自东瓯’”，并保留书名 OCR 疑为《荈赋》的存疑标记。田自秉本段只把杜毓作为赋作者引出，未给生卒、籍贯、官职与著作；单独立条会得到只有一句赋文的空条。故 no_delta，文献线索留在瓯窑条内。",
    "不新建杜毓条；已有 places/ou-kiln.md 保存《薈赋》引文与存疑。",
    "cand-07-50 记 no_delta，target 指向 places/ou-kiln.md。")

# ---- B: ceramics ----
add("07-56", "盘口壶", "create",
    "04-knowledge/units/terms/pan-kou-hu.md",
    "候选为盘口壶（L2771）。检索发现 `terms/tianji-hu.md` 记鸡头壶，并称其在盘口壶基础上加鸡头与把手，但不承担盘口壶本身的形制；`works/hei-you-si-xi-pan-kou-hu.md` 记德清窑单件黑釉四系盘口壶，`places/yue-kiln.md` 只列品种名。新建术语条：记鼓腹、细颈、盘形口、肩系二或四等距、平底、有盖，补 L2827 平底、系耳、晚期桥耳与由浑圆向修长的总势，并明确其与天鸡壶的祖型关系。插图1-①未视觉核验；来源未给尺寸、分期与窑口归属，confidence 取 medium。",
    "批准新建 04-knowledge/units/terms/pan-kou-hu.md：单册单源，consensus=tentative；与天鸡壶条分工互指。",
    "写入 terms/pan-kou-hu.md（新建）；引用 L2771、L2786、L2827；不据插图1补比例与釉色。")

add("07-59", "黄釉瓷扁壶", "create",
    "04-knowledge/units/works/huangyou-ci-bianhu.md",
    "候选为河南安阳北齐墓黄釉瓷扁壶（L2791-L2793）。检索发现 `terms/huangyou.md` 记黄釉，`terms/hunping.md` 为本批同建六朝明器条，works 下无此壶；`places/` 下无安阳条。新建器物条：记黄色釉、两面舞乐浮雕人物、一人在莲花上舞蹈、左右各二人弹琵琶击钹吹笛打拍、精美陶瓷工艺品与中外文化交流的判断，并补扁壶为战国以来北方特殊壶式的背景。插图2未视觉核验；来源未给尺寸、墓号、藏地与胎质，confidence 取 medium。",
    "批准新建 04-knowledge/units/works/huangyou-ci-bianhu.md：单册单源，consensus=tentative。",
    "写入 works/huangyou-ci-bianhu.md（新建）；引用 L2793；不据插图2补人物服饰与乐器形制。")

add("07-60", "魂瓶", "create",
    "04-knowledge/units/terms/hunping.md",
    "候选为魂瓶（L2817）。检索发现 `terms/mingqi.md` 记明器通名，`procedures/liuchao-qingci-zhuangshi-liufa.md` 记六朝青瓷装饰六法，均不含魂瓶的器名、源流与堆饰；terms 下无魂瓶条。新建术语条：记魂亭、神亭、谷仓三名，东汉五联罐来源，坛形，亭台人物鸟兽堆饰，蜥蜴窜洞、老鼠奔跑、龟鳖爬行、鸟雀飞翔，人物守望驱雀与牌楼碑亭，手捻堆贴成饰，并录“所堆之物，取子孙繁衍，六畜繁息之意。以妥死者之魂，而慰生者之望”的用途引文。插图4未视觉核验；来源未给尺寸、墓葬、窑口与纪年，confidence 取 medium。",
    "批准新建 04-knowledge/units/terms/hunping.md：单册单源，consensus=tentative；谷仓别名不当作储存功能证据。",
    "写入 terms/hunping.md（新建）；引用 L2817；不据插图4补堆塑层次与釉色。")

# ---- C: motifs and brick painting ----
add("07-63", "莲花纹", "create",
    "04-knowledge/units/terms/lianhua-wen.md",
    "候选为莲花纹（L2851）。检索发现 `works/lianhua-zun.md` 与 `works/lianhua-qingci-tuowan.md` 记单件莲花装饰器物，`terms/rendong-wen.md` 记并行的忍冬纹，terms 下无莲花纹条。新建术语条：记东晋北魏以后流行、与佛教结合达极盛、跨铜器金银器砖瓦石刻藻井柱础的分布，楚国欣赏传统、芙蓉芙蕖水芝水花荷华五别名、《楚辞》两句、观莲节、新郑立鹤方壶与蔡侯墓铜器、武氏祠与沂南石刻，保留来源对印度传来说的反驳，并记早晚花瓣瘦长与肥硕、刻划与浅浮雕的手法差异。来源未给单元尺寸、瓣数与配色，confidence 取 medium。",
    "批准新建 04-knowledge/units/terms/lianhua-wen.md：单册单源，consensus=tentative；反印度说标为来源判断。",
    "写入 terms/lianhua-wen.md（新建）；引用 L2851；不据莲花尊、托碗补纹样单元。")

add("07-66", "邓县画象砖", "no_delta",
    "04-knowledge/units/places/dengxian-xuezhuang-huaxiangzhuan-mu.md",
    "候选为邓县画象砖（L2879-L2881）。检索发现 `places/dengxian-xuezhuang-huaxiangzhuan-mu.md` 已据田自秉 L2879、L2881 立条，记 1957 年邓县学庄画像砖墓、题材与画像砖工艺，并标出墓室尺寸、砖数与年代未载。本候选所指与该条为同一墓的同一批画像砖，田自秉本段未增加可独立成条的砖数、尺寸或单砖画面；故 no_delta，不另建重复条目。",
    "不新建邓县画象砖条；已有 places/dengxian-xuezhuang-huaxiangzhuan-mu.md 覆盖。",
    "cand-07-66 记 no_delta，target 指向 places/dengxian-xuezhuang-huaxiangzhuan-mu.md。")

add("07-67", "竹林七贤和荣启期砖画", "create",
    "04-knowledge/units/works/zhulin-qixian-rongqiqi-zhuanhua.md",
    "候选为竹林七贤和荣启期砖画（L2883-L2896）。检索发现 `terms/zhu-lin-qi-xian.md` 记七贤群体的思想与文学史评价，明言未列全七人姓名，也不承担砖画；`terms/huaxiangzhuan.md` 记画像砖类型；works 下无此砖画条。新建器物条：记南京西善桥、丹阳胡桥、丹阳建山三处发现与西善桥代表，七贤加荣启期八人，逐人典故与三种神态，名士主题对孔老先贤题材的取代、门阀士族与玄学背景、翠竹青松银杏垂柳陪衬、200多块砖拼合与制陶杰作评价。来源未给尺寸、墓主、画面分配与藏地，confidence 取 medium。",
    "批准新建 04-knowledge/units/works/zhulin-qixian-rongqiqi-zhuanhua.md：单册单源，consensus=tentative；与七贤群体条分工互指。",
    "写入 works/zhulin-qixian-rongqiqi-zhuanhua.md（新建）；引用 L2883、L2896；200多块为来源计数。")

# ---- B: textiles ----
add("08-04", "橦华布", "create",
    "04-knowledge/units/terms/tonghua-bu.md",
    "候选为橦华布（L2906）。检索发现 `terms/ma-bu.md` 与 `terms/ma-zhi.md` 记麻布麻织，`terms/jingjin.md` 记蜀锦，terms 下无橦华布或黄润布条。新建术语条：记《蜀都赋》橦华布与黄润布两名、刘逵注橦为树名、花柔毳可绩为布、出永昌，保留田自秉“实际上这是一种棉布”的判断，并记黄润为筒中细布、筒指装布竹筒、亦称筒中黄润。来源未给幅宽、产量、棉种与织法，confidence 取 medium。",
    "批准新建 04-knowledge/units/terms/tonghua-bu.md：单册单源，consensus=tentative；棉布判断标为来源判断。",
    "写入 terms/tonghua-bu.md（新建）；引用 L2906；不判草棉或木棉。")

add("08-05", "苏氏（窦滔妻）", "create",
    "04-knowledge/units/persons/su-shi-qianqin.md",
    "候选为前秦窦滔妻苏氏（L2910）。检索发现 `persons/su-shi.md` 已存在，为宋代苏轼，与本候选同名异物；为避免 slug 冲突，本条采用 `su-shi-qianqin`，以时代限定，不改既有苏轼条。新建人物条：记前秦秦州刺史窦滔之妻、著名染织工艺家、能用双手织出回文诗句称回文锦、来源对工艺造诣与文学才能的评价。来源只称苏氏，未给名字、生卒、籍贯与回文锦尺寸、字数、存佚，confidence 取 low。",
    "批准新建 04-knowledge/units/persons/su-shi-qianqin.md：单册单源，consensus=tentative；slug 加时代限定以别于苏轼。",
    "写入 persons/su-shi-qianqin.md（新建）；引用 L2910；不补名为苏蕙，不另立回文锦作品条。")

add("08-08", "鸟兽纹绮（晋）", "create",
    "04-knowledge/units/works/niaoshou-wen-qi.md",
    "候选为晋代鸟兽纹绮（L2924-L2925，图注 L2925）。检索发现 `terms/jingjin.md` 记经锦，`terms/yunqi-wen.md` 记汉代云气纹，works 下无鸟兽纹绮条。新建器物条：以插图11 图注“鸟兽纹绮(晋)”为名称依据，记六朝丝织纹样改变汉代云气纹不规则格式、构成规则波状骨架、样式化并形成几何分割线的总述，并明确该总述为六朝丝织的“主要的艺术特点”、不专属本件；另以 L2472 汉代绮的斜纹二重经组织作工艺背景。插图11未视觉核验；来源未给尺寸、组织、经纬密度、墓号与藏地，confidence 取 medium。",
    "批准新建 04-knowledge/units/works/niaoshou-wen-qi.md：单册单源，consensus=tentative；总述与本件分开著录。",
    "写入 works/niaoshou-wen-qi.md（新建）；引用 L2925、L2922；不据图注补鸟兽种类。")

add("08-09", "敦煌莫高窟125～126窟北魏刺绣", "create",
    "04-knowledge/units/works/dunhuang-125-126-ku-xiu.md",
    "候选为敦煌莫高窟125～126窟北魏刺绣（L2931）。检索发现 `places/dunhuang-mogao-ku.md` 记莫高窟，`terms/rendong-wen.md` 与 `terms/tangcao-wen.md` 记两种纹样，works 下无此刺绣条。新建器物条：记1965年发现、一佛二菩萨说法图、黄褐地辫绣、红黄绿紫蓝五色、女供养人高冠对襟长衫与桃形忍冬纹卷草纹边饰、圆圈纹与龟背纹套叠及垂直分割关系、分色、几何图案评价与珍贵刺绣作品的定性，并与 L2929《拾遗记》文献刺绣分开著录。来源未给尺寸、片数、藏地与出土编号，confidence 取 medium。",
    "批准新建 04-knowledge/units/works/dunhuang-125-126-ku-xiu.md：单册单源，consensus=tentative。",
    "写入 works/dunhuang-125-126-ku-xiu.md（新建）；引用 L2931；不据“一佛二菩萨”推造像样式。")

# ---- B: mirrors ----
add("08-11", "六朝铜镜", "create",
    "04-knowledge/units/terms/liuchao-tongjing.md",
    "候选为六朝铜镜（L2939-L2945，并及 L2947、L2951）。检索发现 `terms/tongjing.md` 记铜镜通名与战国形制，`terms/hanjing.md` 记汉代铜镜，`terms/tangjing.md` 记唐镜，`works/wu-zixu-huaxiang-jing.md` 已据 L2947、L2949 单独立条；六朝一段无期别条。新建术语条：记早期草略、晚期纤巧工整、流行纪年铭文与龙虎、翔鹤飞鸿、兽形生肖三类花纹，分述三镜的装饰与出土地，记绍兴浮雕与四类题材但把伍子胥画像镜留给单器条，并录工匠姓氏与两例纪年及私人商品生产的判断。来源未给直径、重量、镜背布局、合金配比与藏地，confidence 取 medium。",
    "批准新建 04-knowledge/units/terms/liuchao-tongjing.md：单册单源，consensus=tentative；与通名、汉镜、唐镜条分工互指。",
    "写入 terms/liuchao-tongjing.md（新建）；引用 L2939-L2945、L2947、L2951；伍子胥镜不重复著录。")

# ---- B: lacquer and sculpture ----
add("08-14", "戴逵", "create",
    "04-knowledge/units/persons/dai-kui.md",
    "候选为戴逵（L2963）。检索发现 `persons/gu-kai-zhi.md` 明确记“谢赫、戴逵、曹仲达、张僧繇尚未成 KU”，并在佛教艺术一节把顾恺之与戴逵并列；persons 下无戴逵条。新建人物条：记晋代雕塑家、以能制作夹纻行像著名、为南京瓦棺寺制作夹纻佛像五躯、与顾恺之维摩诘像及狮子国玉像并称瓦棺寺三绝，并给夹纻作法与行像的背景。来源未给生卒、籍贯、师承与其他作品，confidence 取 medium。",
    "批准新建 04-knowledge/units/persons/dai-kui.md：单册单源，consensus=tentative；与顾恺之条分工互指。",
    "写入 persons/dai-kui.md（新建）；引用 L2963；不补生卒、籍贯与官职。")

add("08-15", "南京瓦棺寺夹纻佛像", "create",
    "04-knowledge/units/works/waguan-si-jiazhu-foxiang.md",
    "候选为南京瓦棺寺夹纻佛像（L2963）。检索发现 `procedures/jiazhu-tai.md` 已记夹纻胎作法与行像，`persons/gu-kai-zhi.md` 记顾恺之与维摩诘像，works 下无瓦棺寺五躯条。新建器物条：记戴逵为南京瓦棺寺制作五躯夹纻佛像、与顾恺之维摩诘像及狮子国玉像并称三绝、夹纻以漆灰造形麻布粘贴为胎且战国两汉已流行、佛教盛行后装车游行称行像、比铜佛轻便比泥佛坚固、引《洛阳伽蓝记》多记夹纻佛像。来源未给五躯尺寸、形制、胎层、漆色与存佚，confidence 取 medium。",
    "批准新建 04-knowledge/units/works/waguan-si-jiazhu-foxiang.md：单册单源，consensus=tentative；工艺细节留在夹纻胎条。",
    "写入 works/waguan-si-jiazhu-foxiang.md（新建）；引用 L2963；三绝不加嵌套引号。")

add("08-16", "斑漆", "create",
    "04-knowledge/units/terms/ban-qi.md",
    "候选为斑漆（L2965-L2967）。检索发现 `terms/xipi.md` 记犀皮，并明确称其实为“六朝斑漆的发展”，但 terms 下无斑漆条，犀皮条不承担斑漆本身的定义；`procedures/jiazhu-tai.md` 记同期夹纻。新建术语条：记斑漆为六朝新创造、多色漆交混或单色漆显深浅两法、前者实为彩漆、仅见文献尚未有遗物、应为变涂技法前身，并把它放在 L2959 所列夹纻造像、斑漆、绿沉漆三突出品种中。来源未给胎体、器形、色料与工序，confidence 取 medium。",
    "批准新建 04-knowledge/units/terms/ban-qi.md：单册单源，consensus=tentative；与犀皮条先后关系照来源。",
    "写入 terms/ban-qi.md（新建）；引用 L2967、L2959；无遗物不作形制推定。")

add("08-17", "绿沉漆", "create",
    "04-knowledge/units/terms/lvchen-qi.md",
    "候选为绿沉漆（L2969-L2978）。检索发现 `terms/xipi.md` 与 `terms/ban-qi.md`（本批同建）记斑纹类漆器，`persons/wang-xi-zhi.md` 记王羲之，terms 下无绿沉漆条。新建术语条：记《书案铭》“刻香镂采，纤银卷足。漆花曜紫，画制舒绿。怪广知平，入雕非曲”、刘桢奏折指韦朗作绿沉漆屏风、王羲之受赠绿沉漆笔管、流行于上层士大夫，以及绿沉为暗绿如物沉水、六朝以前漆色多为朱黄黑、深绿为新产与调色技术新成就的判断。来源作“刘桢”与《书经》，本条照录不代改；未给色料、配方与实物，confidence 取 medium。",
    "批准新建 04-knowledge/units/terms/lvchen-qi.md：单册单源，consensus=tentative；人名书名照录存疑。",
    "写入 terms/lvchen-qi.md（新建）；引用 L2971、L2976、L2978；不改“刘桢”与《书经》。")

add("08-18", "北魏木板漆画", "create",
    "04-knowledge/units/works/beiwei-muban-qihua.md",
    "候选为1966年大同石家寨村北魏木板漆画（L2980）。检索发现 `terms/ping-feng.md` 记屏风，`terms/qimu-jiaju.md` 记漆木家具，`places/yungang-shiku.md` 记大同云冈石窟，works 下无木板漆画条。新建器物条：记1966年大同东南郊石家寨村北魏墓发现、可能为屏风装饰、木板榫卯连接、红漆板面、黑线描人物故事、面部服饰白黄绿橙蓝五色漆、文字题记与榜题、帝王将相高士孝子烈女题材，并录其对漆工艺与服饰家具的双重反映。插图12未视觉核验；来源未给木板数量、尺寸、板厚、墓号、墓主与藏地，confidence 取 medium。",
    "批准新建 04-knowledge/units/works/beiwei-muban-qihua.md：单册单源，consensus=tentative；屏风功能标为推测。",
    "写入 works/beiwei-muban-qihua.md（新建）；引用 L2980；不据插图12补构图与服饰。")

add("08-20", "南京肖景墓前石柱", "create",
    "04-knowledge/units/works/xiao-jing-mu-shizhu.md",
    "候选为南京肖景墓前石柱（L2990）。检索发现 `places/nanjing.md` 记南京，`terms/lianhua-wen.md` 为本批同建莲花纹条，works 下无陵墓石柱条；候选标题作“萧景”，来源原文作“肖景”，本条从来源作肖景并不另立萧景别名。新建器物条：记南京肖景墓前石柱为代表、柱身有棱宛如希腊殿柱、柱顶莲瓣上立辟邪，并录天禄有角居右、辟邪有翼垂舌居左的石兽制度。来源未给高度、柱径、棱数、材质与保存状况，confidence 取 medium。",
    "批准新建 04-knowledge/units/works/xiao-jing-mu-shizhu.md：单册单源，consensus=tentative；字形从来源。",
    "写入 works/xiao-jing-mu-shizhu.md（新建）；引用 L2990；不据“希腊殿柱”推影响路径。")

# ---- no_delta: captions and general terms ----
add("08-100", "伎乐人物龙纹石雕（六朝）", "no_delta",
    "04-knowledge/units/terms/tangcao-wen.md",
    "候选为插图13 图注“伎乐人物龙纹石雕(六朝)”（L2996-L2997），只有品名与朝代，无尺寸、出土地、材质、技法与图像细节。该图注所在的 L2992 段落主题为卷草纹，相关纹样内容已由 `terms/tangcao-wen.md` 承担；石雕总体又见 L2984-L2990 的六朝石雕总述。单凭图注另立作品条会得到无出土单位、无数据的空条，与本批“只有图注、无器物数据的候选记 no_delta”的规则一致。",
    "不新建伎乐人物龙纹石雕条；图注不足以成条，段落纹样已有 terms/tangcao-wen.md。",
    "cand-08-100 记 no_delta，target 指向 terms/tangcao-wen.md；图注未视觉核验。")

add("08-101", "玻璃碗（北燕）", "no_delta",
    "04-knowledge/units/terms/liuli.md",
    "候选为插图14 图注“玻璃碗(北燕)”（L2999-L3002），只有品名与朝代，无尺寸、墓号、藏地与器形细节。L2999 正文所列北票北燕冯素弗墓吹制玻璃器皿五件（玻璃碗、玻璃杯、玻璃钵、鸭形玻璃注及豆足残器）已由本批同建的 `works/wangwen-boli-bei.md` 在同类出土一节完整承载，玻璃工艺通条则由 `terms/liuli.md` 承担。单凭图注另立作品条会得到只有品名的空条，故 no_delta。",
    "不新建北燕玻璃碗条；图注不足以成条，五件组数据留在网纹玻璃杯条。",
    "cand-08-101 记 no_delta，target 指向 terms/liuli.md；图注未视觉核验。")

add("08-22", "网纹玻璃杯", "create",
    "04-knowledge/units/works/wangwen-boli-bei.md",
    "候选为河北景县封氏墓群北魏祖氏墓网纹玻璃杯（L2999）。检索发现 `terms/liuli.md` 记玻璃通条，`places/` 下无景县条，works 下无此杯条。新建器物条：记1948年出土、高6.7厘米、口径10.3厘米、青绿色、杯壁下部网状凸线、现陈列中国历史博物馆，并录“可见当时国内确已制造玻璃器皿”与“不能认为，我国古代的玻璃器都是来自西方”的判断，另列定县塔基、北票冯素弗墓、南京象山与南京大学北园四批出土，以及铜器漆器瓷器大量生产与玻璃质地未过关两条原因。插图14为北燕玻璃碗非本杯；来源未给壁厚、重量、成分与成型工艺，confidence 取 medium。",
    "批准新建 04-knowledge/units/works/wangwen-boli-bei.md：单册单源，consensus=tentative；外来与本土之辨标为来源判断。",
    "写入 works/wangwen-boli-bei.md（新建）；引用 L2999；尺寸两项照录，不推成型方法。")

cfg = {
    "doc": DOC,
    "file": "03基础书籍-md文档/中国工艺美术史（修订本）_田自秉_2010_东方出版中心.md",
    "rules": [
        "单册单源新建：consensus=tentative，evidence_status=source_backed，source_count=1，version=1",
        "同实体更新：跨册追加 source block，source_count+1、version+1、日期续期；同册多跨段追加 citation，source_count 不变",
        "逐字引文用“ ”，跨行拼接用「 」，作者自撰短语不用引号，正文禁 ASCII 双引号，嵌套引号用‘ ’",
        "图版只著录图注原文并标未视觉核验，不据图像补写尺寸、藏地与出土地点",
        "同名异物并列著录，slug 加时代或身份限定，不合并为同一人物（苏轼／前秦苏氏）",
        "来源未给作者、正字或年代时照录原文并存疑，不据来源外材料补写（刘桢、《书经》、肖景）",
        "只有图注、无器物数据的候选记 no_delta，不新建只有图注的作品条",
        "类型条与单器条分工：总类、制法与题材归术语条，单件器物的尺寸、出土与画面归作品条",
        "期别总述与单器条分工：六朝铜镜条记三类镜与工匠纪年，伍子胥画像镜仍归既有单器条",
        "候选 unit_type 与实体性质不符时按实体改写：织物类型记 term，单件器物记 work",
    ],
    "scope_spans": [[2713, 3015]],
    "scope_note": "田自秉 2010 册第七章六朝（L2713-L3015）逐段复读，含陶瓷、染织、金属工艺、漆器、其他工艺与结语；彩版与插图 1、2、4、11、12、13、14 只读图注，未视觉核验。",
    "decisions": D,
}

out = ROOT / "_zn_decisions_t7.json"
out.write_text(json.dumps(cfg, ensure_ascii=False, indent=1), encoding="utf-8", newline="\n")
print("decisions:", len(D))
print(Counter(x["action"] for x in D))
