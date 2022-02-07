def bubbleSort(listValues):
    for j in range(1, len(listValues)*len(listValues)):
        for i in range(0, len(listValues) - 1):
            if listValues[i] > listValues[i + 1]:
                tempValue = listValues[i + 1]
                listValues[i + 1] = listValues[i]
                listValues[i] = tempValue
            elif listValues[i] < listValues[i + 1]:
                pass
            #print(listValues)
    print(listValues)
