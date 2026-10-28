# -*- coding: utf-8 -*-
import io, json

files = ['_zn_decisions_ch3_core.json', '_zn_decisions_ch3_g1.json',
         '_zn_decisions_ch3_g2.json', '_zn_decisions_ch3_g3.json',
         '_zn_decisions_ch3_g4.json']
cids = []
for f in files:
    d = json.load(io.open(f, encoding='utf-8'))
    if isinstance(d, dict):
        d = d['decisions']
    for x in d:
        cids.append(x['cid'])
print('decisions', len(cids), 'unique', len(set(cids)))

idx = {}
for line in io.open('06-runtime/state/candidate-index.jsonl', encoding='utf-8'):
    r = json.loads(line)
    idx[r['candidate_id']] = r

spans = []
missing = []
for c in cids:
    if c not in idx:
        missing.append(c)
        continue
    sp = idx[c]['payload']['source_span']
    spans.append((int(sp['line_start']), int(sp['line_end'])))
print('missing', missing)
spans.sort()
merged = []
for s, e in spans:
    if merged and s <= merged[-1][1] + 1:
        merged[-1][1] = max(merged[-1][1], e)
    else:
        merged.append([s, e])
print('merged', merged)
print('covered', sum(e - s + 1 for s, e in merged))
print('min', min(s for s, e in spans), 'max', max(e for s, e in spans))
