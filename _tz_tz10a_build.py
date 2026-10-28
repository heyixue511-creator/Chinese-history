# -*- coding: utf-8 -*-
"""Build 田自秉 2010 claim rows, batch tz10a (modern craft, other crafts, conclusion, postscript; 8 claims)."""
import json
from pathlib import Path

ROOT = Path(r"D:/中国设计史研究")
DOC = "2010-tianzibing-zhongguo-gongyi-meishushi"
SRC = "03基础书籍-md文档/中国工艺美术史（修订本）_田自秉_2010_东方出版中心.md"
DATE = "2026-10-27"
CH = "第十三章 新中国的工艺美术（现代工艺、其他工艺、结语）与后记"

T = "04-knowledge/units/terms/"
P = "04-knowledge/units/places/"
W = "04-knowledge/units/works/"
PR = "04-knowledge/units/procedures/"
E = "04-knowledge/units/events/"
I = "04-knowledge/units/institutions/"
B = "04-knowledge/units/publications/"

MAP = ROOT / "03-processing/2010-tianzibing-zhongguo-gongyi-meishushi/source-map.jsonl"
BLOCKS = []
for line in MAP.read_text(encoding="utf-8").splitlines():
    if not line.strip():
        continue
    d = json.loads(line)
    BLOCKS.append((d["block_id"], d["line_start"], d["line_end"]))


def blocks(start, end):
    return [b for b, s, e in BLOCKS if s <= end and e >= start]


def Q(s: str) -> str:
    s = s.replace("‘", "“").replace("’", "”")
    assert '"' not in s, s
    return s


def C(claim_id, cand, ctype, zh, en, supported, note, start, end, key_lines, section):
    for p in supported:
        assert (ROOT / p).is_file(), p
    return {
        "claim_id": claim_id,
        "statement_zh": Q(zh),
        "statement_en": en,
        "claim_type": ctype,
        "source": {
            "doc_id": DOC,
            "source_file": SRC,
            "source_span": {
                "line_start": start,
                "line_end": end,
                "span_kind": "line" if start == end else "bounded",
                "key_lines": key_lines,
                "block_ids": blocks(start, end),
                "chapter": CH,
                "section": section,
            },
            "candidate_id": DOC + ":" + cand,
        },
        "confidence": "medium",
        "consensus": "tentative",
        "review_status": "source_backed",
        "supported_by": supported,
        "discussion_notes": Q(note),
        "created": DATE,
        "updated": DATE,
    }


rows = []

rows.append(C(
    "claim-1040", "cand-14-03", "synthetic_claim",
    "解放后，家具材料除继续沿用天然木材外，逐步采用胶合板、纤维板、刨花板、蜂窝板、细木板等人造板以及钢管和塑料；家具结构随之由传统框式向板式发展，使家具工艺设计更省工、轻便，并具有简洁、明快的艺术效果。",
    "After 1949, besides natural timber, furniture increasingly used plywood, fibreboard, particleboard, honeycomb board and blockboard as well as steel tubing and plastics; furniture structure accordingly began moving from traditional frame construction to panel construction, making design more labour-saving and lighter while giving a concise, bright artistic effect.",
    [T + "renzao-cailiao-jiaju.md", T + "gongyi-meishu.md"],
    "断言语义取 L5367。原文将材料替代、结构转变与设计效果三层判断连写，未给具体家具实例或统计；“开始”表明渐进过程，claim 不把板式结构说成全部家具的通例。",
    5367, 5367, [5367], "第十三章 第八节 现代工艺"))

rows.append(C(
    "claim-1041", "cand-14-05", "factual_claim",
    "我国民间很早就有春节用剪纸馈赠或装饰的习俗，唐代诗人李商隐“镂金作胜传荆俗，剪采为人起晋风”诗句即写这种生活。",
    "Folk custom in China long ago included giving or displaying paper-cuts at Spring Festival; Li Shangyin's Tang poem line, cutting gold into sheng ornaments carries the Jing custom and cutting coloured paper into figures rises from Jin ways, depicts this life.",
    [T + "jianzhi.md", T + "gongyi-meishu.md"],
    "断言语义取 L5375。原候选标 source_claim，按六类 claim 映射为 factual_claim。诗句“剪采”照录，今多作“剪彩”；原诗题、卷次未注，且“镂金作胜”写人日剪胜，与春节习俗不完全等同，属以诗证俗的间接旁证。",
    5375, 5375, [5375], "第十三章 第九节 其他工艺"))

rows.append(C(
    "claim-1042", "cand-14-06", "interpretive_claim",
    "剪纸因地域与生活习惯不同而形成地方特色：北方剪纸多取蔬菜、瓜果、劳动、家畜等题材，朴质浑厚、刚劲豪放；江南一带喜用春燕垂柳、亭桥帆影等景色，典雅清新、纤巧秀丽；河北剪纸常用彩色晕染，有染缬效果；广东剪纸多用金纸，色彩艳丽明快。",
    "Paper-cutting develops regional characters from differences of place and custom: northern work favours vegetables, fruit, labour and livestock, plain and vigorous; Jiangnan favours swallows, willows, pavilions, bridges and sails, elegant and delicate; Hebei often adds colour by shading with a resist-dye effect; Guangdong often uses gold paper with bright, vivid colour.",
    [T + "jianzhi.md", T + "gongyi-meishu.md"],
    "断言语义取 L5377。四地风格为作者类型化概括，未注取样范围、艺人或作品；“北方”“江南”为区域，“河北”“广东”为省份，层级不一，claim 保留原文并举结构。",
    5377, 5377, [5377], "第十三章 第九节 其他工艺"))

rows.append(C(
    "claim-1043", "cand-14-10", "historiographic_claim",
    "几千年间工艺美术一直为统治阶级所占有，落后的生产关系束缚着工艺美术的生产和发展；直到中国共产党领导的革命根据地和解放区，工艺美术才回到人民手中，为人民创作、为人民利用，发生了质的变化。",
    "For millennia craft was possessed by the ruling class, and backward relations of production constrained its production and development; only from the revolutionary base areas and liberated areas led by the Chinese Communist Party did craft return to the people, to be created for them and used by them, undergoing a qualitative change.",
    [T + "gongyi-meishu.md", I + "jiefangqu-diyige-taoci-yanjiusuo.md"],
    "断言语义取 L5383。以阶级与生产关系框架作通史分期判断，未给具体史料或统计；“一直”为全称判断，claim 保留原文强度，不弱化。",
    5383, 5383, [5383], "第十三章 第十节 结语"))

rows.append(C(
    "claim-1044", "cand-14-11", "evaluative_claim",
    "新中国工艺美术取得巨大成就：生产规模大、发展速度快，种类繁多、技艺精湛，工艺美术教育与科研机构从无到有、遍布全国；虽经“十年浩劫”严重摧残，但党的十一届三中全会后拨乱反正、改革开放，又迅速重新蓬勃发展。",
    "New China's arts and crafts achieved great results: large-scale, fast-growing production, many kinds and refined techniques, and craft education and research institutions built from nothing across the country; though severely damaged in the ten years of havoc, they revived quickly after the Third Plenary Session of the Eleventh Central Committee through rectification and reform and opening.",
    [E + "craft-recovery-transformation-1950s.md", E + "party-third-plenum.md", T + "xiandai-gongyi.md"],
    "断言语义取 L5385。成就总评为评价性判断，未列统计数字或机构名单；“十年浩劫”为原文历史表述；同段将成就归因于遗产基础、社会主义制度、党的关怀与工作者劳动，属多层归因。",
    5385, 5385, [5385], "第十三章 第十节 结语"))

rows.append(C(
    "claim-1045", "cand-14-22", "interpretive_claim",
    "工艺美术源于生活；时代前进、生活发展，对工艺美术提出越来越高的要求；工艺美术既要具有民族风格，又要具有时代特色；科学进步与新材料新技术为其创作开拓新领域，充分运用现代科学成果增加花色品种、丰富艺术表现力、创造简洁大方明快健康的新的工艺美，是新时代赋予的历史使命。",
    "Craft originates in life; as times advance and life develops, ever higher demands are placed on it; it must have both national style and contemporary character; scientific progress and new materials and techniques open new fields, and fully using modern scientific results to increase variety, enrich expression and create a concise, generous, bright and healthy new craft beauty is the historic mission of the new era.",
    [T + "gongyi-meishu.md", T + "chuantong-sheji.md", T + "xiandai-gongyi.md"],
    "断言语义取 L5387。属规范性理论概括，未引理论来源或例证；“民族风格”与“时代特色”并提，未说明二者冲突时的取舍。",
    5387, 5387, [5387], "第十三章 第十节 结语"))

rows.append(C(
    "claim-1046", "cand-14-09", "interpretive_claim",
    "工艺美术具有物质生产和精神生产的双重属性，既满足物质生活需要，也满足精神生活需要；党据此提出“日用品美术化，工艺品实用化”的发展方向，工艺美术工作者按照“适用、经济、美观”的设计原则和“古为今用”“推陈出新”的方针进行创作。",
    "Arts and crafts have the dual character of material and spiritual production, meeting both material and spiritual needs; on this basis the Party proposed the direction of making daily goods artistic and craft goods practical, and craft workers create according to the design principles suitable, economical, beautiful and the policies make the past serve the present and weed through the old to bring forth the new.",
    [T + "gongyi-meishu.md", T + "riyongpin-meishuhua-gongyipin-shiyonghua.md", T + "yishu-sheji.md"],
    "断言语义取 L5389。双重属性为作者理论概括，随后与党的方向、设计原则并置；claim 保留原文政策话语，不把“双重属性”当作已论证命题。",
    5389, 5389, [5389], "第十三章 第十节 结语"))

rows.append(C(
    "claim-1047", "cand-14-20", "historiographic_claim",
    "田自秉回忆，中央工艺美术学院筹备期间所见中国工艺美术史书籍多为日本、英国、德国和北欧出版物；中国自著仅发现1917年许衍灼《中国工艺沿革史略》一种，其他系统的书籍极少。",
    "Tian Zibing recalled that while the Central Academy of Arts and Crafts was being prepared, the Chinese craft-history books he saw were mostly Japanese, British, German and Nordic publications; of Chinese works he found only Xu Yanzhuo's 1917 Zhongguo Gongyi Yange Shilue, and other systematic books were very few.",
    [B + "zhongguo-gongyi-yange-shilue.md", B + "tian-zizhu-zhongguo-gongyi-meishu-shi.md"],
    "断言语义取 L5725。属个人见闻与回忆，未列调查范围与书目；1917年、许衍灼照录；“仅发现一本”为作者当时所见，不等于当时实际只出版一种。",
    5725, 5725, [5725], "后记"))

out = ROOT / "_tz_tz10a_rows.json"
out.write_text(json.dumps(rows, ensure_ascii=False, indent=1), encoding="utf-8")
print("rows", len(rows))
from collections import Counter
print(Counter(r["claim_type"] for r in rows))
links = [p for r in rows for p in r["supported_by"]]
print("links", len(links), "distinct", len(set(links)))
print("span kinds", Counter(r["source"]["source_span"]["span_kind"] for r in rows))
