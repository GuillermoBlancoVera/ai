#!/usr/bin/env bash

set -euo pipefail

repo_root="$(git rev-parse --show-toplevel)"
cd "$repo_root"

./scripts/update_skill_references.sh

if ! git diff --quiet -- .codex/skills/ai-portfolio-repo-context/references/repo-map.md; then
  printf '%s\n' "Portfolio skill references were refreshed but are not staged."
  printf '%s\n' "Review and stage .codex/skills/ai-portfolio-repo-context/references/repo-map.md before committing."
  exit 1
fi

staged_paths="$(git diff --cached --name-only)"

if printf '%s\n' "$staged_paths" | grep -Eq '^(src/ai_portfolio/|notebooks/)'; then
  if ! printf '%s\n' "$staged_paths" | grep -Eq '^(README\.md|docs/index\.html|notebooks/.+/README\.md)$'; then
    printf '%s\n' "Portfolio examples or notebooks changed without an index update."
    printf '%s\n' "Update and stage README.md, docs/index.html, or the matching notebook README before committing."
    exit 1
  fi
fi

git diff --cached --check

printf '%s\n' "Portfolio sync check passed."
