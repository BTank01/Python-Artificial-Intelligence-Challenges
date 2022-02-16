from sklearn.datasets import fetch_california_housing
from sklearn.neural_network import MLPRegressor
from sklearn.metrics import mean_absolute_error
import matplotlib.pyplot as plt

def houseRegression():
    # Loads the data
    data = fetch_california_housing()
    inputs = data["data"]
    targets = data["target"]

    # Show sata on graph
    """plt.figure()
    plt.scatter(inputs[:, 0], inputs[:, 1], c=targets, cmap="viridis")
    plt.colorbar()
    plt.show()"""


