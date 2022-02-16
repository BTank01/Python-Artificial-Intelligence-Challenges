from sklearn.datasets import load_iris
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import mean_absolute_error

def classifyIrisData():
    # Load Dataset
    data = load_iris()
    inputs = data.data
    targets = data.target

    # Create Neural Network for classifying
    classifier = MLPClassifier()
    # Train Model
    classifier.fit(inputs, targets)
    # Make predictions
    outputs = classifier.predict(inputs)
    # Find the error rate
    errorVal = mean_absolute_error(targets, outputs)
    print(f"Error Rate: {errorVal}")