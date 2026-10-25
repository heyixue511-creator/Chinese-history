from pathlib import Path
checks = {
 '04-knowledge/units/terms/an-furniture.md': ['沙河顶','蹄状','40厘米','8.6'],
 '04-knowledge/units/works/yuan-yinjingjia.md': ['双凤','玉兔','蟾蜍','32.8','17.8'],
 '04-knowledge/units/terms/tihuaji.md': ['李约瑟','4个世纪','王逸','机妇赋'],
 '04-knowledge/units/terms/longyao.md': ['上虞','余姚','宁波','永嘉','共烧','1300'],
 '04-knowledge/units/terms/dougong.md': ['秦汉','硬山','悬山','交棂窗','叠架','庑殿'],
 '04-knowledge/units/places/yungang-shiku.md': ['中国形式','中国化','犍陀罗','3世纪'],
 '04-knowledge/units/terms/chai-yao.md': ['片瓦值千金','秘色','钱氏','郑州','雨过天青'],
 '04-knowledge/units/terms/guan-yao.md': ['大开片','粉青','月色','大绿','胎体较厚'],
 '04-knowledge/units/terms/qingtong-liqi.md': ['祀与戎','万物有灵','饮食器','玉琮','苍璧'],
 '04-knowledge/units/works/san-jiao-lou.md': ['耧犁','日种一顷','扶把','木斗','赵过'],
 '04-knowledge/units/publications/zhouyi.md': ['文王','韦编三绝','系辞','立器','形而上','制器者尚其象'],
 '04-knowledge/units/places/dunhuang-mogao-ku.md': ['366','乐傅','中心塔柱','千佛洞','砂砾岩','353','492','39'],
 '04-knowledge/units/works/kaifeng-xiangguosi-pagoda.md': ['蹬道','中心塔柱','锈铁','琉璃瓦','开封'],
 '04-knowledge/units/works/miaoying-si-baita.md': ['53','阿尼哥','至元八年','1271'],
 '04-knowledge/units/institutions/fujian-chuanzhengju.md': ['天津机器局','旅顺','广东军装','1866','黄鹄'],
 '04-knowledge/units/procedures/jiazhu-tai.md': ['行像','漆灰','脱胎'],
 '04-knowledge/units/terms/qian-you-tao.md': ['关中','硅酸','氧化铅','700','银釉'],
 '04-knowledge/units/terms/jiaoxie.md': ['阿斯塔那','垂拱','688','撮缬','晕染'],
 '04-knowledge/units/terms/wuda-mingyao.md': ['磁州','吉州','偏颇','民窑'],
 '04-knowledge/units/terms/nanjing-yunjin.md': ['蒙藏','明代风格','云纹','妆花','库锦','库缎'],
 '04-knowledge/units/terms/dulunche.md': ['鸡公车','羊角车','画像砖','绳带','肩颈','四川','木牛流马'],
 '04-knowledge/units/works/yuanmingyuan.md': ['郎世宁','罗可可','谐奇趣','长春园','西洋楼'],
 '04-knowledge/units/terms/yuefenpai.md': ['西画','木刻','肤浅','空前绝后','年画'],
 '04-knowledge/units/terms/zisha-tao.md': ['龚春','供春','时大彬','陈鸣远','邵大亨','杨彭年','四大家'],
 '04-knowledge/units/terms/yuexiu.md': ['洋庄','工艺局','汕头','49.675'],
 '04-knowledge/units/works/qin-shi-huang-ling.md': ['铜车马','御车马','1980','3000','安车','戎车'],
 '04-knowledge/units/institutions/zhongguo-meishuguan.md': ['1958','国庆工程','彩画','木雕','十大建筑'],
 '04-knowledge/units/persons/hang-zhiying.md': ['1920','练习生','商务印书馆','广告画家'],
 '04-knowledge/units/terms/wenzhi.md': ['绘事后素','质胜文则野','文胜质则史'],
 '04-knowledge/units/terms/jianghu.md': ['轮班','住坐','明代','232089','62个行业'],
 '04-knowledge/units/terms/lifang-zhi.md': ['夜禁','夜市','北宋','唐代','坊市'],
 '04-knowledge/units/works/liujin-wuma-xianbei-yinhu.md': ['屈膝衔杯','献寿','何家村','1970','皮囊'],
 '04-knowledge/units/terms/zhongshanzhuang.md': ['垫肩','收腰','廓形','4个口袋','5粒','3粒'],
 '04-knowledge/units/terms/kesi.md': ['贡品','新中国','镶色','父子世代'],
 '04-knowledge/units/persons/mozi.md': ['53篇','53 篇','光学','小孔成像'],
 '04-knowledge/units/publications/guanzi.md': ['前723','645','立政','雕饰','刻镂','文章'],
 '04-knowledge/units/works/houfeng-dizhenyi.md': ['78','139','阳嘉元年','都柱','八道','蟾蜍'],
}
for f, toks in checks.items():
    p = Path(f)
    if not p.exists():
        print('MISSING FILE', f); continue
    t = p.read_text(encoding='utf-8')
    miss = [x for x in toks if x not in t]
    print(('OK  ' if not miss else 'GAP '), f, '| missing:', ','.join(miss) if miss else '-')
