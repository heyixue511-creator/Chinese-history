import json
from pathlib import Path

PKG = Path('06-runtime/automation/2026-10-25-term-doc2-batch-c')
mapping = json.load(open(PKG / 'canonical-mapping.json', encoding='utf-8'))
groups = sorted(mapping)
canon = [{'group_id': g, 'entity': mapping[g]['entity'], 'target_ref': mapping[g]['target_ref'],
          'canonical_candidate': mapping[g]['canonical_candidate_id'], 'action': mapping[g]['action']} for g in groups]
created = [mapping[g]['target_ref'] for g in groups if mapping[g]['action'] == 'create']
m = {
 'work_package': '2026-10-25-term-doc2-batch-c',
 'goal': '处理 term 类型 doc_count=2 重复组第三批 27 组（xdup-0390—xdup-0416，54 个候选）：新建 26 个 term KU；百工制度组判定 no_delta，并入既有 baigong.md。',
 'status': 'applied',
 'created_at': '2026-10-25T23:30:00+08:00',
 'updated_at': '2026-10-25T23:50:00+08:00',
 'inputs': {
  'candidate_index_before_apply_fingerprint': 'sha256:1b9c33cd0e9cfc8c69a773dbb2a945f0a352f8274641410aaa4bb0d55adf5815（7,217,974 B，5,339 行）',
  'duplicate_group_recall': '06-runtime/automation/2026-10-25-cross-source-candidate-consolidation/duplicate-groups.jsonl',
  'prior_batch': '06-runtime/automation/2026-10-25-term-doc2-batch-b/manifest.json',
  'source_scope': '前六册（Books 1-6）；Book 7 及以后按用户指示不启动'
 },
 'scope': {
  'group_rule': 'term 类型、doc_count=2、在 term-doc2-batch-b 关闭后按 group_id 升序的前 27 个未关闭组',
  'group_ids': groups, 'groups': 27, 'candidate_rows': 54,
  'canonical_candidates': 27, 'applied_canonical_candidates': 26, 'rejected_candidates': 27,
  'created_units': 26, 'updated_units': 0, 'no_delta_units': 1
 },
 'method': {
  'semantic_step': '逐组复读两册候选摘要，比较定义、年代、器形、工艺与分类口径；同实体重复候选只保留 canonical。对已有同名 KU 的组先核对既有正文覆盖范围。',
  'canonical_rule': '按内容主责册次指定 canonical；两册信息互补时以信息量较大者为主，另一册要点补入正文并保留来源。',
  'decision_rule': '26 组 create；1 组 no_delta（xdup-0409 百工制度 → 既有 terms/baigong.md 已含别名、高丰 L947/L949-L953 与李立新 L827 的完整覆盖）。',
  'state_chain': 'needs_evidence -> ready_for_review -> approved -> applied（26 个 canonical）；needs_evidence -> ready_for_review -> approved -> no_delta（1 个 canonical）；needs_evidence -> rejected（27 个 merged member）',
  'ledger_rows': 108, 'apply_plan_rows': 26
 },
 'outputs': {
  'apply_plan': '06-runtime/automation/2026-10-25-term-doc2-batch-c/apply-plan.jsonl',
  'candidate_decision_ledger': '06-runtime/automation/2026-10-25-term-doc2-batch-c/candidate-decision-ledger.jsonl',
  'canonical_mapping': '06-runtime/automation/2026-10-25-term-doc2-batch-c/canonical-mapping.json',
  'created_units': created,
  'summary': '06-runtime/automation/2026-10-25-term-doc2-batch-c/summary.md'
 },
 'canonical_mapping': canon,
 'validation': {
  'candidate_index_after': {
   'sha256': 'sha256:a7b08640b80f63eac95101a04dbeeb9b5ad8f1d9f2e4d9e41006668d02b9d40b',
   'bytes': 7226649, 'lines': 5339,
   'state_counts': {'applied': 276, 'no_delta': 11, 'rejected': 575, 'needs_evidence': 4477},
   'lifecycle_counts': {'active': 4477, 'terminal': 862}
  },
  'apply_plan_hashes': {'checked': 26, 'matched': 26},
  'content_quality': {'units': 284, 'findings': 0},
  'repo_audit': {'issues': 0, 'evidence_refs': '284/284'},
  'pre_commit': {'rule_drift': 0},
  'duplicate_closure': {'term_doc2_total': 136, 'term_doc2_closed': 83, 'term_doc2_open': 53,
                        'term_doc2_open_members': 106, 'person_doc2_open': 0},
  'notes': '多子盒式的三义并列方法在本批继续用于：沙船创制时代（唐／宋）、犀皮创始期（宋／东吴）、玉壶春瓶时代（宋／元），均并列保留未裁定。'
 }
}
json.dump(m, open(PKG / 'manifest.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('manifest written', len(groups))
