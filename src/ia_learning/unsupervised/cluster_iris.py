"""Cluster the Iris dataset without using labels during training."""

from sklearn.cluster import KMeans
from sklearn.datasets import load_iris
from sklearn.metrics import adjusted_rand_score, silhouette_score
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler


def main() -> None:
    iris = load_iris()

    model = make_pipeline(
        StandardScaler(),
        KMeans(n_clusters=3, n_init="auto", random_state=42),
    )

    clusters = model.fit_predict(iris.data)

    print("Unsupervised learning: Iris clustering")
    print(f"Silhouette score: {silhouette_score(iris.data, clusters):.3f}")
    print(f"Adjusted Rand index against true labels: {adjusted_rand_score(iris.target, clusters):.3f}")
    print()
    print("The model did not see the labels. The adjusted Rand index is only for learning feedback.")


if __name__ == "__main__":
    main()
