def swapList(newList):
    size = len(newList)

    temp = newList[0]
    newList[0] = newList[size -1]
    return newList

newList = [12, 35, 9, 56, 24]
print(swapList(newList))