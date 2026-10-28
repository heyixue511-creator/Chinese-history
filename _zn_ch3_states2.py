# -*- coding: utf-8 -*-
import io, json
from collections import Counter

rows = [json.loads(l) for l in io.open('06-runtime/state/candidate-index.jsonl', encoding='utf-8')]
not_view = set(l.split(' | ')[0] for l in io.open('_zn_ch3_not_view.txt', encoding='utf-8').read().splitlines())
# not_view doesn't include cid; rebuild from diff instead
ch3 = [r for r in rows if r['candidate_id'].startswith('2009-zhaonong')
       and r.get('candidate_type') == 'unit'
       and ((r['payload'].get('source_span') or {}).get('chapter') or '').startswith('第三章')]
view = set(l.split('\t')[0] for l in io.open('_zn_ch3_exist.txt', encoding='utf-8').read().splitlines())
excluded = [r for r in ch3 if r['candidate_id'] not in view]
print('excluded', len(excluded))
c = Counter(r.get('state') for r in excluded)
print(c)
lines = []
for r in excluded:
    p = r['payload']; sp = p.get('source_span') or {}
    lines.append('%s | %s | %s | %s | L%s-L%s' % (r['candidate_id'].split(':')[1], p.get('title'), p.get('unit_type'), r.get('state'), sp.get('line_start'), sp.get('line_end')))
io.open('_zn_ch3_excluded_states.txt', 'w', encoding='utf-8').write('\n'.join(lines))
