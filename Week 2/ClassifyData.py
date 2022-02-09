import matplotlib.pyplot as plt
# Reduce data dimensions
from sklearn.decomposition import PCA
# Load the iris flower dataset
from sklearn.datasets import load_iris
# uses k nearest neighbors to classify
from sklearn.neighbors import KNeighborsClassifier
import pandas


def ClassifyData():
    # Load iris data using sklearn
    data = load_iris()
    inputs = data.data
    targets = data.target

    # Loads iris data using pandas

    # Change dataset into two dimensions using PCA
    pca = PCA(n_components=2)
    compressed = pca.fit_transform(inputs)

    # Trains the classifier using 10 closest neighbors
    classifier = KNeighborsClassifier(n_neighbors=10)
    # Fit input to targets
    classifier.fit(inputs, targets)
    # Tries to predict for all 150 flowers
    classifiedData = classifier.predict(inputs)

    # plots the results in a 2D scatter graph
    plt.figure()
    plt.scatter(compressed[:, 0], compressed[:, 1], c=classifiedData)
    plt.title("PCA Projection")
    plt.savefig("iris_pca_classified.png", bbox_inches="tight")
    plt.show()
