import json, hashlib
from pathlib import Path

PKG = Path('06-runtime/automation/2026-10-25-publication-doc2-batch-b')
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
term_total, term_closed = stat('term', 2)
person_total, person_closed = stat('person', 2)

m = {
 'work_package': '2026-10-25-publication-doc2-batch-b',
 'goal': '处理 publication 类型 doc_count=2 重复组第二批 23 组（xdup-0310—xdup-0332，46 个候选）：23 组 create，共新建 23 个 publication KU；另处理《荀子》《韩非子》人物／典籍同名消歧。',
 'status': 'applied',
 'created_at': '2026-10-25T20:20:00+08:00',
 'updated_at': '2026-10-25T20:50:00+08:00',
 'inputs': {
  'candidate_index_before_apply_fingerprint': 'sha256:…（5,339 行；第一批 manifest 记录为 applied 402 / no_delta 14 / rejected 702 / needs_evidence 4221）',
  'duplicate_group_recall': '06-runtime/automation/2026-10-25-cross-source-candidate-consolidation/duplicate-groups.jsonl',
  'prior_batch': '06-runtime/automation/2026-10-25-publication-doc2-batch-a/manifest.json',
  'source_scope': '前六册（Books 1-6）；Book 7 及以后按用户指示不启动'
 },
 'scope': {
  'group_rule': 'publication 类型、doc_count=2、按 group_id 升序的第 24—46 个未关闭组',
  'group_ids': sorted(mapping), 'groups': 23, 'candidate_rows': 46,
  'canonical_candidates': 23, 'applied_canonical_candidates': 23, 'no_delta_canonical_candidates': 0,
  'rejected_candidates': 23,
  'created_units': 23, 'updated_units': 2, 'no_delta_units': 0
 },
 'method': {
  'semantic_step': '逐组复读两册候选摘要与 F 字段，比较作者、卷次、成书年、出版者与内容提法；同实体重复候选只保留 canonical；同名异书与书名异写分别处理。',
  'canonical_rule': '按信息量较大且正文可证者指定 canonical；另一册要点补入正文并保留来源。',
  'cross_type_rule': '新建《荀子》《韩非子》典籍条与既有 person 条同名，按仓库既有 mengzi／zhuangzi 分流办法，为四条补 `disambiguation` 字段（均以“类型消歧：”开头）；两个 person 条 version 1→2，并同步修正 `persons/han-fei-zi.md` 中“publications/ 下现无该书条目”的过期表述。',
  'decision_rule': '23 组全部 create；无 update／no_delta／reject-canonical。',
  'state_chain': 'needs_evidence -> ready_for_review -> approved -> applied（23 个 canonical）；needs_evidence -> rejected（23 个 merged member）',
  'ledger_rows': 92, 'apply_plan_rows': 23
 },
 'outputs': {
  'apply_plan': '06-runtime/automation/2026-10-25-publication-doc2-batch-b/apply-plan.jsonl',
  'candidate_decision_ledger': '06-runtime/automation/2026-10-25-publication-doc2-batch-b/candidate-decision-ledger.jsonl',
  'canonical_mapping': '06-runtime/automation/2026-10-25-publication-doc2-batch-b/canonical-mapping.json',
  'created_units': created,
  'summary': '06-runtime/automation/2026-10-25-publication-doc2-batch-b/summary.md'
 },
 'auxiliary_edits': [
  {'target_ref': '04-knowledge/units/persons/xunzi.md',
   'reason': '新建 publications/xunzi.md 后出现跨类型同名（且同 basename）；补 `disambiguation` 字段，version 1→2，正文未改。',
   'version_before': 1, 'version_after': 2},
  {'target_ref': '04-knowledge/units/persons/han-fei-zi.md',
   'reason': '新建 publications/hanfeizi.md 后出现跨类型同名；补 `disambiguation` 字段，version 1→2；并修正「相关知识元」中“publications/ 下现无该书条目，属研究债务”的过期表述。',
   'version_before': 1, 'version_after': 2}
 ],
 'validation': {
  'candidate_index_after': {
   'sha256': idx_fp, 'bytes': len(raw), 'lines': text.count('\n'),
   'state_counts': states, 'lifecycle_counts': life
  },
  'apply_plan_hashes': {'checked': len(plan), 'matched': ok},
  'content_quality': {'units': 432, 'findings': 0},
  'repo_audit': {'issues': 0, 'evidence_refs': '432/432', 'cross_type_disambiguation': '6/6（3 组）'},
  'pre_commit': {'rule_drift': 0},
  'duplicate_closure': {'publication_doc2_total': pub_total, 'publication_doc2_closed': pub_closed,
                        'publication_doc2_open': pub_total - pub_closed,
                        'work_doc2_open': work_total - work_closed,
                        'term_doc2_open': term_total - term_closed,
                        'person_doc2_open': person_total - person_closed},
  'notes': '本批并列/异写：《礼记》礼运篇引文 OCR 异文（宫窑／管窑／槽巢）；《竹书纪年》盘庚至纣 273 年（赵农）／253 年（2016）；《绣谱》章名“程工／工程”；《考工记图》“高庫”（疑“高庳”）；《萝轩变古笺谱》“恒版拱花／饾版、拱花”；《鲁班经》“年荣”（疑“午荣”）、“雕新”；《闲情偶寄／闲情偶记》书名异写；《荀子》“玉制”（疑“王制”）。'
 }
}
json.dump(m, open(PKG / 'manifest.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('manifest ok', 'plan', len(plan), 'hashes', ok, 'states', states, 'pub', pub_total, pub_closed, 'work', work_total, work_closed, 'term', term_total, term_closed, 'person', person_total, person_closed)
