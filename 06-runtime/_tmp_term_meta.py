import json, sys
from pathlib import Path

idx={json.loads(l)['candidate_id']:json.loads(l) for l in open('06-runtime/state/candidate-index.jsonl',encoding='utf-8') if l.strip()}
gs=[json.loads(l) for l in open('06-runtime/automation/2026-10-25-cross-source-candidate-consolidation/duplicate-groups.jsonl',encoding='utf-8') if l.strip()]
lo=int(sys.argv[1]); hi=int(sys.argv[2])
sel=[g for g in gs if g['unit_type']=='term' and g['doc_count']==2 and any(idx[m['candidate_id']]['state']=='needs_evidence' for m in g['members'])]
sel.sort(key=lambda g:g['group_id'])
sel=sel[lo:hi]
out=[]
for g in sel:
    out.append(f"===== {g['group_id']} {g['keys'].get('title')}")
    for m in g['members']:
        r=idx[m['candidate_id']]; p=r['payload']; sp=p.get('source_span') or {}
        out.append(f"-- {m['candidate_id']} L{sp.get('line_start')}-L{sp.get('line_end')} slug={p.get('proposed_slug')} state={r['state']}")
        out.append('S: '+(p.get('summary') or '').replace('\n',' '))
        pf=p.get('proposed_fields') or {}
        keep={k:v for k,v in pf.items() if k in ('title','name_en','definition','description','category','period','aliases','tags')}
        if keep: out.append('F: '+json.dumps(keep,ensure_ascii=False))
Path(f'06-runtime/_tmp_term_meta_{lo}_{hi}.txt').write_text('\n'.join(out)+'\n',encoding='utf-8')
print(len(sel),'groups',len(out),'lines')
