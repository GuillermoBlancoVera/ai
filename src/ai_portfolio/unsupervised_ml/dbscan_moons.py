"""DBSCAN clustering on a synthetic two-moons dataset."""

from sklearn.cluster import DBSCAN
from sklearn.datasets import make_moons
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import StandardScaler


def main() -> None:
    features, _ = make_moons(n_samples=400, noise=0.08, random_state=42)
    scaled_features = StandardScaler().fit_transform(features)

    model = DBSCAN(eps=0.28, min_samples=6)
    labels = model.fit_predict(scaled_features)

    unique_clusters = len({label for label in labels if label != -1})
    noise_points = sum(label == -1 for label in labels)

    print("DBSCAN on synthetic moon data")
    print(f"Clusters found: {unique_clusters}")
    print(f"Noise points: {noise_points}")
    if unique_clusters > 1:
        mask = labels != -1
        print(f"Silhouette score: {silhouette_score(scaled_features[mask], labels[mask]):.3f}")


if __name__ == "__main__":
    main()
