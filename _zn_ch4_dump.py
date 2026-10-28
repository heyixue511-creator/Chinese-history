# -*- coding: utf-8 -*-
import io, json

DOC = '2009-zhaonong-zhongguo-yishu-shejishi'
CH = '第四章 统一的气量——秦汉时期的设计'
out = []
for line in io.open('06-runtime/state/candidate-index.jsonl', encoding='utf-8'):
    line = line.strip()
    if not line:
        continue
    r = json.loads(line)
    if not str(r.get('candidate_id','')).startswith(DOC + ':'):
        continue
    if r.get('candidate_type') != 'unit':
        continue
    sp = r.get('payload',{}).get('source_span',{})
    if r.get('state') != 'needs_evidence':
        continue
    out.append(r)
print('needs_evidence total:', len(out))
ch4 = [r for r in out if r['payload']['source_span'].get('chapter') == CH]
print('ch4:', len(ch4))
ch4.sort(key=lambda r: (r['payload']['source_span']['line_start'], r['candidate_id']))
prev_ch = None
for r in out:
    if r['payload']['source_span'].get('chapter') != CH:
        pass
io.open('_zn_ch4_rows.json','w',encoding='utf-8').write(json.dumps(ch4,ensure_ascii=False,indent=1))
for r in ch4:
    p = r['payload']; s = p['source_span']
    t = p.get('title')
    print('%-14s %-8s %-5s L%-5s-%-5s %s' % (r['candidate_id'].split(':')[1], p.get('unit_type'), p.get('proposed_slug'), s['line_start'], s['line_end'], t))
