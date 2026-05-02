---
name: ai-portfolio-site
description: Use when updating the public HTML portfolio in docs/, especially when the repo examples, sections, or public positioning change and the GitHub Pages site needs to stay in sync.
---

# AI Portfolio Site

Use this skill for work in `docs/`.

## Purpose

The site is a lightweight GitHub Pages presentation layer for the repository. It should mirror the repo honestly and make a strong first impression in interviews.

## Workflow

1. Read [references/site-content-rules.md](references/site-content-rules.md).
2. Update `docs/index.html` and `docs/styles.css` as needed.
3. If the public framing changes, keep `README.md` and the site aligned.
4. If the repo structure changes enough to affect the site copy, run:

```bash
./scripts/update_skill_references.sh
```

## Content rules

- Keep the site in English.
- Reflect real examples from the repo.
- Avoid marketing fluff that the code cannot support.
- Prefer clarity, structure, and visual polish over dense explanation.

## Good updates

- adding newly built example categories,
- refreshing featured examples,
- improving GitHub Pages presentation,
- tightening portfolio copy for hiring contexts.
