import json, hashlib
from pathlib import Path

PKG=Path('06-runtime/automation/2026-10-25-person-doc2-batch-m')
PKG.mkdir(parents=True,exist_ok=True)

# group_id -> (entity, slug, dim, canonical_doc_prefix, apply_note)
G = {
 'xdup-0223': ('李有行','li-youxing','C','2016-xiayanjing','高丰只有群体提名，2016 补生卒、里昂美专学历、美亚丝绸厂八年与“限色”方法。'),
 'xdup-0224': ('李诚','li-cheng','B','2016-xiayanjing','赵农记 36 卷 357 篇 3555 条与“以材为祖”，2016 记熙宁至崇宁成书过程、四部分与 13 工种；用字“李诚／李诫”并列。'),
 'xdup-0225': ('李鸿章','li-hongzhang','D','2016-xiayanjing','赵农只有 1891 年纶章造纸局一条，2016 详列洋炮局、江南制造总局、轮船招商局与北洋海军。'),
 'xdup-0227': ('杭穉英','hang-zhiying','C','2004-gaofeng','高丰详记穉英画室、年产量与旗袍美女形象，赵农只列名；高丰同一节“杭释英”为讹写。'),
 'xdup-0228': ('梁思成','liang-sicheng','B','2016-xiayanjing','赵农记清华学派、天安门广场与北京规划，2016 记国徽设计组、1950 年发布令与 1961 年《建筑和建筑艺术》。'),
 'xdup-0229': ('毕昇','bi-sheng','C','2009-zhaonong','赵农记仁宗年间首创活字与“接近铅活字印刷”，李立新记庆历 1041—1048 与王祯—毕昇印刷设计家集群。'),
 'xdup-0231': ('沈括','shen-kuo','B','2009-zhaonong','赵农称《梦溪笔谈》609 条为设计史重要文献，田自秉引其“鉴大则平，鉴小则凸”论铜镜光学。'),
 'xdup-0235': ('苏轼','su-shi','A','2011-lilixin','赵农重其文化形象，李立新引“百工之于艺……至唐而备矣”“渐老渐熟，乃造平淡”并记药玉盏、荷叶杯。'),
 'xdup-0236': ('蒲元','pu-yuan','B','2016-xiayanjing','两版均记独轮车与“木牛流马”，2016 补“鸡公车”、早于欧洲千余年及东汉已有独轮车的来源张力。'),
 'xdup-0238': ('郑曼陀','zheng-mantuo','C','2004-gaofeng','高丰详记擦笔水彩法、风格与三大盟主，赵农只列名。'),
 'xdup-0239': ('郑观应','zheng-guanying','D','2009-zhaonong','赵农详于《盛世危言》工艺论与四项主张，李立新详于洋货入华分析与“商战”“实业救国论”先声。'),
 'xdup-0240': ('都锦生','du-jinsheng','B','2009-xiayanjing','两版文字基本一致：1921 年九溪十八涧、1922 年建厂、1926 年费城博览会金质奖。'),
 'xdup-0241': ('鉴真','jianzhen','E','2016-xiayanjing','赵农详六次东渡经过，2016 据《唐大和尚东征传》记天宝二年同行玉作人、雕檀、刻镂等工手 85 人。'),
 'xdup-0242': ('闻一多','wen-yiduo','C','2016-xiayanjing','赵农记《冯小青》装帧及插图，2016 记比亚兹莱影响与东西艺术手法的结合。'),
 'xdup-0244': ('阿尼哥','anige','B','2016-xiayanjing','赵农记妙应寺白塔与司天台，2016 详塔基、华盖、流苏、风铃与刹顶形制；塔高 53 米／50.9 米并列。'),
 'xdup-0246': ('陶元庆','tao-yuanqing','C','2016-xiayanjing','赵农记《彷徨》《坟》装帧风格，2016 记《时报》馆经历、1925 年结识鲁迅与书装评价。'),
 'xdup-0247': ('雷发达','lei-fada','B','2009-xiayanjing','两版文字几乎一致：应募修紫禁城、工部营造所长班、圆明园楠木样式房掌案与两部著作。'),
 'xdup-0248': ('雷圭元','lei-guiyuan','D','2016-xiayanjing','高丰只有群体提名，2016 补中央工艺美术学院副院长、1953 年座谈与 1992 年逝世 3 周年纪念会。'),
 'xdup-0250': ('顾恺之','gu-kai-zhi','B','2011-lilixin','赵农记《斫琴图》与南方制琴工序，李立新记其早年擅长设计并列入佛教绘画雕刻家谱系。'),
}
NO_TARGET={
 'xdup-0237':('贾兰坡','现代考古学家，两册只引其石器研究结论作为设计起源讨论的学术依据，未记其参与设计或工艺活动；不建立 person KU。'),
 'xdup-0243':('阎立本','唐代画家，两册只以《步辇图》《萧翼赚兰亭图》作唐代服饰、家具史料，未记其参与设计或工艺活动；不建立 person KU。'),
}

rows=[json.loads(l) for l in Path('06-runtime/state/candidate-index.jsonl').read_text(encoding='utf-8').splitlines() if l.strip()]
gs={g['group_id']:g for g in (json.loads(l) for l in open('06-runtime/automation/2026-10-25-cross-source-candidate-consolidation/duplicate-groups.jsonl',encoding='utf-8') if l.strip())}

def fp(p):
    t=Path(p).read_text(encoding='utf-8').replace('\r\n','\n')
    h=hashlib.sha256(t.encode('utf-8')).hexdigest()
    return 'sha256:'+h, len(t.encode('utf-8')), t.count('\n')

plan=[]; ledger=[]; mapping=[]; created=[]
for gid,(entity,slug,dim,canon_doc,note) in G.items():
    g=gs[gid]
    members=[m['candidate_id'] for m in g['members']]
    canon=[c for c in members if c.startswith(canon_doc)]
    assert len(canon)==1,(gid,canon)
    canon=canon[0]
    other=[c for c in members if c!=canon][0]
    target=f'04-knowledge/units/persons/{slug}.md'
    sha,b,n=fp(target)
    plan.append({'action':'create','target_ref':target,'candidate_id':canon,'entity':entity,
                 'before':None,'after_sha256':sha,'bytes':b,'lines':n,'note':note})
    created.append(target)
    ledger.append({'candidate_id':canon,'expected_state':'needs_evidence','state':'ready_for_review',
      'decision':{'status':'pending','reason':f'同组两册候选的重复召回，准备复读后写回 {target}','decided_by':'Agent','decided_at':'2026-10-25'},'updated_at':'2026-10-25'})
    ledger.append({'candidate_id':canon,'expected_state':'ready_for_review','state':'approved',
      'decision':{'status':'approved','reason':f'canonical 候选语义复读完成，批准按 exact change-set 创建 {target}','decided_by':'Agent','decided_at':'2026-10-25'},'updated_at':'2026-10-25'})
    ledger.append({'candidate_id':canon,'expected_state':'approved','state':'applied',
      'decision':{'status':'approved','reason':f'已按 exact change-set 创建 {target}','decided_by':'Agent','decided_at':'2026-10-25'},'target_ref':target,'updated_at':'2026-10-25'})
    ledger.append({'candidate_id':other,'expected_state':'needs_evidence','state':'rejected',
      'decision':{'status':'rejected','reason':f'同组重复候选，与 canonical 候选指向同一 entity（{entity}）；语义已并入 {target}，该候选不再单独写回','decided_by':'Agent','decided_at':'2026-10-25'},'target_ref':target,'updated_at':'2026-10-25'})
    mapping.append({'group_id':gid,'entity':entity,'target_ref':target,'canonical_candidate':canon,'merged_member':other,'decision':'applied','action':'create','update_note':note})
for gid,(entity,reason) in NO_TARGET.items():
    g=gs[gid]
    for m in g['members']:
        ledger.append({'candidate_id':m['candidate_id'],'expected_state':'needs_evidence','state':'rejected',
          'decision':{'status':'rejected','reason':reason,'decided_by':'Agent','decided_at':'2026-10-25'},'updated_at':'2026-10-25'})
    mapping.append({'group_id':gid,'entity':entity,'target_ref':None,'canonical_candidate':None,'merged_member':None,'decision':'rejected','action':'none','update_note':reason})

seen={}; ordered=[]
for r in ledger:
    seen.setdefault(r['candidate_id'],[]).append(r)
for cid,rs in seen.items(): ordered.extend(rs)

(PKG/'apply-plan.jsonl').write_text('\n'.join(json.dumps(r,ensure_ascii=False) for r in plan)+'\n',encoding='utf-8',newline='\n')
(PKG/'candidate-decision-ledger.jsonl').write_text('\n'.join(json.dumps(r,ensure_ascii=False) for r in ordered)+'\n',encoding='utf-8',newline='\n')
(PKG/'canonical-mapping.json').write_text(json.dumps(mapping,ensure_ascii=False,indent=1)+'\n',encoding='utf-8',newline='\n')
print('plan',len(plan),'ledger',len(ordered),'groups',len(G)+len(NO_TARGET))
