import json, hashlib
from pathlib import Path

PKG = Path('06-runtime/automation/2026-10-25-place-doc2-batch')
PKG.mkdir(parents=True, exist_ok=True)
gs = {}
for l in open('06-runtime/automation/2026-10-25-cross-source-candidate-consolidation/duplicate-groups.jsonl', encoding='utf-8'):
    if l.strip():
        g = json.loads(l); gs[g['group_id']] = g

M = {
 'xdup-0252': [('2009-zhaonong', 'sanxingdui')],
 'xdup-0253': [('2009-zhaonong', 'linzi')],
 'xdup-0254': [('2009-zhaonong', 'yungang-shiku')],
 'xdup-0255': [('2010-tianzibing', 'places/yungang-shiku.md', 'no_delta')],
 'xdup-0256': [('2010-tianzibing', 'xianrendong-site')],
 'xdup-0257': [('2009-zhaonong', 'yanshi-shangcheng')],
 'xdup-0258': [('2009-zhaonong', 'nanjing')],
 'xdup-0259': [('2009-zhaonong', 'jizhou-kiln')],
 'xdup-0260': [('2010-tianzibing', 'zhoukoudian-site')],
 'xdup-0261': [('2009-xiayanjing', 'terms/ge-yao.md', 'update')],
 'xdup-0262': [('2009-xiayanjing', 'daxing-cheng')],
 'xdup-0263': [('2009-zhaonong', 'dadiwan-site')],
 'xdup-0264': [('2009-zhaonong', 'fuhao-tomb')],
 'xdup-0265': [('2010-tianzibing', 'yixing')],
 'xdup-0266': [('2010-tianzibing', 'shandingdong-site')],
 'xdup-0267': [('2010-tianzibing', 'miaodigou-site')],
 'xdup-0268': [('2009-zhaonong', 'jian-kiln')],
 'xdup-0269': [('2011-lilixin', 'dunhuang-mogao-ku')],
 'xdup-0270': [('2016-xiayanjing', 'zenghouyi-tomb')],
 'xdup-0271': [('2010-tianzibing', 'mancheng-hanmu')],
 'xdup-0272': [('2010-tianzibing', 'ou-kiln')],
 'xdup-0273': [('2010-tianzibing', 'yaozhou-kiln')],
 'xdup-0274': [('2009-zhaonong', 'liling')],
 'xdup-0275': [('2009-xiayanjing', 'yong-cheng')],
 'xdup-0276': [('2004-gaofeng', 'mawangdui-hanmu')],
}
DATE = '2026-10-25'
BEFORE_GEYAO = {'sha256': 'sha256:8b13f88c9ddc2505ca791b6ebb720937361e9107527d6524dfed86af41d40eec', 'bytes': 3696, 'lines': 85}

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
            tref = f'04-knowledge/units/places/{target}.md'
            row(c, 'needs_evidence', 'ready_for_review', 'pending', f'同组重复候选已回收，准备语义写回 {tref}')
            row(c, 'ready_for_review', 'approved', 'approved', f'canonical 候选六节复读完成，批准 exact change-set 写入 {tref}')
            row(c, 'approved', 'applied', 'approved', f'已按 exact change-set 写入 {tref}', tref)
            sha, by, ln = fp(tref)
            plan.append({'action': 'create', 'target_ref': tref, 'candidate_id': c, 'entity': title,
                         'before': None, 'after_sha256': sha, 'bytes': by, 'lines': ln,
                         'note': f'{gid} 两册来源合并建立 place KU；六节结构与来源定位见候选摘要'})
            mapping[gid] = {'entity': title, 'target_ref': tref, 'canonical_candidate_id': c, 'action': 'create'}
        elif action == 'update':
            tref = '04-knowledge/units/' + target
            row(c, 'needs_evidence', 'ready_for_review', 'pending',
                f'既有 KU {tref} 已覆盖本组主体，核对缺口后准备 update')
            row(c, 'ready_for_review', 'approved', 'approved',
                f'复读确认 {tref} 缺章生兄弟双窑传说、修内司官窑说与“浙江龙泉”说，批准 update')
            row(c, 'approved', 'applied', 'approved',
                f'已在 {tref} 增补章生一、章生二双窑传说、修内司官窑说、失透乳浊釉灰青与赵农“浙江龙泉、南宋官窑”说，四册并列，version 1→2', tref)
            sha, by, ln = fp(tref)
            plan.append({'action': 'update', 'target_ref': tref, 'candidate_id': c, 'entity': '哥窑',
                         'before': BEFORE_GEYAO, 'after_sha256': sha, 'bytes': by, 'lines': ln,
                         'note': '补入夏燕靖 2009 所记章生一、章生二兄弟在两浙路处州、龙泉县各建一窑的传说、传世宫藏哥窑瓷实为南宋修内司官窑烧制的专家说、失透乳浊釉与灰青釉色；补入赵农所记“在浙江龙泉、属龙泉窑系、南宋常为官窑产品、胎质暗黑、收缩差成开片”；窑址“未发现”与“浙江龙泉”并列不裁定；source_count 2→4，version 1→2。'})
            mapping[gid] = {'entity': title, 'target_ref': tref, 'canonical_candidate_id': c, 'action': 'update'}
        else:
            tref = '04-knowledge/units/' + target
            row(c, 'needs_evidence', 'ready_for_review', 'pending',
                '同组重复候选，与本批 xdup-0254 的“云冈石窟”为同一处异写；既有新建条已完整覆盖候选内容，提交 no_delta 判断')
            row(c, 'ready_for_review', 'approved', 'approved',
                f'canonical 候选语义复读完成，批准 no_delta：{tref} 已完整覆盖本组两册候选（田自秉“六朝著名石窟”与 2016“北魏平城、犍陀罗风格”均已并入）')
            row(c, 'approved', 'no_delta', 'approved',
                f'{tref} 已完整覆盖本组候选内容，无需另行写回；判定 no_delta', tref)
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
