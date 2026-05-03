# AI Portfolio

This repository is my personal AI portfolio: a curated collection of machine learning, deep learning, and generative AI examples that I build, refine, and use as a public record of how I work.

The goal is not to present toy notebooks in isolation, but to show a practical range:

- classical ML for structured data,
- unsupervised learning for pattern discovery,
- neural networks for vision tasks,
- generative AI examples for modern LLM workflows.

Everything in this repository is written in English and organized to be easy to review during interviews, technical discussions, and portfolio walkthroughs.

## Portfolio Site

This repository also includes a lightweight static site in `docs/` for GitHub Pages.

Once Pages is enabled for the `main` branch and the `/docs` folder, the portfolio can be shared at:

```text
https://guillermoblancovera.github.io/ai/
```

## What This Repository Shows

- Breadth across different AI paradigms
- Clean, runnable Python examples
- Clear problem framing and evaluation
- A mix of reusable scripts and notebook-ready structure
- Interest in both traditional ML and modern generative AI

## Featured Examples

### Classical Machine Learning

- `KNN` classification on Iris
- `Random Forest` classification on Wine
- `Linear Regression` on Diabetes
- `Random Forest Regressor` on Diabetes

### Unsupervised Learning

- `K-Means` clustering on Iris
- `PCA` for dimensionality reduction and explained variance
- `DBSCAN` on synthetic moon-shaped data

### Deep Learning

- `MLP` for MNIST digit classification
- `CNN` for FashionMNIST image classification

### Generative AI

- `Text generation` with Hugging Face Transformers
- `Summarization` with sequence-to-sequence models
- `Simple RAG pipeline` with TF-IDF retrieval plus local text generation

## Repository Structure

```text
.
├── data/
│   ├── raw/
│   └── processed/
├── models/
├── notebooks/
│   ├── classical_ml/
│   ├── deep_learning/
│   ├── generative_ai/
│   ├── supervised_models/
│   └── unsupervised_ml/
├── reports/
│   └── figures/
├── src/
│   └── ai_portfolio/
│       ├── classical_ml/
│       ├── deep_learning/
│       ├── generative_ai/
│       └── unsupervised_ml/
├── tests/
├── pyproject.toml
└── requirements.txt
```

## How I Use Scripts vs Notebooks

- Scripts are the main source of truth for clean, reviewable implementations.
- Notebooks are reserved for visual exploration, presentation, and interview walkthroughs.

This keeps the repository maintainable while still making it easy to demonstrate ideas interactively.

## Quick Start

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m pip install -e .
```

Run a few examples:

```bash
python -m ai_portfolio.classical_ml.knn_iris
python -m ai_portfolio.classical_ml.random_forest_wine
python -m ai_portfolio.unsupervised_ml.kmeans_iris
python -m ai_portfolio.deep_learning.mnist_mlp
python -m ai_portfolio.generative_ai.text_generation_hf
```

## Portfolio Notes

- Classical ML examples use small built-in datasets so they are easy to run and review.
- Deep learning and generative AI examples may download pretrained datasets or models the first time they run.
- The repository is designed to grow over time as I add stronger end-to-end projects, evaluation experiments, and applied generative AI work.

## Next Additions

- More end-to-end projects with real datasets
- Model comparison reports and charts
- Better experiment tracking
- Retrieval, agents, and evaluation-focused generative AI examples
