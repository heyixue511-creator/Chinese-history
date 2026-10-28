# -*- coding: utf-8 -*-
"""Build 田自秉 2010 claim rows, batch tz4a (Han end + Six Dynasties + Tang start, 46 claims)."""
import json
from pathlib import Path

ROOT = Path(r"D:/中国设计史研究")
DOC = "2010-tianzibing-zhongguo-gongyi-meishushi"
SRC = "03基础书籍-md文档/中国工艺美术史（修订本）_田自秉_2010_东方出版中心.md"
DATE = "2026-10-27"
CH = "汉代末、六朝与隋唐（西汉末至唐代工艺美术）"

T = "04-knowledge/units/terms/"
P = "04-knowledge/units/places/"
R = "04-knowledge/units/persons/"
W = "04-knowledge/units/works/"
B = "04-knowledge/units/publications/"
PR = "04-knowledge/units/procedures/"
E = "04-knowledge/units/events/"
I = "04-knowledge/units/institutions/"

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
    "claim-0884", "cand-07-68", "factual_claim",
    "丝织物上的菱形纹与织造方法有关：织物以经纬线交织点形成斜线，采用斜纹组织，因而适于表现由各种斜线组成的菱形图案。",
    "Rhombic patterns on silk are tied to weaving technique: the weave forms diagonals at warp and weft intersections, so a twill structure suits rhombic motifs built from diagonals.",
    [T + "zhijin.md", T + "qi-silk.md", T + "ling-silk.md"],
    "断言语义取 L2499 汉代丝织几何纹段，原文由双菱纹的盛行解释斜纹组织的技术适配性，属技术—纹样关系判断，未给织造实验或实物组织分析。",
    2499, 2499, [2499], "第五章 第六节 染织工艺 一、丝织"))

rows.append(C(
    "claim-0885", "cand-07-69", "evaluative_claim",
    "用文字作为丝织的装饰图案，是汉锦一个突出的特点；文字多为成句的吉祥语。",
    "Using written characters as silk decoration is a marked feature of Han brocade; the characters usually form auspicious phrases.",
    [W + "wanshi-ruyi-jin.md", T + "zhijin.md"],
    "断言语义取 L2501，原文以新疆、内蒙古出土的延年益寿、万世如意、长乐明光等吉祥语锦为例，属作者对汉锦特征的概括评价。",
    2501, 2501, [2501], "第五章 第六节 染织工艺 一、丝织"))

rows.append(C(
    "claim-0886", "cand-07-70", "factual_claim",
    "马王堆出土的金银色印花纱采用三套版印制，是我国目前见到的最早的多套版印花工艺。",
    "The gold-and-silver printed gauze from Mawangdui was printed with three blocks and is the earliest multi-block printing process known in China so far.",
    [T + "jinyinse-yinhua-sha.md", T + "zhijin.md"],
    "断言语义取 L2517 印染段。原文详述三套版分印骨架、主纹与装饰点，并作最早性断言；“目前见到”已限定为当时材料下的判断。",
    2517, 2517, [2517], "第五章 第六节 染织工艺 二、印染"))

rows.append(C(
    "claim-0887", "cand-07-71", "factual_claim",
    "汉代漆器的生产组织严谨，分工很细；乐浪出土漆器铭文记录了素工、髹工、画工、铜扣黄涂工、清工、造工、漆工、供工等工种。",
    "Han lacquer production was tightly organised and finely divided; Luolang lacquer inscriptions record craftsmen such as body preparers, lacquerers, painters, gilt bronze-fitting workers, finishers, frame makers, lacquer makers and suppliers.",
    [PR + "han-dai-qiqi-zhizuo-fengong.md", I + "han-dai-qiqi-zuofang-guan-yuan.md"],
    "断言语义取 L2565，原文列十一工种铭文；其中“洪工”字义原文已承认难定，本 claim 只取分工细密的总判断，不裁定该字。",
    2565, 2565, [2565], "第五章 第七节 漆器工艺"))

rows.append(C(
    "claim-0888", "cand-07-72", "historiographic_claim",
    "从漆器铭文年代看，西汉昭帝始元二年（公元前85年）至东汉明帝永平十二年（公元69年）前后一百年间，是汉代漆器生产的发达时期。",
    "Judging from inscribed dates, the century from 85 BCE to 69 CE marks the flourishing period of Han lacquer production.",
    [PR + "han-dai-qiqi-zhizuo-fengong.md", I + "han-dai-qiqi-zuofang-guan-yuan.md"],
    "断言语义取 L2567，原文以有铭漆器的年代跨度划分发达期，属分期判断；铭文样本集中于乐浪等地，代表性未讨论。",
    2567, 2567, [2567], "第五章 第七节 漆器工艺"))

rows.append(C(
    "claim-0889", "cand-07-73", "evaluative_claim",
    "汉代的装饰花纹不如战国时期以描写为主，而是更加程式化、图案化，注重装饰效果。",
    "Han decorative motifs are less descriptive than Warring States ones and more stylised and patterned, with emphasis on decorative effect.",
    [T + "huaxiangshi.md", T + "zhijin.md", PR + "qiqi-mutai-san-zuofa.md"],
    "断言语义取 L2599 漆器装饰段末，原文以成都凤凰山漆盘龙凤仅用单纯线条、形象抽象化为据，属汉与战国装饰风格的比较评价。",
    2599, 2599, [2599], "第五章 第七节 漆器工艺"))

rows.append(C(
    "claim-0890", "cand-07-74", "historiographic_claim",
    "汉代漆器贴金片的作法应是唐代金银平脱的前身；乐浪玳瑁小盒的镶嵌也是后来螺钿技法的最早应用。",
    "Han lacquer with applied gold sheet is likely the forerunner of Tang gold-and-silver pingtuo, and the Luolang tortoiseshell-inlaid box is the earliest use of the later luodian technique.",
    [PR + "jinyin-pingtuo.md", E + "tang-ban-jinyin-pingtuo.md", T + "luodian.md"],
    "断言语义取 L2601，原文由贴金片与玳瑁镶嵌实物推溯后世技法源流，使用“应是”“最早”等判断语，未给传承链条证据。",
    2601, 2601, [2601], "第五章 第七节 漆器工艺"))

rows.append(C(
    "claim-0891", "cand-07-75", "interpretive_claim",
    "山东画像石的衰落在东汉末年即汉灵帝以后，这与当时社会矛盾日益尖锐、爆发黄巾大起义有关。",
    "The decline of Shandong pictorial stones after Emperor Ling of Han is connected with sharpening social conflict and the Yellow Turban uprising.",
    [T + "huaxiangshi.md", P + "nanyang-huaxiangshi-qu.md"],
    "断言语义取 L2625，原文把画像石衰落与社会动乱相联系，属因果解释；未给墓葬年代序列与事件年代的对应统计。",
    2625, 2625, [2625], "第五章 第八节 石雕和玉雕"))

rows.append(C(
    "claim-0892", "cand-07-76", "interpretive_claim",
    "泗洪曹庄“曾母投杼”画像石展示了织机的倾斜度，说明织机由最早的立机向平机过渡，以减少经线张力、提高产量；图中已用脚踏移综开口，可双手投梭和打纬。",
    "The Zeng mother pictorial stone shows an inclined loom, indicating a transition from upright to horizontal looms that reduced warp tension and raised output; treadles moved the heddles, leaving both hands free for shuttle and batten.",
    [W + "fangzhi-tu-huaxiangshi.md", T + "huaxiangshi.md"],
    "断言语义取 L2648，原文据画像石图像作织机技术推断；图像细节未作视觉复核，属以图证史的解读。",
    2648, 2648, [2648], "第五章 第八节 石雕和玉雕"))

rows.append(C(
    "claim-0893", "cand-07-77", "evaluative_claim",
    "汉代的装饰风格可以用质、动、紧、味四字概括：古拙朴质而不呆板，云气飞禽走兽富动感，构图满而不乱、密中求疏，纹样具有样式化的装饰韵味。",
    "Han decorative style can be summed up as substance, movement, density and flavour: plain yet not stiff, lively with cloud scrolls and animals, full but not chaotic, and stylised with decorative resonance.",
    [T + "huaxiangshi.md", T + "yunqi-wen.md", T + "zhijin.md"],
    "断言语义取 L2709，原文以质、动、紧、味四字分释汉代装饰风格，属作者的评价性概括，未给形式测量。",
    2709, 2709, [2709], "第五章 第十节 结语"))

rows.append(C(
    "claim-0894", "cand-07-78", "historiographic_claim",
    "汉代石刻的减地法对后世各种雕刻、陶瓷化妆土或釉彩的剔花、金银器的錾花都有深远影响。",
    "The Han relief-carving method of cutting away the ground had a lasting influence on later sculpture, on sgraffito decoration in ceramics, and on chased metalwork.",
    [T + "huaxiangshi.md", T + "huaxiangzhuan.md"],
    "断言语义取 L2711 结语表现手法第四条，原文作长时段影响判断，未举具体传承实例。",
    2711, 2711, [2711], "第五章 第十节 结语"))

rows.append(C(
    "claim-0895", "cand-07-79", "historiographic_claim",
    "六朝时期北方战争频繁，大量人口和工艺技术力量不断南移，改变了长期以北方为工艺美术生产中心的局面，生产重点开始由北方转向南方。",
    "Frequent warfare in the north during the Six Dynasties pushed population and craft skills south, ending the long primacy of northern craft production and shifting its centre southward.",
    [T + "liuchao-gongjiang-zhidu.md", E + "liuchao-buddhist-caves.md"],
    "断言语义取 L2723，原文据人口与技术南移作工艺生产中心转移判断，未给产量或作坊数量的区域统计。",
    2723, 2723, [2723], "第六章 第一节 概说"))

rows.append(C(
    "claim-0896", "cand-07-80", "interpretive_claim",
    "陶和瓷是一种工艺的两个不同发展阶段；瓷是陶的生产的高级阶段，由陶发展演变而来，但瓷出现后陶仍保留，形成两支各自发展。",
    "Pottery and porcelain are two stages of one craft; porcelain is the higher stage evolved from pottery, yet pottery continued alongside it as a separate branch.",
    [T + "taoqi.md", T + "proto-porcelain.md", T + "baici.md"],
    "断言语义取 L2739，原文针对陶瓷同源与异源之争提出阶段论，属理论判断；同段列举原料、火度、物理特性三项区别。",
    2739, 2739, [2739], "第六章 第二节 陶瓷工艺"))

rows.append(C(
    "claim-0897", "cand-07-81", "contested_claim",
    "有人认为莲花在六朝时期因佛教发展而从印度传来，这说法并不确切；中国在楚辞、吴俗、新郑立鹤方壶、蔡侯墓铜器与汉代画像石中已有悠久的莲花装饰传统。",
    "The view that the lotus motif entered China with Buddhism in the Six Dynasties is inaccurate: lotus decoration already had a long Chinese history in the Chu ci, Wu customs, the Xinzheng crane-and-lotus hu, Cai侯 tomb bronzes and Han pictorial stones.",
    [T + "lianhua-wen.md", T + "huaxiangshi.md"],
    "断言语义取 L2851，原文明确反驳莲花印度传入说并举本土实例；属学术争论中的一方，本 claim 按 contested 记录，不判定最终结论。",
    2851, 2851, [2851], "第六章 第二节 陶瓷工艺 一、青瓷"))

rows.append(C(
    "claim-0898", "cand-07-82", "contested_claim",
    "忍冬纹出自近东之说并不可靠；汉代铜镜边饰所称的卷云纹，就是这种卷草纹的前身。",
    "The claim that the honeysuckle scroll came from the Near East is unreliable; the cloud-scroll border on Han mirrors is its Chinese forerunner.",
    [T + "rendong-wen.md", T + "tongjing.md", T + "liuchao-tongjing.md"],
    "断言语义取 L2853，原文反驳忍冬纹近东起源说，以汉代铜镜卷云纹为本土前身；属争论性判断，本 claim 按 contested 记录。",
    2853, 2853, [2853], "第六章 第二节 陶瓷工艺 一、青瓷"))

rows.append(C(
    "claim-0899", "cand-07-83", "historiographic_claim",
    "在装饰图案发展史上，从商周到六朝以动物纹为中心的装饰题材已近尾声，即将过渡到隋唐以后以植物纹为中心的历史阶段。",
    "In the history of ornament, the animal-centred repertory from Shang-Zhou to the Six Dynasties was nearing its end and was about to give way to the plant-centred phase of Sui-Tang and later.",
    [T + "lianhua-wen.md", T + "rendong-wen.md"],
    "断言语义取 L2858，原文以莲花、忍冬为最早植物纹，提出动物纹向植物纹过渡的分期判断；同段以生产力与审美解放作解释。",
    2858, 2858, [2858], "第六章 第二节 陶瓷工艺 一、青瓷"))

rows.append(C(
    "claim-0900", "cand-08-72", "interpretive_claim",
    "装饰题材的发展已由以动物纹为中心向以植物花草为中心过渡；竹林七贤砖画中的翠竹、青松、银杏、垂柳成为人物的主要陪衬即是例证。",
    "Decorative subjects were shifting from animals to plants and flowers, as shown by bamboo, pine, ginkgo and willow serving as the main foils to figures in the Seven Sages brick painting.",
    [W + "zhulin-qixian-huaxiang-zhuan.md", T + "lianhua-wen.md", T + "rendong-wen.md"],
    "断言语义取 L2896，原文以竹林七贤砖画植物陪衬为据作出装饰史判断，与 claim-0899 的总论相邻，分属图像例证与分期总论，未合并。",
    2896, 2896, [2896], "第六章 第二节 陶瓷工艺 三、画象砖"))

rows.append(C(
    "claim-0901", "cand-08-73", "historiographic_claim",
    "据晋初傅玄《马钧传》记载，旧绫机五十综者五十蹑、六十综者六十蹑，马钧皆改为十二蹑，织出奇文异变如自然成形。",
    "According to Fu Xuan's biography of Ma Jun, the old damask looms needed fifty or sixty treadles for fifty or sixty heddles; Ma Jun reduced both to twelve and produced intricate patterns as if naturally formed.",
    [R + "ma-jun.md", T + "ling-silk.md"],
    "断言语义取 L2902，原文转述晋初傅玄《马钧传》的记载，属古代技术史料；候选原标 source_claim，本批按史料转述归为 historiographic_claim。",
    2902, 2902, [2902], "第六章 第三节 染织工艺"))

rows.append(C(
    "claim-0902", "cand-08-74", "historiographic_claim",
    "六朝丝织纹样改变汉代云气纹高低起伏的不规则格式，构成有规则的波状骨架，更加样式化并形成几何分割线。",
    "Six Dynasties silk patterns replaced the irregular swelling cloud-scroll format of Han with a regular wave framework, more stylised and divided into geometric bands.",
    [T + "zhijin.md", T + "yunqi-wen.md"],
    "断言语义取 L2922，原文将此列为六朝丝织纹样主要的艺术特点，属纹样史分期判断；未给织物组织分析。",
    2922, 2922, [2922], "第六章 第三节 染织工艺"))

rows.append(C(
    "claim-0903", "cand-08-75", "interpretive_claim",
    "六朝金属工艺处于衰落时期，日用铜器出土较少；青瓷取代铜器制作生活用品与佛教大量用铜铸佛，可能是其原因。",
    "Six Dynasties metalwork was in decline and daily bronze vessels are scarce; the rise of celadon as a substitute and the heavy use of bronze for Buddhist images may explain this.",
    [T + "liuchao-tongjing.md", T + "tongjing.md", E + "liuchao-buddhist-caves.md"],
    "断言语义取 L2935-L2937，原文以“可能由于以下原因”提出两条解释，属作者推断；同段引《洛阳伽蓝记》《魏书》说明铸佛规模。",
    2935, 2937, [2935, 2936, 2937], "第六章 第四节 金属工艺"))

rows.append(C(
    "claim-0904", "cand-08-76", "factual_claim",
    "夹纻佛像比铜佛轻便得多，又比泥佛坚固得多，一时极为流行，称为“行像”；晋代雕塑家戴逵以制作夹纻行像著名。",
    "Dry-lacquer Buddhist images were far lighter than bronze and sturdier than clay, so they became popular as processional images; the Jin sculptor Dai Kui was famous for making them.",
    [PR + "jiazhu-tai.md", W + "waguan-si-jiazhu-foxiang.md", R + "dai-kui.md"],
    "断言语义取 L2963，原文对夹纻行像的材料性能与流行作直接判断，并以戴逵为瓦棺寺造夹纻佛像五躯为证。",
    2963, 2963, [2963], "第六章 第五节 漆器工艺 一、夹纻"))

rows.append(C(
    "claim-0905", "cand-08-77", "historiographic_claim",
    "绿沉漆是色漆的新发展；这种暗绿色漆的出现，标志着髹漆工艺在调色技术上的新成就。",
    "Dark-green lacquer was a new development in coloured lacquer, marking a fresh achievement in lacquer colour formulation.",
    [T + "lvchen-qi.md"],
    "断言语义取 L2978，原文对绿沉漆在漆工艺史上的定位，属作者评价；同段引梁简文帝《书案铭》与刘桢奏折为文献依据。",
    2978, 2978, [2978], "第六章 第五节 漆器工艺 三、绿沉漆"))

rows.append(C(
    "claim-0906", "cand-08-78", "historiographic_claim",
    "在这以前，汉代的石刻多为平面的“影绘式”；到六朝，除浮雕外，多用立体的圆雕。",
    "Before this, Han stone carving was mostly flat silhouette work; in the Six Dynasties, in addition to relief, three-dimensional sculpture in the round became common.",
    [T + "huaxiangshi.md", P + "yungang-shiku.md"],
    "断言语义取 L2984，原文对六朝石雕相对汉代石刻形态变化的概括，属雕刻史分期判断。",
    2984, 2984, [2984], "第六章 第六节 其他工艺"))

rows.append(C(
    "claim-0907", "cand-08-79", "historiographic_claim",
    "不能认为我国古代的玻璃器都来自西方；我国在战国时期就已制作各种玻璃器皿，但一直没有得到较大的发展。",
    "Ancient Chinese glass vessels cannot all be regarded as imports from the West; China was already making various glass vessels in the Warring States period, though the craft never grew substantially.",
    [T + "glass.md", T + "liuli.md"],
    "断言语义取 L2999，原文以景县、定县、北票、南京等地出土玻璃器与《魏书》《抱朴子》记载反驳全来自西方说；属史学判断。",
    2999, 2999, [2999], "第六章 第六节 其他工艺"))

rows.append(C(
    "claim-0908", "cand-08-80", "historiographic_claim",
    "六朝时期在我国工艺美术发展史上上承两汉、下启隋唐，是一个重要的过渡时期；从风格说，它具有清秀、空疏的艺术特点。",
    "The Six Dynasties period, linking Han and Sui-Tang, was an important transitional phase in Chinese craft history, marked by a refined and airy style.",
    [T + "liuchao-gongjiang-zhidu.md", T + "lianhua-wen.md"],
    "断言语义取 L3010，原文第六章结语的总判断，并以玄学与佛教思想解释风格成因。",
    3010, 3010, [3010], "第六章 第七节 结语"))

rows.append(C(
    "claim-0909", "cand-08-81", "historiographic_claim",
    "工艺美术制作的宗教化，和受外来形式与风格的影响，正是六朝时期的重要时代特色。",
    "The religious turn in craft production and the influence of foreign forms and styles are key characteristics of the Six Dynasties.",
    [E + "liuchao-buddhist-caves.md", P + "yungang-shiku.md", T + "lianhua-wen.md"],
    "断言语义取 L3012，原文以佛教题材遍布铜器、石雕、织绣、夹纻造像及莲花、忍冬纹为依据。",
    3012, 3012, [3012], "第六章 第七节 结语"))

rows.append(C(
    "claim-0910", "cand-08-82", "historiographic_claim",
    "唐代工艺美术的发展和演变大体可分为前期和后期两个阶段，以安史之乱为分界点：前期指初唐、盛唐，后期指中唐、晚唐。",
    "Tang craft development falls into two phases divided by the An Lushan rebellion: the early phase covers the初唐 and 盛唐, the late phase the 中唐 and 晚唐.",
    [T + "tang-dai-qingci-yao.md", T + "tang-sancai.md"],
    "断言语义取 L3034，原文明确以安史之乱分初唐盛唐与中唐晚唐，属分期判断。",
    3034, 3034, [3034], "第七章 第一节 概说"))

rows.append(C(
    "claim-0911", "cand-08-83", "evaluative_claim",
    "唐代是我国封建社会的鼎盛时期，其社会特点可以用“统一、上升、自信、开放”八个字来说明。",
    "The Tang was the peak of Chinese feudal society, characterised by unity, ascent, self-confidence and openness.",
    [T + "sichou-zhilu.md", T + "tang-dai-qingci-yao.md"],
    "断言语义取 L3040，原文以疆域政令统一、民族交流、鲁迅《看镜有感》论汉唐魄力、宗教兼容等分释八字，属评价性概括。",
    3040, 3040, [3040], "第七章 第一节 概说"))

rows.append(C(
    "claim-0912", "cand-08-84", "evaluative_claim",
    "隋代白瓷烧制成功是一项突出的成就，在我国陶瓷史上开创了新纪元，为以后陶瓷发展创造了条件。",
    "The successful firing of white porcelain in the Sui was an outstanding achievement that opened a new era in Chinese ceramic history.",
    [T + "baici.md", W + "baici-pankou-changjing-ping.md"],
    "断言语义取 L3052，原文对隋代白瓷历史地位的评价；同段说明白瓷由青瓷演变、以精炼瓷土降低铁分而成，并称创始确切年代待考。",
    3052, 3052, [3052], "第七章 第二节 陶瓷工艺 一、隋代的陶瓷"))

rows.append(C(
    "claim-0913", "cand-08-85", "historiographic_claim",
    "唐代越窑为提供宫廷用品曾设官督造，这也就是后来历代御器厂或官窑的前身；此类产品称为秘色。",
    "The Tang Yue kilns were placed under official supervision to supply the court, a forerunner of later imperial factories and official kilns; their products were called mise.",
    [T + "tang-dai-qingci-yao.md", T + "baici.md"],
    "断言语义取 L3101，原文把唐代越窑官督造与后世御器厂、官窑建立源流关系，属制度史判断。",
    3101, 3101, [3101], "第七章 第二节 陶瓷工艺 二、唐代的陶瓷"))

rows.append(C(
    "claim-0914", "cand-08-86", "historiographic_claim",
    "据历史学家研究，唐代由于铜料缺乏，以及流行饮茶的社会风尚，间接促进了瓷业的发展。",
    "Historians hold that a shortage of copper and the fashion for tea drinking indirectly promoted the growth of the Tang ceramic industry.",
    [T + "tang-dai-qingci-yao.md", B + "chajing.md"],
    "断言语义取 L3105，原文以“据历史学家研究”引出该因果解释，属转述的学术判断；候选原标 source_claim，本批归为 historiographic_claim。",
    3105, 3105, [3105], "第七章 第二节 陶瓷工艺 二、唐代的陶瓷"))

rows.append(C(
    "claim-0915", "cand-08-87", "historiographic_claim",
    "学者们认为邢窑窑址既不在邢台，也不在内丘，而是在与内丘交界的临城；1980年临城邢瓷研制小组在岗头村、西双井、祁村发现唐代窑址。",
    "Scholars place the Xing kiln site neither at Xingtai nor Neiqiu but at Lincheng on the Neiqiu border, where a 1980 survey found Tang kiln sites at Gangtou, Xishuangjing and Qicun.",
    [T + "baici.md", T + "tang-dai-qingci-yao.md"],
    "断言语义取 L3122，原文转述1980年临城邢瓷研制小组普查后的学者意见；候选原标 source_claim，本批归为 historiographic_claim。",
    3122, 3122, [3122], "第七章 第二节 陶瓷工艺 二、唐代的陶瓷"))

rows.append(C(
    "claim-0916", "cand-08-88", "historiographic_claim",
    "釉下彩在陶瓷装饰史上，特别是在走向彩绘的发展过程中，具有重要的意义。",
    "Underglaze colour holds an important place in ceramic decoration, especially in the move towards painted decoration.",
    [T + "tang-dai-qingci-yao.md", T + "tang-sancai.md"],
    "断言语义取 L3132，原文对釉下彩工艺史地位的判断，并以铜官瓦渣坪与邛崃窑的釉下两色绘为例。",
    3132, 3132, [3132], "第七章 第二节 陶瓷工艺 二、唐代的陶瓷"))

rows.append(C(
    "claim-0917", "cand-08-89", "interpretive_claim",
    "唐三彩是模仿染缬工艺的装饰效果，形成斑驳淋漓的独特艺术风格；其涂蜡形成白斑的工艺与染缬的防染效果相通。",
    "Tang sancai imitated the decorative effects of resist dyeing, producing its mottled style; the wax-resist method that leaves white patches parallels resist-dye techniques.",
    [T + "tang-sancai.md", T + "jiaoxie.md", W + "sancai-nv-yong.md"],
    "断言语义取 L3154，原文据涂蜡形成白斑的工艺推断其模仿染缬效果，属作者解释；未给工艺实验或工匠记载。",
    3154, 3154, [3154], "第七章 第二节 陶瓷工艺 二、唐代的陶瓷"))

rows.append(C(
    "claim-0918", "cand-08-90", "interpretive_claim",
    "唐代陶瓷器皿颈部加长、安上把手、短嘴逐渐加长，是为了便于提取和倒出液体，反映生活方式的变化和日渐实用化；这与六朝席地而坐、唐以后有桌的起居变化相关。",
    "Lengthened necks, added handles and longer spouts on Tang ceramics served lifting and pouring, reflecting changed living habits and growing practicality, linked to the shift from floor-sitting to tables.",
    [T + "tang-dai-qingci-yao.md", T + "gaoxing-jiaju.md", T + "qimu-jiaju.md"],
    "断言语义取 L3170，原文以六朝席地而坐、唐以后有桌的起居变化解释器形演变，属功能—生活方式推断。",
    3170, 3170, [3170], "第七章 第二节 陶瓷工艺 二、唐代的陶瓷"))

rows.append(C(
    "claim-0919", "cand-08-91", "historiographic_claim",
    "这时期丝织生产的中心在中唐以后已经由北方的定州开始向江南转移；《国史补》所记薛兼训募北地织妇与元稹《织妇词》可作旁证。",
    "After the mid-Tang the centre of silk production began shifting from Dingzhou in the north to the Jiangnan region, as suggested by Xue Jianxun's recruitment of northern weavers and Yuan Zhen's poem.",
    [T + "zhijin.md", T + "qi-silk.md"],
    "断言语义取 L3199，原文以《国史补》薛兼训募织妇及元稹《织妇词》为据，属生产中心转移判断，并自注“未必是唯一的原因”。",
    3199, 3199, [3199], "第七章 第三节 染织工艺 一、丝织"))

rows.append(C(
    "claim-0920", "cand-08-92", "contested_claim",
    "联珠纹从当时波斯传入之说并不可靠；联珠纹在我国一直运用，而且具有极为悠久的历史，从甘肃半山型彩陶到隋代织锦均有实例。",
    "The claim that the pearl-roundel motif came from Persia is unreliable; it has a very long Chinese history, from Banshan painted pottery to Sui brocade.",
    [T + "lianzhu-wen.md", W + "lianzhu-luwen-jin.md", W + "lianzhu-yezhutou-wen-jin.md"],
    "断言语义取 L3203，原文明确反驳波斯传入说，并列举中国彩陶至隋唐的联珠纹实例；属争论性判断，本 claim 按 contested 记录。",
    3203, 3203, [3203], "第七章 第三节 染织工艺 一、丝织"))

rows.append(C(
    "claim-0921", "cand-08-93", "historiographic_claim",
    "汉锦古拙、朴质，唐锦则形成清新、活泼、华美、流畅的艺术风格；这一差异与汉锦经线起花、唐锦纬线起花的织法不同有关。",
    "Han brocade is archaic and plain, Tang brocade fresh, lively, sumptuous and fluent; the difference is tied to warp-faced Han and weft-faced Tang weaving.",
    [T + "jingjin.md", T + "zhijin.md", W + "huwang-jin.md"],
    "断言语义取 L3222，原文由经锦与纬锦织法差异引出两个时代织锦风格的对比，属工艺—风格关系判断。",
    3222, 3222, [3222], "第七章 第三节 染织工艺 一、丝织"))

rows.append(C(
    "claim-0922", "cand-08-94", "interpretive_claim",
    "阿斯塔那古墓出土的几何纹图案丝棉交织布应当是我国最早的混纺布。",
    "The silk-cotton interwoven cloth with geometric patterns from Astana is probably China's earliest blended fabric.",
    [T + "zhijin.md", T + "qi-silk.md"],
    "断言语义取 L3238，原文以“应当”表述，是作者带保留的推断，非引自他书的原话；未给纤维检测报告。",
    3238, 3238, [3238], "第七章 第三节 染织工艺 二、麻、棉织"))

rows.append(C(
    "claim-0923", "cand-08-95", "factual_claim",
    "宣州红线毯的原料是丝而不是毛，也就是现代所称的丝毯。",
    "The raw material of Xuanzhou red-thread carpet was silk, not wool; it is what is now called a silk carpet.",
    [T + "hongxian-tan.md", T + "qi-silk.md"],
    "断言语义取 L3242，原文对红线毯材质的直接判断，并以白居易《红线毯》诗所述择茧缫丝为据。",
    3242, 3242, [3242], "第七章 第三节 染织工艺 三、毛织和丝毯"))

rows.append(C(
    "claim-0924", "cand-08-96", "factual_claim",
    "唐代金银器的用途主要是向皇室作贡品；《旧唐书·文宗本纪》规定诸道进奉金花银器，王播一次进奉大小银碗三千四百枚。",
    "Tang gold and silver vessels were mainly tribute to the imperial court; the Old Tang History records Wang Bo presenting 3,400 silver bowls at one time.",
    [I + "jinyin-zuofangyuan.md", PR + "jinyin-pingtuo.md"],
    "断言语义取 L3298，原文引《旧唐书·文宗本纪》进奉金花银器及王播进奉银碗等例证；候选原标 source_claim，本批按事实断言归为 factual_claim。",
    3298, 3298, [3298], "第七章 第四节 金属工艺 一、金银器"))

rows.append(C(
    "claim-0925", "cand-08-97", "factual_claim",
    "银薰炉因重心在球体底部，利用同心圆机环和活轴的平衡作用，可使焚香杯随之转动而不翻倒。",
    "Because its centre of gravity lies at the bottom of the sphere, the silver censer uses concentric rings and pivots to keep the incense cup level as it turns.",
    [W + "yin-xunlu.md", T + "tongjing.md"],
    "断言语义取 L3304，原文对银薰炉结构原理的直接描述；同段记球体镂空、子母口、卡轴与银丝提链。",
    3304, 3304, [3304], "第七章 第四节 金属工艺 一、金银器"))

rows.append(C(
    "claim-0926", "cand-08-98", "evaluative_claim",
    "隋唐时期的金属工艺以金银器和铜镜两大类最为发达，具有较高的艺术成就。",
    "Sui-Tang metalwork was most developed in gold-and-silver vessels and bronze mirrors, both of high artistic achievement.",
    [T + "tongjing.md", I + "jinyin-zuofangyuan.md"],
    "断言语义取 L3278，原文金属工艺节的总体评价；同段说明瓷器兴起后铜制日用品减少。",
    3278, 3278, [3278], "第七章 第四节 金属工艺"))

rows.append(C(
    "claim-0927", "cand-08-99", "historiographic_claim",
    "唐三彩的发展大体经历初创、兴盛和衰落三个时期：初唐制作较简单，盛唐极盛，安史之乱后进入后期并逐渐衰落。",
    "Tang sancai passed through three phases: simple beginnings in the early Tang, a peak in the high Tang, and decline after the An Lushan rebellion.",
    [T + "tang-sancai.md", W + "sancai-nv-yong.md", T + "tang-dai-qingci-yao.md"],
    "断言语义取 L3150，原文以初唐、盛唐、安史之乱后划分唐三彩三期，属分期判断。",
    3150, 3150, [3150], "第七章 第二节 陶瓷工艺 二、唐代的陶瓷"))

rows.append(C(
    "claim-0928", "cand-08-102", "historiographic_claim",
    "唐代工艺美术非常发达，织锦、印染、陶瓷、金银器、漆器、木工等都达到全面繁荣，在艺术、技术和生产规模上远远超过前代；唐代装饰艺术达到高度成熟的黄金时代。",
    "Tang craft was highly developed across brocade, printing and dyeing, ceramics, metalwork, lacquer and carpentry, surpassing earlier periods in art, technique and scale; Tang ornament reached a mature golden age.",
    [T + "tang-sancai.md", T + "tang-dai-qingci-yao.md", T + "zhijin.md"],
    "断言语义取 L3032，原文对唐代工艺美术总体发展水平与装饰艺术阶段的概括性判断。",
    3032, 3032, [3032], "第七章 第一节 概说"))

rows.append(C(
    "claim-0929", "cand-08-103", "interpretive_claim",
    "由于对外交流的发展，唐代工艺美术既继承本国优秀艺术传统，又吸收外国工艺特色加以消化融合，形成唐代新的工艺美术风格。",
    "Expanded foreign exchange led Tang craft to inherit native traditions while absorbing and assimilating foreign techniques, producing a new Tang style.",
    [T + "sichou-zhilu.md", T + "tang-sancai.md", T + "jiaoxie.md"],
    "断言语义取 L3042，原文把唐代新工艺风格的形成解释为本国传统与外来工艺吸收融合的结果，并以杜环《经行记》所记工匠为证。",
    3042, 3042, [3042], "第七章 第一节 概说"))

out = ROOT / "_tz_tz4a_rows.json"
out.write_text(json.dumps(rows, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")

import collections
types = collections.Counter(r["claim_type"] for r in rows)
links = sum(len(r["supported_by"]) for r in rows)
distinct = len({p for r in rows for p in r["supported_by"]})
kinds = collections.Counter(r["source"]["source_span"]["span_kind"] for r in rows)
print("rows", len(rows), "types", dict(types), "links", links, "distinct", distinct, "kinds", dict(kinds))
