import json, glob, re
from pathlib import Path

ku = {}
for d in ['persons','terms','works','places','procedures','events','institutions','publications']:
    for f in glob.glob(f'04-knowledge/units/{d}/*.md'):
        t = open(f, encoding='utf-8').read()
        ti = re.search(r'^title: (.+)$', t, re.M).group(1)
        zh = re.sub(r'（.*?）$', '', ti).strip().replace(' ', '')
        als = re.findall(r'^  - (.+)$', (re.search(r'^aliases:\n((?:  - .+\n)+)', t, re.M) or [None, ''])[1], re.M)
        ku[zh] = f
        for a in als:
            ku.setdefault(a.strip().replace(' ', ''), f)

def norm(s):
    return re.sub(r'[\s·・,，、（）()“”"\'—\-]', '', s or '')

rows = [json.loads(l) for l in open('06-runtime/state/candidate-index.jsonl', encoding='utf-8') if l.strip()]
cand = [r for r in rows if r['state'] == 'needs_evidence' and r['candidate_type'] == 'unit']
out = []
for r in cand:
    p = r['payload']; ti = norm(p.get('title'))
    if ti not in ku: continue
    f = ku[ti]
    t = open(f, encoding='utf-8').read()
    docs = re.findall(r'^      doc_id: (.+)$', t, re.M)
    desc = re.search(r'## 描述\n\n(.+?)\n\n##', t, re.S)
    sp = p.get('source_span') or {}
    out.append(f"===== {r['candidate_id']} | type={p.get('unit_type')} | title={p.get('title')} | slug={p.get('proposed_slug')}")
    out.append(f"KU: {f} | docs: {sorted(set(docs))}")
    out.append(f"span: L{sp.get('line_start')}-L{sp.get('line_end')} | {r['origin_ref']}")
    out.append('S: ' + (p.get('summary') or '').replace('\n', ' '))
    out.append('F: ' + json.dumps(p.get('proposed_fields') or {}, ensure_ascii=False))
    out.append('KUdesc: ' + (desc.group(1).replace('\n', ' ') if desc else '')[:400])
Path('06-runtime/_tmp_overlap_meta.txt').write_text('\n'.join(out) + '\n', encoding='utf-8')
print('candidates', sum(1 for l in out if l.startswith('=====')), 'lines', len(out))
