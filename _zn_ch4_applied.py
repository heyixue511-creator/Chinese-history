# -*- coding: utf-8 -*-
import io, json
DOC='2009-zhaonong-zhongguo-yishu-shejishi'
CH='第四章 统一的气量——秦汉时期的设计'
for line in io.open('06-runtime/state/candidate-index.jsonl',encoding='utf-8'):
    line=line.strip()
    if not line: continue
    r=json.loads(line)
    if not str(r.get('candidate_id','')).startswith(DOC+':'): continue
    p=r.get('payload',{}); sp=p.get('source_span',{})
    if sp.get('chapter')!=CH: continue
    if r.get('candidate_type')!='unit': continue
    if r.get('state')=='needs_evidence': continue
    print('%-14s %-9s %-6s L%-5s-%-5s %-28s -> %s' % (
        r['candidate_id'].split(':')[1], r['state'], p.get('unit_type'), sp['line_start'], sp['line_end'], p.get('title'), r.get('target_ref')))
