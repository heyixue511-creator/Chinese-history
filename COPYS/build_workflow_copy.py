"""Export the current workflow without copying research data or active Skill roots.

Run from the source checkout: python COPYS/build_workflow_copy.py
The archive keeps original workflow files byte-for-byte. Generated scaffolding is
identified separately in the manifest. Replacing this export requires --replace.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile
from datetime import datetime, timezone
import zipfile


BASE = Path(__file__).resolve().parents[1]
OUT = Path(__file__).resolve().parent
ARCHIVE = OUT / "knowledge-distillation-workflow.zip"
PREFIXES = (".agents/", ".claude/", ".codex/", ".github/", "scripts/", "tests/", "01-domain/")
EXACT = {
    "AGENTS.md", "CLAUDE.md", "README.md", "pyproject.toml", ".gitignore", ".gitattributes",
    "03-processing/README.md", "05-outputs/README.md", "05-outputs/drafts/README.md",
    "05-outputs/index/README.md", "06-runtime/README.md", "06-runtime/checkpoints/README.md",
    "06-runtime/traces/README.md", "05-outputs/knowledge-graph.html",
    "05-outputs/knowledge-graph-2d.html", "05-outputs/knowledge-graph-v2.css",
}
DIRS = [
    "02-sources", "03-processing", "04-knowledge/quality/conflicts",
    "04-knowledge/structure/hierarchy", "04-knowledge/structure/taxonomy",
    "05-outputs/exports", "05-outputs/drafts", "05-outputs/index",
    "06-runtime/state", "06-runtime/governance", "06-runtime/automation",
    "06-runtime/eval", "06-runtime/checkpoints", "06-runtime/traces",
] + ["04-knowledge/units/" + name for name in (
    "persons", "institutions", "places", "works", "publications", "terms", "procedures", "events"
)] + ["04-knowledge/structure/" + name for name in ("domains", "dimensions", "themes", "topics")]


def git(*args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=BASE).decode("utf-8")


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def main() -> None:
    if ARCHIVE.exists() and "--replace" not in sys.argv:
        raise SystemExit(f"Refusing to overwrite existing archive: {ARCHIVE}")
    tracked = git("ls-files", "-z").split("\0")
    selected = sorted(path for path in tracked if path and (
        path.startswith(PREFIXES) or path in EXACT
        or path.startswith("05-outputs/vendor/")
        or path.startswith("05-outputs/assets/")
        or (path.startswith("04-knowledge/structure/") and path.endswith("/README.md"))
    ))
    forbidden = ("settings.local.json", ".env", ".pyc")
    if any(Path(path).name in forbidden or "__pycache__" in Path(path).parts for path in selected):
        raise SystemExit("Selection contains a local or cache file")

    records: list[dict] = []
    files: dict[str, bytes] = {}
    for path in selected:
        source = BASE / path
        if source.is_symlink():
            data = str(source.readlink()).replace("\\", "/").encode("utf-8")
            kind = "symlink_target_stub"
        else:
            data = source.read_bytes()
            kind = "exact_source_copy"
        files[path] = data
        records.append({"path": path, "kind": kind, "source_path": path,
                        "sha256": digest(data), "bytes": len(data)})

    def add(path: str, text: str) -> None:
        if path in files:
            raise ValueError(f"Generated file would overwrite a source file: {path}")
        data = text.encode("utf-8")
        files[path] = data
        records.append({"path": path, "kind": "generated_portable_scaffold",
                        "sha256": digest(data), "bytes": len(data)})

    guide = (OUT / "reuse-guide.md").read_text(encoding="utf-8")
    add("REUSE.md", guide)
    add("portable/verify_copy.py", (OUT / "verify_copy.py").read_text(encoding="utf-8"))
    add("portable/run_tests.py", (OUT / "run_portable_tests.py").read_text(encoding="utf-8"))
    for directory in DIRS:
        add(directory + "/.gitkeep", "")
    add("02-sources/_catalog.md", "# 来源目录\n\n本复用副本尚未登记来源。按 ingest 契约追加本项目来源；未复制原项目书籍或全文。\n")
    add("04-knowledge/quality/claim-registry.yml", "# 新项目断言表；尚无断言。\n[]\n")
    add("04-knowledge/quality/relation-index.yml", "# 新项目空关系投影；使用 build_relation_index.py 重建。\n[]\n")
    add("04-knowledge/quality/relation-candidates.yml", "# 新项目空关系候选；不表示语义审查已完成。\n[]\n")
    add("04-knowledge/quality/translation-index.yml", "# 新项目空翻译投影；使用 build_translation_index.py 重建。\n[]\n")
    add("04-knowledge/quality/verification-log.md", "# 验证日志\n\n尚无本项目验证写回记录。\n")
    add("05-outputs/output-registry.yml", "# 新项目输出登记；尚无输出。\n[]\n")
    add("06-runtime/eval/query-eval-set.jsonl", "")
    add("06-runtime/governance/relation-generic-explicit-baseline.jsonl", "")
    add("06-runtime/governance/taxonomy-migration-map.json", json.dumps({
        "status": "not_initialized", "total_entries": 0, "entries": []
    }, ensure_ascii=False, indent=2) + "\n")
    add("06-runtime/governance/system-upgrade-log.md", "# 系统升级记录\n\n## 工作流复刻初始化\n\n- 原工作流按字节复刻，来源及哈希见 workflow-copy-manifest.json。\n- 新增空数据目录与复用说明，不复制源项目知识和历史验收结果。\n- 未执行新领域语义适配，未初始化 Git，未启用或验证客户端 Hook。\n- 复制与回归验证结果见交付文件夹的 validation-report.json。\n- 新项目正式运行后在本文件追加其自身升级记录。\n")
    add("06-runtime/governance/governance-backlog.md", "# 新项目初始化状态\n\n尚未完成领域配置、客户端适配和首次知识摄入；不声明健康或语义验收通过。详见 REUSE.md。\n")

    # Validate and generate only data-independent artifacts in an isolated root.
    with tempfile.TemporaryDirectory(prefix="ikd-workflow-build-") as temp:
        stage = Path(temp)
        for path, data in files.items():
            destination = stage / path
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_bytes(data)
        for script in ("skill_registry.py", "build_runtime_index.py", "build_knowledge_graph_data.py"):
            command = [sys.executable, "-B", "scripts/" + script]
            if script == "skill_registry.py":
                command.append("--export")
            result = subprocess.run(command, cwd=stage, text=True, encoding="utf-8",
                                    errors="replace", capture_output=True)
            if result.returncode:
                raise SystemExit(f"{script} failed:\n{result.stdout}\n{result.stderr}")
        for path in ("06-runtime/state/skill-registry.json", "06-runtime/automation/index.md",
                     "05-outputs/knowledge-graph-data.json", "05-outputs/knowledge-graph-data.js"):
            add(path, (stage / path).read_text(encoding="utf-8"))

    add("05-outputs/knowledge-graph-2d-data.json", files["05-outputs/knowledge-graph-data.json"].decode("utf-8"))
    add("05-outputs/knowledge-graph-2d-data.js", files["05-outputs/knowledge-graph-data.js"].decode("utf-8"))
    # No frozen graph manifest is copied: the old manifest describes old knowledge.
    timestamp = datetime.now(timezone.utc).isoformat()
    manifest = {
        "schema_version": 1, "created_at_utc": timestamp,
        "source_project": "Infographic Knowledge Distillation",
        "source_commit": git("rev-parse", "HEAD").strip(),
        "source_git_status_before_export": git("status", "--porcelain", "--untracked-files=no").strip(),
        "scope": "complete current workflow contracts, skills, executors, tests, adapters and UI code; no research corpus",
        "source_file_count": len(selected),
        "generated_file_count": len(records) - len(selected),
        "skill_count": sum(path.endswith("/SKILL.md") for path in selected),
        "script_python_count": sum(path.startswith("scripts/") and path.endswith(".py") for path in selected),
        "test_python_count": sum(path.startswith("tests/") and path.endswith(".py") for path in selected),
        "excluded": [".git/ and remote credentials", "local settings and secrets", "source books and source texts",
                     "processing evidence and historical work packages", "knowledge units, claims and relations",
                     "materialized domain/dimension/theme/topic nodes", "source-project health and acceptance snapshots",
                     "source-project evaluation cases and migration mappings", "caches, virtual environments and temporary files"],
        "portability": "source domain settings and branded UI retained unchanged; review REUSE.md before activation",
        "files": sorted(records, key=lambda row: row["path"]),
        "manifest_hash_boundary": "This manifest excludes itself; the outer archive SHA-256 covers all archive bytes.",
    }
    manifest_bytes = (json.dumps(manifest, ensure_ascii=False, indent=2) + "\n").encode("utf-8")
    files["workflow-copy-manifest.json"] = manifest_bytes
    next_archive = OUT / "knowledge-distillation-workflow.next.zip"
    if next_archive.exists():
        raise SystemExit("Staging archive already exists: " + str(next_archive))
    with zipfile.ZipFile(next_archive, "x", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for path, data in sorted(files.items()):
            archive.writestr(path, data)
    if next_archive.resolve().parent != OUT.resolve() or ARCHIVE.resolve().parent != OUT.resolve():
        raise ValueError("Archive path escapes export directory")
    next_archive.replace(ARCHIVE)
    (OUT / "workflow-copy-manifest.json").write_bytes(manifest_bytes)
    (OUT / "SHA256SUMS.txt").write_text(digest(ARCHIVE.read_bytes()) + "  " + ARCHIVE.name + "\n", encoding="utf-8")
    print(json.dumps({"archive": str(ARCHIVE), "archive_bytes": ARCHIVE.stat().st_size,
                      "archive_files": len(files), "skills": manifest["skill_count"],
                      "source_files": len(selected), "scripts": manifest["script_python_count"],
                      "tests": manifest["test_python_count"]}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
