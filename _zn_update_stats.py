# -*- coding: utf-8 -*-
import io, json, re, subprocess
from pathlib import Path

root = Path(r"D:/中国设计史研究")
d = json.load(io.open('_zn_decisions_ch3.json', encoding='utf-8'))['decisions']


def fm(text):
    lines = text.replace('\r\n', '\n').split('\n')
    out = {}
    if not lines or lines[0].strip() != '---':
        return out
    for ln in lines[1:]:
        if ln.strip() == '---':
            break
        m = re.match(r'^([a-z_]+):\s*(.*)$', ln)
        if m:
            out[m.group(1)] = m.group(2).strip()
    return out


rows = []
for x in d:
    if x['action'] != 'update':
        continue
    p = x['target']
    cur = fm((root / p).read_text(encoding='utf-8'))
    proc = subprocess.run(['git', 'show', 'HEAD:' + p], capture_output=True, cwd=str(root))
    old = fm(proc.stdout.decode('utf-8', errors='replace')) if proc.returncode == 0 else {}
    rows.append((x['entity'], p, old.get('version'), cur.get('version'), old.get('source_count'), cur.get('source_count')))
for r in rows:
    print(' | '.join(str(v) for v in r))
