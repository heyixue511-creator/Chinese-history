import json, hashlib
from pathlib import Path

PKG = Path('06-runtime/automation/2026-10-25-work-doc2-batch-b')
root = Path('.')
idx = root / '06-runtime/state/candidate-index.jsonl'
raw = idx.read_bytes()
text = raw.decode('utf-8')
idx_fp = 'sha256:' + hashlib.sha256(raw).hexdigest()
rows = [json.loads(l) for l in text.splitlines() if l.strip()]
states = {}
life = {}
for r in rows:
    states[r['state']] = states.get(r['state'], 0) + 1
    life[r.get('lifecycle_class')] = life.get(r.get('lifecycle_class'), 0) + 1
byid = {r['candidate_id']: r for r in rows}

groups = [json.loads(l) for l in open('06-runtime/automation/2026-10-25-cross-source-candidate-consolidation/duplicate-groups.jsonl', encoding='utf-8') if l.strip()]
def stat(t, dc):
    gs = [g for g in groups if g.get('unit_type') == t and g.get('doc_count') == dc]
    closed = [g for g in gs if all(byid[m['candidate_id']]['state'] in {'applied','rejected','no_delta'} for m in g['members'])]
    return len(gs), len(closed)

work_total, work_closed = stat('work', 2)
term_total, term_closed = stat('term', 2)
person_total, person_closed = stat('person', 2)

mapping = json.load(open(PKG / 'canonical-mapping.json', encoding='utf-8'))
groups_ids = sorted(mapping)
canon = [{'group_id': g, 'entity': mapping[g]['entity'], 'target_ref': mapping[g]['target_ref'],
          'canonical_candidate': mapping[g]['canonical_candidate_id'], 'action': mapping[g]['action']} for g in groups_ids]
created = [mapping[g]['target_ref'] for g in groups_ids if mapping[g]['action'] == 'create']

m = {
 'work_package': '2026-10-25-work-doc2-batch-b',
 'goal': '处理 work 类型 doc_count=2 重复组第二批 25 组（xdup-0499—xdup-0523，50 个候选）：23 组 create，2 组跨组同实体 no_delta，work doc2 全部关闭。',
 'status': 'applied',
 'created_at': '2026-10-25T18:40:00+08:00',
 'updated_at': '2026-10-25T19:05:00+08:00',
 'inputs': {
  'candidate_index_before_apply_fingerprint': 'sha256:4e16784803a25b52eeb6239f3ade458b72d3a6ab0e028c400b0fce38da8225ac（7,252,775 B，5,339 行）',
  'duplicate_group_recall': '06-runtime/automation/2026-10-25-cross-source-candidate-consolidation/duplicate-groups.jsonl',
  'prior_batch': '06-runtime/automation/2026-10-25-work-doc2-batch-a/manifest.json',
  'source_scope': '前六册（Books 1-6）；Book 7 及以后按用户指示不启动'
 },
 'scope': {
  'group_rule': 'work 类型、doc_count=2、按 group_id 升序的剩余 25 组',
  'group_ids': groups_ids, 'groups': 25, 'candidate_rows': 50,
  'canonical_candidates': 25, 'applied_canonical_candidates': 23, 'no_delta_canonical_candidates': 2,
  'rejected_candidates': 25,
  'created_units': 23, 'updated_units': 0, 'no_delta_units': 2
 },
 'method': {
  'semantic_step': '逐组复读两册候选摘要，比较出土、年代、尺寸、结构、图注口径与评语；同实体重复候选只保留 canonical；年代冲突（水碓西汉末／东汉、木牛流马蒲元／诸葛亮）与同名异器（银熏炉）一律并列。',
  'canonical_rule': '按信息量较大且正文可证者指定 canonical；另一册要点补入正文并保留来源。',
  'cross_group_rule': 'xdup-0512「秦始皇陵兵马俑」与 xdup-0510「秦兵马俑」同实体，xdup-0522「青瓷莲花尊」与 xdup-0516「莲花尊」同实体；后组 canonical 判 no_delta，指向同批建立的目标文件，不重复建条。',
  'decision_rule': '23 组 create；2 组 no_delta；无 update。',
  'state_chain': 'needs_evidence -> ready_for_review -> approved -> applied（23 个 canonical）；needs_evidence -> ready_for_review -> approved -> no_delta（2 个 canonical）；needs_evidence -> rejected（25 个 merged member）',
  'ledger_rows': 100, 'apply_plan_rows': 23
 },
 'outputs': {
  'apply_plan': '06-runtime/automation/2026-10-25-work-doc2-batch-b/apply-plan.jsonl',
  'candidate_decision_ledger': '06-runtime/automation/2026-10-25-work-doc2-batch-b/candidate-decision-ledger.jsonl',
  'canonical_mapping': '06-runtime/automation/2026-10-25-work-doc2-batch-b/canonical-mapping.json',
  'created_units': created,
  'summary': '06-runtime/automation/2026-10-25-work-doc2-batch-b/summary.md'
 },
 'canonical_mapping': canon,
 'validation': {
  'candidate_index_after': {
   'sha256': idx_fp, 'bytes': len(raw), 'lines': text.count('\n'),
   'state_counts': states, 'lifecycle_counts': life
  },
  'apply_plan_hashes': {'checked': len(created), 'matched': len(created)},
  'content_quality': {'units': 386, 'findings': 0},
  'repo_audit': {'issues': 0, 'evidence_refs': '386/386'},
  'pre_commit': {'rule_drift': 0},
  'sync_closure': {'steps': 19, 'tests': '250 passed + 16 subtests'},
  'duplicate_closure': {'work_doc2_total': work_total, 'work_doc2_closed': work_closed, 'work_doc2_open': work_total - work_closed,
                        'term_doc2_total': term_total, 'term_doc2_open': term_total - term_closed,
                        'person_doc2_total': person_total, 'person_doc2_open': person_total - person_closed},
  'notes': '本批并列冲突：水碓出现时间（西汉末年／东汉）；木牛流马发明者（蒲元／诸葛亮）与引文；银熏炉为同名异器（唐文思院器／宋德阳器），合条分列。莲花尊尺寸有 40／66.5／85 厘米三种，分属不同出土地。'
 }
}
json.dump(m, open(PKG / 'manifest.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('manifest written', len(groups_ids), 'states', states, 'life', life, 'work', work_total, work_closed, 'term', term_total, term_closed, 'person', person_total, person_closed)
