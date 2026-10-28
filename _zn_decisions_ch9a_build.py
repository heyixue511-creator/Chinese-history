# -*- coding: utf-8 -*-
"""Build chapter 9 batch A decisions JSON from generated KU files."""
import json
import re
from collections import Counter
from pathlib import Path

ROOT = Path(r"D:/中国设计史研究")
DOC = "2009-zhaonong-zhongguo-yishu-shejishi"
PREFIX = DOC + ":"

CREATES = [
    ("cand-10-01", "04-knowledge/units/works/ming-changcheng.md", "作品"),
    ("cand-10-06", "04-knowledge/units/persons/zheng-he.md", "人物"),
    ("cand-10-09", "04-knowledge/units/publications/nongzheng-quanshu.md", "出版物"),
    ("cand-10-11", "04-knowledge/units/works/jingzhang-tielu.md", "作品"),
    ("cand-10-12", "04-knowledge/units/persons/zhan-tianyou.md", "人物"),
    ("cand-10-136", "04-knowledge/units/persons/tang-ruowang.md", "人物"),
    ("cand-10-147", "04-knowledge/units/persons/nan-huairen.md", "人物"),
    ("cand-10-17", "04-knowledge/units/persons/kuaixiang.md", "人物"),
    ("cand-10-18", "04-knowledge/units/terms/zuo-zu-you-she.md", "术语"),
    ("cand-10-19", "04-knowledge/units/places/xi-yuan.md", "地点"),
    ("cand-10-21", "04-knowledge/units/works/tiantan.md", "作品"),
    ("cand-10-22", "04-knowledge/units/works/xiannongtan.md", "作品"),
    ("cand-10-23", "04-knowledge/units/works/taihedian.md", "作品"),
    ("cand-10-139", "04-knowledge/units/terms/qianchao-houshi.md", "术语"),
    ("cand-10-25", "04-knowledge/units/works/nanjing-chengqiang.md", "作品"),
    ("cand-10-27", "04-knowledge/units/works/shenyang-gugong.md", "作品"),
    ("cand-10-29", "04-knowledge/units/works/wudangshan-daoguan.md", "作品"),
    ("cand-10-30", "04-knowledge/units/works/wudang-jinding-tongdian.md", "作品"),
    ("cand-10-32", "04-knowledge/units/works/chengde-waibamiao.md", "作品"),
    ("cand-10-34", "04-knowledge/units/works/ming-xiaoling.md", "作品"),
    ("cand-10-35", "04-knowledge/units/works/ming-shisanling.md", "作品"),
    ("cand-10-36", "04-knowledge/units/works/changling-lengendian.md", "作品"),
    ("cand-10-37", "04-knowledge/units/works/dingling.md", "作品"),
    ("cand-10-38", "04-knowledge/units/works/qing-xiling.md", "作品"),
    ("cand-10-39", "04-knowledge/units/works/qing-dongling.md", "作品"),
    ("cand-10-40", "04-knowledge/units/places/shanhaiguan.md", "地点"),
    ("cand-10-41", "04-knowledge/units/places/juyongguan.md", "地点"),
    ("cand-10-42", "04-knowledge/units/places/badaling.md", "地点"),
    ("cand-10-43", "04-knowledge/units/places/jiayuguan.md", "地点"),
]

UPDATES = [
    ("cand-10-02", "紫禁城", "04-knowledge/units/works/beijing-zijincheng.md",
     "既有 KU 据 2016 夏燕靖册《明史》等引文立条；赵农册 L6687 记永乐年间工部侍郎蒯祥规划营建，L6689 记前三殿（皇极殿即清太和殿、中极殿、建极殿）与后三宫（乾清宫、交泰殿、坤宁宫）为主体、大小房屋 9999 间、占地 72 万平方米，L6691 记御花园与乾隆加筑宁寿宫花园，L6693 记角楼俗称“九梁十八柱七十二脊”、护城河俗称“筒子河”，L6701 记前朝后室规范。按跨册更新新增赵农来源块，source_count 加 1，version 加 1，日期顺延至 2027-04-26。",
     "04-knowledge/units/works/beijing-zijincheng.md（更新）；新增引用 L6687、L6689、L6691、L6693、L6701。"),
    ("cand-10-10", "大清工部工程作法则例", "04-knowledge/units/publications/gongcheng-zuofa.md",
     "既有 KU 已据 2016 夏燕靖册与 2009 夏燕靖册立条，source_count 2；赵农册 L6649 以《大清工部工程作法则例》之名记其为一部清代建筑的法典，未给卷数与颁行年代，属同一书名的又一异写。按跨册更新新增赵农来源块，source_count 加 1，version 加 1，别名补“大清工部工程作法则例”。",
     "04-knowledge/units/publications/gongcheng-zuofa.md（更新）；新增引用 L6649。"),
    ("cand-10-16", "北京中轴线", "04-knowledge/units/terms/central-axis.md",
     "既有 KU 据赵农册 L1227、L1281 记二里头与岐山西周宫室的中轴线，source_count 1；L6668 记明清北京以南北中轴线为都城标志：南起永定门至正阳门为外城，正阳门穿承天门进紫禁城、过景山至地安门为宫城，地安门以北至钟鼓楼止于北城墙，三段格局展示都城设计文化意义。按同书多跨度更新扩展 citation，source_count 不增，version 加 1。",
     "04-knowledge/units/terms/central-axis.md（更新）；citation 扩至 L1227、L1281、L6668。"),
    ("cand-10-26", "明代西安城", "04-knowledge/units/places/xian.md",
     "既有 KU 据赵农册 L7811 记西安当代城市形象与明代城墙，source_count 1；L6745 记明清西安以隋唐旧城废墟为基础、利用西、南旧城墙修筑，L6749 记钟鼓楼与十字街，L6751 记城墙周长 14 公里、高 12 米、箭楼瓮城城门序列与明末关城梢门关厢。按同书多跨度更新扩展 citation，source_count 不增，version 加 1。",
     "04-knowledge/units/places/xian.md（更新）；citation 扩至 L6745、L6749、L6751、L7811。"),
]

REJECTS = [
    ("cand-10-03", "江南私家园林", None,
     "绪论 L6641 只有一句总述（江南私家园林是明清个人心态的展示、对政治专制的逃遁，将自然山水与名花奇石汇于一园），未给园名、造园手法与实例；本章第五节 L7346–L7416 对江南园林有整段展开，并另有候选 cand-11-001，届时按该段立条。本候选不另建条，避免同一概念两目。",
     "判 rejected：绪论仅一句总述，实质材料在第五节 L7346–L7416，留待 cand-11-001 处理。",
     "无 canonical；材料保留在来源层。"),
]


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
        "approve": f"批准更新 {target}：保留既有来源，新增赵农 2009 册引用并顺延复核日期。",
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
        "逐字引文用“ ”，跨行或作者判断用「 」，作者自撰短语不用引号，正文禁 ASCII 双引号",
        "原文疑误与内部张力照录标注，不径改",
        "重复实体只保留一个 canonical，其余候选判 rejected",
        "仅图注、单行列举或绪论一句总述不足以立条，实质材料在后续节的候选留待后批处理",
        "图版一律据图注著录，未视觉核验，不据图扩写",
    ],
    "scope_spans": [[6599, 6833]],
    "scope_note": "赵农 2009 册第九章第一至第二节正文 L6599–L6833 逐段复读，含绪论（明清政治、江南园林、科学知识、火器造船、工艺文献、京张铁路）与城市建筑的都城、地方城市、寺观、皇家陵园、万里长城五目；候选 source_span 为块级粗跨度，实际引用行均落在本批范围内。图版未视觉核验。",
    "decisions": decisions,
    "notes": "赵农 2009 册第九章第一至第二节 unit 候选 34 条：create 29、update 4、rejected 1。范围 L6599-L6833。新建覆盖明长城、郑和、农政全书、京张铁路与詹天佑、汤若望与南怀仁、蒯祥、左祖右社、西苑、天坛、先农坛、太和殿、前朝后室、南京城墙、沈阳故宫、武当山道观与金顶铜殿、承德外八庙、明孝陵、明十三陵、长陵棱恩殿、定陵、清西陵、清东陵、山海关、居庸关、八达岭、嘉峪关。4 条更新为紫禁城、工程做法、中轴线、西安；1 条 rejected（江南私家园林绪论仅一句，实质材料留待第五节候选）。本批 31 条 claim 候选仍保持 needs_evidence，未进入 claim-registry。",
}

out = ROOT / "_zn_decisions_ch9a.json"
out.write_text(json.dumps(cfg, ensure_ascii=False, indent=1) + "\n", encoding="utf-8", newline="\n")
print(Counter(d["action"] for d in decisions), len(decisions))
