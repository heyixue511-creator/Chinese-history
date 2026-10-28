# -*- coding: utf-8 -*-
"""Build the chapter 8 decisions JSON from the generated KU files."""
import json
from pathlib import Path

ROOT = Path(r"D:/中国设计史研究")
DOC = "2009-zhaonong-zhongguo-yishu-shejishi"
PREFIX = DOC + ":"

CREATES = [
    ("cand-08-183", "04-knowledge/units/persons/yelv-abaoji.md", "人物"),
    ("cand-08-184", "04-knowledge/units/persons/aguda.md", "人物"),
    ("cand-08-185", "04-knowledge/units/persons/li-yuanhao.md", "人物"),
    ("cand-08-186", "04-knowledge/units/persons/chengjisihan.md", "人物"),
    ("cand-08-187", "04-knowledge/units/persons/hubilie.md", "人物"),
    ("cand-09-01", "04-knowledge/units/terms/qidan-wenzi.md", "术语"),
    ("cand-09-02", "04-knowledge/units/terms/nvzhen-wenzi.md", "术语"),
    ("cand-09-03", "04-knowledge/units/terms/xixia-wenzi.md", "术语"),
    ("cand-09-04", "04-knowledge/units/terms/basiba-zi.md", "术语"),
    ("cand-09-05", "04-knowledge/units/terms/huihui-wenzi.md", "术语"),
    ("cand-09-06", "04-knowledge/units/publications/liaozang.md", "出版物"),
    ("cand-09-07", "04-knowledge/units/publications/mengqiu.md", "出版物"),
    ("cand-09-09", "04-knowledge/units/publications/jinzang.md", "出版物"),
    ("cand-09-10", "04-knowledge/units/publications/weimojie-suoshuo-jing.md", "出版物"),
    ("cand-09-12", "04-knowledge/units/publications/yuhai.md", "出版物"),
    ("cand-09-13", "04-knowledge/units/publications/zhupu.md", "出版物"),
    ("cand-09-15", "04-knowledge/units/publications/jingangjing-zhu.md", "出版物"),
    ("cand-09-16", "04-knowledge/units/publications/xin-quanxiang-sanguozhi-pinghua.md", "出版物"),
    ("cand-09-17", "04-knowledge/units/terms/huaya.md", "术语"),
    ("cand-09-18", "04-knowledge/units/terms/yuanzhuwen.md", "术语"),
    ("cand-09-19", "04-knowledge/units/persons/zhao-mengfu.md", "人物"),
    ("cand-09-22", "04-knowledge/units/works/zhishun-sannian-tong-huoqiang.md", "作品"),
    ("cand-09-23", "04-knowledge/units/terms/xuanfeng-pao.md", "术语"),
    ("cand-09-24", "04-knowledge/units/works/penglai-yuan-zhanshu.md", "作品"),
    ("cand-09-25", "04-knowledge/units/terms/tuoche-xiche.md", "术语"),
    ("cand-09-28", "04-knowledge/units/works/tonghuihe.md", "作品"),
    ("cand-09-29", "04-knowledge/units/works/huitonghe.md", "作品"),
    ("cand-09-30", "04-knowledge/units/places/liao-wujing.md", "地点"),
    ("cand-09-32", "04-knowledge/units/persons/liu-bingzhong.md", "人物"),
    ("cand-09-33", "04-knowledge/units/works/dule-si-guanyin-ge.md", "作品"),
    ("cand-09-34", "04-knowledge/units/works/huayan-si.md", "作品"),
    ("cand-09-35", "04-knowledge/units/works/yingxian-muta.md", "作品"),
    ("cand-09-36", "04-knowledge/units/persons/wang-chongyang.md", "人物"),
    ("cand-09-38", "04-knowledge/units/works/chaoyuan-tu.md", "作品"),
    ("cand-09-41", "04-knowledge/units/works/xixia-wangling.md", "作品"),
    ("cand-09-42", "04-knowledge/units/works/lugou-qiao.md", "作品"),
    ("cand-09-44", "04-knowledge/units/works/dengfeng-guanxingtai.md", "作品"),
    ("cand-09-45", "04-knowledge/units/publications/shoushi-li.md", "出版物"),
    ("cand-09-46", "04-knowledge/units/terms/kunfa.md", "术语"),
    ("cand-09-50", "04-knowledge/units/terms/sadalaqi.md", "术语"),
    ("cand-09-51", "04-knowledge/units/terms/jiaoche.md", "术语"),
    ("cand-09-59", "04-knowledge/units/terms/luanbai-you-ci.md", "术语"),
    ("cand-09-62", "04-knowledge/units/terms/yuan-dai-qiqi-zhuangshi.md", "术语"),
    ("cand-09-63", "04-knowledge/units/works/dushan-dayuhai.md", "作品"),
    ("cand-09-66", "04-knowledge/units/terms/shuilun-sanshi.md", "术语"),
    ("cand-09-68", "04-knowledge/units/terms/jin-dai-jiaochao.md", "术语"),
    ("cand-09-69", "04-knowledge/units/terms/yuan-dai-zhibi.md", "术语"),
    ("cand-09-86", "04-knowledge/units/persons/wang-mian.md", "人物"),
    ("cand-09-87", "04-knowledge/units/persons/sun-wei.md", "人物"),
    ("cand-09-89", "04-knowledge/units/terms/fozhuang.md", "术语"),
    ("cand-09-90", "04-knowledge/units/terms/sufu.md", "术语"),
    ("cand-09-91", "04-knowledge/units/works/lanyou-bailongwen-meiping.md", "作品"),
    ("cand-09-93", "04-knowledge/units/terms/qionglu-zhanzhang.md", "术语"),
    ("cand-09-95", "04-knowledge/units/terms/heiche-baizhang.md", "术语"),
]

UPDATES = [
    ("cand-08-189", "辽三彩", "04-knowledge/units/terms/liao-sancai.md",
     "既有 KU 已据 2016 夏燕靖册立条，并保留「辽三彩是否低温铅釉」的存疑；赵农 2009 册 L5884 记辽瓷对唐三彩的继承、L6352 记辽三彩为低温釉陶，以单色黄、绿、白釉，质地松脆、釉面粗糙为基本样式。按跨册更新新增赵农来源块，source_count 加 1，version 加 1，日期顺延至 2027-04-26。",
     "04-knowledge/units/terms/liao-sancai.md（更新）；新增引用 L5884、L6352。"),
    ("cand-09-21", "火铳", "04-knowledge/units/works/yuan-huoqiang.md",
     "既有 KU 据 2016 夏燕靖册记元代火铳铸造与浸铜法；赵农册 L6061 记火铳成为火枪火炮的基本结构，L6065 记 13 世纪起源、铳即筒的转音、手铳与盏口铳两类及西安东关铳、至顺三年铳尺寸，L6072 记火铳部队编制与《元史》引文。按跨册更新新增来源块，source_count 加 1，version 加 1。",
     "04-knowledge/units/works/yuan-huoqiang.md（更新）；新增引用 L6061、L6065、L6072。"),
    ("cand-09-52", "水力大纺车", "04-knowledge/units/terms/dafangche.md",
     "既有 KU 记宋代大纺车并引《王祯农书》；赵农册 L5336 属宋代段、L6304 属元代纺织段，记大纺车的加捻卷绕、传动、原动三部分结构，增加纱锭、提高加捻卷绕速度并利用水力。按同书更新扩展赵农 citation，source_count 不增，version 加 1，并标注两跨度断代未明。",
     "04-knowledge/units/terms/dafangche.md（更新）；赵农 citation 扩展至 L5336、L6304。"),
    ("cand-09-54", "皮囊壶（鸡冠壶）", "04-knowledge/units/terms/jiguang-hu.md",
     "既有 KU 已据五册立条；赵农册 L5867、L5884、L6325 分别记皮囊形制瓷壶、绿釉划花鸡冠壶与 L6325 的扁圆造型、管状口、环形提梁及游牧适应。按跨册更新新增赵农来源块，source_count 加 1，version 加 1。",
     "04-knowledge/units/terms/jiguang-hu.md（更新）；新增引用 L5867、L5884、L6325。"),
    ("cand-09-94", "地穴式", "04-knowledge/units/terms/bandixue-shi-jianzhu.md",
     "既有 KU 记半地穴式建筑；赵农册 L6431 记女真早期地穴式建筑结构（篱笆墙、木板树皮茅草顶、门东向、环形土床即土炕连通锅灶）及唐宋黄河以北土炕取暖的流传。按术语近缘并入并保留来源用词，新增赵农来源块，source_count 加 1，version 加 1。",
     "04-knowledge/units/terms/bandixue-shi-jianzhu.md（更新）；新增引用 L6431。"),
]

REJECTS = [
    ("cand-08-192", "青花凤首扁壶", None,
     "该候选仅对应图 8-2 图注（L5861）“元 青花凤首扁壶”，绪论正文未展开器形、年代、窑口、藏地与工艺；单条图注不足以支撑独立条目。",
     "判 rejected：仅图注，本候选不另建条。",
     "无 canonical；图 8-2 图注保留在来源层。"),
    ("cand-08-193", "青花双龙纹四系扁壶", None,
     "该候选仅对应图 8-4 图注（L5872）“元 青花双龙纹四系扁壶”，正文未展开器形、年代、窑口与藏地；单条图注不足以支撑独立条目。",
     "判 rejected：仅图注，本候选不另建条。",
     "无 canonical；图 8-4 图注保留在来源层。"),
    ("cand-09-48", "元昊（李元昊）", "04-knowledge/units/persons/li-yuanhao.md",
     "与 cand-08-185 同指李元昊；本批已按 08-185 新建 persons/li-yuanhao.md，并将 L6255–L6259 的服饰材料并入该条，重复立条会造成同一人物两目。",
     "判 rejected：canonical 取 04-knowledge/units/persons/li-yuanhao.md，本候选内容已并入，不另建条。",
     "canonical: 04-knowledge/units/persons/li-yuanhao.md。"),
    ("cand-09-85", "《道藏》", None,
     "L5982 仅与《金藏》并列提及“道教《道藏》”，未给卷数、刊刻与装帧内容；赵农册对《道藏》的实质记载在明代段 L7144（《正统道藏》5302 卷、480 函），不属本章范围。",
     "判 rejected：本章仅并列提及，本候选不立条；明代段材料留待后续批次。",
     "无 canonical。"),
]


def first_sentences(text, n=2):
    out, buf = [], ""
    for ch in text:
        buf += ch
        if ch == "。":
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
    decisions.append({
        "cid": PREFIX + suffix,
        "entity": title_of(target),
        "action": "create",
        "target": target,
        "analysis": f"{lead}检索既有 KU 无同实体条目，按{kind}新建；证据行 {lines}。",
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
        "approve": f"批准更新 {target}：保留既有来源，新增赵农 2009 册引用块并顺延复核日期。",
        "apply_note": apply_note,
        "note": f"canonical: {target}。",
    })

for suffix, entity, target, analysis, approve, note in REJECTS:
    decisions.append({
        "cid": PREFIX + suffix,
        "entity": entity,
        "action": "rejected",
        "target": target,
        "analysis": analysis,
        "approve": approve,
        "apply_note": "不写回。",
        "note": note,
    })

cfg = {
    "doc": DOC,
    "file": "03基础书籍-md文档/中国艺术设计史_赵农_2009_高等教育出版社.md",
    "rules": [
        "单册单源新建：consensus=tentative，evidence_status=source_backed，source_count=1，version=1",
        "同书多跨度更新：sources 单条 citation 内逗号分隔，source_count 不增，version 加 1",
        "跨册更新：新增 source 条，source_count 加 1，version 加 1，review_due 延至 2027-04-26",
        "逐字引文用“ ”，跨行或作者判断用「 」，作者自撰术语不用引号，正文禁 ASCII 双引号",
        "原文疑误与内部张力照录标注，不径改",
        "重复实体只保留一个 canonical，其余候选判 rejected",
        "仅图注或单行并列提及不足以立条，判 rejected",
        "图版一律据图注著录，未视觉核验，不据图扩写",
    ],
    "scope_spans": [[5825, 6598]],
    "scope_note": "赵农 2009 册第八章（辽金西夏元）正文 L5825–L6598 全章逐段复读，含绪论、文字与印刷、兵器火器与造船、车具与大运河、城巿寺院陵墓桥梁、服饰纺织、制瓷杂器、农具货币与结论；候选 source_span 为块级粗跨度，实际引用行均落在本章范围内。图版未视觉核验。",
    "decisions": decisions,
    "notes": "赵农 2009 册第八章 unit 候选 63 条：create 54、update 5、rejected 4。范围 L5825-L6598。新建覆盖辽金西夏元人物（耶律阿保机、阿骨打、李元昊、成吉思汗、忽必烈、赵孟頫、刘秉忠、王重阳、王冕、孙威）、五种文字、八种出版物、花押与圆朱文、兵器火器、战船、车具、通惠河与会通河、辽五京、辽金寺院塔阁、永乐宫壁画、西夏王陵、卢沟桥、观星台与《授时历》、髡发与佛妆、撒答剌欺与速夫、搅车与卵白釉、漆器技法、渎山大玉海、水轮三事、金元纸币、蓝釉白龙纹梅瓶、穹庐毡帐、黑车白帐。5 条更新为辽三彩、火铳、水力大纺车、皮囊壶（鸡冠壶）、地穴式；4 条判 rejected（两件元青花扁壶仅图注、元昊与 08-185 重复、《道藏》仅并列提及）。本章 19 条 claim 候选仍保持 needs_evidence，未进入 claim-registry。",
}

out = ROOT / "_zn_decisions_ch8.json"
out.write_text(json.dumps(cfg, ensure_ascii=False, indent=1) + "\n", encoding="utf-8", newline="\n")
from collections import Counter
print(Counter(d["action"] for d in decisions), len(decisions))
