import json, hashlib
from pathlib import Path

PKG = Path('06-runtime/automation/2026-10-25-publication-doc2-batch-a')
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
    if 'sha256:' + hashlib.sha256(b).hexdigest() == r['after_sha256'] and len(b) == r['bytes'] and t.count('\n') == r['lines']:
        ok += 1

mapping = json.load(open(PKG / 'canonical-mapping.json', encoding='utf-8'))
created = [v['target_ref'] for v in mapping.values() if v['action'] == 'create']
pub_total, pub_closed = stat('publication', 2)
work_total, work_closed = stat('work', 2)

m = {
 'work_package': '2026-10-25-publication-doc2-batch-a',
 'goal': '处理 publication 类型 doc_count=2 重复组第一批 23 组（xdup-0287—xdup-0309，46 个候选）：22 组 create（其中同名异书 1 组拆为 2 条），1 组跨组同实体 no_delta，共新建 23 个 publication KU。',
 'status': 'applied',
 'created_at': '2026-10-25T19:20:00+08:00',
 'updated_at': '2026-10-25T20:05:00+08:00',
 'inputs': {
  'candidate_index_before_apply_fingerprint': 'sha256:850e060cecd281bed1d6634b31051658077865356f9432e90a4d18774fac04a5（7,266,836 B，5,339 行）',
  'duplicate_group_recall': '06-runtime/automation/2026-10-25-cross-source-candidate-consolidation/duplicate-groups.jsonl',
  'prior_batch': '06-runtime/automation/2026-10-25-work-doc2-batch-b/manifest.json',
  'source_scope': '前六册（Books 1-6）；Book 7 及以后按用户指示不启动'
 },
 'scope': {
  'group_rule': 'publication 类型、doc_count=2、按 group_id 升序的前 23 个未关闭组',
  'group_ids': sorted(mapping), 'groups': 23, 'candidate_rows': 46,
  'canonical_candidates': 24, 'applied_canonical_candidates': 23, 'no_delta_canonical_candidates': 1,
  'rejected_candidates': 22,
  'created_units': 23, 'updated_units': 1, 'no_delta_units': 1
 },
 'method': {
  'semantic_step': '逐组复读两册候选摘要与 F 字段，比较作者、卷次、成书年、出版者与内容提法；同实体重复候选只保留 canonical；同名异书与书名异写分别处理。',
  'canonical_rule': '按信息量较大且正文可证者指定 canonical；另一册要点补入正文并保留来源。',
  'split_rule': 'xdup-0289 两册同名《中国设计史》但作者、出版社、结构均不同，判为同名异书，不合并：高丰本建 `publications/zhongguo-shejishi-gaofeng.md`，夏燕靖本建 `publications/zhongguo-shejishi-xiayanjing.md`，两个候选各走完整 applied 链。',
  'cross_group_rule': 'xdup-0300「梦梁录」与 xdup-0302「梦粱录」为同一书（2016 同册两处标题即作“梦梁录／梦粱录”）；0302 canonical 建条，0300 canonical 判 no_delta 指向同文件。',
  'decision_rule': '22 组 create（含 1 组拆 2 条）；1 组 no_delta；无 update 候选。',
  'state_chain': 'needs_evidence -> ready_for_review -> approved -> applied（23 个 canonical）；needs_evidence -> ready_for_review -> approved -> no_delta（1 个 canonical）；needs_evidence -> rejected（22 个 merged member）',
  'ledger_rows': 94, 'apply_plan_rows': 23
 },
 'outputs': {
  'apply_plan': '06-runtime/automation/2026-10-25-publication-doc2-batch-a/apply-plan.jsonl',
  'candidate_decision_ledger': '06-runtime/automation/2026-10-25-publication-doc2-batch-a/candidate-decision-ledger.jsonl',
  'canonical_mapping': '06-runtime/automation/2026-10-25-publication-doc2-batch-a/canonical-mapping.json',
  'created_units': created,
  'summary': '06-runtime/automation/2026-10-25-publication-doc2-batch-a/summary.md'
 },
 'auxiliary_edits': [
  {'target_ref': '04-knowledge/units/persons/zhuangzi.md',
   'reason': '新建 publications/zhuangzi.md 后出现跨类型同名；补 `disambiguation` 字段并写明“类型消歧”，version 1→2，正文未改。',
   'version_before': 1, 'version_after': 2}
 ],
 'validation': {
  'candidate_index_after': {
   'sha256': idx_fp, 'bytes': len(raw), 'lines': text.count('\n'),
   'state_counts': states, 'lifecycle_counts': life
  },
  'apply_plan_hashes': {'checked': len(plan), 'matched': ok},
  'content_quality': {'units': 409, 'findings': 0},
  'repo_audit': {'issues': 0, 'evidence_refs': '409/409', 'cross_type_disambiguation': '4/4'},
  'pre_commit': {'rule_drift': 0},
  'sync_closure': {'steps': 19, 'tests': '250 passed + 16 subtests'},
  'duplicate_closure': {'publication_doc2_total': pub_total, 'publication_doc2_closed': pub_closed,
                        'publication_doc2_open': pub_total - pub_closed,
                        'work_doc2_open': work_total - work_closed},
  'notes': '本批并列/异写：十竹斋画谱版名“恒版／短版”（均疑为“饾版”之 OCR 误写）；《梦梁录／梦粱录》书名异写；《中国设计史》同名异书；《申报》广告定位“原形／雏形”。'
 }
}
json.dump(m, open(PKG / 'manifest.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('manifest ok', 'plan', len(plan), 'hashes', ok, 'states', states, 'pub', pub_total, pub_closed, 'work', work_total, work_closed)
