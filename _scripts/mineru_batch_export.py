#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""MinerU 批量解析导出：把一个目录下的章节 PDF 全部转成 Markdown。

输出结构与既有资料库一致：<目标目录>/<pdf文件名>-<zip uuid>/full.md + images/ + layout.json ...

用法:
  python mineru_batch_export.py <源目录> <目标目录> [--model vlm|pipeline] [--ocr] [--skip-existing]

token 读取顺序：环境变量 MINERU_TOKEN → <workspace>/mineru/config.json
"""
import argparse
import http.client
import json
import os
import shutil
import ssl
import sys
import time
import urllib.error
import urllib.request
import zipfile
from urllib.parse import urlsplit

BASE = "https://mineru.net/api/v4"
CFG_CANDIDATES = [
    os.environ.get("MINERU_CONFIG", ""),
    r"C:\Users\lenovo\WorkBuddy AI\2026-10-24-15-35-43\mineru\config.json",
]


def load_token():
    if os.environ.get("MINERU_TOKEN"):
        return os.environ["MINERU_TOKEN"]
    for p in CFG_CANDIDATES:
        if p and os.path.exists(p):
            with open(p, encoding="utf-8") as f:
                return json.load(f)["token"]
    sys.exit("未找到 MinerU token")


TOKEN = load_token()


def api(method, path, payload=None, timeout=90):
    data = json.dumps(payload, ensure_ascii=False).encode() if payload is not None else None
    headers = {"Authorization": "Bearer " + TOKEN}
    if data:
        headers["Content-Type"] = "application/json"
    req = urllib.request.Request(BASE + path, data=data, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return json.loads(r.read().decode())
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", "replace")
        try:
            return json.loads(body)
        except Exception:
            return {"code": -1, "msg": f"HTTP {e.code}: {body[:200]}"}


def put_file(url, path):
    """OSS 签名上传：不能带 Content-Type，所以用 http.client 发原始 PUT。"""
    with open(path, "rb") as f:
        blob = f.read()
    parts = urlsplit(url)
    # 部分 OSS 节点证书密钥强度偏低，Python 3.13 默认 SECLEVEL 会直接拒绝握手
    ctx = ssl.create_default_context()
    try:
        ctx.set_ciphers("DEFAULT@SECLEVEL=1")
    except ssl.SSLError:
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE
    conn = http.client.HTTPSConnection(parts.netloc, timeout=600, context=ctx)
    p = parts.path + (("?" + parts.query) if parts.query else "")
    conn.putrequest("PUT", p, skip_accept_encoding=True)
    conn.putheader("Content-Length", str(len(blob)))
    conn.endheaders()
    conn.send(blob)
    resp = conn.getresponse()
    body = resp.read().decode("utf-8", "replace")
    conn.close()
    if resp.status not in (200, 201):
        print(f"  upload host={parts.netloc} resp={body[:300]}")
    return resp.status


def download(url, dest):
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req, timeout=300) as r, open(dest, "wb") as f:
        shutil.copyfileobj(r, f)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("src")
    ap.add_argument("dst")
    ap.add_argument("--model", default="vlm")
    ap.add_argument("--ocr", action="store_true")
    ap.add_argument("--skip-existing", action="store_true")
    ap.add_argument("--timeout", type=int, default=3600)
    a = ap.parse_args()

    src = os.path.abspath(a.src)
    dst = os.path.abspath(a.dst)
    os.makedirs(dst, exist_ok=True)

    pdfs = sorted(f for f in os.listdir(src) if f.lower().endswith(".pdf"))
    if not pdfs:
        sys.exit(f"{src} 下没有 PDF")

    if a.skip_existing:
        keep = []
        for f in pdfs:
            stem = os.path.splitext(f)[0]
            if any(d.startswith(stem + ".pdf-") or d.startswith(stem + "-")
                   for d in os.listdir(dst)):
                print(f"[跳过] {f} 已有输出")
                continue
            keep.append(f)
        pdfs = keep
        if not pdfs:
            print("全部已存在，无需处理")
            return

    print(f"共 {len(pdfs)} 个文件，模型 {a.model}，提交任务...")

    payload = {
        "files": [{"name": f} for f in pdfs],
        "model_version": a.model,
        "language": "ch",
        "enable_formula": True,
        "enable_table": True,
        "is_ocr": bool(a.ocr),
    }
    res = api("POST", "/file-urls/batch", payload)
    if res.get("code") != 0:
        sys.exit(f"提交失败: {res}")
    batch_id = res["data"]["batch_id"]
    urls = res["data"]["file_urls"]
    print(f"batch_id={batch_id}")

    for f, u in zip(pdfs, urls):
        size = os.path.getsize(os.path.join(src, f)) / 1048576
        code = put_file(u, os.path.join(src, f))
        print(f"  上传 {f} ({size:.1f} MB) -> HTTP {code}", flush=True)
        if code not in (200, 201):
            print(f"  !! 上传失败 {f}")

    print("上传完成，等待解析...")
    start = time.time()
    done = {}
    while time.time() - start < a.timeout:
        r = api("GET", f"/extract-results/batch/{batch_id}")
        items = (r.get("data") or {}).get("extract_result") or []
        pending = 0
        for it in items:
            name, state = it.get("file_name"), it.get("state")
            if state == "done" and name not in done:
                done[name] = it
                print(f"  [完成] {name}", flush=True)
            elif state == "failed":
                print(f"  [失败] {name}: {it.get('err_msg')}", flush=True)
                done[name] = it
            elif state not in ("done", "failed"):
                pending += 1
        if pending == 0 and len(done) >= len(pdfs):
            break
        prog = items[0].get("extract_progress") if items else None
        print(f"  [{int(time.time()-start)}s] 待解析 {pending} 个"
              + (f"，首个进度 {prog.get('extracted_pages')}/{prog.get('total_pages')} 页" if prog else ""),
              flush=True)
        time.sleep(15)

    print("\n下载并解压...")
    ok = 0
    for f in pdfs:
        it = done.get(f)
        if not it or it.get("state") != "done":
            print(f"  [跳过] {f} 未成功解析")
            continue
        zip_url = it["full_zip_url"]
        uid = os.path.basename(zip_url).rsplit(".", 1)[0]
        stem = os.path.splitext(f)[0]
        outdir = os.path.join(dst, f"{stem}.pdf-{uid}")
        tmp = os.path.join(dst, f"_{uid}.zip")
        download(zip_url, tmp)
        if os.path.isdir(outdir):
            shutil.rmtree(outdir)
        os.makedirs(outdir, exist_ok=True)
        with zipfile.ZipFile(tmp) as z:
            z.extractall(outdir)
        os.remove(tmp)
        md = os.path.join(outdir, "full.md")
        chars = len(open(md, encoding="utf-8").read()) if os.path.exists(md) else 0
        print(f"  {stem}.pdf-{uid}  full.md {chars} 字符")
        ok += 1

    print(f"\n完成 {ok}/{len(pdfs)} 个")


if __name__ == "__main__":
    main()
