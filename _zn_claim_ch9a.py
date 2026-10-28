# -*- coding: utf-8 -*-
import json

n = 0
for line in open('06-runtime/state/candidate-index.jsonl', encoding='utf-8'):
    r = json.loads(line)
    s = r.get('payload', {}).get('source_span') or {}
    ls = s.get('line_start')
    if r.get('payload', {}).get('candidate_type') == 'claim' and isinstance(ls, int) and 6599 <= ls <= 6833:
        n += 1
print('claims in scope:', n)
