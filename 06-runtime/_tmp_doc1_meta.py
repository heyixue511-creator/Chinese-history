import json
from pathlib import Path

idx = {}
for l in open('06-runtime/state/candidate-index.jsonl', encoding='utf-8'):
    if l.strip():
        r = json.loads(l); idx[r['candidate_id']] = r
gs = [json.loads(l) for l in open('06-runtime/automation/2026-10-25-cross-source-candidate-consolidation/duplicate-groups.jsonl', encoding='utf-8') if l.strip()]
IDS = ['xdup-0213', 'xdup-0232', 'xdup-0371', 'xdup-0373', 'xdup-0383', 'xdup-0471']
out = []
for g in gs:
    if g['group_id'] not in IDS: continue
    out.append(f"===== {g['group_id']} type={g['unit_type']} doc_count={g['doc_count']} title={g['keys'].get('title')}")
    out.append('keys: ' + json.dumps(g['keys'], ensure_ascii=False))
    for m in g['members']:
        r = idx[m['candidate_id']]; p = r['payload']; sp = p.get('source_span') or {}
        out.append(f"-- {m['candidate_id']} L{sp.get('line_start')}-L{sp.get('line_end')} slug={p.get('proposed_slug')} state={r['state']}")
        out.append('S: ' + (p.get('summary') or '').replace('\n', ' '))
        pf = p.get('proposed_fields') or {}
        out.append('F: ' + json.dumps(pf, ensure_ascii=False))
Path('06-runtime/_tmp_doc1_meta.txt').write_text('\n'.join(out) + '\n', encoding='utf-8')
print('groups', sum(1 for g in gs if g['group_id'] in IDS), 'lines', len(out))
