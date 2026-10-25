import json, hashlib
from pathlib import Path

PKG=Path('06-runtime/automation/2026-10-25-person-doc2-batch-l')
groups={g['group_id']:g for g in (json.loads(l) for l in open('06-runtime/automation/2026-10-25-cross-source-candidate-consolidation/duplicate-groups.jsonl',encoding='utf-8') if l.strip())}
plan=[json.loads(l) for l in (PKG/'apply-plan.jsonl').read_text(encoding='utf-8').splitlines() if l.strip()]
by_target={r['target_ref']:r for r in plan}

ORDER=[('xdup-0203','丰子恺','C'),('xdup-0205','刘昼','A'),('xdup-0206','利玛窦','E'),('xdup-0207','卫改','B'),
 ('xdup-0208','吕彦直','B'),('xdup-0209','商汤','D'),('xdup-0211','夏燕靖',None),('xdup-0212','大禹','D'),
 ('xdup-0214','孙中山','D'),('xdup-0215','张光宇','C'),('xdup-0217','张衡','B'),('xdup-0219','曾国藩','D'),
 ('xdup-0221','朱启钤','D'),('xdup-0222','朱熹','A')]
NOTE={
 'xdup-0203':'赵农 2009 记民国书籍插图风格与谱系，夏燕靖 2016 记漫画笔法与装饰性构图；两册均无生卒年。',
 'xdup-0205':'夏燕靖 2009 记北朝、裘蓑之喻与“施用有宜”，2016 记北齐与《刘子新论》；引文用字有“黡／麕”差异，并列保留。',
 'xdup-0206':'赵农记望远镜、自鸣钟、世界地图与科学知识传入，李立新记 1601 年向万历帝进献自鸣钟及传教士携带奇器谱系。',
 'xdup-0207':'田自秉只列武氏祠石工姓名，李立新补碑文“良匠卫改……”与高平、山阳工匠集群。',
 'xdup-0208':'赵农记 1929 年中山陵设计手法与广州中山纪念堂，2016 记 1927 年竞图首奖、评判报告引文与历史意义。',
 'xdup-0209':'赵农记约前 1711 年灭夏、矿产资源与青铜文化，2016 记约前 1600 年成汤革夏；年代两说并列。',
 'xdup-0211':'来源作者简历／版本元数据，属来源 paratext，不构成中国设计史知识层的设计主体；不建立 person KU。',
 'xdup-0212':'赵农记治水、农耕与“最早的规划设计师”评价，2016 记收九牧之金铸九鼎传说与九鼎成为传国重器。',
 'xdup-0214':'赵农记 1919 年《建国方略》东方大港与浦东市宅中心，2016 记中山装设计、形制寓意与剪辫易服法令。',
 'xdup-0215':'赵农记《万象》封面风格与 1949 年后字体设计，2016 记 1992 年《装饰》纪念张光宇特刊。',
 'xdup-0217':'赵农记地动仪、浑天说与地图／指南车贡献，2016 记青铜浑天仪、候风地动仪结构与“形似酒尊”形制；2016 一处误作“张仪”。',
 'xdup-0219':'赵农只有洋务派群体一句，2016 详列安庆军械所、采买机器、江南机器制造总局、翻译馆、幼童留美五件实事。',
 'xdup-0221':'赵农记营造学会、中国营造学社与《园冶》《梓人遗制》整理，2016 记 1927 年刊刻《髹饰录》及其乾坤两集结构。',
 'xdup-0222':'赵农记“男子有三紧”的服饰观，李立新记“简易”“致用”“道即器，器即道”与《训学斋规》器物整饬。',
}

mapping=[]; created=[]
for gid,entity,dim in ORDER:
    g=groups[gid]
    ids=[m['candidate_id'] for m in g['members']]
    slug={'夏燕靖':None}.get(entity)
    if entity=='夏燕靖':
        mapping.append({'group_id':gid,'entity':entity,'target_ref':None,'canonical_candidate':None,'merged_member':None,'decision':'rejected','action':'none','update_note':NOTE[gid]})
        continue
    row=next(r for r in plan if r['entity']==entity)
    canon=row['candidate_id']; other=[i for i in ids if i!=canon][0]
    mapping.append({'group_id':gid,'entity':entity,'target_ref':row['target_ref'],'canonical_candidate':canon,'merged_member':other,'decision':'applied','action':'create','update_note':NOTE[gid]})
    created.append(row['target_ref'])

manifest={
 'work_package':'2026-10-25-person-doc2-batch-l',
 'goal':'第十四批：对 14 个 doc_count=2 的 person 组（28 个候选）做新建／拒绝裁决；13 个新 person KU 建立，15 个候选 rejected（13 个同组重复候选并入新建 KU，夏燕靖组 2 个候选作为来源 paratext 拒绝）。',
 'status':'applied',
 'created_at':'2026-10-25T20:10:00+08:00',
 'updated_at':'2026-10-25T20:10:00+08:00',
 'inputs':{
   'candidate_index_before_apply':'06-runtime/state/candidate-index.jsonl',
   'candidate_index_before_apply_fingerprint':'sha256:1a17f697105bdda1883a0540e544aa2c4471ecec53b278e9ff20e6b5f3337a19（7,189,312 B，5,339 行）',
   'duplicate_group_recall':'06-runtime/automation/2026-10-25-cross-source-candidate-consolidation/duplicate-groups.jsonl',
   'prior_batch':'06-runtime/automation/2026-10-25-ten-person-units-and-mozi-update/manifest.json',
   'source_scope':'前六册（Books 1-6）；Book 7 及以后按用户指示不启动'
 },
 'scope':{
   'group_rule':'doc_count=2 的 person 组中，按 group_id 顺序选出的 14 组；其中 xdup-0211（夏燕靖）两册候选均为来源作者简历／版本元数据，整组拒绝，不建 KU。',
   'group_ids':[gid for gid,_,_ in ORDER],
   'groups':14,'candidate_rows':28,'canonical_candidates':13,'applied_canonical_candidates':13,
   'rejected_candidates':15,'created_units':13,'updated_units':0,'no_delta_units':0
 },
 'method':{
   'semantic_step':'逐组复读两册候选摘要与来源段落，比较人物时代、身份、作品、师承、评价与用字差异；有实质设计史内容即新建，同组另一候选并入后 rejected；来源作者简历不入知识层。',
   'canonical_rule':'每组选内容最完整、且 proposed_slug 与最终文件名最接近的候选为 canonical；另一成员以“同一 entity，语义已并入”rejected。',
   'decision_rule':'13 组新建：丰子恺、刘昼、利玛窦、卫改、吕彦直、商汤、大禹、孙中山、张光宇、张衡、曾国藩、朱启钤、朱熹；1 组整组拒绝：夏燕靖；0 组 no_delta。',
   'state_chain':'needs_evidence -> ready_for_review -> approved -> applied（13 条 canonical）；needs_evidence -> rejected（13 条 merged member + 2 条夏燕靖）',
   'ledger_rows':54,
   'apply_plan_rows':13
 },
 'outputs':{
   'apply_plan':'06-runtime/automation/2026-10-25-person-doc2-batch-l/apply-plan.jsonl',
   'candidate_decision_ledger':'06-runtime/automation/2026-10-25-person-doc2-batch-l/candidate-decision-ledger.jsonl',
   'created_units':created,
   'summary':'06-runtime/automation/2026-10-25-person-doc2-batch-l/summary.md'
 },
 'canonical_mapping':mapping,
 'source_variance_notes':[
   '丰子恺：赵农作“书籍插图”风格与谱系，2016 作“书装”手法；两册均未给生卒年；图 10-37、10-38 未视觉核验。',
   '刘昼：2009 作“北朝”，2016 作“北齐”；引文“黡管苍蒯”／“麕管苍蒯”用字不同；《刘子》与《刘子新论》两名并列。',
   '利玛窦：赵农记“利玛窦等人”与科学知识传播，李立新记 1601 年进献自鸣钟；两册均未给生卒年；图 3—6 未视觉核验。',
   '卫改：田自秉只列姓名，李立新补碑文与工匠集群；碑文标点按来源照录。',
   '吕彦直：赵农记 1929 年设计，2016 记 1927 年竞图；陵墓平面“钟形”与“木铎警世”评语仅 2016 明记。',
   '商汤：立国年代有约前 1711 年（赵农）与约前 1600 年（2016）两说；名号有“商汤”与“成汤”两种。',
   '大禹：治水、农耕与“最早的规划设计师”评价仅赵农明记；铸九鼎、九鼎成为传国重器仅 2016 明记；传说与史实界限按来源保留。',
   '孙中山：赵农详于《建国方略》与东方大港，2016 详于中山装形制与剪辫易服；中山装寓意原文冠以“据说”。',
   '张光宇：赵农详于《万象》与 1949 年后字体设计，2016 只有 1992 年纪念特刊；两册均未给生卒年。',
   '张衡：赵农详于浑天说与地图／指南车，2016 详于浑天仪、地动仪结构与图版；2016 同段一处误作“张仪”。',
   '曾国藩：赵农只有洋务派群体一句，2016 详列五件实事；两册评价侧重不同，并列保留。',
   '朱启钤：赵农详于营造学会与中国营造学社，2016 只记《髹饰录》刊刻；两册均未给生卒年。',
   '朱熹：赵农详于“男子有三紧”的服饰观，李立新详于“简易”“致用”与道器关系；引文用字按各自来源照录。',
   '夏燕靖：2009 候选为作者简历（L54-L65），2016 候选为全书 front matter（L11-L6538），均属来源元数据，不进入设计史知识层。'
 ],
 'semantic_change':{'created_knowledge_units':13,'updated_knowledge_units':0,'deleted_knowledge_units':0,'new_relations':0,'new_claims':0,'source_files_modified':0,
   'confidence_posture':'全部 13 条 KU 保持 confidence=medium、consensus=tentative、evidence_status=source_backed；未标 confirmed、externally_verified 或 L1-L7 级验证。'},
 'validation':{'result':'pending'},
 'boundaries':[
   '不 commit、不 push；只改工作树。',
   '不新建分支或 worktree；只保留 main。',
   '02-sources/ 与 03基础书籍-md文档/ 只读，未改写、未删除。',
   '未使用外部验证平台，证据仅来自六册 Markdown 文本。',
   '未做图版、器物、手稿或档案的视觉与实物核对。',
   'primary_theme 与 topic_memberships 留空；Theme/Topic 尚未 materialize，记为研究债。',
   '未写入正式 relations；同组与同章共现只作非断言性叙述。',
   '来源分歧（年代、身份、用字、师承、评价）一律并列保留，不做调和。',
   '本批只覆盖前六册；Book 7 及以后未启动。'
 ]
}
(PKG/'manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=1)+'\n',encoding='utf-8',newline='\n')
print('written',len(mapping),'mapping',len(created),'created')
