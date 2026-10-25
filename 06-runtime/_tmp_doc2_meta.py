import json, sys, collections
from pathlib import Path

idx = {}
for l in open('06-runtime/state/candidate-index.jsonl', encoding='utf-8'):
    if l.strip():
        r = json.loads(l); idx[r['candidate_id']] = r
gs = [json.loads(l) for l in open('06-runtime/automation/2026-10-25-cross-source-candidate-consolidation/duplicate-groups.jsonl', encoding='utf-8') if l.strip()]

open_all = [g for g in gs if g['doc_count'] == 2 and any(idx[m['candidate_id']]['state'] == 'needs_evidence' for m in g['members'])]
if sys.argv[1] == 'survey':
    c = collections.Counter(g['unit_type'] for g in open_all)
    for k, v in sorted(c.items(), key=lambda x: -x[1]):
        print(k, v)
    print('total', len(open_all))
    raise SystemExit

ut = sys.argv[1]
lo = int(sys.argv[2]); hi = int(sys.argv[3])
sel = [g for g in open_all if g['unit_type'] == ut]
sel.sort(key=lambda g: g['group_id'])
total = len(sel)
sel = sel[lo:hi]
out = []
for g in sel:
    out.append(f"===== {g['group_id']} {g['keys'].get('title')}")
    for m in g['members']:
        r = idx[m['candidate_id']]; p = r['payload']; sp = p.get('source_span') or {}
        out.append(f"-- {m['candidate_id']} L{sp.get('line_start')}-L{sp.get('line_end')} slug={p.get('proposed_slug')} state={r['state']}")
        out.append('S: ' + (p.get('summary') or '').replace('\n', ' '))
        pf = p.get('proposed_fields') or {}
        keep = {k: v for k, v in pf.items() if k in ('title', 'name_en', 'name_original', 'definition', 'description', 'category', 'period', 'aliases', 'tags', 'location', 'role', 'birth_year', 'death_year', 'date', 'author', 'publisher', 'year')}
        if keep:
            out.append('F: ' + json.dumps(keep, ensure_ascii=False))
Path(f'06-runtime/_tmp_{ut}_meta_{lo}_{hi}.txt').write_text('\n'.join(out) + '\n', encoding='utf-8')
print(total, 'open', ut, 'groups; wrote', len(sel), 'groups', len(out), 'lines')
