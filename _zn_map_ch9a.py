# -*- coding: utf-8 -*-
import json

cfg = json.load(open('_zn_decisions_ch9a.json', encoding='utf-8'))
ids = {d['cid']: d for d in cfg['decisions']}
for line in open('06-runtime/state/candidate-index.jsonl', encoding='utf-8'):
    r = json.loads(line)
    if r['candidate_id'] in ids:
        d = ids[r['candidate_id']]
        s = r.get('payload', {}).get('source_span', {})
        print(r['candidate_id'].split(':')[1], d['action'][:4], s.get('line_start'), s.get('section'), d['entity'])
