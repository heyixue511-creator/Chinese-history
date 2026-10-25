import json, hashlib
from pathlib import Path

PKG = Path('06-runtime/automation/2026-10-25-doc1-groups-batch')
PKG.mkdir(parents=True, exist_ok=True)
gs = {}
for l in open('06-runtime/automation/2026-10-25-cross-source-candidate-consolidation/duplicate-groups.jsonl', encoding='utf-8'):
    if l.strip():
        g = json.loads(l); gs[g['group_id']] = g

P = '2009-zhaonong-zhongguo-yishu-shejishi:'
M = {
 'xdup-0213': (P+'cand-01-20', '04-knowledge/units/persons/nuwa.md'),
 'xdup-0232': (P+'cand-08-70', '04-knowledge/units/persons/yan-su.md'),
 'xdup-0371': (P+'cand-10-83', '04-knowledge/units/terms/xuan-zhi.md'),
 'xdup-0373': (P+'cand-06-16', '04-knowledge/units/terms/ping-feng.md'),
 'xdup-0383': (P+'cand-12-159', '04-knowledge/units/terms/zhao-tie.md'),
 'xdup-0471': (P+'cand-12-119', '04-knowledge/units/works/shanghai-expo-china-pavilion-2010.md'),
}
DATE = '2026-10-25'

def fp(path):
    t = Path(path).read_text(encoding='utf-8').replace('\r\n', '\n'); b = t.encode('utf-8')
    return 'sha256:' + hashlib.sha256(b).hexdigest(), len(b), t.count('\n')

ledger, plan, mapping = [], [], {}
def row(cid, exp, st, status, reason, target=None):
    d = {'candidate_id': cid, 'expected_state': exp, 'state': st,
         'decision': {'status': status, 'reason': reason, 'decided_by': 'Agent', 'decided_at': DATE},
         'updated_at': DATE}
    if target: d['target_ref'] = target
    ledger.append(d)

for gid, (canon_id, tref) in M.items():
    g = gs[gid]; title = g['keys'].get('title'); members = [m['candidate_id'] for m in g['members']]
    assert canon_id in members, (gid, canon_id, members)
    row(canon_id, 'needs_evidence', 'ready_for_review', 'pending', f'同组重复候选已回收，准备语义写回 {tref}')
    row(canon_id, 'ready_for_review', 'approved', 'approved', f'canonical 候选复读完成，批准 exact change-set 写入 {tref}')
    row(canon_id, 'approved', 'applied', 'approved', f'已按 exact change-set 写入 {tref}', tref)
    sha, by, ln = fp(tref)
    plan.append({'action': 'create', 'target_ref': tref, 'candidate_id': canon_id, 'entity': title,
                 'before': None, 'after_sha256': sha, 'bytes': by, 'lines': ln,
                 'note': f'{gid} 同一册内两处候选合并建立 KU；六节结构与来源定位见候选摘要'})
    mapping[gid] = {'entity': title, 'target_ref': tref, 'canonical_candidate_id': canon_id, 'action': 'create'}
    for cid in members:
        if cid == canon_id: continue
        row(cid, 'needs_evidence', 'rejected', 'rejected',
            f'同组重复候选，canonical 候选指向同一 entity「{title}」，内容已并入 {tref}，该候选不再单独写回', tref)

with open(PKG / 'candidate-decision-ledger.jsonl', 'w', encoding='utf-8', newline='\n') as f:
    for r in ledger: f.write(json.dumps(r, ensure_ascii=False) + '\n')
with open(PKG / 'apply-plan.jsonl', 'w', encoding='utf-8', newline='\n') as f:
    for r in plan: f.write(json.dumps(r, ensure_ascii=False) + '\n')
json.dump(mapping, open(PKG / 'canonical-mapping.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('plan', len(plan), 'ledger', len(ledger), 'mapping', len(mapping))
for r in plan: print(r['target_ref'], r['after_sha256'][:20])
