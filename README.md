# IA Learning Lab

A hands-on repository for learning how to train AI models, starting with classic machine learning and growing into deep learning.

The goal is to build intuition by training small models, measuring them, changing one thing at a time, and keeping notes about what happened.

## Learning Tracks

### 1. Supervised Learning

Use labeled examples to predict a known target.

Start with:

- Regression: predict a number.
- Classification: predict a category.
- Evaluation: split data, measure error, inspect mistakes.

Starter script:

```bash
python -m ia_learning.supervised.train_iris_classifier
```

### 2. Unsupervised Learning

Find structure in data without labels.

Start with:

- Clustering: group similar examples.
- Dimensionality reduction: compress features for visualization.
- Evaluation: inspect patterns and compare cluster behavior.

Starter script:

```bash
python -m ia_learning.unsupervised.cluster_iris
```

### 3. Deep Learning

Train neural networks with tensors, gradients, and optimization loops.

Start with:

- Tensors and automatic differentiation.
- A small neural network.
- Training loops, validation, and overfitting.

Starter script:

```bash
python -m ia_learning.deep_learning.train_mnist_mlp
```

## Repository Structure

```text
.
├── data/
│   ├── raw/              # Original datasets, not edited by hand
│   └── processed/        # Cleaned or transformed datasets
├── models/               # Saved model artifacts
├── notebooks/            # Experiments and study notes
├── reports/
│   └── figures/          # Charts and exported visuals
├── src/
│   └── ia_learning/      # Reusable training code
├── tests/                # Small checks for helper code
├── requirements.txt      # Beginner-friendly dependencies
└── pyproject.toml        # Project metadata and tooling
```

## Setup

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

## Suggested Study Flow

1. Run one starter script exactly as provided.
2. Read the printed metrics and comments.
3. Change one parameter, such as model type, number of clusters, or learning rate.
4. Run it again and record what changed.
5. Move repeated logic from notebooks into `src/ia_learning`.

## Good Habits

- Keep raw data unchanged in `data/raw`.
- Save generated datasets in `data/processed`.
- Save trained models in `models`.
- Track metrics before trusting a model.
- Prefer small experiments over large mysterious training runs.

## Next Milestones

- Add a first supervised regression exercise.
- Add notebooks for each learning track.
- Add plotting helpers for confusion matrices and clusters.
- Add model saving and loading examples.
- Add a notes file for experiment logs.
