import json, hashlib
from pathlib import Path

PKG = Path('06-runtime/automation/2026-10-25-place-doc2-batch')
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
        before_ok = r['before']['sha256'].startswith('sha256:') and r['before']['bytes'] == 3696 and r['before']['lines'] == 85
    if 'sha256:' + hashlib.sha256(b).hexdigest() == r['after_sha256'] and len(b) == r['bytes'] and t.count('\n') == r['lines'] and before_ok:
        ok += 1

mapping = json.load(open(PKG / 'canonical-mapping.json', encoding='utf-8'))
created = [v['target_ref'] for v in mapping.values() if v['action'] == 'create']
updated = [v['target_ref'] for v in mapping.values() if v['action'] == 'update']
no_delta = [v['target_ref'] for v in mapping.values() if v['action'] == 'no_delta']
pub_total, pub_closed = stat('publication', 2)
work_total, work_closed = stat('work', 2)
inst_total, inst_closed = stat('institution', 2)
place_total, place_closed = stat('place', 2)
proc_total, proc_closed = stat('procedure', 2)
event_total, event_closed = stat('event', 2)

m = {
 'work_package': '2026-10-25-place-doc2-batch',
 'goal': '处理 place 类型 doc_count=2 全部 25 组（xdup-0252—xdup-0276，50 个候选）：23 组 create 新建 23 个 place KU，1 组（哥窑）update 既有 `terms/ge-yao.md`，1 组（云岗石窟）no_delta 并入同批新建的 `places/yungang-shiku.md`。',
 'status': 'applied',
 'created_at': '2026-10-25T22:05:00+08:00',
 'updated_at': '2026-10-25T22:40:00+08:00',
 'inputs': {
  'candidate_index_before_apply_fingerprint': '5,339 行；place 批次前状态为 applied 451 / no_delta 14 / rejected 751 / needs_evidence 4123',
  'duplicate_group_recall': '06-runtime/automation/2026-10-25-cross-source-candidate-consolidation/duplicate-groups.jsonl',
  'prior_batch': '06-runtime/automation/2026-10-25-institution-doc2-batch-a/manifest.json',
  'source_scope': '前六册（Books 1-6）；Book 7 及以后按用户指示不启动'
 },
 'scope': {
  'group_rule': 'place 类型、doc_count=2 的全部未关闭组（共 25 组）',
  'group_ids': sorted(mapping), 'groups': 25, 'candidate_rows': 50,
  'canonical_candidates': 25, 'applied_canonical_candidates': 24, 'no_delta_canonical_candidates': 1,
  'rejected_candidates': 25,
  'created_units': 23, 'updated_units': 1, 'no_delta_units': 1
 },
 'method': {
  'semantic_step': '逐组复读两册候选摘要与 F 字段，比较遗址/窑址/都城的性质、地点、年代、规模、器物与工艺特征；同实体重复候选只保留 canonical，另一册要点补入正文并保留来源。',
  'canonical_rule': '按信息量较大且正文可证者指定 canonical：赵农 9 组、田自秉 6 组、夏燕靖 2009 4 组、夏燕靖 2016 1 组、李立新 1 组、高丰 1 组、2010+2016 异写 1 组。',
  'update_rule': 'xdup-0261「哥窑」与既有 `terms/ge-yao.md` 为同一实体，且窑址未发现、不宜作 place：以 2009xy cand-04-91 为 canonical 执行 update，补入章生一、章生二兄弟双窑传说、传世宫藏哥窑瓷实为南宋修内司官窑烧制的专家说、失透乳浊釉与灰青釉色，以及赵农“在浙江龙泉、属龙泉窑系、南宋常为官窑产品、胎质暗黑、利用收缩差成开片”；source_count 2→4，version 1→2，title 与 type 不变。',
  'heterogeneity_rule': 'xdup-0254「云冈石窟」与 xdup-0255「云岗石窟」为同一处异写，按《梦梁录／梦粱录》先例合为一条：0254 两册为 canonical 新建 `places/yungang-shiku.md`，0255 两册判 no_delta 指向同文件，“云岗石窟”保留为 alias；田自秉“六朝著名石窟”与 2016“北魏平城、犍陀罗风格”已并入该条。',
  'decision_rule': '23 组 create；1 组 update；1 组 no_delta。',
  'state_chain': 'needs_evidence -> ready_for_review -> approved -> applied（23 create）/ applied（1 update）；approved -> no_delta（1 组 canonical）；needs_evidence -> rejected（25 个 merged member）',
  'ledger_rows': 100, 'apply_plan_rows': 24
 },
 'outputs': {
  'apply_plan': '06-runtime/automation/2026-10-25-place-doc2-batch/apply-plan.jsonl',
  'candidate_decision_ledger': '06-runtime/automation/2026-10-25-place-doc2-batch/candidate-decision-ledger.jsonl',
  'canonical_mapping': '06-runtime/automation/2026-10-25-place-doc2-batch/canonical-mapping.json',
  'created_units': created,
  'updated_units': updated,
  'no_delta_units': no_delta,
  'summary': '06-runtime/automation/2026-10-25-place-doc2-batch/summary.md'
 },
 'validation': {
  'candidate_index_after': {
   'sha256': idx_fp, 'bytes': len(raw), 'lines': text.count('\n'),
   'state_counts': states, 'lifecycle_counts': life
  },
  'apply_plan_hashes': {'checked': len(plan), 'matched': ok},
  'content_quality': {'units': 480, 'findings': 0},
  'repo_audit': {'issues': 0, 'evidence_refs': '480/480', 'cross_type_disambiguation': '6/6（3 组）'},
  'pre_commit': {'rule_drift': 0},
  'duplicate_closure': {'publication_doc2_open': pub_total - pub_closed, 'work_doc2_open': work_total - work_closed,
                        'institution_doc2_open': inst_total - inst_closed,
                        'place_doc2_total': place_total, 'place_doc2_closed': place_closed,
                        'place_doc2_open': place_total - place_closed,
                        'procedure_doc2_open': proc_total - proc_closed,
                        'event_doc2_open': event_total - event_closed},
  'notes': '本批并列：建窑地点（福建建阳／建瓯、水吉）；瓯窑时代（唐／六朝）；宜兴时代（清代／明清）；马王堆衣物件数（50余件／58件）；吉州窑时代（南宋／宋代）；云冈石窟窟数与各册提名不一。2016 妇好墓“4件”与所列三器名不符，照录不改。'
 }
}
json.dump(m, open(PKG / 'manifest.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('manifest ok', 'plan', len(plan), 'hashes', ok, 'states', states, 'place', place_total, place_closed, 'proc', proc_total, proc_closed, 'event', event_total, event_closed)
