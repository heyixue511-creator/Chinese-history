import json, hashlib
from pathlib import Path

PKG=Path('06-runtime/automation/2026-10-25-person-doc2-batch-m')
plan=[json.loads(l) for l in (PKG/'apply-plan.jsonl').read_text(encoding='utf-8').splitlines() if l.strip()]
mapping=json.loads((PKG/'canonical-mapping.json').read_text(encoding='utf-8'))

NOTE={
 'xdup-0223':'高丰只有群体提名，2016 补生卒、里昂美专学历、美亚丝绸厂八年与“限色”方法。',
 'xdup-0224':'赵农记 36 卷 357 篇 3555 条与“以材为祖”，2016 记熙宁至崇宁成书过程、四部分与 13 工种；用字“李诚／李诫”并列。',
 'xdup-0225':'赵农只有 1891 年纶章造纸局一条，2016 详列洋炮局、江南制造总局、轮船招商局与北洋海军。',
 'xdup-0227':'高丰详记穉英画室、年产量与旗袍美女形象，赵农只列名；高丰同一节“杭释英”为讹写。',
 'xdup-0228':'赵农记清华学派、天安门广场与北京规划，2016 记国徽设计组、1950 年发布令与 1961 年《建筑和建筑艺术》。',
 'xdup-0229':'赵农记仁宗年间首创活字与“接近铅活字印刷”，李立新记庆历 1041—1048 与王祯—毕昇印刷设计家集群。',
 'xdup-0231':'赵农称《梦溪笔谈》609 条为设计史重要文献，田自秉引其“鉴大则平，鉴小则凸”论铜镜光学。',
 'xdup-0235':'赵农重其文化形象，李立新引“百工之于艺……至唐而备矣”“渐老渐熟，乃造平淡”并记药玉盏、荷叶杯。',
 'xdup-0236':'两版均记独轮车与“木牛流马”，2016 补“鸡公车”、早于欧洲千余年及东汉已有独轮车的来源张力。',
 'xdup-0238':'高丰详记擦笔水彩法、风格与三大盟主，赵农只列名。',
 'xdup-0239':'赵农详于《盛世危言》工艺论与四项主张，李立新详于洋货入华分析与“商战”“实业救国论”先声。',
 'xdup-0240':'两版文字基本一致：1921 年九溪十八涧、1922 年建厂、1926 年费城博览会金质奖。',
 'xdup-0241':'赵农详六次东渡经过，2016 据《唐大和尚东征传》记天宝二年同行玉作人、雕檀、刻镂等工手 85 人。',
 'xdup-0242':'赵农记《冯小青》装帧及插图，2016 记比亚兹莱影响与东西艺术手法的结合。',
 'xdup-0244':'赵农记妙应寺白塔与司天台，2016 详塔基、华盖、流苏、风铃与刹顶形制；塔高 53 米／50.9 米并列。',
 'xdup-0246':'赵农记《彷徨》《坟》装帧风格，2016 记《时报》馆经历、1925 年结识鲁迅与书装评价。',
 'xdup-0247':'两版文字几乎一致：应募修紫禁城、工部营造所长班、圆明园楠木样式房掌案与两部著作。',
 'xdup-0248':'高丰只有群体提名，2016 补中央工艺美术学院副院长、1953 年座谈与 1992 年逝世 3 周年纪念会。',
 'xdup-0250':'赵农记《斫琴图》与南方制琴工序，李立新记其早年擅长设计并列入佛教绘画雕刻家谱系。',
}

manifest={
 'work_package':'2026-10-25-person-doc2-batch-m',
 'goal':'第十五批：对剩余 21 个 doc_count=2 的 person 组（42 个候选）做新建／拒绝裁决；19 个新 person KU 建立，23 个候选 rejected（19 个同组重复候选并入新建 KU，阎立本、贾兰坡两组 4 个候选整组拒绝）。',
 'status':'applied',
 'created_at':'2026-10-25T21:05:00+08:00',
 'updated_at':'2026-10-25T21:05:00+08:00',
 'inputs':{
   'candidate_index_before_apply':'06-runtime/state/candidate-index.jsonl',
   'candidate_index_before_apply_fingerprint':'sha256:53a77971c3e950f0174e304b1f681038af9c226bf2143d1092c1367d6e910c00（7,193,758 B，5,339 行）',
   'duplicate_group_recall':'06-runtime/automation/2026-10-25-cross-source-candidate-consolidation/duplicate-groups.jsonl',
   'prior_batch':'06-runtime/automation/2026-10-25-person-doc2-batch-l/manifest.json',
   'source_scope':'前六册（Books 1-6）；Book 7 及以后按用户指示不启动'
 },
 'scope':{
   'group_rule':'doc_count=2 的 person 组中尚未关闭的 21 组；其中 xdup-0237（贾兰坡）、xdup-0243（阎立本）两册候选均只作学术引用或史料，整组拒绝，不建 KU。',
   'group_ids':[m['group_id'] for m in mapping],
   'groups':21,'candidate_rows':42,'canonical_candidates':19,'applied_canonical_candidates':19,
   'rejected_candidates':23,'created_units':19,'updated_units':0,'no_delta_units':0
 },
 'method':{
   'semantic_step':'逐组复读两册候选摘要与来源段落，比较人物时代、身份、作品、师承、评价与用字差异；有实质设计史内容即新建，同组另一候选并入后 rejected；仅作学术引用或图像史料的人物不入知识层。',
   'canonical_rule':'每组选内容最完整、且 proposed_slug 与最终文件名最接近的候选为 canonical；另一成员以“同一 entity，语义已并入”rejected。',
   'decision_rule':'19 组新建：李有行、李诚、李鸿章、杭穉英、梁思成、毕昇、沈括、苏轼、蒲元、郑曼陀、郑观应、都锦生、鉴真、闻一多、阿尼哥、陶元庆、雷发达、雷圭元、顾恺之；2 组整组拒绝：贾兰坡、阎立本；0 组 no_delta。',
   'state_chain':'needs_evidence -> ready_for_review -> approved -> applied（19 条 canonical）；needs_evidence -> rejected（19 条 merged member + 4 条整组拒绝）',
   'ledger_rows':80,
   'apply_plan_rows':19
 },
 'outputs':{
   'apply_plan':'06-runtime/automation/2026-10-25-person-doc2-batch-m/apply-plan.jsonl',
   'candidate_decision_ledger':'06-runtime/automation/2026-10-25-person-doc2-batch-m/candidate-decision-ledger.jsonl',
   'canonical_mapping':'06-runtime/automation/2026-10-25-person-doc2-batch-m/canonical-mapping.json',
   'created_units':[r['target_ref'] for r in plan],
   'summary':'06-runtime/automation/2026-10-25-person-doc2-batch-m/summary.md'
 },
 'canonical_mapping':mapping,
 'source_variance_notes':[
   '李有行：高丰只有“重要开拓者”群体提名，2016 有 1905—1982、里昂美专、美亚丝绸厂与“限色”；两册均无图版核对。',
   '李诚：赵农作“宋哲宗时编著、宋徽宗时刊行”，2016 作熙宁编、元符三年成书、崇宁二年刊行；用字“李诚”与通行“李诫”并列。',
   '李鸿章：赵农只有纶章造纸局，2016 详列洋炮局、江南制造总局、轮船招商局、北洋海军；两册均未给生卒年。',
   '杭穉英：高丰同一节又作“杭释英”，图 9-8b 同；赵农只列名，未记画室与产量。',
   '梁思成：赵农详于“清华学派”与北京规划争议，2016 详于国徽设计组名单与 1961 年文章；两册均未给生卒年。',
   '毕昇：赵农作“仁宗年间”，李立新作“庆历年间（1041—1048）”；赵农图 7-4 误作“毕异像”。',
   '沈括：赵农详于《梦溪笔谈》609 条的文献价值，田自秉只引铜镜一条；两册均未给生卒年。',
   '苏轼：赵农重文化形象，李立新重造物评价与审美；《药玉盏》《荷叶杯》见李立新 L1109。',
   '蒲元：2016 先称汉魏盛行独轮车、由蒲元发明，又记东汉民间已有独轮车；发明者与时代关系原文未清，并列保留。',
   '郑曼陀：高丰详于“擦笔水彩法”与三大盟主，赵农只列名；两册均未给生卒年。',
   '郑观应：赵农把《盛世危言》的“工艺”解为“工业设计”，另一处又作“科学技术”；李立新引文侧重洋货冲击与商战。',
   '都锦生：两版文字基本一致，2016 图号由 10-11 后移为 10-12。',
   '鉴真：赵农详六次东渡，2016 据《唐大和尚东征传》记工匠 85 人；两册均未给生卒年。',
   '闻一多：赵农只记《冯小青》，2016 补比亚兹莱影响与“东西艺术手法结合”评价；两册均未给生卒年。',
   '阿尼哥：塔高有 53 米（赵农）与 50.9 米（2016）两说；塔身描述一作“宝瓶”，一作“覆钵式”。',
   '陶元庆：赵农详《彷徨》《坟》风格，2016 详《时报》馆、鲁迅关系与书装评价；两册均未给生卒年。',
   '雷发达：两版文字几乎一致，均作“紫金城”“紫徽照令”，为“紫禁城”“紫微”讹写，照录。',
   '雷圭元：高丰只有群体提名，2016 补副院长、1953 年座谈与 1992 年纪念会；生卒年据“逝世 3 周年”推知，原文未直接给出。',
   '顾恺之：赵农只有《斫琴图》，李立新补“早年擅长设计”与佛教艺术谱系；两册均未给生卒年。',
   '贾兰坡：现代考古学家，两册只引其石器研究结论作设计起源讨论的学术依据，不建立 person KU。',
   '阎立本：唐代画家，两册只以《步辇图》《萧翼赚兰亭图》作唐代服饰、家具史料，不建立 person KU。'
 ],
 'semantic_change':{'created_knowledge_units':19,'updated_knowledge_units':0,'deleted_knowledge_units':0,'new_relations':0,'new_claims':0,'source_files_modified':0,
   'confidence_posture':'全部 19 条 KU 保持 confidence=medium、consensus=tentative、evidence_status=source_backed；未标 confirmed、externally_verified 或 L1-L7 级验证。'},
 'validation':{
   'result':'passed',
   'candidate_index_after':'sha256:f16a7b1cb03c7dbbdd6a38df36fe7c2e2735100882a412578fc29c2364fbb689（7,200,546 B，5,339 行）',
   'candidate_state_counts':{'applied':197,'no_delta':10,'rejected':492,'needs_evidence':4640},
   'lifecycle_counts':{'active':4640,'terminal':699},
   'apply_plan_hashes':'19/19',
   'knowledge_units_total':206,
   'content_quality':'206 KU，0 findings',
   'repo_audit':'0 问题；evidence 206/206；persons 72',
   'pre_commit':'规则漂移 0',
   'sync_closure':'19 steps；250 passed, 16 subtests',
   'duplicate_closure':{'doc2_total':352,'doc2_open':302,'doc2_closed':50,'doc1_open':6,'doc3plus_open':0,'open_members':617}
 },
 'boundaries':[
   '不 commit、不 push；只改工作树。',
   '不新建分支或 worktree；只保留 main。',
   '02-sources/ 与 03基础书籍-md文档/ 只读，未改写、未删除。',
   '未使用外部验证平台，证据仅来自六册 Markdown 文本。',
   '未做图版、器物、手稿或档案的视觉与实物核对。',
   'primary_theme 与 topic_memberships 留空；Theme/Topic 尚未 materialize，记为研究债。',
   '未写入正式 relations；同组与同章共现只作非断言性叙述。',
   '来源分歧（年代、身份、用字、师承、评价、数据）一律并列保留，不做调和。',
   '本批只覆盖前六册；Book 7 及以后未启动。'
 ]
}
(PKG/'manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=1)+'\n',encoding='utf-8',newline='\n')
print('written',len(mapping),'mapping',len(plan),'plan')
