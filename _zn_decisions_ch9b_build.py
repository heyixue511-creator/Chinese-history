# -*- coding: utf-8 -*-
"""Build chapter 9 batch B decisions JSON from generated KU files."""
import json
from collections import Counter
from pathlib import Path

ROOT = Path(r"D:/中国设计史研究")
DOC = "2009-zhaonong-zhongguo-yishu-shejishi"
PREFIX = DOC + ":"

CREATES = [
    ("cand-10-46", "04-knowledge/units/terms/zhaopai.md", "术语"),
    ("cand-10-49", "04-knowledge/units/terms/yanghuo.md", "术语"),
    ("cand-10-51", "04-knowledge/units/terms/daming-tongxing-baochao.md", "术语"),
    ("cand-10-52", "04-knowledge/units/terms/qing-baochao.md", "术语"),
    ("cand-10-53", "04-knowledge/units/terms/hubu-guanpiao.md", "术语"),
    ("cand-10-54", "04-knowledge/units/terms/longyang.md", "术语"),
    ("cand-10-55", "04-knowledge/units/works/dalong-youpiao.md", "作品"),
    ("cand-10-57", "04-knowledge/units/persons/liu-mingchuan.md", "人物"),
    ("cand-10-58", "04-knowledge/units/terms/siheyuan.md", "术语"),
    ("cand-10-59", "04-knowledge/units/terms/yaodong.md", "术语"),
    ("cand-10-60", "04-knowledge/units/terms/jiangnan-minju.md", "术语"),
    ("cand-10-61", "04-knowledge/units/terms/matou-qiang.md", "术语"),
    ("cand-10-62", "04-knowledge/units/terms/minnan-tulou.md", "术语"),
    ("cand-10-64", "04-knowledge/units/terms/yikeyin.md", "术语"),
    ("cand-10-65", "04-knowledge/units/terms/diaolou.md", "术语"),
    ("cand-10-66", "04-knowledge/units/terms/menggubao.md", "术语"),
    ("cand-10-141", "04-knowledge/units/terms/shanxi-siheyuan.md", "术语"),
    ("cand-10-68", "04-knowledge/units/terms/guanmao-yi.md", "术语"),
    ("cand-10-70", "04-knowledge/units/terms/meigui-yi.md", "术语"),
    ("cand-10-71", "04-knowledge/units/terms/jiazi-chuang.md", "术语"),
    ("cand-10-72", "04-knowledge/units/terms/luohan-chuang.md", "术语"),
    ("cand-10-73", "04-knowledge/units/terms/babu-chuang.md", "术语"),
    ("cand-10-142", "04-knowledge/units/terms/dengdun.md", "术语"),
    ("cand-10-144", "04-knowledge/units/terms/qingshi-ta.md", "术语"),
    ("cand-10-76", "04-knowledge/units/terms/pilumao.md", "术语"),
    ("cand-10-77", "04-knowledge/units/terms/longdun.md", "术语"),
    ("cand-10-78", "04-knowledge/units/terms/lujiao-yi.md", "术语"),
    ("cand-10-79", "04-knowledge/units/terms/anle-yi.md", "术语"),
    ("cand-10-81", "04-knowledge/units/terms/hubi.md", "术语"),
    ("cand-10-82", "04-knowledge/units/terms/huimo.md", "术语"),
    ("cand-10-87", "04-knowledge/units/terms/taoyan.md", "术语"),
    ("cand-10-88", "04-knowledge/units/terms/chengni-yan.md", "术语"),
    ("cand-10-89", "04-knowledge/units/publications/xiqing-yanpu.md", "出版物"),
    ("cand-10-90", "04-knowledge/units/terms/maobian-zhi.md", "术语"),
    ("cand-10-100", "04-knowledge/units/persons/chen-hongshou.md", "人物"),
    ("cand-10-106", "04-knowledge/units/persons/johannes-gutenberg.md", "人物"),
    ("cand-10-92", "04-knowledge/units/publications/yongle-dadian.md", "出版物"),
    ("cand-10-94", "04-knowledge/units/persons/zhu-zaiyu.md", "人物"),
    ("cand-10-95", "04-knowledge/units/terms/shier-pingjun-lv.md", "术语"),
    ("cand-10-96", "04-knowledge/units/publications/yuelv-quanshu.md", "出版物"),
    ("cand-10-97", "04-knowledge/units/publications/yongle-beizang.md", "出版物"),
    ("cand-10-109", "04-knowledge/units/terms/dianben.md", "术语"),
    ("cand-10-111", "04-knowledge/units/publications/quan-tangshi.md", "出版物"),
    ("cand-10-114", "04-knowledge/units/terms/qingdai-diaoban-chatu.md", "术语"),
    ("cand-10-117", "04-knowledge/units/persons/zhai-jinsheng.md", "人物"),
    ("cand-10-118", "04-knowledge/units/publications/wuyingdian-juzhenban-chengshi.md", "出版物"),
    ("cand-10-145", "04-knowledge/units/publications/nanjiang-yishi-kanben.md", "出版物"),
    ("cand-10-146", "04-knowledge/units/publications/chaobao.md", "出版物"),
    ("cand-10-123", "04-knowledge/units/terms/maozhuang.md", "术语"),
    ("cand-10-124", "04-knowledge/units/terms/hantao.md", "术语"),
    ("cand-10-125", "04-knowledge/units/terms/jiaban.md", "术语"),
    ("cand-10-126", "04-knowledge/units/terms/hanhe.md", "术语"),
    ("cand-10-127", "04-knowledge/units/terms/shuxiang.md", "术语"),
]

UPDATES = [
    ("cand-10-103", "十竹斋画谱", "04-knowledge/units/publications/shizhuzhai-huapu.md",
     "既有 KU 据 2011 李立新册 L1846 与 2016 夏燕靖册 L4619-L4656 立条，source_count 2、version 1；赵农册 L7195 记《十竹斋书画谱》与《十竹斋笺谱》同用短版技术，L7197 记其分书画谱、墨花谱、果谱、翎毛谱、兰谱、竹谱、梅谱、石谱 8 部分、每部分 40 幅图、配有文字而文图并茂，并萃集赵孟頫、沈周、文征明等前贤书画及胡正言与画友作品。按跨册更新新增赵农来源块，source_count 加 1、version 加 1，别名补“十竹斋书画谱”，日期顺延至 2027-04-26。",
     "04-knowledge/units/publications/shizhuzhai-huapu.md（更新）；新增引用 L7195、L7197，source_count 2→3，version 1→2。"),
]

REJECTS = [
    ("cand-10-50", "苏州网师园", None,
     "候选仅对应 L6855 图注“▲ 图 9-19 苏州网师园”，正文 L6834–L6865 市井段未给园名、布局、造园手法与年代；本章第五节 L7346–L7416 对江南园林有整段展开，届时按该段立条。本候选不另建条，避免以图注立目。",
     "判 rejected：仅图注，无正文材料。",
     "无 canonical；材料保留在来源层，园林实体留待第五节候选处理。"),
    ("cand-10-143", "罗汉床（清式变化）", None,
     "同批 cand-10-72 已据 L7025 建 canonical `04-knowledge/units/terms/luohan-chuang.md`，L7029 清式床足内翻蹄形与围屏小木料雕制拼装纹饰已并入该条；本候选与 canonical 同实体，若另建条将造成同一概念两目。",
     "判 rejected：与 cand-10-72 同实体，材料已并入 terms/luohan-chuang.md。",
     "无独立 canonical；内容归 terms/luohan-chuang.md。"),
    ("cand-10-112", "清末地方官书局", None,
     "既有 `04-knowledge/units/institutions/jinling-shuju.md` 已由 cand-10-148 据 L7221–L7227 建条，湖南思贤书局、浙江书局、成都存古书局亦分别由 cand-10-149/150/151 建条；L7221–L7227 材料已分见四局条目，且“地方官书局”作为通名无独立本体信息。本候选若建条将与四局条目重复。",
     "判 rejected：通名无独立本体，材料已分见金陵、思贤、浙江、存古四局条目。",
     "无 canonical；内容归四处官书局 KU。"),
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
    "scope_spans": [[6834, 7296]],
    "scope_note": "赵农 2009 册第九章第三节商业与民居、第四节文具与书籍正文 L6834–L7296 逐段复读，含市井广告、钱币与邮票、地域民居、明式与清式家具、文房四宝、明代与清代印刷、书籍装帧；候选 source_span 为块级粗跨度，实际引用行均落在本批范围内。图版未视觉核验。",
    "decisions": decisions,
    "notes": "赵农 2009 册第九章第三至第四节 unit 候选 57 条：create 53、update 1、rejected 3。范围 L6834-L7296。新建覆盖招牌、洋货、大明通行宝钞、大清宝钞、户部官票、龙洋、大龙邮票、刘铭传、四合院、窑洞、江南民居、马头墙、闽南土楼、一颗印、碉楼、蒙古包、山西四合院、官帽椅、玫瑰椅、架子床、罗汉床、拔步床、凳墩、清式榻、毗卢帽、龙墩、鹿角椅、安乐椅、湖笔、徽墨、洮砚、澄泥砚、西清砚谱、毛边纸、陈洪绶、古腾堡、永乐大典、朱载堉、十二平均律、乐律全书、永乐北藏、殿本、全唐诗、清代雕版插图、翟金生、武英殿聚珍版程式、南疆绎史勘本、朝报、毛装、函套、夹板、函盒、书箱。1 条更新为十竹斋画谱（跨册，source_count 2→3、version 1→2）；3 条 rejected（苏州网师园仅图注、罗汉床 L7029 与 cand-10-72 同实体、清末地方官书局与既有四局条目重复）。本批范围内 6 条 claim 候选仍保持 needs_evidence，未进入 claim-registry。",
}

out = ROOT / "_zn_decisions_ch9b.json"
out.write_text(json.dumps(cfg, ensure_ascii=False, indent=1) + "\n", encoding="utf-8", newline="\n")
print(Counter(d["action"] for d in decisions), len(decisions))
