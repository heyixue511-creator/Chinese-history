import json
from pathlib import Path

PKG = Path('06-runtime/automation/2026-10-25-term-doc2-batch-a')
mapping = json.load(open(PKG / 'canonical-mapping.json', encoding='utf-8'))
groups = sorted(mapping)
canon = [{'group_id': g, 'entity': mapping[g]['entity'], 'target_ref': mapping[g]['target_ref'],
          'canonical_candidate': mapping[g]['canonical_candidate_id'], 'action': mapping[g]['action']}
         for g in groups]
created = [mapping[g]['target_ref'] for g in groups if mapping[g]['action'] == 'create']
updated = [mapping[g]['target_ref'] for g in groups if mapping[g]['action'] == 'update']
rejected_groups = [g for g in groups if mapping[g]['action'] == 'merged_into_existing']

m = {
 'work_package': '2026-10-25-term-doc2-batch-a',
 'goal': '处理 term 类型 doc_count=2 重复组的前 27 组（xdup-0137、xdup-0333—xdup-0358，55 个候选）：新建 25 个 term KU，更新 1 个既有 KU（proto-porcelain），整组拒绝 1 组（原始瓷，并入既有条目），其余 29 个同组重复候选 rejected。',
 'status': 'applied',
 'created_at': '2026-10-25T22:10:00+08:00',
 'updated_at': '2026-10-25T22:40:00+08:00',
 'inputs': {
  'candidate_index_before_apply': '06-runtime/state/candidate-index.jsonl',
  'candidate_index_before_apply_fingerprint': 'sha256:f16a7b1cb03c7dbbdd6a38df36fe7c2e2735100882a412578fc29c2364fbb689（7,200,546 B，5,339 行）',
  'duplicate_group_recall': '06-runtime/automation/2026-10-25-cross-source-candidate-consolidation/duplicate-groups.jsonl',
  'prior_batch': '06-runtime/automation/2026-10-25-person-doc2-batch-m/manifest.json',
  'source_scope': '前六册（Books 1-6）；Book 7 及以后按用户指示不启动'
 },
 'scope': {
  'group_rule': 'term 类型、doc_count=2、按 group_id 升序的前 27 个未关闭组',
  'group_ids': groups,
  'groups': 27,
  'candidate_rows': 55,
  'canonical_candidates': 26,
  'applied_canonical_candidates': 26,
  'rejected_candidates': 29,
  'created_units': 25,
  'updated_units': 1,
  'no_delta_units': 0,
  'rejected_groups': rejected_groups
 },
 'method': {
  'semantic_step': '逐组复读候选摘要与来源定位，比较两册对同一概念的定义、年代、器形、工艺与分类口径；同实体的重复候选只保留 canonical，其余按「内容已并入」rejected。',
  'canonical_rule': '每组按内容主责册次指定 canonical 文档；同册多候选时按候选编号（如 xdup-0137 取 cand-04-145）指定，其余成员 rejected。update 组以提出该 slug 的高丰 2004 候选为 canonical。',
  'decision_rule': '25 组 create（透光镜、丁村文化、中国固有式建筑、中山装、五代十国、五大名窑、五彩、仿宋体、作铺、佩璜、俎、元谋人、凭几、列鼎制度、剪纸、包买主、化妆土、北京人、匜、匠户、半地穴式建筑、南京云锦、吉祥图案、哥窑、喜克索斯人）；1 组 update（原始瓷器 → 既有 terms/proto-porcelain.md，补高丰来源并修正「高丰全书无此词」误判）；1 组整组 rejected（原始瓷，与既有 KU 同实体）；0 组 no_delta。',
  'state_chain': 'needs_evidence -> ready_for_review -> approved -> applied（26 个 canonical）；needs_evidence -> rejected（29 个 merged member，含原始瓷整组 2 个）',
  'ledger_rows': 107,
  'apply_plan_rows': 26
 },
 'outputs': {
  'apply_plan': '06-runtime/automation/2026-10-25-term-doc2-batch-a/apply-plan.jsonl',
  'candidate_decision_ledger': '06-runtime/automation/2026-10-25-term-doc2-batch-a/candidate-decision-ledger.jsonl',
  'canonical_mapping': '06-runtime/automation/2026-10-25-term-doc2-batch-a/canonical-mapping.json',
  'created_units': created,
  'updated_units': updated,
  'summary': '06-runtime/automation/2026-10-25-term-doc2-batch-a/summary.md'
 },
 'canonical_mapping': canon,
 'validation': {
  'candidate_index_after': {
   'sha256': 'sha256:e82bd95f3ceb73186b800708d1052e8f45ec27ff3093bb67063f2d8bf92aca82',
   'bytes': 7209591,
   'lines': 5339,
   'state_counts': {'applied': 223, 'no_delta': 10, 'rejected': 521, 'needs_evidence': 4585},
   'lifecycle_counts': {'active': 4585, 'terminal': 754}
  },
  'apply_plan_hashes': {'checked': 26, 'matched': 26, 'note': '25 个 create 的 after_sha256/bytes/lines 与磁盘一致；1 个 update 的 before 为修订前指纹、after 为修订后指纹'},
  'content_quality': {'units': 231, 'findings': 0},
  'repo_audit': {'issues': 0, 'evidence_refs': '231/231'},
  'pre_commit': {'rule_drift': 0},
  'duplicate_closure': {
   'term_doc2_total': 136, 'term_doc2_closed': 29, 'term_doc2_open': 107, 'term_doc2_open_members': 214,
   'person_doc2_total': 48, 'person_doc2_open': 0
  },
  'notes': '原始瓷与原始瓷器两组共用同一实体，0354 两候选整组 rejected 并指向 proto-porcelain.md；0355 由高丰 canonical 执行 update，田自秉候选 rejected（该册来源已在既有 KU 中绑定 L1917-L1919）。'
 }
}
json.dump(m, open(PKG / 'manifest.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('manifest written', len(created), len(updated))
