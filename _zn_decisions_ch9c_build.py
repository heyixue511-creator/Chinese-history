# -*- coding: utf-8 -*-
"""Build chapter 9 batch C decisions JSON from generated KU files."""
import json
from collections import Counter
from pathlib import Path

ROOT = Path(r"D:/中国设计史研究")
DOC = "2009-zhaonong-zhongguo-yishu-shejishi"
PREFIX = DOC + ":"

CREATES = [
    ("cand-10-128", "04-knowledge/units/works/beihai.md", "作品"),
    ("cand-10-130", "04-knowledge/units/works/jingyiyuan.md", "作品"),
    ("cand-10-131", "04-knowledge/units/works/qianlong-huayuan.md", "作品"),
    ("cand-10-133", "04-knowledge/units/works/bishu-shanzhuang.md", "作品"),
    ("cand-11-001", "04-knowledge/units/terms/jiangnan-yuanlin.md", "术语"),
    ("cand-11-002", "04-knowledge/units/terms/huzhong-tiandi.md", "术语"),
    ("cand-11-006", "04-knowledge/units/works/liuyuan.md", "作品"),
    ("cand-11-007", "04-knowledge/units/works/shizilin.md", "作品"),
    ("cand-11-011", "04-knowledge/units/works/huanxiu-shanzhuang.md", "作品"),
    ("cand-11-013", "04-knowledge/units/works/yipu.md", "作品"),
    ("cand-11-014", "04-knowledge/units/works/tuisiyuan.md", "作品"),
    ("cand-11-015", "04-knowledge/units/works/geyuan.md", "作品"),
    ("cand-11-016", "04-knowledge/units/works/jixiao-shanzhuang.md", "作品"),
    ("cand-11-017", "04-knowledge/units/works/pianshi-shanfang.md", "作品"),
    ("cand-11-019", "04-knowledge/units/works/jichangyuan.md", "作品"),
    ("cand-11-020", "04-knowledge/units/works/yuyuan.md", "作品"),
    ("cand-11-178", "04-knowledge/units/works/shihu-yuan.md", "作品"),
    ("cand-11-179", "04-knowledge/units/works/wanzhu-yuan.md", "作品"),
    ("cand-11-005", "04-knowledge/units/persons/wen-zhengming.md", "人物"),
    ("cand-11-018", "04-knowledge/units/persons/shi-tao.md", "人物"),
    ("cand-11-008", "04-knowledge/units/persons/ni-yunlin.md", "人物"),
    ("cand-11-012", "04-knowledge/units/persons/ge-yuliang.md", "人物"),
    ("cand-11-180", "04-knowledge/units/persons/zhang-lian.md", "人物"),
    ("cand-11-181", "04-knowledge/units/persons/cao-liang.md", "人物"),
    ("cand-11-182", "04-knowledge/units/persons/gu-shanshi.md", "人物"),
    ("cand-11-183", "04-knowledge/units/persons/mi-wanzhong.md", "人物"),
    ("cand-11-184", "04-knowledge/units/persons/liu-e.md", "人物"),
    ("cand-11-030", "04-knowledge/units/publications/hongloumeng.md", "出版物"),
    ("cand-11-185", "04-knowledge/units/publications/laocan-youji.md", "出版物"),
    ("cand-11-026", "04-knowledge/units/terms/tou-lou-shou.md", "术语"),
    ("cand-11-031", "04-knowledge/units/terms/tianbai.md", "术语"),
    ("cand-11-038", "04-knowledge/units/terms/hongyou.md", "术语"),
    ("cand-11-039", "04-knowledge/units/terms/huangyou.md", "术语"),
]

UPDATES = [
    ("cand-11-009", "网师园", "04-knowledge/units/places/suzhou-wangshiyuan.md",
     "既有 KU 据 2011 李立新册 L326-L328 图注立条，source_count 1、version 1、confidence low、primary_dimension D；赵农册 L7382 另记网师园为乾隆年间建筑、有渔隐之意，入园为大厅和撷绣楼，出楼见竹外一枝轩、看松读画轩、射鸭廊，以月到风来亭为主景，游廊连接濯缨水阁、小山丛桂轩，水池如玉环，借碧竹、绿水、秋月、寒松寓意四季，并有殿春簃等建筑与观赏、卧游、宴饮、读书功能。按跨册更新新增赵农来源块，source_count 加 1、version 加 1；新证据为园林布局与景点序列，primary_dimension 由 D 改为 B、secondary 保留 D，confidence 由 low 调为 medium，日期顺延至 2027-04-26。",
     "04-knowledge/units/places/suzhou-wangshiyuan.md（更新）；新增引用 L7382，source_count 1→2，version 1→2，confidence low→medium，primary_dimension D→B。"),
    ("cand-11-027", "《芥子园画谱》", "04-knowledge/units/publications/jieziyuan-huazhuan.md",
     "既有 KU 已据 2004 高丰册 L5174 与赵农册 L7210-L7258 立条，source_count 2、version 1；赵农册 L7425 在造园段把李渔的芥子园与参与编撰的《芥子园画谱》中的树石山水并提，称其对造园艺术有着深远影响，并以《芥子园画谱》为同书异名。按同书多跨度更新，在既有赵农 citation 内追加 L7425，source_count 不增，version 加 1，日期顺延至 2027-04-26；该句只说参与编撰，未明言编撰者为准，条目照录并注明。",
     "04-knowledge/units/publications/jieziyuan-huazhuan.md（更新）；赵农 citation 追加 L7425，source_count 2 不变，version 1→2。"),
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
        "重复实体只保留一个 canonical，其余候选判 rejected",
        "仅图注、单行列举或绪论一句总述不足以立条，实质材料在后续节的候选留待后批处理",
        "图版一律据图注著录，未视觉核验，不据图扩写",
    ],
    "scope_spans": [[7297, 7468]],
    "scope_note": "赵农 2009 册第九章第五节园林与瓷器正文 L7297–L7468 逐段复读，含皇家园林、江南园林、明清造园理念与青花、其他瓷器；候选 source_span 为块级粗跨度，实际引用行均落在本批范围内。图版未视觉核验。",
    "decisions": decisions,
    "notes": "赵农 2009 册第九章第五节 unit 候选 35 条：create 33、update 2、rejected 0。范围 L7297-L7468。新建覆盖皇家园林（北海、静宜园、乾隆花园、避暑山庄）、江南园林总称与壶中天地观念、十二座江南与北方园林（留园、狮子林、环秀山庄、艺圃、退思园、个园、寄啸山庄、片石山房、寄畅园、豫园、十笏园、万竹园）、九位造园相关人物（文征明、石涛、倪云林、戈裕良、张涟、曹谅、顾山师、米万钟、刘鹗）、两部小说（《红楼梦》《老残游记》）与透、漏、瘦、甜白、红釉、黄釉。2 条更新：网师园（跨册，source_count 1→2、version 1→2）与《芥子园画谱》（同书多跨度，source_count 不变、version 1→2）。颐和园、圆明园、拙政园三条候选取自同一节，但已在早前批次 applied；园冶、计成、李渔、青花四候选早前已判 rejected 并入既有条目，本批不重复处理。",
}

out = ROOT / "_zn_decisions_ch9c.json"
out.write_text(json.dumps(cfg, ensure_ascii=False, indent=1) + "\n", encoding="utf-8", newline="\n")
print(Counter(d["action"] for d in decisions), len(decisions))
