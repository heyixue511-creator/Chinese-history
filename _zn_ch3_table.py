# -*- coding: utf-8 -*-
import io, json

d = json.load(io.open('_zn_decisions_ch3.json', encoding='utf-8'))['decisions']
idx = {}
for line in io.open('06-runtime/state/candidate-index.jsonl', encoding='utf-8'):
    r = json.loads(line)
    idx[r['candidate_id']] = r
rows = []
for x in d:
    sp = idx[x['cid']]['payload']['source_span']
    rows.append((int(sp['line_start']), x['cid'].split(':')[1], x['entity'], x['action'],
                 x['target'].replace('04-knowledge/units/', '')))
lines = ['| 候选 | 实体 | 动作 | 目标 |', '|---|---|---|---|']
for r in sorted(rows):
    lines.append('| %s | %s | %s | `%s` |' % (r[1], r[2], r[3], r[4]))
io.open('_zn_ch3_table.md', 'w', encoding='utf-8').write('\n'.join(lines) + '\n')
print('rows', len(rows))
