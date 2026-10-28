import json

d = json.load(open("_zn_decisions_ch4.json", encoding="utf-8"))
for x in d["decisions"]:
    cid = x["cid"].split(":")[-1]
    tgt = x["target"].replace("04-knowledge/units/", "")
    print(f"| {cid} | {x['entity']} | {x['action']} | `{tgt}` |")
