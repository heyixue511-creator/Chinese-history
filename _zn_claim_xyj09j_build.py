# -*- coding: utf-8 -*-
"""Build CL2j claim rows for Xia Yanjing 2009, New China chapter and postscript."""
import json
from pathlib import Path

ROOT = Path(r"D:/中国设计史研究")
DOC = "2009-xiayanjing-zhongguo-shejishi"
SRC = "03基础书籍-md文档/中国设计史_夏燕靖_2009_上海人民美术出版社.md"
DATE = "2026-10-27"
CH_NEW = "新中国时期的艺术设计"
SEC_NEW = "4. 新时期的工艺美术及面向 21 世纪的艺术设计事业"
SEC_CHRON = "当代中国工艺美术、艺术设计大事年表（1949～2000）"
ROWS = []


def Q(s: str) -> str:
    s = s.replace("‘", "“").replace("’", "”")
    assert '"' not in s, s
    return s


def C(cid, ctype, zh, en, confidence, supported, note, start, end, kind,
      key_lines, block_ids, chapter, section):
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
                "chapter": chapter,
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


C("cand-06-67", "historiographic_claim",
  "夏燕靖把新中国艺术设计分为两大历史阶段：新中国建立初期至20世纪80年代初，"
  "是艺术设计的前身工艺美术恢复、发展、徘徊和转型的时期；改革开放以来，"
  "是艺术设计从孕育走向成熟并不断发展与更新的时期。",
  "Xia Yanjing divides the history of design in New China into two major stages: "
  "from the founding of the People's Republic to the early 1980s, a period in which "
  "craft art, the predecessor of art design, was restored, developed, hesitated and "
  "transformed; and from the beginning of reform and opening up onward, a period in "
  "which art design moved from gestation to maturity and continued to develop and renew.",
  "high",
  ["04-knowledge/units/events/craft-recovery-transformation-1950s.md",
   "04-knowledge/units/events/party-third-plenum.md",
   "04-knowledge/units/events/1998-moe-major-catalog.md"],
  "候选作 periodization，路由 historiographic；断言取 L4159 章首导语。来源把两阶段展开为"
  "恢复、发展、徘徊、转型与孕育、成熟、更新，本条只取分期骨架，不并入后文"
  "“可喜成绩”“朝阳产业”等评价。",
  4159, 4159, "line", [4159], ["b0484"], CH_NEW, "章首导论")

C("cand-06-68", "interpretive_claim",
  "夏燕靖指出，中央工艺美术学院建院初期提出三种办学思路，其中以手工艺工人为主、"
  "师徒相授的作坊式教学与接受欧美综合设计思想两种思路差异很大；本属教学范畴的"
  "学术主张之争后来演变为尖锐冲突，在反右运动中那些主张“设计之路”的学者蒙受不幸的人生灾难。",
  "Xia Yanjing points out that the Central Academy of Arts and Design proposed three "
  "educational approaches in its early years; the workshop model centered on handicraft "
  "workers and the approach that embraced comprehensive European and American design ideas "
  "differed greatly, and an academic debate that originally belonged to teaching later turned "
  "into a sharp conflict, in which scholars who advocated a design path suffered tragic "
  "personal consequences during the Anti-Rightist Campaign.",
  "high",
  ["04-knowledge/units/institutions/central-academy-arts-design.md",
   "04-knowledge/units/persons/pang-xunqin.md"],
  "候选作 interpretation，路由 interpretive；断言取 L4285。同段列三种办学思路，本条只括出"
  "前两种的差异与后果，第三种民族民间装饰艺术路线未展开；来源以“设计之路”指称当时主张，"
  "不把“设计之路”写成既有术语。",
  4285, 4285, "line", [4285], ["b0492"], CH_NEW,
  "2. 全面建设社会主义时期的工艺美术")

C("cand-06-69", "interpretive_claim",
  "夏燕靖指出，人民大会堂室内设计首次聘请装饰设计专家和画家、雕塑家配合建筑师；"
  "周恩来决定将人民大会堂近30个厅分别包给各省市人民政府，由各省市结合自身特点完成"
  "接见厅的室内、家具和纺织面料设计并负责施工，这一决定启动了全国各省市对室内设计的重视，"
  "推动了我国室内设计的发展。",
  "Xia Yanjing points out that the interior design of the Great Hall of the People was the "
  "first to hire decorative design specialists, painters and sculptors to work with architects; "
  "Zhou Enlai decided to allocate nearly 30 halls of the Great Hall to provincial and municipal "
  "governments, which were to design and produce the interiors, furniture and textile fabrics for "
  "their reception halls in light of local characteristics. This decision drew nationwide attention "
  "to interior design and promoted its development in China.",
  "high",
  ["04-knowledge/units/works/renmin-dahuitang-1959.md",
   "04-knowledge/units/events/beijing-ten-great-buildings.md",
   "04-knowledge/units/persons/zhou-enlai.md"],
  "候选作 interpretation，路由 interpretive；断言取 L4305。来源记“首次聘请”，未给比较对象"
  "与全国范围内其他案例；近30个厅为约数。周恩来分包决定与各省市设计制作、施工的因果链"
  "按原文保留。",
  4305, 4305, "line", [4305], ["b0494"], CH_NEW,
  "2. 全面建设社会主义时期的工艺美术")

C("cand-06-70", "interpretive_claim",
  "夏燕靖认为，“文革”期间工艺美术是在曲折中艰难地行进，这种有限的发展是在老一辈革命家"
  "力主下针对“四人帮”倒行逆施才获得的；到1976年全国工艺美术产值为23.4亿元，"
  "比1972年的10亿元增长118%。",
  "Xia Yanjing argues that craft art during the Cultural Revolution advanced with difficulty, "
  "and that its limited development was obtained under the insistence of veteran revolutionaries "
  "against the perverse actions of the Gang of Four; by 1976 the national output value of craft "
  "art was 2.34 billion yuan, an increase of 118% over the 1 billion yuan of 1972.",
  "high",
  ["04-knowledge/units/events/cultural-revolution-crafts-four-olds.md",
   "04-knowledge/units/events/1972-1976-dingci-huifu.md",
   "04-knowledge/units/events/national-craft-exhibition-1972.md",
   "04-knowledge/units/events/zhou-enlai-handicraft-1972.md",
   "04-knowledge/units/works/great-wall-tapestry.md"],
  "候选作 interpretation，路由 interpretive；断言取 L4339。来源原文作“$118\\%$”，本条规范为"
  "“118%”；23.4亿元与10亿元均为来源统计，未给统计口径。works/great-wall-tapestry.md "
  "同记1976年23.4亿元，用于承载产值数字。",
  4339, 4339, "line", [4339], ["b0496"], CH_NEW,
  "3. “文革”时期的工艺美术")

C("cand-06-71", "interpretive_claim",
  "夏燕靖指出，“文革”时期书籍装帧几乎都与政治挂钩，主要参照毛泽东著作和马恩列斯著作的"
  "版式设计；《红旗》《解放军文艺》是当时期刊装帧设计的代表，“红、光、亮”审美原则主宰了"
  "当时的书籍设计，书籍装帧呈现空洞、单调、贫乏的面貌。",
  "Xia Yanjing points out that book binding during the Cultural Revolution was almost entirely "
  "tied to politics and mainly followed the layouts of Mao Zedong's works and those of Marx, "
  "Engels, Lenin and Stalin; Red Flag and Liberation Army Literature and Art were representative "
  "periodical designs of the time, and the red, bright and shining aesthetic principle dominated "
  "book design, which presented an empty, monotonous and impoverished appearance.",
  "high",
  ["04-knowledge/units/terms/hong-haiyang.md",
   "04-knowledge/units/publications/hongqi.md",
   "04-knowledge/units/publications/jiefangjun-wenyi.md",
   "04-knowledge/units/events/cultural-revolution-crafts-four-olds.md"],
  "候选作 interpretation，路由 interpretive；断言取 L4358。末句“空洞、单调、贫乏”是来源的"
  "评价性总结，本条保留为作者判断，不改写为可量化事实，也不单独路由 evaluative，"
  "因为断言主干是政治化装帧与审美原则的历史描述。",
  4358, 4358, "line", [4358], ["b0497"], CH_NEW,
  "3. “文革”时期的工艺美术")

C("cand-06-72", "interpretive_claim",
  "夏燕靖认为，20世纪80年代中后期以来，我国现代工业形成完整产业体系并在市场经济中"
  "飞速发展，工艺美术的特殊经济地位随之失落；失去国家政策性扶持后，整个工艺美术行业"
  "备受市场经济冲击，成为受创最重的行业，许多企业倒闭或转产，一些历史悠久的工艺品种"
  "逐渐消失甚至人亡艺绝。",
  "Xia Yanjing argues that from the mid-to-late 1980s onward, China's modern industry formed "
  "a complete industrial system and grew rapidly in the market economy, while craft art lost its "
  "special economic position; after losing state policy support, the entire craft-art industry was "
  "hit hard by the market economy and became the sector most severely damaged, with many enterprises "
  "closing or converting production and some long-established craft varieties gradually disappearing, "
  "in some cases along with their artisans.",
  "medium",
  ["04-knowledge/units/publications/chuantong-gongyi-meishu-baohu-tiaoli.md",
   "04-knowledge/units/terms/gongyi-meishu.md"],
  "候选作 interpretation，路由 interpretive；断言取 L4385。来源同段先记1983年产值超过50亿元"
  "与80年代发展顶峰，本条只取80年代中后期转折及其后果；“受创最重”“人亡艺绝”为来源判断，"
  "未给企业数、品种数与地区分布。当前无直接记录1990年代工艺美术企业倒闭的 KU，"
  "仅以保护条例与学科更名为制度语境。",
  4385, 4385, "line", [4385], ["b0499"], CH_NEW, SEC_NEW)

C("cand-06-73", "interpretive_claim",
  "夏燕靖认为，面向21世纪，我国现代设计仍然处于摸索之中，许多设计实践尚处在引进、"
  "学习与消化过程中；影响我国现代设计发展的核心因素仍然是科技创新与设计研发，"
  "关键问题在于设计教育与制造产业的需求如何形成有效接口。",
  "Xia Yanjing argues that, facing the twenty-first century, China's modern design is still "
  "groping its way, and many design practices are still in the process of importation, learning "
  "and digestion; the core factor affecting the development of modern design remains technological "
  "innovation and design research and development, and the key question is how design education "
  "and the needs of the manufacturing industry can form an effective interface.",
  "medium",
  ["04-knowledge/units/terms/industrial-design.md",
   "04-knowledge/units/events/1998-moe-major-catalog.md",
   "04-knowledge/units/events/1999-design-education-forum.md",
   "04-knowledge/units/institutions/central-academy-arts-design.md"],
  "候选作 interpretation，路由 interpretive；断言取 L4456 与 L4460，记 contiguous。"
  "两关键行之间的 L4457-L4459 是“知识链接：动画”框，排录插入正文，故首句“工业产品”"
  "与次句“设计，从电器到手机”被切断；本条只取框前后的论断，不把动画内容并入。"
  "设计教育与制造产业接口的判断无统计支撑，记 medium。",
  4456, 4460, "contiguous", [4456, 4460], ["b0504"], CH_NEW, SEC_NEW)

C("cand-07-10", "factual_claim",
  "夏燕靖指出，1966年5月“文化大革命”开始后，全国工艺美术行业受到严重破坏，"
  "传统工艺品一律被打成“四旧”而遭禁锢。",
  "Xia Yanjing points out that after the Cultural Revolution began in May 1966, the national "
  "craft-art industry was severely damaged, and traditional craft products were all labeled "
  "the Four Olds and banned.",
  "high",
  ["04-knowledge/units/events/cultural-revolution-crafts-four-olds.md"],
  "候选作 interpretation，路由 factual；断言取 L4698 大事年表。内容是1966年5月的时点事件"
  "与行业处置，按事实性断言路由；“严重破坏”是来源总评，本条不另量化。"
  "events/cultural-revolution-crafts-four-olds.md 同记该句并补1970年产值下降47%。",
  4698, 4698, "line", [4698], ["b0527"], CH_NEW, SEC_CHRON)

C("cand-07-18", "interpretive_claim",
  "夏燕靖指出，中央工艺美术学院编辑出版的《工艺美术参考》从1983年起重点发表有关"
  "工业设计教育的文论，引发全国设计教育培养方向的讨论。",
  "Xia Yanjing points out that Craft Art Reference, edited and published by the Central Academy "
  "of Arts and Design, began in 1983 to focus on essays about industrial design education, "
  "triggering a nationwide discussion of the direction of design education.",
  "medium",
  ["04-knowledge/units/publications/gongyi-meishu-cankao.md",
   "04-knowledge/units/institutions/central-academy-arts-design.md"],
  "候选作 interpretation，路由 interpretive；断言取 L4790。来源只记1983年1月《工艺美术参考》"
  "的转向与“引发讨论”，未给文章、作者、期数与讨论范围；"
  "publications/gongyi-meishu-cankao.md 另记该刊1982年7月1日出版，两处时间口径并列，"
  "不合并为同一天。",
  4790, 4790, "line", [4790], ["b0534"], CH_NEW, SEC_CHRON)

C("cand-07-22", "factual_claim",
  "夏燕靖据纺织工业部统计指出，1994年底中国成衣出口已占世界第一位，达232.7亿美元，"
  "成为国家出口的支柱行业。",
  "Citing statistics from the Ministry of the Textile Industry, Xia Yanjing points out that by "
  "the end of 1994 China's garment exports ranked first in the world, reaching 23.27 billion "
  "US dollars, and became a pillar of the country's exports.",
  "medium",
  [],
  "候选作 basic_fact，路由 factual；断言取 L4960。来源原文作“232，7亿美元”，显系小数点"
  "误作逗号，本条规范为“232.7亿美元”，并在断言中保留“据纺织工业部统计”的来源归属。"
  "当前无纺织工业部或成衣出口的 KU，supported_by 为空。",
  4960, 4960, "line", [4960], ["b0544"], CH_NEW, SEC_CHRON)

C("cand-07-23", "factual_claim",
  "夏燕靖指出，1998年7月，教育部颁布《普通高等学校本科专业目录》，"
  "将“工艺美术专业”改为“艺术设计专业”。",
  "Xia Yanjing points out that in July 1998 the Ministry of Education issued the Catalogue of "
  "Undergraduate Majors for Ordinary Higher Education Institutions, changing the major of craft "
  "art to the major of art design.",
  "high",
  ["04-knowledge/units/events/1998-moe-major-catalog.md",
   "04-knowledge/units/publications/putong-gaoxiao-benke-zhuanye-mulu.md",
   "04-knowledge/units/institutions/jiaoyubu.md"],
  "候选作 basic_fact，路由 factual；断言取 L5016。1998年7月、教育部、"
  "《普通高等学校本科专业目录》与专业改名四项均按原文；"
  "events/1998-moe-major-catalog.md、publications/putong-gaoxiao-benke-zhuanye-mulu.md "
  "与 institutions/jiaoyubu.md 均记同一事件。",
  5016, 5016, "line", [5016], ["b0548"], CH_NEW, SEC_CHRON)

C("cand-07-24", "interpretive_claim",
  "夏燕靖在《后记》中说明，设计史与工艺史的主要区别未能明晰，甚至出现较多重叠，"
  "因此本教程需要重新结构，明确勾画艺术设计史的叙事脉络。",
  "In the postscript, Xia Yanjing explains that the main differences between design history and "
  "craft history had not been clarified and that the two even overlapped considerably, so the "
  "textbook needed to be restructured to clearly delineate the narrative thread of art-design history.",
  "medium",
  ["04-knowledge/units/terms/yishu-shejishi.md",
   "04-knowledge/units/terms/gongyi-meishu.md"],
  "候选作 interpretation，路由 interpretive；断言取 L5380《后记》。这是作者对旧稿叙事方式的"
  "自我检讨，不是对学界总体状况的统计判断；“设计史与工艺史的主要区别未能明晰”按原文引语保留。"
  "terms/yishu-shejishi.md 与 terms/gongyi-meishu.md 只作跨作者概念语境，"
  "不构成对夏燕靖自述的旁证。",
  5380, 5380, "line", [5380], ["b0602"], "后记", None)

C("cand-07-25", "interpretive_claim",
  "夏燕靖在《后记》中主张，教程应弄清设计史演变的来龙去脉、知识要点和文史背景，"
  "不能局限于一孔之见，而需尽可能多地包容学界已有的研究成果。",
  "In the postscript, Xia Yanjing argues that the textbook should clarify the origins and "
  "development of design history, its key knowledge points and its literary and historical "
  "background, and should not be confined to a single viewpoint but should incorporate as much "
  "existing scholarship as possible.",
  "medium",
  [],
  "候选作 interpretation，路由 interpretive；断言取 L5380《后记》。这是作者关于教程取材与"
  "写作方法的规范性主张，“尽可能多地包容学界已有的研究成果”按原文引语保留；"
  "当前无直接承载该方法的 KU，supported_by 为空。",
  5380, 5380, "line", [5380], ["b0602"], "后记", None)


def main():
    assert len(ROWS) == 13
    src_lines = (ROOT / SRC).read_text(encoding="utf-8").splitlines()
    for i, row in enumerate(ROWS):
        row["claim_id"] = "claim-%04d" % (247 + i)
        assert row["statement_zh"].startswith("夏燕靖"), row["claim_id"]
        assert '"' not in row["statement_zh"], row["claim_id"]
        assert row["consensus"] == "tentative"
        assert row["review_status"] == "source_backed"
        sp = row["source"]["source_span"]
        assert 4157 <= sp["line_start"] <= sp["line_end"] <= 5409, row["claim_id"]
        assert sp["key_lines"] and all(sp["line_start"] <= k <= sp["line_end"] for k in sp["key_lines"])
        assert sp["block_ids"]
        assert sp["span_kind"] in {"line", "contiguous", "bounded"}
        if sp["span_kind"] == "line":
            assert sp["line_start"] == sp["line_end"] == sp["key_lines"][0]
        if sp["span_kind"] == "contiguous":
            assert len(sp["key_lines"]) >= 2
        for path in row["supported_by"]:
            assert path.startswith("04-knowledge/units/"), path
            assert (ROOT / path).is_file(), path
        assert sp["line_end"] <= len(src_lines)
    out = ROOT / "_zn_claim_xyj09j_rows.json"
    out.write_text(json.dumps(ROWS, ensure_ascii=False, indent=1), encoding="utf-8")
    links = [p for r in ROWS for p in r["supported_by"]]
    print(json.dumps({
        "claims": len(ROWS),
        "ids": [ROWS[0]["claim_id"], ROWS[-1]["claim_id"]],
        "with_support": sum(1 for r in ROWS if r["supported_by"]),
        "links": len(links),
        "distinct_support": len(set(links)),
        "types": {t: sum(1 for r in ROWS if r["claim_type"] == t) for t in sorted({r["claim_type"] for r in ROWS})},
        "confidence": {c: sum(1 for r in ROWS if r["confidence"] == c) for c in ("high", "medium", "low")},
    }, ensure_ascii=False))


if __name__ == "__main__":
    main()
