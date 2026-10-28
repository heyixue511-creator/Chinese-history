# -*- coding: utf-8 -*-
import io, json, glob, os
from collections import Counter

rows = [json.loads(l) for l in io.open('06-runtime/state/candidate-index.jsonl', encoding='utf-8')]
cnt = Counter()
for r in rows:
    if not r['candidate_id'].startswith('2009-zhaonong'):
        continue
    if r.get('candidate_type') != 'unit':
        continue
    p = r['payload']; sp = p.get('source_span') or {}
    cnt[sp.get('chapter') or '(none)'] += 1
for k, v in cnt.items():
    print(v, k)

print('--- ledger files ---')
for f in sorted(glob.glob('06-runtime/automation/*zhaonong*/*.jsonl')):
    n = sum(1 for _ in io.open(f, encoding='utf-8'))
    print(n, os.path.basename(os.path.dirname(f)), os.path.basename(f))
