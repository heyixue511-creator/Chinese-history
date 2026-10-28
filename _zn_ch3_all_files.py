# -*- coding: utf-8 -*-
import io, json

d = json.load(io.open('_zn_decisions_ch3.json', encoding='utf-8'))['decisions']
allf, creates = [], []
for x in d:
    if x['action'] in ('create', 'update'):
        allf.append(x['target'])
        if x['action'] == 'create':
            creates.append(x['target'])
io.open('_zn_ch3_all_targets.txt', 'w', encoding='utf-8').write('\n'.join(allf) + '\n')
io.open('_zn_ch3_creates.txt', 'w', encoding='utf-8').write('\n'.join(creates) + '\n')
print(len(allf), len(creates))
