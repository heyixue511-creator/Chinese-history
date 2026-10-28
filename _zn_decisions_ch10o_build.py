# -*- coding: utf-8 -*-
"""Build chapter 10 batch O decisions JSON from generated KU files."""
import json
from collections import Counter
from pathlib import Path

ROOT = Path(r"D:/中国设计史研究")
DOC = "2009-zhaonong-zhongguo-yishu-shejishi"
PREFIX = DOC + ":"

# (candidate suffix, target, kind, analysis, apply_note)
CREATES = [
    ("cand-11-145", "04-knowledge/units/terms/xiangjiao.md", "术语",
     "橡胶是赵农所述现代高分子材料，有天然与合成两类：天然橡胶以橡浆（胶乳）加工，合成橡胶由单体聚合；经加热、液化、模制可成标准物件，用于轮胎、电线、电缆、胶带、胶垫与雨鞋、胶靴等。既有 `terms/plastic.md`、`terms/glass.md`、`terms/tangci.md` 分记塑料、玻璃与搪瓷，无橡胶条目；材料名称与工业应用不合并。按术语新建，证据行 L7938。来源只给材料定义与用途，无中国橡胶工业的产量、厂址与分期，confidence 取 medium。",
     "写入 04-knowledge/units/terms/xiangjiao.md（新建）；引用 L7938。"),
    ("cand-11-150", "04-knowledge/units/terms/gonggong-qiju.md", "术语",
     "公共器具是赵农对办公家具与公共场所器具的合称：办公家具含办公桌椅、文件柜、文件箱、文件盒、沙发、折叠椅、电脑桌、电脑椅、会议桌等；公共场所器具含影剧院、车站、机场、法庭、医院、公园等场所座椅及学校课桌椅、黑板、幕布与餐饮住宿场所椅凳、沙发、茶几、时钟等。公共器具的充分使用形成「家具社会化」景象，并按场合区分木材、塑料、压缩板材与款式、色泽；铅笔、钢笔等文具亦属办公用品。检索无同实体术语；`terms/ming-shi-jiaju.md` 等记传统家具类型，与本条现代公共器具不合并。按术语新建，证据行 L7967-L7973。来源为分类列举，无设计者、尺度标准与采购制度，confidence 取 medium。",
     "写入 04-knowledge/units/terms/gonggong-qiju.md（新建）；引用 L7967-L7973。"),
    ("cand-11-151", "04-knowledge/units/terms/jiayong-xiao-gongju.md", "术语",
     "家用小工具是赵农所列家庭为自行解决日常琐碎问题而常备的手工具，含榔头、手钳、改锥、手锯、剪刀、针线、锥子、刀子、钉子、镊子、多角扳手、管钳、试电笔、压线钳等。检索无同实体术语。按术语新建，证据行 L7977。来源只一句列举，无单件形制、材料、产地与设计者，confidence 取 low。",
     "写入 04-knowledge/units/terms/jiayong-xiao-gongju.md（新建）；引用 L7977。"),
    ("cand-11-152", "04-knowledge/units/terms/dianqi.md", "术语",
     "电器是赵农视为生活现代化标志的用品类别，满足物质与精神需求；电视机、电冰箱、电暖气、空调等专业性强者需请专业人员维修。检索无同实体术语；`terms/shoubiao.md` 等为单件用品，与本条类别不同。按术语新建，证据行 L7988。来源只两句定位与维修判断，无品类谱系、设计史与品牌，confidence 取 low。",
     "写入 04-knowledge/units/terms/dianqi.md（新建）；引用 L7988。"),
    ("cand-11-153", "04-knowledge/units/terms/shougong-bianzhi.md", "术语",
     "手工编织是赵农所述生活中最常见的器物制作方式，含竹编、草编、藤编、棕编、柳编、荆编、麦秆编、玉米皮编等材料与方法，因地域形成不同技术特色：竹编以浙江、四川、江西、湖南等南方地区为主，草编以山东、河北、河南、浙江、广东等地为主，藤编盛行于四川、湖南、陕南，柳编、荆编、麦秆编、玉米皮编广泛流行于北方。产品有竹制椅具、箱子、书架、盒子、垫子、帽子、篮子，藤制坐椅、箱子，棕编大床、箱子及柳条、荆条篮筐等，具朴素无华、自然天成的特点；手工地毯以彩色毛线或丝线编成。赵农称传统手工艺在近现代工业化影响下扮演了悲壮的角色。检索无同实体术语。按术语新建，证据行 L7992-L8002。来源覆盖材料、地域、产品与文化评价，无具体技法、工具与传承谱系，confidence 取 medium。",
     "写入 04-knowledge/units/terms/shougong-bianzhi.md（新建）；引用 L7992-L8002。"),
    ("cand-11-157", "04-knowledge/units/persons/wang-caiyun.md", "人物",
     "王才运是上海南京路「荣昌祥呢绒西服店」的裁缝，赵农称相传最初设计制作中山装的人就是他，孙中山及其助手黄隆生也参与设计，因孙中山第一次在公共场合穿出而称「中山装」。既有 `terms/zhongshanzhuang.md` 记中山装形制与得名，未立王才运人物条；检索无同实体人物。按人物新建，证据行 L8044。来源只一句记身份与制作关系并冠以「相传」，无生卒、籍贯、学艺与其他作品，confidence 取 low。",
     "写入 04-knowledge/units/persons/wang-caiyun.md（新建）；引用 L8044。"),
    ("cand-11-158", "04-knowledge/units/persons/huang-longsheng.md", "人物",
     "黄隆生是孙中山的助手，赵农记其参与中山装设计。检索无同实体人物；`persons/wang-caiyun.md` 为同段裁缝，二者分属不同人物。按人物新建，证据行 L8044。来源只一句提及，无生卒、籍贯、革命经历与具体分工，confidence 取 low。",
     "写入 04-knowledge/units/persons/huang-longsheng.md（新建）；引用 L8044。"),
    ("cand-11-160", "04-knowledge/units/terms/hongwei-fu.md", "术语",
     "红卫服是文化大革命时期由军便服改造而成的全民化服装，也称「毛服」；草绿色、灰蓝色甚至黑色的毛服成为男女老少的基本服饰，工人以灰蓝色工作服为主，农民以对襟盘扣的黑蓝布衫为主。检索无同实体术语；`terms/zhongshanzhuang.md` 记中山装、`terms/junbian-zhuang.md` 记军便装，均与红卫服不同。按术语新建，证据行 L8054、L8058。来源分记改造来源与城乡穿着，中隔节标题与图版，按文字著录；无形制、面料、设计者与命名由来，confidence 取 medium。",
     "写入 04-knowledge/units/terms/hongwei-fu.md（新建）；引用 L8054、L8058。"),
    ("cand-11-200", "04-knowledge/units/terms/junbian-zhuang.md", "术语",
     "军便装是 1949 年以后与中山装并列的男服样式，赵农把它与连衣裙、列宁装同列为当时服装首选；文化大革命时期全民化服装由军便服改造成「红卫服」。检索无同实体术语。按术语新建，证据行 L8022、L8054。来源只提名与改造关系，无形制、面料、配发制度与设计者，confidence 取 low。",
     "写入 04-knowledge/units/terms/junbian-zhuang.md（新建）；引用 L8022、L8054。"),
    ("cand-11-201", "04-knowledge/units/terms/liening-zhuang.md", "术语",
     "列宁装是 1949 年以后受苏联服饰影响、与连衣裙并列的女性服装首选；当时人们摒弃旧中国的长袍马褂，在服饰中有意追求朴素的工农兵形象。检索无同实体术语。按术语新建，证据行 L8022。来源只一句列举与一句背景，无形制、面料、传入路径与设计者，confidence 取 low。",
     "写入 04-knowledge/units/terms/liening-zhuang.md（新建）；引用 L8022。"),
    ("cand-11-202", "04-knowledge/units/terms/yingbin-fu.md", "术语",
     "迎宾服是 1949 年以后青年女性穿着的平领服装，与日常对襟花布衣并列。检索无同实体术语。按术语新建，证据行 L8022。来源只给名称、领型与穿着群体，无使用场合、整体形制、面料与设计者，confidence 取 low。",
     "写入 04-knowledge/units/terms/yingbin-fu.md（新建）；引用 L8022。"),
    ("cand-11-161", "04-knowledge/units/terms/xifu.md", "术语",
     "西服是欧洲传统服装，20 世纪初由西方商业人士及中国留学欧美的学生引入，西服制衣行业开始在上海盛行；形制有拨折领、前衣片三只开袋、肩部衬垫、后背背缝，分便服与礼服，礼服又有晨礼服、晚礼服、常礼服等样式。20 世纪上半叶仅在上流阶层流行，文化大革命时期几乎销声匿迹，80 年代以后在各阶层迅速流行并演变为无明显阶层特征的平民化服饰。检索无同实体术语；`terms/zhongshanzhuang.md` 记中山装，二者并列而非同一。按术语新建，证据行 L8060-L8062。来源无裁剪尺寸、面料规格与上海西服店谱系，confidence 取 medium。",
     "写入 04-knowledge/units/terms/xifu.md（新建）；引用 L8060-L8062。"),
    ("cand-11-162", "04-knowledge/units/terms/zhiye-zhuang.md", "术语",
     "职业装是赵农所述由于社会分工需要而演变出的服饰：20 世纪中国职业装中士兵服饰最具特色，1949 年后解放军战士服装一度成为全民服装样式；现代职业装以警察、法官、医师、厨师、清洁工、中小学生校服最引人注目，而工商、税务、保安人员服饰模仿警察服并加佩饰、皮带，常使市民误识，被视为职业装设计误区。检索无同实体术语。按术语新建，证据行 L8064。来源无各类职业装的具体形制、配发制度与设计者，confidence 取 medium。",
     "写入 04-knowledge/units/terms/zhiye-zhuang.md（新建）；引用 L8064。"),
    ("cand-11-163", "04-knowledge/units/terms/tangzhuang.md", "术语",
     "唐装是伴随人们对传统中式衣衫的怀念而近年流行的服饰：以锦缎为面料，对中国传统对襟盘扣样式进行改造，在肩部加垫衬，将原先与肩部连接的衣袖重新接缝，形成别具一格的样子。检索无同实体术语；`terms/zhongshanzhuang.md`、`terms/qipao.md` 分记中山装与旗袍，不合并。按术语新建，证据行 L8066。来源无命名由来、流行年份、设计者与产业规模，confidence 取 medium。",
     "写入 04-knowledge/units/terms/tangzhuang.md（新建）；引用 L8066。"),
    ("cand-11-164", "04-knowledge/units/terms/shizhuang-fabuhui.md", "术语",
     "时装发布会是赵农所定义的一种服装纺织业商业活动：时装即流行的服装，发布会通过对流行服饰的预测和设计，对面料、款式、色彩发展趋势予以推荐和引导，促进服装发展；涉及女装、男装、童装、中老年服装及鞋帽、围巾、领带、腰带、手套、首饰、提包等。1980 年以后重新进入中国社会生活，逐渐与国际服装产业衔接，皮尔·卡丹、花花公子、耐克、鳄鱼、宝姿等名牌进入中国市场。检索无同实体术语；本条按商业活动类型入 D 维度，不按单场活动立目。来源无发布会制度、举办机构、场次与流程，confidence 取 medium。",
     "写入 04-knowledge/units/terms/shizhuang-fabuhui.md（新建）；引用 L8082。"),
    ("cand-11-165", "04-knowledge/units/terms/maozedong-xiangzhang.md", "术语",
     "毛泽东像章是文化大革命时期流行的佩带毛泽东头像的纪念章，材料有铜、铝、锡、瓷、塑料、有机玻璃等，花样很多，有时直径达 15 厘米，挂在胸前宛若护心镜；许多人家以收集像章为乐，成为文革初期的一大社会景象。检索无同实体术语。按术语新建，证据行 L8078。来源无制作单位、设计者、发行数量与图样谱系，confidence 取 medium。",
     "写入 04-knowledge/units/terms/maozedong-xiangzhang.md（新建）；引用 L8078。"),
    ("cand-11-203", "04-knowledge/units/terms/limao.md", "术语",
     "礼帽是赵农所列 20 世纪帽饰样式之一，与瓜皮帽、鸭舌帽同属民国主要男帽；20 年代以后知识分子多采用长袍、西裤、皮鞋、围巾、礼帽的搭配方式。检索无同实体术语；`terms/guapi-mao.md` 记瓜皮帽，本条单列礼帽。按术语新建，证据行 L8015、L8068。来源无帽型、材质、产地与设计者，confidence 取 low。",
     "写入 04-knowledge/units/terms/limao.md（新建）；引用 L8015、L8068。"),
    ("cand-11-204", "04-knowledge/units/terms/junmao.md", "术语",
     "军帽是赵农所列 20 世纪帽饰样式之一，称战争及政治年代中主要是军帽。检索无同实体术语。按术语新建，证据行 L8068。来源只一句分期判断，无帽型、帽徽、军种差异与配发制度，confidence 取 low。",
     "写入 04-knowledge/units/terms/junmao.md（新建）；引用 L8068。"),
    ("cand-11-205", "04-knowledge/units/terms/yashed-mao.md", "术语",
     "鸭舌帽是赵农所列 20 世纪帽饰样式之一，与瓜皮帽、礼帽同属民国主要男帽。检索无同实体术语。按术语新建，证据行 L8068。来源只一句列举，无帽型、帽檐、材质、产地与设计者，confidence 取 low。",
     "写入 04-knowledge/units/terms/yashed-mao.md（新建）；引用 L8068。"),
    ("cand-11-206", "04-knowledge/units/terms/beilei-mao.md", "术语",
     "贝雷帽是赵农所列 20 世纪帽饰样式之一，在三四十年代的艺术界比较流行，到 20 世纪末又开始回流，为一部分少女喜爱，并演化为时装帽样式。检索无同实体术语。按术语新建，证据行 L8068。来源只一句分期与群体描述，无帽型、材质、产地与设计者，confidence 取 low。",
     "写入 04-knowledge/units/terms/beilei-mao.md（新建）；引用 L8068。"),
    ("cand-11-207", "04-knowledge/units/terms/shoubiao.md", "术语",
     "手表是赵农所述兼具实用功能与手饰意义的个人用品，成为人们象征财富的携带之物；人们贴上透光颜色纸，红黄蓝绿，既求美观也有炫耀意味，赵农称这说明了贫困年代人们的精神饥渴。「三转一响」（手表、自行车、缝纫机、收音机）是一般家庭的最高生活需求。检索无同实体术语。按术语新建，证据行 L8070。来源无品牌、机芯、产地、价格与普及率，confidence 取 medium。",
     "写入 04-knowledge/units/terms/shoubiao.md（新建）；引用 L8070。"),
    ("cand-11-208", "04-knowledge/units/terms/sanzhuan-yixiang.md", "术语",
     "三转一响是赵农所记 20 世纪中国一般家庭的最高生活需求，指手表、自行车、缝纫机与收音机四件物品。检索无同实体术语；`terms/shoubiao.md` 记手表单品，本条记消费组合，不合并。按术语新建，证据行 L8070。来源只有一句列举，无说法起源、年代上下限、地区差异与品牌，confidence 取 low。",
     "写入 04-knowledge/units/terms/sanzhuan-yixiang.md（新建）；引用 L8070。"),
    ("cand-12-01", "04-knowledge/units/terms/yangbu.md", "术语",
     "洋布是 19 世纪末大量现代纺织技术进入中国沿海地区后生产的价廉物美的机织布；它冲击中国社会现实生活，破坏传统纺织技术的生存条件，使传统纺织仅成为乡村社会底层妇女在农闲时期的劳作，少许手工纺织品仅在周围集市交换，赵农称「丝绸大国」的盛景已不复存在。检索无同实体术语；`terms/nanjing-yunjin.md`、`terms/song-jin.md` 等记传统丝织名品，与本条近代机织布不合并。按术语新建，证据行 L8086。来源无洋布品类、规格、价格、产地与市场份额，confidence 取 medium。",
     "写入 04-knowledge/units/terms/yangbu.md（新建）；引用 L8086。"),
    ("cand-12-02", "04-knowledge/units/terms/sida-mingxiu.md", "术语",
     "四大名绣是 1949 年以后江南丝绸业恢复过程中形成的苏绣、湘绣、粤绣、蜀绣合称；当时以上海、苏州、杭州为中心重新开发丝绸产品，恢复锦、绸、缎、纱、罗、绫等传统技术，南京云锦、四川蜀锦也有所发展；河南汴绣、山东鲁绣有所突破，少数民族的苗绣、黎绣、土家绣各具特色，蜡染、扎染等技术也有突破性发展。检索无同实体术语；`terms/yuexiu.md` 记粤绣单品，本条为四绣合称，不合并。按术语新建，证据行 L8092-L8097。来源无针法谱系、代表性传承人与产区规模，confidence 取 medium。",
     "写入 04-knowledge/units/terms/sida-mingxiu.md（新建）；引用 L8092-L8097。"),
    ("cand-12-160", "04-knowledge/units/terms/mianfangchang.md", "术语",
     "棉纺厂是 20 世纪五六十年代产棉地区纷纷建立的纺织厂，以现代纺织机器生产大量棉、毛、麻、丝布等产品；在计划经济下建立的纺织厂随市场化需求面临转型选择。检索无同实体术语；本条按工厂类型入 D 维度，不按单厂立目。按术语新建，证据行 L8101。来源无厂名、厂址、纱锭数、建设时间与经营状况，confidence 取 low。",
     "写入 04-knowledge/units/terms/mianfangchang.md（新建）；引用 L8101。"),
]

UPDATES = [
    ("cand-11-141", "04-knowledge/units/terms/zisha-tao.md", "术语",
     "宜兴紫砂陶与既有 `terms/zisha-tao.md` 同指。赵农 L7913 记江苏宜兴陶制业发达，宜兴的紫砂陶、钧陶、精陶等闻名江南，为既有条目补江南名产并称，属跨书新增来源（第 5 册）。不新建同名术语，按跨书更新处理：新增赵农 2009 来源块，source_count 4→5，version 3→4，日期续为 2026-10-26。",
     "更新 04-knowledge/units/terms/zisha-tao.md（跨书新增来源）；引用 L7913。"),
    ("cand-11-196", "04-knowledge/units/places/jun-kiln.md", "术语",
     "钧窑瓷与既有 `places/jun-kiln.md` 同指。赵农 L7915 记传统钧窑瓷、汝窑瓷、龙泉窑瓷、耀州窑瓷等生产技术在 20 世纪后半叶也得到一定程度的恢复，补出既有条目未覆盖的现代恢复段。不新建同名条目，按同书多跨度更新处理：在赵农来源 citation 内追加 L7915，source_count 不变，version 2→3。",
     "更新 04-knowledge/units/places/jun-kiln.md（同书多跨度）；追加 L7915。"),
    ("cand-11-197", "04-knowledge/units/places/ru-kiln.md", "术语",
     "汝窑瓷与既有 `places/ru-kiln.md` 同指。赵农 L7915 记传统汝窑瓷等生产技术在 20 世纪后半叶也得到一定程度的恢复，补出既有条目未覆盖的现代恢复段。不新建同名条目，按同书多跨度更新处理：在赵农来源 citation 内追加 L7915，source_count 不变，version 1→2。",
     "更新 04-knowledge/units/places/ru-kiln.md（同书多跨度）；追加 L7915。"),
    ("cand-11-198", "04-knowledge/units/places/longquan-kiln.md", "术语",
     "龙泉窑瓷与既有 `places/longquan-kiln.md` 同指。赵农 L7915 记传统龙泉窑瓷等生产技术在 20 世纪后半叶也得到一定程度的恢复，与既有条目所记元代初年恢复生产分属不同时代，须并列标注。不新建同名条目，按同书多跨度更新处理：在赵农来源 citation 内追加 L7915，source_count 不变，version 1→2。",
     "更新 04-knowledge/units/places/longquan-kiln.md（同书多跨度）；追加 L7915。"),
    ("cand-11-199", "04-knowledge/units/places/yaozhou-kiln.md", "术语",
     "耀州窑瓷与既有 `places/yaozhou-kiln.md` 同指。赵农 L7915 记传统耀州窑瓷等生产技术在 20 世纪后半叶也得到一定程度的恢复，补出既有条目未覆盖的现代恢复段。不新建同名条目，按同书多跨度更新处理：在赵农来源 citation 内追加 L7915，source_count 不变，version 1→2。",
     "更新 04-knowledge/units/places/yaozhou-kiln.md（同书多跨度）；追加 L7915。"),
]

NO_DELTA = [
    ("cand-11-142", "石湾陶塑", "04-knowledge/units/places/shiwan-yao.md", "术语",
     "石湾陶塑与既有 `places/shiwan-yao.md` 同指。既有条目已据田自秉与夏燕靖 2016 记石湾陶塑「采用少许上釉而露出底胎」「藏拙于巧」的工艺特征；赵农 L7913 同述石湾陶塑采用少许上釉而露出底胎的方法、藏拙于巧，未提供新事实、年代或人物。按 no_delta 处理，不改写既有条目。",
     "不写入知识元；候选标 no_delta，目标 places/shiwan-yao.md。"),
]


def title_of(path):
    for line in Path(path).read_text(encoding="utf-8").splitlines():
        if line.startswith("title:"):
            return line.split(":", 1)[1].strip().split("（")[0].strip()
    return Path(path).stem


decisions = []
for suffix, target, kind, analysis, apply_note in CREATES:
    decisions.append({
        "cid": PREFIX + suffix,
        "entity": title_of(target),
        "action": "create",
        "target": target,
        "analysis": analysis,
        "approve": f"批准新建 {target}：单册单源，consensus=tentative，confidence 按证据厚度评定。",
        "apply_note": apply_note,
        "note": f"canonical: {target}。",
    })

for suffix, target, kind, analysis, apply_note in UPDATES:
    decisions.append({
        "cid": PREFIX + suffix,
        "entity": title_of(target),
        "action": "update",
        "target": target,
        "analysis": analysis,
        "approve": f"批准更新 {target}：同实体已有条目，按既有字段契约追加证据，不新建重复条目。",
        "apply_note": apply_note,
        "note": f"canonical: {target}。",
    })

for suffix, entity, target, kind, analysis, apply_note in NO_DELTA:
    decisions.append({
        "cid": PREFIX + suffix,
        "entity": entity,
        "action": "no_delta",
        "target": target,
        "analysis": analysis,
        "approve": "批准 no_delta：「石湾陶塑」与既有石湾窑条同指，且赵农 L7913 未超出既有证据，保持原状。",
        "apply_note": apply_note,
        "note": f"canonical: {target}。",
    })

cfg = {
    "doc": DOC,
    "file": "03基础书籍-md文档/中国艺术设计史_赵农_2009_高等教育出版社.md",
    "rules": [
        "单册单源新建：consensus=tentative，evidence_status=source_backed，source_count=1，version=1",
        "同书多跨度更新：sources 单条 citation 内逗号分隔，source_count 不增，version 加 1",
        "跨书新增来源：sources 追加新来源块，source_count 加 1，version 加 1",
        "逐字引文用“ ”，跨行或作者判断用「 」，作者自撰短语不用引号，正文禁 ASCII 双引号",
        "列举型候选只著录来源所列名称、领型、材质、颜色与用途，不据来源外材料补形制、裁剪尺寸与设计者",
        "同名实体不重复立条：紫砂陶、钧窑、汝窑、龙泉窑、耀州窑、石湾窑按更新或 no_delta 处理",
        "类型与单品分层：四大名绣为合称条，手表与三转一响分属单品与消费组合",
        "跨页残句不逐字引：被图版、页眉或章节页分隔的文字只作内容转述",
        "原文疑误与内部张力照录标注，不径改",
        "图版一律据图注著录，未视觉核验，不据图扩写",
    ],
    "scope_spans": [[7899, 8102]],
    "scope_note": "赵农 2009 册第十章第三节器皿与家具、第四节服饰与纺织 L7899–L8102 逐段复读，含陶瓷与窑口恢复、塑料玻璃等材料、公共器具与家用工具、手工编织、20 世纪服饰与帽饰、手表与消费、纺织业；候选 source_span 为块级粗跨度，实际引用行均落在本批范围内。图版未视觉核验。",
    "decisions": decisions,
    "notes": "赵农 2009 册第十章第三至第四节 unit 候选 31 条：create 25、update 5、no_delta 1。范围 L7899-L8102。新建覆盖橡胶、公共器具、家用小工具、电器、手工编织、王才运、黄隆生、红卫服、军便装、列宁装、迎宾服、西服、职业装、唐装、时装发布会、毛泽东像章、礼帽、军帽、鸭舌帽、贝雷帽、手表、三转一响、洋布、四大名绣、棉纺厂；update 为宜兴紫砂陶（跨书）与钧、汝、龙泉、耀州四窑（同书多跨度）；no_delta 为石湾陶塑。塑料、玻璃、搪瓷、红木、瓜皮帽、中山装、旗袍等已有 KU，本批不重复立条；图 10-21 至图 10-36 未视觉核验。",
}

out = ROOT / "_zn_decisions_ch10o.json"
out.write_text(json.dumps(cfg, ensure_ascii=False, indent=1) + "\n", encoding="utf-8", newline="\n")
print(Counter(d["action"] for d in decisions), len(decisions))
