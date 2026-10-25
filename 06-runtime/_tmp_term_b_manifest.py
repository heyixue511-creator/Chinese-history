import json
from pathlib import Path

PKG = Path('06-runtime/automation/2026-10-25-term-doc2-batch-b')
mapping = json.load(open(PKG / 'canonical-mapping.json', encoding='utf-8'))
groups = sorted(mapping)
canon = [{'group_id': g, 'entity': mapping[g]['entity'], 'target_ref': mapping[g]['target_ref'],
          'canonical_candidate': mapping[g]['canonical_candidate_id'], 'action': 'create'} for g in groups]
m = {
 'work_package': '2026-10-25-term-doc2-batch-b',
 'goal': '处理 term 类型 doc_count=2 重复组第二批 27 组（xdup-0359—xdup-0389，54 个候选）：全部新建 term KU，每组一个 canonical applied、另一成员 rejected。',
 'status': 'applied',
 'created_at': '2026-10-25T22:55:00+08:00',
 'updated_at': '2026-10-25T23:15:00+08:00',
 'inputs': {
  'candidate_index_before_apply_fingerprint': 'sha256:e82bd95f3ceb73186b800708d1052e8f45ec27ff3093bb67063f2d8bf92aca82（7,209,591 B，5,339 行）',
  'duplicate_group_recall': '06-runtime/automation/2026-10-25-cross-source-candidate-consolidation/duplicate-groups.jsonl',
  'prior_batch': '06-runtime/automation/2026-10-25-term-doc2-batch-a/manifest.json',
  'source_scope': '前六册（Books 1-6）；Book 7 及以后按用户指示不启动'
 },
 'scope': {
  'group_rule': 'term 类型、doc_count=2、在 term-doc2-batch-a 关闭后按 group_id 升序的前 27 个未关闭组',
  'group_ids': groups, 'groups': 27, 'candidate_rows': 54,
  'canonical_candidates': 27, 'applied_canonical_candidates': 27, 'rejected_candidates': 27,
  'created_units': 27, 'updated_units': 0, 'no_delta_units': 0
 },
 'method': {
  'semantic_step': '逐组复读两册候选摘要，比较定义、年代、器形、工艺与分类口径；同实体重复候选只保留 canonical，另一成员按内容已并 rejected。',
  'canonical_rule': '按内容主责册次指定 canonical；两册各有独立信息时以信息量较大者为主，另一册要点补入正文并保留来源。',
  'decision_rule': '27 组全部 create：圆领袍衫、塑料、士、壮锦、多子盒、天鸡壶、夹缬、妆花、宋体字、宋版书、官窑、官营手工业、小篆、工艺美术、带柄工具、席、帷帐、开片、影青、忍冬纹、戗金、披帛、提花机、搪瓷、敦、文质、斗拱。',
  'state_chain': 'needs_evidence -> ready_for_review -> approved -> applied（27 个 canonical）；needs_evidence -> rejected（27 个 merged member）',
  'ledger_rows': 108, 'apply_plan_rows': 27
 },
 'outputs': {
  'apply_plan': '06-runtime/automation/2026-10-25-term-doc2-batch-b/apply-plan.jsonl',
  'candidate_decision_ledger': '06-runtime/automation/2026-10-25-term-doc2-batch-b/candidate-decision-ledger.jsonl',
  'canonical_mapping': '06-runtime/automation/2026-10-25-term-doc2-batch-b/canonical-mapping.json',
  'created_units': [mapping[g]['target_ref'] for g in groups],
  'summary': '06-runtime/automation/2026-10-25-term-doc2-batch-b/summary.md'
 },
 'canonical_mapping': canon,
 'validation': {
  'candidate_index_after': {
   'sha256': 'sha256:1b9c33cd0e9cfc8c69a773dbb2a945f0a352f8274641410aaa4bb0d55adf5815',
   'bytes': 7217974, 'lines': 5339,
   'state_counts': {'applied': 250, 'no_delta': 10, 'rejected': 548, 'needs_evidence': 4531},
   'lifecycle_counts': {'active': 4531, 'terminal': 808}
  },
  'apply_plan_hashes': {'checked': 27, 'matched': 27},
  'content_quality': {'units': 258, 'findings': 0},
  'repo_audit': {'issues': 0, 'evidence_refs': '258/258'},
  'pre_commit': {'rule_drift': 0},
  'duplicate_closure': {'term_doc2_total': 136, 'term_doc2_closed': 56, 'term_doc2_open': 80,
                        'term_doc2_open_members': 160, 'person_doc2_open': 0},
  'notes': '多子盒三义（多格食器／宋瓷盒／汉漆套盒）、敦的功能两说（盛食器／炖肉器）、戗金的创始时代（宋／秦汉）均并列保留，未裁定。'
 }
}
json.dump(m, open(PKG / 'manifest.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('manifest written', len(groups))
