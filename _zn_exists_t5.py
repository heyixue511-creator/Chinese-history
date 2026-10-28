from pathlib import Path
u=Path(r"D:/中国设计史研究/04-knowledge/units")
names=["places/dingxian-hanmu.md","places/xinye.md","places/chengdu.md","places/tianghuishan.md","places/fenghuangshan-qinmu.md","places/hanjiang-ganquan.md","places/wuwei-leitai-hanmu.md","terms/kongxin-zhuan.md","terms/niaochong-shu.md","terms/cuojin-yinzhu.md","terms/jinsheng.md","terms/jin-yinqi.md","terms/qiqi.md","procedures/qiqi-zhizuo.md","procedures/cuojin-yinzhu.md","institutions/shaofu.md","terms/hu-vessel.md","terms/wadang.md","terms/hanjing.md","terms/mingqi.md","terms/li-cauldron.md","works/shiwu-lianzhan-tongdeng.md","works/wenjiu-tongbeilu.md","places/shuihudi-qinmu.md","places/xianyang.md","terms/yuhuchun-ping.md","terms/baigong.md","works/cuojin-boshanlu.md","works/changxin-palace-lamp.md","terms/tongjing.md","terms/dian-la-man.md"]
for n in names:
    print(("OK " if (u/n).exists() else "NO ")+n)
