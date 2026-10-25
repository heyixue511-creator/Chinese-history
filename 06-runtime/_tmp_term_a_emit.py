import json, hashlib
from pathlib import Path

PKG = Path('06-runtime/automation/2026-10-25-term-doc2-batch-a')
PKG.mkdir(parents=True, exist_ok=True)
TERMS = Path('04-knowledge/units/terms')

idx = {}
for l in open('06-runtime/state/candidate-index.jsonl', encoding='utf-8'):
    if l.strip():
        r = json.loads(l); idx[r['candidate_id']] = r
gs = {}
for l in open('06-runtime/automation/2026-10-25-cross-source-candidate-consolidation/duplicate-groups.jsonl', encoding='utf-8'):
    if l.strip():
        g = json.loads(l); gs[g['group_id']] = g

# group -> (doc prefix of canonical, slug, action)
M = {
 'xdup-0137': ('2009-zhaonong', 'touguang-jing', 'create', 'cand-04-145'),
 'xdup-0333': ('2016-xiayanjing', 'dingcun-wenhua', 'create'),
 'xdup-0334': ('2009-xiayanjing', 'zhongguo-guyou-shi-jianzhu', 'create'),
 'xdup-0335': ('2009-xiayanjing', 'zhongshanzhuang', 'create'),
 'xdup-0336': ('2009-zhaonong', 'wudai-shiguo', 'create'),
 'xdup-0337': ('2009-zhaonong', 'wuda-mingyao', 'create'),
 'xdup-0338': ('2016-xiayanjing', 'wucai', 'create'),
 'xdup-0339': ('2016-xiayanjing', 'fangsongti', 'create'),
 'xdup-0340': ('2009-xiayanjing', 'zuopu', 'create'),
 'xdup-0341': ('2009-xiayanjing', 'pei-huang', 'create'),
 'xdup-0342': ('2004-gaofeng', 'zu-ritual-vessel', 'create'),
 'xdup-0343': ('2016-xiayanjing', 'yuanmouren', 'create'),
 'xdup-0344': ('2004-gaofeng', 'ping-ji', 'create'),
 'xdup-0345': ('2009-zhaonong', 'lieding-system', 'create'),
 'xdup-0346': ('2009-zhaonong', 'jianzhi', 'create'),
 'xdup-0347': ('2009-xiayanjing', 'baomaizhu', 'create'),
 'xdup-0348': ('2009-xiayanjing', 'huazhuangtu', 'create'),
 'xdup-0349': ('2009-xiayanjing', 'beijingren', 'create'),
 'xdup-0350': ('2010-tianzibing', 'yi-pourer', 'create'),
 'xdup-0351': ('2009-zhaonong', 'jianghu', 'create'),
 'xdup-0352': ('2009-xiayanjing', 'bandixue-shi-jianzhu', 'create'),
 'xdup-0353': ('2009-xiayanjing', 'nanjing-yunjin', 'create'),
 'xdup-0356': ('2004-gaofeng', 'jixiang-tu-an', 'create'),
 'xdup-0357': ('2010-tianzibing', 'ge-yao', 'create'),
 'xdup-0358': ('2009-xiayanjing', 'xikesuosi-ren', 'create'),
}
UPDATE = {'xdup-0355': ('2004-gaofeng', '04-knowledge/units/terms/proto-porcelain.md')}
FULLREJECT = {'xdup-0354': '原始瓷与既有 terms/proto-porcelain.md（原始青瓷）为同一器物概念，两册内容已由 xdup-0355 的 canonical 更新并入该 KU；本条不另立条目'}

DATE = '2026-10-25'
def fp(path):
    t = Path(path).read_text(encoding='utf-8').replace('\r\n', '\n')
    b = t.encode('utf-8')
    return 'sha256:' + hashlib.sha256(b).hexdigest(), len(b), t.count('\n')

ledger, plan, mapping = [], [], {}

def row(cid, exp, st, status, reason, target=None):
    d = {'candidate_id': cid, 'expected_state': exp, 'state': st,
         'decision': {'status': status, 'reason': reason, 'decided_by': 'Agent', 'decided_at': DATE},
         'updated_at': DATE}
    if target:
        d['target_ref'] = target
    ledger.append(d)

for gid, spec in M.items():
    prefix, slug, action = spec[:3]
    g = gs[gid]
    members = g['members']
    title = g['keys'].get('title')
    canon = [m for m in members if m['doc_id'].startswith(prefix)]
    if len(M[gid]) > 3:
        canon = [m for m in canon if m['candidate_id'].endswith(M[gid][3])]
    assert len(canon) == 1, (gid, canon)
    c = canon[0]['candidate_id']
    tref = f'04-knowledge/units/terms/{slug}.md'
    row(c, 'needs_evidence', 'ready_for_review', 'pending',
        f'同组重复候选已回收，准备语义写回 {tref}')
    row(c, 'ready_for_review', 'approved', 'approved',
        f'canonical 候选六节复读完成，批准 exact change-set 写入 {tref}')
    row(c, 'approved', 'applied', 'approved',
        f'已按 exact change-set 写入 {tref}', tref)
    for m in members:
        if m['candidate_id'] == c:
            continue
        row(m['candidate_id'], 'needs_evidence', 'rejected', 'rejected',
            f'同组重复候选，canonical 候选指向同一 entity「{title}」，内容已并入 {tref}，该候选不再单独写回', tref)
    sha, by, ln = fp(tref)
    plan.append({'action': 'create', 'target_ref': tref, 'candidate_id': c,
                 'entity': title, 'before': None, 'after_sha256': sha,
                 'bytes': by, 'lines': ln,
                 'note': f'{gid} 两册来源合并建立 term KU；六节结构与来源定位见候选摘要'})
    mapping[gid] = {'entity': title, 'target_ref': tref, 'canonical_candidate_id': c,
                    'action': 'create'}

for gid, (prefix, tref) in UPDATE.items():
    g = gs[gid]
    members = g['members']
    title = g['keys'].get('title')
    canon = [m for m in members if m['doc_id'].startswith(prefix)]
    assert len(canon) == 1, (gid, canon)
    c = canon[0]['candidate_id']
    row(c, 'needs_evidence', 'ready_for_review', 'pending',
        f'同组重复候选已回收，准备更新既有 {tref}')
    row(c, 'ready_for_review', 'approved', 'approved',
        f'canonical 候选复读完成，确认补正既有 KU 的「高丰无此词」判断，批准 exact change-set')
    row(c, 'approved', 'applied', 'approved',
        f'已按 exact change-set 更新 {tref}', tref)
    for m in members:
        if m['candidate_id'] == c:
            continue
        row(m['candidate_id'], 'needs_evidence', 'rejected', 'rejected',
            f'同组重复候选，内容已由 canonical 候选并入既有 {tref}（该册来源原有绑定保留），不再单独写回', tref)
    bsha, bby, bln = ('sha256:8c80f1baca9a065fe5c6389e889e95c09c8b66047840f043d592a775357b9c28', 9996, 120)
    asha, aby, aln = fp(tref)
    plan.append({'action': 'update', 'target_ref': tref, 'candidate_id': c,
                 'entity': title, 'before': {'sha256': bsha, 'bytes': bby, 'lines': bln},
                 'after_sha256': asha, 'bytes': aby, 'lines': aln,
                 'note': '补高丰 2004 L1246-L1258 的「原始瓷器」命名由来、《中国陶瓷史》过渡阶段定义与约 1000 多年过渡时长；修正正文「高丰一册全书无此词」误判，改为六册均有直接记载；aliases 增「原始瓷器（高丰用语）」；source_count 5→6，version 2→3，参考文献与验证状态同步'})
    mapping[gid] = {'entity': title, 'target_ref': tref, 'canonical_candidate_id': c,
                    'action': 'update'}

for gid, reason in FULLREJECT.items():
    g = gs[gid]
    for m in g['members']:
        row(m['candidate_id'], 'needs_evidence', 'rejected', 'rejected', reason,
            '04-knowledge/units/terms/proto-porcelain.md')
    mapping[gid] = {'entity': g['keys'].get('title'),
                    'target_ref': '04-knowledge/units/terms/proto-porcelain.md',
                    'canonical_candidate_id': None, 'action': 'merged_into_existing'}

with open(PKG / 'candidate-decision-ledger.jsonl', 'w', encoding='utf-8', newline='\n') as f:
    for r in ledger:
        f.write(json.dumps(r, ensure_ascii=False) + '\n')
with open(PKG / 'apply-plan.jsonl', 'w', encoding='utf-8', newline='\n') as f:
    for r in plan:
        f.write(json.dumps(r, ensure_ascii=False) + '\n')
json.dump(mapping, open(PKG / 'canonical-mapping.json', 'w', encoding='utf-8'),
          ensure_ascii=False, indent=1)
print('plan', len(plan), 'ledger', len(ledger), 'groups', len(mapping))
