"""Random forest classification on the Wine dataset."""

from sklearn.datasets import load_wine
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split


def main() -> None:
    dataset = load_wine()
    x_train, x_test, y_train, y_test = train_test_split(
        dataset.data,
        dataset.target,
        test_size=0.25,
        random_state=42,
        stratify=dataset.target,
    )

    model = RandomForestClassifier(
        n_estimators=300,
        max_depth=None,
        random_state=42,
    )
    model.fit(x_train, y_train)
    predictions = model.predict(x_test)

    print("Random Forest classification on Wine")
    print(f"Accuracy: {accuracy_score(y_test, predictions):.3f}")
    print()
    print(classification_report(y_test, predictions, target_names=dataset.target_names))


if __name__ == "__main__":
    main()
