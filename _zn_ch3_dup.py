# -*- coding: utf-8 -*-
import io, json
from collections import Counter, defaultdict

files = ['_zn_decisions_ch3_core.json', '_zn_decisions_ch3_g1.json',
         '_zn_decisions_ch3_g2.json', '_zn_decisions_ch3_g3.json',
         '_zn_decisions_ch3_g4.json']
where = defaultdict(list)
for f in files:
    d = json.load(io.open(f, encoding='utf-8'))
    if isinstance(d, dict):
        d = d['decisions']
    for x in d:
        where[x['cid']].append(f)
dups = {k: v for k, v in where.items() if len(v) > 1}
print('dups:')
for k, v in dups.items():
    print(k, v)

view = set(l.split('\t')[0] for l in io.open('_zn_ch3_exist.txt', encoding='utf-8').read().splitlines())
print('view', len(view), 'decided', len(where))
print('in view not decided:')
for c in sorted(view - set(where)):
    r = None
    for line in io.open('06-runtime/state/candidate-index.jsonl', encoding='utf-8'):
        rr = json.loads(line)
        if rr['candidate_id'] == c:
            r = rr; break
    p = r['payload']
    print(c, p.get('title'), p.get('proposed_slug'), p.get('unit_type'), p.get('source_span', {}).get('line_start'))
print('decided not in view:')
for c in sorted(set(where) - view):
    print(c, where[c])
