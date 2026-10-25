import hashlib
from pathlib import Path

DOC = {
 '2004': ('2004-gaofeng-zhongguo-shejishi','中国设计史_高丰_2004_广西美术出版社.md','高丰','中国设计史','广西美术出版社','2004'),
 '2009xy': ('2009-xiayanjing-zhongguo-shejishi','中国设计史_夏燕靖_2009_上海人民美术出版社.md','夏燕靖','中国设计史','上海: 上海人民美术出版社','2009'),
 '2009zn': ('2009-zhaonong-zhongguo-yishu-shejishi','中国艺术设计史_赵农_2009_高等教育出版社.md','赵农','中国艺术设计史','北京: 高等教育出版社','2009'),
 '2010': ('2010-tianzibing-zhongguo-gongyi-meishushi','中国工艺美术史（修订本）_田自秉_2010_东方出版中心.md','田自秉','中国工艺美术史（修订本）','上海: 东方出版中心','2010'),
 '2011': ('2011-lilixin-zhongguo-sheji-yishu-shilun','中国设计艺术史论_李立新_2011_人民出版社.md','李立新','中国设计艺术史论','北京: 人民出版社','2011'),
 '2016': ('2016-xiayanjing-zhongguo-yishu-shejishi-upgrade','中国艺术设计史（升级版）_夏燕靖_2016_上海人民美术出版社.md','夏燕靖','中国艺术设计史（升级版）','上海: 上海人民美术出版社','2016'),
}
D = {'A':'设计史观与史学方法','B':'造物、工艺与生产技术','C':'视觉传达与文字设计','D':'商业、制度与设计教育','E':'现代性与跨文化互动'}

def render(units, outdir='04-knowledge/units/institutions'):
    out=[]
    for u in units:
        srcs=[]; docs=[]
        for key,loc in u['srcs']:
            doc,fn,author,book,pub,year=DOC[key]
            if doc not in docs: docs.append(doc)
            srcs.append(f'  - citation: "{author}, *{book}* ({pub}, {year}), {loc}."\n    location: "{loc}"\n    evidence_ref:\n      doc_id: {doc}\n      source_file: 03基础书籍-md文档/{fn}\n      chapter_id: null\n      chunk_id: null')
        tags='\n'.join(f'  - {t}' for t in u['tags'])
        extra=''
        if u.get('aliases'):
            extra+='aliases:\n'+'\n'.join(f'  - {a}' for a in u['aliases'])+'\n'
        if u.get('location'): extra+=f'location: {u["location"]}\n'
        if u.get('active_period'): extra+=f'active_period: {u["active_period"]}\n'
        bullets='\n'.join('- '+b for b in u['bullets'])
        refs=[f'{DOC[k][2]}. *{DOC[k][3]}*. {DOC[k][4]}, {DOC[k][5]}.' for k in DOC if DOC[k][0] in docs]
        refblock='\n'.join(f'{i+1}. {r}' for i,r in enumerate(refs))
        text=f'''---
title: {u["title"]}（{u["en"]}）
name_en: {u["en"]}
type: institution
sub_type: {u["sub"]}
name_original: {u["orig"]}
name_original_language: zh
name_zh: {u["orig"]}
translation_status: provisional
translation_note: {u["tn"]}
tags:
{tags}
{extra}sources:
{chr(10).join(srcs)}
created: 2026-10-25
updated: 2026-10-25
confidence: medium
consensus: tentative
source_count: {len(u["srcs"])}
last_verified: 2026-10-25
review_due: 2027-04-25
version: 1
evidence_status: source_backed
primary_domain: chinese-design-history
primary_dimension: {u["dim"]}
hierarchy_scope_note: "{u["scope"]}"
---

## 描述

{u["desc"]}

## 核心内容

{bullets}

## 在层级体系中的位置

- primary_domain: chinese-design-history
- primary_dimension: {u["dim"]}（{D[u["dim"]]}）
- primary_theme: 未建立；Theme 尚未 materialize
- topic_memberships: 无；Topic 尚未 materialize
- role_in_theme: 未定
- scope_note: {u["scope"]}

## 相关知识元

{u["related"]}

## 验证状态

- 证据状态: source_backed（来源内复读）
- 验证层级: 未评定；consensus 为 tentative，按字段契约不填 L1–L7
- 验证平台: 未使用外部平台
- 匹配质量: {u["verif"]}
- 验证日期: 2026-10-25
- 证据范围: 仅前六册 Markdown 文本；未做来源外核对

## 参考文献

{refblock}
'''
        p=Path(outdir)/(u['slug']+'.md'); p.parent.mkdir(parents=True,exist_ok=True)
        p.write_text(text,encoding='utf-8',newline='\n')
        t=text.replace('\r\n','\n'); b=t.encode()
        out.append((u['slug'],'sha256:'+hashlib.sha256(b).hexdigest(),len(b),t.count('\n')))
    return out
