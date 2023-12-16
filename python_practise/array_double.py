# given an array of integers, return a new array with each value doubled

def maps(a):
    for i in range(len(a)):
        a[i] *= 2
    return a


# def maps(a):
#     return [n * 2 for n in a]