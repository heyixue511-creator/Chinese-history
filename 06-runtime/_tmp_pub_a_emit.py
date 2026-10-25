import json, hashlib
from pathlib import Path

PKG = Path('06-runtime/automation/2026-10-25-publication-doc2-batch-a')
PKG.mkdir(parents=True, exist_ok=True)
gs = {}
for l in open('06-runtime/automation/2026-10-25-cross-source-candidate-consolidation/duplicate-groups.jsonl', encoding='utf-8'):
    if l.strip():
        g = json.loads(l); gs[g['group_id']] = g

# group -> list of (prefix, slug) for create; or (prefix, slug, 'no_delta')
M = {
 'xdup-0287': [('2016-xiayanjing', 'sixiu-biji')],
 'xdup-0288': [('2011-lilixin', 'zhongguo-gongyi-yange-shilue')],
 'xdup-0289': [('2004-gaofeng', 'zhongguo-shejishi-gaofeng'), ('2009-xiayanjing', 'zhongguo-shejishi-xiayanjing')],
 'xdup-0290': [('2009-xiayanjing', 'chuantong-gongyi-meishu-baohu-tiaoli')],
 'xdup-0291': [('2016-xiayanjing', 'shizhuzhai-huapu')],
 'xdup-0292': [('2009-zhaonong', 'lidai-minghua-ji')],
 'xdup-0293': [('2009-zhaonong', 'shiji')],
 'xdup-0294': [('2004-gaofeng', 'zhouyi')],
 'xdup-0295': [('2009-zhaonong', 'zhuangzi')],
 'xdup-0296': [('2009-zhaonong', 'xin-qingnian')],
 'xdup-0297': [('2016-xiayanjing', 'jifufu')],
 'xdup-0298': [('2016-xiayanjing', 'gegu-yaolun')],
 'xdup-0299': [('2009-xiayanjing', 'ziren-zhuan')],
 'xdup-0300': [('2016-xiayanjing', 'menglianglu', 'no_delta')],
 'xdup-0301': [('2010-tianzibing', 'mengxi-bitan')],
 'xdup-0302': [('2016-xiayanjing', 'menglianglu')],
 'xdup-0303': [('2010-tianzibing', 'chuci')],
 'xdup-0304': [('2009-zhaonong', 'wujing-zongyao')],
 'xdup-0305': [('2011-lilixin', 'haiguo-tuzhi')],
 'xdup-0306': [('2016-xiayanjing', 'qingmi-cang')],
 'xdup-0307': [('2016-xiayanjing', 'dianshizhai-huabao')],
 'xdup-0308': [('2010-tianzibing', 'yanxian-qingshang-jian')],
 'xdup-0309': [('2016-xiayanjing', 'shenbao')],
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

for gid, specs in M.items():
    g = gs[gid]; members = g['members']; title = g['keys'].get('title')
    used = set()
    for spec in specs:
        prefix, slug = spec[0], spec[1]
        action = spec[2] if len(spec) > 2 else 'create'
        canon = [m for m in members if m['doc_id'].startswith(prefix) and m['candidate_id'] not in used]
        assert len(canon) == 1, (gid, prefix, canon)
        c = canon[0]['candidate_id']; used.add(c)
        tref = f'04-knowledge/units/publications/{slug}.md'
        if action == 'create':
            row(c, 'needs_evidence', 'ready_for_review', 'pending', f'同组重复候选已回收，准备语义写回 {tref}')
            row(c, 'ready_for_review', 'approved', 'approved', f'canonical 候选六节复读完成，批准 exact change-set 写入 {tref}')
            row(c, 'approved', 'applied', 'approved', f'已按 exact change-set 写入 {tref}', tref)
            sha, by, ln = fp(tref)
            plan.append({'action': 'create', 'target_ref': tref, 'candidate_id': c, 'entity': title,
                         'before': None, 'after_sha256': sha, 'bytes': by, 'lines': ln,
                         'note': f'{gid} 两册来源合并建立 publication KU；六节结构与来源定位见候选摘要'})
            mapping[gid + ('#2' if len(specs) > 1 and spec is specs[1] else '')] = {
                'entity': title, 'target_ref': tref, 'canonical_candidate_id': c, 'action': 'create'}
        else:
            row(c, 'needs_evidence', 'ready_for_review', 'pending', f'跨组同实体核对：目标 {tref} 已由同批 xdup-0302 建立')
            row(c, 'ready_for_review', 'approved', 'approved', f'复读确认 {tref} 已完整覆盖本组候选内容，批准 no_delta')
            row(c, 'approved', 'no_delta', 'approved',
                f'{tref} 已完整覆盖本组候选内容（含“梦梁录／梦粱录”异写与赵农铺席、夜市记载），无需重复建条；判定 no_delta', tref)
            mapping[gid] = {'entity': title, 'target_ref': tref, 'canonical_candidate_id': c, 'action': 'no_delta'}
    for m in members:
        if m['candidate_id'] in used: continue
        row(m['candidate_id'], 'needs_evidence', 'rejected', 'rejected',
            f'同组重复候选，canonical 候选指向同一 entity「{title}」，内容已并入 {tref}，该候选不再单独写回', tref)

with open(PKG / 'candidate-decision-ledger.jsonl', 'w', encoding='utf-8', newline='\n') as f:
    for r in ledger: f.write(json.dumps(r, ensure_ascii=False) + '\n')
with open(PKG / 'apply-plan.jsonl', 'w', encoding='utf-8', newline='\n') as f:
    for r in plan: f.write(json.dumps(r, ensure_ascii=False) + '\n')
json.dump(mapping, open(PKG / 'canonical-mapping.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('plan', len(plan), 'ledger', len(ledger), 'mapping', len(mapping))
