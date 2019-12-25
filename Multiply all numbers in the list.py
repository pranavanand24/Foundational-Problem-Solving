def multiplyList(myList) :

    result = 1

    for x in myList:
        result = result * x
    return result

list1 = [1, 2, 3]
print(multiplyList(list1))