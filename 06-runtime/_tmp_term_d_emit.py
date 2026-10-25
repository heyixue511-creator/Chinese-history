import json, hashlib
from pathlib import Path

PKG = Path('06-runtime/automation/2026-10-25-term-doc2-batch-d')
PKG.mkdir(parents=True, exist_ok=True)
gs = {}
for l in open('06-runtime/automation/2026-10-25-cross-source-candidate-consolidation/duplicate-groups.jsonl', encoding='utf-8'):
    if l.strip():
        g = json.loads(l); gs[g['group_id']] = g

M = {
 'xdup-0417': ('2010-tianzibing', 'zikou-tiezu'),
 'xdup-0418': ('2016-xiayanjing', 'zisha-tao'),
 'xdup-0419': ('2016-xiayanjing', 'hongmu'),
 'xdup-0420': ('2009-xiayanjing', 'xishiqi'),
 'xdup-0421': ('2010-tianzibing', 'jingjin'),
 'xdup-0422': ('2016-xiayanjing', 'jiaoxie'),
 'xdup-0423': ('2016-xiayanjing', 'ling-silk'),
 'xdup-0424': ('2009-xiayanjing', 'lvse-sheji'),
 'xdup-0425': ('2009-zhaonong', 'bianzhong'),
 'xdup-0426': ('2010-tianzibing', 'piao-ci'),
 'xdup-0427': ('2009-xiayanjing', 'meijin-ejin'),
 'xdup-0428': ('2016-xiayanjing', 'chanheliao'),
 'xdup-0429': ('2009-zhaonong', 'leisi'),
 'xdup-0430': ('2004-gaofeng', 'lianzhu-wen'),
 'xdup-0431': ('2009-zhaonong', 'hufu'),
 'xdup-0432': ('2010-tianzibing', 'tuotai-qiqi'),
 'xdup-0433': ('2009-zhaonong', 'yishu-sheji'),
 'xdup-0434': ('2016-xiayanjing', 'huayou'),
 'xdup-0435': ('2016-xiayanjing', 'huadian'),
 'xdup-0436': ('2009-xiayanjing', 'sushi-caihua'),
 'xdup-0437': ('2010-tianzibing', 'suniboqing'),
 'xdup-0438': ('2016-xiayanjing', 'lantianren'),
 'xdup-0439': ('2009-xiayanjing', 'cangli-yuqi'),
 'xdup-0440': ('2016-xiayanjing', 'danke-heitao'),
 'xdup-0441': ('2010-tianzibing', 'shu-brocade'),
 'xdup-0442': ('2004-gaofeng', 'hudie-zhuang'),
 'xdup-0443': ('2016-xiayanjing', 'he-wool'),
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

for gid, (prefix, slug) in M.items():
    g = gs[gid]; members = g['members']; title = g['keys'].get('title')
    canon = [m for m in members if m['doc_id'].startswith(prefix)]
    assert len(canon) == 1, (gid, canon)
    c = canon[0]['candidate_id']; tref = f'04-knowledge/units/terms/{slug}.md'
    row(c, 'needs_evidence', 'ready_for_review', 'pending', f'同组重复候选已回收，准备语义写回 {tref}')
    row(c, 'ready_for_review', 'approved', 'approved', f'canonical 候选六节复读完成，批准 exact change-set 写入 {tref}')
    row(c, 'approved', 'applied', 'approved', f'已按 exact change-set 写入 {tref}', tref)
    for m in members:
        if m['candidate_id'] == c: continue
        row(m['candidate_id'], 'needs_evidence', 'rejected', 'rejected',
            f'同组重复候选，canonical 候选指向同一 entity「{title}」，内容已并入 {tref}，该候选不再单独写回', tref)
    sha, by, ln = fp(tref)
    plan.append({'action': 'create', 'target_ref': tref, 'candidate_id': c, 'entity': title,
                 'before': None, 'after_sha256': sha, 'bytes': by, 'lines': ln,
                 'note': f'{gid} 两册来源合并建立 term KU；六节结构与来源定位见候选摘要'})
    mapping[gid] = {'entity': title, 'target_ref': tref, 'canonical_candidate_id': c, 'action': 'create'}

with open(PKG / 'candidate-decision-ledger.jsonl', 'w', encoding='utf-8', newline='\n') as f:
    for r in ledger: f.write(json.dumps(r, ensure_ascii=False) + '\n')
with open(PKG / 'apply-plan.jsonl', 'w', encoding='utf-8', newline='\n') as f:
    for r in plan: f.write(json.dumps(r, ensure_ascii=False) + '\n')
json.dump(mapping, open(PKG / 'canonical-mapping.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('plan', len(plan), 'ledger', len(ledger), 'groups', len(mapping))
