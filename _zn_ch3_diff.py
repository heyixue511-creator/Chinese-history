# -*- coding: utf-8 -*-
import io, json

rows = [json.loads(l) for l in io.open('06-runtime/state/candidate-index.jsonl', encoding='utf-8')]
by_id = {r['candidate_id']: r for r in rows}
view = [l.split('\t')[0] for l in io.open('_zn_ch3_view.txt', encoding='utf-8').read().splitlines()]
viewset = set(view)

ch3 = [r for r in rows if r['candidate_id'].startswith('2009-zhaonong')
       and r.get('candidate_type') == 'unit'
       and ((r['payload'].get('source_span') or {}).get('chapter') or '').startswith('第三章')]
print('view', len(view), 'ch3 units', len(ch3))

in_view = [r for r in ch3 if r['candidate_id'] in viewset]
not_view = [r for r in ch3 if r['candidate_id'] not in viewset]
print('in view', len(in_view), 'not in view', len(not_view))

def describe(r):
    p = r['payload']; sp = p.get('source_span') or {}
    return '%s | %s | %s | L%s-L%s | %s' % (r['candidate_id'].split(':')[1], p.get('title'), p.get('unit_type'), sp.get('line_start'), sp.get('line_end'), sp.get('section'))

lines = []
for r in not_view:
    lines.append(describe(r))
io.open('_zn_ch3_not_view.txt', 'w', encoding='utf-8').write('\n'.join(lines))
print('\n'.join(lines[:15]))
