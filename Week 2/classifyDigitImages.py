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
