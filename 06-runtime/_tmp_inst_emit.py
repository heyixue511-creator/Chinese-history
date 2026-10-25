import json, hashlib
from pathlib import Path

PKG = Path('06-runtime/automation/2026-10-25-institution-doc2-batch-a')
PKG.mkdir(parents=True, exist_ok=True)
gs = {}
for l in open('06-runtime/automation/2026-10-25-cross-source-candidate-consolidation/duplicate-groups.jsonl', encoding='utf-8'):
    if l.strip():
        g = json.loads(l); gs[g['group_id']] = g

# group -> (prefix, target) ; target is slug for create or relative path for update
M = {
 'xdup-0176': [('2009-zhaonong', 'sanfuguan')],
 'xdup-0177': [('2009-xiayanjing', 'shanghai-meishu-dianying-zhipianchang')],
 'xdup-0178': [('2011-lilixin', 'liangjiang-shifan-xuetang')],
 'xdup-0179': [('2016-xiayanjing', 'zhongguo-gongyi-meishu-xuehui')],
 'xdup-0180': [('2016-xiayanjing', 'zhongguo-gongyi-meishuguan')],
 'xdup-0181': [('2016-xiayanjing', 'zhongguo-meishuguan')],
 'xdup-0182': [('2009-xiayanjing', 'zhongtian-dianjichang')],
 'xdup-0183': [('2016-xiayanjing', 'zhongyang-gongyi-meishu-kexue-yanjiu-suo')],
 'xdup-0184': [('2016-xiayanjing', 'zhongyang-meishu-xueyuan')],
 'xdup-0185': [('2009-xiayanjing', 'yunjin-yanjiu-gongzuozu')],
 'xdup-0186': [('2009-xiayanjing', 'yaping-yishu-zhuangshi-gongsi')],
 'xdup-0187': [('2004-gaofeng', 'neiwufu-zaobanchu')],
 'xdup-0188': [('2016-xiayanjing', 'nanjing-yunjin-yanjiusuo')],
 'xdup-0189': [('2016-xiayanjing', 'shangwu-yinshuguan')],
 'xdup-0190': [('2009-zhaonong', 'institutions/shaofujian.md', 'update')],
 'xdup-0191': [('2011-lilixin', 'shangmei-tuananguan')],
 'xdup-0192': [('2011-lilixin', 'gugong-bowuyuan')],
 'xdup-0193': [('2010-tianzibing', 'wensiyuan')],
 'xdup-0194': [('2009-xiayanjing', 'jiangnan-zhizao-zongju')],
 'xdup-0195': [('2016-xiayanjing', 'jiguge')],
 'xdup-0196': [('2009-xiayanjing', 'shenxin-fangzhi-gongsi')],
 'xdup-0197': [('2016-xiayanjing', 'dier-qinggongyebu')],
 'xdup-0198': [('2016-xiayanjing', 'chuangong')],
 'xdup-0199': [('2016-xiayanjing', 'lunchuan-zhaoshangju')],
 'xdup-0200': [('2010-tianzibing', 'jinyin-zuofangyuan')],
 'xdup-0201': [('2010-tianzibing', 'zhujingju')],
}
DATE = '2026-10-25'
BEFORE_SHAOFU = {'sha256': 'sha256:0b9d23452e1903e1427ecf365de39c5c7fb9bd203542dbcb32e9a928cb91c037', 'bytes': 6951, 'lines': 116}

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
            tref = f'04-knowledge/units/institutions/{target}.md'
            row(c, 'needs_evidence', 'ready_for_review', 'pending', f'同组重复候选已回收，准备语义写回 {tref}')
            row(c, 'ready_for_review', 'approved', 'approved', f'canonical 候选六节复读完成，批准 exact change-set 写入 {tref}')
            row(c, 'approved', 'applied', 'approved', f'已按 exact change-set 写入 {tref}', tref)
            sha, by, ln = fp(tref)
            plan.append({'action': 'create', 'target_ref': tref, 'candidate_id': c, 'entity': title,
                         'before': None, 'after_sha256': sha, 'bytes': by, 'lines': ln,
                         'note': f'{gid} 两册来源合并建立 institution KU；六节结构与来源定位见候选摘要'})
            mapping[gid] = {'entity': title, 'target_ref': tref, 'canonical_candidate_id': c, 'action': 'create'}
        else:
            tref = '04-knowledge/units/' + target
            row(c, 'needs_evidence', 'ready_for_review', 'pending',
                f'既有 KU {tref} 已覆盖本组主体，核对缺口后准备 update')
            row(c, 'ready_for_review', 'approved', 'approved',
                f'复读确认 {tref} 缺汉代属官、唐代别名与《新唐书》职掌，批准 update')
            row(c, 'approved', 'applied', 'approved',
                f'已在 {tref} 增补汉代属官、唐代别名与品级、《新唐书·百官志》职掌、工匠 19850 人与分工评述，version 1→2', tref)
            sha, by, ln = fp(tref)
            plan.append({'action': 'update', 'target_ref': tref, 'candidate_id': c, 'entity': '少府监（少府）',
                         'before': BEFORE_SHAOFU, 'after_sha256': sha, 'bytes': by, 'lines': ln,
                         'note': '补入李立新所记汉代少府属官（尚方、考工室、若庐、东织西织、东园匠）与赵农所记唐代别名尚方监、从三品、《新唐书·百官志》五署及诸冶铸钱互市等监、工匠 19850 人、分工导致设计华丽富贵的评述；title 不变，增 aliases「少府」「尚方监」，工匠数由两说扩为三说并列。'})
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
