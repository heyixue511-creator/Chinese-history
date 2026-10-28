# -*- coding: utf-8 -*-
import json
import re

cfg = json.load(open('_zn_decisions_ch9a.json', encoding='utf-8'))
for d in cfg['decisions']:
    if d['action'] == 'rejected':
        continue
    t = open(d['target'], encoding='utf-8').read()
    fm = t.split('---')[1]
    title = re.search(r'^title: (.+)$', fm, re.M).group(1)
    dim = re.search(r'^primary_dimension: (\w+)', fm, re.M).group(1)
    conf = re.search(r'^confidence: (\w+)', fm, re.M).group(1)
    secs = len(re.findall(r'^## ', t, re.M))
    scope = re.search(r'^hierarchy_scope_note: "?(.+?)"?$', fm, re.M).group(1)
    print(d['action'][:3], title, dim, conf, 'secs=%d' % secs, scope[:50], sep=' | ')
