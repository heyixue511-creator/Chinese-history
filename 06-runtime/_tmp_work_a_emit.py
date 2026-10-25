import json, hashlib, sys
from pathlib import Path

PKG = Path('06-runtime/automation/2026-10-25-work-doc2-batch-a')
PKG.mkdir(parents=True, exist_ok=True)
gs = {}
for l in open('06-runtime/automation/2026-10-25-cross-source-candidate-consolidation/duplicate-groups.jsonl', encoding='utf-8'):
    if l.strip():
        g = json.loads(l); gs[g['group_id']] = g

M = {
 'xdup-0472': ('2004-gaofeng', 'yannian-yishou-jin'),
 'xdup-0473': ('2016-xiayanjing', 'qikong-shidao'),
 'xdup-0474': ('2009-xiayanjing', 'san-jiao-lou'),
 'xdup-0475': ('2009-xiayanjing', 'shanghai-huifeng-yinhang'),
 'xdup-0476': ('2009-zhaonong', 'foguang-si-dadian'),
 'xdup-0477': ('2009-xiayanjing', 'houfeng-dizhenyi'),
 'xdup-0478': ('2016-xiayanjing', 'ou-fangyi'),
 'xdup-0479': ('2009-xiayanjing', 'guiguxiashan-qinghua-guan'),
 'xdup-0480': ('2016-xiayanjing', 'yuan-yinjingjia'),
 'xdup-0481': ('2009-xiayanjing', 'xiangyun-huoju'),
 'xdup-0482': ('2009-xiayanjing', 'miaoying-si-baita'),
 'xdup-0483': ('2009-zhaonong', 'shiwu-lianzhan-tongdeng'),
 'xdup-0484': ('2009-xiayanjing', 'nanhai-one'),
 'xdup-0485': ('2009-zhaonong', 'nanchan-si-dadian'),
 'xdup-0486': ('2009-xiayanjing', 'tang-yin-xiangnang'),
 'xdup-0487': ('2009-xiayanjing', 'shang-elephant-zun'),
 'xdup-0488': ('2009-zhaonong', 'siyang-fangzun'),
 'xdup-0489': ('2004-gaofeng', 'simei-tu'),
 'xdup-0490': ('2009-zhaonong', 'yuanmingyuan'),
 'xdup-0491': ('2016-xiayanjing', 'da-ke-ding'),
 'xdup-0492': ('2016-xiayanjing', 'daming-gong'),
 'xdup-0493': ('2009-zhaonong', 'dayunhe'),
 'xdup-0494': ('2009-xiayanjing', 'dingxian-kaiyuansi-liaodi-pagoda'),
 'xdup-0495': ('2010-tianzibing', 'dingyao-haier-zhen'),
 'xdup-0496': ('2009-xiayanjing', 'kaifeng-xiangguosi-pagoda'),
 'xdup-0497': ('2009-xiayanjing', 'caiqi-mudiao-dongwu-zuoping'),
 'xdup-0498': ('2009-zhaonong', 'zhuozhengyuan'),
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
    c = canon[0]['candidate_id']; tref = f'04-knowledge/units/works/{slug}.md'
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
                 'note': f'{gid} 两册来源合并建立 work KU；六节结构与来源定位见候选摘要'})
    mapping[gid] = {'entity': title, 'target_ref': tref, 'canonical_candidate_id': c, 'action': 'create'}

with open(PKG / 'candidate-decision-ledger.jsonl', 'w', encoding='utf-8', newline='\n') as f:
    for r in ledger: f.write(json.dumps(r, ensure_ascii=False) + '\n')
with open(PKG / 'apply-plan.jsonl', 'w', encoding='utf-8', newline='\n') as f:
    for r in plan: f.write(json.dumps(r, ensure_ascii=False) + '\n')
json.dump(mapping, open(PKG / 'canonical-mapping.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('plan', len(plan), 'ledger', len(ledger), 'groups', len(mapping))
