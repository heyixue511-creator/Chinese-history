import json, hashlib
from pathlib import Path

PKG=Path('06-runtime/automation/2026-10-25-person-doc2-batch-l')
PKG.mkdir(parents=True,exist_ok=True)

# group_id -> (entity, target_slug, dim, canonical_candidate_suffix_doc, apply_note)
G = {
 'xdup-0203': ('丰子恺','feng-zikai','C','2009-zhaonong','赵农 2009 记民国书籍插图风格与谱系，夏燕靖 2016 记漫画笔法与装饰性构图；两册均无生卒年。'),
 'xdup-0205': ('刘昼','liu-zhou','A','2009-xiayanjing','夏燕靖 2009 记北朝、裘蓑之喻与“施用有宜”，2016 记北齐与《刘子新论》；引文用字有“黡／麕”差异，并列保留。'),
 'xdup-0206': ('利玛窦','li-madou','E','2009-zhaonong','赵农记望远镜、自鸣钟、世界地图与科学知识传入，李立新记 1601 年向万历帝进献自鸣钟及传教士携带奇器谱系。'),
 'xdup-0207': ('卫改','wei-gai','B','2011-lilixin','田自秉只列武氏祠石工姓名，李立新补碑文“良匠卫改……”与高平、山阳工匠集群。'),
 'xdup-0208': ('吕彦直','lu-yanzhi','B','2016-xiayanjing','赵农记 1929 年中山陵设计手法与广州中山纪念堂，2016 记 1927 年竞图首奖、评判报告引文与历史意义。'),
 'xdup-0209': ('商汤','shang-tang','D','2009-zhaonong','赵农记约前 1711 年灭夏、矿产资源与青铜文化，2016 记约前 1600 年成汤革夏；年代两说并列。'),
 'xdup-0212': ('大禹','dayu','D','2009-zhaonong','赵农记治水、农耕与“最早的规划设计师”评价，2016 记收九牧之金铸九鼎传说与九鼎成为传国重器。'),
 'xdup-0214': ('孙中山','sun-yat-sen','D','2016-xiayanjing','赵农记 1919 年《建国方略》东方大港与浦东市宅中心，2016 记中山装设计、形制寓意与剪辫易服法令。'),
 'xdup-0215': ('张光宇','zhang-guang-yu','C','2009-zhaonong','赵农记《万象》封面风格与 1949 年后字体设计，2016 记 1992 年《装饰》纪念张光宇特刊。'),
 'xdup-0217': ('张衡','zhang-heng','B','2016-xiayanjing','赵农记地动仪、浑天说与地图／指南车贡献，2016 记青铜浑天仪、候风地动仪结构与“形似酒尊”形制；2016 一处误作“张仪”。'),
 'xdup-0219': ('曾国藩','zeng-guofan','D','2016-xiayanjing','赵农只有洋务派群体一句，2016 详列安庆军械所、采买机器、江南机器制造总局、翻译馆、幼童留美五件实事。'),
 'xdup-0221': ('朱启钤','zhu-qijian','D','2009-zhaonong','赵农记营造学会、中国营造学社与《园冶》《梓人遗制》整理，2016 记 1927 年刊刻《髹饰录》及其乾坤两集结构。'),
 'xdup-0222': ('朱熹','zhu-xi','A','2011-lilixin','赵农记“男子有三紧”的服饰观，李立新记“简易”“致用”“道即器，器即道”与《训学斋规》器物整饬。'),
}
EXCLUDE={'xdup-0211':'夏燕靖'}
NO_TARGET={'xdup-0211':'来源作者简历／版本元数据，属来源 paratext，不构成中国设计史知识层的设计主体；不建立 person KU。'}

rows=[json.loads(l) for l in Path('06-runtime/state/candidate-index.jsonl').read_text(encoding='utf-8').splitlines() if l.strip()]
st={r['candidate_id']:r for r in rows}
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
for gid,reason in NO_TARGET.items():
    g=gs[gid]
    for m in g['members']:
        ledger.append({'candidate_id':m['candidate_id'],'expected_state':'needs_evidence','state':'rejected',
          'decision':{'status':'rejected','reason':reason,'decided_by':'Agent','decided_at':'2026-10-25'},'updated_at':'2026-10-25'})
    mapping.append({'group_id':gid,'entity':'夏燕靖','target_ref':None,'canonical_candidate':None,'merged_member':None,'decision':'rejected','action':'none','update_note':reason})

# order ledger: group by candidate first appearance, preserving chain order
seen={}; ordered=[]
for r in ledger:
    seen.setdefault(r['candidate_id'],[]).append(r)
for cid,rs in seen.items(): ordered.extend(rs)

(PKG/'apply-plan.jsonl').write_text('\n'.join(json.dumps(r,ensure_ascii=False) for r in plan)+'\n',encoding='utf-8',newline='\n')
(PKG/'candidate-decision-ledger.jsonl').write_text('\n'.join(json.dumps(r,ensure_ascii=False) for r in ordered)+'\n',encoding='utf-8',newline='\n')
print('plan',len(plan),'ledger',len(ordered),'groups',len(G)+len(NO_TARGET))
print(json.dumps(mapping,ensure_ascii=False,indent=1)[:1200])
