"""Chapter-4 decisions, part B1: works (18)."""
import json

P = "2009-zhaonong-zhongguo-yishu-shejishi:"
D = []


def add(cid, entity, action, target, analysis, approve, apply_note, note):
    D.append({
        "cid": P + cid, "entity": entity, "action": action, "target": target,
        "analysis": analysis, "approve": approve, "apply_note": apply_note, "note": note,
    })


add("cand-04-64", "石鼓文", "create", "04-knowledge/units/works/shi-gu-wen.md",
    "L2586 给秦国文字的代表、亦称大篆或籀文并与西周金文有关联，L2590 给李斯据其书写特点制定小篆；两处合为一条，来源只有书写传统层面的描述。",
    "新建 works/shi-gu-wen.md：sub_type inscription，primary_dimension C；confidence 记 low，只写文字史定位。",
    "六节齐全；不写石鼓形制、字数、现藏与发现经过；大篆、籀文两名并列；李斯与小篆的关系单列一条核心内容。",
    "canonical 为新建石鼓文条目；与 terms/xiaozhuan.md 是前源文字与规范书体的分工。")

add("cand-04-65", "商鞅方升", "create", "04-knowledge/units/works/shang-yang-fang-sheng.md",
    "L2586 与 L2590 给商鞅变法时的量器、铭刻文字与李斯据其铭文制定小篆，L2819-L2821 给商鞅“平权衡正度量”、秦始皇依秦制颁全国与廿六年诏书；同一器物跨文字与量制两节。",
    "新建 works/shang-yang-fang-sheng.md：sub_type measuring_vessel，primary_dimension B，secondary D；铭文与量制两项合并。",
    "六节齐全；廿六年诏书“法度量则不壹歉疑者皆明壹之”逐字照录；不补器高、容积与藏地；秦量制度归 terms/qin-liang.md。",
    "canonical 为新建商鞅方升条目；与 terms/qin-liang.md、terms/qin-quan.md 是单器与制度的分别，与山东秦陶量的诏书关系另记。")

add("cand-04-67", "睡虎地秦简", "create", "04-knowledge/units/works/shuihudi-qin-bamboo-slips.md",
    "L2592 一句给湖北云梦睡虎地出土与秦隶代表作品；全章只有这一句。",
    "新建 works/shuihudi-qin-bamboo-slips.md：sub_type manuscript，primary_dimension C；confidence 记 low。",
    "六节齐全；只写出土地点与书体史地位；不补简数、内容、墓主与年代；与程邈传说、秦隶的关系归 terms/li-shu.md。",
    "canonical 为新建睡虎地秦简条目；与 places/shuihudi-qinmu.md 是简牍与墓葬的分工。")

add("cand-04-69", "居延汉简", "create", "04-knowledge/units/works/juyan-han-slips.md",
    "L2603 一句给甘肃居延出土、西汉末年草书字体的代表、以隶书为基点、飘逸活泼与笔意连缀；全章只有这一句。",
    "新建 works/juyan-han-slips.md：sub_type manuscript，primary_dimension C；confidence 记 low。",
    "六节齐全；只写出土地点与书体特征；不补简数、年代与内容；章草本体归 terms/zhang-cao.md。",
    "canonical 为新建居延汉简条目；与 terms/zhang-cao.md 是实物与书体的分工。")

add("cand-04-72", "宣示表", "create", "04-knowledge/units/works/xuan-shi-biao.md",
    "L2607 一句给钟繇代表作、最早楷书作品、横波顿挫、减少隶书捺挑与整洁简练；全章只有这一句。",
    "新建 works/xuan-shi-biao.md：sub_type calligraphy，primary_dimension C；confidence 记 low。",
    "六节齐全；只写书体地位与笔法评价；来源未给内容、流传与拓本，明写为证据边界；不补帖文与尺寸。",
    "canonical 为新建《宣示表》条目；与 persons/zhong-yao.md、terms/kai-shu.md 分属作品、人物与书体。")

add("cand-04-77", "秦驰道", "create", "04-knowledge/units/works/qin-chi-dao.md",
    "L2651-L2672 给以咸阳为中心辐射、宽约60米、高出地面、分皇帝专用道／军事道／常人道、每10里一管理亭、北通九原约1400公里、《汉书·贾山传》引文与汉代扩为长安中心道路。",
    "新建 works/qin-chi-dao.md：sub_type road，primary_dimension B，secondary D；制度与工程合并叙述。",
    "六节齐全；宽度、里程与亭距照录；《贾山传》引文逐字照录；不补路线图与考古勘测；车同轨另见 terms/che-tong-gui.md。",
    "canonical 为新建秦驰道条目；与 terms/che-tong-gui.md 是道路工程与车制标准的分工，与 persons/meng-tian.md 是工程与主持者。")

add("cand-04-85", "褒斜道", "create", "04-knowledge/units/works/baoxie-road.md",
    "L2710-L2719 给秦惠王时修、连接秦岭北麓眉县斜水谷与南麓褒水谷、长200余公里、石孔30厘米见方50厘米深、三层结构、《史记·货殖列传》“栈道千里…唯褒斜道绾毂其口”、刘邦烧绝栈道与韩信明修暗渡。",
    "新建 works/baoxie-road.md：sub_type road，primary_dimension B；单条道路，栈道通制归 terms/zhan-dao.md。",
    "六节齐全；石孔尺寸与里程照录；《货殖列传》引文按原样压缩；烧绝栈道与明修暗渡标为史事与传说并存；不补现存遗迹。",
    "canonical 为新建褒斜道条目；与 terms/zhan-dao.md 是具体道路与道路类型的分工。")

add("cand-04-86", "灵渠", "create", "04-knowledge/units/works/ling-qu.md",
    "L2723-L2725 给公元前219年史禄主持、广西兴安、连通湘江漓江、长33公里、连通长江珠江水系、船闸提高平衡水位、分水工程保持水源与岭南设行政机构。",
    "新建 works/ling-qu.md：sub_type waterway_engineering，primary_dimension B；工程本体，主持者归 persons/shi-lu.md。",
    "六节齐全；里程与年代照录；船闸与分水工程按来源描述，不补坡降、斗门数与渠宽；水道联通关系只写来源原话。",
    "canonical 为新建灵渠条目；与 persons/shi-lu.md 是工程与主持者的分工。")

add("cand-04-88", "渭水三桥", "create", "04-knowledge/units/works/weishui-three-bridges.md",
    "L2727 给东中西三座、中渭桥战国已修秦始皇加固翻修、长约525米宽约13.8米、750根木桩67个桥墩、横梁桥面、雕花护栏、中间高两边斜下呈八字、石灯华表与汉代增修东西两桥。",
    "新建 works/weishui-three-bridges.md：sub_type bridge，primary_dimension B；三桥合一条，不拆为三条。",
    "六节齐全；长度、宽度、桩数与墩数照录；八字桥面与石灯华表按来源描述，不补结构图；不补三桥各自址点。",
    "canonical 为新建渭水三桥条目；与 works/ba-bridge.md 是渭水与灞水两组桥的分工。")

add("cand-04-89", "灞桥", "create", "04-knowledge/units/works/ba-bridge.md",
    "L2729 给西安灞河、汉代古桥、初为木桥、王莽时烧毁、屡毁屡修与十里相送灞柳相别；来源未给长度与形制。",
    "新建 works/ba-bridge.md：sub_type bridge，primary_dimension B；只写沿革与送别文化两项。",
    "六节齐全；“灞柳相别”标为后世送别习俗，不写成汉代制度；不补桥长、桥墩与遗址发掘。",
    "canonical 为新建灞桥条目；与 works/weishui-three-bridges.md 并列，不合并为“汉代桥梁”。")

add("cand-04-103", "风车", "create", "04-knowledge/units/works/winnowing-machine.md",
    "L2805 给汉代发明、叶形风扇、摇动生风分离秕壳与籽粒、吹去杂草与粮食加工便利；来源未给尺寸、材质与传动结构。",
    "新建 works/winnowing-machine.md：sub_type agricultural_machine，primary_dimension B；与耧车、水碓同列粮食加工器具。",
    "六节齐全；只写工作原理与用途；不补扇叶数、箱体与曲柄结构；与石磨、舂米的工序关系按来源概括，不补工艺流程。",
    "canonical 为新建风车条目；与 works/san-jiao-lou.md、works/shui-dui.md 是播种、舂米与扬场三类农具的并列。")

add("cand-04-109", "咸阳宫", "create", "04-knowledge/units/works/xianyang-palace.md",
    "L2852-L2854 给咸阳原上多重楼台建筑群、主殿侧殿卧室浴室、回廊甬道连通、陶制下水管道、灭一国即仿建其宫殿、六国宫殿别称与六国纹饰瓦当。",
    "新建 works/xianyang-palace.md：sub_type palace，primary_dimension B；建筑群与仿建制度合并。",
    "六节齐全；仿建六国宫殿按来源记录，不补六国宫名；陶制下水管道只写来源所给功能，不补管径与走向；不补遗址面积。",
    "canonical 为新建咸阳宫条目；与 places/xianyang.md 是宫殿与城址的分工，与 works/epang-palace.md 是两座秦宫分别立条。")

add("cand-04-110", "未央宫", "create", "04-knowledge/units/works/weiyang-palace.md",
    "L2856-L2860 给汉长安城重要建筑、遗址南北200余米东西100余米高10余米夯土高台、《史记·高祖本纪》萧何营作与“非壮丽无以重威”长引文、张衡《西京赋》“正紫宫于未央”引句、长安城周长25公里与夯土板筑。",
    "新建 works/weiyang-palace.md：sub_type palace，primary_dimension B，secondary D；建筑、遗址与文献三项合并。",
    "六节齐全；遗址尺度与城墙周长照录；《高祖本纪》《西京赋》引文分别标注；萧何本人的营作动机归 persons/xiao-he.md，本条只留建筑与制度关系。",
    "canonical 为新建未央宫条目；与 places/han-chang-an.md 是宫殿与都城的分工。")

add("cand-04-114", "嵩山三阙", "create", "04-knowledge/units/works/songshan-three-que.md",
    "L2881 给东汉营造、石质、坛庙性祭祀建筑遗迹与“汉代地表建筑现在仅存的是阙”；来源未给三阙具体名称、位置与尺寸。",
    "新建 works/songshan-three-que.md：sub_type stone_architecture，primary_dimension B；confidence 记 low。",
    "六节齐全；只写年代、材质与坛庙性质；不补太室、少室、启母三阙的名称与测绘数据；门阙通制归 terms/men-que.md。",
    "canonical 为新建嵩山三阙条目；与 places/wushi-ci.md 的陵墓性门阙形成两类对照。")

add("cand-04-118", "阿房宫", "create", "04-knowledge/units/works/epang-palace.md",
    "L2893-L2911 给夯土高台上大型木构架建筑群、四川湖北木材运关中、《史记·秦始皇本纪》长引文（东西五百步南北五十丈、上坐万人下建五丈旗、阁道复道、未成）、“阿，近也”颜师古语与“我的房子”解、七十余万人分作、蜀山兀阿房出、项羽烧秦宫室火三月不灭但未确指阿房宫与遗址尚存。",
    "新建 works/epang-palace.md：sub_type palace，primary_dimension B，secondary A；工程、文献与焚毁三事合并。",
    "六节齐全；《秦始皇本纪》引文与颜师古语分别标注；“项羽烧阿房”按来源的不确定表述记录，不写成定论；《阿房宫赋》的文学形象归 publications/efang-palace-fu.md。",
    "canonical 为新建阿房宫条目；与 publications/efang-palace-fu.md 是建筑与文学文本的分工，来源“哪个更真实”的追问两边都保留。")

add("cand-04-121", "长城", "create", "04-knowledge/units/works/qin-han-changcheng.md",
    "L2917-L2928 给战国边墙、秦拆中原城墙保留北方边墙、公元前214年蒙恬率30万军民连结秦赵燕旧长城、西起临洮东入辽东、汉武帝向西延2000里至阳关、阴山以北外长城、板筑夯土与草木芦苇石块、烽燧报警、王昌龄《出塞》与明代砌砖护面。",
    "新建 works/qin-han-changcheng.md：sub_type defensive_wall，primary_dimension B，secondary D；秦汉长城合一条，不拆为秦、汉两条。",
    "六节齐全；里数、军民数与起止照录；《出塞》引诗标为王昌龄；明代砌砖只作后世对照一句；烽燧本体归 terms/feng-sui.md。",
    "canonical 为新建秦汉长城条目；与 terms/feng-sui.md 是墙体与报警设施的分工，与 procedures/rammed-earth-board-construction.md 是工程与工艺。")

add("cand-04-126", "马踏匈奴", "create", "04-knowledge/units/works/horse-treading-xiongnu.md",
    "L2973 与 L2982 给霍去病墓石刻群的中心、纪念碑式石雕、写意雕凿、以石赋形化形寓意与浮雕线雕圆雕结合，并给石刻约16件与马牛虎羊象猪鱼怪兽熊人的形象范围。",
    "新建 works/horse-treading-xiongnu.md：sub_type sculpture，primary_dimension B，secondary A；单件作品，墓与整组石刻归 places/huoqubing-mu.md。",
    "六节齐全；不补石雕尺寸、石质与现藏；不据图版描述马与人的姿态细节；整组件数与名录只在墓条展开，本条只留一句背景。",
    "canonical 为新建《马踏匈奴》条目；与 places/huoqubing-mu.md 是单件与墓群的分工。")

add("cand-05-30", "马王堆帛地图", "create", "04-knowledge/units/works/mawangdui-boditu.md",
    "L3183-L3193 给1973年长沙马王堆出土、三幅帛地图（地形图、驻军图、城邑图）、西汉重要地图资料、繁密而井然详备而明晰、地形图18万分之一、驻军图8万分之一与《汉书·地理志》的地理记录。",
    "新建 works/mawangdui-boditu.md：sub_type map，primary_dimension C，secondary B；三幅合一条，按图幅分述。",
    "六节齐全；比例尺照录；三幅图的名称与功能按来源分列；不补图幅尺寸、帛色与墓号；马王堆墓葬背景归 places/mawangdui-hanmu.md。",
    "canonical 为新建马王堆帛地图条目；与 places/mawangdui-hanmu.md 是器物与墓葬的分工。")

if __name__ == "__main__":
    print(len(D))
    with open("_zn_decisions_ch4_b1.json", "w", encoding="utf-8", newline="\n") as h:
        json.dump(D, h, ensure_ascii=False, indent=1)
        h.write("\n")
