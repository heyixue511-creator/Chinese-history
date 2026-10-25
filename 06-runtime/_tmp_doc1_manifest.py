import json, hashlib
from pathlib import Path

PKG = Path('06-runtime/automation/2026-10-25-doc1-groups-batch')
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
closed_states = {'applied', 'rejected', 'no_delta'}
open_groups = [g for g in groups if not all(byid[m['candidate_id']]['state'] in closed_states for m in g['members'])]

plan = [json.loads(l) for l in open(PKG / 'apply-plan.jsonl', encoding='utf-8') if l.strip()]
ok = 0
for r in plan:
    t = Path(r['target_ref']).read_text(encoding='utf-8').replace('\r\n', '\n'); b = t.encode()
    if 'sha256:' + hashlib.sha256(b).hexdigest() == r['after_sha256'] and len(b) == r['bytes'] and t.count('\n') == r['lines']:
        ok += 1

mapping = json.load(open(PKG / 'canonical-mapping.json', encoding='utf-8'))
created = [v['target_ref'] for v in mapping.values()]
by_type = {}
for g in groups:
    if g['group_id'] in mapping:
        by_type[g['unit_type']] = by_type.get(g['unit_type'], 0) + 1

m = {
 'work_package': '2026-10-25-doc1-groups-batch',
 'goal': '处理全部 doc_count=1 的 6 个重复组（person 2、term 3、work 1，共 12 个候选）：每组 1 条 create，合并同册两处候选建立 6 个 KU；至此 523 个重复组全部关闭。',
 'status': 'applied',
 'created_at': '2026-10-25T17:35:00+08:00',
 'updated_at': '2026-10-25T17:50:00+08:00',
 'inputs': {
  'candidate_index_before_apply_fingerprint': '5,339 行；本批前状态为 applied 494 / no_delta 15 / rejected 795 / needs_evidence 4035',
  'duplicate_group_recall': '06-runtime/automation/2026-10-25-cross-source-candidate-consolidation/duplicate-groups.jsonl',
  'prior_batch': '06-runtime/automation/2026-10-25-event-doc2-batch/manifest.json',
  'source_scope': '前六册（Books 1-6）；Book 7 及以后按用户指示不启动'
 },
 'scope': {
  'group_rule': '全部 doc_count=1 的未关闭组（person 2、term 3、work 1，共 6 组）',
  'group_ids': sorted(mapping), 'groups': 6, 'candidate_rows': 12,
  'by_unit_type': by_type,
  'canonical_candidates': 6, 'applied_canonical_candidates': 6, 'no_delta_canonical_candidates': 0,
  'rejected_candidates': 6,
  'created_units': 6, 'updated_units': 0, 'no_delta_units': 0
 },
 'method': {
  'semantic_step': '逐组复读同册两处候选摘要与 F 字段，并回读赵农原文对应段落；同组重复候选只保留信息量大者作 canonical，另一处的说法补入同一 KU 正文并保留来源定位。',
  'canonical_rule': '按信息量较大者指定 canonical：女娲 cand-01-20、燕肃 cand-08-70、宣纸 cand-10-83、屏风 cand-06-16、招贴 cand-12-159、中国馆 cand-12-119。',
  'heterogeneity_rule': '同册异节候选不拆条：女娲（导论传说／第一章乐器）、燕肃（第七章总述／用具节）、宣纸（宋代造纸／明清文房四宝）、屏风（战国家具／魏晋陈设）、招贴（宋代广告／现代广告）、中国馆（导论图注／第十章图注）均合为一条。',
  'decision_rule': '6 组 create；无 update、无 no_delta。既有 KU 无同名条目；`works/simei-tu.md`、`terms/zhinan-che.md`、`terms/huangzi.md` 等他条不构成同实体重复。',
  'state_chain': 'needs_evidence -> ready_for_review -> approved -> applied（6 个 canonical）；needs_evidence -> rejected（6 个 merged member）',
  'ledger_rows': 24, 'apply_plan_rows': 6
 },
 'outputs': {
  'apply_plan': '06-runtime/automation/2026-10-25-doc1-groups-batch/apply-plan.jsonl',
  'candidate_decision_ledger': '06-runtime/automation/2026-10-25-doc1-groups-batch/candidate-decision-ledger.jsonl',
  'canonical_mapping': '06-runtime/automation/2026-10-25-doc1-groups-batch/canonical-mapping.json',
  'created_units': created,
  'summary': '06-runtime/automation/2026-10-25-doc1-groups-batch/summary.md'
 },
 'validation': {
  'candidate_index_after': {
   'sha256': idx_fp, 'bytes': len(raw), 'lines': text.count('\n'),
   'state_counts': states, 'lifecycle_counts': life
  },
  'apply_plan_hashes': {'checked': len(plan), 'matched': ok},
  'content_quality': {'units': 504, 'findings': 0},
  'repo_audit': {'issues': 0, 'evidence_refs': '504/504', 'cross_type_disambiguation': '6/6（3 组）'},
  'pre_commit': {'rule_drift': 0},
  'duplicate_closure': {
   'total_groups': len(groups), 'closed_groups': len(groups) - len(open_groups), 'open_groups': len(open_groups),
   'by_doc_count': {str(d): sum(1 for g in groups if g['doc_count'] == d) for d in sorted({g['doc_count'] for g in groups})},
   'notes': '523 个重复组全部关闭；此后不再有 duplicate group 待办。'
  },
  'notes': '本批并列与边界：女娲候选分属导论“上古传说的设计”与第一章“乐器”，内容互补；燕肃生卒年未记；宣纸澄心堂纸前史仅赵农一册所记；屏风“扆／黼扆”作别名保留；招贴的宋代义与 20 世纪分类体系同条并列；中国馆两处均仅图注，图版未视觉核验，不补外部建筑信息。'
 }
}
json.dump(m, open(PKG / 'manifest.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('manifest ok', 'plan', len(plan), 'hashes', ok, 'states', states, 'open groups', len(open_groups))
