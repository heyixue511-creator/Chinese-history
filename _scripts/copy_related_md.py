# -*- coding: utf-8 -*-
"""按《相关研究书目清单.md》从知识库 01-基础文献 取 MD，复制到 md。

用法：
    python copy_related_md.py            # 预览
    python copy_related_md.py --copy     # 复制并写索引
"""
import os
import re
import shutil
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

ROOT = r"D:\中国设计史研究"
KB = r"D:\Design-history-知识库\01-基础文献"
CAT = os.path.join(KB, "参考文献清单.md")
DST = os.path.join(ROOT, "md")
LIST_MD = os.path.join(ROOT, "相关研究书目清单.md")

# 清单路径含省略号，按实际文件名改指
OVERRIDE = {
    "B168": "Giorgio Riello：《Cotton The Fabric That Made the Modern World》_clean.md",
    "B258": "Kenneth Pomeranz：《The Great Divergence China, Europe, and the Making of the Modern World Economy》_clean.md",
    "B242": "Junichiro Tanizaki：《In Praise of Shadows》，1933_clean.md",
}

# (序号, 知识库编号, 目标文件名, 备注)
MAP = [
    ("1-01", "B511", "赵农_中国艺术设计史_2004.md", "D盘MD为2004年版；清单称多个版次"),
    ("1-02", "B477", "夏燕靖_中国艺术设计史_2010.md", "清单作2001年辽宁美术初版；知识库仅见2010年南京师大版"),
    ("1-03", "B476", "夏燕靖_中国艺术设计史（升级版）_2016.md", ""),
    ("1-07", "B500", "沈榆_观念的演进_2021.md", ""),
    ("1-08", "B485", "曹小鸥_中国现代设计思想_2018.md", ""),
    ("1-09", "B472", "周博_断裂与绵延_2023.md", ""),
    ("1-10", "B493", "杭间_中国工艺美学史（第三版修订本）_2018.md", "第三版修订本"),
    ("1-11", "B495", "杭间_设计道_2008.md", ""),
    ("1-12", "B494", "杭间_手艺的思想（修订版）_2017.md", "修订版"),
    ("1-13", "B491", "李砚祖_造物之美_2000.md", ""),
    ("1-14", "B496", "柳冠中_事理学方法论_2019.md", ""),
    ("1-15", "B497", "柳冠中_设计方法论.md", "知识库本为「第三章 设计方法论」节选，非全本"),
    ("2-10", "B473", "周博_现代设计伦理思想史.md", ""),
    ("3-01", "B471", "周博_中国现代文字设计图史_2018.md", "按清单更正为2018年；库内文件名原标2017"),
    ("3-04", "B517", "靳埭强等_中国现代设计与包豪斯_2013.md", ""),
    ("3-05", "B492", "杭间等_包豪斯道路_2014.md", "杭间、靳埭强、胡恩威主编"),
    ("3-06", "B501", "王受之_世界平面设计史_2002.md", ""),
    ("3-07", "B514", "邹德侬等_中国现代建筑史_2010.md", ""),
    ("3-08", "B516", "霍维国等_中国室内设计史（第2版）_2007.md", "第2版"),
    ("3-09", "B499", "樊进等_中国当代设计全集第4卷_2015.md", "第4卷 平面类编 图案篇"),
    ("4-01", "B480", "佩夫斯纳_现代设计的先驱者_2019.md", "中译本"),
    ("4-02", "B503", "王受之_世界现代设计史（第2版）_2015.md", "第2版"),
    ("4-03", "B486", "朱和平_世界现代设计史_2013.md", ""),
    ("4-04", "B487", "朱和平_现代设计史（五南版）_2012.md", "五南版"),
    ("4-05", "B498", "梁梅_世界现代设计史_2013.md", ""),
    ("4-06", "B478", "瑞兹曼_现代设计史（第2版）_2013.md", "中译本第2版"),
    ("4-06", "B102", "Raizman_History of Modern Design_3rd_2023.md", "英文第3版"),
    ("4-07", "B506", "马格林_世界设计史（第1卷）_2020.md", "第1卷中译本"),
    ("4-07", "B507", "马格林_世界设计史（第2卷）_2015.md", "第2卷中译本"),
    ("4-08", "B515", "福蒂_欲求之物_2001.md", "中译本"),
    ("4-09", "B509", "斯帕克_唯有粉红_2018.md", "中译本"),
    ("4-10", "B318", "Yanagi_The Unknown Craftsman.md", "仅有英译本；中译本未检出"),
    ("4-11", "B242", "Tanizaki_In Praise of Shadows.md", "仅有英文版；中译本未检出"),
    ("4-12", "B131", "Berg_The Age of Manufactures 1700-1820.md", "英文版"),
    ("4-13", "B304", "Berg_Luxury and Pleasure_2007.md", "英文版"),
    ("4-14", "B168", "Riello_Cotton_2013.md", "英文版"),
    ("4-15", "B040", "Beckert_Empire of Cotton_2014.md", "英文版"),
    ("4-16", "B258", "Pomeranz_The Great Divergence.md", "仅有英文版；中译本未检出"),
    ("4-17", "B004", "Adamson et al_Global Design History_2011.md", "英文版"),
    ("4-18", "B089", "Clunas_Superfluous Things_1991.md", "英文版"),
]

GROUPS = {
    "1": "一、分析样本：中国设计通史与观念史",
    "2": "二、设计史学史与方法论研究",
    "3": "三、专门史：节点检验的材料来源",
    "4": "四、世界与全球设计史参照",
}

# 清单全部 59 条中无 MD 的条目：(序号, 作者, 题名, 类型)
MISSING = [
    ("1-04", "夏燕靖", "中国艺术设计史（增补版）", "专著", "2021年上海人民美术出版社，知识库未检出"),
    ("1-05", "夏燕靖", "中国艺术设计史（第3版）", "专著", "2024年南京师范大学出版社，知识库未检出"),
    ("1-06", "沈榆", "中国现代设计观念史", "专著", "2017年版，知识库未检出（仅有2021年修订版）"),
    ("2-01", "祝帅", "中国设计研究百年", "专著", "知识库未检出"),
    ("2-02", "杭间", "中国设计史构建的反思", "论文", "全文待取得，知识库未检出"),
    ("2-03", "杭间", "“设计史”的本质——从工具理性到“日常生活的审美化”", "论文", "知识库未检出"),
    ("2-04", "李立新", "设计史的历史叙事、文本书写与史学理论问题", "论文", "知识库未检出"),
    ("2-05", "李立新", "设计史研究的方法论转向——去田野中寻找生活的设计历史", "论文", "知识库未检出"),
    ("2-06", "黄厚石", "日常生活设计研究的意义", "论文", "知识库未检出"),
    ("2-07", "（作者待核）", "设计史叙事模式的研究现状述评", "论文", "知识库未检出"),
    ("2-08", "（作者待核）", "作为一种史学范式的“新中国设计史”——中国设计史研究分期问题再讨论", "论文", "知识库未检出"),
    ("2-09", "（作者待核）", "基于知识图谱的中国设计学研究主题可视化分析", "论文", "全文待取得，知识库未检出"),
    ("2-11", "周博", "人道的栖居：中国当代设计批评", "专著", "知识库未检出"),
    ("2-12", "袁宣萍 主编", "中国近现代设计史论丛", "论文集", "知识库未检出"),
    ("2-13", "北京大学艺术学院", "“三大体系”建设与《中国设计通史》写作学术论坛", "会议", "会议资料，非MD"),
    ("3-02", "周博 主编", "字体摩登：字体书和中国现代文字设计的再发现（1919-1955）", "专著", "知识库未检出"),
    ("3-03", "陈楠", "中国汉字设计史", "专著", "知识库未检出"),
    ("3-10", "周博", "改革开放以来的视觉传达设计：媒介转型与社会变迁", "论文", "知识库未检出"),
    ("3-11", "沈榆", "从设计中见证生活发展——评《共和国100个经典民生设计》", "书评", "知识库未检出"),
    ("3-12", "方正字库", "“641体”与方正报宋承续关系官方说明", "网页", "网页资料，非MD"),
    ("3-13", "清华大学美术学院", "综合造型设计基础课程资料（1984年开设）", "课程资料", "课程资料，非MD"),
]


def parse_catalog():
    txt = open(CAT, encoding="utf-8").read()
    out = {}
    for blk in re.split(r"\n(?=\*\*[BP]\d{3}\*\*)", txt):
        m = re.match(r"\*\*([BP]\d{3})\*\*", blk)
        if not m:
            continue
        pm = re.search(r"- 路径：`([^`]+)`", blk)
        if pm:
            out[m.group(1)] = pm.group(1)
    return out


def resolve(rel, kid):
    p = os.path.join(KB, rel.replace("/", os.sep))
    if os.path.exists(p):
        return p
    folder = os.path.dirname(p)
    if kid in OVERRIDE:
        q = os.path.join(folder, OVERRIDE[kid])
        return q if os.path.exists(q) else None
    bn = os.path.basename(rel)
    if "…" in bn:
        pre, suf = bn.split("…", 1)
        cand = [f for f in os.listdir(folder) if f.startswith(pre) and f.endswith(suf)]
        if len(cand) == 1:
            return os.path.join(folder, cand[0])
    return None


def main():
    cat = parse_catalog()
    plan, problems = [], []
    for no, kid, dest, note in MAP:
        rel = cat.get(kid)
        if not rel:
            problems.append(f"{no}: 清单无 {kid}")
            continue
        src = resolve(rel, kid)
        if not src:
            problems.append(f"{no}: 文件无法定位 {rel}")
            continue
        plan.append((no, kid, src, dest, note))

    total = 0
    for no, kid, src, dest, note in plan:
        size = os.path.getsize(src)
        total += size
        print(f"{no}\t{kid}\t{size:>9d}\t{dest}")
    for no, _a, _t, _ty, _n in MISSING:
        print(f"{no}\t未检出")
    print(f"\n条目 59；有 MD {len({p[0] for p in plan})}；文件 {len(plan)}；"
          f"合计 {total / 1024 / 1024:.1f} MB")
    for p in problems:
        print(" -", p)
    if problems:
        return

    if "--copy" not in sys.argv:
        return
    os.makedirs(DST, exist_ok=True)
    for _no, _kid, src, dest, _note in plan:
        shutil.copy2(src, os.path.join(DST, dest))
    print(f"Copied into {DST}")

    by_no = {}
    for no, kid, _src, dest, note in plan:
        by_no.setdefault(no, []).append((kid, dest, note))

    L = []
    L.append("# 相关研究书目 MD 对照索引")
    L.append("")
    L.append("**生成日期**：2026-10-22  ")
    L.append(f"**清单**：`{LIST_MD}`（59 条）  ")
    L.append(f"**来源**：`{KB}` 的 `books/`（书目身份据同目录《参考文献清单.md》）  ")
    L.append("**结果**：38 条有对应 MD（40 个文件）；18 条未检出 MD；3 条为会议／网页／课程资料，无 MD。  ")
    L.append("**命名**：与 `基础文献/` 中的 PDF 同名（仅扩展名不同），便于对照。  ")
    L.append("")
    for g in ("1", "2", "3", "4"):
        L.append(f"## {GROUPS[g]}")
        L.append("")
        L.append("| 序号 | 作者 | 书名／题名 | 状态 | MD 文件 | 知识库条目 | 备注 |")
        L.append("| --- | --- | --- | --- | --- | --- | --- |")
        missing_by_no = {row[0]: row for row in MISSING}
        order = sorted(set([k for k in by_no if k.startswith(g + "-")] +
                           [k for k in missing_by_no if k.startswith(g + "-")]))
        for no in order:
            if no in missing_by_no:
                _no, author, title, typ, note = missing_by_no[no]
                status = "非MD资料" if typ in ("会议", "网页", "课程资料") else "未检出"
                L.append(f"| {no} | {author} | {title} | {status} | — | — | {note} |")
            else:
                author, title = title_of(no)
                for kid, dest, note in by_no[no]:
                    L.append(f"| {no} | {author} | {title} | 已复制 | `{dest}` | {kid} | {note} |")
        L.append("")
    L.append("## 未检出条目（18 条）")
    L.append("")
    L.append("以下条目在知识库 `books/`、`papers/` 中无对应 MD，须另行取得：")
    L.append("")
    for no, author, title, typ, note in MISSING:
        if typ not in ("会议", "网页", "课程资料"):
            L.append(f"- **{no}** {author}《{title}》——{note}")
    L.append("")
    with open(os.path.join(DST, "00_书目清单MD对照索引.md"), "w", encoding="utf-8") as fh:
        fh.write("\n".join(L))
    print("Wrote 00_书目清单MD对照索引.md")


def missing_rows(g):
    for row in MISSING:
        if row[0].startswith(g + "-"):
            yield row


def title_of(no):
    from copy_related_bibliography import PLAN
    for p in PLAN:
        if p[0] == no:
            return p[1], p[2]
    return "", ""


if __name__ == "__main__":
    main()
