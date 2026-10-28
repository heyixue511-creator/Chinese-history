# -*- coding: utf-8 -*-
"""Build chapter 9 batch D decisions JSON from generated KU files."""
import json
from collections import Counter
from pathlib import Path

ROOT = Path(r"D:/中国设计史研究")
DOC = "2009-zhaonong-zhongguo-yishu-shejishi"
PREFIX = DOC + ":"

CREATES = [
    ("cand-11-047", "04-knowledge/units/terms/mingzhuang.md", "术语"),
    ("cand-11-051", "04-knowledge/units/terms/bijia.md", "术语"),
    ("cand-11-052", "04-knowledge/units/terms/sancun-jinlian.md", "术语"),
    ("cand-11-053", "04-knowledge/units/terms/guapi-mao.md", "术语"),
    ("cand-11-056", "04-knowledge/units/terms/sizhua-mao.md", "术语"),
    ("cand-11-057", "04-knowledge/units/terms/mingdai-san-da-chuanxing.md", "术语"),
    ("cand-11-058", "04-knowledge/units/terms/haijin.md", "术语"),
    ("cand-11-059", "04-knowledge/units/terms/qianhai-ling.md", "术语"),
    ("cand-11-060", "04-knowledge/units/works/huanghu-hao.md", "作品"),
    ("cand-11-061", "04-knowledge/units/persons/xu-shou.md", "人物"),
    ("cand-11-067", "04-knowledge/units/works/dawankou-chong.md", "作品"),
    ("cand-11-069", "04-knowledge/units/terms/folangji-pao.md", "术语"),
    ("cand-11-070", "04-knowledge/units/terms/hongyi-pao.md", "术语"),
    ("cand-11-071", "04-knowledge/units/terms/shenwei-dajiangjun-pao.md", "术语"),
    ("cand-11-072", "04-knowledge/units/works/humen-huopao.md", "作品"),
    ("cand-11-074", "04-knowledge/units/persons/wanhu.md", "人物"),
    ("cand-11-075", "04-knowledge/units/persons/feng-ru.md", "人物"),
    ("cand-11-076", "04-knowledge/units/persons/yang-yixian.md", "人物"),
    ("cand-11-077", "04-knowledge/units/works/wusong-tielu.md", "作品"),
    ("cand-11-078", "04-knowledge/units/works/tangxu-tielu.md", "作品"),
    ("cand-11-079", "04-knowledge/units/works/longhao-jiche.md", "作品"),
]

UPDATES = [
    ("cand-11-048", "明代女装裙式（百褶裙、凤尾裙、玉裙）", "04-knowledge/units/terms/ming-dai-nvzhuang.md",
     "候选是百褶裙、凤尾裙、玉裙三名裙式的清单级聚合，来源只在女装段一句并列，未给各自形制与尺寸，不足以单独立条。既有 `terms/ming-dai-nvzhuang.md` 是夏燕靖 2009 册 L3514 的明代女装清单级条目，同属明代女装的上位实体；赵农 L7494 的裙褶三名与“细密／飘逸”的差别为该条新增材料，按跨册更新补入。百褶裙另已由 `terms/yang-chang-qun.md` 以羊肠裙立目、百褶裙为别名，不另立条，也不与羊肠裙合并。更新新增赵农 source 条，source_count 1→2、version 1→2，日期顺延至 2027-04-26。",
     "04-knowledge/units/terms/ming-dai-nvzhuang.md（更新）；新增赵农 L7494 来源块，source_count 1→2，version 1→2；裙式三名并入，不另立条。"),
    ("cand-11-050", "褙子", "04-knowledge/units/terms/beizi.md",
     "既有 KU 以背子立目、褙子为别名，据赵农册 L5725、L5738 记宋代形制与女性服用。赵农册 L7499 在明代民服节另记褙子为常见服饰、身份不同样式不同，贵族合领大袖对襟与庶民直领小袖对襟有细微区别；该段起句作“褥子”，下文均作“褙子”，疑为字讹，照录标疑。按同书多跨度更新，在既有赵农 citation 内追加 L7499，source_count 不增，version 加 1。",
     "04-knowledge/units/terms/beizi.md（更新）；赵农 citation 追加 L7499，source_count 1 不变，version 1→2。"),
    ("cand-11-082", "人字形铁路", "04-knowledge/units/works/jingzhang-tielu.md",
     "人字形铁路是京张铁路在北京八达岭青龙桥车站的线路设计，来源未把它列为独立作品名目。既有 `works/jingzhang-tielu.md` 已据赵农册 L6651 记人字形爬坡铁轨与两台机车；L7591 另记 1909 年通车与近代化评价，L7593-L7595 给耶鲁学历、工程压力、青龙桥车站的“人”字形铁路、石拱桥减预算与中国人自行设计的第一条铁路，均为同一条目的新增材料。按同书多跨度更新，在既有 citation 内追加 L7591、L7593-L7595，source_count 不增，version 加 1；不另立“人字形铁路”条目。",
     "04-knowledge/units/works/jingzhang-tielu.md（更新）；赵农 citation 追加 L7591、L7593-L7595，source_count 1 不变，version 1→2。"),
]

OVERRIDES = {
    "cand-11-047": "明装是明代庶民服装样式日趋丰富而形成的服饰特色。既有 `terms/ming-dai-nvzhuang.md` 记明代女装与冠饰，`terms/xiapei.md` 记霞帔，本候选为庶民服饰总称与男装配套，无同实体条目；按术语新建，证据行 L7492、L7494、L7503、L7507。",
    "cand-11-052": "三寸金莲是汉族妇女缠足所穿的小巧木底弓鞋。既有 `terms/huapendi-xie.md` 记满族旗女花盆底鞋，与本条为满汉对照的两类鞋式，非同一实体；按术语新建，证据行 L7505、L7507-L7509。",
    "cand-11-057": "明代三大船型是赵农对明代船型的分类（沙船、福船、广船）。既有 `terms/sida-chuanxing.md` 记 2016 册四大船型（沙船、鸟船、福船、广船），分类不同，另 `terms/shachuan.md`、`terms/fuchuan.md` 为单一船型专条；本条为分类级条目，按术语新建，两说并列不合并，证据行 L7533、L7535。",
    "cand-11-067": "大碗口铳是洪武年间的铁炮。既有 `procedures/huo-pao-zhuzao.md` 记明清火炮铸造工序并提及本炮，但工序不是炮器本体；按作品新建，证据行 L7553。",
    "cand-11-069": "佛朗机炮是明代正德年间传入并仿制的火炮。`procedures/huo-pao-zhuzao.md` 记铸造工序，非炮型本体；按术语新建，证据行 L7562。",
    "cand-11-070": "红夷炮是荷兰火炮的俗称。`procedures/huo-pao-zhuzao.md` 只在佛朗机炮末句提及，非炮型本体；按术语新建，证据行 L7562。",
    "cand-11-071": "神威大将军炮是清代火炮名目。`procedures/huo-pao-zhuzao.md` 只在铸造段并称，非炮型本体；按术语新建，证据行 L7564。",
    "cand-11-072": "虎门火炮是道光年间铸造的虎门炮台铁炮。`procedures/huo-pao-zhuzao.md` 记铸造工序并引其尺寸，`events/opium-war.md` 记战争，均非炮器本体；按作品新建，证据行 L7564。",
    "cand-11-060": "黄鹄号是 1865 年徐寿等人制造的机械轮船。既有 `events/xu-shou-hua-hengfang-zhengqi-ji.md` 记同治元年蒸汽机研制，事件不同；按作品新建，证据行 L7549。",
    "cand-11-061": "徐寿是晚清造船者。既有 `events/xu-shou-hua-hengfang-zhengqi-ji.md` 为徐寿、华衡芳研制蒸汽机的事件条目，无人物条目；按人物新建，证据行 L7549。",
}


def first_sentences(text, n=2):
    out, buf = [], ""
    for ch in text:
        buf += ch
        if ch in "。！？":
            out.append(buf)
            buf = ""
            if len(out) == n:
                return "".join(out)
    return "".join(out) or text


def location_of(path):
    for line in Path(path).read_text(encoding="utf-8").splitlines():
        if line.strip().startswith("location:"):
            return line.split(":", 1)[1].strip().strip('"')
    return ""


def title_of(path):
    for line in Path(path).read_text(encoding="utf-8").splitlines():
        if line.startswith("title:"):
            return line.split(":", 1)[1].strip().split("（")[0].strip()
    return Path(path).stem


decisions = []
for suffix, target, kind in CREATES:
    text = Path(target).read_text(encoding="utf-8")
    desc = text.split("## 描述", 1)[1].split("## 核心内容", 1)[0].strip()
    lead = first_sentences(desc)
    lines = location_of(target)
    analysis = OVERRIDES.get(suffix) or f"{lead}检索既有 KU 无同实体条目，按{kind}新建；证据行 {lines}。"
    decisions.append({
        "cid": PREFIX + suffix,
        "entity": title_of(target),
        "action": "create",
        "target": target,
        "analysis": analysis,
        "approve": f"批准新建 {target}：单册单源，consensus=tentative，confidence 按证据厚度评定。",
        "apply_note": f"写入 {target}（新建）；引用 {lines}。",
        "note": f"canonical: {target}。",
    })

for suffix, entity, target, analysis, apply_note in UPDATES:
    decisions.append({
        "cid": PREFIX + suffix,
        "entity": entity,
        "action": "update",
        "target": target,
        "analysis": analysis,
        "approve": f"批准更新 {target}：保留既有来源，补入赵农 2009 册材料并顺延复核日期。",
        "apply_note": apply_note,
        "note": f"canonical: {target}。",
    })

cfg = {
    "doc": DOC,
    "file": "03基础书籍-md文档/中国艺术设计史_赵农_2009_高等教育出版社.md",
    "rules": [
        "单册单源新建：consensus=tentative，evidence_status=source_backed，source_count=1，version=1",
        "同书多跨度更新：sources 单条 citation 内逗号分隔，source_count 不增，version 加 1",
        "跨册更新：新增 source 条，source_count 加 1，version 加 1，review_due 延至 2027-04-26",
        "逐字引文用“ ”，跨行或作者判断用「 」，作者自撰短语不用引号，正文禁 ASCII 双引号",
        "原文疑误与内部张力照录标注，不径改",
        "清单级聚合不足以单独立条时，并入同名的上位实体或分类级条目，并在裁定中写明",
        "同一实体只保留一个 canonical；既有专条不因同段并提而合并",
        "图版一律据图注著录，未视觉核验，不据图扩写",
    ],
    "scope_spans": [[7469, 7596]],
    "scope_note": "赵农 2009 册第九章第六节服饰与交通正文 L7469–L7596 逐段复读，含官服、民服、造船、大炮、飞机与京张铁路；候选 source_span 为块级粗跨度，实际引用行均落在本批范围内。图版未视觉核验。",
    "decisions": decisions,
    "notes": "赵农 2009 册第九章第六节 unit 候选 24 条：create 21、update 3、rejected 0。范围 L7469-L7596。新建覆盖明装、比甲、三寸金莲、瓜皮帽、四爪锚、明代三大船型、海禁、迁海令、黄鹄号、徐寿、大碗口铳、佛朗机炮、红夷炮、神威大将军炮、虎门火炮、万户、冯如、杨逸仙、吴淞铁路、唐胥铁路、龙号机车；更新为明代女装（并入三名裙式）、背子（追加明代 L7499）与京张铁路（并入人字形 L7591、L7593-L7595）。官服补子与帽子段无候选；霞帔已有专条；百褶裙由羊肠裙条以别名著录；火炮铸造工序已有 procedure 条目，本批只立炮器与炮型本体。",
}

out = ROOT / "_zn_decisions_ch9d.json"
out.write_text(json.dumps(cfg, ensure_ascii=False, indent=1) + "\n", encoding="utf-8", newline="\n")
print(Counter(d["action"] for d in decisions), len(decisions))
