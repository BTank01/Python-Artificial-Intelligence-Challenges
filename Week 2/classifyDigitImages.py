import matplotlib.pyplot as plt
# Reduce data dimensions
from sklearn.decomposition import PCA
# Load the iris flower dataset
from sklearn.datasets import load_digits
# uses k nearest neighbors to classify
from sklearn.neighbors import KNeighborsClassifier

def classifyDigitImages():
    # Loads the data
    digits = load_digits()

    # Extract the 3 different parts of the data
    data = digits.data
    images = digits.images
    target = digits.target

    # shows an image and the value it represents. ingVal < 1797
    """
    imgVal = 1070
    plt.figure()
    plt.imshow(images[imgVal])
    plt.title(target[imgVal])
    plt.show()
    """

    # Classify Data
    # Change dataset into two dimensions using PCA
    pca = PCA(n_components=2)
    compressed = pca.fit_transform(data)

    # Trains the classifier using 10 closest neighbors
    classifier = KNeighborsClassifier(n_neighbors=10)
    # Fit input to targets
    classifier.fit(data, target)
    # Tries to predict for all images
    classifiedData = classifier.predict(data)

    # plots the results in a 2D scatter graph
    plt.figure()
    plt.scatter(compressed[:, 0], compressed[:, 1], c=classifiedData)
    plt.title("PCA Projection")
    plt.savefig("digits_pca_pre-accuracy_classified.png", bbox_inches="tight")
    plt.show()


    #