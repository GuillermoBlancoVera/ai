#!/usr/bin/env python3

"""Clear outputs and execution counts from staged Jupyter notebooks."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


def staged_notebooks() -> list[Path]:
    result = subprocess.run(
        ["git", "diff", "--cached", "--name-only", "--diff-filter=ACMR"],
        check=True,
        capture_output=True,
        text=True,
    )
    return [Path(line) for line in result.stdout.splitlines() if line.endswith(".ipynb")]


def strip_notebook(path: Path) -> bool:
    data = json.loads(path.read_text(encoding="utf-8"))
    changed = False

    for cell in data.get("cells", []):
        if cell.get("cell_type") != "code":
            continue

        if cell.get("outputs"):
            cell["outputs"] = []
            changed = True

        if cell.get("execution_count") is not None:
            cell["execution_count"] = None
            changed = True

    metadata = data.get("metadata", {})
    if "widgets" in metadata:
        metadata.pop("widgets", None)
        changed = True

    if changed:
        path.write_text(json.dumps(data, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")

    return changed


def main() -> int:
    notebooks = staged_notebooks()
    if not notebooks:
        return 0

    changed_paths: list[str] = []
    for notebook in notebooks:
        if notebook.exists() and strip_notebook(notebook):
            subprocess.run(["git", "add", str(notebook)], check=True)
            changed_paths.append(str(notebook))

    if changed_paths:
        print("Stripped notebook outputs:")
        for path in changed_paths:
            print(f"  - {path}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
