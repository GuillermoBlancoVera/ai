---
name: ai-portfolio-repo-context
description: Use when working anywhere in this repository and you need the local conventions, project layout, portfolio goals, or a compact repo-aware workflow. Especially useful before making structural changes, updating README/docs, or adding new AI examples.
---

# AI Portfolio Repo Context

This skill gives the minimum repository-specific context needed to work efficiently in this repo without re-reading the whole tree.

## Use this skill to

- understand the repo purpose and public-facing positioning,
- follow naming and placement conventions,
- keep the portfolio presentation aligned with the code,
- refresh skill references after structural changes.

## Repo intent

This repository is a personal AI portfolio, not a course or toy sandbox.

Priorities:

1. Keep everything in English.
2. Make the repository work as both a personal presentation and a practical index of its contents.
3. Prefer clear, runnable scripts as the source of truth.
4. Use notebooks as presentation layers or exploration companions.
5. Keep the GitHub Pages site in `docs/` aligned with the repository content.

## Workflow

1. Read [references/repo-map.md](references/repo-map.md) for the current structure.
2. If the task adds, removes, or renames important files or folders, run:

```bash
./scripts/update_skill_references.sh
```

3. If portfolio positioning changes, update both `README.md` and `docs/index.html`.
4. Keep new examples grouped by paradigm under `src/ai_portfolio/`.
5. Before committing development changes, run:

```bash
./scripts/check_portfolio_sync.sh
```

## Placement rules

- Put runnable code in `src/ai_portfolio/<category>/`.
- Put notebook stubs or walkthrough notebooks in `notebooks/<category>/`.
- Put public static portfolio assets in `docs/`.
- Keep heavy generated artifacts out of git unless they are intentionally part of the portfolio.

## Categories

- `classical_ml`
- `unsupervised_ml`
- `deep_learning`
- `generative_ai`

## Maintenance rule

Whenever you change examples, notebooks, folders, or public-facing portfolio content, keep the skill references and index surfaces synchronized before finishing:

- run `./scripts/update_skill_references.sh` after structural changes,
- update `README.md`, `docs/index.html`, or the relevant notebook README when examples or notebooks change,
- run `./scripts/check_portfolio_sync.sh` before committing.
