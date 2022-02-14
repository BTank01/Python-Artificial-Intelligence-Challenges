import matplotlib.pyplot as plt
# Reduce data dimensions
from sklearn.decomposition import PCA
# Load the iris flower dataset
from sklearn.datasets import load_iris
# uses k nearest neighbors to classify
from sklearn.neighbors import KNeighborsClassifier
import pandas
import numpy as np

def PandasClassify():
    # Loads and displays the csv file
    data = pandas.read_csv("IRIS.csv")
    print(data)

    # Extract inputs
    inputs = data.values[:, :-1].astype(float)

    # Extract targets, convert to numerical values. Helps when colouring results
    classes = ["Iris-setosa", "Iris-versicolor", "Iris-virginica"]
    targets = [classes.index(cl) for cl in data.values[:, -1].astype(str)]
    targets = np.array(targets)

    ########## Same as Before ##########
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
    plt.title("PCA Projection PANDAS")
    plt.savefig("iris_pca_classified_Pandas.png", bbox_inches="tight")
    plt.show()



