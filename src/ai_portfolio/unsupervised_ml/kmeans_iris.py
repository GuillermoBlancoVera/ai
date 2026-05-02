"""K-Means clustering on the Iris dataset."""

from sklearn.cluster import KMeans
from sklearn.datasets import load_iris
from sklearn.metrics import adjusted_rand_score, silhouette_score
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler


def main() -> None:
    dataset = load_iris()
    model = make_pipeline(
        StandardScaler(),
        KMeans(n_clusters=3, n_init=10, random_state=42),
    )

    clusters = model.fit_predict(dataset.data)

    print("K-Means clustering on Iris")
    print(f"Silhouette score: {silhouette_score(dataset.data, clusters):.3f}")
    print(f"Adjusted Rand index: {adjusted_rand_score(dataset.target, clusters):.3f}")


if __name__ == "__main__":
    main()
