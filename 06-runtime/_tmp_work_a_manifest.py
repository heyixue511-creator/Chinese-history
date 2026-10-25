import json
from pathlib import Path

PKG = Path('06-runtime/automation/2026-10-25-work-doc2-batch-a')
mapping = json.load(open(PKG / 'canonical-mapping.json', encoding='utf-8'))
groups = sorted(mapping)
canon = [{'group_id': g, 'entity': mapping[g]['entity'], 'target_ref': mapping[g]['target_ref'],
          'canonical_candidate': mapping[g]['canonical_candidate_id'], 'action': mapping[g]['action']} for g in groups]
created = [mapping[g]['target_ref'] for g in groups if mapping[g]['action'] == 'create']
m = {
 'work_package': '2026-10-25-work-doc2-batch-a',
 'goal': '处理 work 类型 doc_count=2 重复组第一批 27 组（xdup-0472—xdup-0498，54 个候选）：全部 create，新建 27 个 work KU。',
 'status': 'applied',
 'created_at': '2026-10-25T17:50:00+08:00',
 'updated_at': '2026-10-25T18:25:00+08:00',
 'inputs': {
  'candidate_index_before_apply_fingerprint': 'sha256:63ed6cf3d6b4f0f1322af9e286f33f9fe20715ad52c4cd63c7b80c65c11caebb（7,243,359 B，5,339 行）',
  'duplicate_group_recall': '06-runtime/automation/2026-10-25-cross-source-candidate-consolidation/duplicate-groups.jsonl',
  'prior_batch': '06-runtime/automation/2026-10-25-term-doc2-batch-e/manifest.json',
  'source_scope': '前六册（Books 1-6）；Book 7 及以后按用户指示不启动'
 },
 'scope': {
  'group_rule': 'work 类型、doc_count=2、按 group_id 升序的前 27 个未关闭组',
  'group_ids': groups, 'groups': 27, 'candidate_rows': 54,
  'canonical_candidates': 27, 'applied_canonical_candidates': 27, 'rejected_candidates': 27,
  'created_units': 27, 'updated_units': 0, 'no_delta_units': 0
 },
 'method': {
  'semantic_step': '逐组复读两册候选摘要，比较出土、年代、尺寸、结构与图注口径；同实体重复候选只保留 canonical；图注年代冲突与同册并存两说一律并列。',
  'canonical_rule': '按信息量较大且正文可证者指定 canonical；另一册要点补入正文并保留来源。仅有图注的条目按证据下限写作，不据器名补写形制。',
  'decision_rule': '27 组全部 create；无 update、无 no_delta。',
  'state_chain': 'needs_evidence -> ready_for_review -> approved -> applied（27 个 canonical）；needs_evidence -> rejected（27 个 merged member）',
  'ledger_rows': 108, 'apply_plan_rows': 27
 },
 'outputs': {
  'apply_plan': '06-runtime/automation/2026-10-25-work-doc2-batch-a/apply-plan.jsonl',
  'candidate_decision_ledger': '06-runtime/automation/2026-10-25-work-doc2-batch-a/candidate-decision-ledger.jsonl',
  'canonical_mapping': '06-runtime/automation/2026-10-25-work-doc2-batch-a/canonical-mapping.json',
  'created_units': created,
  'summary': '06-runtime/automation/2026-10-25-work-doc2-batch-a/summary.md'
 },
 'canonical_mapping': canon,
 'validation': {
  'candidate_index_after': {
   'sha256': 'sha256:4e16784803a25b52eeb6239f3ade458b72d3a6ab0e028c400b0fce38da8225ac',
   'bytes': 7252775, 'lines': 5339,
   'state_counts': {'applied': 356, 'no_delta': 11, 'rejected': 655, 'needs_evidence': 4317},
   'lifecycle_counts': {'active': 4317, 'terminal': 1022}
  },
  'apply_plan_hashes': {'checked': 27, 'matched': 27},
  'content_quality': {'units': 363, 'findings': 0},
  'repo_audit': {'issues': 0, 'evidence_refs': '363/363'},
  'pre_commit': {'rule_drift': 0},
  'sync_closure': {'steps': 19, 'tests': '250 passed + 16 subtests'},
  'duplicate_closure': {'work_doc2_total': 52, 'work_doc2_closed': 27, 'work_doc2_open': 25,
                        'term_doc2_open': 0, 'person_doc2_open': 0},
  'notes': '本批并列冲突：四羊方尊图注年代“商／西周”相反；偶方彝 2016 图注作“商周”而正文为妇好墓商代，且原文称 4 件仅列 3 名；四美图“金代／北宋末年”两说并存；大明宫“原为太极宫一处／原名永安宫”表述不同。'
 }
}
json.dump(m, open(PKG / 'manifest.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('manifest written', len(groups))
