# -*- coding: utf-8 -*-
"""把《中国设计史相关文献总汇.md》的 94 种著作匹配到知识库 01-基础文献/books 的 MD。

用法：
    python match_kb_md.py            # 预览匹配
    python match_kb_md.py --copy     # 复制到 01-文献md
"""
import csv
import os
import re
import shutil
import sys
import unicodedata
from difflib import SequenceMatcher

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build_base_library as b

KB = r"D:\Design-history-知识库\01-基础文献"
CAT = os.path.join(KB, "参考文献清单.md")
BOOKS = os.path.join(KB, "books")
DST = r"D:\中国设计史研究\01-文献md"


def norm(s):
    s = unicodedata.normalize("NFKC", s).lower()
    s = s.replace("&", "and")
    return "".join(ch for ch in s if ch.isalnum() or "\u4e00" <= ch <= "\u9fff")


def variants(title):
    out = {title}
    t = re.sub(r"（[^）]*）|\([^)]*\)", "", title)
    out.add(t)
    for sep in ["：", ":"]:
        if sep in t:
            out.add(t.split(sep)[0])
    # 去掉卷次、版次
    for s in list(out):
        out.add(re.sub(r"第[一二三四五六七八九十0-9]+[卷版]", "", s))
        out.add(re.sub(r"\b(vol\.?|volume)\s*\d+", "", s, flags=re.I))
    return {norm(x) for x in out if len(norm(x)) >= 3}


def parse_catalog():
    txt = open(CAT, encoding="utf-8").read()
    blocks = re.split(r"\n(?=\*\*B\d{3}\*\*)", txt)
    entries = []
    for blk in blocks:
        m = re.match(r"\*\*(B\d{3})\*\*\s*(.*)", blk)
        if not m:
            continue
        eid = m.group(1)
        cit = m.group(2)
        pm = re.search(r"- 路径：`([^`]+)`", blk)
        if not pm:
            continue
        path = pm.group(1)
        seen = ""
        sm = re.search(r"- 核读所见：(.*)", blk)
        if sm:
            seen = sm.group(1)
        entries.append(dict(id=eid, cit=cit, seen=seen, path=path,
                            text=norm(cit + " " + seen)))
    return entries


def author_keys(author):
    a = re.sub(r"（[^）]*）|\([^)]*\)", "", author)
    a = a.replace("（编）", "").replace("(eds.)", "")
    parts = re.split(r"[、,，;；&]| and ", a)
    keys = []
    for p in parts:
        p = p.strip()
        if not p:
            continue
        keys.append(norm(p))
        toks = p.replace(".", " ").split()
        if toks:
            keys.append(norm(toks[-1]))
    return [k for k in keys if len(k) >= 2]


def score_work(w, entries):
    tv = variants(w["title"])
    ak = author_keys(w["author"])
    yr = (w.get("year") or "").strip()
    scored = []
    for e in entries:
        text = e["text"]
        title_score = 0
        for t in tv:
            if t and t in text:
                title_score = max(title_score, 100 + len(t) / 100)
        if not title_score:
            title_score = 60 * max(SequenceMatcher(None, t, text).ratio() for t in tv)
        a_score = 40 if any(k in text for k in ak) else 0
        y_score = 8 if yr and yr in e["cit"] else 0
        total = title_score + a_score + y_score
        scored.append((total, e))
    scored.sort(key=lambda x: -x[0])
    return scored[:3]


def main():
    entries = parse_catalog()
    out = []
    used = {}
    for w in b.WORKS:
        if w.get("alias_of"):
            continue
        top = score_work(w, entries)
        best_score, best = top[0]
        second = top[1][0] if len(top) > 1 else 0
        print(f"{w['ids'][0]}\t{best_score:6.1f}\t{second:6.1f}\t{w['title'][:38]}\t{best['id']} {best['path'][:80]}")
        out.append(dict(rid=w["ids"][0], title=w["title"], author=w["author"],
                        score=best_score, second=second, kb=best["id"], path=best["path"]))
    with open(os.path.join(os.path.dirname(__file__), "md_match_preview.tsv"), "w",
              encoding="utf-8", newline="") as fh:
        wr = csv.DictWriter(fh, fieldnames=list(out[0]), delimiter="\t")
        wr.writeheader()
        wr.writerows(out)


if __name__ == "__main__":
    main()
