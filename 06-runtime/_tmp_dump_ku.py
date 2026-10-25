import re
from pathlib import Path
files = [x.strip() for x in Path('06-runtime/_tmp_targets.txt').read_text(encoding='utf-8').splitlines() if x.strip()]
out=[]
for f in files:
    t = Path(f).read_text(encoding='utf-8')
    title = re.search(r'^title: (.+)$', t, re.M).group(1)
    desc = re.search(r'## 描述\n\n(.+?)\n\n## ', t, re.S)
    core = re.search(r'## 核心内容\n\n(.*?)\n\n## ', t, re.S)
    mq = re.search(r'- 匹配质量: (.+)$', t, re.M)
    out.append('##### '+f+' | '+title)
    out.append('D: '+(desc.group(1).replace('\n',' ') if desc else ''))
    out.append('C:')
    if core:
        for ln in core.group(1).splitlines():
            if ln.strip().startswith('- '): out.append(ln)
    out.append('MQ: '+(mq.group(1) if mq else ''))
Path('06-runtime/_tmp_dump_ku.txt').write_text('\n'.join(out)+'\n', encoding='utf-8')
print(len(out))
