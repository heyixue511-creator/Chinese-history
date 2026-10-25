import json, hashlib, sys, collections
from pathlib import Path
pkg = Path(sys.argv[1])
p = Path('06-runtime/state/candidate-index.jsonl'); t = p.read_text(encoding='utf-8').replace('\r\n', '\n')
b = t.encode()
rows = [json.loads(l) for l in t.split('\n') if l.strip()]
out = {'sha256': 'sha256:' + hashlib.sha256(b).hexdigest(), 'bytes': len(b), 'lines': t.count('\n'),
       'states': dict(collections.Counter(r['state'] for r in rows)),
       'lifecycle': dict(collections.Counter(r.get('lifecycle_class') for r in rows))}
plan = [json.loads(l) for l in open(pkg / 'apply-plan.jsonl', encoding='utf-8') if l.strip()]
ok = 0; bad = []
for r in plan:
    t2 = Path(r['target_ref']).read_text(encoding='utf-8').replace('\r\n', '\n')
    if 'sha256:' + hashlib.sha256(t2.encode()).hexdigest() == r['after_sha256'] and len(t2.encode()) == r['bytes'] and t2.count('\n') == r['lines']:
        ok += 1
    else:
        bad.append(r['target_ref'])
out['plan'] = {'rows': len(plan), 'ok': ok, 'bad': bad}
gs = [json.loads(l) for l in open('06-runtime/automation/2026-10-25-cross-source-candidate-consolidation/duplicate-groups.jsonl', encoding='utf-8') if l.strip()]
idx = {r['candidate_id']: r for r in rows}
TERM = {'applied', 'rejected', 'no_delta'}
sel = [g for g in gs if g['unit_type'] == 'term' and g['doc_count'] == 2]
closed = [g for g in sel if all(idx[m['candidate_id']]['state'] in TERM for m in g['members'])]
opn = [g for g in sel if g not in closed]
out['term_doc2'] = {'total': len(sel), 'closed': len(closed), 'open': len(opn),
                    'open_members': sum(1 for g in opn for m in g['members'] if idx[m['candidate_id']]['state'] not in TERM)}
per = [g for g in gs if g['unit_type'] == 'person' and g['doc_count'] == 2]
out['person_doc2'] = {'total': len(per), 'open': sum(1 for g in per if any(idx[m['candidate_id']]['state'] not in TERM for m in g['members']))}
print(json.dumps(out, ensure_ascii=False, indent=1))
