---
name: ai-portfolio-example-authoring
description: Use when adding or revising AI examples in this repository, especially new machine learning, deep learning, or generative AI scripts and their companion notebook/docs entries.
---

# AI Portfolio Example Authoring

Use this skill when creating a new example that should feel portfolio-ready instead of purely experimental.

## Goals

- Show breadth without clutter.
- Prefer small, inspectable examples over oversized pipelines.
- Make examples readable in a GitHub interview walkthrough.
- Include lightweight evaluation or output that proves the example does something real.

## Default pattern

1. Add the runnable implementation under `src/ai_portfolio/<category>/`.
2. Use a descriptive filename based on the model or task.
3. Print concise metrics, outputs, or saved artifact paths.
4. Update `README.md` if the example is portfolio-worthy.
5. Update the notebook README in the matching `notebooks/<category>/` folder if the example should later have a notebook version.
6. If the repo structure changed, run:

```bash
./scripts/update_skill_references.sh
```

## Style rules

- Keep code straightforward and interview-friendly.
- Avoid unnecessary abstractions.
- Use built-in or small datasets when possible for classical ML examples.
- For generative AI, prefer examples that demonstrate a workflow, not only a prompt.

## Example categories

- `classical_ml`: KNN, regression, tree models, ensembles
- `unsupervised_ml`: clustering, dimensionality reduction, anomaly detection
- `deep_learning`: MLPs, CNNs, training loops, evaluation
- `generative_ai`: text generation, summarization, retrieval, agents, evaluation

## Before finishing

Read [references/example-checklist.md](references/example-checklist.md) and make sure the example still fits the portfolio voice.
