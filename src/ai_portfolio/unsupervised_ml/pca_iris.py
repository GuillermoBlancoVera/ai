"""PCA dimensionality reduction on the Iris dataset."""

from sklearn.datasets import load_iris
from sklearn.decomposition import PCA
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler


def main() -> None:
    dataset = load_iris()
    model = make_pipeline(
        StandardScaler(),
        PCA(n_components=2),
    )

    transformed = model.fit_transform(dataset.data)
    pca = model.named_steps["pca"]

    print("PCA on Iris")
    print(f"Output shape: {transformed.shape}")
    print(f"Explained variance ratio: {pca.explained_variance_ratio_}")
    print(f"Total explained variance: {pca.explained_variance_ratio_.sum():.3f}")


if __name__ == "__main__":
    main()
