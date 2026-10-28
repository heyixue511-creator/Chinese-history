# -*- coding: utf-8 -*-
import io, json

rows = [json.loads(l) for l in io.open('06-runtime/state/candidate-index.jsonl', encoding='utf-8')]
ch3 = []
for r in rows:
    if not r['candidate_id'].startswith('2009-zhaonong'):
        continue
    p = r['payload']
    sp = p.get('source_span') or {}
    ch = sp.get('chapter') or ''
    if ch.startswith('第三章') and r.get('candidate_type') == 'unit':
        ch3.append(r)
print('ch3 unit total', len(ch3))

assigned = {}
for f in ['_zn_decisions_ch3_core.json', '_zn_decisions_ch3_g1.json', '_zn_decisions_ch3_g2.json', '_zn_decisions_ch3_g4.json']:
    d = json.load(io.open(f, encoding='utf-8'))
    if isinstance(d, dict):
        d = d['decisions']
    for x in d:
        assigned[x['cid']] = (f, x['action'], x['target'])

print('assigned', len(assigned))
out = []
for r in ch3:
    if r['candidate_id'] not in assigned:
        p = r['payload']
        out.append(json.dumps({'cid': r['candidate_id'], 'title': p.get('title'),
                               'slug': p.get('proposed_slug'), 'type': p.get('unit_type'),
                               'span': p.get('source_span')}, ensure_ascii=False))
io.open('_zn_ch3_unassigned.txt', 'w', encoding='utf-8').write('\n'.join(out))
print('unassigned', len(out))

# also check duplicates in assigned across files
from collections import Counter
c = Counter()
for f in ['_zn_decisions_ch3_core.json', '_zn_decisions_ch3_g1.json', '_zn_decisions_ch3_g2.json', '_zn_decisions_ch3_g4.json']:
    d = json.load(io.open(f, encoding='utf-8'))
    if isinstance(d, dict):
        d = d['decisions']
    for x in d:
        c[x['cid']] += 1
dups = [k for k, v in c.items() if v > 1]
print('dups', dups)
