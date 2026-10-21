# -*- coding: utf-8 -*-
"""按《相关研究书目清单.md》只复制知识库 02-文献解析 中每本书的「分析报告」子文件夹。

用法：
    python copy_related_reports.py            # 预览
    python copy_related_reports.py --copy     # 复制并写索引
"""
import os
import shutil
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import copy_related_md as cm

ROOT = r"D:\中国设计史研究"
SRC = r"D:\Design-history-知识库\02-文献解析\book-reports"
DST = os.path.join(ROOT, "分析报告")
LIST_MD = os.path.join(ROOT, "相关研究书目清单.md")


def report_folder(src_md):
    name = os.path.basename(src_md)
    if name.lower().endswith(".md"):
        name = name[:-3]
    for suf in ("_paged_clean", "_clean"):
        if name.endswith(suf):
            name = name[: -len(suf)]
    return name


def main():
    cat = cm.parse_catalog()
    plan, problems = [], []
    for no, kid, dest, note in cm.MAP:
        rel = cat.get(kid)
        src_md = cm.resolve(rel, kid) if rel else None
        if not src_md:
            problems.append(f"{no}: 源 MD 无法定位（{kid}）")
            continue
        folder = report_folder(src_md)
        rep = os.path.join(SRC, folder, "分析报告")
        if not os.path.isdir(rep):
            problems.append(f"{no}: 分析报告目录不存在 {folder}")
            continue
        n = sum(len(fs) for _dp, _dn, fs in os.walk(rep))
        plan.append((no, kid, folder, rep, note, n))

    for no, kid, folder, rep, note, n in plan:
        print(f"{no}\t{kid}\t{n:3d} files\t{folder}")
    print(f"\n条目 {len({p[0] for p in plan})}；分析报告文件夹 {len(plan)}；文件 {sum(p[5] for p in plan)}")
    for p in problems:
        print(" -", p)
    if problems:
        return

    if "--copy" not in sys.argv:
        return
    os.makedirs(DST, exist_ok=True)
    for _no, _kid, folder, rep, _note, _n in plan:
        dst = os.path.join(DST, folder)
        if os.path.isdir(dst):
            shutil.rmtree(dst)
        shutil.copytree(rep, dst)
    print(f"Copied {len(plan)} 分析报告 folders into {DST}")

    by_no = {}
    for no, kid, folder, _rep, note, n in plan:
        by_no.setdefault(no, []).append((kid, folder, note, n))

    L = []
    L.append("# 相关研究书目分析报告对照索引")
    L.append("")
    L.append("**生成日期**：2026-10-22  ")
    L.append(f"**清单**：`{LIST_MD}`（59 条）  ")
    L.append(f"**来源**：`{SRC}`（每本书只取 `分析报告/` 子文件夹，不含 `知识涌现分析/` 与根目录 `分析报告.md`）  ")
    L.append("**结果**：38 条有对应分析报告（40 个文件夹）；18 条未检出；3 条为会议／网页／课程资料，无分析报告。  ")
    L.append("**目录**：`分析报告/<书名>/` 内为该书的 `00_整体分析报告.md`、分章报告与专项索引。  ")
    L.append("")
    for g in ("1", "2", "3", "4"):
        L.append(f"## {cm.GROUPS[g]}")
        L.append("")
        L.append("| 序号 | 作者 | 书名／题名 | 状态 | 报告文件夹 | 知识库条目 | 文件数 | 备注 |")
        L.append("| --- | --- | --- | --- | --- | --- | --- | --- |")
        missing_by_no = {row[0]: row for row in cm.MISSING}
        order = sorted(set([k for k in by_no if k.startswith(g + "-")] +
                           [k for k in missing_by_no if k.startswith(g + "-")]))
        for no in order:
            if no in missing_by_no:
                _no, author, title, typ, note = missing_by_no[no]
                status = "非MD资料" if typ in ("会议", "网页", "课程资料") else "未检出"
                L.append(f"| {no} | {author} | {title} | {status} | — | — | 0 | {note} |")
            else:
                author, title = cm.title_of(no)
                for kid, folder, note, n in by_no[no]:
                    L.append(f"| {no} | {author} | {title} | 已复制 | `{folder}` | {kid} | {n} | {note} |")
        L.append("")
    L.append("## 未检出条目（18 条）")
    L.append("")
    L.append("以下条目在知识库 `02-文献解析/book-reports` 中无对应分析报告：")
    L.append("")
    for no, author, title, typ, note in cm.MISSING:
        if typ not in ("会议", "网页", "课程资料"):
            L.append(f"- **{no}** {author}《{title}》——{note}")
    L.append("")
    with open(os.path.join(DST, "00_书目清单分析报告对照索引.md"), "w", encoding="utf-8") as fh:
        fh.write("\n".join(L))
    print("Wrote 00_书目清单分析报告对照索引.md")


if __name__ == "__main__":
    main()
