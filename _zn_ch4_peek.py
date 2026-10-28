# -*- coding: utf-8 -*-
import io, os, re, sys

paths = sys.argv[1:]
for p in paths:
    if not os.path.exists(p):
        print('MISSING', p); continue
    txt = io.open(p, encoding='utf-8').read()
    lines = txt.split('\n')
    fm = {}
    i = 0
    if lines and lines[0].strip() == '---':
        i = 1
        while i < len(lines) and lines[i].strip() != '---':
            if ':' in lines[i]:
                k, v = lines[i].split(':', 1)
                fm[k.strip()] = v.strip()
            i += 1
    print('='*70)
    print(p)
    for k in ('title','aliases','unit_type','dimensions','period','date'):
        if k in fm: print('  %s: %s' % (k, fm[k]))
    desc = ''
    m = re.search(r'## 描述\s*\n+(.+)', txt)
    if m: desc = m.group(1)[:300]
    print('  DESC:', desc)
