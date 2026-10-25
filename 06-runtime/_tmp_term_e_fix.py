import json, hashlib
from pathlib import Path

PKG = Path('06-runtime/automation/2026-10-25-term-doc2-batch-e')
plan = [json.loads(l) for l in open(PKG / 'apply-plan.jsonl', encoding='utf-8') if l.strip()]
for r in plan:
    if r['action'] != 'update':
        continue
    t = Path(r['target_ref']).read_text(encoding='utf-8').replace('\r\n', '\n'); b = t.encode()
    r['after_sha256'] = 'sha256:' + hashlib.sha256(b).hexdigest()
    r['bytes'] = len(b); r['lines'] = t.count('\n')
    r['note'] += '；应用后修正 citation 书名与 source_file 路径为“中国工艺美术史（修订本）”，after 指纹随之重算'
with open(PKG / 'apply-plan.jsonl', 'w', encoding='utf-8', newline='\n') as f:
    for r in plan:
        f.write(json.dumps(r, ensure_ascii=False) + '\n')
print([r['after_sha256'] for r in plan if r['action'] == 'update'])
