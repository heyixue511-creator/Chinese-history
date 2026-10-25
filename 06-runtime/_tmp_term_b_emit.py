import json, hashlib
from pathlib import Path

PKG = Path('06-runtime/automation/2026-10-25-term-doc2-batch-b')
PKG.mkdir(parents=True, exist_ok=True)
idx = {}
for l in open('06-runtime/state/candidate-index.jsonl', encoding='utf-8'):
    if l.strip():
        r = json.loads(l); idx[r['candidate_id']] = r
gs = {}
for l in open('06-runtime/automation/2026-10-25-cross-source-candidate-consolidation/duplicate-groups.jsonl', encoding='utf-8'):
    if l.strip():
        g = json.loads(l); gs[g['group_id']] = g

M = {
 'xdup-0359': ('2009-xiayanjing', 'yuanling-paoshan'),
 'xdup-0360': ('2009-zhaonong', 'plastic'),
 'xdup-0361': ('2009-xiayanjing', 'shi-class'),
 'xdup-0362': ('2004-gaofeng', 'zhuangjin'),
 'xdup-0363': ('2009-zhaonong', 'duozi-he'),
 'xdup-0364': ('2016-xiayanjing', 'tianji-hu'),
 'xdup-0365': ('2016-xiayanjing', 'jiaxie'),
 'xdup-0366': ('2010-tianzibing', 'zhuanghua'),
 'xdup-0367': ('2004-gaofeng', 'songti-zi'),
 'xdup-0368': ('2009-zhaonong', 'songban-shu'),
 'xdup-0369': ('2016-xiayanjing', 'guan-yao'),
 'xdup-0370': ('2011-lilixin', 'guanying-shougongye'),
 'xdup-0372': ('2004-gaofeng', 'xiaozhuan'),
 'xdup-0374': ('2009-zhaonong', 'gongyi-meishu'),
 'xdup-0375': ('2016-xiayanjing', 'daibing-gongju'),
 'xdup-0376': ('2004-gaofeng', 'xi-mat'),
 'xdup-0377': ('2004-gaofeng', 'weizhang'),
 'xdup-0378': ('2010-tianzibing', 'kaipian'),
 'xdup-0379': ('2010-tianzibing', 'yingqing'),
 'xdup-0380': ('2011-lilixin', 'rendong-wen'),
 'xdup-0381': ('2010-tianzibing', 'qiangjin'),
 'xdup-0382': ('2009-xiayanjing', 'pibo'),
 'xdup-0385': ('2009-zhaonong', 'tihuaji'),
 'xdup-0386': ('2009-zhaonong', 'tangci'),
 'xdup-0387': ('2009-zhaonong', 'dui-vessel'),
 'xdup-0388': ('2009-xiayanjing', 'wenzhi'),
 'xdup-0389': ('2009-zhaonong', 'dougong'),
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
