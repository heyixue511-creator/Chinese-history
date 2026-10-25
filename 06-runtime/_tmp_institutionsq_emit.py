import hashlib
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
PKG = ROOT / "06-runtime" / "automation" / "2026-10-25-2009zhaonong-institutions-batch-q"
PKG.mkdir(parents=True, exist_ok=True)
DOC = "2009-zhaonong-zhongguo-yishu-shejishi"
DATE = "2026-10-25"


def fp_bytes(raw: bytes) -> dict:
    text = raw.decode("utf-8").replace("\r\n", "\n").replace("\r", "\n")
    data = text.encode("utf-8")
    return {
        "sha256": "sha256:" + hashlib.sha256(data).hexdigest(),
        "bytes": len(data),
        "lines": text.count("\n"),
    }


def fp(path: pathlib.Path) -> dict:
    return fp_bytes(path.read_bytes())


def cid(n: str) -> str:
    return f"{DOC}:{n}"


creates = [
    (
        "cand-09-64",
        "司农司",
        "04-knowledge/units/institutions/sinongsi.md",
        "新建government_office：元朝官方设“司农司”，各地选派“劝农官”，鼓励开荒、禁止毁田，诏诸路劝课农桑；来源未给设立年份、品秩、隶属与员额",
    ),
    (
        "cand-10-105",
        "会通馆",
        "04-knowledge/units/institutions/huitongguan.md",
        "新建publishing_house：明代中期无锡华家“会通馆”，印《宋诸臣奏议》为现存最早铜活字印刷书籍；镌刻、排字、施墨、印刷形成秩序化操作",
    ),
    (
        "cand-10-148",
        "金陵书局",
        "04-knowledge/units/institutions/jinling-shuju.md",
        "新建publishing_house：清末同治年间曾国藩在南京开设，与其他地方官书局联刻《二十四史》，“流布雅俗，开启民思”",
    ),
    (
        "cand-10-149",
        "湖南思贤书局",
        "04-knowledge/units/institutions/hunan-sixian-shuju.md",
        "新建publishing_house：清末湖南官办书局，出版《王船山遗书》，整理出版王船山遗著并推动清末社会变革",
    ),
    (
        "cand-10-150",
        "浙江书局",
        "04-knowledge/units/institutions/zhejiang-shuju.md",
        "新建publishing_house：清末浙江官办书局，出版《二十二子》，来源将其列入对晚清社会产生积极影响的官书局例子",
    ),
    (
        "cand-10-151",
        "成都存古书局",
        "04-knowledge/units/institutions/chengdu-cungu-shuju.md",
        "新建publishing_house：清末成都官办书局，出版《说文解字注》，来源将其列入对晚清社会产生积极影响的官书局例子",
    ),
    (
        "cand-10-47",
        "六必居",
        "04-knowledge/units/institutions/liubiju.md",
        "新建commercial_enterprise：北京明代“六必居”酱菜店铺，流传至今；来源以之为招牌（商铺匾额）与书法、店铺信誉结合的例证",
    ),
    (
        "cand-10-48",
        "王麻子剪刀铺",
        "04-knowledge/units/institutions/wangmazi-jiandao-pu.md",
        "新建commercial_enterprise：北京王麻子剪刀铺，图9-15图题；来源称其长年累月获得良好商业信誉，作为招牌段例证",
    ),
]

updates = [
    (
        "cand-10-110",
        "武英殿",
        "04-knowledge/units/institutions/wuyingdian-xiushuchu.md",
        "更新既有武英殿修书处：补入赵农2009官刻序列（内府本—英武殿本—殿本）、殿本《十三经》《二十一史》、《大藏经》经版数与《武英殿聚珍版程式》；source_count 1→2、version 1→2",
    ),
]

rejected = [
    (
        "cand-10-135",
        "奴儿干都指挥使司",
        "来源仅一句背景：明朝曾在黑龙江设奴儿干都指挥使司，女真族为其中一部分并接受明朝赐封。该机构属东北边疆军事行政建置，来源未涉设计、工艺、生产组织或设计制度，不构成设计史 institution 条目，判 rejected。",
    ),
]

order = [
    "cand-09-64", "cand-10-105", "cand-10-110", "cand-10-135", "cand-10-148",
    "cand-10-149", "cand-10-150", "cand-10-151", "cand-10-47", "cand-10-48",
]
assert len(order) == 10

create_map = {c[0]: c for c in creates}
update_map = {u[0]: u for u in updates}
reject_map = {r[0]: r for r in rejected}

ledger = []
for n in order:
    if n in reject_map:
        _, title, reason = reject_map[n]
        ledger.append({
            "candidate_id": cid(n), "expected_state": "needs_evidence", "state": "rejected",
            "decision": {"status": "rejected", "reason": reason, "decided_by": "Agent", "decided_at": DATE},
            "updated_at": DATE,
        })
        continue
    if n in create_map:
        _, title, target, note = create_map[n]
        verb = "新建"
    else:
        _, title, target, note = update_map[n]
        verb = "更新"
    ledger.append({
        "candidate_id": cid(n), "expected_state": "needs_evidence", "state": "ready_for_review",
        "decision": {"status": "pending", "reason": f"已完成语义复读：{verb} {target}", "decided_by": "Agent", "decided_at": DATE},
        "updated_at": DATE,
    })
    ledger.append({
        "candidate_id": cid(n), "expected_state": "ready_for_review", "state": "approved",
        "decision": {"status": "approved", "reason": f"canonical 候选语义复读完成，批准{verb} {target}", "decided_by": "Agent", "decided_at": DATE},
        "updated_at": DATE,
    })
    ledger.append({
        "candidate_id": cid(n), "expected_state": "approved", "state": "applied",
        "decision": {"status": "approved", "reason": f"已判定 applied：{verb} {target}", "decided_by": "Agent", "decided_at": DATE},
        "updated_at": DATE, "target_ref": target,
    })

plan = []
for n, title, target, note in creates:
    p = ROOT / target
    f = fp(p)
    plan.append({
        "action": "create", "target_ref": target, "candidate_id": cid(n),
        "entity": title, "before": None, "after_sha256": f["sha256"], "bytes": f["bytes"],
        "lines": f["lines"], "note": note,
    })

# 更新行的 before 指纹由当前文件逆向我方编辑还原，正向重放校验一致后取指纹。
target = updates[0][2]
cur = (ROOT / target).read_text(encoding="utf-8")
pairs = [
    ("name_zh: 武英殿修书处\ninstitution_type: 清代内府出版机构",
     "name_zh: 武英殿修书处\naliases:\n  - 武英殿\ninstitution_type: 清代内府出版机构"),
    ("  - 出版\n  - 活字", "  - 出版\n  - 官刻\n  - 殿本\n  - 活字"),
    ("      doc_id: 2004-gaofeng-zhongguo-shejishi\n      source_file: 03基础书籍-md文档/中国设计史_高丰_2004_广西美术出版社.md\n      chapter_id: null\n      chunk_id: null\ncreated: 2026-10-25",
     "      doc_id: 2004-gaofeng-zhongguo-shejishi\n      source_file: 03基础书籍-md文档/中国设计史_高丰_2004_广西美术出版社.md\n      chapter_id: null\n      chunk_id: null\n  - citation: \"赵农, *中国艺术设计史* (北京: 高等教育出版社, 2009), L7210-L7258.\"\n    location: \"L7210-L7258\"\n    evidence_ref:\n      doc_id: 2009-zhaonong-zhongguo-yishu-shejishi\n      source_file: 03基础书籍-md文档/中国艺术设计史_赵农_2009_高等教育出版社.md\n      chapter_id: null\n      chunk_id: null\ncreated: 2026-10-25"),
    ("source_count: 2\nlast_verified: 2026-10-25\nreview_due: 2027-04-25\nversion: 2",
     "source_count: 1\nlast_verified: 2026-10-25\nreview_due: 2027-04-25\nversion: 1"),
    ("hierarchy_scope_note: \"武英殿修书处是 C 维度下清代内府出版与书籍设计的机构条目，其内府与官刻制度归 D、活字刻制与雕版工艺归 B；当前只到 Dimension。\"",
     "hierarchy_scope_note: \"武英殿修书处是 C 维度下清代内府出版与书籍设计的机构条目，其内府制度归 D、活字刻制工艺归 B；当前只到 Dimension。\""),
]
# 反向：仅替换 new→old 的部分；为清晰起见，这里显式列 old/new 对。
edit_pairs = [
    ("name_zh: 武英殿修书处\ninstitution_type: 清代内府出版机构",
     "name_zh: 武英殿修书处\naliases:\n  - 武英殿\ninstitution_type: 清代内府出版机构"),
    ("  - 出版\n  - 活字", "  - 出版\n  - 官刻\n  - 殿本\n  - 活字"),
    ("hierarchy_scope_note: \"武英殿修书处是 C 维度下清代内府出版与书籍设计的机构条目，其内府制度归 D、活字刻制工艺归 B；当前只到 Dimension。\"",
     "hierarchy_scope_note: \"武英殿修书处是 C 维度下清代内府出版与书籍设计的机构条目，其内府与官刻制度归 D、活字刻制与雕版工艺归 B；当前只到 Dimension。\""),
    ("source_count: 1\nlast_verified: 2026-10-25\nreview_due: 2027-04-25\nversion: 1",
     "source_count: 2\nlast_verified: 2026-10-25\nreview_due: 2027-04-25\nversion: 2"),
    ("      doc_id: 2004-gaofeng-zhongguo-shejishi\n      source_file: 03基础书籍-md文档/中国设计史_高丰_2004_广西美术出版社.md\n      chapter_id: null\n      chunk_id: null\ncreated: 2026-10-25",
     "      doc_id: 2004-gaofeng-zhongguo-shejishi\n      source_file: 03基础书籍-md文档/中国设计史_高丰_2004_广西美术出版社.md\n      chapter_id: null\n      chunk_id: null\n  - citation: \"赵农, *中国艺术设计史* (北京: 高等教育出版社, 2009), L7210-L7258.\"\n    location: \"L7210-L7258\"\n    evidence_ref:\n      doc_id: 2009-zhaonong-zhongguo-yishu-shejishi\n      source_file: 03基础书籍-md文档/中国艺术设计史_赵农_2009_高等教育出版社.md\n      chapter_id: null\n      chunk_id: null\ncreated: 2026-10-25"),
    ("来源在此处转引潘吉星《中国科学技术史·造纸与印刷卷》。\n\n来源只给机构名、隶属、三朝出版种数、金简主持刻制活字与丛书种卷数，没有给修书处的设立年份、内部机构、员额、刻工与印工数量、活字排印工序、纸张与装帧材料、书籍目录与流通范围。本条目只登记其作为清代内府出版机构的本体，不写成清代出版史或活字印刷通史。",
     "来源在此处转引潘吉星《中国科学技术史·造纸与印刷卷》。\n\n赵农《中国艺术设计史》（2009）在“清代印刷”官刻段另记：清代初期官刻中先有内务府管理的“内府本”书籍，再有武英殿管理的“英武殿本”（原文用字），最后合为“殿本”，由饱读诗书的翰林学士负责其事，因而殿本雕刻精良、编排得当，殿本的《十三经》《二十一史》为清代官方雕版印刷书籍的杰作。同段还记乾隆年间印制《大藏经》用两面版经版 79,000 余块，共 7,000 多卷，分装 724 函，收佛经 1,669 部，约 6,700 万字；同书活字段又记乾隆时期木活字以刻印《武英殿聚珍版丛书》而著名，编纂者金简撰《武英殿聚珍版程式》，对木活字制作技术作详细绘图说明。2009 册只称“武英殿”，未用“武英殿修书处”全称；其“内府本—英武殿本—殿本”的三段表述与高丰 2004 的“武英殿修书处”条可互补，但两册对隶属层级的说法不完全一致，正文并录，不据一说改写另一说。\n\n两册来源只给机构名、隶属、出版种数、官刻序列、代表刻本、金简主持刻制活字与丛书种卷数，没有给修书处的设立年份、内部机构、员额、刻工与印工数量、活字排印工序、纸张与装帧材料、书籍目录与流通范围。本条目只登记其作为清代内府出版机构的本体，不写成清代出版史或活字印刷通史。"),
    ("- **资料来源**: 来源此处转引潘吉星《中国科学技术史·造纸与印刷卷》（科学出版社 1998 年版，第 423、427 页）（高丰 2004）\n- **证据边界**: 来源未给修书处设立年份、内部机构、员额、刻工与印工数量、活字排印工序、纸张与装帧材料、书籍目录与流通范围",
     "- **资料来源**: 来源此处转引潘吉星《中国科学技术史·造纸与印刷卷》（科学出版社 1998 年版，第 423、427 页）（高丰 2004）\n- **官刻序列**: 内务府“内府本”→武英殿“英武殿本”（原文用字）→合为“殿本”（赵农 2009）\n- **校刻人员**: 由饱读诗书的翰林学士负责其事（赵农 2009）\n- **殿本代表作**: 《十三经》《二十一史》为清代官方雕版印刷书籍的杰作（赵农 2009）\n- **官刻佛经**: 乾隆年间印制《大藏经》，用两面版经版 79,000 余块，共 7,000 多卷，分装 724 函，收佛经 1,669 部，约 6,700 万字（赵农 2009；同段属官刻，来源未明言由武英殿主持）\n- **木活字程式**: 乾隆时期以刻印《武英殿聚珍版丛书》著名；金简撰《武英殿聚珍版程式》，对木活字制作技术作详细绘图说明（赵农 2009）\n- **口径说明**: 2009 册称“武英殿”，未用“武英殿修书处”全称；“英武殿本”为原文用字；与高丰 2004 的隶属表述并录\n- **证据边界**: 来源未给修书处设立年份、内部机构、员额、刻工与印工数量、活字排印工序、纸张与装帧材料、书籍目录与流通范围；未给武英殿与内务府的实际统属关系、殿本刻书目录与《大藏经》刊印分工"),
    ("- 匹配质量: 单一来源一段，机构名、隶属、三朝出版种数、金简主持、活字数与丛书种卷数明确；设立年份、内部机构、员额、工序与书目缺失\n- 验证日期: 2026-10-25\n- 证据范围: 仅前六册 Markdown 文本；未查武英殿刻书档案、清代内府出版研究或《武英殿珍版丛书》原目，未做来源外核对",
     "- 匹配质量: 两册来源均指向清代内府出版机构：高丰 2004 记机构名、隶属、三朝出版种数、金简主持、活字数与丛书种卷数；赵农 2009 记官刻序列、殿本代表作、《大藏经》经版数与《武英殿聚珍版程式》。2009 只称“武英殿”，与“武英殿修书处”全称不一致；“英武殿本”为原文用字；两册对隶属层级表述不完全一致。设立年份、内部机构、员额、工序与书目缺失\n- 验证日期: 2026-10-25\n- 证据范围: 仅前六册 Markdown 文本；未查武英殿刻书档案、清代内府出版研究、《武英殿珍版丛书》原目或《大藏经》刊印档案，未做来源外核对"),
    ("1. 高丰. *中国设计史*. 南宁: 广西美术出版社, 2004.",
     "1. 高丰. *中国设计史*. 南宁: 广西美术出版社, 2004.\n2. 赵农. *中国艺术设计史*. 北京: 高等教育出版社, 2009."),
]
old_text = cur
for old, new in edit_pairs:
    assert new in old_text, f"missing new block: {new[:40]}"
    old_text = old_text.replace(new, old, 1)
for old, new in edit_pairs:
    assert old in old_text, f"missing old block: {old[:40]}"
    old_text = old_text.replace(old, new, 1)
assert old_text == cur, "reconstruction mismatch"
old_text = cur
for old, new in edit_pairs:
    old_text = old_text.replace(new, old, 1)
assert "source_count: 1" in old_text and "version: 1" in old_text
assert old_text.count("- citation:") == 1

before = fp_bytes(old_text.encode("utf-8"))
after = fp(ROOT / target)
plan.append({
    "action": "update", "target_ref": target, "candidate_id": cid(updates[0][0]),
    "entity": updates[0][1], "before": before, "after_sha256": after["sha256"],
    "bytes": after["bytes"], "lines": after["lines"], "note": updates[0][3],
})

mapping = []
for n, title, target, note in creates:
    mapping.append({
        "entity": title, "target_ref": target, "action": "create",
        "canonical_candidate": cid(n), "merged_candidates": [],
    })
for n, title, target, note in updates:
    mapping.append({
        "entity": title, "target_ref": target, "action": "update",
        "canonical_candidate": cid(n), "merged_candidates": [], "note": note,
    })

with (PKG / "candidate-decision-ledger.jsonl").open("w", encoding="utf-8", newline="\n") as f:
    for row in ledger:
        f.write(json.dumps(row, ensure_ascii=False) + "\n")
with (PKG / "apply-plan.jsonl").open("w", encoding="utf-8", newline="\n") as f:
    for row in plan:
        f.write(json.dumps(row, ensure_ascii=False) + "\n")
(PKG / "canonical-mapping.json").write_text(json.dumps(mapping, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

manifest = {
    "work_package": PKG.name,
    "goal": "处理赵农《中国艺术设计史》2009 册 institution 候选 10 个：8 个新建、1 个更新、0 个 no_delta、1 个 rejected。",
    "status": "applied",
    "date": DATE,
    "inputs": {
        "candidate_index": {
            "path": "06-runtime\\state\\candidate-index.jsonl",
            "rows_before": 5339,
            "sha256_before": "sha256:bb92c619b1c3003bb661c6dd4ee7d8e54b3f5a93a7da18472afac1251a3d9f25",
            "sha256_scope": "CRLF→LF 归一后",
            "counts_before": {"applied": 857, "needs_evidence": 3619, "no_delta": 56, "rejected": 807},
        },
        "source": {
            "doc_id": DOC,
            "file": "03基础书籍-md文档/中国艺术设计史_赵农_2009_高等教育出版社.md",
            "spans": [
                "L6486-L6519", "L7125-L7209", "L7210-L7258", "L6613", "L7221-L7227",
                "L6836-L6866",
            ],
        },
    },
    "method": {
        "rules": [
            "institution 候选按实体对账：先与既有 institution KU 的标题、别名与正文对齐，再定 create／update／no_delta／rejected。",
            "候选“司农司”按元代劝农行政机构立目：官方设司农司、各地选派劝农官、鼓励开荒、禁止毁田、诏诸路劝课农桑；不补品秩、员额与《元史》原文以外的制度细节。",
            "候选“会通馆”按明代无锡华家铜活字印书工坊立目：印《宋诸臣奏议》为现存最早铜活字印刷书籍，镌刻、排字、施墨、印刷形成秩序化操作；不补主人姓名与活字数量。",
            "候选“武英殿”判 update：既有 wuyingdian-xiushuchu.md 即武英殿修书处，补入赵农 2009 官刻序列、殿本代表作、《大藏经》经版数与《武英殿聚珍版程式》；2009 册只称“武英殿”，正文并录两册隶属表述，不据一说改写另一说。",
            "候选“奴儿干都指挥使司”判 rejected：来源仅一句女真族背景，机构属东北边疆军事行政建置，未涉设计、工艺、生产组织或设计制度，不立设计史 institution 条目。",
            "候选“金陵书局”按清末南京官办书局立目：同治年间曾国藩开设，与其他地方官书局联刻《二十四史》，“流布雅俗，开启民思”。",
            "候选“湖南思贤书局”按清末湖南官办书局立目：出版《王船山遗书》，整理出版王船山遗著并推动清末社会变革。",
            "候选“浙江书局”按清末浙江官办书局立目：出版《二十二子》；影响句为四局并列，不单独归因于浙江书局。",
            "候选“成都存古书局”按清末成都官办书局立目：出版《说文解字注》；与《说文解字》本体条目分条，不合并。",
            "候选“六必居”按明清北京酱菜老字号立目：来源以之为招牌（商铺匾额）例证，记其明代、北京、酱菜与流传至今；不并入幌子条目对“六必居”三字的释义。",
            "候选“王麻子剪刀铺”按明清北京剪刀铺立目：图 9-15 图题与“长年累月获得良好商业信誉”正文；与幌子条目“王麻子刀剪铺”分条并存，不合并。",
            "03基础书籍-md文档只读；本批写 04-knowledge/units/institutions，8 条新建、1 条更新、1 条 rejected。",
        ],
    },
    "outputs": {
        "apply_plan": {"path": f"06-runtime\\automation\\{PKG.name}\\apply-plan.jsonl", "rows": len(plan), "create": len(creates), "update": len(updates)},
        "ledger": {"path": f"06-runtime\\automation\\{PKG.name}\\candidate-decision-ledger.jsonl", "rows": len(ledger), "candidates": len(order), "applied": len(creates) + len(updates), "no_delta": 0, "rejected": len(rejected)},
        "canonical_mapping": {"path": f"06-runtime\\automation\\{PKG.name}\\canonical-mapping.json", "entries": len(mapping), "merged_candidates": []},
    },
    "state_after": {},
}
(PKG / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

assert len(ledger) == 28, len(ledger)
assert len(plan) == 9, len(plan)
assert len(mapping) == 9, len(mapping)
print(json.dumps({
    "ledger": len(ledger), "plan": len(plan), "mapping": len(mapping),
    "creates": len(creates), "updates": len(updates), "rejected": len(rejected),
    "before": before, "after": after,
}, ensure_ascii=False))
