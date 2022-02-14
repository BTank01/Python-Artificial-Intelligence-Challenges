# Week 2 python tasks.
from ClassifyData import *
from ClassifyDataWithPandas import *
from classifyDigitImages import *

if __name__ == '__main__':
    message = """
    |=======================================|
    |   Select an Option:                   |
    |   1: Iris Dataset using Sklearn       |
    |   2: Iris Dataset using Pandas        |
    |   3: Handwritten Digits Dataset       |
    |=======================================|
    """

    while True:
        clearConsole = lambda: print('\n' * 150)
        clearConsole()
        useSelect = int(input(message))
        if useSelect == 1:
            # Uses KNN to classify flowers
            ClassifyData()
        elif useSelect == 2:
            # Process data using pandas
            PandasClassify()
        elif useSelect == 3:
            # Uses KNN to classify handwritten numbers
            classifyDigitImages()
