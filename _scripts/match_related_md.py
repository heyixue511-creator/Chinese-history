# -*- coding: utf-8 -*-
"""把《相关研究书目清单.md》的 59 条匹配到知识库 01-基础文献 的 MD。

只输出候选，确认后写入 copy_related_md.py 的 MAP。
"""
import os
import re
import sys
import unicodedata
from difflib import SequenceMatcher

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from copy_related_bibliography import PLAN

KB = r"D:\Design-history-知识库\01-基础文献"
CAT = os.path.join(KB, "参考文献清单.md")


def norm(s):
    s = unicodedata.normalize("NFKC", s).lower()
    s = s.replace("&", "and")
    return "".join(ch for ch in s if ch.isalnum() or "\u4e00" <= ch <= "\u9fff")


def title_variants(t):
    t = re.sub(r"（[^）]*）|\([^)]*\)", "", t)
    out = {t}
    for sep in ("：", ":", "——", "—", "·"):
        if sep in t:
            out.add(t.split(sep)[0])
    return {norm(x) for x in out if len(norm(x)) >= 3}


def author_keys(a):
    a = re.sub(r"（[^）]*）|\([^)]*\)|主编|编|等", "", a)
    keys = []
    for p in re.split(r"[、,，;；/]", a):
        p = p.strip()
        if len(norm(p)) >= 2:
            keys.append(norm(p))
    return keys


def parse_catalog():
    txt = open(CAT, encoding="utf-8").read()
    out = []
    for blk in re.split(r"\n(?=\*\*[BP]\d{3}\*\*)", txt):
        m = re.match(r"\*\*([BP]\d{3})\*\*\s*(.*)", blk)
        if not m:
            continue
        pm = re.search(r"- 路径：`([^`]+)`", blk)
        if not pm:
            continue
        cit = m.group(2)
        seen = ""
        sm = re.search(r"- 核读所见：(.*)", blk)
        if sm:
            seen = sm.group(1)
        out.append(dict(id=m.group(1), cit=cit, path=pm.group(1),
                        text=norm(cit + " " + seen), raw=blk[:300]))
    return out


def main():
    entries = parse_catalog()
    for no, author, title, typ, _files, _note in PLAN:
        tv = title_variants(title)
        ak = author_keys(author)
        scored = []
        for e in entries:
            ts = 0.0
            for t in tv:
                if t and t in e["text"]:
                    ts = max(ts, 100 + len(t) / 100)
            if not ts:
                ts = 45 * max(SequenceMatcher(None, t, e["text"][:120]).ratio() for t in tv)
            a_s = 30 if any(k in e["text"] for k in ak) else 0
            scored.append((ts + a_s, e))
        scored.sort(key=lambda x: -x[0])
        top = scored[:2]
        print(f"\n### {no} {author}《{title}》")
        for sc, e in top:
            print(f"  {sc:6.1f} {e['id']} {e['path']}")
            print(f"        {e['cit'][:110]}")


if __name__ == "__main__":
    main()
