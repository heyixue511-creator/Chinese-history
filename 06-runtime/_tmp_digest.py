import json, sys
from pathlib import Path

rows=[json.loads(l) for l in Path('06-runtime/state/candidate-index.jsonl').read_text(encoding='utf-8').splitlines() if l.strip()]
state={r['candidate_id']:r for r in rows}
groups=[json.loads(l) for l in open('06-runtime/automation/2026-10-25-cross-source-candidate-consolidation/duplicate-groups.jsonl',encoding='utf-8') if l.strip()]
ut=sys.argv[1]; dc=int(sys.argv[2])
sel=[g for g in groups if g['unit_type']==ut and g['doc_count']==dc and any(state[m['candidate_id']]['state']=='needs_evidence' for m in g['members'])]
sel.sort(key=lambda g:g['group_id'])
out=[]
for g in sel:
    out.append(f"===== {g['group_id']} title={g['keys'].get('title')} docs={g['doc_count']}")
    for m in g['members']:
        r=state[m['candidate_id']]
        if r['state']!='needs_evidence':
            out.append(f"--- {m['candidate_id']} STATE={r['state']}"); continue
        p=r['payload']; sp=p.get('source_span') or {}
        doc=r.get('origin_ref') or ''
        out.append(f"--- {m['candidate_id']} slug={p.get('proposed_slug')} span=L{sp.get('line_start')}-L{sp.get('line_end')}")
        out.append('SUMMARY: '+(p.get('summary') or '').replace('\n',' '))
        pf=p.get('proposed_fields')
        if pf: out.append('FIELDS: '+json.dumps(pf,ensure_ascii=False))
        src=Path('03基础书籍-md文档')
        # locate source file from evidence refs
        ev=(r.get('evidence_refs') or [''])[0]
        fp=ev.split('#')[0]
        if fp and Path(fp).is_file() and sp.get('line_start'):
            lines=Path(fp).read_text(encoding='utf-8').splitlines()
            a=max(0,int(sp['line_start'])-1); b=min(len(lines),int(sp['line_end']))
            title=(p.get('title') or '').strip('《》')
            if b-a>40:
                hit=None
                for i in range(a,b):
                    if title and title in lines[i]: hit=i; break
                if hit is None: hit=a
                a=max(a,hit-8); b=min(b,a+32)
            out.append(f"### {fp} L{a+1}-L{b}")
            out.extend(lines[a:b])
Path(f'06-runtime/_tmp_digest_{ut}_{dc}.txt').write_text('\n'.join(out)+'\n',encoding='utf-8')
print('groups',len(sel),'lines',len(out))
