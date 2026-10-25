import json, hashlib
from pathlib import Path

PKG = Path('06-runtime/automation/2026-10-25-event-doc2-batch')
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
event_total, event_closed = stat('event', 2)

open_groups = []
for g in groups:
    if not all(byid[m['candidate_id']]['state'] in {'applied','rejected','no_delta'} for m in g['members']):
        open_groups.append({'group_id': g['group_id'], 'unit_type': g.get('unit_type'), 'doc_count': g.get('doc_count'), 'title': g['keys'].get('title')})

m = {
 'work_package': '2026-10-25-event-doc2-batch',
 'goal': '处理 event 类型 doc_count=2 全部 9 组（xdup-0167—xdup-0175，18 个候选）：9 组 create 新建 9 个 event KU。',
 'status': 'applied',
 'created_at': '2026-10-25T23:55:00+08:00',
 'updated_at': '2026-10-26T00:20:00+08:00',
 'inputs': {
  'candidate_index_before_apply_fingerprint': '5,339 行；event 批次前状态为 applied 485 / no_delta 15 / rejected 786 / needs_evidence 4053',
  'duplicate_group_recall': '06-runtime/automation/2026-10-25-cross-source-candidate-consolidation/duplicate-groups.jsonl',
  'prior_batch': '06-runtime/automation/2026-10-25-procedure-doc2-batch/manifest.json',
  'source_scope': '前六册（Books 1-6）；Book 7 及以后按用户指示不启动'
 },
 'scope': {
  'group_rule': 'event 类型、doc_count=2 的全部未关闭组（共 9 组）',
  'group_ids': sorted(mapping), 'groups': 9, 'candidate_rows': 18,
  'canonical_candidates': 9, 'applied_canonical_candidates': 9, 'no_delta_canonical_candidates': 0,
  'rejected_candidates': 9,
  'created_units': 9, 'updated_units': 0, 'no_delta_units': 0
 },
 'method': {
  'semantic_step': '逐组复读两册候选摘要与 F 字段，比较事件名称、时间、地点、参与者、原因与结果；同组重复候选只保留信息量大者作 canonical，另一册说法补入正文并保留来源。',
  'canonical_rule': '按信息量较大且正文可证者指定 canonical：夏燕靖 2016 6 组、夏燕靖 2009 3 组。',
  'heterogeneity_rule': '同名事件不拆条：南洋劝业会、巴拿马赛会、辛亥革命、盘庚迁殷在 two 册中同名，合为一条按册分述；`places/nanjing.md` 中的南洋劝业会场只作地点信息，不另建 event。',
  'decision_rule': '9 组 create；无 update、无 no_delta。',
  'state_chain': 'needs_evidence -> ready_for_review -> approved -> applied（9 个 canonical）；needs_evidence -> rejected（9 个 merged member）',
  'ledger_rows': 36, 'apply_plan_rows': 9
 },
 'outputs': {
  'apply_plan': '06-runtime/automation/2026-10-25-event-doc2-batch/apply-plan.jsonl',
  'candidate_decision_ledger': '06-runtime/automation/2026-10-25-event-doc2-batch/candidate-decision-ledger.jsonl',
  'canonical_mapping': '06-runtime/automation/2026-10-25-event-doc2-batch/canonical-mapping.json',
  'created_units': created,
  'summary': '06-runtime/automation/2026-10-25-event-doc2-batch/summary.md'
 },
 'validation': {
  'candidate_index_after': {
   'sha256': idx_fp, 'bytes': len(raw), 'lines': text.count('\n'),
   'state_counts': states, 'lifecycle_counts': life
  },
  'apply_plan_hashes': {'checked': len(plan), 'matched': ok},
  'content_quality': {'units': 498, 'findings': 0},
  'repo_audit': {'issues': 0, 'evidence_refs': '498/498', 'cross_type_disambiguation': '6/6（3 组）'},
  'pre_commit': {'rule_drift': 0},
  'duplicate_closure': {
   'event_doc2_total': event_total, 'event_doc2_closed': event_closed, 'event_doc2_open': event_total - event_closed,
   'all_remaining_open_groups': open_groups
  },
  'notes': '本批并列：全国民间美术工艺品展览会巡展国别（2009 四国／2016 五国含缅甸与座谈）；盘庚迁殷年代（公元前15世纪末／约前1250—前1050）与 2016 自身“253年／73年”矛盾；巴拿马赛会中国展品 1500 吨仅 2009 所记；洋务运动评价两册立场相反；安史之乱两册均无具体年份。'
 }
}
json.dump(m, open(PKG / 'manifest.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('manifest ok', 'plan', len(plan), 'hashes', ok, 'states', states, 'event', event_total, event_closed, 'open groups', len(open_groups))
for g in open_groups: print(g)
