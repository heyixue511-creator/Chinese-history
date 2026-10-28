# -*- coding: utf-8 -*-
"""Build CL2i claim rows (Xia Yanjing 2009, ch.10 modern design)."""
import json
from pathlib import Path

ROOT = Path(r"D:/中国设计史研究")
DOC = "2009-xiayanjing-zhongguo-shejishi"
SRC = "03基础书籍-md文档/中国设计史_夏燕靖_2009_上海人民美术出版社.md"
DATE = "2026-10-27"
CH = "近现代史上的艺术设计"

ROWS = []


def Q(s: str) -> str:
    s = s.replace("‘", "“").replace("’", "”")
    assert '"' not in s, s
    return s


def C(cid, ctype, zh, en, confidence, supported, note, start, end, kind,
      key_lines, block_ids, section):
    ROWS.append({
        "claim_id": None,
        "statement_zh": Q(zh),
        "statement_en": en,
        "claim_type": ctype,
        "source": {
            "doc_id": DOC,
            "source_file": SRC,
            "source_span": {
                "line_start": start,
                "line_end": end,
                "span_kind": kind,
                "key_lines": key_lines,
                "block_ids": block_ids,
                "chapter": CH,
                "section": section,
            },
            "candidate_id": DOC + ":" + cid,
        },
        "confidence": confidence,
        "consensus": "tentative",
        "review_status": "source_backed",
        "supported_by": supported,
        "discussion_notes": Q(note),
        "created": DATE,
        "updated": DATE,
    })


C("cand-06-74", "historiographic_claim",
  "夏燕靖把 1840 年鸦片战争视为中国近代史的序幕，认为 19 世纪中叶以后西方主要资本主义国家向帝国主义阶段发展，中国虽已出现资本主义萌芽但基本上仍是古老的封建帝制国家，传统手工业由此进入重要的历史转折时期。",
  "Xia Yanjing treats the Opium War of 1840 as the opening of modern Chinese history: from the mid-nineteenth century the leading Western capitalist states moved toward imperialism, while China, though showing incipient capitalism, remained essentially an old feudal monarchy, and its traditional handicrafts entered a major historical transition.",
  "high",
  ["04-knowledge/units/events/opium-war.md",
   "04-knowledge/units/events/jiawu-haizhan.md",
   "04-knowledge/units/events/yangwu-yundong.md",
   "04-knowledge/units/terms/baomaizhu.md"],
  "候选作 periodization，路由 historiographic；断言合并 L3808 的世界格局、社会性质与鸦片战争分期意义，以及 L3816 的传统手工业转折判断，跨度 L3808-L3816，中间隔图 10-1、10-2 与两行图注，记 contiguous。L3808 句末“延续了两千多年”与 L3816 句首“的封建社会”被图版切开，按文意连读；不把 L3816 后段商品倾销、甲午战后民族工业等具体过程并入本条。李立新“早期工业化”条（terms/zaoqi-gongyehua.md）明确指明代中后期并与近现代工业化相区别，故不作本条承载单元。",
  3808, 3816, "contiguous", [3808, 3816], ["b0449"], "章首导论")

C("cand-06-59", "interpretive_claim",
  "夏燕靖认为，中国近代艺术设计伴随近代手工业和对外贸易萌生发展；抗日战争爆发中断了这些新兴设计行业的脉络，抗战胜利后又因内战与政局不稳，现代工艺与设计仅局限于少数沿海城市并走向衰落。",
  "Xia Yanjing argues that modern Chinese art design emerged and developed alongside modern handicrafts and foreign trade; the outbreak of the War of Resistance cut off these new design industries, and after 1945 civil war and political instability confined modern craft and design to a few coastal cities, where they declined.",
  "medium",
  ["04-knowledge/units/events/opium-war.md",
   "04-knowledge/units/terms/baomaizhu.md",
   "04-knowledge/units/places/shanghai.md"],
  "候选作 interpretation，路由 interpretive；断言取 L3822。同段列举 20 世纪初商品属性转变、机器印花、商品与包装设计、装潢美化，以及抗战时期手工艺人改行流离，均作为背景，不逐项并入。来源未给抗战前后设计行业规模、城市名单与统计数据，“少数沿海城市”保留作者概括；抗战无独立 KU，本条以 places/shanghai.md 作为沿海城市语境承载，medium。",
  3822, 3822, "line", [3822], ["b0450"], "1. 伴随近代手工业和对外贸易发展起来的艺术设计")

C("cand-06-60", "interpretive_claim",
  "夏燕靖指出，中国近代机器工业不是在资本主义萌芽基础上自然发展起来的，而是在欧风美雨的刺激下产生的；它缺乏资本原始积累条件，无法先由民间资本投资创办，而由洋务派封建官僚倡办新式机器工业拉开序幕。",
  "Xia Yanjing points out that modern machine industry in China did not grow naturally out of incipient capitalism but arose under the stimulus of Western influence; lacking the conditions for primitive capital accumulation, it could not be initiated by private capital and was instead opened by machine industry founded by Self-Strengthening bureaucrats.",
  "high",
  ["04-knowledge/units/events/opium-war.md",
   "04-knowledge/units/events/yangwu-yundong.md",
   "04-knowledge/units/institutions/jiangnan-zhizao-zongju.md",
   "04-knowledge/units/institutions/fujian-chuanzhengju.md"],
  "候选作 interpretation，路由 interpretive；断言取 L3828。高丰 claim-0025 已从整体路径判断中国近代工业由外国机器工业移植而来，本条补出“缺乏资本原始积累”与“洋务派官僚倡办”两个机制环节，主题相近而断点不同，不合并。同段末句“民族资本主义产生于 19 世纪六七十年代”属另一断言，未并入。",
  3828, 3828, "line", [3828], ["b0451"], "1. 伴随近代手工业和对外贸易发展起来的艺术设计｜知识链接：我国资本主义产生的历史背景")

C("cand-06-61", "interpretive_claim",
  "夏燕靖认为，中山装是在西装基本款形基础上糅合中国传统文化意识形成的，整体廓形垫肩收腰、均衡对称，穿着稳重大方；其四个口袋、前襟五粒钮扣与袖口三粒扣分别附会礼义廉耻、五权分立与三民主义。",
  "Xia Yanjing argues that the Zhongshan suit was formed by blending Chinese cultural meanings into a basic Western-suit cut, with padded shoulders, a fitted waist, symmetry and a dignified look; its four pockets, five front buttons and three cuff buttons were respectively associated with the four virtues, the five-power system and the Three Principles of the People.",
  "high",
  ["04-knowledge/units/terms/zhongshanzhuang.md",
   "04-knowledge/units/terms/xifu.md",
   "04-knowledge/units/persons/sun-yat-sen.md"],
  "候选作 interpretation，路由 interpretive；断言取 L3958。同段先述早期背面有缝、九粒钮扣与胖裥，再述定型款，本条取定型款及其寓意；来源以“据说”引出《易经》与周代礼仪依据，断言保留“附会”性质，不写成已证制度事实。terms/zhongshanzhuang.md 并列 2009 与赵农两说，terms/xifu.md 只承载西装基本款形背景。",
  3958, 3958, "line", [3958], ["b0466"], "3. 服饰设计水平的提高｜1）男装新制")

C("cand-06-62", "interpretive_claim",
  "夏燕靖指出，近代新出现的工业行当大多从国外引进机器、生产技术，利用中国廉价劳动力和原料设厂；上海等沿海城市机器行业的较大企业已设艺术设计部门并自行培养人才，但从严格意义上说，具有本土意识的产品造型设计尚未形成，仍处于萌芽或仿制加工阶段。",
  "Xia Yanjing points out that most new modern industries imported machines and production technology and set up factories using cheap Chinese labour and materials; larger machine-industry firms in Shanghai and other coastal cities established design departments and trained their own personnel, yet product styling with an indigenous sensibility had not yet formed and remained at an embryonic or imitation-processing stage.",
  "medium",
  ["04-knowledge/units/places/shanghai.md",
   "04-knowledge/units/institutions/jiangnan-zhizao-zongju.md",
   "04-knowledge/units/terms/baomaizhu.md"],
  "候选作 interpretation，路由 interpretive；断言取 L3994。同段“近代新出现的工业行当有 20 余种”与自行车、搪瓷、日用化工等清单，以及从修理、零部件到动力机器的阶段描述，作为背景保留，不逐项并入。来源未给企业名单、设计部门数量与人才规模，“尚未形成”是作者限定性判断，medium。terms/zaoqi-gongyehua.md 指明代中后期且明确区别于近现代工业化，不作本条承载。",
  3994, 3994, "line", [3994], ["b0470"], "4. 新兴产业的出现与艺术设计的新发展")

C("cand-06-63", "interpretive_claim",
  "夏燕靖认为，洋务运动是中国近代巨大社会变革的开始，是中国社会重要进程的标志之一，也是中国工业设计和现代设计孕育的土壤。",
  "Xia Yanjing argues that the Self-Strengthening Movement marked the beginning of China's great modern social transformation and was one of the landmarks of its social development, as well as the soil in which Chinese industrial design and modern design were nurtured.",
  "high",
  ["04-knowledge/units/events/yangwu-yundong.md",
   "04-knowledge/units/institutions/jiangnan-zhizao-zongju.md",
   "04-knowledge/units/institutions/fujian-chuanzhengju.md",
   "04-knowledge/units/persons/li-hongzhang.md",
   "04-knowledge/units/persons/zeng-guofan.md",
   "04-knowledge/units/persons/zuo-zongtang.md"],
  "候选作 interpretation，路由 interpretive；断言取 L4040。L4038 先论工业技术是生产力与强国之本，L4040 再由官办军工转民用企业、刺激民间投资推到历史定位；本条只取末句定位，不把曾国藩、左宗棠、李鸿章事迹并入。events/yangwu-yundong.md 已收 2016 版同一历史定位，persons/li-hongzhang.md、zeng-guofan.md、zuo-zongtang.md 承载人物背景。",
  4040, 4040, "line", [4040], ["b0473"], "4. 新兴产业的出现与艺术设计的新发展｜1）国外技术的引进与机器制造业的产生")

C("cand-06-64", "interpretive_claim",
  "夏燕靖把中国近代书籍装帧设计的风格特色概括为东方式的淡雅、朴素和内敛，并指出石版、铜版印刷技术逐渐改变传统雕版活字方式，鲁迅、陶元庆、钱君陶、丰子恺、陈之佛等推动书籍装帧向现代形态转变。",
  "Xia Yanjing characterizes modern Chinese book design as an Eastern style of quiet elegance, plainness and restraint, noting that lithographic and copperplate printing gradually changed traditional woodblock and movable-type methods, while Lu Xun, Tao Yuanqing, Qian Juntao, Feng Zikai and Chen Zhifo helped move book design toward a modern form.",
  "medium",
  ["04-knowledge/units/persons/lu-xun.md",
   "04-knowledge/units/persons/tao-yuanqing.md",
   "04-knowledge/units/persons/qian-juntao.md",
   "04-knowledge/units/persons/feng-zikai.md",
   "04-knowledge/units/persons/chen-zhifo.md",
   "04-knowledge/units/procedures/shiyin-ben.md",
   "04-knowledge/units/procedures/tongban-yinshua.md",
   "04-knowledge/units/publications/dianshizhai-huabao.md"],
  "候选作 interpretation，路由 interpretive；断言取 L4073 的风格概括，并以同节 L4073-L4094 的印刷技术与设计家群像作背景。本条只取首句与印刷技术、代表人物两组事实，不把《申报》《点石斋画报》《新青年》及各家风格细节并入。风格概括属整体判断，来源未给取样范围与比较对象，medium。",
  4073, 4073, "line", [4073], ["b0476"], "4. 新兴产业的出现与艺术设计的新发展｜3）书籍装帧艺术设计的发展与特色")

C("cand-06-65", "interpretive_claim",
  "夏燕靖认为，中国固有式建筑并不是纯传统的宫室式，而是受西方建筑思潮强烈影响、近于折衷主义的新形式；留学生与外国建筑师的参与使许多建筑留下模仿或拼凑的痕迹，南京金陵大学北大楼、北京辅仁大学教学楼是典型样式。",
  "Xia Yanjing argues that Chinese inherent-style architecture was not purely traditional palace architecture but a new, quasi-eclectic form strongly shaped by Western architectural currents; the involvement of returned students and foreign architects left many buildings with traces of imitation or patchwork, with Nanjing University's North Building and Beijing Fu Jen University's teaching building as typical examples.",
  "high",
  ["04-knowledge/units/terms/zhongguo-guyou-shi-jianzhu.md",
   "04-knowledge/units/terms/wailaishi-jianzhu.md",
   "04-knowledge/units/terms/zhongxi-hunheshi-jianzhu.md",
   "04-knowledge/units/publications/shanghai-center-plan.md"],
  "候选作 interpretation，路由 interpretive；断言取 L4108。L4106 的中国固有式定义、《上海市市中心区域规划》规定与五四背景，由 terms/zhongguo-guyou-shi-jianzhu.md、publications/shanghai-center-plan.md 承载；L4108 末句举金陵大学北大楼、辅仁大学教学楼。来源未给两校建筑的年代、建筑师与图纸，实例只作类型例证，不另建 works 条。",
  4108, 4108, "line", [4108], ["b0479"], "5. 建筑艺术的变迁与建筑装饰的兴起｜2）从中国固有样式建筑到现代中国样建筑")

C("cand-06-66", "interpretive_claim",
  "夏燕靖认为，中山陵是中国近代建筑史上首次具有规划设计意识的大型建筑群组，其重要意义在于摆脱纯欧化的模仿或拼凑，以新工艺、新材料改革传统建筑形式，为后来的传统式建筑树立典范；中山陵于民国十六年公开征图，吕彦直方案获首奖。",
  "Xia Yanjing argues that the Sun Yat-sen Mausoleum was the first large architectural complex in modern Chinese architectural history conceived with a planning consciousness; it broke away from purely Europeanized imitation or patchwork, reformed traditional forms with new techniques and materials, and set a model for later traditional-style architecture. The mausoleum held an open design competition in 1927, and Lu Yanzhi's scheme won first prize.",
  "high",
  ["04-knowledge/units/works/zhongshan-ling-1929.md",
   "04-knowledge/units/persons/lu-yanzhi.md",
   "04-knowledge/units/terms/zhongguo-guyou-shi-jianzhu.md",
   "04-knowledge/units/places/nanjing.md"],
  "候选作 interpretation，路由 interpretive；断言合并 L4116 的征图、吕彦直首奖与历史意义两层。同段引《凌鸿勋关于陵墓图案评判报告》《王一亭关于陵墓图案评判报告》“木铎警世”语，works/zhongshan-ling-1929.md 已收，本条不重复引文。来源记“民国十六年”，即 1927 年；persons/lu-yanzhi.md 同样记 1927 年竞图首奖，赵农记 1929 年设计，年代口径并列保留。",
  4116, 4116, "line", [4116], ["b0479"], "5. 建筑艺术的变迁与建筑装饰的兴起｜2）从中国固有样式建筑到现代中国样建筑")


def main():
    assert len(ROWS) == 9, len(ROWS)
    out = []
    for i, row in enumerate(ROWS):
        row["claim_id"] = "claim-%04d" % (238 + i)
        sp = row["source"]["source_span"]
        assert 3806 <= sp["line_start"] <= sp["line_end"] <= 4156, row["claim_id"]
        assert sp["key_lines"] and all(sp["line_start"] <= k <= sp["line_end"] for k in sp["key_lines"]), row["claim_id"]
        assert sp["block_ids"], row["claim_id"]
        assert sp["span_kind"] in {"line", "contiguous", "bounded"}, row["claim_id"]
        if sp["span_kind"] == "line":
            assert sp["line_start"] == sp["line_end"], row["claim_id"]
        for p in row["supported_by"]:
            assert p.startswith("04-knowledge/units/"), p
            assert (ROOT / p).exists(), p
        out.append(row)
    (ROOT / "_zn_claim_xyj09i_rows.json").write_text(
        json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
    from collections import Counter
    print(json.dumps({
        "claims": len(out),
        "with_support": sum(1 for r in out if r["supported_by"]),
        "links": sum(len(r["supported_by"]) for r in out),
        "distinct_support": len({p for r in out for p in r["supported_by"]}),
        "types": dict(Counter(r["claim_type"] for r in out)),
        "confidence": dict(Counter(r["confidence"] for r in out)),
        "span_kinds": dict(Counter(r["source"]["source_span"]["span_kind"] for r in out)),
    }, ensure_ascii=False))


if __name__ == "__main__":
    main()
