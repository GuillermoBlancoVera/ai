# AI Portfolio

This repository is my personal AI portfolio and repository index: a curated collection of machine learning, deep learning, and generative AI examples that I build, refine, and use as a public record of how I work.

The goal is twofold: to work as my carta de presentacion and to make it easy to understand what is inside the repo, where each example lives, and what each notebook is meant to demonstrate.

The portfolio currently covers:

- supervised learning notebooks for common scikit-learn models,
- classical ML scripts for structured data,
- unsupervised learning notebooks and scripts for pattern discovery,
- neural networks for vision tasks,
- generative AI examples for modern LLM workflows.

Everything in this repository is written in English and organized to be easy to navigate during technical reviews, project discussions, and portfolio walkthroughs.

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
- A mix of reusable scripts and presentation-friendly notebooks
- Interest in both traditional ML and modern generative AI
- A practical index of what exists in the repository and where to find it

## Featured Examples

### Supervised Learning Notebooks

- `Linear Regression` on Diabetes
- `Logistic Regression` on Breast Cancer
- `Decision Tree` on Wine
- `Random Forest` on Wine
- `Support Vector Machine` on Breast Cancer
- `Gradient Boosting` on Breast Cancer
- `Naive Bayes` on Iris
- `KNN` on Iris

### Classical Machine Learning

- `KNN` classification on Iris
- `Random Forest` classification on Wine
- `Linear Regression` on Diabetes
- `Random Forest Regressor` on Diabetes

### Unsupervised Learning

- `K-Means` clustering on Iris
- `Agglomerative Clustering` on Iris
- `Gaussian Mixture Models` on Iris
- `PCA` for dimensionality reduction and explained variance
- `t-SNE` for digit visualization
- `DBSCAN` on synthetic moon-shaped data
- `Isolation Forest` for anomaly detection

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
- Notebooks are used for visual exploration, compact explanations, and presentation-friendly walkthroughs.

This keeps the repository maintainable while still making it easy to demonstrate ideas interactively.

## Development Sync Rule

When new examples, notebooks, folders, or portfolio-facing content change, the repo index and Codex skill references should be updated in the same development pass.

Before committing, run:

```bash
./scripts/check_portfolio_sync.sh
```

The pre-commit hook also runs this check so commits do not silently drift away from the current repository structure.

## Notebook Index

### `notebooks/supervised_models/`

- `linear_regression_diabetes.ipynb`
- `logistic_regression_breast_cancer.ipynb`
- `decision_tree_wine.ipynb`
- `random_forest_wine.ipynb`
- `support_vector_machine_breast_cancer.ipynb`
- `gradient_boosting_breast_cancer.ipynb`
- `naive_bayes_iris.ipynb`
- `kNN.ipynb`

### `notebooks/unsupervised_ml/`

- `kmeans_iris.ipynb`
- `agglomerative_clustering_iris.ipynb`
- `dbscan_moons.ipynb`
- `gaussian_mixture_iris.ipynb`
- `pca_iris_visualization.ipynb`
- `tsne_digits_visualization.ipynb`
- `isolation_forest_anomaly_detection.ipynb`

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
