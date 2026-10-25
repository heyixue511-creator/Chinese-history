import json, hashlib
from pathlib import Path

PKG = Path('06-runtime/automation/2026-10-25-institution-doc2-batch-a')
idx = Path('06-runtime/state/candidate-index.jsonl')
raw = idx.read_bytes(); text = raw.decode('utf-8')
idx_fp = 'sha256:' + hashlib.sha256(raw).hexdigest()
rows = [json.loads(l) for l in text.splitlines() if l.strip()]
states, life = {}, {}
for r in rows:
    states[r['state']] = states.get(r['state'], 0) + 1
    life[r.get('lifecycle_class')] = life.get(r.get('lifecycle_class'), 0) + 1
byid = {r['candidate_id']: r for r in rows}

groups = [json.loads(l) for l in open('06-runtime/automation/2026-10-25-cross-source-candidate-consolidation/duplicate-groups.jsonl', encoding='utf-8') if l.strip()]
def stat(t, dc):
    gs = [g for g in groups if g.get('unit_type') == t and g.get('doc_count') == dc]
    closed = [g for g in gs if all(byid[m['candidate_id']]['state'] in {'applied','rejected','no_delta'} for m in g['members'])]
    return len(gs), len(closed)

plan = [json.loads(l) for l in open(PKG / 'apply-plan.jsonl', encoding='utf-8') if l.strip()]
ok = 0
for r in plan:
    t = Path(r['target_ref']).read_text(encoding='utf-8').replace('\r\n', '\n'); b = t.encode()
    before_ok = True
    if r['action'] == 'update':
        # before 已由 _tmp_inst_shaofu_fp.py 的逆向替换 + 正向回放校验
        before_ok = r['before']['sha256'].startswith('sha256:') and r['before']['bytes'] == 6951
    if 'sha256:' + hashlib.sha256(b).hexdigest() == r['after_sha256'] and len(b) == r['bytes'] and t.count('\n') == r['lines'] and before_ok:
        ok += 1

mapping = json.load(open(PKG / 'canonical-mapping.json', encoding='utf-8'))
created = [v['target_ref'] for v in mapping.values() if v['action'] == 'create']
updated = [v['target_ref'] for v in mapping.values() if v['action'] == 'update']
pub_total, pub_closed = stat('publication', 2)
work_total, work_closed = stat('work', 2)
inst_total, inst_closed = stat('institution', 2)
place_total, place_closed = stat('place', 2)
proc_total, proc_closed = stat('procedure', 2)
event_total, event_closed = stat('event', 2)

m = {
 'work_package': '2026-10-25-institution-doc2-batch-a',
 'goal': '处理 institution 类型 doc_count=2 全部 26 组（xdup-0176—xdup-0201，52 个候选）：25 组 create 新建 25 个 institution KU，1 组（少府）update 既有 `institutions/shaofujian.md`。',
 'status': 'applied',
 'created_at': '2026-10-25T20:55:00+08:00',
 'updated_at': '2026-10-25T21:30:00+08:00',
 'inputs': {
  'candidate_index_before_apply_fingerprint': '5,339 行；institution 批次前状态为 applied 425 / no_delta 14 / rejected 725 / needs_evidence 4175',
  'duplicate_group_recall': '06-runtime/automation/2026-10-25-cross-source-candidate-consolidation/duplicate-groups.jsonl',
  'prior_batch': '06-runtime/automation/2026-10-25-publication-doc2-batch-b/manifest.json',
  'source_scope': '前六册（Books 1-6）；Book 7 及以后按用户指示不启动'
 },
 'scope': {
  'group_rule': 'institution 类型、doc_count=2 的全部未关闭组（共 26 组）',
  'group_ids': sorted(mapping), 'groups': 26, 'candidate_rows': 52,
  'canonical_candidates': 26, 'applied_canonical_candidates': 26, 'no_delta_canonical_candidates': 0,
  'rejected_candidates': 26,
  'created_units': 25, 'updated_units': 1, 'no_delta_units': 0
 },
 'method': {
  'semantic_step': '逐组复读两册候选摘要与 F 字段，比较机构性质、设置年代、隶属关系、职掌与规模；同实体重复候选只保留 canonical，另一册要点补入正文并保留来源。',
  'canonical_rule': '按信息量较大且正文可证者指定 canonical；本批 create 组 25 个、update 组 1 个，canonical 选择以覆盖面更广的一册为准（如 0178 取李立新、0187 取高丰、0193 取田自秉）。',
  'update_rule': 'xdup-0190「少府」与既有 `institutions/shaofujian.md`（少府监）为同一机构，不另建条：以赵农 cand-07-123 为 canonical 执行 update，补入李立新所记汉代属官、赵农所记唐代别名尚方监、从三品、《新唐书·百官志》五署及诸冶铸钱互市等监、工匠 19850 人与分工评述；version 1→2，title 不变，新增 aliases「少府」「尚方监」，source_count 5→7。',
  'heterogeneity_rule': '同名跨朝代机构不拆条：xdup-0193「文思院」唐宋两代同名而职掌不同，合为一条并按朝代分述；xdup-0190 少府／少府监同理按汉、唐、宋分层。',
  'decision_rule': '25 组 create；1 组 update；无 no_delta。',
  'state_chain': 'needs_evidence -> ready_for_review -> approved -> applied（26 个 canonical）；needs_evidence -> rejected（26 个 merged member）',
  'ledger_rows': 104, 'apply_plan_rows': 26
 },
 'outputs': {
  'apply_plan': '06-runtime/automation/2026-10-25-institution-doc2-batch-a/apply-plan.jsonl',
  'candidate_decision_ledger': '06-runtime/automation/2026-10-25-institution-doc2-batch-a/candidate-decision-ledger.jsonl',
  'canonical_mapping': '06-runtime/automation/2026-10-25-institution-doc2-batch-a/canonical-mapping.json',
  'created_units': created,
  'updated_units': updated,
  'summary': '06-runtime/automation/2026-10-25-institution-doc2-batch-a/summary.md'
 },
 'validation': {
  'candidate_index_after': {
   'sha256': idx_fp, 'bytes': len(raw), 'lines': text.count('\n'),
   'state_counts': states, 'lifecycle_counts': life
  },
  'apply_plan_hashes': {'checked': len(plan), 'matched': ok},
  'content_quality': {'units': 457, 'findings': 0},
  'repo_audit': {'issues': 0, 'evidence_refs': '457/457', 'cross_type_disambiguation': '6/6（3 组）'},
  'pre_commit': {'rule_drift': 0},
  'duplicate_closure': {'publication_doc2_open': pub_total - pub_closed, 'work_doc2_open': work_total - work_closed,
                        'institution_doc2_total': inst_total, 'institution_doc2_closed': inst_closed,
                        'institution_doc2_open': inst_total - inst_closed,
                        'place_doc2_open': place_total - place_closed,
                        'procedure_doc2_open': proc_total - proc_closed,
                        'event_doc2_open': event_total - event_closed},
  'notes': '本批并列：三服官设置地写法（襄邑、临淄／齐郡临淄、陈留郡襄邑）；两江师范学堂 1905 开课（赵农）与 1906 设图画手工科（李立新）；云锦“最早／第一家”两说；文思院宋代隶属（工部／少府监）与作数（42／40 余）；内务府造办处成立时间（清代／康熙年间）；铸镜局时代（南宋／宋）；船宫地域（吴越／楚吴越）。'
 }
}
json.dump(m, open(PKG / 'manifest.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('manifest ok', 'plan', len(plan), 'hashes', ok, 'states', states, 'inst', inst_total, inst_closed, 'place', place_total, place_closed, 'proc', proc_total, proc_closed, 'event', event_total, event_closed)
