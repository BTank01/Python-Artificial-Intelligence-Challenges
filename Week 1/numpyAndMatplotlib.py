import numpy as n
import matplotlib.pyplot as p

def sineGraph():
    piConst = n.pi
    sineValues = n.linspace((piConst*-1), piConst, num=100)
    print(n.sin(sineValues))

    #Sine Graph as a line
    p.plot(sineValues, n.sin(sineValues))
    p.show()

    #Sine graph as points
    p.scatter(sineValues, n.sin(sineValues))
    p.show()

def dists():
    #Gets 100 values for these two distributions
    randNormal = n.random.randn(100)
    randUniform = n.random.rand(100)

    #Plot these as a boxplot
    p.boxplot(randUniform)
    p.show()

    p.boxplot(randNormal)
    p.show()
