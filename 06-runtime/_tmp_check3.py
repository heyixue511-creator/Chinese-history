from pathlib import Path
checks = {
 '04-knowledge/units/places/longmen-grottoes.md': ['宾阳洞','藻井','莲花','卷草','流苏'],
 '04-knowledge/units/terms/ganlan-shi-jianzhu.md': ['河姆渡','25米','榫卯','巢居','藤索'],
 '04-knowledge/units/works/caiqi-mudiao-dongwu-zuoping.md': ['蛇','鹿','凤','雀','蛙','50'],
 '04-knowledge/units/procedures/lost-wax-casting.md': ['商代','公元前五六世纪','春秋','蜡'],
 '04-knowledge/units/terms/rendong-wen.md': ['响堂山','二方连续','敦煌','藻井','卷草'],
 '04-knowledge/units/places/ru-kiln.md': ['支钉','不足百件','粉青','豆青','卵青','虾青','玉石'],
 '04-knowledge/units/places/ding-kiln.md': ['芒口','泪痕','覆烧','奉华','聚秀','竹丝刷纹'],
 '04-knowledge/units/persons/huang-dacheng.md': ['隆庆','新安','髹饰录'],
 '04-knowledge/units/persons/li-cheng.md': ['1103','崇宁二年'],
 '04-knowledge/units/works/shui-dui.md': ['西汉末年','舂米','水'],
}
for f, toks in checks.items():
    p = Path(f)
    if not p.exists(): print('NOFILE', f); continue
    t = p.read_text(encoding='utf-8')
    miss = [x for x in toks if x not in t]
    print(('OK  ' if not miss else 'GAP '), f, '|', ','.join(miss) if miss else '-')
