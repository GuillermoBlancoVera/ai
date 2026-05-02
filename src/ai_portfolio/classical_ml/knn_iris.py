"""KNN classification on the Iris dataset."""

from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler


def main() -> None:
    dataset = load_iris()
    x_train, x_test, y_train, y_test = train_test_split(
        dataset.data,
        dataset.target,
        test_size=0.2,
        random_state=42,
        stratify=dataset.target,
    )

    model = make_pipeline(
        StandardScaler(),
        KNeighborsClassifier(n_neighbors=5),
    )
    model.fit(x_train, y_train)
    predictions = model.predict(x_test)

    print("KNN classification on Iris")
    print(f"Accuracy: {accuracy_score(y_test, predictions):.3f}")
    print()
    print(classification_report(y_test, predictions, target_names=dataset.target_names))


if __name__ == "__main__":
    main()
