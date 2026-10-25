import hashlib
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
PKG = ROOT / "06-runtime" / "automation" / "2026-10-25-2011lilixin-places-batch-z"
PKG.mkdir(parents=True, exist_ok=True)
DOC = "2011-lilixin-zhongguo-sheji-yishu-shilun"
DATE = "2026-10-25"


def fp(path: pathlib.Path) -> dict:
    text = path.read_bytes().decode("utf-8").replace("\r\n", "\n").replace("\r", "\n")
    data = text.encode("utf-8")
    return {
        "sha256": "sha256:" + hashlib.sha256(data).hexdigest(),
        "bytes": len(data),
        "lines": text.count("\n"),
    }


creates = [
    ("cand-01-52", "苏州网师园", "04-knowledge/units/places/suzhou-wangshiyuan.md",
     "新建garden：李立新 2011 L326-L328 图注称苏州网师园布局巧妙、结构紧凑，湖石与树木参差错落、疏朗闲适，为中国园林设计中的精品，标注清，引自《中国古建筑》；单条图注，缺建园年代、面积、设计者，confidence 定为 low；不并入拙政园条目"),
    ("cand-02-05", "奥杜韦峡谷", "04-knowledge/units/places/olduvai-gorge.md",
     "新建archaeological_site：李立新 2011 L421、L427 记坦桑尼亚奥杜韦峡谷发现距今200万年前最典型石器工具亦选砾石打制，图1-3 为砾石砍斫器（奥杜韦文化），正文称此类传统为“砾石文化”且其产生是渐进的；缺发掘与研究史，confidence 定为 low"),
    ("cand-02-158", "甘肃庆阳", "04-knowledge/units/places/gansu-qingyang.md",
     "新建geographical_region：李立新 2011 L421 记1920年法国古生物学家桑志华在甘肃庆阳找到一件石核和两件石片，出土于黄土底部砾石层；单句、地点宽泛、无正式遗址名，confidence 定为 low"),
    ("cand-02-11", "薛家岗遗址", "04-knowledge/units/places/xuejiagang-site.md",
     "新建archaeological_site：李立新 2011 L495-L498、L504 记安徽潜山薛家岗出土朱绘有孔石斧（图1-7），并以薛家岗精细石钺上的画痕论“适应”概念；同段推测部分磨光石器为祭坛礼器；单源但器物与判断完整，confidence 定为 medium"),
    ("cand-02-19", "火烧沟遗址", "04-knowledge/units/places/huoshaogou-site.md",
     "新建archaeological_site：李立新 2011 L540 记玉门火烧沟出土人形罐，口部双肩耳短领，罐底座设计成象形双足，形成鼓腹站立人形；作为“象生器”例证与大地湾人头形彩陶瓶并列；缺年代与文化命名，confidence 定为 low"),
    ("cand-02-157", "张家坡遗址", "04-knowledge/units/places/zhangjiapo-site.md",
     "新建archaeological_site：李立新 2011 L635、L640 记西周丰京张家坡墓地出土包铜漆木方盒，为打锻、锤揲工艺例证；又记张家坡遗址青、黄绿釉经测定烧成温度达1200℃、矿物成分近瓷，称原始瓷；缺墓葬与检测报告，confidence 定为 medium"),
    ("cand-02-46", "西水坡遗址", "04-knowledge/units/places/xishuipo-site.md",
     "新建archaeological_site：李立新 2011 L651-L658 记河南濮阳西水坡三组蚌壳摆塑，其中一组龙背骑人，引张光直“巫跻”解释及其“艺术形象似乎也可以发挥实际的作用”之说，图1-21 为龙虎蚌塑；缺发掘与墓葬背景，confidence 定为 medium"),
    ("cand-02-56", "包山楚墓", "04-knowledge/units/places/baoshan-chumu.md",
     "新建archaeological_site：李立新 2011 L685-L688 记包山大冢楚墓漆奁盖圈《车马人物出行图》，直径28厘米，展开长87.4、高5.2厘米，将使臣出访情节的各时间跨度在空间中组成“有机整体”，被视为图形表现时间连续变化的特例；confidence 定为 medium"),
    ("cand-02-156", "江陵马山一号楚墓", "04-knowledge/units/places/jiangling-mashan-yihao-chumu.md",
     "新建archaeological_site：李立新 2011 L701 仅在“与天地人有关的神怪观念”段列江陵马山一号楚墓中的动物、人物纹样，未给墓葬结构、年代与器物细节；单句列举，confidence 定为 low；不把该墓丝织品研究并入"),
    ("cand-02-59", "子弹库楚墓", "04-knowledge/units/places/zidanku-chumu.md",
     "新建archaeological_site：李立新 2011 L701、L704 记长沙子弹库战国帛书上的神怪图纹，图1-26 为楚帛书（湖南长沙子弹库楚墓出土）；缺墓葬与帛书著录，confidence 定为 low"),
    ("cand-02-78", "荣成松郭家村遗址", "04-knowledge/units/places/rongcheng-songguojia-site.md",
     "新建archaeological_site：李立新 2011 L757 记1979年山东荣成松郭家村出土距今4000年前新石器独木舟，壁厚约5厘米、板面平整光洁、有榫卯孔眼，用以论证舟船技术规范化；缺舟体尺寸与树种，confidence 定为 medium"),
    ("cand-02-85", "长沙伍家岭", "04-knowledge/units/places/changsha-wujialing.md",
     "新建archaeological_site：李立新 2011 L773-L775 记湖南长沙伍家岭出土汉代木船模型一件，复原三间舱房，出十六根木桨（每根长52.8厘米、桨叶长25.6厘米）及尾桨约100厘米，论汉代造船设计标准划一；缺墓葬与现藏地，confidence 定为 medium"),
    ("cand-02-88", "武梁祠", "04-knowledge/units/places/wuliangci.md",
     "新建archaeological_site：李立新 2011 L786 仅存图1-32“伏羲女娲手执规矩图（规被人形化）（武梁祠石刻）”图注，配合孟子规矩准绳论；缺祠堂地点、年代、祠主与石刻尺寸，confidence 定为 low，所在地不据来源外常识补写"),
    ("cand-03-28", "阿斯塔那古墓", "04-knowledge/units/places/asitana-gumu.md",
     "新建archaeological_site：李立新 2011 L863-L871、L1070-L1071 记新疆吐鲁番阿斯塔那古墓出土大量北朝织锦，验证北魏孝文帝奖劝农桑、设官营丝织作坊与任民织造；图2-1 云气动物纹织锦、图2-27 花鸟纹锦（北区三八一号墓）；confidence 定为 medium"),
    ("cand-03-27", "孔望山摩崖造像", "04-knowledge/units/places/kongwangshan-moya-zaoxiang.md",
     "新建archaeological_site：李立新 2011 L916 仅以“连云港孔望山有摩崖造像”与沂南汉画像石墓佛像、彭山崖墓一佛二菩萨像并列为佛教传入的造型证据；缺造像年代、数量与题材，confidence 定为 low"),
    ("cand-03-29", "尼雅遗址", "04-knowledge/units/places/niya-site.md",
     "新建archaeological_site：李立新 2011 L916 记1959年新疆民丰尼雅遗址出土东汉腊缬棉布，蓝色印花、半身裸体人物像，具佛教艺术色彩；有学者认为人物为希腊丰收女神或西亚女神伊什塔尔，狮尾、角杯、葡萄等显示东西文化融合；confidence 定为 medium"),
    ("cand-03-30", "法门寺塔基地宫", "04-knowledge/units/places/famen-si-digong.md",
     "新建archaeological_site（canonical）：李立新 2011 L964-L1028、L1681-L1683 记地宫曼荼罗形制与陈设、八重宝函第四重四面造像、捧真身菩萨莲花底座、鎏金卧龟莲花纹朵带五足银熏炉、鎏金飞鸿球路纹银笼子、鎏金茶罗子、贴花盘口琉璃瓶、1987年13件秘色瓷、20件伊斯兰玻璃器与描金刻花蓝玻璃盘；熏炉“高295cm、腹深70cm”疑脱小数点，已标疑；合并 cand-05-08"),
    ("cand-04-33", "嘉兴西塘扬汇", "04-knowledge/units/places/jiaxing-xitang-yanghui.md",
     "新建geographical_region：李立新 2011 L1447-L1454 记元代嘉兴髹漆中心在府城东北西塘扬汇，靖康之乱后工匠南迁，名家张成、杨茂、彭君宝，《格古要论》称其剔红最得名；录张成剔红栀子花圆盘、剔犀漆盒，杨茂剔红花卉渣斗、观瀑图八方盘及张德刚入营缮所；confidence 定为 medium"),
    ("cand-05-04", "岐山凤雏村西周建筑遗址", "04-knowledge/units/places/qishan-fengchucun-yizhi.md",
     "新建archaeological_site：李立新 2011 L1658 记陕西岐山凤雏村西周早期大型建筑遗址，四周通行、前中后三进、左右对称，由屏、门、塾、中庭、大室、东西庭、寝、闱、东西厢、阙、庑共11部分组成，已脱离“茅茨土阶”演化为宫室建筑；缺面积与分期，confidence 定为 medium"),
    ("cand-05-07", "山东博山", "04-knowledge/units/places/shandong-boshan.md",
     "新建geographical_region：李立新 2011 L1683 记元末明初山东博山出现玻璃生产作坊，清代博山玻璃作坊达百余家，康熙设宫廷玻璃厂并雇欧洲工匠，近代汉口、上海、北京、福州、秦皇岛设大型玻璃厂；本条只记博山地点与产业，不重复造办处机构条；confidence 定为 medium"),
    ("cand-05-20", "花厅墓地", "04-knowledge/units/places/huating-mudi.md",
     "新建archaeological_site：李立新 2011 L1755、L1757 记江苏新沂花厅墓地处于大汶口文化与良渚文化交界，出土许多良渚输入品，陶器与玉器具良渚因素，500余件玉器与良渚所产相同，交换与掠夺性战争因素并存；confidence 定为 medium"),
]

updates = [
    ("cand-01-50", "唐长安城", "04-knowledge/units/places/daxing-cheng.md",
     "更新既有daxing-cheng：大兴城即唐长安城，不新建 tang-changancheng；补李立新 2011 L318-L319 图注——布局规整对称、明德门向北为中轴大街、全城分东西、街道纵横形成100多个坊市、中国古代规模最大（引自《文明的轨迹》）；并入历史名称唐长安城、长安城，source_count 2→3、version 1→2",
     {"sha256": "sha256:199ccc354cf609478ebb4dc568a32ace6647877758bd1f8dd54060f1cf4788ec", "bytes": 3951, "lines": 86}),
    ("cand-02-32", "殷墟妇好墓", "04-knowledge/units/places/fuhao-tomb.md",
     "更新既有fuhao-tomb：补李立新 2011 L642 记妇好墓出土755件精美玉器，证明殷商刮摩治玉技术成熟，并论玉器与政治、经济、礼乐文化关联；赵农426件与李立新755件并列，统计口径待考；source_count 2→3、version 1→2",
     {"sha256": "sha256:704d3e7dc9d45b1f59bf5f27b1d9efea256763f8e5dd440f4e317b708920b68f", "bytes": 3998, "lines": 83}),
    ("cand-02-95", "马王堆一号汉墓", "04-knowledge/units/places/mawangdui-hanmu.md",
     "更新既有mawangdui-hanmu：补李立新 2011 L814 记1号墓成套漆食具（耳杯一、卮二、盘五及竹箸）与耳杯盒（七只耳杯，六顺一反，反扣杯两耳断面三角形相扣合）；原文“耳环”疑为“耳杯”，已标疑；source_count 2→3、version 1→2",
     {"sha256": "sha256:490db9fd8c7154222560e8563611c1c34414d34ed4a172b2bc5251c5cccaace3", "bytes": 4188, "lines": 85}),
]

no_delta = [
    ("cand-05-08", "法门寺地宫", "04-knowledge/units/places/famen-si-digong.md",
     "no_delta：与 cand-03-30“法门寺塔基地宫”同指法门寺地宫；其20件伊斯兰玻璃器与描金刻花蓝玻璃盘内容已并入 canonical create 的 famen-si-digong.md，不重复写回，合并记录进 canonical-mapping"),
]

ledger = []
for cid, entity, target, note in [(c[0], c[1], c[2], c[3]) for c in creates + updates]:
    action_word = "更新" if target in {u[2] for u in updates} else "新建"
    ledger.append({
        "candidate_id": f"{DOC}:{cid}",
        "expected_state": "needs_evidence",
        "state": "ready_for_review",
        "decision": {"status": "pending", "reason": f"已完成语义复读：{action_word} {target}", "decided_by": "Agent", "decided_at": DATE},
        "updated_at": DATE,
    })
    ledger.append({
        "candidate_id": f"{DOC}:{cid}",
        "expected_state": "ready_for_review",
        "state": "approved",
        "decision": {"status": "approved", "reason": f"canonical 候选语义复读完成，批准{action_word} {target}", "decided_by": "Agent", "decided_at": DATE},
        "updated_at": DATE,
    })
    ledger.append({
        "candidate_id": f"{DOC}:{cid}",
        "expected_state": "approved",
        "state": "applied",
        "decision": {"status": "approved", "reason": f"已判定 applied：{action_word} {target}", "decided_by": "Agent", "decided_at": DATE},
        "updated_at": DATE,
        "target_ref": target,
    })

for cid, entity, target, note in no_delta:
    ledger.append({
        "candidate_id": f"{DOC}:{cid}",
        "expected_state": "needs_evidence",
        "state": "ready_for_review",
        "decision": {"status": "pending", "reason": f"已完成语义复读：{target} 已有 canonical 候选，待合并判定", "decided_by": "Agent", "decided_at": DATE},
        "updated_at": DATE,
    })
    ledger.append({
        "candidate_id": f"{DOC}:{cid}",
        "expected_state": "ready_for_review",
        "state": "approved",
        "decision": {"status": "approved", "reason": f"批准作为合并候选并入 {target}，不重复写回", "decided_by": "Agent", "decided_at": DATE},
        "updated_at": DATE,
    })
    ledger.append({
        "candidate_id": f"{DOC}:{cid}",
        "expected_state": "approved",
        "state": "no_delta",
        "decision": {"status": "approved", "reason": f"判定 no_delta：内容已并入 canonical create，target {target}", "decided_by": "Agent", "decided_at": DATE},
        "updated_at": DATE,
        "target_ref": target,
    })

plan = []
for cid, entity, target, note in creates:
    f = fp(ROOT / target)
    plan.append({
        "action": "create",
        "target_ref": target,
        "candidate_id": f"{DOC}:{cid}",
        "entity": entity,
        "before": None,
        "after_sha256": f["sha256"],
        "bytes": f["bytes"],
        "lines": f["lines"],
        "note": note,
    })
for cid, entity, target, note, before in updates:
    f = fp(ROOT / target)
    plan.append({
        "action": "update",
        "target_ref": target,
        "candidate_id": f"{DOC}:{cid}",
        "entity": entity,
        "before": before,
        "after_sha256": f["sha256"],
        "bytes": f["bytes"],
        "lines": f["lines"],
        "note": note,
    })

merged = [f"{DOC}:{n[0]}" for n in no_delta]
mapping = []
for cid, entity, target, note in creates:
    item = {
        "entity": entity,
        "target_ref": target,
        "action": "create",
        "canonical_candidate": f"{DOC}:{cid}",
        "merged_candidates": [],
    }
    if target == "04-knowledge/units/places/famen-si-digong.md":
        item["merged_candidates"] = merged
    mapping.append(item)
for cid, entity, target, note, before in updates:
    mapping.append({
        "entity": entity,
        "target_ref": target,
        "action": "update",
        "canonical_candidate": f"{DOC}:{cid}",
        "merged_candidates": [],
    })

assert len(ledger) == 75, len(ledger)
assert len(plan) == 24, len(plan)
assert len(mapping) == 24, len(mapping)
assert sum(1 for r in plan if r["action"] == "create") == 21
assert sum(1 for r in plan if r["action"] == "update") == 3

(PKG / "candidate-decision-ledger.jsonl").write_text(
    "\n".join(json.dumps(r, ensure_ascii=False) for r in ledger) + "\n", encoding="utf-8"
)
(PKG / "apply-plan.jsonl").write_text(
    "\n".join(json.dumps(r, ensure_ascii=False) for r in plan) + "\n", encoding="utf-8"
)
(PKG / "canonical-mapping.json").write_text(
    json.dumps(mapping, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
)

manifest = {
    "work_package": "2026-10-25-2011lilixin-places-batch-z",
    "goal": "处理李立新《中国设计艺术史论》2011 册 place 候选 25 个：21 个新建、3 个更新、1 个 no_delta、0 个 rejected。",
    "status": "applied",
    "date": DATE,
    "inputs": {
        "candidate_index": {
            "path": "06-runtime\\state\\candidate-index.jsonl",
            "rows_before": 5339,
            "sha256_before": "sha256:39f64e7d09fa93c28f0c8598fb85dbe77cb6e4df03d5d3d2025bdafa437841f0",
            "sha256_scope": "CRLF→LF 归一后",
            "counts_before": {"applied": 933, "needs_evidence": 3537, "no_delta": 57, "rejected": 812},
        },
        "source": {
            "doc_id": DOC,
            "file": "03基础书籍-md文档/中国设计艺术史论_李立新_2011_人民出版社.md",
            "spans": [
                "L318-L319", "L326-L328", "L421", "L421-L427", "L495-L504", "L540",
                "L635", "L640", "L642", "L651-L658", "L685-L688", "L701", "L704",
                "L757", "L773-L775", "L786", "L814", "L863-L871", "L916",
                "L964-L1028", "L1070-L1071", "L1447-L1454", "L1658",
                "L1681-L1683", "L1755-L1757",
            ],
        },
    },
    "method": {
        "rules": [
            "place 候选先与既有 41 个 place KU 对账，再定 create／update／no_delta／rejected。",
            "唐长安城判 update 既有 `places/daxing-cheng.md`：大兴城为唐长安城前身与同城异名，不新建 `tang-changancheng.md`；补李立新图注明德门中轴、100多个坊市与“规模最大”判断，source_count 2→3、version 1→2。",
            "殷墟妇好墓判 update 既有 `places/fuhao-tomb.md`：补李立新 755 件玉器与刮摩治玉技术判断；赵农 426 件与李立新 755 件数目不同，统计口径未明，两说并列不改数。",
            "马王堆一号汉墓判 update 既有 `places/mawangdui-hanmu.md`：补李立新成套漆食具与耳杯盒；原文“耳环”按器物组合疑为“耳杯”，照录并标疑。",
            "法门寺塔基地宫与法门寺地宫两个候选同指一地：以 `cand-03-30` 为 canonical 新建 `famen-si-digong.md`，两段内容合并写入；`cand-05-08` 判 no_delta 并记入 `merged_candidates`。",
            "其余 18 个候选按遗址／地点实体新建；图注单条、单句列举或地点宽泛者 confidence 定 low，器物与判断较完整者定 medium；全部 consensus 为 tentative，不评 L1–L7。",
            "place 的 sub_type 使用 archaeological_site、garden、geographical_region；所在地与年代只写来源可证者，来源未记者不据来源外常识补写。",
            "03基础书籍-md文档只读；本批写 04-knowledge/units/places；不 commit、不 push。",
        ]
    },
    "outputs": {
        "apply_plan": {"path": "06-runtime\\automation\\2026-10-25-2011lilixin-places-batch-z\\apply-plan.jsonl", "rows": 24, "create": 21, "update": 3},
        "ledger": {"path": "06-runtime\\automation\\2026-10-25-2011lilixin-places-batch-z\\candidate-decision-ledger.jsonl", "rows": 75, "candidates": 25, "applied": 24, "no_delta": 1, "rejected": 0},
        "canonical_mapping": {"path": "06-runtime\\automation\\2026-10-25-2011lilixin-places-batch-z\\canonical-mapping.json", "entries": 24, "merged_candidates": merged},
    },
    "state_after": {"applied": 957, "needs_evidence": 3512, "no_delta": 58, "rejected": 812, "total": 5339},
}

(PKG / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"ledger": len(ledger), "plan": len(plan), "mapping": len(mapping), "pkg": str(PKG)}, ensure_ascii=False, indent=2))
