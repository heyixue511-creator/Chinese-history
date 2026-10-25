import json, hashlib
from pathlib import Path

PKG = Path('06-runtime/automation/2026-10-25-procedure-doc2-batch')
PKG.mkdir(parents=True, exist_ok=True)
gs = {}
for l in open('06-runtime/automation/2026-10-25-cross-source-candidate-consolidation/duplicate-groups.jsonl', encoding='utf-8'):
    if l.strip():
        g = json.loads(l); gs[g['group_id']] = g

M = {
 'xdup-0277': [('2009-xiayanjing', 'chuihui-fa')],
 'xdup-0278': [('2004-gaofeng', 'jiazhu-tai')],
 'xdup-0279': [('2004-gaofeng', 'terms/jiaxie.md', 'update')],
 'xdup-0280': [('2009-xiayanjing', 'daolian-fa')],
 'xdup-0281': [('2010-tianzibing', 'ni-tiao-panzhu')],
 'xdup-0282': [('2009-xiayanjing', 'liuli-shaozhao')],
 'xdup-0283': [('2009-xiayanjing', 'zhuanlun-paizifa')],
 'xdup-0284': [('2009-zhaonong', 'liujin')],
 'xdup-0285': [('2009-xiayanjing', 'tiefan-zhuzao')],
 'xdup-0286': [('2009-zhaonong', 'diaoban-yinshua')],
}
DATE = '2026-10-25'
BEFORE_JIAXIE = {'sha256': 'sha256:1001a47130bfbe013e771aff4990b53af1929e35df4c5ae57d81749a2345f746', 'bytes': 4133, 'lines': 86}

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
        prefix, target = spec[0], spec[1]
        action = spec[2] if len(spec) > 2 else 'create'
        canon = [m for m in members if m['doc_id'].startswith(prefix) and m['candidate_id'] not in used]
        assert len(canon) == 1, (gid, prefix, canon)
        c = canon[0]['candidate_id']; used.add(c)
        if action == 'create':
            tref = f'04-knowledge/units/procedures/{target}.md'
            row(c, 'needs_evidence', 'ready_for_review', 'pending', f'同组重复候选已回收，准备语义写回 {tref}')
            row(c, 'ready_for_review', 'approved', 'approved', f'canonical 候选六节复读完成，批准 exact change-set 写入 {tref}')
            row(c, 'approved', 'applied', 'approved', f'已按 exact change-set 写入 {tref}', tref)
            sha, by, ln = fp(tref)
            plan.append({'action': 'create', 'target_ref': tref, 'candidate_id': c, 'entity': title,
                         'before': None, 'after_sha256': sha, 'bytes': by, 'lines': ln,
                         'note': f'{gid} 两册来源合并建立 procedure KU；六节结构与来源定位见候选摘要'})
            mapping[gid] = {'entity': title, 'target_ref': tref, 'canonical_candidate_id': c, 'action': 'create'}
        else:
            tref = '04-knowledge/units/' + target
            row(c, 'needs_evidence', 'ready_for_review', 'pending',
                f'既有 KU {tref} 已覆盖本组主体，核对缺口后准备 update')
            row(c, 'ready_for_review', 'approved', 'approved',
                f'复读确认 {tref} 缺《二仪实录》源流、唐代军服用途、正仓院屏风与隋开皇六年吐鲁番实物，批准 update')
            row(c, 'approved', 'applied', 'approved',
                f'已在 {tref} 增补《二仪实录》“秦汉间已有、陈梁间贵贱通服”、唐代军服、正仓院藏唐夹缬屏风、隋开皇六年吐鲁番实物、两三色与对称均衡，source_count 2→4，version 1→2', tref)
            sha, by, ln = fp(tref)
            plan.append({'action': 'update', 'target_ref': tref, 'candidate_id': c, 'entity': '夹缬',
                         'before': BEFORE_JIAXIE, 'after_sha256': sha, 'bytes': by, 'lines': ln,
                         'note': '补入高丰所引《事物纪原》转引《二仪实录》的秦汉源流、陈梁间贵贱通服、盛唐宫廷、唐代军服与日本正仓院唐夹缬屏风；补入田自秉所记隋开皇六年（586）吐鲁番实物、可染两三色、花纹对称均衡与家具装饰；源流三说（东汉／秦汉／隋）按层并列，不裁定；source_count 2→4，version 1→2。'})
            mapping[gid] = {'entity': title, 'target_ref': tref, 'canonical_candidate_id': c, 'action': 'update'}
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
