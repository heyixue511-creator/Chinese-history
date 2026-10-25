import re
from pathlib import Path
files = """04-knowledge/units/terms/an-furniture.md
04-knowledge/units/works/yuan-yinjingjia.md
04-knowledge/units/terms/tihuaji.md
04-knowledge/units/terms/longyao.md
04-knowledge/units/terms/dougong.md
04-knowledge/units/places/yungang-shiku.md
04-knowledge/units/terms/chai-yao.md
04-knowledge/units/terms/guan-yao.md
04-knowledge/units/terms/qingtong-liqi.md
04-knowledge/units/works/san-jiao-lou.md
04-knowledge/units/publications/zhouyi.md
04-knowledge/units/places/dunhuang-mogao-ku.md
04-knowledge/units/works/kaifeng-xiangguosi-pagoda.md
04-knowledge/units/works/miaoying-si-baita.md
04-knowledge/units/institutions/fujian-chuanzhengju.md
04-knowledge/units/procedures/jiazhu-tai.md
04-knowledge/units/terms/qian-you-tao.md
04-knowledge/units/terms/jiaoxie.md
04-knowledge/units/terms/wuda-mingyao.md
04-knowledge/units/terms/nanjing-yunjin.md
04-knowledge/units/terms/dulunche.md
04-knowledge/units/works/yuanmingyuan.md
04-knowledge/units/terms/yuefenpai.md
04-knowledge/units/terms/zisha-tao.md
04-knowledge/units/terms/yuexiu.md
04-knowledge/units/works/qin-shi-huang-ling.md
04-knowledge/units/institutions/zhongguo-meishuguan.md
04-knowledge/units/persons/hang-zhiying.md
04-knowledge/units/terms/wenzhi.md
04-knowledge/units/terms/jianghu.md
04-knowledge/units/terms/lifang-zhi.md
04-knowledge/units/works/liujin-wuma-xianbei-yinhu.md
04-knowledge/units/terms/zhongshanzhuang.md
04-knowledge/units/terms/kesi.md
04-knowledge/units/persons/mozi.md
04-knowledge/units/publications/guanzi.md
04-knowledge/units/works/houfeng-dizhenyi.md""".split()
for f in files:
    t = Path(f).read_text(encoding='utf-8')
    sc = re.search(r'^source_count: (.+)$', t, re.M).group(1)
    v = re.search(r'^version: (.+)$', t, re.M).group(1)
    docs = re.findall(r'doc_id: (.+)', t)
    locs = re.findall(r'location: "(.+)"', t)
    print(f"{f} sc={sc} v={v}")
    for d, l in zip(docs, locs): print('   ', d, '|', l)
