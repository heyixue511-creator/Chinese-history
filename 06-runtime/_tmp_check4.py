from pathlib import Path
f='04-knowledge/units/persons/guan-zhong.md'
t=Path(f).read_text(encoding='utf-8')
for tok in ['前723','前645','夷吾','春秋第一相','立政','刻镂','文章','雕饰']:
    print(tok, tok in t)
import re
print(re.search(r'## 核心内容\n\n(.*?)\n\n##', t, re.S).group(1)[:1500])
print('---sources---')
print(re.findall(r'doc_id: (.+)', t)); print(re.findall(r'location: "(.+)"', t))
