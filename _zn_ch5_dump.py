# -*- coding: utf-8 -*-
import io, json

DOC = '2009-zhaonong-zhongguo-yishu-shejishi'
CH = '第五章 丧乱的文明——三国两晋南北朝时期的设计'
rows = []
for line in io.open('06-runtime/state/candidate-index.jsonl', encoding='utf-8'):
    line = line.strip()
    if not line:
        continue
    r = json.loads(line)
    if not str(r.get('candidate_id', '')).startswith(DOC + ':'):
        continue
    if r.get('candidate_type') != 'unit':
        continue
    sp = r.get('payload', {}).get('source_span', {})
    if r.get('state') != 'needs_evidence':
        continue
    rows.append(r)
ch5 = [r for r in rows if r['payload']['source_span'].get('chapter') == CH]
ch5.sort(key=lambda r: (r['payload']['source_span']['line_start'], r['candidate_id']))
io.open('_zn_ch5_rows.json', 'w', encoding='utf-8').write(json.dumps(ch5, ensure_ascii=False, indent=1))
print('needs_evidence total:', len(rows))
print('ch5:', len(ch5))
from collections import Counter
print(Counter(r['payload'].get('unit_type') for r in ch5))
print(Counter(r['payload'].get('knowledge_match', {}).get('status') for r in ch5))
with io.open('_zn_ch5_list.txt', 'w', encoding='utf-8') as h:
    for r in ch5:
        p = r['payload']; s = p['source_span']
        h.write('=== %s | %s | %s | %s | L%s-L%s | km=%s\n' % (
            r['candidate_id'].split(':')[1], p.get('title'), p.get('unit_type'),
            p.get('proposed_slug'), s['line_start'], s['line_end'],
            p.get('knowledge_match', {}).get('status')))
        h.write('SUMMARY: %s\n' % (p.get('summary') or ''))
        km = p.get('knowledge_match', {})
        if km.get('target_refs'):
            h.write('TARGET_REFS: %s\n' % ', '.join(km['target_refs']))
        if km.get('notes'):
            h.write('KM_NOTES: %s\n' % km['notes'])
        if p.get('notes'):
            h.write('NOTES: %s\n' % p['notes'])
print('wrote _zn_ch5_list.txt')
