import json, hashlib
from pathlib import Path

PKG = Path('06-runtime/automation/2026-10-25-work-doc2-batch-b')
PKG.mkdir(parents=True, exist_ok=True)
gs = {}
for l in open('06-runtime/automation/2026-10-25-cross-source-candidate-consolidation/duplicate-groups.jsonl', encoding='utf-8'):
    if l.strip():
        g = json.loads(l); gs[g['group_id']] = g

# group_id -> (canonical prefix, slug, action)
M = {
 'xdup-0499': ('2016-xiayanjing', 'tibi-chaju', 'create'),
 'xdup-0500': ('2009-zhaonong', 'zenghouyi-zunpan', 'create'),
 'xdup-0501': ('2009-zhaonong', 'muniu-liuma', 'create'),
 'xdup-0502': ('2009-xiayanjing', 'luanshu-fou', 'create'),
 'xdup-0503': ('2009-zhaonong', 'mao-gong-ding', 'create'),
 'xdup-0504': ('2009-zhaonong', 'shui-dui', 'create'),
 'xdup-0505': ('2010-tianzibing', 'shuilu-gongzhan-jian', 'create'),
 'xdup-0506': ('2009-zhaonong', 'yongle-gong', 'create'),
 'xdup-0507': ('2009-xiayanjing', 'haigu-zhanchuan', 'create'),
 'xdup-0508': ('2009-zhaonong', 'qingming-shanghe-tu', 'create'),
 'xdup-0509': ('2009-xiayanjing', 'yu-pingtuo-shuang-putao-jing', 'create'),
 'xdup-0510': ('2004-gaofeng', 'qin-bing-ma-yong', 'create'),
 'xdup-0511': ('2009-xiayanjing', 'qin-shi-huang-ling', 'create'),
 'xdup-0512': ('2009-xiayanjing', 'qin-bing-ma-yong', 'no_delta'),
 'xdup-0513': ('2016-xiayanjing', 'lv-you-tao-lou', 'create'),
 'xdup-0514': ('2009-xiayanjing', 'wudao-renwu-dongwu-wen-sanse-jin', 'create'),
 'xdup-0515': ('2010-tianzibing', 'huaniao-renwu-luodian-jing', 'create'),
 'xdup-0516': ('2010-tianzibing', 'lianhua-zun', 'create'),
 'xdup-0517': ('2009-zhaonong', 'huwen-da-shiqing', 'create'),
 'xdup-0518': ('2016-xiayanjing', 'liujin-wuma-xianbei-yinhu', 'create'),
 'xdup-0519': ('2016-xiayanjing', 'tong-niu-deng', 'create'),
 'xdup-0520': ('2009-xiayanjing', 'yin-xunlu', 'create'),
 'xdup-0521': ('2010-tianzibing', 'cuojin-boshanlu', 'create'),
 'xdup-0522': ('2009-xiayanjing', 'lianhua-zun', 'no_delta'),
 'xdup-0523': ('2009-zhaonong', 'yiheyuan', 'create'),
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

for gid, (prefix, slug, action) in M.items():
    g = gs[gid]; members = g['members']; title = g['keys'].get('title')
    canon = [m for m in members if m['doc_id'].startswith(prefix)]
    assert len(canon) == 1, (gid, canon)
    c = canon[0]['candidate_id']; tref = f'04-knowledge/units/works/{slug}.md'
    if action == 'create':
        row(c, 'needs_evidence', 'ready_for_review', 'pending', f'同组重复候选已回收，准备语义写回 {tref}')
        row(c, 'ready_for_review', 'approved', 'approved', f'canonical 候选六节复读完成，批准 exact change-set 写入 {tref}')
        row(c, 'approved', 'applied', 'approved', f'已按 exact change-set 写入 {tref}', tref)
    else:
        row(c, 'needs_evidence', 'ready_for_review', 'pending', f'跨组同实体核对：目标 {tref} 已由同批 xdup-0516/0510 建立')
        row(c, 'ready_for_review', 'approved', 'approved', f'复读确认 {tref} 已完整覆盖本组候选内容，批准 no_delta')
        row(c, 'approved', 'no_delta', 'approved',
            f'{tref} 已完整覆盖本组候选内容（含两册评语），无需重复建条；判定 no_delta', tref)
    for m in members:
        if m['candidate_id'] == c: continue
        row(m['candidate_id'], 'needs_evidence', 'rejected', 'rejected',
            f'同组重复候选，canonical 候选指向同一 entity「{title}」，内容已并入 {tref}，该候选不再单独写回', tref)
    if action == 'create':
        sha, by, ln = fp(tref)
        plan.append({'action': 'create', 'target_ref': tref, 'candidate_id': c, 'entity': title,
                     'before': None, 'after_sha256': sha, 'bytes': by, 'lines': ln,
                     'note': f'{gid} 两册来源合并建立 work KU；六节结构与来源定位见候选摘要'})
    mapping[gid] = {'entity': title, 'target_ref': tref, 'canonical_candidate_id': c, 'action': action}

with open(PKG / 'candidate-decision-ledger.jsonl', 'w', encoding='utf-8', newline='\n') as f:
    for r in ledger: f.write(json.dumps(r, ensure_ascii=False) + '\n')
with open(PKG / 'apply-plan.jsonl', 'w', encoding='utf-8', newline='\n') as f:
    for r in plan: f.write(json.dumps(r, ensure_ascii=False) + '\n')
json.dump(mapping, open(PKG / 'canonical-mapping.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('plan', len(plan), 'ledger', len(ledger), 'groups', len(mapping))
