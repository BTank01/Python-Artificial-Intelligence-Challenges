def fib(value):
    fibValues = []
    for i in range(0, value - 1):
        if i == 0 or i == 1:
            fibValues.append(i)
        else:
            fibValues.append(fibValues[i-2]+fibValues[i-1])
        #print(fibValues)
    print("-------------------------------")
    print(fibValues)
