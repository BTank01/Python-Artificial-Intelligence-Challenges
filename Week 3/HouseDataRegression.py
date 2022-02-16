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

