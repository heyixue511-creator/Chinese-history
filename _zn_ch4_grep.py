# -*- coding: utf-8 -*-
import io, json, os, re, glob

rows = json.load(io.open('_zn_ch4_rows.json', encoding='utf-8'))
FILES = glob.glob('04-knowledge/units/**/*.md', recursive=True)
CORP = {}
for f in FILES:
    CORP[f] = io.open(f, encoding='utf-8').read()

def keyof(cid):
    return KEYS.get(cid)

KEYS = {
 'cand-04-40':'秦始皇','cand-04-42':'汉武帝','cand-04-43':'董仲舒','cand-04-45':'司马迁',
 'cand-04-47':'班固','cand-04-48':'汉书','cand-04-49':'许慎','cand-04-51':'论衡',
 'cand-04-52':'李斯','cand-04-53':'蔡伦','cand-04-56':'浑天说','cand-04-57':'四神',
 'cand-04-60':'秦半两','cand-04-61':'五铢','cand-04-64':'石鼓文','cand-04-65':'商鞅方升',
 'cand-04-66':'隶书','cand-04-67':'睡虎地','cand-04-68':'章草','cand-04-69':'居延',
 'cand-04-70':'楷书','cand-04-71':'钟繇','cand-04-72':'宣示表','cand-04-141':'程邈',
 'cand-04-74':'金错刀','cand-04-75':'王莽','cand-04-142':'马蹄金','cand-04-155':'麟趾金',
 'cand-04-156':'金五铢','cand-04-77':'驰道','cand-04-78':'车同轨','cand-04-80':'金根车',
 'cand-04-82':'张骞','cand-04-83':'班超','cand-04-84':'栈道','cand-04-85':'褒斜道',
 'cand-04-86':'灵渠','cand-04-87':'史禄','cand-04-88':'渭水三桥','cand-04-89':'灞桥',
 'cand-04-92':'青铜剑','cand-04-96':'弩机','cand-04-97':'环首刀','cand-04-98':'钩镶',
 'cand-04-99':'铠甲','cand-04-100':'耦犁','cand-04-103':'风车','cand-04-105':'石磨',
 'cand-04-106':'秦权','cand-04-107':'秦量','cand-04-109':'咸阳宫','cand-04-110':'未央宫',
 'cand-04-113':'门阙','cand-04-114':'嵩山三阙','cand-04-115':'武氏祠','cand-04-143':'萧何',
 'cand-04-118':'阿房宫','cand-04-119':'阿房宫赋','cand-04-121':'长城','cand-04-122':'蒙恬',
 'cand-04-123':'烽燧','cand-04-144':'卫青','cand-04-125':'霍去病墓石刻','cand-04-126':'马踏匈奴',
 'cand-04-127':'霍去病','cand-05-02':'覆斗','cand-05-106':'起绒锦','cand-05-09':'进贤冠',
 'cand-05-10':'兵马俑','cand-05-107':'禅衣','cand-05-108':'舄','cand-05-13':'透光镜',
 'cand-05-17':'被中香炉','cand-05-18':'西京杂记','cand-05-25':'地动仪','cand-05-21':'蔡侯纸',
 'cand-05-27':'司南','cand-05-30':'马王堆','cand-05-33':'动物形灯',
}

for r in rows:
    cid = r['candidate_id'].split(':')[1]
    k = KEYS.get(cid, r['payload'].get('title',''))
    tl, body = [], []
    for f, txt in CORP.items():
        head = txt[:600]
        if k in head:
            tl.append(os.path.basename(f)[:-3])
        n = txt.count(k)
        if n and k not in head:
            body.append('%s(%d)' % (os.path.basename(f)[:-3], n))
    print('%-14s %-8s TITLE/HEAD: %-40s BODY: %s' % (cid, k, ','.join(tl[:5]) or '-', ','.join(sorted(body)[:6]) or '-'))
