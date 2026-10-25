"""Validate the delivered archive in an isolated temporary directory."""
from __future__ import annotations

from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import zipfile

from verify_copy import check


OUT = Path(__file__).resolve().parent
SOURCE = OUT.parent
ARCHIVE = OUT / "knowledge-distillation-workflow.zip"


def main() -> None:
    report = {
        "checked_at_utc": datetime.now(timezone.utc).isoformat(),
        "archive": ARCHIVE.name,
        "python": sys.version,
        "archive_integrity": check(ARCHIVE),
        "source_copy_mismatches": [],
        "checks": [],
        "not_verified": [
            "新领域配置与结构节点的语义适配",
            "目标客户端 Hook 的加载、信任与真实执行",
            "目标机器 Claude Skill 符号链接恢复与发现",
            "外部联网 collector 的实时访问",
            "迁移后网页交互及项目文案的正确性",
            "包含 Git、真实知识、评测和派生基线的全仓发布门禁",
        ],
    }
    if not report["archive_integrity"]["passed"]:
        raise SystemExit(json.dumps(report, ensure_ascii=False))
    manifest = json.loads((OUT / "workflow-copy-manifest.json").read_text(encoding="utf-8"))
    for record in manifest["files"]:
        if "source_path" not in record:
            continue
        source = SOURCE / record["source_path"]
        data = (str(source.readlink()).replace("\\", "/").encode("utf-8")
                if source.is_symlink() else source.read_bytes())
        if hashlib.sha256(data).hexdigest() != record["sha256"]:
            report["source_copy_mismatches"].append(record["source_path"])

    env = dict(os.environ, PYTHONIOENCODING="utf-8", PYTHONDONTWRITEBYTECODE="1")
    commands = [
        ("extracted_file_integrity", [sys.executable, "-B", "portable/verify_copy.py", "."]),
        ("skill_registry_and_references", [sys.executable, "-B", "scripts/skill_registry.py"]),
        ("all_copied_tests_with_isolated_fixtures", [sys.executable, "-B", "portable/run_tests.py"]),
    ]
    with tempfile.TemporaryDirectory(prefix="ikd-workflow-verify-") as temp:
        stage = Path(temp)
        with zipfile.ZipFile(ARCHIVE) as archive:
            archive.extractall(stage)  # paths checked by check() above
        for name, command in commands:
            print("Running " + name, flush=True)
            result = subprocess.run(command, cwd=stage, env=env, encoding="utf-8",
                                    errors="replace", capture_output=True, timeout=240)
            output = result.stdout + result.stderr
            (OUT / (name + ".log")).write_text(output, encoding="utf-8")
            report["checks"].append({"name": name, "command": command,
                                     "cwd": "isolated temporary extraction outside source checkout",
                                     "exit_code": result.returncode, "log": name + ".log"})
            print(output[-2500:], flush=True)
        # Tests must not alter the copied contracts, code or template payload.
        report["post_test_integrity"] = check(stage)

    report["passed"] = (not report["source_copy_mismatches"]
                        and report["post_test_integrity"]["passed"]
                        and all(row["exit_code"] == 0 for row in report["checks"]))
    (OUT / "validation-report.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))
    raise SystemExit(0 if report["passed"] else 1)


if __name__ == "__main__":
    main()
