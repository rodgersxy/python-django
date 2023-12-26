# Divide and Conquer: it is  a technique where a problem is divided into smaller sub-problems, which are then solved independently.

def divideAndConquer_Max(arr, ind, length):
    maximum = -1
    if (ind >= length - 2):
        if (arr[ind] > arr[ind + 1]):
            return arr[ind]
        else:
            return arr[ind + 1]
    maximum = divideAndConquer_Max(arr, ind + 1, length)
    if (arr[ind] > maximum):
        return arr[ind]
    else:
        return maximum
print(divideAndConquer_Max([1, 2, 3, 4, 5], 0, 5))

def divideAndConquer_Min(arr, ind, length):
    minimum = 0
    if (ind >= length - 2):
        if (arr[ind] < arr[ind + 1]):
            return arr[ind]
        else:
            return arr[ind + 1]
    minimum = divideAndConquer_Min(arr, ind + 1, length)
    if (arr[ind] < minimum):
        return arr[ind]
    else:
        return minimum
    
print(divideAndConquer_Min([1, 2, 3, 4, 5], 0, 5))