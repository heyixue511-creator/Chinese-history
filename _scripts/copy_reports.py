# -*- coding: utf-8 -*-
"""复制 02-文献解析/book-reports 的整本书分析报告到 02-分析报告。

用法：
    python copy_reports.py            # 预览
    python copy_reports.py --copy     # 复制
"""
import os
import shutil
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import copy_md as cm

SRC = r"D:\Design-history-知识库\02-文献解析\book-reports"
PAPER_SRC = r"D:\Design-history-知识库\02-文献解析\paper-reports"
DST = r"D:\中国设计史研究\02-分析报告"

FOLDER_OVERRIDE = {
    "B065": "马格林, 布坎南：《设计的观念：设计问题读本》，2018",
}


def report_folder(src_md):
    name = os.path.basename(src_md)
    if name.lower().endswith(".md"):
        name = name[:-3]
    for suf in ("_paged_clean", "_clean"):
        if name.endswith(suf):
            name = name[: -len(suf)]
    return name


def find_report(src_md):
    folder = report_folder(src_md)
    for base in (SRC, PAPER_SRC):
        p = os.path.join(base, folder)
        if os.path.isdir(p):
            return p, folder
    return None, folder


def main():
    cat = cm.parse_catalog()
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import build_base_library as b
    works = {w["ids"][0]: w for w in b.WORKS if not w.get("alias_of")}
    peri = {w["ids"][0]: w for w in b.PERIPHERAL}

    plan, peri_plan, problems = [], [], []
    for rid, kid in cm.MAP.items():
        src_md = cm.resolve(cat.get(kid, ""), rid)
        if not src_md:
            problems.append(f"{rid}: 源 MD 无法定位（{kid}）")
            continue
        src, folder = find_report(src_md)
        if not src:
            problems.append(f"{rid}: 报告目录不存在 {folder}")
            continue
        name = FOLDER_OVERRIDE.get(rid, folder)
        plan.append((rid, works[rid], src, name))

    for rid, kid in cm.PERI_MAP.items():
        src_md = cm.resolve(cat.get(kid, ""), rid)
        if not src_md:
            problems.append(f"{rid}: 外围源 MD 无法定位（{kid}）")
            continue
        src, folder = find_report(src_md)
        if not src:
            problems.append(f"{rid}: 外围报告目录不存在 {folder}")
            continue
        peri_plan.append((rid, peri[rid], src, folder))

    for rid, w, src, name in plan:
        n = sum(len(fs) for _dp, _dn, fs in os.walk(src))
        print(f"{rid}\t{w['title'][:32]:<32}\t{n:3d} files\t{name}")
    print(f"\n核心 {len(plan)} 种，外围 {len(peri_plan)} 种")
    for p in problems:
        print(" -", p)

    if "--copy" not in sys.argv:
        return
    os.makedirs(DST, exist_ok=True)
    legacy = os.path.join(DST, "00-外围参照")
    if os.path.isdir(legacy):
        shutil.rmtree(legacy)
    for rid, _w, src, name in plan:
        dst = os.path.join(DST, name)
        if os.path.isdir(dst):
            shutil.rmtree(dst)
        shutil.copytree(src, dst)
    for rid, _w, src, name in peri_plan:
        dst = os.path.join(DST, name)
        if os.path.isdir(dst):
            shutil.rmtree(dst)
        shutil.copytree(src, dst)
    # 总校验报告
    chk = os.path.join(SRC, "00_二次校验报告_2026-08.md")
    if os.path.exists(chk):
        shutil.copy2(chk, os.path.join(DST, "00_二次校验报告_2026-08.md"))
    print(f"Copied {len(plan)} + {len(peri_plan)} report folders into {DST}")

    # 索引
    import build_base_library as bb
    by_rid = {p[0]: p for p in plan}
    L = []
    L.append("# 分析报告对照索引")
    L.append("")
    L.append("**生成日期**：2026-10-22  ")
    L.append(f"**来源**：`{SRC}`（论文两篇取自 `{PAPER_SRC}`）  ")
    L.append("**每本书的目录内含**：`分析报告/`（含 `00_整体分析报告.md` 及各章报告）、`知识涌现分析/`；部分书另有根目录 `分析报告.md` 汇总本。  ")
    L.append(f"**结果**：94 种著作 {len(plan)} 种有报告；外围 9 种同置本目录，不计入 102。")
    L.append("")
    for sec in [bb.S1, bb.S2, bb.S3, bb.S4, bb.S5, bb.S6]:
        block = [by_rid[rid] for rid in by_rid if by_rid[rid][1]["sec"] == sec]
        if not block:
            continue
        L.append(f"## {bb.SEC_NAMES[sec]}")
        L.append("")
        L.append("| 编号 | 著者 | 著作 | 报告目录 | 知识库条目 |")
        L.append("| --- | --- | --- | --- | --- |")
        for rid, w, _src, name in block:
            L.append(f"| {rid} | {w['author']} | {w['title']} | `{name}` | {cm.MAP[rid]} |")
        L.append("")
    L.append("## 外围参照（不计入 102，同置本目录）")
    L.append("")
    L.append("| 编号 | 著者 | 著作 | 报告目录 | 知识库条目 |")
    L.append("| --- | --- | --- | --- | --- |")
    for rid, w, _src, name in peri_plan:
        L.append(f"| {rid} | {w['author']} | {w['title']} | `{name}` | {cm.PERI_MAP[rid]} |")
    L.append("")
    with open(os.path.join(DST, "00_分析报告对照索引.md"), "w", encoding="utf-8") as fh:
        fh.write("\n".join(L))
    print("Wrote 00_分析报告对照索引.md")


if __name__ == "__main__":
    main()
