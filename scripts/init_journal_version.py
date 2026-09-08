#!/usr/bin/env python3
"""Create an isolated target-journal version from a frozen submission mother."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import shutil
from datetime import datetime, timezone
from pathlib import Path


def digest(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def copy_atomic(source: Path, destination: Path) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    temporary = destination.with_suffix(destination.suffix + ".tmp")
    shutil.copy2(source, temporary)
    os.replace(temporary, destination)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--project-dir", required=True, type=Path)
    parser.add_argument("--decision", required=True, type=Path)
    parser.add_argument("--mother-cn", type=Path)
    parser.add_argument("--mother-en", required=True, type=Path)
    args = parser.parse_args()
    project = args.project_dir.expanduser().resolve()
    decision = json.loads(args.decision.expanduser().resolve().read_text(encoding="utf-8"))
    if decision.get("status") != "locked":
        raise SystemExit("journal_decision.json must be locked before adaptation.")
    slug = decision["target_journal"]["slug"]
    base = project / "journal_versions" / slug
    state_path = base / "version_state.json"
    if state_path.exists():
        print(state_path)
        return
    for rel in ("manuscript/en",):
        (base / rel).mkdir(parents=True, exist_ok=True)
    sources = {}
    if args.mother_cn:
        source = args.mother_cn.expanduser().resolve()
        target = base / "manuscript" / "cn" / f"paper_cn_{slug}.docx"
        copy_atomic(source, target)
        sources["cn"] = {"path": str(source), "sha256": digest(source), "derived": str(target)}
    source = args.mother_en.expanduser().resolve()
    target = base / "manuscript" / "en" / f"paper_en_{slug}.docx"
    copy_atomic(source, target)
    sources["en"] = {"path": str(source), "sha256": digest(source), "derived": str(target)}
    state = {
        "schema_version": 1, "journal": decision["target_journal"],
        "created_at": datetime.now(timezone.utc).isoformat(), "status": "initialized",
        "sources": sources, "active_manuscript": str(target),
        "auto_generate_submission": False,
        "gates": {"zotero": "pending", "bilingual": "pending" if args.mother_cn else "not_applicable", "figures": "pending", "formulas": "pending", "tables": "pending", "submission": "not_requested"},
    }
    state_path.write_text(json.dumps(state, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (base / "revision_ledger.md").write_text(f"# Revision Ledger: {decision['target_journal']['journal']}\n\n", encoding="utf-8")
    print(state_path)


if __name__ == "__main__":
    main()
