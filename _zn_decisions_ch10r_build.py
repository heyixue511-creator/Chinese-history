# -*- coding: utf-8 -*-
"""Build chapter 10 batch R decisions JSON from generated KU files."""
import json
from collections import Counter
from pathlib import Path

ROOT = Path(r"D:/中国设计史研究")
DOC = "2009-zhaonong-zhongguo-yishu-shejishi"
PREFIX = DOC + ":"

CREATES = [
    ("cand-12-122", "04-knowledge/units/persons/lin-zexu.md",
     "林则徐（1785—1850）是晚清官员。赵农在总结首段记其「虎门销烟」，并判断这对发动鸦片战争的英国政府只是借口。检索无同实体人物。按人物新建，证据行 L8502。来源只一句提及，未给任职、禁烟过程与销烟数量；原文把英国发动鸦片战争系于 1842 年，照录存疑。confidence 取 low。",
     "写入 04-knowledge/units/persons/lin-zexu.md（新建）；引用 L8502；年份照录存疑。"),
    ("cand-12-124", "04-knowledge/units/works/shuijinggong.md",
     "水晶宫是 1851 年英国「万国博览会」的钢铁、玻璃结构建筑。赵农称其出现揭开了现代艺术设计的序幕。检索无同实体条目；`institutions/` 下的博览会机构与建筑作品不同。按作品新建，证据行 L8502。来源未给设计者、建筑面积、结构尺寸与建造拆除年份，confidence 取 medium。",
     "写入 04-knowledge/units/works/shuijinggong.md（新建）；引用 L8502。"),
    ("cand-12-125", "04-knowledge/units/persons/wei-yuan.md",
     "魏源（1794—1857）是晚清学者。赵农记其放眼世界、主张变法，提出「师夷长技以制夷」的向西方学习观点，介绍蒸汽机、火轮船等西方生产技术，呼吁发展中国近代工业，并在《海国图志》中初步介绍西方民主政治制度。检索无同实体人物；`publications/` 无《海国图志》条。按人物新建，证据行 L8504。来源未给仕途、著述书目与思想分期，confidence 取 medium。",
     "写入 04-knowledge/units/persons/wei-yuan.md（新建）；引用 L8504。"),
    ("cand-12-128", "04-knowledge/units/persons/feng-guifen.md",
     "冯桂芬（1809—1874）是晚清学者。赵农记其在《校邠庐抗议》中提出「始则师而法之，继则比而齐之，终则驾而上之，自强之道，实在乎是」的自强理想，并把洋务派官员视为继承魏源思想者。检索无同实体人物。按人物新建，证据行 L8506。来源未给仕途、著述书目与变法活动，confidence 取 medium。",
     "写入 04-knowledge/units/persons/feng-guifen.md（新建）；引用 L8506。"),
    ("cand-12-129", "04-knowledge/units/publications/xiaobinlu-kangyi.md",
     "《校邠庐抗议》是冯桂芬的著述。赵农引其「始则师而法之，继则比而齐之，终则驾而上之，自强之道，实在乎是」，用以说明洋务运动前后的自强理想。检索无同实体出版物。按出版物新建，证据行 L8506。来源未给成书年份、卷数、刊本与全书结构，confidence 取 low。",
     "写入 04-knowledge/units/publications/xiaobinlu-kangyi.md（新建）；引用 L8506。"),
    ("cand-12-144", "04-knowledge/units/persons/chen-duxiu.md",
     "陈独秀（1880—1942）是新文化运动人物。赵农记其以《新青年》为阵地积聚文化精英，与胡适等人宣传「民主」和「科学」，反对封建专制，「打倒孔家店」，提倡「白话文」。检索无同实体人物。按人物新建，证据行 L8533。来源未给任职、著述书目与政治活动，confidence 取 medium。",
     "写入 04-knowledge/units/persons/chen-duxiu.md（新建）；引用 L8533。"),
    ("cand-12-146", "04-knowledge/units/persons/hu-shi.md",
     "胡适（1891—1962）是留美归国学者。赵农记其与陈独秀等人宣传「民主」和「科学」，反对封建专制，「打倒孔家店」，提倡「白话文」，倡导新文化运动。检索无同实体人物。按人物新建，证据行 L8533。来源未给学位、任教机构、著述书目与具体主张，confidence 取 medium。",
     "写入 04-knowledge/units/persons/hu-shi.md（新建）；引用 L8533。"),
    ("cand-12-148", "04-knowledge/units/persons/kang-youwei.md",
     "康有为（1858—1927）是晚清民初学者。赵农记其提出「取欧画写形之精，以补吾国之短」「合中西而为画学新纪元者」的想法，用以说明中国艺术知识向古典主义文化形态嫁接的取向。检索无同实体人物。按人物新建，证据行 L8533。来源未给政治活动、著述书目与画学主张全文，confidence 取 medium。",
     "写入 04-knowledge/units/persons/kang-youwei.md（新建）；引用 L8533。"),
    ("cand-12-149", "04-knowledge/units/terms/zhongguo-feng.md",
     "中国风是 17、18 世纪欧洲社会形成的对中国工艺与文化的风尚。赵农记中国瓷器、丝织品、漆器、壁纸、印刷术、火药、文化典籍对欧洲产生深远影响，欧洲社会在摆脱中世纪宗教压迫后形成「中国风」，并视为欧洲转型进入新文化环境的重要因素。检索无同实体术语。按术语新建，证据行 L8540。来源未给具体国家、年代分段、代表人物与器物谱系，confidence 取 medium。",
     "写入 04-knowledge/units/terms/zhongguo-feng.md（新建）；引用 L8540。"),
]


def title_of(path):
    for line in Path(path).read_text(encoding="utf-8").splitlines():
        if line.startswith("title:"):
            return line.split(":", 1)[1].strip().split("（")[0].strip()
    return Path(path).stem


decisions = []
for suffix, target, analysis, apply_note in CREATES:
    decisions.append({
        "cid": PREFIX + suffix,
        "entity": title_of(target),
        "action": "create",
        "target": target,
        "analysis": analysis,
        "approve": f"批准新建 {target}：单册单源，consensus=tentative，confidence 按证据厚度评定。",
        "apply_note": apply_note,
        "note": f"canonical: {target}。",
    })

cfg = {
    "doc": DOC,
    "file": "03基础书籍-md文档/中国艺术设计史_赵农_2009_高等教育出版社.md",
    "rules": [
        "单册单源新建：consensus=tentative，evidence_status=source_backed，source_count=1，version=1",
        "逐字引文用“ ”，作者判断用「 」，作者自撰短语不用引号，正文禁 ASCII 双引号",
        "总结段只作宏观判断时，条目只著录来源所说，不据来源外材料补生平、版本与器物谱系",
        "原文年份疑误照录并标注，不径改",
        "人物、著作、建筑与风尚术语按类型分列，不因同段出现而合并",
    ],
    "scope_spans": [[8484, 8560]],
    "scope_note": "赵农 2009 册「总结」L8484–L8560 逐段复读，含鸦片战争、洋务运动、新文化运动与欧洲中国风；候选 source_span 为块级粗跨度，实际引用行均落在本批范围内。图总结-1 至图总结-7 未视觉核验。",
    "decisions": decisions,
    "notes": "赵农 2009 册总结段 unit 候选 9 条，全部 create。范围 L8484-L8560。新建覆盖林则徐、魏源、冯桂芬、陈独秀、胡适、康有为六人，水晶宫一件建筑作品，《校邠庐抗议》一种著述，中国风一术语。曾国藩、左宗棠、李鸿章、张之洞、张謇、孙中山、郑观应、詹天佑等虽有提及，但不在本批候选内，未新建；《海国图志》《新青年》《建国方略》《盛世危言》等亦未在本批立目。图总结-1 至图总结-7 未视觉核验。",
}

out = ROOT / "_zn_decisions_ch10r.json"
out.write_text(json.dumps(cfg, ensure_ascii=False, indent=1) + "\n", encoding="utf-8", newline="\n")
print(Counter(d["action"] for d in decisions), len(decisions))
