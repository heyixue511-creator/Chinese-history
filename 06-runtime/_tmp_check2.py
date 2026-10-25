from pathlib import Path
import re
checks = {
 '04-knowledge/units/persons/pang-xunqin.md': ['1906','1925','1930','决澜社','中央工艺美术学院','工商美术'],
 '04-knowledge/units/places/longmen-shiku.md': ['宾阳洞','藻井','莲花','卷草'],
 '04-knowledge/units/terms/ganlan-shi.md': ['河姆渡','25米','榫卯','巢居'],
 '04-knowledge/units/works/caiqi-zuoping.md': ['蛇','鹿','凤','雀','蛙','50'],
 '04-knowledge/units/procedures/lamo-fa.md': ['商代','公元前五六世纪','春秋'],
 '04-knowledge/units/works/simuwu-ding.md': ['875','133','110','78','84.77','11.64','2.79'],
 '04-knowledge/units/terms/juancao-wen.md': ['响堂山','二方连续','敦煌','藻井'],
 '04-knowledge/units/terms/ru-yao.md': ['支钉','不足百件','粉青','豆青','卵青','虾青'],
 '04-knowledge/units/terms/ding-yao.md': ['芒口','泪痕','覆烧','奉华','聚秀'],
 '04-knowledge/units/persons/huang-cheng.md': ['隆庆','新安','髹饰录'],
 '04-knowledge/units/persons/li-jie.md': ['1103','崇宁二年','营造法式'],
 '04-knowledge/units/terms/shui-dui.md': ['西汉末年','舂米','水'],
}
for f, toks in checks.items():
    p = Path(f)
    if not p.exists():
        # try find by slug
        cands = list(Path('04-knowledge/units').rglob(Path(f).name))
        print('NOFILE', f, '->', [str(c) for c in cands]); continue
    t = p.read_text(encoding='utf-8')
    miss = [x for x in toks if x not in t]
    print(('OK  ' if not miss else 'GAP '), f, '|', ','.join(miss) if miss else '-')
print('--- aliases/sources ---')
for f in ['04-knowledge/units/terms/jianghu.md','04-knowledge/units/publications/guanzi.md','04-knowledge/units/terms/kesi.md','04-knowledge/units/works/qin-shi-huang-ling.md']:
    t = Path(f).read_text(encoding='utf-8')
    al = re.search(r'^aliases:\n((?:  - .+\n)+)', t, re.M)
    print(f, '| aliases:', al.group(1).replace('\n',' ') if al else 'none')
