import json, hashlib
from pathlib import Path

PKG = Path('06-runtime/automation/2026-10-25-term-doc2-batch-c')
PKG.mkdir(parents=True, exist_ok=True)
gs = {}
for l in open('06-runtime/automation/2026-10-25-cross-source-candidate-consolidation/duplicate-groups.jsonl', encoding='utf-8'):
    if l.strip():
        g = json.loads(l); gs[g['group_id']] = g

M = {
 'xdup-0390': ('2016-xiayanjing', 'xinshiqi-shidai'),
 'xdup-0391': ('2016-xiayanjing', 'mingguang-kai'),
 'xdup-0392': ('2009-xiayanjing', 'mingqi'),
 'xdup-0393': ('2010-tianzibing', 'jingtai-lan'),
 'xdup-0394': ('2004-gaofeng', 'yuefenpai'),
 'xdup-0395': ('2010-tianzibing', 'chai-yao'),
 'xdup-0396': ('2016-xiayanjing', 'an-furniture'),
 'xdup-0397': ('2009-zhaonong', 'meiping'),
 'xdup-0398': ('2009-xiayanjing', 'louchuan'),
 'xdup-0399': ('2009-zhaonong', 'she-yan'),
 'xdup-0400': ('2016-xiayanjing', 'shachuan'),
 'xdup-0401': ('2016-xiayanjing', 'qingdai-jiaju-sanda-mingzuo'),
 'xdup-0402': ('2009-zhaonong', 'huohua'),
 'xdup-0403': ('2010-tianzibing', 'xipi'),
 'xdup-0404': ('2016-xiayanjing', 'dulunche'),
 'xdup-0405': ('2009-zhaonong', 'yuhuchun-ping'),
 'xdup-0406': ('2009-zhaonong', 'glass'),
 'xdup-0407': ('2009-zhaonong', 'oracle-bone-script'),
 'xdup-0408': ('2016-xiayanjing', 'baici'),
 'xdup-0410': ('2016-xiayanjing', 'xiangxie'),
 'xdup-0411': ('2016-xiayanjing', 'shiliu-qun'),
 'xdup-0412': ('2016-xiayanjing', 'zuyongdiao'),
 'xdup-0413': ('2010-tianzibing', 'yaobian'),
 'xdup-0414': ('2009-zhaonong', 'duan-yan'),
 'xdup-0415': ('2016-xiayanjing', 'fu-vessel'),
 'xdup-0416': ('2010-tianzibing', 'yuexiu'),
}
NO_DELTA = {'xdup-0409': '04-knowledge/units/terms/baigong.md'}
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

for gid, tref in NO_DELTA.items():
    g = gs[gid]; members = g['members']; title = g['keys'].get('title')
    c = members[0]['candidate_id']
    reason = ('既有 terms/baigong.md 已覆盖「百工制度」：其 aliases 已列「百工制度」，正文已引高丰 2004 L947、L949-L953 与李立新 2011 L827 的官府手工业者、六工分职与制度成熟判断。'
              '本组两候选所指内容与既有 KU 重叠，无需新增字段或段落，判定 no_delta。')
    row(c, 'needs_evidence', 'ready_for_review', 'pending', f'同组候选复读后指向既有 {tref}，准备 no_delta 判定')
    row(c, 'ready_for_review', 'approved', 'approved', f'确认既有 {tref} 已完整覆盖本条，批准 no_delta')
    row(c, 'approved', 'no_delta', 'approved', reason, tref)
    for m in members:
        if m['candidate_id'] == c: continue
        row(m['candidate_id'], 'needs_evidence', 'rejected', 'rejected',
            f'同组重复候选，内容已由 {tref} 覆盖并为 canonical 候选 no_delta 所吸收，不再单独写回', tref)
    mapping[gid] = {'entity': title, 'target_ref': tref, 'canonical_candidate_id': c, 'action': 'no_delta'}

with open(PKG / 'candidate-decision-ledger.jsonl', 'w', encoding='utf-8', newline='\n') as f:
    for r in ledger: f.write(json.dumps(r, ensure_ascii=False) + '\n')
with open(PKG / 'apply-plan.jsonl', 'w', encoding='utf-8', newline='\n') as f:
    for r in plan: f.write(json.dumps(r, ensure_ascii=False) + '\n')
json.dump(mapping, open(PKG / 'canonical-mapping.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('plan', len(plan), 'ledger', len(ledger), 'groups', len(mapping))
