# -*- coding: utf-8 -*-
import io, json, collections

DOC = '2009-zhaonong-zhongguo-yishu-shejishi'
rows = []
for line in io.open('06-runtime/state/candidate-index.jsonl', encoding='utf-8'):
    line = line.strip()
    if not line:
        continue
    r = json.loads(line)
    if not str(r.get('candidate_id','')).startswith(DOC + ':'):
        continue
    rows.append(r)
kinds = collections.Counter(r.get('candidate_type') for r in rows)
print('total:', len(rows), 'kinds:', dict(kinds))
units = [r for r in rows if r.get('candidate_type') == 'unit']
print('unit total:', len(units))
ch = collections.Counter()
st = collections.defaultdict(collections.Counter)
for r in units:
    c = r.get('payload',{}).get('source_span',{}).get('chapter')
    ch[c] += 1
    st[c][r.get('state')] += 1
for c in sorted(ch, key=lambda x: (x is None, str(x))):
    print(repr(c), ch[c], dict(st[c]))
