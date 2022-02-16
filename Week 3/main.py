from ClassifyIrisData import classifyIrisData
from HouseDataRegression import  houseRegression

msg = """
|===========================================================|
|                           Options                         |
|   1: Classify Iris dataset.                               |
|   2: Regression with californian house prices dataset.    |
|                                                           |
|===========================================================|
"""
if __name__ == '__main__':
    houseRegression()

"""
    print(msg)
    useSelect = int(input("Enter an Option: "))
    if useSelect == 1:
        classifyIrisData()
    elif useSelect == 2:
        houseRegression()
"""

