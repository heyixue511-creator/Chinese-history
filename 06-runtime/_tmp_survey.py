import json, re
from pathlib import Path
from collections import Counter, defaultdict

rows=[json.loads(l) for l in Path('06-runtime/state/candidate-index.jsonl').read_text(encoding='utf-8').splitlines() if l.strip()]
groups=[json.loads(l) for l in open('06-runtime/automation/2026-10-25-cross-source-candidate-consolidation/duplicate-groups.jsonl',encoding='utf-8') if l.strip()]
ing={m['candidate_id'] for g in groups for m in g['members']}
un=[r for r in rows if r['state']=='needs_evidence' and r['candidate_type']=='unit' and r['candidate_id'] not in ing]

# existing KU titles/aliases
existing=defaultdict(set)
for p in Path('04-knowledge/units').rglob('*.md'):
    t=p.read_text(encoding='utf-8')
    title=re.search(r'^title:\s*(.+)$',t,re.M)
    if title:
        v=title.group(1).strip()
        v=re.sub(r'（.*?）','',v).strip()
        existing[p.parent.name].add(v)
    al=re.search(r'^aliases:\n((?:\s+- .+\n)+)',t,re.M)
    if al:
        for line in al.group(1).splitlines():
            existing[p.parent.name].add(line.strip('- ').strip())

lines=[]
lines.append('# ungrouped survey\n')
lines.append(f'total ungrouped {len(un)}\n')
lines.append('## by type\n')
for k,v in Counter(r['payload'].get('unit_type') for r in un).most_common():
    lines.append(f'- {k}: {v}')
lines.append('\n## title frequency (top 60)\n')
for k,v in Counter(r['payload'].get('title') for r in un).most_common(60):
    lines.append(f'- {k}: {v}')
lines.append('\n## title equals existing KU title/alias\n')
covered=[r for r in un if (r['payload'].get('title') or '').strip() in existing.get(r['payload'].get('unit_type'),set())]
lines.append(f'count {len(covered)} / {len(un)}')
lines.append('\n## by doc\n')
for k,v in Counter(r['candidate_id'].split(':')[0] for r in un).most_common():
    lines.append(f'- {k}: {v}')
lines.append('\n## samples per type\n')
for ut in ['person','term','work','publication','place','institution','procedure','event']:
    sel=[r for r in un if r['payload'].get('unit_type')==ut]
    lines.append(f'\n### {ut} ({len(sel)})')
    for r in sel[:8]:
        t=r['payload'].get('title'); s=(r['payload'].get('summary') or '')[:160]
        lines.append(f'- {t}｜{r["candidate_id"]}｜{s}')
Path('06-runtime/_tmp_survey.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')
print('wrote', len(un))
