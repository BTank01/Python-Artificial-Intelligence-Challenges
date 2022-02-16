from sklearn.datasets import fetch_california_housing
from sklearn.neural_network import MLPRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt

def houseRegression():
    # Loads the data
    data = fetch_california_housing()
    inputs = data["data"]
    targets = data["target"]

    # Show data on graph
    """plt.figure()
    plt.scatter(inputs[:, 0], inputs[:, 1], c=targets, cmap="viridis")
    plt.colorbar()
    plt.show()"""

    # Normalise Data
    scaler = MinMaxScaler()
    modelData = scaler.fit(inputs)
    scaledData = modelData.transform(inputs)

    i = 0
    errorRates = []
    while i < 100:
        # Train the Regressor Model
        # Create Neural Network for classifying
        regressor = MLPRegressor()
        # Train Model
        regressor.fit(inputs, targets)
        # Make predictions
        outputs = regressor.predict(inputs)
        # Find the error rate
        errorVal = mean_absolute_error(targets, outputs)
        print(f"Error Rate: {errorVal}")
        errorRates.append(errorVal)
        i += 1

    print(f"The smallest error rate was {min(errorRates)} and the largest error was {max(errorRates)}")
