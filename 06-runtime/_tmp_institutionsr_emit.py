import hashlib
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
PKG = ROOT / "06-runtime" / "automation" / "2026-10-25-2009zhaonong-institutions-batch-r"
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
        "cand-10-56",
        "台湾邮政总局",
        "04-knowledge/units/institutions/taiwan-youzheng-zongju.md",
        "新建government_office：1888年台湾巡抚刘铭传创办，发行“台湾邮票”“邮政商票”两种官商形式邮票，两联发售、一联作存根，为最早商业邮政尝试；来源未给地址、隶属、邮路与停办时间",
    ),
    (
        "cand-10-93",
        "经厂",
        "04-knowledge/units/institutions/jingchang.md",
        "新建publishing_house：明代官方书籍由内府转司礼监管理后设“经厂”，挑刻工、印工、折配工、装订工，出200余种经厂本，纸张光洁、版式精美，但因太监校勘有限而文字错误较多",
    ),
    (
        "cand-10-98",
        "建阳书坊",
        "04-knowledge/units/institutions/jianyang-shufang.md",
        "新建publishing_house：明代建阳80余家书坊群（非单一书坊），出诗文、通俗、小说、医学书，插图本较多，并刻朱熹、吕祖谦等理学史学著作；杭州24家、徽州10余家仅作比较",
    ),
    (
        "cand-11-105",
        "包豪斯（Bauhaus）",
        "04-knowledge/units/institutions/bauhaus.md",
        "新建design_school：1919年德国包豪斯成立，来源以之为西方工艺美术与设计学科剥离完成的标志；原文拼写“Bauhuas”照录；未给创办人、课程、关闭时间与影响",
    ),
    (
        "cand-11-130",
        "中国营造学社",
        "04-knowledge/units/institutions/zhongguo-yingzao-xueshe.md",
        "新建research_institute：朱启钤1925年发起“营造学会”、1930年改名“中国营造学社”，梁思成、刘敦桢等整理《园冶》《梓人遗制》，在河北山西山东测绘，抗战期间在西南续研，1946年停止活动",
    ),
    (
        "cand-12-132",
        "金陵机器局",
        "04-knowledge/units/institutions/jinling-jiqiju.md",
        "新建government_office：1865年设立，与江南制造总局、福州船政局、天津机器局、湖北枪炮厂并列；来源整体批评“官商一体”阻碍资本主义与现代化，未给局址、创办人、产品与沿革",
    ),
    (
        "cand-12-134",
        "天津机器局",
        "04-knowledge/units/institutions/tianjin-jiqiju.md",
        "新建government_office：1867年设立，与江南制造总局、金陵机器局、福州船政局、湖北枪炮厂并列；来源整体批评“官商一体”阻碍资本主义与现代化，未给局址、创办人、产品与沿革",
    ),
    (
        "cand-12-135",
        "湖北枪炮厂",
        "04-knowledge/units/institutions/hubei-qiangpaochang.md",
        "新建government_office：1891年设立，与江南制造总局、金陵机器局、福州船政局、天津机器局并列；来源整体批评“官商一体”阻碍资本主义与现代化，未给厂址、创办人、产品与沿革",
    ),
]

updates = [
    (
        "cand-11-045",
        "养心殿造办处",
        "04-knowledge/units/institutions/neiwufu-zaobanchu.md",
        "更新既有内务府造办处：加别名“养心殿造办处”、补赵农2009“对皇室用具及服饰进行严格管理”与名称差异说明；source_count 2→3、version 1→2",
    ),
    (
        "cand-11-046",
        "江南织造",
        "04-knowledge/units/institutions/jiangning-zhizaoju.md",
        "更新既有江宁织造局：加别名“江南织造”、补赵农2009“在南京设立”“采买丝绸织物”与指称范围说明；source_count 3→4、version 1→2",
    ),
]

order = [
    "cand-10-56", "cand-10-93", "cand-10-98", "cand-11-045", "cand-11-046",
    "cand-11-105", "cand-11-130", "cand-12-132", "cand-12-134", "cand-12-135",
]
assert len(order) == 10

create_map = {c[0]: c for c in creates}
update_map = {u[0]: u for u in updates}

ledger = []
for n in order:
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

# 两个 update 的 before 指纹：对当前文件逆向执行本批编辑，再正向重放并断言回到当前文件。
NEIWUFU_PAIRS = [
    (
        "name_zh: 内务府造办处\ntranslation_status: provisional\ntranslation_note: 采用描述性译名 Imperial Household Department Workshops；来源未给英译。\ntags:\n  - 清代\n  - 宫廷作坊\n  - 家具\n  - 珐琅作\n  - 乾隆\nlocation: 北京",
        "name_zh: 内务府造办处\ntranslation_status: provisional\ntranslation_note: 采用描述性译名 Imperial Household Department Workshops；来源未给英译。\ntags:\n  - 清代\n  - 宫廷作坊\n  - 家具\n  - 珐琅作\n  - 乾隆\n  - 服饰管理\naliases:\n  - 养心殿造办处\nlocation: 北京",
    ),
    (
        "      doc_id: 2016-xiayanjing-zhongguo-yishu-shejishi-upgrade\n      source_file: 03基础书籍-md文档/中国艺术设计史（升级版）_夏燕靖_2016_上海人民美术出版社.md\n      chapter_id: null\n      chunk_id: null\ncreated: 2026-10-25\nupdated: 2026-10-25\nconfidence: medium\nconsensus: tentative\nsource_count: 2\nlast_verified: 2026-10-25\nreview_due: 2027-04-25\nversion: 1",
        "      doc_id: 2016-xiayanjing-zhongguo-yishu-shejishi-upgrade\n      source_file: 03基础书籍-md文档/中国艺术设计史（升级版）_夏燕靖_2016_上海人民美术出版社.md\n      chapter_id: null\n      chunk_id: null\n  - citation: \"赵农, *中国艺术设计史* (北京: 高等教育出版社, 2009), L7488.\"\n    location: \"L7488\"\n    evidence_ref:\n      doc_id: 2009-zhaonong-zhongguo-yishu-shejishi\n      source_file: 03基础书籍-md文档/中国艺术设计史_赵农_2009_高等教育出版社.md\n      chapter_id: null\n      chunk_id: null\ncreated: 2026-10-25\nupdated: 2026-10-25\nconfidence: medium\nconsensus: tentative\nsource_count: 3\nlast_verified: 2026-10-25\nreview_due: 2027-04-25\nversion: 2",
    ),
    (
        "2016 记其为清代宫廷制造皇家御用品的专门机构，康熙年间成立至 1924 年，先后设 60 多个专业作坊；珐琅彩在北京用进口珐琅彩料绘制；与明代内廷作坊同为宫廷家具制作机构。",
        "2016 记其为清代宫廷制造皇家御用品的专门机构，康熙年间成立至 1924 年，先后设 60 多个专业作坊；珐琅彩在北京用进口珐琅彩料绘制；与明代内廷作坊同为宫廷家具制作机构。赵农 2009 在“清代服饰”段称“清代官方设有养心殿造办处，对皇室用具及服饰进行严格管理”，以“养心殿造办处”之名记本机构，并把管理范围明确扩及服饰；该来源未给造办处沿革、作坊与人员。",
    ),
    (
        "- **与明代内廷作坊的关系**: 同为宫廷家具制作机构（2016）\n- **设计史意义**",
        "- **与明代内廷作坊的关系**: 同为宫廷家具制作机构（2016）\n- **服饰管理（赵农 2009，六册中仅见）**: “清代官方设有养心殿造办处，对皇室用具及服饰进行严格管理”（赵农 2009）\n- **名称差异**: 赵农 2009 作“养心殿造办处”，高丰、夏燕靖 2016 作“内务府造办处”；来源未说明二者是否为同一机构的不同称法，本条按同一机构并入，别名照录\n- **设计史意义**",
    ),
    (
        "与 江宁织造局同属清代宫廷相关造物机构，一为内廷作坊、一为地方织造。relation 未审查。",
        "与江宁织造局同属清代宫廷相关造物机构，一为内廷作坊、一为地方织造；赵农 2009 同一段并记二者，先造办处、后江南织造，可支持“内廷—地方”的宫廷造物管理序列。relation 未审查，不写入正式 `relations`。",
    ),
    (
        "- 匹配质量: 2016 条 location L4341-L6330 为超大跨度，珐琅彩与作坊数位置待核；两册对成立时间的详略不同（清代／康熙年间），已并列。\n- 验证日期: 2026-10-25\n- 证据范围: 仅前六册 Markdown 文本；未做来源外核对",
        "- 匹配质量: 2016 条 location L4341-L6330 为超大跨度，珐琅彩与作坊数位置待核；两册对成立时间的详略不同（清代／康熙年间），已并列。赵农 2009 仅一句，称“养心殿造办处”并记服饰管理，未给沿革、作坊与人员；与“内务府造办处”是否同一机构，来源未明言，属编者按同一机构并入。\n- 验证日期: 2026-10-25\n- 证据范围: 仅前六册 Markdown 文本；未查内务府档案、造办处活计档或清代服饰制度研究，未做来源外核对",
    ),
    (
        "1. 高丰. *中国设计史*. 广西美术出版社, 2004.\n2. 夏燕靖. *中国艺术设计史（升级版）*. 上海: 上海人民美术出版社, 2016.",
        "1. 高丰. *中国设计史*. 广西美术出版社, 2004.\n2. 夏燕靖. *中国艺术设计史（升级版）*. 上海: 上海人民美术出版社, 2016.\n3. 赵农. *中国艺术设计史*. 北京: 高等教育出版社, 2009.",
    ),
]

JIANGNING_PAIRS = [
    (
        "aliases:\n  - 江宁织造\n  - 江宁织造署",
        "aliases:\n  - 江宁织造\n  - 江宁织造署\n  - 江南织造",
    ),
    (
        "      doc_id: 2016-xiayanjing-zhongguo-yishu-shejishi-upgrade\n      source_file: 03基础书籍-md文档/中国艺术设计史（升级版）_夏燕靖_2016_上海人民美术出版社.md\n      chapter_id: null\n      chunk_id: null\ncreated: 2026-10-25\nupdated: 2026-10-25\nconfidence: medium\nconsensus: tentative\nsource_count: 3\nlast_verified: 2026-10-25\nreview_due: 2027-04-25\nversion: 1",
        "      doc_id: 2016-xiayanjing-zhongguo-yishu-shejishi-upgrade\n      source_file: 03基础书籍-md文档/中国艺术设计史（升级版）_夏燕靖_2016_上海人民美术出版社.md\n      chapter_id: null\n      chunk_id: null\n  - citation: \"赵农, *中国艺术设计史* (北京: 高等教育出版社, 2009), L7488.\"\n    location: \"L7488\"\n    evidence_ref:\n      doc_id: 2009-zhaonong-zhongguo-yishu-shejishi\n      source_file: 03基础书籍-md文档/中国艺术设计史_赵农_2009_高等教育出版社.md\n      chapter_id: null\n      chunk_id: null\ncreated: 2026-10-25\nupdated: 2026-10-25\nconfidence: medium\nconsensus: tentative\nsource_count: 4\nlast_verified: 2026-10-25\nreview_due: 2027-04-25\nversion: 2",
    ),
    (
        "三册对曹氏任职年数的记法不一致，夏燕靖 2016 一册内部也有两处年数并存。",
        "三册对曹氏任职年数的记法不一致，夏燕靖 2016 一册内部也有两处年数并存。赵农 2009 在“清代服饰”段以“江南织造”之名记本机构，称清政府“在南京设立了江南织造，采买丝绸织物，以供皇家生活之需”，把江宁织造的位置系于南京、职能系于采买，与前三册的“织造生产”侧重不同。",
    ),
    (
        "- **文献来源（田自秉）**: 引《首都丝织业调查记》“江宁织锦之艺，由来已久。究创始于何年，发明者何人，以年久淹没，均不可考……至明清两朝方盛行，当满清时代江南锦缎乃贡品中最珍贵者，故设有专司监察督制”；引《中国经济志》“云锦亦名锦缎，凡缎质而有花色者均属之……宋时宋锦即其鼻祖，限于专供御用”",
        "- **文献来源（田自秉）**: 引《首都丝织业调查记》“江宁织锦之艺，由来已久。究创始于何年，发明者何人，以年久淹没，均不可考……至明清两朝方盛行，当满清时代江南锦缎乃贡品中最珍贵者，故设有专司监察督制”；引《中国经济志》“云锦亦名锦缎，凡缎质而有花色者均属之……宋时宋锦即其鼻祖，限于专供御用”\n- **“江南织造”与采买职能（赵农 2009，六册中仅见）**: “清政府还在南京设立了江南织造，采买丝绸织物，以供皇家生活之需”（赵农 2009）——该来源以“江南织造”称本机构，并明确说“在南京设立”，职能表述为“采买”；与夏燕靖两版、田自秉的织造生产侧重不同\n- **名称与指称范围**: 赵农 2009 的“江南织造”在字面上可兼指江宁、苏州、杭州三织造，但该来源紧接“在南京设立了江南织造”，本条据此按江宁织造局并入，别名照录；来源未说明“江南织造”是总称还是江宁一局的别称",
    ),
    (
        "- 证据状态: source_backed（三册来源内复读）\n- 验证层级: 未评定；consensus 为 tentative，按字段契约不填 L1–L7\n- 验证平台: 未使用外部平台\n- 匹配质量: 三册均有直接文本。夏燕靖两版与田自秉对曹玺职务与云锦关系的表述一致（“内务府官”、曹雪芹祖父），可互相印证；分歧在职能表述（“特织御用云锦”／“管理织锦的生产”）与年数（夏燕靖 2016 同段 58 年／60 余年并存）。康熙二年（1663）、雍正五年（1727）、首任郎中、世袭与巡盐等细节仅 2016 一册给出，属单源细节。田自秉所引“173 张／800 张、667 人／2330 人”一组数据系于苏州而非江宁，引用时须防误置\n- 验证日期: 2026-10-25\n- 证据范围: 仅三册 Markdown 文本；未查《明史·食货志》、周汝昌与严中《江宁织造与曹家》原书、内务府档案，未查云锦实物与织机",
        "- 证据状态: source_backed（四册来源内复读）\n- 验证层级: 未评定；consensus 为 tentative，按字段契约不填 L1–L7\n- 验证平台: 未使用外部平台\n- 匹配质量: 三册均有直接文本。夏燕靖两版与田自秉对曹玺职务与云锦关系的表述一致（“内务府官”、曹雪芹祖父），可互相印证；分歧在职能表述（“特织御用云锦”／“管理织锦的生产”）与年数（夏燕靖 2016 同段 58 年／60 余年并存）。康熙二年（1663）、雍正五年（1727）、首任郎中、世袭与巡盐等细节仅 2016 一册给出，属单源细节。田自秉所引“173 张／800 张、667 人／2330 人”一组数据系于苏州而非江宁，引用时须防误置。赵农 2009 仅一句，称“江南织造”“在南京设立”“采买丝绸织物”，未给织造品种、织机、匠役与沿革；“江南织造”的指称范围（总称或江宁一局）来源未明言，属编者按南京一局并入。\n- 验证日期: 2026-10-25\n- 证据范围: 仅四册 Markdown 文本；未查《明史·食货志》、周汝昌与严中《江宁织造与曹家》原书、内务府档案、清代江南三织造档案，未查云锦实物与织机",
    ),
    (
        "1. 夏燕靖. *中国设计史*. 上海: 上海人民美术出版社, 2009.\n2. 田自秉. *中国工艺美术史（修订本）*. 上海: 东方出版中心, 2010.\n3. 夏燕靖. *中国艺术设计史（升级版）*. 上海: 上海人民美术出版社, 2016.",
        "1. 夏燕靖. *中国设计史*. 上海: 上海人民美术出版社, 2009.\n2. 田自秉. *中国工艺美术史（修订本）*. 上海: 东方出版中心, 2010.\n3. 夏燕靖. *中国艺术设计史（升级版）*. 上海: 上海人民美术出版社, 2016.\n4. 赵农. *中国艺术设计史*. 北京: 高等教育出版社, 2009.",
    ),
]


def reconstruct(target: str, pairs: list, expected_citations: int) -> tuple[dict, dict]:
    cur = (ROOT / target).read_text(encoding="utf-8")
    old_text = cur
    for old, new in pairs:
        assert new in old_text, f"{target}: missing new block: {new[:30]}"
        old_text = old_text.replace(new, old, 1)
    replay = old_text
    for old, new in pairs:
        assert old in replay, f"{target}: missing old block: {old[:30]}"
        replay = replay.replace(old, new, 1)
    assert replay == cur, f"{target}: reconstruction mismatch"
    assert old_text.count("- citation:") == expected_citations, (target, old_text.count("- citation:"))
    return fp_bytes(old_text.encode("utf-8")), fp(ROOT / target)


for n, title, target, note in updates:
    pairs = NEIWUFU_PAIRS if "neiwufu" in target else JIANGNING_PAIRS
    expected = 2 if "neiwufu" in target else 3
    before, after = reconstruct(target, pairs, expected)
    plan.append({
        "action": "update", "target_ref": target, "candidate_id": cid(n),
        "entity": title, "before": before, "after_sha256": after["sha256"],
        "bytes": after["bytes"], "lines": after["lines"], "note": note,
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
    "goal": "处理赵农《中国艺术设计史》2009 册 institution 候选 10 个：8 个新建、2 个更新、0 个 no_delta、0 个 rejected。",
    "status": "applied",
    "date": DATE,
    "inputs": {
        "candidate_index": {
            "path": "06-runtime\\state\\candidate-index.jsonl",
            "rows_before": 5339,
            "sha256_before": "sha256:c9aee8261718e648b5eccc3df691136cb7906b683e950a9bfdad40b64cfe01f3",
            "sha256_scope": "CRLF→LF 归一后",
            "counts_before": {"applied": 866, "needs_evidence": 3609, "no_delta": 56, "rejected": 808},
        },
        "source": {
            "doc_id": DOC,
            "file": "03基础书籍-md文档/中国艺术设计史_赵农_2009_高等教育出版社.md",
            "spans": [
                "L6867-L6899", "L7125-L7209", "L7471-L7489", "L7682-L7742",
                "L7868-L7871", "L8484-L8560",
            ],
        },
    },
    "method": {
        "rules": [
            "institution 候选按实体对账：先与既有 institution KU 的标题、别名与正文对齐，再定 create／update／no_delta／rejected。",
            "候选“台湾邮政总局”按清末台湾邮政机构立目：1888 年刘铭传创办，发行“台湾邮票”“邮政商票”两种官商形式邮票，两联发售、一联作存根，为最早商业邮政尝试；不补地址、隶属、邮路、资费与停办时间。",
            "候选“经厂”按明代司礼监所属官方印刷出版机构立目：内府→司礼监的隶属变化、200 余种经厂本、刻工/印工/折配工/装订工与“纸张光洁、版式精美但文字错误较多”的评价；不补书目与印量。",
            "候选“建阳书坊”按明代区域性书坊群立目（80 余家，非单一书坊）：诗文、通俗、小说、医学、插图本与朱熹吕祖谦理学史学著作；杭州 24 家、徽州 10 余家只作比较，不并入本条。",
            "候选“养心殿造办处”判 update：与既有内务府造办处为同一机构的不同称法，加别名并补赵农 2009 的服饰管理句；两册名称差异与来源未明言之处在正文并录。",
            "候选“江南织造”判 update：赵农 2009 明言“在南京设立了江南织造”，按江宁织造局并入，加别名并补“采买丝绸织物”职能；该名在字面上可兼指三织造，指称范围在正文标注。",
            "候选“包豪斯（Bauhaus）”按德国现代设计学校立目：1919 年成立，来源以之为工艺美术与设计学科剥离完成的标志；原文拼写“Bauhuas”照录并标注；不补创办人、课程与校史。",
            "候选“中国营造学社”按传统建筑研究学术团体立目：1925 年朱启钤发起“营造学会”、1930 年改名、1946 年停止活动，成员、古籍整理、实地测绘与抗战期间研究照录；不补章程、经费与成员总数。",
            "候选“金陵机器局”“天津机器局”“湖北枪炮厂”分别按晚清洋务军工企业立目（1865／1867／1891）：来源仅给局名、年份与“官商一体”整体评价，三条件只登记企业本体与五局序列，不补创办人、隶属、产品与沿革。",
            "03基础书籍-md文档只读；本批写 04-knowledge/units/institutions，8 条新建、2 条更新、0 条 rejected。",
        ],
    },
    "outputs": {
        "apply_plan": {"path": f"06-runtime\\automation\\{PKG.name}\\apply-plan.jsonl", "rows": len(plan), "create": len(creates), "update": len(updates)},
        "ledger": {"path": f"06-runtime\\automation\\{PKG.name}\\candidate-decision-ledger.jsonl", "rows": len(ledger), "candidates": len(order), "applied": len(creates) + len(updates), "no_delta": 0, "rejected": 0},
        "canonical_mapping": {"path": f"06-runtime\\automation\\{PKG.name}\\canonical-mapping.json", "entries": len(mapping), "merged_candidates": []},
    },
    "state_after": {},
}
(PKG / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

assert len(ledger) == 30, len(ledger)
assert len(plan) == 10, len(plan)
assert len(mapping) == 10, len(mapping)
print(json.dumps({
    "ledger": len(ledger), "plan": len(plan), "mapping": len(mapping),
    "creates": len(creates), "updates": len(updates), "rejected": 0,
    "update_fingerprints": [p["before"] for p in plan if p["action"] == "update"],
}, ensure_ascii=False))
