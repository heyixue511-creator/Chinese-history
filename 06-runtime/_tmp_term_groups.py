import json
from pathlib import Path
idx={json.loads(l)['candidate_id']:json.loads(l) for l in open('06-runtime/state/candidate-index.jsonl',encoding='utf-8') if l.strip()}
gs=[json.loads(l) for l in open('06-runtime/automation/2026-10-25-cross-source-candidate-consolidation/duplicate-groups.jsonl',encoding='utf-8') if l.strip()]
sel=[g for g in gs if g['unit_type']=='term' and g['doc_count']==2 and any(idx[m['candidate_id']]['state']=='needs_evidence' for m in g['members'])]
sel.sort(key=lambda g:g['group_id'])
files={p.stem for p in Path('04-knowledge/units/terms').glob('*.md')}
out=[]
for g in sel:
    t=g['keys'].get('title'); slugs=[]
    for m in g['members']:
        p=idx[m['candidate_id']]['payload']; s=p.get('proposed_slug')
        slugs.append(s+('*' if s in files else ''))
    out.append(f"{g['group_id']} {t} | "+' / '.join(slugs))
Path('06-runtime/_tmp_term_groups.txt').write_text('\n'.join(out)+'\n',encoding='utf-8')
print('\n'.join(out))
