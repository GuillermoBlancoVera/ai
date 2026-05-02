"""Linear regression on the Diabetes dataset."""

from sklearn.datasets import load_diabetes
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split


def main() -> None:
    dataset = load_diabetes()
    x_train, x_test, y_train, y_test = train_test_split(
        dataset.data,
        dataset.target,
        test_size=0.2,
        random_state=42,
    )

    model = LinearRegression()
    model.fit(x_train, y_train)
    predictions = model.predict(x_test)

    rmse = mean_squared_error(y_test, predictions, squared=False)

    print("Linear Regression on Diabetes")
    print(f"MAE: {mean_absolute_error(y_test, predictions):.3f}")
    print(f"RMSE: {rmse:.3f}")
    print(f"R2: {r2_score(y_test, predictions):.3f}")


if __name__ == "__main__":
    main()
