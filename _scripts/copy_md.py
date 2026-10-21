# -*- coding: utf-8 -*-
"""把 94 种基础文献复制为 MD：从 D:\\Design-history-知识库\\01-基础文献\\books 取件。

映射依据《参考文献清单.md》逐条核对后的书目对应关系（见 MAP）。
用法：
    python copy_md.py            # 预览
    python copy_md.py --copy     # 复制到 01-文献md
"""
import os
import re
import shutil
import sys

KB = r"D:\Design-history-知识库\01-基础文献"
CAT = os.path.join(KB, "参考文献清单.md")
DST = r"D:\中国设计史研究\01-文献md"

# 本库 ref_id -> 知识库清单 B 编号
MAP = {
    "B511": "B511", "B477": "B477", "B476": "B476", "B516": "B516", "B514": "B514",
    "B469": "B469", "B465": "B465", "B472": "B472", "B500": "B500", "B485": "B485",
    "B495": "B495", "B493": "B493", "B494": "B494", "B491": "B491", "B479": "B479",
    "B496": "B496", "B497": "B497", "B512": "B512", "B471": "B471", "B499": "B499",
    "B492": "B492", "B517": "B517", "B505": "B505",
    "B089": "B089", "B079": "B079", "B326": "B326",
    "B288": "B506", "B289": "B431", "B004": "B004", "B102": "B102", "B103": "B103",
    "B153": "B153", "B168": "B168", "B383": "B383", "B147": "B147", "B180": "B180",
    "B073": "B073", "B164": "B164", "B425": "B425", "B265": "B265",
    "B503": "B503", "B501": "B501", "B486": "B486", "B487": "B487", "B498": "B498",
    "B481": "B481", "B482": "B482", "B468": "B468", "B508": "B508", "B504": "B504",
    "B513": "B513", "B489": "B489", "B490": "B490",
    "B480": "B480", "B515": "B515", "B478": "B478", "B466": "B507", "B065": "B065",
    "B509": "B509", "B510": "B510", "B470": "B470", "B233": "B233", "B463": "B463",
    "B462": "B462",
    "B284": "B284", "B139": "B139", "B031": "B031", "B461": "B461", "B174": "B174",
    "B082": "B082", "B038": "B038", "B209": "B209", "B019": "B019", "B414": "B414",
    "B422": "B422", "B245": "B245",
    "B258": "B258", "B483": "B483", "B040": "B040", "B304": "B304", "B212": "B212",
    "B131": "B131", "B189": "B189", "B484": "B484",
    "B163": "B163", "B197": "B197", "B318": "B318", "B293": "B293", "B450": "B450",
    "B242": "B242", "B252": "B252", "B259": "B259",
    "P044": "P044", "P030": "P030",
}
PERI_MAP = {
    "W01": "B009", "W02": "B223", "W03": "B331", "W04": "B306", "W05": "B214",
    "W06": "B333", "W07": "B313", "W08": "B154", "W09": "B473",
}
# 特殊情况：源文件名与内容不符，复制时改用正名
RENAME = {
    "B065": "马格林, 布坎南：《设计的观念：设计问题读本》，2018.md",
}
# 清单中的路径含省略号或与实际文件名不符时，按实际文件改指
OVERRIDE_BASENAME = {
    "B168": "Giorgio Riello：《Cotton The Fabric That Made the Modern World》_clean.md",
    "B383": "S. J. Vainker：《Chinese pottery and porcelain from prehistory to the present》_clean.md",
    "B265": "Landsberger：《Chinese propaganda posters from revolution to modernization》.md",
    "B233": "Jonathan M. Woodham：《Dictionary of Modern Design》_clean.md",
    "B209": "Jeremy Prestholdt：《Domesticating the World African Consumerism and the Genealogies of Globalization》_clean.md",
    "B245": "Kajri Jain：《Gods in the Bazaar The Economies of Indian Calendar Art》.md",
    "B258": "Kenneth Pomeranz：《The Great Divergence China, Europe, and the Making of the Modern World Economy》_clean.md",
    "B212": "Joel Mokyr：《The lever of riches - technological creativity and economic progress (1990)》.md",
    "B163": "Gennifer Weisenfeld.：《Mavo Japanese Artists and the Avant-Garde, 1905-1931》.md",
    "B242": "Junichiro Tanizaki：《In Praise of Shadows》，1933_clean.md",
    "B252": "Kathryn B Hiesinger：《JAPANESE DESIGN A SURVEY SINCE 1950》.md",
    "B259": "Kenya Hara：《Designing Design》，2007.md",
    "W02": "John Pile, Judith Gura, Drew Plunkett：《A History of Interior Design, 5th Edition》，2023_clean.md",
    "W05": "Johanna Drucker, Emily McVarish：《Graphic Design History A Critical Guide》，2009_clean.md",
    "W06": "Parthasarathi, Prasannan：Why Europe Grew Rich and Asia Did Not：Global Economic Divergence, 1600-1850, 2011_clean.md",
}
NOTE = {
    "B065": "源文件名为 Carl DiSalvo《Adversarial Design》，经清单 B065 核读确认实为本书中译本",
    "B497": "知识库本为「第三章 设计方法论」节选，非全本",
    "B288": "知识库文件为 2015 年版中译（世界设计史1）",
    "B466": "知识库文件为 2015 年版中译（世界设计史2）",
    "B189": "知识库文件名作 Age of Revolution 1789-1848",
    "B462": "知识库本为 2004 年朱锷译本",
    "B505": "知识库本为同题论文（非专著），无出版项",
    "P044": "期刊论文（Feminist Theory, 2016），非专著",
    "P030": "文件名为 Towards a Critical Regionalism，正文实为 Six Points for an Architecture of Resistance（见清单 P030）",
}
MISSING = {}


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


def resolve(rel, rid):
    p = os.path.join(KB, rel.replace("/", os.sep))
    if os.path.exists(p):
        return p
    folder = os.path.dirname(p)
    if rid in OVERRIDE_BASENAME:
        q = os.path.join(folder, OVERRIDE_BASENAME[rid])
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
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import build_base_library as b
    works = {w["ids"][0]: w for w in b.WORKS if not w.get("alias_of")}
    peri = {w["ids"][0]: w for w in b.PERIPHERAL}

    plan, problems = [], []
    for rid, kid in MAP.items():
        w = works.get(rid)
        if not w:
            problems.append(f"{rid}: 不在 WORKS")
            continue
        rel = cat.get(kid)
        if not rel:
            problems.append(f"{rid}: 清单无 {kid}")
            continue
        src = resolve(rel, rid)
        if not src:
            problems.append(f"{rid}: 文件无法定位 {rel}")
            continue
        name = RENAME.get(rid, os.path.basename(src))
        plan.append((rid, w, src, name, NOTE.get(rid, "")))

    peri_plan = []
    for rid, kid in PERI_MAP.items():
        w = peri.get(rid)
        rel = cat.get(kid)
        if not w or not rel:
            problems.append(f"{rid}: 外围映射失败 {kid}")
            continue
        src = resolve(rel, rid)
        if not src:
            problems.append(f"{rid}: 外围文件无法定位 {rel}")
            continue
        peri_plan.append((rid, w, src, os.path.basename(src), ""))

    for rid, w, src, name, _ in plan:
        print(f"{rid}\t{w['title'][:36]:<36}\t{name}")
    print(f"\n核心 {len(plan)} 种，外围 {len(peri_plan)} 种，缺 MD {len(MISSING)} 种")
    for rid, why in MISSING.items():
        print(f"  缺: {rid} {why}")
    if problems:
        print("PROBLEMS:")
        for p in problems:
            print(" -", p)

    if "--copy" not in sys.argv:
        return
    os.makedirs(DST, exist_ok=True)
    legacy = os.path.join(DST, "00-外围参照")
    if os.path.isdir(legacy):
        shutil.rmtree(legacy)
    for rid, _w, src, name, _ in plan:
        shutil.copy2(src, os.path.join(DST, name))
    for rid, _w, src, name, _ in peri_plan:
        shutil.copy2(src, os.path.join(DST, name))
    print(f"Copied {len(plan)} + {len(peri_plan)} files into {DST}")

    # 索引
    import build_base_library as bb
    by_rid = {p[0]: p for p in plan}
    peri_by_rid = {p[0]: p for p in peri_plan}
    L = []
    L.append("# 文献 MD 对照索引")
    L.append("")
    L.append("**生成日期**：2026-10-22  ")
    L.append(f"**来源**：`{os.path.join(KB, 'books')}`（P044、P030 两篇取自 `{os.path.join(KB, 'papers')}`）；书目身份据同目录《参考文献清单.md》  ")
    L.append("**范围**：文档 102 个 ref_id 去重后的 94 种著作；8.2 外围参照 9 种同置本目录，不计入 102。  ")
    L.append(f"**结果**：94 种著作中 {len(plan)} 种有 MD，{len(MISSING)} 种无；外围 {len(peri_plan)} 种有 MD。")
    L.append("")
    for sec in [bb.S1, bb.S2, bb.S3, bb.S4, bb.S5, bb.S6]:
        block = [by_rid[rid] for rid in by_rid if by_rid[rid][1]["sec"] == sec]
        if not block:
            continue
        L.append(f"## {bb.SEC_NAMES[sec]}")
        L.append("")
        L.append("| 编号 | 著者 | 著作 | 年份 | MD 文件 | 知识库条目 | 备注 |")
        L.append("| --- | --- | --- | --- | --- | --- | --- |")
        for rid, w, _src, name, note in block:
            L.append(f"| {rid} | {w['author']} | {w['title']} | {w['year']} | `{name}` | {MAP[rid]} | {note} |")
        L.append("")
    L.append("## 外围参照（不计入 102，同置本目录）")
    L.append("")
    L.append("| 编号 | 著者 | 著作 | 年份 | MD 文件 | 知识库条目 |")
    L.append("| --- | --- | --- | --- | --- | --- |")
    for rid, w, _src, name, _note in peri_plan:
        L.append(f"| {rid} | {w['author']} | {w['title']} | {w['year']} | `{name}` | {PERI_MAP[rid]} |")
    L.append("")
    if MISSING:
        L.append("## 无 MD 的著作")
        L.append("")
        for rid, why in MISSING.items():
            w = works.get(rid, {})
            L.append(f"- **{rid}** {w.get('author', '')}《{w.get('title', '')}》——{why}")
        L.append("")
    with open(os.path.join(DST, "00_文献md对照索引.md"), "w", encoding="utf-8") as fh:
        fh.write("\n".join(L))
    print("Wrote 00_文献md对照索引.md")


if __name__ == "__main__":
    main()
