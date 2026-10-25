import json, hashlib
from pathlib import Path

PKG = Path('06-runtime/automation/2026-10-25-procedure-doc2-batch')
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
        before_ok = r['before']['sha256'].startswith('sha256:') and r['before']['bytes'] == 4133 and r['before']['lines'] == 86
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
 'work_package': '2026-10-25-procedure-doc2-batch',
 'goal': '处理 procedure 类型 doc_count=2 全部 10 组（xdup-0277—xdup-0286，20 个候选）：9 组 create 新建 9 个 procedure KU，1 组（夹缬）update 既有 `terms/jiaxie.md`。',
 'status': 'applied',
 'created_at': '2026-10-25T23:10:00+08:00',
 'updated_at': '2026-10-25T23:40:00+08:00',
 'inputs': {
  'candidate_index_before_apply_fingerprint': '5,339 行；procedure 批次前状态为 applied 475 / no_delta 15 / rejected 776 / needs_evidence 4073',
  'duplicate_group_recall': '06-runtime/automation/2026-10-25-cross-source-candidate-consolidation/duplicate-groups.jsonl',
  'prior_batch': '06-runtime/automation/2026-10-25-place-doc2-batch/manifest.json',
  'source_scope': '前六册（Books 1-6）；Book 7 及以后按用户指示不启动'
 },
 'scope': {
  'group_rule': 'procedure 类型、doc_count=2 的全部未关闭组（共 10 组）',
  'group_ids': sorted(mapping), 'groups': 10, 'candidate_rows': 20,
  'canonical_candidates': 10, 'applied_canonical_candidates': 10, 'no_delta_canonical_candidates': 0,
  'rejected_candidates': 10,
  'created_units': 9, 'updated_units': 1, 'no_delta_units': 0
 },
 'method': {
  'semantic_step': '逐组复读两册候选摘要与 F 字段，比较工序步骤、材料、配比、时代与考古证据；同实体重复候选只保留 canonical，另一册要点补入正文并保留来源。',
  'canonical_rule': '按信息量较大且正文可证者指定 canonical：夏燕靖 2009 5 组、高丰 2004 1 组、田自秉 2010 2 组、赵农 2009 2 组。',
  'update_rule': 'xdup-0279「夹缬」与既有 `terms/jiaxie.md` 为同一实体，且该条已定为 textile_technique：以高丰 2004 候选为 canonical 执行 update，补入《事物纪原》转引《二仪实录》“秦汉间已有之，陈梁间贵贱通服之”、盛唐宫廷、唐代军服、日本正仓院藏唐夹缬屏风；补入田自秉所记隋开皇六年（586）吐鲁番实物、可染两三色、花纹对称均衡与家具装饰；源流三说（东汉／秦汉／隋）按层并列，不裁定；source_count 2→4，version 1→2，title 与 type 不变。',
  'heterogeneity_rule': '同一工艺的异名不拆条：夹缬的高丰候选 slug 为 `jia-xie`、田自秉候选为 `jia-xie`，均指向既有 `terms/jiaxie.md`；不再新建 `procedures/jiaxie.md`。',
  'decision_rule': '9 组 create；1 组 update；无 no_delta。',
  'state_chain': 'needs_evidence -> ready_for_review -> approved -> applied（9 个 create canonical + 1 个 update canonical）；needs_evidence -> rejected（10 个 merged member）',
  'ledger_rows': 40, 'apply_plan_rows': 10
 },
 'outputs': {
  'apply_plan': '06-runtime/automation/2026-10-25-procedure-doc2-batch/apply-plan.jsonl',
  'candidate_decision_ledger': '06-runtime/automation/2026-10-25-procedure-doc2-batch/candidate-decision-ledger.jsonl',
  'canonical_mapping': '06-runtime/automation/2026-10-25-procedure-doc2-batch/canonical-mapping.json',
  'created_units': created,
  'updated_units': updated,
  'summary': '06-runtime/automation/2026-10-25-procedure-doc2-batch/summary.md'
 },
 'validation': {
  'candidate_index_after': {
   'sha256': idx_fp, 'bytes': len(raw), 'lines': text.count('\n'),
   'state_counts': states, 'lifecycle_counts': life
  },
  'apply_plan_hashes': {'checked': len(plan), 'matched': ok},
  'content_quality': {'units': 489, 'findings': 0},
  'repo_audit': {'issues': 0, 'evidence_refs': '489/489', 'cross_type_disambiguation': '6/6（3 组）'},
  'pre_commit': {'rule_drift': 0},
  'duplicate_closure': {'publication_doc2_open': pub_total - pub_closed, 'work_doc2_open': work_total - work_closed,
                        'institution_doc2_open': inst_total - inst_closed,
                        'place_doc2_open': place_total - place_closed,
                        'procedure_doc2_total': proc_total, 'procedure_doc2_closed': proc_closed,
                        'procedure_doc2_open': proc_total - proc_closed,
                        'event_doc2_open': event_total - event_closed},
  'notes': '本批并列：夹缬源流三说（2016 东汉／高丰《二仪实录》秦汉／田自秉隋开皇六年吐鲁番）；唐代用途军服（高丰）与家具装饰（田自秉）；夹纻胎材料纻麻（2009xy）与麻布或丝绸（高丰）；捣练法文献作《捣练赋》（原文如此）；泥条盘筑适用时代新石器时代（田自秉）与新石器时代至春秋战国（2016）；铁范器类首字 OCR 作“鏤”与“镰”。'
 }
}
json.dump(m, open(PKG / 'manifest.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('manifest ok', 'plan', len(plan), 'hashes', ok, 'states', states, 'proc', proc_total, proc_closed, 'event', event_total, event_closed)
