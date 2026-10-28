# -*- coding: utf-8 -*-
import io, json, os, re, glob

rows = json.load(io.open('_zn_ch4_rows.json', encoding='utf-8'))
files = glob.glob('04-knowledge/units/**/*.md', recursive=True)
index = []
for f in files:
    txt = io.open(f, encoding='utf-8').read()
    base = os.path.basename(f)
    m = re.search(r'^title:\s*(.+)$', txt, re.M)
    title = m.group(1).strip().strip('"\'') if m else ''
    m2 = re.search(r'^aliases:\s*(.+)$', txt, re.M)
    aliases = m2.group(1).strip() if m2 else ''
    index.append((f, title, aliases, txt))

out = []
for r in rows:
    p = r['payload']; t = p.get('title','')
    slug = p.get('proposed_slug','')
    key = re.split(r'[（(]', t)[0].strip().strip('《》')
    hits = []
    for f, title, aliases, txt in index:
        if key and (key in title or key in aliases or key in os.path.basename(f)):
            hits.append('%s [%s]' % (f, title))
    out.append((r['candidate_id'].split(':')[1], p.get('unit_type'), slug, t, hits))

for cid, ut, slug, t, hits in out:
    print('%s\t%s\t%s\t%s\t%s' % (cid, ut, slug, t, ' || '.join(hits[:6]) if hits else '-'))
print('---')
print('with hits:', sum(1 for x in out if x[4]))
print('no hits:', sum(1 for x in out if not x[4]))
