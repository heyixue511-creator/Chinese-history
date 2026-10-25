import json, hashlib
from pathlib import Path

PKG = Path('06-runtime/automation/2026-10-25-term-doc2-batch-e')
PKG.mkdir(parents=True, exist_ok=True)
gs = {}
for l in open('06-runtime/automation/2026-10-25-cross-source-candidate-consolidation/duplicate-groups.jsonl', encoding='utf-8'):
    if l.strip():
        g = json.loads(l); gs[g['group_id']] = g

M = {
 'xdup-0444': ('2010-tianzibing', 'he-cai'),
 'xdup-0445': ('2009-xiayanjing', 'bao-yi-bo-dai'),
 'xdup-0447': ('2016-xiayanjing', 'dou-vessel'),
 'xdup-0448': ('2016-xiayanjing', 'zhisun-fu'),
 'xdup-0449': ('2009-xiayanjing', 'youshang-cai'),
 'xdup-0450': ('2009-xiayanjing', 'youlihong-ci'),
 'xdup-0451': ('2016-xiayanjing', 'lifang-zhi'),
 'xdup-0452': ('2016-xiayanjing', 'tieqi-shidai'),
 'xdup-0453': ('2016-xiayanjing', 'qian-you-tao'),
 'xdup-0454': ('2016-xiayanjing', 'zhu-ding-xiang-wu'),
 'xdup-0455': ('2016-xiayanjing', 'tao-zeng'),
 'xdup-0456': ('2016-xiayanjing', 'tao-gui'),
 'xdup-0457': ('2004-gaofeng', 'diao-qi'),
 'xdup-0458': ('2009-zhaonong', 'qing-ci'),
 'xdup-0459': ('2004-gaofeng', 'qingtong'),
 'xdup-0460': ('2009-xiayanjing', 'qingtong-shidai'),
 'xdup-0461': ('2009-xiayanjing', 'qingtong-shuiqi'),
 'xdup-0462': ('2009-xiayanjing', 'qingtong-liqi'),
 'xdup-0463': ('2009-xiayanjing', 'qingtong-jiuqi'),
 'xdup-0464': ('2009-xiayanjing', 'qingtong-shiqi'),
 'xdup-0465': ('2016-xiayanjing', 'feiyi'),
 'xdup-0466': ('2009-xiayanjing', 'gugu-guan'),
 'xdup-0467': ('2016-xiayanjing', 'yu-dai'),
 'xdup-0469': ('2010-tianzibing', 'qijia-wenhua'),
 'xdup-0470': ('2009-zhaonong', 'longyao'),
}
UPD = {'xdup-0468': ('2016-xiayanjing', '04-knowledge/units/terms/tianji-hu.md',
                     {'sha256': 'sha256:b9774b6c31080dfbf8ef257072e4d96a4cf93b5c0cec831b9225b878f72f0933', 'bytes': 3372, 'lines': 84})}
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

for gid, (prefix, tref, before) in UPD.items():
    g = gs[gid]; members = g['members']; title = g['keys'].get('title')
    canon = [m for m in members if m['doc_id'].startswith(prefix)]
    assert len(canon) == 1, (gid, canon)
    c = canon[0]['candidate_id']
    row(c, 'needs_evidence', 'ready_for_review', 'pending', f'同组重复候选已回收，既有 {tref} 需补入田自秉形制源流，准备 update')
    row(c, 'ready_for_review', 'approved', 'approved', f'既有 KU 复读完成，批准 exact change-set 追加来源并改写描述与核心内容 → {tref}')
    row(c, 'approved', 'applied', 'approved', f'已按 exact change-set 更新 {tref}（version 1→2）', tref)
    for m in members:
        if m['candidate_id'] == c: continue
        row(m['candidate_id'], 'needs_evidence', 'rejected', 'rejected',
            f'同组重复候选，canonical 候选指向同一 entity「{title}」，内容已并入 {tref}，该候选不再单独写回', tref)
    sha, by, ln = fp(tref)
    plan.append({'action': 'update', 'target_ref': tref, 'candidate_id': c, 'entity': title,
                 'before': before, 'after_sha256': sha, 'bytes': by, 'lines': ln,
                 'note': f'{gid} 在既有 tianji-hu.md 上补入田自秉 2010 的盘口壶源流、鸡头装饰化与唐代龙耳壶演变；source_count 2→3，version 1→2'})
    mapping[gid] = {'entity': title, 'target_ref': tref, 'canonical_candidate_id': c, 'action': 'update'}

with open(PKG / 'candidate-decision-ledger.jsonl', 'w', encoding='utf-8', newline='\n') as f:
    for r in ledger: f.write(json.dumps(r, ensure_ascii=False) + '\n')
with open(PKG / 'apply-plan.jsonl', 'w', encoding='utf-8', newline='\n') as f:
    for r in plan: f.write(json.dumps(r, ensure_ascii=False) + '\n')
json.dump(mapping, open(PKG / 'canonical-mapping.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('plan', len(plan), 'ledger', len(ledger), 'groups', len(mapping))
