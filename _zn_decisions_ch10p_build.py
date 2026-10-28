# -*- coding: utf-8 -*-
"""Build chapter 10 batch P decisions JSON from generated KU files."""
import json
from collections import Counter
from pathlib import Path

ROOT = Path(r"D:/中国设计史研究")
DOC = "2009-zhaonong-zhongguo-yishu-shejishi"
PREFIX = DOC + ":"

# (candidate suffix, target, analysis, apply_note)
CREATES = [
    ("cand-12-05", "04-knowledge/units/publications/nahan.md",
     "《呐喊》是鲁迅小说集。赵农称其简洁朴素、明快大方，有着中国传统书籍与西方书籍装帧结合的特色，并以鲁迅受传统古籍插图与金石碑帖影响、在封面、标题、插图、版式上都有很好意见为背景。检索 `persons/lu-xun.md` 记鲁迅，无《呐喊》出版物条；`publications/liangyou.md`、`publications/zhuangshi-zazhi.md` 为其他刊物。按出版物新建，证据行 L8114。来源未给出版年、出版社、开本、印数与设计者署名，confidence 取 medium。",
     "写入 04-knowledge/units/publications/nahan.md（新建）；引用 L8114。"),
    ("cand-12-07", "04-knowledge/units/publications/panghuang.md",
     "《彷徨》是鲁迅小说集，由陶元庆装帧。赵农称陶元庆的《彷徨》《坟》等作品装帧具有含蓄深刻、饱满整洁的特点。检索无《彷徨》出版物条；`persons/lu-xun.md` 记作者，`publications/nahan.md` 为同段另一部小说集。按出版物新建，证据行 L8114。来源未给出版年、出版社、开本与陶元庆的设计说明，confidence 取 low。",
     "写入 04-knowledge/units/publications/panghuang.md（新建）；引用 L8114。"),
    ("cand-12-08", "04-knowledge/units/publications/fen.md",
     "《坟》是鲁迅文集，由陶元庆装帧。赵农称陶元庆的《彷徨》《坟》等作品装帧具有含蓄深刻、饱满整洁的特点。检索无《坟》出版物条。按出版物新建，证据行 L8114。来源未给出版年、出版社、开本与设计说明，confidence 取 low。",
     "写入 04-knowledge/units/publications/fen.md（新建）；引用 L8114。"),
    ("cand-12-09", "04-knowledge/units/persons/qian-juntao.md",
     "钱君陶是民国时期为文学家设计书籍封面的设计者。赵农称其封面文雅平和、素净古朴，与鲁迅、陶元庆、丰子恺的书籍设计并论。检索无同实体人物；`persons/lu-xun.md` 为同段作者兼设计者。按人物新建，证据行 L8114。来源只一句评语，无生卒、籍贯、教育背景、任职与封面作品清单，confidence 取 low。",
     "写入 04-knowledge/units/persons/qian-juntao.md（新建）；引用 L8114。"),
    ("cand-12-13", "04-knowledge/units/publications/feng-xiaoqing.md",
     "《冯小青》是闻一多为之设计装帧及插图的文学作品。赵农在记闻一多经常为文学作品设计封面时举此为例。检索 `persons/wen-yiduo.md` 记闻一多，无《冯小青》出版物条。按出版物新建，证据行 L8125。来源未给文体、作者、出版年、出版社与开本，confidence 取 low。",
     "写入 04-knowledge/units/publications/feng-xiaoqing.md（新建）；引用 L8125。"),
    ("cand-12-15", "04-knowledge/units/publications/wanxiang.md",
     "《万象》是张光宇设计封面的杂志。赵农称其封面装饰风格显著、大方得体、民族气息浓郁。检索 `persons/zhang-guang-yu.md` 记张光宇，无《万象》出版物条。按出版物新建，证据行 L8125。来源未给创刊年、出版地、主编、刊期与封面图样，confidence 取 low。",
     "写入 04-knowledge/units/publications/wanxiang.md（新建）；引用 L8125。"),
    ("cand-12-18", "04-knowledge/units/publications/zhongguo-lidai-huobi-daxi.md",
     "《中国历代货币大系》是赵农在 1949 年后书籍装帧段举为保持风格的少数作品之一，与张光宇的《装饰》字体设计、集体设计的《毛泽东选集》并列，署名为任意。检索无同实体出版物。按出版物新建，证据行 L8127。来源未给卷数、出版社、出版年、开本与任意的设计分工，confidence 取 low。",
     "写入 04-knowledge/units/publications/zhongguo-lidai-huobi-daxi.md（新建）；引用 L8127。"),
    ("cand-12-19", "04-knowledge/units/publications/maozedong-xuanji.md",
     "《毛泽东选集》是赵农在 1949 年后书籍装帧段举为保持风格的少数作品之一，称其封面为集体设计，与张光宇的《装饰》字体设计、任意的《中国历代货币大系》并列。检索 `persons/mao-zedong.md` 记毛泽东本人，无《毛泽东选集》出版物条。按出版物新建，证据行 L8127。来源未给卷数、出版社、出版年与集体设计成员，confidence 取 low。",
     "写入 04-knowledge/units/publications/maozedong-xuanji.md（新建）；引用 L8127。"),
    ("cand-12-20", "04-knowledge/units/publications/zhongguo-lidai-huihua.md",
     "《中国历代绘画》是人民美术出版社 1978 年出版的大型绘画图录。赵农称其与上海古籍出版社 1980 年的《陈寅恪文集》古朴沉稳、风格典雅。检索无同实体出版物。按出版物新建，证据行 L8131。来源未给编者、卷数、开本与印数，confidence 取 medium。",
     "写入 04-knowledge/units/publications/zhongguo-lidai-huihua.md（新建）；引用 L8131。"),
    ("cand-12-21", "04-knowledge/units/publications/chen-yinke-wenji.md",
     "《陈寅恪文集》是上海古籍出版社 1980 年出版的学者文集。赵农称其与人民美术出版社 1978 年的《中国历代绘画》古朴沉稳、风格典雅。检索无同实体出版物；`persons/chen-yinke.md` 未见于本库当前索引。按出版物新建，证据行 L8131。来源未给卷数、编者、开本与印数，confidence 取 medium。",
     "写入 04-knowledge/units/publications/chen-yinke-wenji.md（新建）；引用 L8131。"),
    ("cand-12-22", "04-knowledge/units/publications/lao-fangzi.md",
     "《老房子》是江苏美术出版社 1993 年出版的图集。赵农在改革开放后书籍装帧恢复段，将其与《中国历代绘画》《陈寅恪文集》《读书》《装饰》《老照片》并列为封面装帧焕然一新的出版物。检索无同实体出版物。按出版物新建，证据行 L8131。来源未给编者、册数、开本与印数，confidence 取 low。",
     "写入 04-knowledge/units/publications/lao-fangzi.md（新建）；引用 L8131。"),
    ("cand-12-23", "04-knowledge/units/publications/lao-zhaopian.md",
     "《老照片》是山东画报出版社出版的图文书。赵农在改革开放后书籍装帧恢复段，将其与《中国历代绘画》《陈寅恪文集》《读书》《装饰》《老房子》并列为封面装帧焕然一新的出版物。检索无同实体出版物。按出版物新建，证据行 L8131。来源未给出版年、编者、辑数、开本与印数，confidence 取 low。",
     "写入 04-knowledge/units/publications/lao-zhaopian.md（新建）；引用 L8131。"),
    ("cand-12-24", "04-knowledge/units/publications/hansheng.md",
     "《汉声》是台湾杂志。赵农称其以现代文化的视野，对传统民间艺术进行梳理，装帧设计也别具匠心，并与香港商业文化书籍装帧的明快醒目并论。检索无同实体出版物。按出版物新建，证据行 L8131。来源未给创刊年、创办人、刊期与开本，confidence 取 medium。",
     "写入 04-knowledge/units/publications/hansheng.md（新建）；引用 L8131。"),
    ("cand-12-162", "04-knowledge/units/publications/dushu.md",
     "《读书》是三联书店创办的杂志。赵农在改革开放后书籍装帧恢复段，将其与《中国历代绘画》《陈寅恪文集》《装饰》《老房子》《老照片》并列为封面装帧焕然一新的出版物。检索无同实体出版物。按出版物新建，证据行 L8131。来源未给创刊年、主编、刊期与开本，confidence 取 low。",
     "写入 04-knowledge/units/publications/dushu.md（新建）；引用 L8131。"),
    ("cand-12-40", "04-knowledge/units/terms/yindanshilin-sebu.md",
     "阴丹士林色布是民国时期以阴丹士林染料染制的色布，在本节以月份牌或报刊广告主体出现：广告以着布女性为主角，标题意为「她何以充满了愉快」，正文列举色泽鲜明、夏日曝晒不褪色、洗涤不褪色等卖点。来源所录广告文字为繁体竖排 OCR，字序与字形残缺，不能逐字引用；本条按可辨语义概述。检索无同实体术语；`terms/yangbu.md` 记近代机织布大类，与本条染色布产品不合并。按术语新建，证据行 L8172-L8175。来源未给品牌、厂商、刊登报刊与年代，confidence 取 low。",
     "写入 04-knowledge/units/terms/yindanshilin-sebu.md（新建）；引用 L8172-L8175；OCR 残缺，未逐字引。"),
    ("cand-12-44", "04-knowledge/units/persons/jin-meisheng.md",
     "金梅生是月份牌设计者中的代表人物之一。赵农将其与郑曼陀、杭穉英、李慕白并列为月份牌设计的代表。检索 `persons/zheng-mantuo.md`、`persons/hang-zhiying.md` 分记郑曼陀与杭穉英，无金梅生条。按人物新建，证据行 L8188。来源只列名，未给生卒、籍贯、师承与代表作品，confidence 取 low。",
     "写入 04-knowledge/units/persons/jin-meisheng.md（新建）；引用 L8188。"),
    ("cand-12-45", "04-knowledge/units/persons/li-mubai.md",
     "李慕白是月份牌设计者中的代表人物之一。赵农将其与郑曼陀、杭穉英、金梅生并列为月份牌设计的代表。检索无同实体人物。按人物新建，证据行 L8188。来源只列名，未给生卒、籍贯、师承与代表作品，confidence 取 low。",
     "写入 04-knowledge/units/persons/li-mubai.md（新建）；引用 L8188。"),
    ("cand-12-46", "04-knowledge/units/publications/guoji-guanggao.md",
     "《国际广告》是 1992 年以后中国探讨广告业的专业杂志之一。赵农在广告复兴段，将其与《中国广告》并称，并记中国艺术设计界引入 CI 设计、建立标准化企业识别系统。检索无同实体出版物。按出版物新建，证据行 L8194。来源未给创办单位、创刊年、刊期与主编，confidence 取 low。",
     "写入 04-knowledge/units/publications/guoji-guanggao.md（新建）；引用 L8194。"),
    ("cand-12-47", "04-knowledge/units/publications/zhongguo-guanggao.md",
     "《中国广告》是 1992 年以后中国探讨广告业的专业杂志之一。赵农在广告复兴段，将其与《国际广告》并称，并记中国艺术设计界引入 CI 设计、建立标准化企业识别系统。检索无同实体出版物。按出版物新建，证据行 L8194。来源未给创办单位、创刊年、刊期与主编，confidence 取 low。",
     "写入 04-knowledge/units/publications/zhongguo-guanggao.md（新建）；引用 L8194。"),
    ("cand-12-50", "04-knowledge/units/terms/youpiao.md",
     "邮票在本节被赵农视为一种特殊的招贴，并举《梅兰芳》《西厢记》《中国民居》《十二生肖》等邮票，称其已成为众多集邮爱好者的珍藏。四个候选题名属同一邮票类别，合并为「邮票」一条，不按四套邮票分列；检索无同实体术语。按术语新建，证据行 L8212。来源未给发行制度、面值、齿孔、印制工艺与发行年代，confidence 取 medium。",
     "写入 04-knowledge/units/terms/youpiao.md（新建）；四条候选合并为一条；引用 L8212。"),
    ("cand-12-52", "04-knowledge/units/publications/zhongguo-baozhuang.md",
     "《中国包装》是包装行业的刊物。赵农称其与《包装年鉴》同为包装行业权威信息发布的刊物。检索无同实体出版物。按出版物新建，证据行 L8218。来源未给创办单位、创刊年、刊期与主编，confidence 取 low。",
     "写入 04-knowledge/units/publications/zhongguo-baozhuang.md（新建）；引用 L8218。"),
    ("cand-12-53", "04-knowledge/units/publications/baozhuang-nianjian.md",
     "《包装年鉴》是包装行业的年鉴。赵农称其与《中国包装》同为包装行业权威信息发布的刊物。检索无同实体出版物；与《中国包装》分属年鉴与期刊，不合并。按出版物新建，证据行 L8218。来源未给编纂单位、创刊年、卷次与主编，confidence 取 low。",
     "写入 04-knowledge/units/publications/baozhuang-nianjian.md（新建）；引用 L8218。"),
    ("cand-12-57", "04-knowledge/units/works/aoyun-2008-biaozhi.md",
     "2008 年北京奥运会标志是赵农在「文化标志」段举为具有中国文化特殊意义的设计作品之一，与申办奥运标志并列。检索 `works/guohui-1950.md` 记国徽，无奥运标志条。按作品新建，证据行 L8236。来源只一句评语，未给设计者、发布年份、图形构成与色彩规范；本条不据来源外材料补奥运视觉识别史，confidence 取 low。",
     "写入 04-knowledge/units/works/aoyun-2008-biaozhi.md（新建）；引用 L8236。"),
    ("cand-12-58", "04-knowledge/units/works/zhongguo-yinhang-biaozhi.md",
     "中国银行标志是赵农在标志设计段举为成功设计之一的企业标志，称其以圆形方孔的古币为依托，演绎出新的精神意义。检索无同实体作品。按作品新建，证据行 L8238。来源未给设计者、启用年份、图形比例、字体与色彩规范，confidence 取 medium。",
     "写入 04-knowledge/units/works/zhongguo-yinhang-biaozhi.md（新建）；引用 L8238。"),
    ("cand-12-59", "04-knowledge/units/works/zhongguo-tielu-biaozhi.md",
     "中国铁路标志是赵农在标志设计段举为成功设计之一的企业标志，称其稳定庄重、简洁明快，给人以特殊思考的印象。检索无同实体作品。按作品新建，证据行 L8238。来源未给设计者、启用年份、图形构成与色彩规范，confidence 取 medium。",
     "写入 04-knowledge/units/works/zhongguo-tielu-biaozhi.md（新建）；引用 L8238。"),
    ("cand-12-60", "04-knowledge/units/works/yongjiu-zixingche.md",
     "「永久」牌自行车是赵农在标志设计段举为成功设计之一的品牌，称其字体变形与自行车形结合密切。检索无同实体作品；`terms/sanzhuan-yixiang.md` 记三转一响中的自行车消费组合，与本条品牌不合并。按作品新建，证据行 L8238。来源未给生产厂家、创牌年份、车型与产量，confidence 取 low。",
     "写入 04-knowledge/units/works/yongjiu-zixingche.md（新建）；引用 L8238。"),
    ("cand-12-61", "04-knowledge/units/works/minhang-fenghuang-biaozhi.md",
     "中国民航「凤凰」标志是赵农在标志设计段举为成功设计之一的企业标志，称其利用中国远古传说中凤鸟的吉祥美丽来表现现代文明。检索无同实体作品。按作品新建，证据行 L8238。来源未给设计者、启用年份、图形构成与色彩规范，confidence 取 medium。",
     "写入 04-knowledge/units/works/minhang-fenghuang-biaozhi.md（新建）；引用 L8238。"),
    ("cand-12-62", "04-knowledge/units/works/zhengxie-huihui.md",
     "中国人民政治协商会议会徽在本节仅以图 10-45 图注出现，正文未展开设计者、年代、图形构成与象征含义。按作品新建，证据行 L8227。图片本身未能核读，本条只登记图注事实，不据来源外材料补会徽设计史，confidence 取 low。",
     "写入 04-knowledge/units/works/zhengxie-huihui.md（新建）；引用 L8227；仅图注，未视觉核验。"),
    ("cand-12-167", "04-knowledge/units/terms/jiaotong-biaozhi.md",
     "交通标志是城市道路中指示通行规则的公共标识系统。赵农称明确的道路交通标志对提高社会生活水平有明显作用，并举红绿灯、斑马线、停车标志、站牌与城市交通图。检索无同实体术语。按术语新建，证据行 L8240。来源未给图形标准、设置规范、颁布年代与具体城市案例，confidence 取 low。",
     "写入 04-knowledge/units/terms/jiaotong-biaozhi.md（新建）；引用 L8240。"),
    ("cand-12-168", "04-knowledge/units/terms/shangpin-biaozhi.md",
     "商品标志是标示商品来源与品牌的视觉记号。赵农称商标在一定程度上能影响商品的市场占有率，区分长期标志与短期标志，并提到欧美日本名牌产品及其品牌标志对设计行业的冲击。检索无同实体术语；`terms/huohua.md`、`terms/zhao-tie.md` 等为其他商业视觉形式。按术语新建，证据行 L8242。来源未给商标法、注册制度与具体品牌案例，confidence 取 medium。",
     "写入 04-knowledge/units/terms/shangpin-biaozhi.md（新建）；引用 L8242。"),
]

UPDATES = [
    ("cand-12-16", "04-knowledge/units/publications/liangyou.md",
     "《良友画报》与既有 `publications/liangyou.md` 同指。赵农 L8125 在记陈之佛、闻一多、张光宇、丁聪、廖冰兄等民国书籍与杂志设计后，称「以及当时的《良友画报》都有一定的影响」，为既有条目补入赵农一源。不新建同名条目，按跨书更新处理：新增赵农 2009 来源块，source_count 2→3，version 1→2，日期续为 2026-10-26。",
     "更新 04-knowledge/units/publications/liangyou.md（跨书新增来源）；引用 L8125。"),
    ("cand-12-17", "04-knowledge/units/publications/zhuangshi-zazhi.md",
     "《装饰》与既有 `publications/zhuangshi-zazhi.md` 同指。赵农两处提到：L8127 在 1949 年后书籍装帧段举「张光宇的《装饰》等字体设计」为少数保持风格者；L8131 在改革开放后段列「中央工艺美术学院的《装饰》」封面装帧焕然一新。L8127 未说明是杂志还是单行本，本条按同名杂志归并并保留不确定。不新建同名条目，按跨书更新处理：新增赵农 2009 来源块，source_count 2→3，version 1→2。",
     "更新 04-knowledge/units/publications/zhuangshi-zazhi.md（跨书新增来源）；引用 L8127、L8131，并标注载体不确定。"),
]


def title_of(path):
    for line in Path(path).read_text(encoding="utf-8").splitlines():
        if line.startswith("title:"):
            return line.split(":", 1)[1].strip().split("（")[0].strip()
    return Path(path).stem


decisions = []
for suffix, target, analysis, apply_note in CREATES:
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

for suffix, target, analysis, apply_note in UPDATES:
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

cfg = {
    "doc": DOC,
    "file": "03基础书籍-md文档/中国艺术设计史_赵农_2009_高等教育出版社.md",
    "rules": [
        "单册单源新建：consensus=tentative，evidence_status=source_backed，source_count=1，version=1",
        "跨书新增来源：sources 追加新来源块，source_count 加 1，version 加 1",
        "逐字引文用“ ”，跨行或作者判断用「 」，作者自撰短语不用引号，正文禁 ASCII 双引号",
        "列举型候选只著录来源所列名称、出版者、年份与评语，不据来源外材料补版本史、印数与设计者",
        "同名实体不重复立条：良友画报与《装饰》按跨书更新处理",
        "四条邮票候选合并为「邮票」一条，不按单套邮票分列",
        "阴丹士林色布广告文字 OCR 残缺，只作语义概述，不逐字引用",
        "图版一律据图注著录，未视觉核验，不据图扩写；政协徽仅图注一行",
        "原文疑误与内部张力照录标注，不径改",
    ],
    "scope_spans": [[8103, 8245]],
    "scope_note": "赵农 2009 册第十章第五节书籍与包装 L8103–L8245 逐段复读，含书籍装帧、纸张、印刷、广告招贴、包装与标志六小节；候选 source_span 为块级粗跨度，实际引用行均落在本批范围内。图 10-37 至图 10-46 未视觉核验；阴丹士林广告文字为残缺 OCR。",
    "decisions": decisions,
    "notes": "赵农 2009 册第十章第五节 unit 候选 32 条：create 30、update 2。范围 L8103-L8245。新建覆盖《呐喊》《彷徨》《坟》《冯小青》《万象》《中国历代货币大系》《毛泽东选集》《中国历代绘画》《陈寅恪文集》《老房子》《老照片》《汉声》《读书》《国际广告》《中国广告》《中国包装》《包装年鉴》十七种出版物，钱君陶、金梅生、李慕白三人，阴丹士林色布、邮票、交通标志、商品标志四术语，2008 北京奥运标志、中国银行标志、中国铁路标志、永久牌自行车、民航凤凰标志、政协徽六件作品；update 为《良友画报》与《装饰》。鲁迅、陈之佛、闻一多、张光宇、郑曼陀、杭穉英等已有 KU，本批不重复立条；国徽已有 `works/guohui-1950.md`，不新建。图 10-37 至图 10-46 未视觉核验。",
}

out = ROOT / "_zn_decisions_ch10p.json"
out.write_text(json.dumps(cfg, ensure_ascii=False, indent=1) + "\n", encoding="utf-8", newline="\n")
print(Counter(d["action"] for d in decisions), len(decisions))
