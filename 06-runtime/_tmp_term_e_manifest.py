import json
from pathlib import Path

PKG = Path('06-runtime/automation/2026-10-25-term-doc2-batch-e')
mapping = json.load(open(PKG / 'canonical-mapping.json', encoding='utf-8'))
groups = sorted(mapping)
canon = [{'group_id': g, 'entity': mapping[g]['entity'], 'target_ref': mapping[g]['target_ref'],
          'canonical_candidate': mapping[g]['canonical_candidate_id'], 'action': mapping[g]['action']} for g in groups]
created = [mapping[g]['target_ref'] for g in groups if mapping[g]['action'] == 'create']
m = {
 'work_package': '2026-10-25-term-doc2-batch-e',
 'goal': '处理 term 类型 doc_count=2 重复组第五批（末批）26 组（xdup-0444—xdup-0470，缺 0446 已关闭）：新建 25 个 term KU；鸡头壶／天鸡壶组 update 既有 tianji-hu.md。',
 'status': 'applied',
 'created_at': '2026-10-25T17:10:00+08:00',
 'updated_at': '2026-10-25T17:45:00+08:00',
 'inputs': {
  'candidate_index_before_apply_fingerprint': 'sha256:a35d7454624549197c1c60622ff9d9a2c5f71d37dcdd60f8bf5328c18e9cb913（7,235,061 B，5,339 行）',
  'duplicate_group_recall': '06-runtime/automation/2026-10-25-cross-source-candidate-consolidation/duplicate-groups.jsonl',
  'prior_batch': '06-runtime/automation/2026-10-25-term-doc2-batch-d/manifest.json',
  'source_scope': '前六册（Books 1-6）；Book 7 及以后按用户指示不启动'
 },
 'scope': {
  'group_rule': 'term 类型、doc_count=2、在 term-doc2-batch-d 关闭后按 group_id 升序的全部剩余 26 个未关闭组',
  'group_ids': groups, 'groups': 26, 'candidate_rows': 52,
  'canonical_candidates': 26, 'applied_canonical_candidates': 26, 'rejected_candidates': 26,
  'created_units': 25, 'updated_units': 1, 'no_delta_units': 0
 },
 'method': {
  'semantic_step': '逐组复读两册候选摘要，比较定义、年代、器形、工艺与分类口径；同实体重复候选只保留 canonical；对年代、分期、器形与用字冲突一律并列保留。',
  'canonical_rule': '按内容主责册次指定 canonical；两册信息互补时以信息量较大者为主，另一册要点补入正文并保留来源。',
  'decision_rule': '25 组 create；1 组 update（xdup-0468 鸡头壶／天鸡壶 → 既有 tianji-hu.md，补入田自秉 2010 的盘口壶源流、鸡头装饰化过程与唐代龙耳壶演变）。',
  'state_chain': 'needs_evidence -> ready_for_review -> approved -> applied（26 个 canonical）；needs_evidence -> rejected（26 个 merged member）',
  'ledger_rows': 104, 'apply_plan_rows': 26
 },
 'outputs': {
  'apply_plan': '06-runtime/automation/2026-10-25-term-doc2-batch-e/apply-plan.jsonl',
  'candidate_decision_ledger': '06-runtime/automation/2026-10-25-term-doc2-batch-e/candidate-decision-ledger.jsonl',
  'canonical_mapping': '06-runtime/automation/2026-10-25-term-doc2-batch-e/canonical-mapping.json',
  'created_units': created,
  'updated_units': ['04-knowledge/units/terms/tianji-hu.md'],
  'summary': '06-runtime/automation/2026-10-25-term-doc2-batch-e/summary.md'
 },
 'canonical_mapping': canon,
 'validation': {
  'candidate_index_after': {
   'sha256': 'sha256:63ed6cf3d6b4f0f1322af9e286f33f9fe20715ad52c4cd63c7b80c65c11caebb',
   'bytes': 7243359, 'lines': 5339,
   'state_counts': {'applied': 329, 'no_delta': 11, 'rejected': 628, 'needs_evidence': 4371},
   'lifecycle_counts': {'active': 4371, 'terminal': 968}
  },
  'apply_plan_hashes': {'checked': 26, 'matched': 26},
  'content_quality': {'units': 336, 'findings': 0},
  'repo_audit': {'issues': 0, 'evidence_refs': '336/336'},
  'pre_commit': {'rule_drift': 0},
  'sync_closure': {'steps': 19, 'tests': '250 passed + 16 subtests'},
  'duplicate_closure': {'term_doc2_total': 136, 'term_doc2_closed': 136, 'term_doc2_open': 0,
                        'term_doc2_open_members': 0, 'person_doc2_open': 0},
  'notes': 'term 类型 doc_count=2 重复组已全部关闭。本批并列冲突：盘为圆形浅腹／虢季子白盘为长方形；盛食器用字盌／盨；齐家文化“约龙山、与夏相始终”／“新石器中晚期”；褒衣博带世俗服饰义／云冈佛像服饰义。'
 }
}
json.dump(m, open(PKG / 'manifest.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('manifest written', len(groups))
